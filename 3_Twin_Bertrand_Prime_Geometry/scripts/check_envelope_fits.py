#!/usr/bin/env python3
"""Check the twin-gap exponent and the GBP envelope. Both fail as stated.

    python check_envelope_fits.py [limit]     # default 100,000,000

Two claims, from RESULTS.md and results/uniform_envelope_fits.md:

  (A) envelope     G < 0.1709 (log P)^3.2210        pooled over twins,
                                                    cousins, sexy; R^2 = 0.982
  (B) typical gap  G_k ~ 0.70 (log T_k)^1.866       "below the HL beta = 2"

FINDINGS at 1e8 (440,312 twin pairs), all reproducible below.

(A) THE ENVELOPE IS VIOLATED — 204 times for T > 1000, worst 1.87x, at
    T = 850,349 where G = 1452 against a bound of 775. Not marginal.

    The cause is a mismatch of extremals. The fit was performed on
    sup(r_k - 1) = sup(G/T) over nested tails, but sup(G/T) is attained
    at SMALL T (its maximum over the whole range is at T = 5), while the
    stated envelope is a bound on G, whose extreme sits at LARGE T.
    Fitting one extremal statistic and stating the other does not
    transfer, and here it does not.

    The exponent is also not determined by the data. Forcing delta and
    refitting C gives a plausible envelope for anything from 2.5 to 4.0;
    only delta = 4.0 is violation-free at 1e8. Meanwhile R^2 stays above
    0.98 for every subset of tails tried while C moves by 63% — the high
    R^2 comes from fitting two parameters to five NESTED (hence strongly
    dependent) points, not from the model being right.

(B) THE TYPICAL-GAP EXPONENT IS ~2, NOT 1.866. Measured over four
    decades: mean G ~ 0.792 (log T)^1.978, against the Hardy-Littlewood
    prediction (log T)^2 / C_2 = 0.757 (log T)^2. The claimed 1.866 is
    not reproduced, so "below the HL beta = 2" is not supported — the
    shortfall looks like the usual under-estimate from a log-log fit
    over a short range.

Standard library only. ~3 min at 1e8.
"""
import sys
import math


def twins(N):
    b = bytearray([1]) * (N + 1)
    b[0] = b[1] = 0
    i = 2
    while i * i <= N:
        if b[i]:
            b[i*i::i] = bytearray(len(b[i*i::i]))
        i += 1
    return [p for p in range(3, N - 1) if b[p] and b[p + 2]]


def loglog_fit(xs, ys):
    """Fit y = C x^d in log-log. Returns (d, C, R^2)."""
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(lx); mx = sum(lx)/n; my = sum(ly)/n
    d = sum((a-mx)*(b-my) for a, b in zip(lx, ly)) / sum((a-mx)**2 for a in lx)
    C = math.exp(my - d*mx)
    ss = sum((b-my)**2 for b in ly)
    rs = sum((b-(my + d*(a-mx)))**2 for a, b in zip(lx, ly))
    return d, C, 1 - rs/ss


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000_000
    print(f"Sieving to {N:,} ...", end=" ", flush=True)
    T = twins(N)
    G = [(T[i+1] - T[i], T[i]) for i in range(len(T) - 1)]
    print(f"{len(T):,} twin pairs\n")

    C0, D0 = 0.1709, 3.2210

    print("=" * 72)
    print("  (A) THE ENVELOPE  G < 0.1709 (log P)^3.2210")
    print("=" * 72)
    bad = sorted(((g / (C0*math.log(t)**D0), t, g) for g, t in G if t > 1000),
                 reverse=True)
    nv = sum(1 for r, _, _ in bad if r >= 1)
    print(f"   violations (T > 1000): {nv:,} of {len(bad):,}  ({100*nv/len(bad):.2f}%)")
    print(f"   {'T':>12} {'G':>7} {'bound':>9} {'G/bound':>9}")
    for r, t, g in bad[:5]:
        print(f"   {t:>12,} {g:>7} {C0*math.log(t)**D0:>9.1f} {r:>9.3f}  VIOLATES")

    print("\n   WHY: the fit used sup(r-1) = sup(G/T); the claim is about sup(G).")
    mg, at = max(G)
    mr, atr = max(((g/t, t) for g, t in G))
    print(f"     max G     = {mg:,} at T = {at:,}        (large T)")
    print(f"     max G/T   = {mr:.3e} at T = {atr}            (small T)")
    print("     Different extremals. Fitting one does not bound the other.")

    print("\n   IS THE EXPONENT DETERMINED? force delta, refit C, count violations")
    print(f"   {'delta':>7} {'C':>9} {'violations':>12} {'worst':>8}")
    tails = []
    for e in range(2, 8):
        s = at2 = 0
        for i, t in enumerate(T[:-1]):
            if t > 10**e:
                rr = T[i+1]/t - 1
                if rr > s: s, at2 = rr, t
        if s: tails.append((at2, s))
    for d in (2.5, 2.8, 3.0, 3.22, 3.5, 4.0):
        C = max(s*a/math.log(a)**d for a, s in tails)
        v = worst = 0
        for g, t in G:
            if t <= 1000: continue
            rr = g / (C*math.log(t)**d)
            if rr >= 1: v += 1
            worst = max(worst, rr)
        print(f"   {d:>7.2f} {C:>9.4f} {v:>12,} {worst:>8.3f}")
    print("   -> anything from 2.5 to 4.0 is arguable; 3.22 is not pinned by the data.")

    print("\n" + "=" * 72)
    print("  (B) THE TYPICAL GAP  G_k ~ 0.70 (log T_k)^1.866")
    print("=" * 72)
    xs, ys = [], []
    print(f"   {'range':>22} {'mean G':>9} {'claimed':>9} {'ratio':>7}")
    for lo in range(4, int(math.log10(N))):
        sel = [(g, t) for g, t in G if 10**lo <= t < 10**(lo+1)]
        if len(sel) < 50: continue
        m = sum(g for g, _ in sel)/len(sel)
        md = sorted(t for _, t in sel)[len(sel)//2]
        xs.append(math.log(md)); ys.append(m)
        pred = 0.70*math.log(md)**1.866
        print(f"   [1e{lo:02d}, 1e{lo+1:02d})".rjust(22)
              + f" {m:>9.2f} {pred:>9.2f} {m/pred:>7.3f}")
    d, C, r2 = loglog_fit(xs, ys)
    print(f"\n   fitted   : mean G ~ {C:.3f} (log T)^{d:.3f}   (R^2 = {r2:.4f})")
    print(f"   claimed  : mean G ~ 0.700 (log T)^1.866")
    print(f"   Hardy-Littlewood : (log T)^2 / C_2 = {1/1.32032:.3f} (log T)^2")
    print("   -> the measured exponent is ~2, the HL value. 'Below beta = 2' is")
    print("      not supported here; 1.866 looks like a short-range fit artifact.")


if __name__ == "__main__":
    main()
