# Corrections

Claims that were published and later withdrawn or corrected, one entry each. The papers state only the corrected versions; the live results are in [Results](../RESULTS.md).

---

## Withdrawn

**The angle-record equivalence (PG II Theorem 6, PG III Theorem 7).** Published as: every angle record of the prime triangle is a twin *if and only if* TPB holds. The direction "TPB ⇒ records are twins" is proved, and every twin is a record unconditionally. The converse proof assumed a non-twin pair $(P, P+g)$ with $P > 2T_k$ beats the twin at $T_k$, but Lemma 2.1 needs $2P > gT_k$, which follows from $P > 2T_k$ only when $g \le 4$. So if TPB failed at $T_k$, a non-twin record would appear only if some pair in $(T_k, T_{k+1})$ had $2P > gT_k$ — near $2T_k$, a cousin pair — which is not guaranteed. The 440,312 = 440,312 check is a consequence of TPB, not an equivalent; TPB itself is verified directly by the ratio check. The same gap is in PG III's generalized version. → [Twin Bertrand §2.3](../3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**The "Geometric PNT" (FSPapers I Theorem 5.2).** Published as $\pi(N) \sim N\prod_{q\le\sqrt N}(1 - 1/q)$, derived from independence of the coverage layers. By Mertens the right side is $\sim 2e^{-\gamma}N/\ln N \approx 1.123\,N/\ln N$, so the statement is false by that constant (Mertens' paradox); the layers are not independent up to $\sqrt N$. The same independence argument underlay the stated derivations of Möbius cancellation and Erdős–Kac. These classical results are now described as pictured by the skyline, not derived from it. → [The Factor Skyline §7](../1_Factor_Skyline/Factor_Skyline.md)

**"$C_H > 1$ for every admissible $H$" as a theorem (FSPapers I Theorem 4.7).** The proof given covered pairs only and deferred the rest to "standard arguments". For pairs it holds by the formula $C_{\{0,h\}} = 2C_2\prod_{p\mid h,p>2}\frac{p-1}{p-2}$; for $k \ge 3$ it is now stated as checked numerically. The sexy-prime constant was also listed as 2.6455; it is $2\cdot2C_2 = 2.6406$. → [The Factor Skyline §3](../1_Factor_Skyline/Factor_Skyline.md)

**"Gap 6 dominates because it is the maximal gap of the 5#-template."** The maximal open-position gap of the 7#-template is 10, not 30, so the stated progression $6 \to 30 \to 210$ does not follow from template maxima. Jumping champions are explained by the singular-series weights of the offset comb. → [The Prime Crystal §1](../2_One_Wheel_Many_Shadows/Prime_Crystal.md)

**The switchback run-length law.** Published as a prime fact: sign-runs of the prime-angle change die faster than a coin ($63/27/8/1.6\%$ for lengths 1–4, reversal odds $63\to74\to80\to82\%$), identically at every scale. The baseline was a fair coin, which differencing already beats. Against the gap-shuffled null the effect vanishes:

| run length | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| real | 64.00% | 27.25% | 7.18% | 1.34% |
| null | 64.66% | 27.31% | 6.74% | 1.13% |

It is a property of any increasing, bounded-gap sequence. The mod-6 traffic law in the same paper is unaffected. → [The Null-Model Discipline §2](../2_One_Wheel_Many_Shadows/Null_Model_Discipline.md)

**The balance ratio as a new signal.** Its entire deviation from a shuffle null equals $\mathrm{cov}(g_n, g_{n+1})$ by the definition of covariance. Now listed as a restatement. → [Gap Correlations §5.3](../2_One_Wheel_Many_Shadows/Gap_Correlations.md)

