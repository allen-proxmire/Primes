"""Factor Skyline §4: the active template, and what no finished template copies.

  python active_template.py          # numpy + matplotlib; under a minute, ~1 GB RAM

1. Draws figures/FS_active_template.png (birth at p, activation at p^2;
   period p# against epoch length; periods per epoch).
2. Measures the alternation of neighbouring windows of wide-column length,
   n in [5e6, 5e7], for the real primes and for fair templates (wheel
   survivors to Q, thinned to prime density), with the pool ratio of each.
3. Neighbouring prime counts in short intervals, real vs a fair template vs
   the Montgomery-Soundararajan size.
"""
from math import prod
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- 1. figure
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#888", "xtick.color": "#555", "ytick.color": "#555"})
fig, ax = plt.subplots(1, 3, figsize=(17, 5.4))
for i, p in enumerate(P[:-1]):
    ax[0].plot([p, p * p], [i, i], color="#c9d8ee", lw=6, solid_capstyle="butt")
    ax[0].plot(p, i, "o", color="#2a78d6", ms=6)
    ax[0].plot(p * p, i, "s", color="#eb6834", ms=6)
    ax[0].text(p * 0.82, i, str(p), ha="right", va="center", fontsize=8, color="#555")
ax[0].set_xscale("log"); ax[0].set_yticks([]); ax[0].set_xlabel("n")
ax[0].plot([], [], "o", color="#2a78d6", label="born at p")
ax[0].plot([], [], "s", color="#eb6834", label="activates at p²")
ax[0].legend(frameon=False, loc="lower right")
ax[0].set_title("1. Each prime: born at p, activates at p²", loc="left", fontsize=11)
for i, p in enumerate(P[:-1]):
    a, b, T = p * p, P[i + 1] ** 2, prod(P[: i + 1])
    ax[1].plot([a, b], [T, T], color="#eb6834", lw=2.4)
    ax[1].plot([a, b], [b - a, b - a], color="#1baf7a", lw=2.4)
    if i < 9:
        ax[1].text(a * 1.05, T * 1.6, "%d#" % p, fontsize=8, color="#eb6834")
ax[1].plot([], [], color="#eb6834", lw=2.4, label="template period p#")
ax[1].plot([], [], color="#1baf7a", lw=2.4, label="epoch length (p² to next p²)")
ax[1].set_xscale("log"); ax[1].set_yscale("log"); ax[1].set_xlabel("n"); ax[1].set_ylabel("length")
ax[1].legend(frameon=False, loc="upper left")
ax[1].set_title("2. The period outruns the epoch from 5 on", loc="left", fontsize=11)
fr = [(P[i + 1] ** 2 - P[i] ** 2) / prod(P[: i + 1]) for i in range(len(P) - 1)]
ax[2].bar(range(len(fr)), fr, color=["#2a78d6" if f >= 1 else "#eb6834" for f in fr])
ax[2].axhline(1, color="#555", lw=1, ls="--")
ax[2].text(len(fr) - 1, 1.4, "one full period", ha="right", fontsize=9, color="#555")
ax[2].set_yscale("log"); ax[2].set_xticks(range(len(fr))); ax[2].set_xticklabels([str(p) for p in P[:-1]])
ax[2].set_xlabel("template with widths up to p"); ax[2].set_ylabel("periods completed per epoch")
ax[2].set_title("3. Never a whole period from 5 on", loc="left", fontsize=11)
for i, f in enumerate(fr[:6]):
    ax[2].text(i, f * 1.3, "%.2g" % f, ha="center", fontsize=8)
fig.tight_layout(); fig.savefig("../figures/FS_active_template.png", dpi=130)

# ------------------------------------------------- 2. alternation of windows
N = 50_000_000
isp = np.ones(N + 1, bool); isp[:2] = False
for p in range(2, int(N ** 0.5) + 1):
    if isp[p]:
        isp[p * p::p] = False
