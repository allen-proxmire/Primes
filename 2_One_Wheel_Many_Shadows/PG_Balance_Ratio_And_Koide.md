# The balance ratio: consecutive primes, and where Koide sits

### v2 — the open question is closed: the balance ratio is the wheel's fifth shadow

*Written 2026-09-18 with Claude, from Allen's Copilot exchange. Revised 2026-09-20 after the measurements the v1 draft called for. Everything below is checked arithmetic, measured against a stated null, or a standard result; the honest verdict is at the end.*

> **What changed in v2.** v1 ended with a "measurable question" — detrend the balance ratio and look for the wheel in the residuals. That question has now been run, and the answer is complete: the statistic reduces to an **exact gap identity** (§2), its deviation from a matched null **reduces exactly to the consecutive-gap covariance**, so the statistic is redundant (§5), and **no residue class carries an excess** (§6). The balance ratio is not a new signal. It is a **fifth shadow of the wheel**, fully accounted for. v1's §"Generation time" also had its accounting backwards; §8 corrects it, and what survives is sharper than what it replaced. Tags: **[fact]** exact · **[emp]** measured · **[approx]** · **[interp]** reading.

---

## 1. The quantity

For three positive numbers a, b, c:

> **K = (a² + b² + c²) / (a + b + c)²**, and its inverse **1/K = (a + b + c)² / (a² + b² + c²)**

Applied to consecutive primes p₁, p₂, p₃, it's the ratio that drifts toward 1/3 (inverse 3).

Koide's relation is **the same quantity applied to the square roots of the lepton masses:**

> **Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² ≈ 2/3**

So if the primes play the role of the square roots of masses, the two live on the same scale. That's why they're comparable at all.

## 2. What K is, exactly: the gap identity

v1 established that K is a spread measure. The sharper statement is that it is a **gap** statistic, written in the currency the rest of this collection trades in. For any three numbers a < b < c with gaps g₁ = b−a, g₂ = c−b and mean m = (a+b+c)/3:

> **K − 1/3 = (2/27) · (g₁² + g₁g₂ + g₂²) / m²**   **[fact]**

**Checked as an exact rational identity** — not a small-spread approximation. Verified on 2-3-5, 3-5-7, 5-7-11, 11-13-17, 101-103-107, 547-557-563, and on the deliberately lopsided 7-100-1000, where it also holds exactly.

The older form is the first-order shadow of this one: writing the three numbers as a mean times (1 + εᵢ) with the εᵢ summing to zero gives K = 1/3 + (ε₁² + ε₂² + ε₃²)/9, and the identity above is what that becomes once the εᵢ are resolved into gaps.

Three consequences, and the third is the one that does all the work later:

- **K knows nothing about primality.** Any three numbers that get relatively closer together march toward 1/3.
- **The quadratic form g₁² + g₁g₂ + g₂² is the Loeschian form** — the norm form of the Eisenstein integers, the quadratic form of the triangular lattice. The wheel's first real filter is mod 6, also hexagonal. *Whether that is a connection or a pun is open, and nothing in this note rests on it.*
- **The cross-term g₁g₂ is the only place prime-specific information can enter.** Squares of gaps are blind to ordering; a product of *consecutive* gaps is not. This is what lets §5 reduce the whole statistic to a single known quantity.

## 3. The geometric reading (why 45° turns up)

Put the three numbers in a vector and compare it with the "all equal" direction (1, 1, 1). Then

> **cos²θ = 1 / (3K)**

| K | 1/K | angle to the all-equal direction | meaning |
|---|---|---|---|
| **1/3** | 3 | 0° | all three equal |
| **2/3** | 1.5 | **45°** | **Koide** |
| **1** | 1 | 54.7356° | one number is everything |

- **Koide's 2/3 is exactly the 45° condition,** and it sits at the midpoint of K's allowed range [1/3, 1].
- **With measured lepton masses:** Q = 0.666661 and the angle is **44.9997°**.

## 4. Consecutive primes, computed