**The twin-gap exponent 1.866.** Published as $G_k \sim 0.70(\log T_k)^{1.866}$, "below the Hardy–Littlewood $\beta = 2$". Measured over four decades to $10^8$: $G \sim 0.792(\log T)^{1.978}$, against the prediction $(\log T)^2/C_2 = 0.757(\log T)^2$. → [`check_envelope_fits.py`](../3_Twin_Bertrand_Prime_Geometry/scripts/check_envelope_fits.py)

**The GBP envelope $G < 0.171(\log P)^{3.22}$.** Violated 204 times below $10^8$, worst $1.87\times$ at $T = 850{,}349$ ($G = 1452$ against a bound of 775). Fitted on $\sup(G/T)$, attained at small $T$, then stated as a bound on $G$, whose extreme sits at large $T$; $R^2 = 0.982$ came from two parameters fitted to five nested running suprema. → [envelope fits](uniform_envelope_fits.md)

**The Filling Condition.** The twin-slope paper named a "Filling Condition" as the only obstacle to the twin prime conjecture, strictly weaker than the parity barrier. Its Form 3 is verbatim TPB, TPB implies the twin prime conjecture unaided, and the parity barrier blocks the existential statement too. → [Twin Bertrand §3.4](../3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**Primorials seeding the doubling ladders.** The record ladder (length 6) is seeded by $2362974 = 2\cdot3\cdot23\cdot17123$; among small primorials only 30 is a working sum. → [Consecutive-Prime Sums §5.4](../2_One_Wheel_Many_Shadows/Consecutive_Prime_Sums.md)

**Jitter recoil "+2.7 pp genuine".** Published as 81.8% real / 79.2% null. Of thirty threshold definitions, several reproduce each number, none reproduces both, and all give a genuine column between $-0.7$ and $+0.2$ pp. The pair was computed at two different thresholds; the effect is $\approx 0$, as the $-\tfrac12$ identity requires. → [Gap Correlations §4](../2_One_Wheel_Many_Shadows/Gap_Correlations.md)

**"One polytope generates the Exponent Database" (X5D Theorem 4.9).** Stated as: every output of the database is uniquely determined by a single region $\mathcal P \subset \mathbb R^5$, newly identified as the central object. Three qualifications the theorem omitted: the exponent-pair hull, $\beta^*$ and $\mu$ hull generate constraints on $\mathcal P$ rather than descending from it; the Ivić and Bourgain closed-form routes to $A(\sigma)$ bypass $\mathcal P$; and the database builds a finite family $\mathcal P^{(i)}$, not one region. The five-dimensional region of tuples $(\sigma,\tau,\rho,\rho^*,s)$ is Tao–Trudgian–Yang's own $\mathcal E$. The "proof" was a correspondence with code paths. Now stated as a description of the downstream pipeline. → [X5D §3](../5_X5D_EXPDB/X5D.md)

**Two different θ's conflated (X5D headline).** The headline paired the X5D pipeline with "the prime-gap exponent $\theta = 17/30$". The pipeline's $\theta$ (`compute_gap2`) is the second-moment exponent $\theta_{\mathrm{gap},2}$, whose database route gives $\frac32$; $\frac{17}{30}$ is $\theta_{\mathrm{PNT}}$, primes in all short intervals, and is Guth and Maynard's bound. The "attack surface about 0.006 wide" had no derivation in the paper and was dropped. → [X5D §6](../5_X5D_EXPDB/X5D.md)

**X5D convergence and monotonicity.** The paper claimed the iteration would stabilize even without the code's truncation constants, and that every stage including $\theta$ is monotone. Without truncation the exponent-pair hull can keep gaining vertices; and the $\theta$ stage is not monotone in $A$ (see the next entry). Stabilization rests on the truncations and the finite pool of half-spaces. → [X5D §5](../5_X5D_EXPDB/X5D.md)

**"Replacing $\mathcal P$ by its convex hull leaves every bound unchanged" (X5D §4.9).** A section of $\mathrm{conv}(\mathcal P)$ at fixed $\sigma$ can be larger than the section of $\mathcal P$, so the rational supremum $\sup_\tau \rho/\tau$ can change. → [X5D §3](../5_X5D_EXPDB/X5D.md)

**The $\theta_{\mathrm{gap},2}$ refinement note.** Presented as improving the database's $\theta_{\mathrm{gap},2} \le \frac32$ to $\frac{33}{23}$. The arithmetic is right, but $\frac32$ is only the output of one route (Prop. 15.9); the database itself lists $\frac{23}{18}$ (Heath-Brown 1979) and $\frac{123}{100}$ (Stadlmann 2022), so $\frac{33}{23}$ is not a new bound. The note also defined $\theta_{\mathrm{gap},2}$ as the short-interval exponent (it is the second moment $\sum_{p_n\le x}(p_{n+1}-p_n)^2$); described $\alpha$ as increasing in $A$ (it decreases, which is why a weaker $A$ helps); and took $\lVert A\rVert_\infty = 2$ for the first term (with the envelope it is $\frac{30}{13}$, giving $\frac{17}{15}$). Now stated as an observation about the route. → [X5D §6.2](../5_X5D_EXPDB/X5D.md)

## Corrected

**PSD last digit: $p_n \ge 7$, not $p_n \ge 5$.** $(5, 7, 11)$ gives $\mathrm{PSD} = 8$, the sole counterexample below $5\times10^6$; the mod-5 step fails at $p = 5$. → [Twin Bertrand §2.4](../3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**Twin-slope ceiling proof.** The theorem holds (verified to $10^6$); the published general case concluded "$8/9 < 2/3$". The corrected bound is $\Delta x_{FS} \ge \frac{5g}{2} - 2$, giving $g/\Delta x_{FS} \le 2g/(5g-4) \le \frac23$. The twin-segment count is 8,168, not 8,169. → [Twin Bertrand §3.2](../3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**A circular table row.** The $Q = 1732$ row of the lag-1 surrogate table: over $[10^6, 3\times10^6)$ every integer coprime to all primes $\le 1732$ is prime (pool ratio 1.00). The conclusion stands on the $Q = 317$ row (pool ratio 1.39). → [Gap Correlations §3](../2_One_Wheel_Many_Shadows/Gap_Correlations.md)

**"68% of everything knowable."** Correct at $N = 10^4$ only; activation grows without bound, so the share drifts (59% at $10^6$). The stable statements are the template's 1.70 bits, 73.3% of positions removed free, and $\approx 0.84$ bits per open slot. → [The Factor Skyline §5](../1_Factor_Skyline/Factor_Skyline.md)

**The escape-ridge constant.** $4e^{-\gamma}$ applies Mertens where Buchstab's function governs; the measured ratio is 3.2 at $10^7$ and still falling. The order $N^{3/2}/\ln^2 N$ stands; the constant is marked heuristic. → [The Factor Skyline §6](../1_Factor_Skyline/Factor_Skyline.md)

**The pre-Guth–Maynard cusp.** The claim that it sat at $\sigma \approx 5/7$ with height $12/5$ is inconsistent: $A_{\mathrm{Ing}}(5/7) = 7/3$, and a peak of $12/5$ on Ingham's curve forces $\sigma = 3/4$ — the Ingham–Huxley crossing with $3/(3\sigma-1)$. → [X5D §6.1](../5_X5D_EXPDB/X5D.md)

**Rational supremum breakpoints.** Stated as rational; two degree-$(1,1)$ rational functions meet at roots of a quadratic, so the breakpoints are algebraic. → [X5D §3](../5_X5D_EXPDB/X5D.md)

**Upstream reproducibility stubs.** The Factor Skyline's original `reproducibility/tables/` scripts returned placeholder values; the entropy numbers were first re-derived by [`entropy_budget.py`](../1_Factor_Skyline/repro/entropy_budget.py).

---

How the earlier corrections were caught, in plain language: [How We Know](HOW_WE_KNOW.md).
