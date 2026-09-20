#!/usr/bin/env python3
"""Verify the Prime Square-Difference results of PG I -- Theorems 3 and 5.

    python check_psd.py [limit]     # default 5,000,000

This is the first claim in series 3 to be independently re-verified. It
found an off-by-one: Theorem 5.2 is stated for p_n >= 5 and has exactly
one counterexample there, the triple (5, 7, 11). It is true for p_n >= 7.

  Theorem 3   C_2^2 - C_1^2 = p_{n+2}^2 - p_n^2 = G_n (2 p_n + G_n)
              CONFIRMED -- and it needs no primality at all; the shared
              p_{n+1} terms cancel for any three numbers whatever.

  Theorem 5.1 PSD_n = (p_{n+2}^2 - p_n^2) / 12 is an integer for p_n >= 5
              CONFIRMED, and the threshold is sharp: (2,3,5) gives 7/4
              and (3,5,7) gives 10/3.

  Theorem 5.2 last digit of PSD_n is in {0, 4, 6}
              FALSE for p_n >= 5 as published -- (5,7,11) gives PSD = 8.
              TRUE for p_n >= 7, no exceptions found.

              Why: the proof's mod-6 step is fine, but the last digit
              also needs p^2 = +/-1 (mod 5), which fails at p = 5 itself.

  Bonus       the last digits are not equidistributed. 4 and 6 occur
              EXACTLY equally (forced: the two transition types interleave,
              so their counts differ by at most 1). 0 occurs roughly twice
              as often -- 1.92x at 5e6, approaching 2 but not equal to it.
              The shortfall is a finite-range effect plus the residue
              correlations of Lemke Oliver-Soundararajan, so the deviation
              is itself a small measurement rather than an error.

Standard library only.
"""
import sys
import collections
from fractions import Fraction


def sieve(n):
    b = bytearray([1]) * (n + 1)
    b[0] = b[1] = 0
    i = 2
    while i * i <= n:
        if b[i]:
            b[i*i::i] = bytearray(len(b[i*i::i]))
        i += 1
    return b


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 5_000_000
    print(f"Sieving to {N:,} ...", end=" ", flush=True)
    b = sieve(N)
    P = [i for i in range(2, N + 1) if b[i]]
    print(f"{len(P):,} primes, {len(P)-2:,} consecutive triples\n")

    psd_num = lambda i: P[i+2]**2 - P[i]**2

    # ---- Theorem 3 -----------------------------------------------------
    print("THEOREM 3 — C_2^2 - C_1^2 = p_{n+2}^2 - p_n^2")
    bad = sum(1 for i in range(len(P)-2)
              if (P[i+1]**2 + P[i+2]**2) - (P[i]**2 + P[i+1]**2) != psd_num(i))
    badG = sum(1 for i in range(len(P)-2)
               if psd_num(i) != (P[i+2]-P[i]) * (2*P[i] + (P[i+2]-P[i])))
    print(f"   counterexamples: {bad}      (skip-gap form: {badG})")
    a, c, d = 4, 9, 25
    print(f"   holds with no primality: (a,b,c)=({a},{c},{d}) ->",
          (c**2 + d**2) - (a**2 + c**2) == d**2 - a**2)

    # ---- Theorem 5.1 ---------------------------------------------------
    print("\nTHEOREM 5.1 — PSD integral for p_n >= 5")
    bad = [i for i in range(len(P)-2) if P[i] >= 5 and psd_num(i) % 12]
    print(f"   counterexamples: {len(bad)}")
    print("   threshold is sharp — just below it:")
    for i in range(2):
        v = Fraction(psd_num(i), 12)
        print(f"      ({P[i]},{P[i+1]},{P[i+2]})   PSD = {v}   "
              f"{'integer' if v.denominator == 1 else 'NOT an integer'}")

    # ---- Theorem 5.2 ---------------------------------------------------
    print("\nTHEOREM 5.2 — last digit of PSD in {0, 4, 6}")
    for thr in (5, 7):
        bad = [(P[i], P[i+1], P[i+2], psd_num(i)//12)
               for i in range(len(P)-2)
               if P[i] >= thr and psd_num(i) % 12 == 0
               and (psd_num(i)//12) % 10 not in (0, 4, 6)]
        mark = "  <-- AS PUBLISHED" if thr == 5 else "  <-- CORRECTED"
        print(f"   p_n >= {thr}:  counterexamples: {len(bad)}{mark}")
        for t in bad[:5]:
            print(f"      ({t[0]},{t[1]},{t[2]})  ->  PSD = {t[3]}   last digit {t[3] % 10}")

    # ---- the 2:1:1 ------------------------------------------------------
    print("\nBONUS — the last digits are not equidistributed")
    d = collections.Counter((psd_num(i)//12) % 10
                            for i in range(len(P)-2) if P[i] >= 7)
    tot = sum(d.values())
    for k in sorted(d):
        print(f"   last digit {k}: {d[k]:>9,}  ({100*d[k]/tot:5.2f}%)")
    if d[4] and d[6]:
        print(f"   ratio 0 : 4 : 6  =  {d[0]/d[4]:.4f} : 1 : {d[6]/d[4]:.4f}")
        print(f"   4 and 6 differ by {abs(d[4]-d[6])} — exact equality is forced (see below)")
    print("\n   PSD is even (24 divides the numerator) and mod 5 lands in {0,1,4},")
    print("   so the last digit is 0, 6 or 4 respectively. A uniform model over the")
    print("   16 residue pairs (p_n, p_{n+2}) mod 5 would predict 2 : 1 : 1.")
    print("   4 and 6 ARE exactly equal — they count the two directions of the same")
    print("   transition, which interleave, so their counts differ by at most 1.")
    print("   0 is NOT exactly double. The shortfall from 2 is a finite-range effect")
    print("   plus Lemke Oliver-Soundararajan residue correlations: the uniform")
    print("   model is an approximation here, not a theorem.")


if __name__ == "__main__":
    main()