| triple | K | 1/K | 3 − 1/K | Σ(relative deviation)² | angle |
|---|---|---|---|---|---|
| 2, 3, 5 | 0.380000 | 2.63158 | 0.368421 | 0.420000 | 20.51° |
| 3, 5, 7 | 0.368889 | 2.71084 | 0.289157 | 0.320000 | 18.09° |
| 5, 7, 11 | 0.368620 | 2.71282 | 0.287179 | 0.317580 | 18.02° |
| 11, 13, 17 | 0.344438 | 2.90328 | 0.096718 | 0.099941 | 10.34° |
| 17, 19, 23 | 0.338696 | 2.95250 | 0.047498 | 0.048262 | 7.23° |
| 101, 103, 107 | 0.333526 | 2.99826 | 0.001736 | 0.001737 | 1.38° |
| 547, 557, 563 | 0.333380 | 2.99958 | 0.000423 | 0.000423 | 0.68° |
| 3581, 3583, 3593 | 0.333334 | 2.99999 | 0.000006 | 0.000006 | 0.08° |
| 17393, 17401, 17417 | 0.333333 | 3.00000 | 0.000001 | 0.000001 | 0.03° |

**The approach to 3 is set by the gaps**, exactly as §2 requires: the distance from 3 is the Loeschian form over m², so it falls like (gap/p)², which is roughly (ln p / p)². At p ≈ 101 that predicts about 0.002, and the table shows 0.0017.

**So the drift toward 1/3 is guaranteed and carries no information.** Everything of interest is in the deviation from a matched null — which is what §5 and §6 measure.

## 5. The statistic is redundant: it reduces to the gap covariance

**The reduction, and it is algebra, not evidence.** By §2 the mean of K − 1/3 depends on the gaps only through E[g₁² + g₁g₂ + g₂²]. A gap-shuffle preserves the multiset of gaps, so it leaves the two square terms untouched and can move only the cross-term. Under the shuffle the two gaps are independent, so E[g₁g₂] becomes E[g]². Therefore

> shift = E[g₁g₂] − E[g]² = **cov(gₙ, gₙ₊₁)**,

**which is the definition of covariance.** This is not a prediction about primes — it holds for any sequence whatever, including random data. It is a *reduction*: it says the balance ratio carries **no information beyond the consecutive-gap covariance**, and therefore that mining it further is pointless.

*(An earlier draft of this section presented the agreement below as "predicted in advance and confirmed." That was an overstatement — the agreement is forced by the algebra, and the measurement below verifies the arithmetic and the negligibility of finite-sample effects, not a hypothesis about primes.)*

**The check.** All 270,014 consecutive-prime gaps in [10⁶, 5×10⁶] (mean gap 14.814, sd 12.292). Null = shuffle the gaps, **then** re-form the triples — the transform-matched null of [*Prime-Gap Memory and the Differencing Trap*](Prime_Gap_Memory_Differencing_Trap.md). Five runs.

| quantity | value |
|---|---|
| E[g₁² + g₁g₂ + g₂²], real primes | 953.633 |
| E[g₁² + g₁g₂ + g₂²], gap-shuffled null | 960.436 (spread across 5 runs: 0.937) |
| **measured shift** | **−6.802  (−0.708%)** |
| cov(gₙ, gₙ₊₁) | −6.903  (corr −0.0457) |
| **shift forced by the algebra** | **−6.903  (−0.719%)** |

**[emp]** Measurement and algebra agree well inside the null's own run-to-run spread — confirming the computation, as expected.

**What this identifies.** The −0.0457 is the **consecutive-gap anti-correlation** already established and *fully* attributed to the wheel in [*The Prime-Triangle Angle* §4.1](PG_Angle_Wobble.md), where a wheel-only surrogate reproduces it with no detectable residual. So the balance ratio's entire deviation from chance is a quantity this collection had already measured and explained, arriving in new clothes.

### 5.1 A note in the balance ratio's favour

Worth saying plainly, because this collection has been burned in the neighbourhood. **K is a *level* statistic on the gaps, not a difference of them.** The exact corr = −1/2 differencing artifact — the pedestal that accounted for 42 of the 44 apparent points of predictability in the windowed wobble — **has no analogue here at all.** K needs a gap-shuffle null (pooled) or a wheel surrogate (per class), and nothing beyond that. It is a cleaner instrument than Δg.

## 6. Residue classes: nothing left over

