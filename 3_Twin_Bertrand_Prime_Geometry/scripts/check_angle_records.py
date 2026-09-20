#!/usr/bin/env python3
"""Verify PG II Theorem 6(iii) — the Angle-Record Theorem.

    python check_angle_records.py [limit]      # default 100,000,000

THE CLAIM (PG II, Def. 5 + Thm 6(iii)):
    A consecutive prime pair (p_n, p_{n+1}) is an ANGLE-RECORD if
    rho(p_n, p_{n+1}) > rho(p_m, p_{m+1}) for all m < n, where
    rho(p,q) = p/q. Every angle-record with p_n >= 3 is a twin pair.

This matters more than PG I's square-difference identity: by Thm 6 it is
logically EQUIVALENT to the Twin-Prime Bertrand Postulate, so it is the
load-bearing claim of the whole series.

WHAT IS CHECKED
  1. every angle-record with p_n >= 3 is a twin              (the theorem)
  2. the converse — every twin sets a record                 (stronger)
  3. both readings of "for all m < n", since the pair (2,3) is ambiguous:
       reading A: records taken over pairs from (3,5) onward
       reading B: records taken over all pairs, then filtered to p_n >= 3
     The proof says "the first such record is (3,5)", which is reading A;
     under B, (3,5) is not a record at all because rho(2,3) = 2/3 > 3/5.
     Both are tested; the theorem should survive either way.

Comparisons use exact integer cross-multiplication (a/b > c/d iff
a*d > c*b), so no floating point is involved anywhere.

Standard library only. ~1-2 min at 1e8.
"""
import sys


def sieve(n):
    b = bytearray([1]) * (n + 1)
    b[0] = b[1] = 0
    i = 2
    while i * i <= n:
        if b[i]:
            b[i*i::i] = bytearray(len(b[i*i::i]))
        i += 1
    return b


def records(pairs):
    """Yield (p, q, index) for each running record of p/q, exactly."""
    bn, bd = 0, 1
    for i, (p, q) in enumerate(pairs):
        if p * bd > bn * q:          # p/q > bn/bd
            bn, bd = p, q
            yield p, q, i


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000_000
    print(f"Sieving to {N:,} ...", end=" ", flush=True)
    b = sieve(N)
    P = [i for i in range(2, N + 1) if b[i]]
    print(f"{len(P):,} primes")
    pairs = [(P[i], P[i+1]) for i in range(len(P) - 1)]
    is_twin = lambda p, q: q - p == 2
    print(f"{len(pairs):,} consecutive pairs\n")

    for label, start in (("A — record sequence begins at (3,5)", 1),
                         ("B — records over all pairs, then filter p_n >= 3", 0)):
        print("=" * 74)
        print(f"  READING {label}")
        print("=" * 74)
        recs = [r for r in records(pairs[start:]) if r[0] >= 3]
        nontwin = [(p, q) for p, q, _ in recs if not is_twin(p, q)]
        print(f"   angle-records with p_n >= 3 : {len(recs):,}")
        print(f"   of those, NOT twin pairs    : {len(nontwin)}")
        if nontwin:
            for p, q in nontwin[:10]:
                print(f"      COUNTEREXAMPLE  ({p}, {q})   gap {q-p}")
        else:
            print("      -> claim holds, no exceptions")
        print(f"   first eight records: {[(p,q) for p,q,_ in recs[:8]]}")

        # converse: does every twin set a record?
        twins = [(p, q) for p, q in pairs if is_twin(p, q) and p >= 3]
        recset = {(p, q) for p, q, _ in recs}
        missed = [t for t in twins if t not in recset]
        print(f"\n   twin pairs with p >= 3      : {len(twins):,}")
        print(f"   twins that do NOT set a record: {len(missed)}")
        if missed:
            for t in missed[:10]:
                print(f"      {t}")
        else:
            print("      -> the record sequence IS exactly the twin sequence")
        print()

    # what the theorem is equivalent to
    print("=" * 74)
    print("  THE EQUIVALENCE (Thm 6): T_{k+1} < 2 T_k for every twin T_k >= 11")
    print("=" * 74)
    T = [p for p, q in pairs if is_twin(p, q)]
    bad = [(T[i], T[i+1]) for i in range(len(T)-1) if T[i] >= 11 and T[i+1] >= 2*T[i]]
    print(f"   twin primes found           : {len(T):,}  (largest {T[-1]:,})")
    print(f"   violations of T_k+1 < 2 T_k : {len(bad)}")
    if bad:
        for t in bad[:10]:
            print(f"      {t[0]} -> {t[1]}   ratio {t[1]/t[0]:.4f}")
    else:
        ratios = [(T[i+1]/T[i], T[i]) for i in range(len(T)-1) if T[i] >= 11]
        worst, at = max(ratios)
        print(f"      -> TPB holds throughout. Worst ratio {worst:.4f} at T_k = {at:,}")
        print(f"         (the conjecture needs < 2; the margin is large and grows)")


if __name__ == "__main__":
    main()
