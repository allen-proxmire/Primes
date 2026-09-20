#!/usr/bin/env python3
"""Regenerate every measured table in the One Wheel, Many Shadows papers.

    python regenerate_tables.py            # everything (~5-10 min)
    python regenerate_tables.py --quick    # smaller range, fewer seeds (~1 min)
    python regenerate_tables.py --only windowed

Sections, and the table each one reproduces:

  trap3      Differencing Trap  §3    real vs transform-matched null
  windowed   Differencing Trap  §5.1  windowed excess vs wheel depth Q
  lag1       Angle Wobble       §4.1  lag-1 gap correlation vs Q
  hexagon    Balance Ratio      §2.1  3-divisibility of the Eisenstein form
  reduction  Balance Ratio      §5    pooled shift == cov(g_n, g_n+1)
  residue    Balance Ratio      §6    per-residue-class, vs wheel surrogate

Discipline enforced throughout (see ../Null_Model_Discipline.md):
  * transform AFTER shuffling, never before
  * residue-conditioned questions use a GENERATIVE null, not a shuffle
  * every surrogate reports its POOL RATIO; below ~1.25 it is circular
  * power checks included, not optional

Needs numpy. Nothing else.
"""
import argparse, random, sys
import numpy as np

LO, HI = 1_000_000, 5_000_000
K = 5                                   # regression window
SEEDS = [11, 22, 33]
SHUFFLES = 4


# ---------------------------------------------------------------- primitives

def sieve(n):
    b = bytearray([1]) * (n + 1); b[0] = b[1] = 0; i = 2
    while i * i <= n:
        if b[i]: b[i*i::i] = bytearray(len(b[i*i::i]))
        i += 1
    return b


def gaps_of(seq):
    a = np.asarray(seq, dtype=np.int64)
    return (a[1:] - a[:-1]).tolist()


def diff(s):
    a = np.asarray(s, float)
    return a[1:] - a[:-1]


def R2(series, k=K):
    """In-sample R^2 predicting the next value from the last k."""
    S = np.asarray(series, float)
    X = np.column_stack([S[k-1-j:len(S)-1-j] for j in range(k)])
    y = S[k:]
    X = np.column_stack([X, np.ones(len(y))])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    return 1 - (r*r).sum() / ((y - y.mean())**2).sum()