§5 settles the pooled question. The sharper one is whether any *residue class* carries an excess that the single covariance number misses — the Lemke Oliver–Soundararajan biases make this worth asking rather than assuming.

**The null had to change, and that is a methodological point in its own right.** A gap-shuffle is invalid the moment you condition on residue: shuffled gaps do not respect residue consistency — a gap of 4 cannot follow p ≡ 5 (mod 6), since 5 + 4 = 9 is divisible by 3 — so the shuffled triples are arithmetically **impossible** and the per-class comparison has no referent. The null must become **generative rather than permutational**: the wheel-only surrogate of [§4.1](PG_Angle_Wobble.md), keeping integers coprime to every prime ≤ 317 and thinning independently to prime density. It respects residues because it is built from them. *(This rule is developed in [the Differencing Trap note, §8](Prime_Gap_Memory_Differencing_Trap.md).)*

Real primes in [10⁶, 5×10⁶] against three surrogate seeds, statistic Q = g₁² + g₁g₂ + g₂²:

| class (p mod 6) | n | mean Q real | mean Q wheel | diff |
|---|---|---|---|---|
| 1 | 134,957 | 970.15 ± 3.30 | 964.67 | +0.57% |
| 5 | 135,056 | 937.13 ± 3.25 | 937.08 | +0.00% |

| class (p mod 30) | n | mean Q real | mean Q wheel | diff |
|---|---|---|---|---|
| 1 | 33,714 | 974.51 ± 6.59 | 966.39 | +0.84% |
| 7 | 33,767 | 898.10 ± 6.47 | 892.39 | +0.64% |
| 11 | 33,731 | 899.25 ± 6.36 | 901.60 | −0.26% |
| 13 | 33,787 | 990.32 ± 6.72 | 983.91 | +0.65% |
| 17 | 33,790 | 939.54 ± 6.42 | 942.88 | −0.35% |
| 19 | 33,689 | 1017.79 ± 6.63 | 1016.13 | +0.16% |
| 23 | 33,763 | 994.21 ± 6.60 | 993.90 | +0.03% |
| 29 | 33,772 | 915.47 ± 6.61 | 909.90 | +0.61% |

| LOS pair (p, p′ mod 6) | n | mean Q real | mean Q wheel | diff |
|---|---|---|---|---|
| (1, 1) | 58,006 | 1038.67 ± 5.22 | 1029.20 | +0.92% |
| (1, 5) | 76,951 | 918.51 ± 4.24 | 915.66 | +0.31% |
| (5, 1) | 76,951 | 891.16 ± 4.19 | 890.54 | +0.07% |
| (5, 5) | 58,105 | 998.00 ± 5.12 | 998.37 | −0.04% |

**[emp] No class carries an excess.** Folding in the surrogate's own seed-to-seed uncertainty (which the ± columns exclude), the largest deviation across all 14 classes is **1.3σ**. Two or three readings near 1σ is what 14 comparisons produce by chance.

### 6.1 The test is not blind

A null result is worth nothing without a demonstration of power. Does this setup see a known bias?

| pair (p, p′ mod 6) | real | wheel surrogate | even odds |
|---|---|---|---|
| (1, 1) | 21.48% | 21.58% | 25% |
| (1, 5) | 28.50% | 28.42% | 25% |
| (5, 1) | 28.50% | 28.42% | 25% |
| (5, 5) | 21.52% | 21.58% | 25% |

**The Lemke Oliver–Soundararajan residue-repetition bias is enormous and unmissable** — consecutive primes repeat their mod-6 residue 14% less often than even odds — and the test finds it instantly. **The wheel-only surrogate reproduces it to within 0.1 percentage point.** So: the instrument has ample power, it sees the known bias in the counts, and it finds nothing extra in the balance ratio.

As a further consistency check, the surrogate reproduces 96% of the consecutive-gap covariance (−6.605 against the real −6.903) — the same conclusion as [§4.1](PG_Angle_Wobble.md), reached through a different statistic.

## 7. Two 45°s that are unrelated, and two prime angles that are not

v1 said the prime-triangle 45° and Koide's 45° are "shared coordinates, not a shared cause." **That verdict on Koide stands.** But it left the wrong impression about the two *prime* angles, which are not independent of each other — both are linear in gap/p:

- **prime-triangle angle:** α → 45° **from below**, with 45° − α = (90/π)·g/p ≈ **28.65 · g/p** degrees
- **balance-ratio angle:** θ → 0° **from above**, with θ ≈ **(46.78 to 54.02) · ḡ/m** degrees, where ḡ = (g₁+g₂)/2

**[approx, verified]** The coefficient range is exact algebra: writing s = g₁+g₂ and d = g₁−g₂, the Loeschian form is (3s² + d²)/4, so the coefficient runs from 46.78 at equal gaps (d = 0) to 54.02 in the limit of one vanishing gap (d/s → 1). Measured against exact θ = arccos(1/√(3K)) on 70,433 real triples near 10⁶: **min 46.78, median 48.01, max 53.62** — bracketed by the algebra, and tight to about ±7%.

**So θ ≈ 48 · ḡ/p degrees.** Same driver as α, opposite direction, and the only reason the coefficients differ is that α measures **one** gap while θ measures the **asymmetry of two**.

Koide remains the genuine outsider: the primes head to the "nothing distinguishes them" corner (θ → 0), while the leptons sit far from it at 45°.

## 8. Generation time — corrected

*v1's framing: the wheel is the state, the verdicts are the events. The dynamical reading survives; the accounting in v1 was wrong and is replaced here.*

**What survives unchanged.** An ordering alone isn't a dynamics — "13 after 11" says nothing about 11 causing 13. Dynamics needs the current state to constrain what comes next, and the sieve has that:

| | in the sieve | what it is |
|---|---|---|
| **State at step k** | The surviving pattern of residues modulo p₁p₂…p_k | The wheel |
| **Event** | The next prime: the smallest survivor above 1 | A verdict, not a number coming into being |
| **Update** | Switching that prime on refines the wheel to the next primorial | The wheel turns over |

Also unchanged: **it's the verdicts that arrive, not the numbers** (every integer is an address as soon as you can count to it), and **the sieve's time sits outside the integers** — the number line doesn't grow, only the annotation does.

**What was wrong.** v1 said the decided region grows quadratically "while the state needed to describe the rule explodes," and read that gap as the home of the apparent randomness. **Three different things were collapsed into the word "state," and they scale differently:**

| | size | in p_k |
|---|---|---|
| **program** — bits to write the rule (= Σ log₂ pᵢ = log₂ of the primorial) | 1.4427 · p_k | **linear** |
| **territory** — integers the rule decides (everything below p²_{k+1}) | p_k² | **quadratic** |
| **period** — length of the unrolled pattern (the primorial itself) | 2^(1.4427 · p_k) | **exponential** |

**[fact]** The program slope converges to 1/ln 2 = 1.4427, as θ(x) ~ x requires: measured 1.3489 at p_k = 541, 1.4233 at 7,919, 1.4417 at 2×10⁶.

**The thing you carry is the program, not the unrolled pattern** — and the program is *linear* while the territory it decides is *quadratic*. So cost per decided integer is 1.4427/p_k bits and **falls to zero**; the wheel is a compression that improves with scale. The correct verdict is the opposite of v1's: **the wheel is cheap to carry, and gets cheaper.** The "for free, with no test" of [*The Prime Prediction Budget*](Prime_Prediction_Budget.md) is vindicated, not challenged.

**What survives, and it is sharper.** The exponential scale is real — it is simply not a *cost*. It is the **period**, and it has an exact consequence:

> **From p = 7 onward, forever, the wheel's period exceeds the territory it decides.** **[fact]**

Crossover is at k = 4: primorial 210 against territory 121. The gap never closes again — by p_k = 7,919 the period exceeds the territory by a factor of 2^11,245.

**So the wheel is never seen to complete a single period inside the window where it is the operative rule.** It is always partial, never observed to repeat: a fully determined, cheaply described object that is *structurally incapable of looking periodic in its own domain of validity*. That is what v1's generation-time section was reaching for.

