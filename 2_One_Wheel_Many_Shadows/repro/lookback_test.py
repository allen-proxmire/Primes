#!/usr/bin/env python3
"""Regenerate the "Looking back" section of `The_Ninety_Percent_Rule.md`.

    python lookback_test.py

The question: before walking forward from a prime, look back at the last few
gaps. Does that history tell you anything the four wheels do not?

Part 1 -- the zig-zag. Guess that the next gap moves opposite to the last one
(the angle "wobble" reversing). Score it on the real gaps, and on the SAME
gaps shuffled into random order. Any sequence of independent values reverses
about two-thirds of the time, so the shuffle is the baseline to beat.

Part 2 -- does history change the slot count? Split the starting primes by
the direction and by the size of the last gap, and re-measure the walk.

Part 3 -- is the sliver the wheel? The size of the last gap does carry a
little signal. To see where it comes from, build fake "primes" that contain
ONLY wheel structure: strike the multiples of every prime up to y, then keep
survivors at random, matched to the real prime count. Repeat for deeper y.
The walker always carries the same four wheels; only the fake changes.

The pool ratio (survivors / real primes) is reported for every fake. As it
approaches 1 the fake stops containing any randomness and simply IS the
primes, so agreement there is automatic and carries no evidence -- see
Null_Model_Discipline.md. Read the rows with a real pool ratio.

Part 4 -- the non-circular version of part 3. Keep the REAL walks, and group
them by exactly which of the next 12 open slots the wheels up to y strike.
Compare big-last-gap against small-last-gap inside each group. Whatever
difference survives the grouping is not carried by those wheels. No fakes,
no chosen coin density, and a spread column shows the grouping has not
simply rebuilt the primes. Run on [10^6, 2*10^6] and on [10^7, 2*10^7].

Windows: parts 1-3 use every prime in [10^6, 2*10^6]. Requires numpy.
Runtime a few minutes, most of it part 4 on the larger window.
"""
import numpy as np

LO, TOP = 10**6, 2 * 10**6
HI = TOP + 20000
N = HI + 1
SEEDS = 12
DEPTHS = [7, 11, 13, 31, 100, 300, 700, 1000]
x = np.arange(N)


def is_small_prime(p):
    return p > 1 and all(p % q for q in range(2, int(p**0.5) + 1))


def sieve_upto(y):
    """Survivors of striking multiples of every prime <= y (primes themselves kept)."""
    alive = np.ones(N, bool)
    alive[:2] = False
    for p in range(2, y + 1):
        if is_small_prime(p):
            alive[p * p::p] = False
    return alive


real = sieve_upto(int(HI**0.5) + 1)
open4 = (x % 2 != 0) & (x % 3 != 0) & (x % 5 != 0) & (x % 7 != 0)
slot_count = np.cumsum(open4)          # the four-wheel walker's slot counter


def walk(isp):
    """For each starting prime in the window: last gap, the one before, next gap, slots walked."""
    P = np.nonzero(isp)[0]
    P = P[P > 11]
    i = np.arange(2, len(P) - 1)
    i = i[(P[i] >= LO) & (P[i] <= TOP)]
    g_before = P[i - 1] - P[i - 2]
    g_last = P[i] - P[i - 1]
    g_next = P[i + 1] - P[i]
    k = slot_count[P[i + 1]] - slot_count[P[i]]
    return g_before, g_last, g_next, k


def sliver(isp):
    """Extra slots needed after a SMALL last gap versus after a BIG one."""
    _, g_last, _, k = walk(isp)
    med = np.median(g_last)
    return k[g_last < med].mean() - k[g_last > med].mean()


def ninety(k):
    return next(j for j in range(1, 200) if (k <= j).mean() >= 0.90)


def main():
    gb, gl, gn, k = walk(real)
    med = np.median(gl)
    print(f"starting primes in [1e6, 2e6]: {len(k):,}\n")

    # ---- part 1 --------------------------------------------------------
    m = (gl != gb) & (gn != gl)
    zig = ((gn - gl) * (gl - gb) < 0)[m].mean()
    c = gl != med
    toward = np.where(gl > med, gn < gl, gn > gl)[c].mean()
    rng = np.random.default_rng(1)
    s = rng.permutation(gn)
    a, b, cc = s[:-2], s[1:-1], s[2:]
    ms = (b != a) & (cc != b)
    zig_shuf = ((cc - b) * (b - a) < 0)[ms].mean()
    print("PART 1 -- the zig-zag guess")
    print(f"  'next move reverses the last'           real gaps : {100*zig:.1f}%")
    print(f"  same guess, gaps shuffled (no structure)          : {100*zig_shuf:.1f}%")
    print(f"  'next gap moves back toward typical' (no history)  : {100*toward:.1f}%\n")

    # ---- part 2 --------------------------------------------------------
    print("PART 2 -- does the history change the walk?")
    print(f"  {'what you know':<26} {'n':>7} {'mean slots':>11} {'caught by 7':>12} {'90% at':>7}")
    for name, sel in [("nothing", np.ones_like(k, bool)),
                      ("last move UP", gl > gb),
                      ("last move DOWN", gl < gb),
                      ("last gap BIG", gl > med),
                      ("last gap SMALL", gl < med)]:
        kk = k[sel]
        print(f"  {name:<26} {len(kk):>7,} {kk.mean():>11.2f} {100*(kk<=7).mean():>11.1f}% {ninety(kk):>7}")
    print()

    # ---- part 3 --------------------------------------------------------
    d_real = sliver(real)
    target = real[LO:TOP + 1].sum()
    print("PART 3 -- is the sliver the wheel?")
    print(f"  {'model':<26} {'sliver':>8} {'s.e.':>7} {'share of real':>14} {'pool ratio':>11}")
    print(f"  {'REAL PRIMES':<26} {d_real:>+8.3f} {'':>7} {'100%':>14} {'--':>11}")
    rng = np.random.default_rng(2026)
    for y in DEPTHS:
        base = sieve_upto(y)
        base[:y + 1] = False
        pool = base[LO:TOP + 1].sum()
        rate = target / pool
        ds = [sliver(base & (rng.random(N) < rate)) for _ in range(SEEDS)]
        mu, se = np.mean(ds), np.std(ds, ddof=1) / np.sqrt(SEEDS)
        print(f"  {'fake, wheels to ' + str(y):<26} {mu:>+8.3f} {se:>7.3f} "
              f"{100*mu/d_real:>13.0f}% {pool/target:>11.2f}")