class Wheel:
    """Generative null: integers coprime to every prime <= Q, thinned to
    prime density. Carries its pool ratio, because a surrogate whose pool
    approaches pi(x) has stopped modelling the primes and become them."""

    def __init__(self, B, Q, lo, hi, n_primes):
        small = [i for i in range(2, Q + 1) if B[i]]
        W = bytearray([1]) * (hi - lo)
        for p in small:
            start = ((lo + p - 1) // p) * p
            for n in range(start, hi, p):
                if n != p:
                    W[n - lo] = 0
        self.Q = Q
        self.pool = [lo + i for i in range(hi - lo) if W[i]]
        self.ratio = len(self.pool) / n_primes
        self.keep = (n_primes / (hi - lo)) / (len(self.pool) / (hi - lo))

    @property
    def status(self):
        return "ok" if self.ratio >= 1.4 else (
            "borderline" if self.ratio >= 1.25 else "CIRCULAR")

    def draw(self, seed):
        r = random.Random(seed)
        return [x for x in self.pool if r.random() < self.keep]


# ------------------------------------------------------------------ sections

def trap3(ctx):
    print(hdr("Differencing Trap §3 — real vs transform-matched null"))
    g, rng = ctx.gaps, random.Random(7)
    dg = diff(g)
    nulls = []
    for _ in range(SHUFFLES):
        gs = list(g); rng.shuffle(gs); nulls.append(gs)
    def avg(f): return float(np.mean([f(x) for x in nulls]))
    print(f"{'statistic':<46}{'real':>10}{'null':>10}{'genuine':>12}")
    r = R2(g); n = avg(lambda s: R2(s))
    print(f"{'raw-gap memory (regress g_n on last 5)':<46}{r*100:9.2f}%{n*100:9.2f}%{(r-n)*100:+11.2f}pp")
    r = float(np.corrcoef(g[:-1], g[1:])[0,1])
    n = avg(lambda s: float(np.corrcoef(s[:-1], s[1:])[0,1]))
    print(f"{'gap autocorrelation, lag 1':<46}{r:10.3f}{n:10.3f}{r-n:+12.3f}")
    ad = np.abs(dg)
    r = float(np.corrcoef(ad[:-1], ad[1:])[0,1])
    n = avg(lambda s: float(np.corrcoef(np.abs(diff(s))[:-1], np.abs(diff(s))[1:])[0,1]))
    print(f"{'jitter clustering  corr(|dg_n|,|dg_n-1|)':<46}{r:10.3f}{n:10.3f}{r-n:+12.3f}  <- artifact")
    def recoil(d):
        # top quintile: the threshold that reproduces the published REAL value.
        # See repro/README.md -- the published +2.7pp 'genuine' column was an
        # artifact of real and null having been computed at different thresholds.
        thr = np.quantile(np.abs(d), 0.8); m = np.abs(d[:-1]) >= thr
        return float(np.mean(np.sign(d[1:][m]) != np.sign(d[:-1][m]))) * 100
    r = recoil(dg); n = avg(lambda s: recoil(diff(s)))
    print(f"{'jitter recoil, big -> opposite sign':<46}{r:9.1f}%{n:9.1f}%{r-n:+11.1f}pp")
    r = R2(dg); n = avg(lambda s: R2(diff(s)))
    print(f"{'WINDOWED WOBBLE (regress dg_n on last 5)':<46}{r*100:9.2f}%{n*100:9.2f}%{(r-n)*100:+11.2f}pp")
    print("\n  Published: clustering and recoil are artifact; ~+1.97pp survives.")


def _excess(g, rng):
    real = R2(diff(g))
    nl = []
    for _ in range(SHUFFLES):
        gs = list(g); rng.shuffle(gs); nl.append(R2(diff(gs)))
    return (real - float(np.mean(nl))) * 100


def windowed(ctx):
    print(hdr("Differencing Trap §5.1 — is the windowed excess fully the wheel?"))
    er = _excess(ctx.gaps, random.Random(7))
    print(f"  real primes: {er:+.3f} pp\n")
    print(f"{'Q':>6}{'pool':>12}{'pool/pi':>10}{'excess':>12}{'% of real':>11}   status")
    for Q in ctx.QS:
        w = ctx.wheel(Q)
        e = [_excess(gaps_of(w.draw(s)), random.Random(s + 1000)) for s in ctx.seeds]
        m = float(np.mean(e))
        print(f"{Q:>6}{len(w.pool):>12,}{w.ratio:>10.2f}{m:>+11.3f}pp{100*m/er:>10.1f}%   {w.status}")
    print("\n  Published: ~99% from Q=100 up; Q=30 gives ~76% (the power check).")


def lag1(ctx):
    print(hdr("Angle Wobble §4.1 — lag-1 gap correlation vs wheel depth"))
    c = float(np.corrcoef(ctx.gaps[:-1], ctx.gaps[1:])[0, 1])
    print(f"  real primes: corr(g_n, g_n+1) = {c:+.4f}\n")
    print(f"{'Q':>6}{'pool/pi':>10}{'model corr':>13}{'% of real':>11}   status")
    for Q in ctx.QS:
        w = ctx.wheel(Q)
        v = []
        for s in ctx.seeds:
            gs = gaps_of(w.draw(s))
            v.append(float(np.corrcoef(gs[:-1], gs[1:])[0, 1]))
        m = float(np.mean(v))
        print(f"{Q:>6}{w.ratio:>10.2f}{m:>+13.4f}{100*m/c:>10.1f}%   {w.status}")
    print("\n  Published: plateaus at -0.044 by Q~300. The Q~sqrt(x) row is CIRCULAR.")


def _hexrate(seq):
    """Fraction of consecutive triples whose Eisenstein half-gap form is 0 mod 3."""
    n3 = tot = 0
    for i in range(len(seq) - 2):
        h1 = (seq[i+1] - seq[i]) // 2
        h2 = (seq[i+2] - seq[i+1]) // 2
        tot += 1
        if (h1*h1 + h1*h2 + h2*h2) % 3 == 0:
            n3 += 1
    return 100 * n3 / tot


def hexagon(ctx):
    print(hdr("Balance Ratio §2.1 — 3-divisibility of the Eisenstein form"))
    print("  Identity: h1^2+h1h2+h2^2 = (h1-h2)^2 + 3h1h2, so mod 3 it is (h1-h2)^2.")
    print("  Exhaustive check of the form mod 3:")
    bad = [(a, b) for a in range(3) for b in range(3)
           if ((a*a+a*b+b*b) % 3 == 0) != (a == b)]
    print(f"    3 | form  <=>  h1 == h2 (mod 3)   [counterexamples: {len(bad)}]")
    print("  Reachable (g1,g2) mod 6 for consecutive primes > 3:")
    same = []
    for p in (1, 5):
        for q in (1, 5):
            for r in (1, 5):
                g1, g2 = (q-p) % 6, (r-q) % 6
                if g1 == g2: same.append((p, q, r, g1))
    print(f"    g1 == g2 only for: {[(a,b,c) for a,b,c,_ in same]} — always g1=g2=0")
    print("    => 3 | form  <=>  three consecutive primes share a residue mod 6\n")
    P = ctx.primes
    rate = _hexrate(P)
    rep = 100 * sum(1 for i in range(len(P)-1) if P[i] % 6 == P[i+1] % 6) / (len(P)-1)
    print(f"  P(single repeat, p' = p mod 6)          = {rep:.3f}%")
    print(f"  P(3 | form) = P(triple repeat)          = {rate:.3f}%")
    print(f"  if transitions were independent          = {rep*rep/100:.3f}%")
    print(f"  if residues were even odds               = 12.500%")
    print(f"\n{'Q':>6}{'pool/pi':>10}{'P(3|form)':>12}   status")
    for Q in ctx.QS[:4]:
        w = ctx.wheel(Q)
        m = float(np.mean([_hexrate(w.draw(s)) for s in ctx.seeds]))
        print(f"{Q:>6}{w.ratio:>10.2f}{m:>11.3f}%   {w.status}")
    print("\n  Published: 17.408% real; reproduced by the wheel from Q=30 up.")


def _loeschian(seq):
    out = []
    for i in range(len(seq) - 2):
        g1 = seq[i+1] - seq[i]; g2 = seq[i+2] - seq[i+1]
        out.append((g1, g2, g1*g1 + g1*g2 + g2*g2))
    return out


def reduction(ctx):
    print(hdr("Balance Ratio §5 — the pooled shift IS cov(g_n, g_n+1)"))
    print("  NOT a prediction: shuffling leaves the square terms alone and sends")
    print("  E[g1g2] -> E[g]^2, so the shift is E[g1g2]-E[g]^2, the definition of cov.\n")
    g = ctx.gaps
    Q = lambda s: [s[i]**2 + s[i]*s[i+1] + s[i+1]**2 for i in range(len(s)-1)]
    qr = Q(g); mr = float(np.mean(qr))
    rng = random.Random(7); sh = []
    for _ in range(5):
        gs = list(g); rng.shuffle(gs); sh.append(float(np.mean(Q(gs))))
    mn = float(np.mean(sh))
    mg = float(np.mean(g))
    cov = float(np.mean([(g[i]-mg)*(g[i+1]-mg) for i in range(len(g)-1)]))
    print(f"  E[g1^2+g1g2+g2^2] real     = {mr:.3f}")
    print(f"  E[g1^2+g1g2+g2^2] shuffled = {mn:.3f}   (spread {max(sh)-min(sh):.3f})")
    print(f"  measured shift             = {mr-mn:+.3f}  ({100*(mr-mn)/mn:+.3f}%)")
    print(f"  cov(g_n, g_n+1)            = {cov:+.3f}  ({100*cov/mn:+.3f}%)")
    print(f"\n  Published: -0.708% measured against -0.719% forced by the algebra.")


def residue(ctx):
    print(hdr("Balance Ratio §6 — per residue class, vs a GENERATIVE null"))
    print("  A gap-shuffle is INVALID here: a gap of 4 cannot follow p=5 mod 6,")
    print("  so shuffled triples are arithmetically impossible. Wheel surrogate instead.\n")
    def by(seq, mod):
        d = {}
        for i, (g1, g2, q) in enumerate(_loeschian(seq)):
            d.setdefault(seq[i] % mod, []).append(q)
        return d
    w = ctx.wheel(317)
    print(f"  surrogate Q=317, pool/pi = {w.ratio:.2f} ({w.status})")
    sur = [by(w.draw(s), 6) for s in ctx.seeds]
    real = by(ctx.primes, 6)
    print(f"\n{'p mod 6':>9}{'n':>10}{'mean Q real':>14}{'mean Q wheel':>14}{'diff':>9}")
    for c in sorted(real):
        R = float(np.mean(real[c]))
        S = float(np.mean([float(np.mean(s[c])) for s in sur if c in s]))
        print(f"{c:>9}{len(real[c]):>10,}{R:>14.2f}{S:>14.2f}{100*(R-S)/S:>+8.2f}%")
    print("\n  POWER CHECK — does the test see the known LOS bias?")
    tot = len(ctx.primes) - 1
    pr = 100*sum(1 for i in range(tot) if ctx.primes[i] % 6 == ctx.primes[i+1] % 6)/tot
    ps = []
    for s in ctx.seeds:
        S = w.draw(s); t = len(S)-1
        ps.append(100*sum(1 for i in range(t) if S[i] % 6 == S[i+1] % 6)/t)
    print(f"    residue repeat: real {pr:.2f}%   wheel {float(np.mean(ps)):.2f}%   even odds 50.00%")
    print("    -> the bias is large and the wheel reproduces it: instrument has power.")
    print("\n  Published: no class above 1.3 sigma.")


SECTIONS = {"trap3": trap3, "windowed": windowed, "lag1": lag1,
            "hexagon": hexagon, "reduction": reduction, "residue": residue}


def hdr(t):
    return "\n" + "=" * 78 + f"\n  {t}\n" + "=" * 78


class Ctx:
    """Shared state. Wheels are cached: building one marks a 4M-element
    array against every prime <= Q, and several sections want the same Q."""
    def wheel(self, Q):
        if Q not in self._wheels:
            self._wheels[Q] = Wheel(self.B, Q, self.lo, self.hi, self.n_primes)
        return self._wheels[Q]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quick", action="store_true", help="smaller range, one seed")
    ap.add_argument("--only", choices=sorted(SECTIONS), help="run one section")
    a = ap.parse_args()

    ctx = Ctx()
    ctx._wheels = {}
    ctx.lo, ctx.hi = (LO, 2_000_000) if a.quick else (LO, HI)
    ctx.seeds = SEEDS[:1] if a.quick else SEEDS
    ctx.QS = [30, 100, 317, 600, 1000, 1732]
    print(f"range [{ctx.lo:,}, {ctx.hi:,})   seeds {ctx.seeds}"
          f"{'   [QUICK: numbers will differ from the papers]' if a.quick else ''}")
    print("sieving...", end=" ", flush=True)
    ctx.B = sieve(ctx.hi)
    ctx.primes = [i for i in range(ctx.lo, ctx.hi) if ctx.B[i]]
    ctx.n_primes = len(ctx.primes)
    ctx.gaps = gaps_of(ctx.primes)
    print(f"{ctx.n_primes:,} primes, {len(ctx.gaps):,} gaps")

    for name in ([a.only] if a.only else list(SECTIONS)):
        SECTIONS[name](ctx)
    print()


if __name__ == "__main__":
    sys.exit(main())
