#!/usr/bin/env python3
"""Numerical companion to X5D §6.2 (numpy).

    python gap2_free_choice.py

Evaluates the theta_gap,2 route  max(alpha, beta)  with
    alpha = 4s - 2 + 2(B(1-s) - 1)/(B - A),   beta = 4s - 2 + (B(1-s) - 1)/A
two ways: feeding the pointwise-best zero-density bound A, and choosing A
freely in [best A, min(||A||, B)) at each sigma (the proposition accepts any
upper bounds).

Test 1 -- consistency of the "any upper bound" reading, 1979 inputs:
    Ingham 3/(2-s), Huxley 3/(3s-1), a sqrt(1-s)-type bound, Heath-Brown's
    energy bounds; ||A|| = 12/5.  Free choice should not beat Heath-Brown's 23/18
    (and certainly not 123/100).
Test 2 -- [59/60, 1) with the database's near-1 estimates
    (Bourgain 6/(303s-290), Tao-Trudgian-Yang 3/(10s-7)), B = 12/(4s-1).
"""
import math
import numpy as np

def B79(s):
    if s <= 2/3: return (10 - 11*s) / ((2 - s) * (1 - s))
    if s <= 3/4: return (18 - 19*s) / ((4 - 2*s) * (1 - s))
    return 12 / (4*s - 1)

def route(s, A, B):
    N = B * (1 - s) - 1
    return max(4*s - 2 + 2*N / (B - A), 4*s - 2 + N / A)

def sup_route(sigmas, A0, B, M, free):
    worst = -math.inf
    for s in sigmas:
        a0, b = A0(s), B(s)
        if free:
            grid = np.linspace(a0, min(M, b), 600, endpoint=False)
            v = min(route(s, a, b) for a in grid)
        else:
            v = route(s, a0, b)
        worst = max(worst, v)
    return worst

A79 = lambda s: min(3/(2 - s), 3/(3*s - 1), 6.42*math.sqrt(1 - s))
S1 = np.linspace(0.5, 0.9999, 2500)
M = 12/5
print("Test 1 (1979 inputs, ||A|| = 12/5, first term 2 - 2/||A|| = %.4f)" % (2 - 2/M))
print("  pointwise-best A : %.4f" % max(2 - 2/M, sup_route(S1, A79, B79, M, False)))
print("  A chosen freely  : %.4f   (Heath-Brown 23/18 = %.4f; Stadlmann 123/100 = 1.23)"
      % (max(2 - 2/M, sup_route(S1, A79, B79, M, True)), 23/18))

Anear = lambda s: min(6/(303*s - 290), 3/(10*s - 7))
Bnear = lambda s: 12/(4*s - 1)
S2 = np.linspace(59/60, 0.999999, 2000)
print("Test 2 ([59/60, 1), database near-1 estimates)")
print("  pointwise-best A : %.4f   (-> 33/23 = %.4f)" % (sup_route(S2, Anear, Bnear, 30/13, False), 33/23))
print("  A chosen freely  : %.4f   (endpoint optimum 5/4)" % sup_route(S2, Anear, Bnear, 30/13, True))