PR = np.nonzero(isp)[0]
C0 = np.concatenate([[0], np.cumsum(isp, dtype=np.int64)])
lo_p = int(N ** (1 / 3)) + 1                 # every width >= lo_p has p^3 > N:
Pw = PR[(PR >= lo_p) & (PR <= int(N ** 0.5))]  # its columns are p*q, q prime >= p
qmax = N // lo_p + 2
rng = np.random.default_rng(11)

def wide_length(C, H, off, start=5_000_000):
    """sum of widths of wide columns in windows [a, a+H): sum_p p * #{q prime, q>=p, pq in window}"""
    a = np.arange(start + off, N - H, H).astype(float); S = np.zeros(len(a))
    for p in Pw:
        lo = np.maximum(np.ceil(a / p), p); hi = np.floor((a + H - 1) / p)
        S += p * np.maximum(0, C[(hi + 1).astype(np.int64)] - C[np.minimum(lo, hi + 1).astype(np.int64)])
    return a, S

def lag1(a, S, deg=3):
    r = np.log(np.maximum(S, 1)); r -= np.polyval(np.polyfit(np.log(a), r, deg), np.log(a))
    return np.corrcoef(r[:-1], r[1:])[0, 1]

def wheel(Q):
    ok = np.ones(qmax + 1, bool); ok[:2] = False
    for r in PR[PR <= Q]:
        ok[::r] = False
    return ok

def fair(ok, Q):
    """wheel survivors thinned to the local prime count (blocks of 1000); returns cumulative counts"""
    q = np.zeros(qmax + 1, bool)
    for s in range(0, qmax + 1, 1000):
        o = ok[s:s + 1000]; m = o.sum()
        if m:
            q[s:s + 1000] = o & (rng.random(len(o)) < isp[s:s + 1000].sum() / m)
    q[:Q + 1] = isp[:Q + 1]
    return np.concatenate([[0], np.cumsum(q, dtype=np.int64)])

def pool(ok, a, b):
    return ok[a:b].sum() / isp[a:b].sum()

print("pool ratio of the template, near-square zone q in [2000, 7100) (fair above ~1.25)")
for Q in (13, 23, 31, 41):
    print("  Q = %2d: %.2f" % (Q, pool(wheel(Q), 2000, 7100)))
for H in (100_000, 200_000):
    real = np.mean([lag1(*wide_length(C0, H, o)) for o in (0, H // 3, 2 * H // 3)])
    print("\nwindows of %d: real primes %.3f" % (H, real))
    for Q in (13, 23, 31, 41):
        ok = wheel(Q); v = np.array([lag1(*wide_length(fair(ok, Q), H, 0)) for _ in range(20)])
        print("  template to %2d: %+.3f +- %.3f  (real %.1f sd below)" % (Q, v.mean(), v.std(), (v.mean() - real) / v.std()))

# ------------------------------------- 3. neighbouring short-interval counts
B = 1 - np.euler_gamma - np.log(2 * np.pi)
ok31 = wheel(31); fairs = [fair(ok31, 31) for _ in range(12)]
rr = lambda x: np.corrcoef(x[:-1] - x.mean(), x[1:] - x.mean())[0, 1]
print("\nneighbouring prime counts in intervals of length L")
for q1, q2, L in ((2000, 8000, 200), (8000, 40000, 60), (40000, 135000, 200)):
    e = np.arange(q1, q2, L)
    cnt = lambda C: (C[e[1:]] - C[e[:-1]]).astype(float)
    ms = -np.log(2) / (2 * (np.log(np.sqrt(q1 * q2) / L) + B))
    print("  q in [%d, %d), L = %d: real %+.2f   template to 31 %+.2f   Montgomery-Soundararajan %+.2f"
          % (q1, q2, L, rr(cnt(C0)), np.mean([rr(cnt(c)) for c in fairs]), ms))
