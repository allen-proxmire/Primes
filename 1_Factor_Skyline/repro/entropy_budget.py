#!/usr/bin/env python3
"""Reproduce the Factor Skyline entropy budget -- and show its scale dependence.

    python entropy_budget.py

The collection's most-quoted numbers come from FSPapers_03 3.7 and are
repeated in the Prediction Budget, RESULTS.md and elsewhere:

    total H(dx) = 2.48 bits, of which
      template   1.70   (68% -- "everything the wheel tells you")
      escape     0.26   (irreducible; the parity barrier)
      activation 0.52   (which lpf a composite has)

All four reproduce here EXACTLY -- at N = 10^4, and only there. The
components behave very differently as N grows, so the headline ratio
"1.70 of 2.48" is a statement about a range that the papers do not name.
See repro/README.md for what that does and does not undermine.

Definitions, following FSPapers_03:
    lpf(n)  least prime factor
    dx(n)   the FS-x increment: 1 if n is prime, else lpf(n)
    D(p)    escape density, prod_{q<=p} (1 - 1/q)

    template   = H(dx) - H(dx | n mod 30)     what the 5#-wheel tells you
    escape     = (8/30) * H_b(P(prime | open))  binary prime/not at open slots
    activation = H(dx | n mod 30) - escape    which lpf, given covered/open

Needs nothing but the standard library. ~2 min.
"""
import math
import collections

NMAX = 3_000_000
RANGES = (10**3, 10**4, 10**5, 10**6, 3 * 10**6)
WHEEL = 30            # the 5# template the papers use


def least_prime_factors(n):
    lpf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if lpf[i] == i:
            for j in range(i * i, n + 1, i):
                if lpf[j] == j:
                    lpf[j] = i
    return lpf


def H(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)


def budget(lpf, N, wheel=WHEEL):
    dx = [(1 if lpf[n] == n else lpf[n]) for n in range(2, N + 1)]
    tot = len(dx)

    c = collections.Counter(dx)
    H_dx = H([v / tot for v in c.values()])

    by_res = collections.defaultdict(collections.Counter)
    for i, n in enumerate(range(2, N + 1)):
        by_res[n % wheel][dx[i]] += 1
    H_cond = 0.0
    for cnt in by_res.values():
        t = sum(cnt.values())
        H_cond += (t / tot) * H([v / t for v in cnt.values()])

    template = H_dx - H_cond

    opens = [n for n in range(2, N + 1) if math.gcd(n, wheel) == 1]
    q = sum(1 for n in opens if lpf[n] == n) / len(opens)
    H_b = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
    open_density = len(opens) / tot
    escape = H_b * open_density

    return dict(N=N, H_dx=H_dx, template=template, escape=escape,
                activation=H_cond - escape, q=q, H_b=H_b,
                open_density=open_density)


def main():
    print("Sieving to %s ..." % f"{NMAX:,}", end=" ", flush=True)
    lpf = least_prime_factors(NMAX)
    print("done\n")

    print("=" * 78)
    print("  FACTOR SKYLINE ENTROPY BUDGET, by range   (5#-wheel, mod 30)")
    print("=" * 78)
    print("  FSPapers_03 3.7 quotes:  H(dx) 2.48 | template 1.70 | escape 0.26 | activation 0.52")
    print()
    print("%11s %9s %10s %9s %11s %9s" % (
        "N", "H(dx)", "template", "escape", "activation", "wheel %"))
    rows = []
    for N in RANGES:
        r = budget(lpf, N)
        rows.append(r)
        print("%11s %9.4f %10.4f %9.4f %11.4f %8.1f%%" % (
            f"{N:,}", r["H_dx"], r["template"], r["escape"], r["activation"],
            100 * r["template"] / r["H_dx"]))

    m = next(r for r in rows if r["N"] == 10**4)
    print()
    print("  AT N = 10,000 ALL FOUR PUBLISHED NUMBERS REPRODUCE:")
    print("    H(dx)      %.4f  vs 2.48" % m["H_dx"])
    print("    template   %.4f  vs 1.70" % m["template"])
    print("    escape     %.4f  vs 0.26" % m["escape"])
    print("    activation %.4f  vs 0.52" % m["activation"])

    print()
    print("=" * 78)
    print("  BUT THE COMPONENTS DO NOT SCALE ALIKE")
    print("=" * 78)
    lo, hi = rows[0], rows[-1]
    print("    template    %.4f -> %.4f   STABLE. A genuine invariant of the wheel."
          % (lo["template"], hi["template"]))
    print("    escape      %.4f -> %.4f   peaks near 10^4, declines slowly"
          % (lo["escape"], hi["escape"]))
    print("    activation  %.4f -> %.4f   GROWS WITHOUT BOUND (more distinct lpf values)"
          % (lo["activation"], hi["activation"]))
    print("    H(dx)       %.4f -> %.4f   grows, driven entirely by activation"
          % (lo["H_dx"], hi["H_dx"]))
    print()
    print("    So 'the wheel is 68% of everything knowable' holds at N = 10^4.")
    print("    At N = 10^6 it is %.0f%%, and the share keeps falling -- not because the"
          % (100 * rows[-2]["template"] / rows[-2]["H_dx"]))
    print("    wheel weakens (it does not) but because the denominator grows.")

    print()
    print("=" * 78)
    print("  THE PART THAT ACTUALLY BEARS ON FINDING PRIMES")
    print("=" * 78)
    print("  Locating the next prime needs only prime/not-prime, so 'activation'")
    print("  -- which lpf a composite has -- is irrelevant to that question.")
    print()
    print("%11s %14s %13s %12s" % ("N", "P(prime|open)", "H_b per open", "per integer"))
    for r in rows:
        print("%11s %14.4f %13.4f %12.4f" % (
            f"{r['N']:,}", r["q"], r["H_b"], r["escape"]))
    print()
    print("  The wheel kills %.1f%% of positions for free (22/30), and what is left"
          % (100 * (1 - hi["open_density"])))
    print("  at an open slot is %.4f bits of genuine uncertainty. THAT ratio is the"
          % hi["H_b"])
    print("  Prediction Budget's real subject, and it is stable.")


if __name__ == "__main__":
    main()
