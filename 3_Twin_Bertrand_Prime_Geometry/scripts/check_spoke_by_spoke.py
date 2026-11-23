"""Twin Bertrand §1.5, spoke by spoke: in each front [p^2, p'^2) apply the spokes smallest first and compare the
twin-open candidates still standing with the fair share L * (1/2) prod (1 - 2/q). Then, at p^0.6, p^0.8, p^0.9,
split the candidates into real twins and the rest, and compare what the remaining spokes strike with their
fair share. numpy; ~1 min."""
import numpy as np
N = 110000; s = np.ones(N, bool); s[:2] = False
for q in range(2, 340):
    if s[q]: s[q * q::q] = False
P = np.nonzero(s)[0]
ts = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
print("1. candidates left / fair share, spokes up to p^t")
print("fronts near p      " + "  ".join("t=%.1f" % t for t in ts))
split = {}
for lo, cnt in ((1000, 40), (10000, 40), (100000, 12)):
    i0 = np.searchsorted(P, lo); num = np.zeros(len(ts)); den = np.zeros(len(ts))
    cand = np.zeros(len(ts)); fair_rest = np.zeros(len(ts)); twins = 0
    for a, b in zip(P[i0:i0 + cnt], P[i0 + 1:i0 + cnt + 1]):
        A, B = int(a) ** 2, int(b) ** 2 - 2; L = B - A; alive = np.ones(L, bool); dens = 1.0; k = 0
        stage = []
        for q in P:
            if q > a: break
            while k < len(ts) and q > a ** ts[k]:
                stage.append((alive.sum(), dens)); k += 1
            if q == 2: alive[(-A) % 2::2] = False; dens *= 0.5
            else:
                alive[(-A) % q::q] = False; alive[(-A - 2) % q::q] = False; dens *= 1 - 2 / q
        while k < len(ts): stage.append((alive.sum(), dens)); k += 1
        twins += alive.sum()
        for j, (c, d) in enumerate(stage):
            num[j] += c; den[j] += L * d; cand[j] += c; fair_rest[j] += c * (1 - dens / d)
    print("p ~ %6d (%2d)   " % (lo, cnt) + "  ".join("%.3f" % x for x in num / den))
    split[lo] = (cand, fair_rest, twins)
print("e^{2 gamma}/4 = %.3f" % (np.exp(2 * np.euler_gamma) / 4))
print("\n2. at p^t: candidates = real twins + pairs with a two-big-prime member; what the spokes in (p^t, p] strike vs their fair share")
for lo, (cand, fair, tw) in split.items():
    for t in (0.6, 0.8, 0.9):
        j = ts.index(t); c = cand[j]
        print("p ~ %6d  t=%.1f: candidates %6d  real twins %5d (%4.1f%%)  struck %6d  fair-share strike %6.0f  struck/fair %.2f"
              % (lo, t, c, tw, 100 * tw / c, c - tw, fair[j], (c - tw) / fair[j]))
