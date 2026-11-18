# Corrections

Claims that were published and later withdrawn or corrected, one entry each. The live results are in [Results](../RESULTS.md); each paper also records its own change in place.

---

## Withdrawn

**The switchback run-length law.** Published as a prime fact: sign-runs of the prime-angle change die faster than a coin ($63/27/8/1.6\%$ for lengths 1–4, reversal odds $63\to74\to80\to82\%$), identically at every scale. The baseline was a fair coin, which differencing already beats. Against the gap-shuffled null the effect vanishes:

| run length | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| real | 64.00% | 27.25% | 7.18% | 1.34% |
| null | 64.66% | 27.31% | 6.74% | 1.13% |

It is a property of any increasing, bounded-gap sequence. The $45°$-ceiling mechanism is real but belongs to the skeleton, which a gap-shuffle preserves; the paper's change-shuffle tested the wrong layer. The mod-6 traffic law in the same paper is unaffected. → [Switchback Law §3](../2_One_Wheel_Many_Shadows/Switchback_Law.md)

**The balance ratio as a new signal.** Its entire deviation from a shuffle null equals $\mathrm{cov}(g_n, g_{n+1})$ by the definition of covariance — true of any sequence. Now listed as a restatement in the audit. → [Balance Ratio §5–§6](../2_One_Wheel_Many_Shadows/PG_Balance_Ratio_And_Koide.md)

**The twin-gap exponent 1.866.** Published as $G_k \sim 0.70(\log T_k)^{1.866}$, "below the Hardy–Littlewood $\beta = 2$". Measured over four decades to $10^8$: $G \sim 0.792(\log T)^{1.978}$, against the prediction $(\log T)^2/C_2 = 0.757(\log T)^2$. The shortfall was a short-range log-log fit. → [`check_envelope_fits.py`](../3_Twin_Bertrand_Prime_Geometry/scripts/check_envelope_fits.py)

**The GBP envelope $G < 0.171(\log P)^{3.22}$.** Violated 204 times below $10^8$, worst $1.87\times$ at $T = 850{,}349$ ($G = 1452$ against a bound of 775). It was fitted on $\sup(G/T)$, attained at small $T$, then stated as a bound on $G$, whose extreme sits at large $T$. The exponent is not pinned (anything in $[2.5, 4.0]$ is arguable) and $R^2 = 0.982$ came from two parameters fitted to five nested running suprema. The shape survives. → [envelope fits](../3_Twin_Bertrand_Prime_Geometry/results/uniform_envelope_fits.md)

**The Filling Condition.** The twin-slope paper named a "Filling Condition" as the only obstacle to the twin prime conjecture, strictly weaker than the parity barrier. Its Form 3 is verbatim TPB, TPB implies the twin prime conjecture unaided, and the parity barrier blocks the existential statement too. The paper now stands on what survives: a second geometric route to TPB. → [Twin-Slope Ceiling](../3_Twin_Bertrand_Prime_Geometry/FS_twin_prime_geometry.md)

**Primorials seeding the doubling ladders.** $30\to60\to120\to240$ suggested primorials seed the long ladders. The record ladder (length 6) is seeded by $2362974 = 2\cdot3\cdot23\cdot17123$; among small primorials only 30 is even a working sum. → [Synthesis](../2_One_Wheel_Many_Shadows/FS_Synthesis_Doubling_and_Wheel.md)

**Jitter recoil "+2.7 pp genuine".** Published as 81.8% real / 79.2% null. Thirty threshold definitions were tested; several reproduce each number, none reproduces both, and all give a genuine column between $-0.7$ and $+0.2$ pp. The pair was computed at two different thresholds. The row now reads $\approx 0$ (artifact), as §4's exact $-\tfrac12$ identity requires. → [Differencing Trap §3](../2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md), [`repro/`](../2_One_Wheel_Many_Shadows/repro/)

## Corrected

**PSD last digit: $p_n \ge 7$, not $p_n \ge 5$.** $(5, 7, 11)$ gives $\mathrm{PSD} = 8$, the sole counterexample below $5\times10^6$; the proof's mod-5 step has nothing to stand on at $p = 5$. → [PG I](../3_Twin_Bertrand_Prime_Geometry/PG_I_PrimeTriangle.md)

**Twin-slope ceiling proof.** The theorem holds (verified to $10^6$); the published general case had an inequality running the wrong way and is repaired in place. → [Twin-Slope Ceiling](../3_Twin_Bertrand_Prime_Geometry/FS_twin_prime_geometry.md)

**A circular table row.** The $Q = 1732$ row of the lag-1 surrogate table: over $[10^6, 3\times10^6)$ every integer coprime to all primes $\le 1732$ is prime (pool ratio exactly 1.00), so it carries no evidence. The conclusion stands on the $Q = 317$ row (pool ratio 1.39). → [Angle Wobble §4.1](../2_One_Wheel_Many_Shadows/PG_Angle_Wobble.md)

**"68% of everything knowable."** Correct at $N = 10^4$ only; activation grows without bound, so the ratio drifts ($59\%$ at $10^6$). The stable statements are the template's $1.70$ bits, 73.3% of positions removed free, and $\approx 0.84$ bits per open slot. → [`entropy_budget.py`](../1_Factor_Skyline/repro/entropy_budget.py)

**The pre-Guth–Maynard cusp.** The claim that it sat at $\sigma \approx 5/7$ with height $12/5$ is inconsistent: $A_{\mathrm{Ing}}(5/7) = 7/3$, and a peak of $12/5$ on Ingham's curve forces $\sigma = 3/4$. Peripheral to the X5D result. → [figures/README](../5_X5D_EXPDB/figures/README.md)

**Upstream reproducibility stubs.** The Factor Skyline's original `reproducibility/tables/` scripts returned placeholder values; the entropy-budget numbers were first actually re-derived by [`entropy_budget.py`](../1_Factor_Skyline/repro/entropy_budget.py).

---

How these were caught, in plain language: [How We Know](HOW_WE_KNOW.md).