def part4(lo, top, depths=(7, 11, 13, 31, 100, 300), ahead=12, boot=300):
    """Group REAL walks by where the wheels up to y strike the road ahead.

    For each starting prime, record which of the next `ahead` open slots (of
    the four-wheel walker) survive every wheel up to y. Primes with the same
    pattern face the same wheel-struck road. Inside each group, compare the
    real slot count after a small last gap with that after a big one, and
    average the differences (weighted by group size). What is left is the
    part of the sliver NOT carried by the wheels up to y.

    Nothing is simulated and no coin density is chosen: every outcome is a
    real walk. The circularity check is the last column -- how much the real
    walks still vary inside a group. If the grouping had simply rebuilt the
    primes, that spread would collapse toward zero.
    """
    hi = top + 20000
    n = hi + 1
    xs = np.arange(n)

    def surv(y):
        a = np.ones(n, bool)
        a[:2] = False
        for q in range(2, y + 1):
            if is_small_prime(q):
                a[q * q::q] = False
        return a

    primes_bool = surv(int(hi**0.5) + 1)
    slots = np.nonzero((xs % 2 != 0) & (xs % 3 != 0) & (xs % 5 != 0) & (xs % 7 != 0))[0]
    P = np.nonzero(primes_bool)[0]
    P = P[P > 11]
    i = np.arange(2, len(P) - 1)
    i = i[(P[i] >= lo) & (P[i] <= top)]
    p = P[i]
    g_last = p - P[i - 1]
    k = np.searchsorted(slots, P[i + 1]) - np.searchsorted(slots, p)
    med = np.median(g_last)
    big, small = g_last > med, g_last < med
    real_sliver = k[small].mean() - k[big].mean()

    first = np.searchsorted(slots, p, side="right")
    ahead_idx = slots[first[:, None] + np.arange(ahead)[None, :]]
    bits = 1 << np.arange(ahead)

    print(f"\nPART 4 -- group the real walks by the wheel pattern ahead, primes in "
          f"[{lo:.0e}, {top:.0e}] (n = {len(k):,})")
    print(f"  real sliver {real_sliver:+.3f};  spread of slot count with no grouping {k.std():.2f}")
    print(f"  {'wheels to':>10} {'groups':>7} {'left over':>10} {'s.e.':>6} {'explained':>10} "
          f"{'primes used':>12} {'spread left':>12}")
    rng = np.random.default_rng(0)
    for y in depths:
        s = surv(y)
        key = (s[ahead_idx].astype(np.int64) * bits).sum(1)
        order = np.argsort(key, kind="stable")
        ks, kk, bb, ss = key[order], k[order], big[order], small[order]
        cuts = np.flatnonzero(np.diff(ks)) + 1
        diffs, wts, used, var_sum = [], [], 0, 0.0
        for grp in np.split(np.arange(len(ks)), cuts):
            kb, ksm = kk[grp][bb[grp]], kk[grp][ss[grp]]
            if len(kb) >= 2 and len(ksm) >= 2:
                wt = 1 / (1 / len(kb) + 1 / len(ksm))
                diffs.append(ksm.mean() - kb.mean())
                wts.append(wt)
                used += len(grp)
                var_sum += kk[grp].var() * len(grp)
        diffs, wts = np.array(diffs), np.array(wts)
        left = (diffs * wts).sum() / wts.sum()
        bs = []
        for _ in range(boot):
            j = rng.integers(0, len(diffs), len(diffs))
            bs.append((diffs[j] * wts[j]).sum() / wts[j].sum())
        print(f"  {y:>10} {len(diffs):>7} {left:>+10.3f} {np.std(bs):>6.3f} "
              f"{100 * (1 - left / real_sliver):>9.0f}% {100 * used / len(k):>11.0f}% "
              f"{np.sqrt(var_sum / used):>12.2f}")


if __name__ == "__main__":
    main()
    part4(10**6, 2 * 10**6)
    part4(10**7, 2 * 10**7)
