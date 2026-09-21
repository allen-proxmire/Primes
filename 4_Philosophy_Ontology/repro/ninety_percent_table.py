#!/usr/bin/env python3
"""Regenerate every number in `The_Ninety_Percent_Rule.md`.

    python ninety_percent_table.py

Question: standing on a prime near N, carrying only the wheels 2, 3, 5 and 7,
how many OPEN positions must you test before you have caught the next prime
90% of the time?

Method. For each decade N we take the window [N, 2N] -- one doubling, so the
neighbourhood is genuinely local and the prime density does not drift. From
every prime in that window we walk forward over the positions coprime to 210,
counting how many we test before landing on the next prime. The k-th entry of
the survival curve is the fraction of starting primes whose next prime was
caught within k open slots.

The window is capped at 2e6 wide so the high decades stay computable; that
caps the sample, not the accuracy -- 86,817 starting primes at 1e10.

Sieving is segmented: base primes to sqrt(2*N) only, so 1e10 needs a base
sieve to ~1.5e5, not a sieve of the whole line.

Standard library only. Runtime a couple of minutes, dominated by the 1e10 row.
"""
import math

DECADES = [10**k for k in range(3, 11)]
WHEEL = [2, 3, 5, 7]
MODULUS = 2 * 3 * 5 * 7                 # 210
OPEN_RESIDUES = [r for r in range(MODULUS) if all(r % p for p in WHEEL)]
OPEN_SET = set(OPEN_RESIDUES)
TARGET = 0.90
MAX_WIDTH = 2 * 10**6
MAX_SLOTS = 40


def base_sieve(limit):
    """All primes <= limit, plain sieve."""
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
    return [i for i in range(limit + 1) if sieve[i]]


def segment(lo, hi, base):
    """Bitmap of primality for [lo, hi), via the base primes."""
    n = hi - lo
    seg = bytearray([1]) * n
    for p in base:
        if p * p >= hi:
            break
        start = max(p * p, ((lo + p - 1) // p) * p)
        seg[start - lo:: p] = bytearray(len(seg[start - lo:: p]))
    if lo == 0:
        seg[0:2] = b"\x00\x00"
    elif lo == 1:
        seg[0] = 0
    return seg


def open_positions(lo, hi):
    """Every position in [lo, hi) coprime to 210, in order."""
    out = []
    block = (lo // MODULUS) * MODULUS
    while block < hi:
        for r in OPEN_RESIDUES:
            x = block + r
            if lo <= x < hi:
                out.append(x)
        block += MODULUS
    return sorted(out)


def measure(N, base):
    lo, hi = N, min(2 * N, N + MAX_WIDTH)
    seg = segment(lo, hi, base)
    primes = [lo + i for i, b in enumerate(seg) if b]
    if len(primes) < 2:
        return None

    slots = open_positions(lo, hi)
    slot_is_prime = [bool(seg[s - lo]) for s in slots]
    # index of the first slot >= x, for each starting prime
    slot_index = {s: i for i, s in enumerate(slots)}

    caught = [0] * (MAX_SLOTS + 1)      # caught[k] = # caught within k slots
    exact = [0] * (MAX_SLOTS + 1)       # exact[k]  = # caught at exactly slot k
    first_prime = 0
    total = 0
    tests_sum = 0

    for a, b in zip(primes, primes[1:]):
        # first open slot strictly after a
        j = slot_index.get(a)
        if j is None:                   # a is 2,3,5 or 7 itself
            continue
        j += 1
        if j >= len(slots):
            break
        total += 1
        k = 0
        idx = j
        while idx < len(slots) and slots[idx] <= b:
            k += 1
            if slot_is_prime[idx]:
                break
            idx += 1
        if k == 0 or k > MAX_SLOTS:
            continue
        if k == 1:
            first_prime += 1
        exact[k] += 1
        tests_sum += k
        for m in range(k, MAX_SLOTS + 1):
            caught[m] += 1

    ninety = next((k for k in range(1, MAX_SLOTS + 1)
                   if caught[k] / total >= TARGET), None)

    # theory: q = (prime density) / (open-slot density)
    q = MODULUS / (len(OPEN_RESIDUES) * math.log(N))
    k_theory = math.ceil(math.log(1 - TARGET) / math.log(1 - q))

    return dict(N=N, lo=lo, hi=hi, total=total,
                mean_gap=(primes[-1] - primes[0]) / (len(primes) - 1),
                p_first=first_prime / total,
                mean_tests=tests_sum / total,
                ninety=ninety, q=q, k_theory=k_theory,
                curve=[caught[k] / total for k in range(1, 13)],
                exact=[exact[k] / total for k in range(1, 13)])


def main():
    print(f"open residues mod {MODULUS}: {len(OPEN_RESIDUES)}"
          f"  ->  {100*len(OPEN_RESIDUES)/MODULUS:.1f}% open,"
          f" {100*(1-len(OPEN_RESIDUES)/MODULUS):.1f}% killed free\n")

    base = base_sieve(int((2 * DECADES[-1])**0.5) + 1000)
    rows = [measure(N, base) for N in DECADES]

    print(f"{'N':>7} {'primes':>10} {'mean gap':>9} {'P(slot1)':>9} "
          f"{'mean tests':>11} {'90% at':>7} {'theory':>7} {'q':>7}")
    for r in rows:
        print(f"10^{int(math.log10(r['N'])):<4} {r['total']:>10,} "
              f"{r['mean_gap']:>9.1f} {100*r['p_first']:>8.1f}% "
              f"{r['mean_tests']:>11.2f} {r['ninety']:>7} {r['k_theory']:>7} "
              f"{100*r['q']:>6.1f}%")

    print("\nsurvival curve -- P(caught within k open slots)")
    print("   N  " + "".join(f"{k:>6}" for k in range(1, 13)))
    for r in rows:
        print(f"10^{int(math.log10(r['N'])):<3}" +
              "".join(f"{100*v:>5.0f}%" for v in r['curve']))

    print("\nexactly at slot k -- and the geometric prediction q(1-q)^(k-1)")
    for r in rows:
        if r['N'] != 10**6:
            continue
        q = r['p_first']
        print(f"  measured (10^6): " + " ".join(f"{100*v:>5.1f}" for v in r['exact'][:7]))
        print(f"  geometric      : " +
              " ".join(f"{100*q*(1-q)**(k):>5.1f}" for k in range(7)))


if __name__ == "__main__":
    main()
