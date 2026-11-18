#!/usr/bin/env python3
"""Exact checks of every closed-form number in X5D.md (standard library only).

    python check_x5d_arithmetic.py      # exits non-zero if any check fails

§6.1  The Ingham / Guth-Maynard cusp and theta_PNT <= 17/30.
§6.2  The theta_gap,2 route: exponent pair, Bourgain's conditions,
      the closed forms of alpha and beta, and the limit 33/23.
"""
from fractions import Fraction as F
import sys

fails = []
def check(label, cond):
    print(("  ok    " if cond else "  FAIL  ") + label)
    if not cond:
        fails.append(label)

print("§6.1  the cusp")
ingham = lambda s: F(3) / (2 - s)
gm = lambda s: F(15) / (5 * s + 3)
s0 = F(7, 10)
check("Ingham(7/10) = 30/13", ingham(s0) == F(30, 13))
check("Guth-Maynard(7/10) = 30/13", gm(s0) == F(30, 13))
check("Ingham increasing on [1/2, 7/10]", all(ingham(F(50 + i, 100)) < ingham(F(51 + i, 100)) for i in range(20)))
check("Guth-Maynard decreasing on [7/10, 1]", all(gm(F(70 + i, 100)) > gm(F(71 + i, 100)) for i in range(30)))
A = F(30, 13)
check("theta_PNT <= 1 - 1/||A|| = 17/30", 1 - 1 / A == F(17, 30))
check("theta_PNT-AA <= 1 - 2/||A|| = 2/15", 1 - 2 / A == F(2, 15))
check("d theta / d||A|| = 1/||A||^2 = 169/900", 1 / A**2 == F(169, 900))
check("Ingham-Huxley: 3/(2-s) = 3/(3s-1) at s = 3/4, height 12/5",
      ingham(F(3, 4)) == F(12, 5) == F(3) / (3 * F(3, 4) - 1))

print("§6.2  the theta_gap,2 route")
m = 6
k = F(2, (m - 1) ** 2 * (m + 2))
l = 1 - F(3 * m - 2, m * (m - 1) * (m + 2))
check("Heath-Brown pair m=6 is (1/100, 14/15)", (k, l) == (F(1, 100), F(14, 15)))
check("Bourgain conditions k<1/5, l>3/5, 15l+20k>13, k<=11/85",
      k < F(1, 5) and l > F(3, 5) and 15 * l + 20 * k > 13 and k <= F(11, 85))
check("threshold (l+1)/(2(k+1)) = 290/303", (l + 1) / (2 * (k + 1)) == F(290, 303))
Abour = lambda s: 4 * k / (2 * (1 + k) * s - 1 - l)
Aused = lambda s: F(6) / (303 * s - 290)
B = lambda s: F(12) / (4 * s - 1)
alpha = lambda s: 4 * s - 2 + 2 * (B(s) * (1 - s) - 1) / (B(s) - Aused(s))
beta = lambda s: 4 * s - 2 + (B(s) * (1 - s) - 1) / Aused(s)
grid = [F(5900 + i, 6000) for i in range(100)]
check("Bourgain bound = 6/(303 s - 290)", all(Abour(s) == Aused(s) for s in grid))
check("alpha = (2376 s^2 - 1981 s - 296) / (3 (602 s - 579))",
      all(alpha(s) == (2376 * s * s - 1981 * s - 296) / (3 * (602 * s - 579)) for s in grid))
check("beta = (-4752 s^2 + 8507 s - 3758) / (6 (4 s - 1))",
      all(beta(s) == (-4752 * s * s + 8507 * s - 3758) / (6 * (4 * s - 1)) for s in grid))
check("A < B on [59/60, 1)", all(Aused(s) < B(s) for s in grid))
check("alpha increasing on [59/60, 1)", all(alpha(grid[i]) < alpha(grid[i + 1]) for i in range(99)))
check("alpha(59/60) = 16043/11670", alpha(F(59, 60)) == F(16043, 11670))
check("lim alpha (s -> 1) = 33/23", F(2376 - 1981 - 296, 3 * (602 - 579)) == F(33, 23))
check("lim alpha = 2 - 2/(B(1) - A(1)) = 33/23", 2 - 2 / (B(F(1)) - Aused(F(1))) == F(33, 23))
check("with A(1-) = 0: lim alpha = 2 - 2/B(1) = 3/2", 2 - 2 / B(F(1)) == F(3, 2))
check("beta < alpha on [59/60, 1)", all(beta(s) < alpha(s) for s in grid))
check("endpoint balance: A1 = B1/3 = 4/3 gives alpha = beta = 5/4",
      2 - 2 / (4 - F(4, 3)) == 2 - 1 / F(4, 3) == F(5, 4) == 2 - F(3, 4))
check("3/(10s-7) <= 4/3 iff s >= 37/40", F(3) / (10 * F(37, 40) - 7) == F(4, 3))
check("Bourgain 6/(303s-290) <= 4/3 iff s >= 589/606", F(6) / (303 * F(589, 606) - 290) == F(4, 3))
check("first term 2 - 2/||A|| with ||A|| = 30/13 is 17/15 < 33/23", 2 - 2 / A == F(17, 15) < F(33, 23))

print()
print("FAILED: %d" % len(fails) if fails else "all checks pass")
sys.exit(1 if fails else 0)