**It is also, as a prior-art check established on 2026-09-20, already in this collection** — stated earlier, and with a better-chosen comparison. [`FS_primorial_epochs` §2.2](../Archive/Factor%20Skyline/modules/FS_primorial_epochs.md) measures the primorial period against the **activation epoch** [p_k², p²_{k+1}), the window in which the coverage configuration is genuinely frozen — the right denominator — and concludes that from p ≥ 5 "the full primorial structure is never 'seen' within a single epoch… the coverage pattern's period outgrows the epoch length." Separately, [`FSPapers_02.1` §13.2–13.3](../1_Factor_Skyline/FSPapers_02.1_correlations_and_randomness.md) gives the cheap-rule/random-output gap in a stronger form — Kolmogorov complexity K = O(log N) against entropy H ~ 0.26N — under the heading "the randomness paradox resolved."

**So §8's correction to v1 stands, but none of its content is new to the collection.** Cite the Factor Skyline papers here; do not re-derive them.

## 9. The verdict

**What's real:**
- The identity K − 1/3 = (2/27)(g₁² + g₁g₂ + g₂²)/m², exact.
- Koide's 2/3 is the 45° condition, and the midpoint of the possible range.
- Consecutive primes march to the equality end (1/3, inverse 3), and the rate is governed by the gaps.
- **The balance ratio's entire deviation from a matched null reduces, by algebra, to the wheel's consecutive-gap anti-correlation** — and no residue class carries an excess beyond it.

**What isn't:**
- **There's no prime–lepton connection here.** The primes head to the "nothing distinguishes them" corner; the leptons sit far from it, at 45°.
- **"2/3 is twice 1/3" isn't the meaningful fact.** The meaningful facts are the range [1/3, 1], the midpoint, and the angle.
- **The balance ratio is not a new prime signal, and is not independent evidence for one.** It is the consecutive-gap covariance in other clothes; §5 is a redundancy proof, and §6 confirms the redundancy holds class by class.

**The question worth keeping,** in Copilot's framing and sharpened:
> 1/3 is where three quantities land when nothing distinguishes them. The leptons sit exactly halfway between that and "only one of them exists." **What picks the midpoint?**

**Caveats on Koide:** it holds to about one part in 10⁵ with measured pole masses and has no accepted explanation; masses run with energy scale, and the relation is not as clean at other scales, so whether 2/3 is fundamental is open.

**Still open here:** whether the Loeschian/hexagonal form of §2 connects to the wheel's mod-6 filter or is a coincidence. Probably a coincidence — the form falls out of the algebra of three points on a line and has no obvious reason to know about 6 — but it is untested.

---

## Checked

| claim | how |
|---|---|
| The identity of §2 | Exact rational arithmetic, 2026-09-20; 7 triples including the lopsided 7-100-1000 |
| The v1 table | Computed 2026-09-18 (sieve to 20,000) |
| Koide's value and angle | Pole masses m_e = 0.51099895, m_μ = 105.6583755, m_τ = 1776.86 MeV: Q = 0.666661, angle 44.9997° |
| Range and geometry | cos²θ = 1/(3K); K = 1/3 at equality, 1 at full concentration (54.7356°) |
| §5 reduction and check | 270,014 gaps in [10⁶, 5×10⁶]; gap-shuffle null, 5 runs |
| §6 residue classes | Same range; wheel-only surrogate (coprime to primes ≤ 317, thinned to matched density), 3 seeds |
| §7 coefficient range | Exact algebra via (3s²+d²)/4; checked against exact θ on 70,433 triples near 10⁶ |
| §8 three scales | Program slope over primes to 2×10⁶; crossover by exact primorial arithmetic |

## References

- A. Proxmire, *The Prime-Triangle Angle* (this collection) — the α angle, and §4.1's wheel-only surrogate.
- A. Proxmire, *Prime-Gap Memory and the Differencing Trap* (this collection) — the transform-matched null, and §8's rule on when a shuffle null is valid.
- A. Proxmire, *The Prime Prediction Budget* (this collection) — the payoff ledger vindicated in §8.
- A. Proxmire, *Primorial Epochs and the Tiling Structure of the Factor Skyline* §2.2 (this collection, Archive) — the period-outgrows-the-epoch result §8 rediscovered.
- A. Proxmire, *FS Papers 02.1: Correlations and Randomness* §13.2–13.3 (this collection) — K = O(log N) against H ~ 0.26N; the randomness paradox.
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes* (PNAS, 2016).
- Y. Koide, *A fermion-boson composite model of quarks and leptons* (Phys. Lett. B, 1983).
