"""The Next Twin: the wheel size needed for the next twin pair after a prime to fall within one turn.
Checks the rule W >= -ln(1-s) ln^2 p / (2 C2) against every prime up to 4e7, and the turn-by-turn shares.
numpy; ~30 s."""
import numpy as np
from math import log, sqrt

C2 = 0.6601618
N = 40_000_000
s = np.ones(N + 3, bool); s[:2] = False
for q in range(2, int(N ** 0.5) + 2):
    if s[q]:
        s[q * q::q] = False
T = np.nonzero(s[:N + 1] & s[2:N + 3])[0]            # lower members t of twin pairs (t, t+2)
P = np.nonzero(s[:N - 3000])[0]

def first_twin_wait(ps):
    """distance from p to the upper member of the first twin pair above p"""
    return T[np.searchsorted(T, ps, "right")] + 2 - ps

print("1. which wheel, up to where (from the rule)")
for share in (0.5, 0.9, 0.99):
    a = -log(1 - share) / (2 * C2)
    print("   %2d%%: W >= %.2f ln^2 p;  " % (100 * share, a) +
          ", ".join("%d-wheel to ~10^%.1f" % (W, sqrt(W / a) / log(10)) for W in (30, 210, 2310, 30030, 510510)))

print("\n2. share of primes whose next twin falls within one turn: seen vs predicted 1 - exp(-W 2C2 / ln^2 p)")
for c, W in ((20, 30), (60, 30), (2500, 210), (5e4, 210), (1e5, 210), (1e6, 210), (1e7, 210), (1e7, 2310)):
    ps = P[(P > c / 1.3) & (P < c * 1.3)]
    seen = np.mean(first_twin_wait(ps) <= W)
    pred = 1 - np.exp(-W * 2 * C2 / log(c) ** 2)
    print("   p ~ %8.0e  %5d-wheel  seen %6.2f%%  predicted %6.2f%%  (%d primes)" % (c, W, 100 * seen, 100 * pred, len(ps)))

print("\n3. which turn of the 210-wheel holds the first twin: seen vs (1-f) f^(k-1), f = exp(-210 2C2 / ln^2 p)")
for c in (1e5, 1e6, 1e7):
    ps = P[(P > c / 2) & (P < c * 2)]
    k = (first_twin_wait(ps) - 1) // 210 + 1
    f = np.exp(-210 * 2 * C2 / log(c) ** 2)
    print("   p ~ %.0e: " % c + "  ".join("turn %d %5.1f%% (%4.1f%%)" % (j, 100 * np.mean(k == j), 100 * (1 - f) * f ** (j - 1)) for j in (1, 2, 3, 4)))

print("\n4. which 210-wheel twin slot holds the first twin after a prime (p in 1e3..4e7)")
from math import gcd
slots = [r for r in range(210) if gcd(r, 210) == 1 and gcd(r + 2, 210) == 1]
ps = P[P > 1000]
res = T[np.searchsorted(T, ps, "right")] % 210
print("   " + "  ".join("%d: %.1f%%" % (r, 100 * np.mean(res == r)) for r in slots))
