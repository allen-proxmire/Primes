# Worklog — September 2026

*A running list of routes, results, and dead ends. Not a paper. Started 2026-09-20 with Claude, poking at [PG_Balance_Ratio_And_Koide.md](../2_One_Wheel_Many_Shadows/PG_Balance_Ratio_And_Koide.md).*

> **This file is just the log** — what was tried, on what range, against what null, and what came out. **The keepers live in [NOTES_Carry_Forward.md](NOTES_Carry_Forward.md)**, one entry per durable finding, each tagged with the note it should eventually be folded into. If something here is worth remembering, it should have an N-number over there.

**House rules for this log**
- Every route gets a status: **open** / **running** / **done** / **dead**.
- Record the number, the range it was measured on, and the null it was measured against. A number without a null is not a result.
- Tags as elsewhere: **[fact]** exact · **[emp]** measured · **[approx]** · **[conj]** · **[interp]** reading.
- **Prior-art check before drafting, not after.** The collection is large enough to rediscover itself, and `Archive/` — discontinued repos kept as reference, not canon — is untracked, so an ordinary repo grep misses it. Run:
  `grep -rn -i "phrase" "Archive/Factor Skyline/modules/" "Archive/Factor Skyline/archive/" 1_Factor_Skyline/`
  See [`DERIVATION_MODULES.md`](../1_Factor_Skyline/DERIVATION_MODULES.md). This rule exists because 2026-09-20 cost a full draft.
- When a route turns into something worth keeping, it graduates to its own doc and gets linked from here.

---

## Status board

| # | route | status | one-line verdict |
|---|---|---|---|
| R1 | K reduces exactly to a gap form | **done** | Exact identity. K is the hexagonal norm of the gap pair. |
| R2 | The balance ratio's wheel signal is the known −0.05 | **done** | Predicted −0.719%, measured −0.708%. Inside null noise. |
| R3 | Residuals sorted mod 6 / mod 30 | **done** | Null result, and a clean one. No class exceeds 1.3σ. |
| R4 | The two prime angles share one driver | **open** | Both linear in g/p. Note currently implies otherwise. |
| R5 | The Budget is a payoff ledger with no cost column | **done** | Cost column exists and is *cheap*. My framing was backwards; see N6, N7. |
| R6 | Is the hexagonal norm meaningful or a coincidence? | **done** | **Meaningful.** 3 divides the form ⟺ three consecutive primes share a residue mod 6. |
| R7 | Is the +1.97pp windowed memory fully the wheel? | **done** | Yes. 99% at Q=100; Q=30 gives 76%, so the test has resolution. |
| — | "What picks Koide's midpoint?" | **parked** | Not our problem. Physics, and unresolved there. |

---

## R1 — K reduces exactly to a gap form · **done**

**Idea.** The note calls K "a gap measure in disguise." Make that exact.

**Result [fact].** For any three numbers a < b < c with gaps g1 = b−a, g2 = c−b and mean m = (a+b+c)/3:

> **K − 1/3 = (2/27) · (g1² + g1·g2 + g2²) / m²**

Verified as an exact rational identity (no floating point) on 2-3-5, 3-5-7, 5-7-11, 11-13-17, 101-103-107, 547-557-563, and the deliberately lopsided 7-100-1000. Exact in every case, including the lopsided one — so it is not a small-spread approximation, it is the thing itself.

**Notes.**
- This is strictly better than "squared relative spread" because it is written in gaps, which is the currency the rest of the folder trades in. It moves the balance ratio into the gap program instead of alongside it.
- g1² + g1·g2 + g2² is the **hexagonal norm** (the Loeschian form, the norm form of the Eisenstein integers). See R6.
- The cross-term g1·g2 is the only place prime-specific information can enter. That observation is what makes R2 work.

---

## R2 — The wheel signal in the balance ratio is the known −0.05 · **done**

**Idea.** The note asks whether the leftover, after detrending, carries the wheel's fingerprints. Because of R1 the answer is computable in advance: the mean of K−1/3 depends on the gaps only through E[g1² + g1·g2 + g2²], and the only term a gap-shuffle can change is the cross-term. So the shift from the null is **exactly cov(g_n, g_n+1)**. **Note (corrected later the same day): that is the definition of covariance, so this is a reduction, not a prediction** — it holds for any sequence, and the measurement below checks the arithmetic rather than testing a hypothesis.

**Test.** All 270,014 consecutive-prime gaps in [10^6, 5×10^6]. Mean gap 14.814, sd 12.292. Null = shuffle the gaps, then re-form the triples (the transform-matched null from the [Differencing Trap](../2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md)), 5 runs.

| quantity | value |
|---|---|
| E[g1² + g1·g2 + g2²], real primes | 953.633 |
| E[g1² + g1·g2 + g2²], gap-shuffled null | 960.436 (spread across 5 runs: 0.937) |
| **measured shift** | **−6.802  (−0.708%)** |
| cov(g_n, g_n+1) | −6.903  (corr −0.0457) |
| **predicted shift** | **−6.903  (−0.719%)** |

**Result [emp].** Predicted and measured agree to well inside the null's own run-to-run spread.

**Verdict.** The balance ratio does carry the wheel — and it is the *same* −0.05 consecutive-gap anti-correlation already established and fully attributed to the wheel in [PG_Angle_Wobble §4.1](../2_One_Wheel_Many_Shadows/PG_Angle_Wobble.md). **Not a new signal: a fifth shadow.** This is the deflationary, unifying shape the rest of the collection has.

**Notes.**
- Worth stating out loud when this is written up: K is a **level** statistic on the gaps, not a difference of them. The exact −1/2 differencing pedestal that ate 42 of the 44 points in the wobble **does not apply here at all.** The balance ratio is a cleaner instrument than Δg. It needs the gap-shuffle null and nothing more.
- This closes the note's open question with a matched prediction rather than an exploration, which is a stronger result than the note asked for.

---

## R3 — Residuals sorted mod 6 and mod 30 · **done**

**Idea (the note's own).** Sort the balance-ratio statistic by residue class mod 6 and mod 30, and see whether the leftover looks random or carries the wheel. Lemke Oliver–Soundararajan says the second is worth a look.

**Prediction registered before looking [conj].** Per the Budget's Tier-2 argument, the LOS bias is the wheel wearing another hat, so the residue-resolved values should also be reproduced by a wheel-only surrogate with no residual.

### The null had to be changed, and this is the methodological point of the route

The plan said "use the gap-shuffle null." **That null is wrong for a residue-resolved question, and I nearly ran it.** Shuffled gaps do not respect residue consistency — a gap of 4 cannot follow p ≡ 5 (mod 6), since 5+4 = 9 is divisible by 3 — so the shuffled triples are arithmetically *impossible*, and any per-class comparison against them is meaningless. The gap-shuffle is fine for the pooled question (R2) and breaks the moment you condition on residue.

**The correct null is generative, not a shuffle:** the wheel-only surrogate from [PG_Angle_Wobble §4.1](../2_One_Wheel_Many_Shadows/PG_Angle_Wobble.md) — keep integers coprime to every prime ≤ 317, thin independently to prime density, no other structure. It respects residues automatically because it is built from them.

*Filed as a rule for this log: a shuffle null is only valid where the shuffle preserves every hard constraint the statistic conditions on.*

**Test.** Real primes in [10^6, 5×10^6] (270,015 primes) against three surrogate seeds matched to the same density (thin-keep 0.6995). Statistic per triple: Q = g1² + g1·g2 + g2².

| class (p mod 6) | n | mean Q real | mean Q wheel | diff |
|---|---|---|---|---|
| 1 | 134,957 | 970.15 ± 3.30 | 964.67 (spread 9.52) | +0.57% |
| 5 | 135,056 | 937.13 ± 3.25 | 937.08 (spread 0.78) | +0.00% |

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

**Result [emp]. No class carries an excess.** Folding in the surrogate's own seed-to-seed uncertainty (which the ± columns above exclude), the largest deviation anywhere is **1.3σ** — the (1,1) pair — across 14 classes tested. Two or three readings near 1σ is what 14 comparisons produce by chance. **The prediction holds: the wheel accounts for the residue-resolved balance ratio with no detectable residual.**

Pooled, as a consistency check against R2: real mean Q 953.633, wheel surrogate 950.876, +0.29%; real cov(g1,g2) −6.903 against wheel −6.605, i.e. the surrogate reproduces **96%** of the covariance. That is the same conclusion as [PG_Angle_Wobble §4.1](../2_One_Wheel_Many_Shadows/PG_Angle_Wobble.md), reached through a different statistic.

### Power check — the instrument can detect things

A null result is worth nothing if the test is blind. So: does this setup see the LOS bias at all?

| pair (p, p′ mod 6) | real | wheel surrogate | even odds |
|---|---|---|---|
| (1, 1) | 21.48% | 21.58% | 25% |
| (1, 5) | 28.50% | 28.42% | 25% |
| (5, 1) | 28.50% | 28.42% | 25% |
| (5, 5) | 21.52% | 21.58% | 25% |

**The LOS residue-repetition bias is enormous and unmissable** — consecutive primes repeat their mod-6 residue 14% less often than even odds. The test sees it instantly. **And the wheel-only surrogate reproduces it to within 0.1 percentage point**, which is Budget Tier 2 confirmed on its own terms: LOS *is* the wheel.

So the instrument has plenty of power, it finds the known bias in the counts, and it finds nothing extra in Q.

**Verdict.** R3 closes the note's open question. Combined with R2: the balance ratio carries the wheel, the wheel carries all of it, and there is nothing underneath — pooled or per residue class. **The balance ratio is a fifth shadow, fully accounted for.**

---

## R4 — The two prime angles share one driver · **open**

**Idea.** The note says the prime-triangle 45° and Koide's 45° are "shared coordinates, not a shared cause." Correct about Koide. But it leaves the impression that the balance-ratio angle θ and the prime-triangle angle α are unrelated, and they are not — both are linear in g/p:

- prime-triangle: α → 45° **from below**, distance = (90/π)·g/p ≈ 28.6·g/p degrees
- balance-ratio: θ → 0° **from above**, size ≈ (27 to 47)·g/p degrees

**Where the range comes from [approx].** Small-spread expansion gives θ ≈ sqrt(2(g1² + g1·g2 + g2²)) / (3m) radians. The coefficient depends on the *shape* of the gap pair: equal gaps give ≈46.8·g/m degrees, maximally lopsided gives ≈27.0·g/m. Spot-checked against the note's own table — predicted 0.0328° vs tabulated 0.03° for 17393-17401-17417 (good); predicted 18.64° vs tabulated 18.02° for 5-7-11 (small-spread approximation straining, as expected at tiny p).

**The reading.** Same driver, opposite directions, because α measures one gap while θ measures the *asymmetry* of two. Koide is the genuine outsider. Worth a paragraph correcting the note.

**To do.** Verify the coefficient range properly instead of by two spot checks.

---

## R5 — The Budget has a payoff column and no cost column · **open**

**Idea.** This is where the note's generation-time half lands, and it may be the most original thing in the note.

[The Prime Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) is an honest ledger of **payoff**: the wheel is worth ≈1.70 bits of the ≈2.48-bit local uncertainty, ≈0.26 bits are irreducible escape, and you pin the next prime to ~7–8 candidates at 90%. It says the wheel kills 73–77% of positions **"for free, with no test."**

**That "for free" is doing work.** The wheel through Q is free only because you already know every prime up to Q. The new note's generation-time section is exactly the missing cost accounting:

| | grows like | what it is |
|---|---|---|
| the decided region | p_k² | how far the first k primes settle the line |
| the state describing the rule | p_1·p_2·…·p_k (primorial) | the wheel's period |

The territory decided grows **quadratically**; the state needed to describe the rule grows **exponentially**. To decide primality below x you need the wheel through sqrt(x), whose period is astronomically larger than x.

**The claim I went in with [wrong].** "The structure is cheap to *use* and exponentially expensive to *carry*, and that gap is where the apparent randomness lives."

**That is backwards, and the measurement says so.** The error was counting the *unrolled pattern* as the cost when the thing you actually carry is the *program*: the list of primes up to p_k. Three different scales were being collapsed into one word, "state."

### The three scales, measured

| | size | in p_k |
|---|---|---|
| **program** — bits to write the rule (= log2 of the primorial = Σ log2 p_i) | 1.4427 · p_k bits | **linear** |
| **territory** — integers the rule decides (everything below p_{k+1}²) | p_k² | **quadratic** |
| **period** — length of the unrolled pattern (the primorial itself) | 2^(1.4427 · p_k) | **exponential** |

The program slope converges to 1/ln2 = 1.4427 exactly as it must (θ(x) ~ x):

| p_k | program (bits) | program / p_k |
|---|---|---|
| 541 | 729.7 | 1.3489 |
| 7,919 | 11,270.7 | 1.4233 |
| 104,729 | 150,606.1 | 1.4381 |
| 611,953 | 881,836.2 | 1.4410 |
| 1,999,993 | 2,883,352.6 | 1.4417 |

**So the program is linear and the territory is quadratic — the wheel is a compression, and it gets better with scale.** Cost per decided integer is 1.4427/p_k bits and falls to zero:

| p_k | cost to learn one more prime | new integers thereby decided | integers per bit |
|---|---|---|---|
| 29 | 4.95 bits | 408 | 82 |
| 541 | 9.10 bits | 11,040 | 1,213 |
| 7,919 | 12.95 bits | 95,160 | 7,346 |
| 104,729 | 16.68 bits | 3,352,032 | 201,003 |
| 1,299,709 | 20.31 bits | 57,188,208 | 2,815,797 |

**Result [fact].** The return on the wheel grows without bound. The Budget's phrase "for free, with no test" is *more* defensible than I claimed, not less. There is no missing cost column in the sense I meant: the cost exists, it is tiny, and it shrinks.

### What survives, and it is the sharp part

The exponential scale is real — it is just not a *cost*. It is the **period**, and it has a consequence that is exact:

**The wheel's period exceeds the territory it decides, from p = 7 onward, forever.** [fact]

| k | p_k | primorial (period) | territory (p_{k+1}²) | |
|---|---|---|---|---|
| 1 | 2 | 2 | 9 | period < territory |
| 2 | 3 | 6 | 25 | period < territory |
| 3 | 5 | 30 | 49 | period < territory |
| **4** | **7** | **210** | **121** | **period > territory** |
| 5 | 11 | 2,310 | 169 | period > territory |
| 8 | 19 | 9,699,690 | 529 | period > territory |

After the crossover at p = 7 the gap never closes again — by p_k = 7,919 the period exceeds the territory by a factor of 2^11,245.

**So the wheel never completes a single period inside the region where it is the operative rule.** The pattern is always in its first period, always partial, never seen to repeat. That is a fully determined, cheaply described object that is *structurally incapable of looking periodic in its own domain of validity* — and that is a real mechanism for apparent randomness, stated exactly. It is the defensible core of the note's generation-time section.

**Verdict.** The note's intuition survives; its accounting does not. Not "expensive to carry" but **"cheap to carry, and it never repeats where you can see it."** Carried forward as N6 and N7.

**Still to do.**
- Check whether the three-scale framing is already somewhere in [Factor Skyline](../1_Factor_Skyline/) in other words.
- Decide: own note, or an appendix to the Budget. Leaning own note — the Budget is finished and this reframes rather than extends it.

---

## R6 — Hexagonal norm: meaningful or coincidence? · **open**

g1² + g1·g2 + g2² is the norm form of the triangular lattice / Eisenstein integers. The wheel's first real filter is mod 6, which is also hexagonal. Probably a coincidence — the form falls out of the algebra of three points on a line and has no obvious reason to know about mod 6 — but it is cheap to check whether the form's value distribution over real prime gaps differs from the null in a way that references 6. Low priority, filed so it is not lost.

---

## R6 — Is the hexagonal norm meaningful? · **done**

**Answer: meaningful, and exactly so.** Above p = 3 all gaps are even; with half-gaps h = g/2 the form is h1²+h1h2+h2² = (h1−h2)² + 3h1h2, so **3 divides the form ⟺ h1 ≡ h2 (mod 3) ⟺ g1 ≡ g2 (mod 6)**. Enumerating the eight residue transitions for p, p′, p″ ∈ {1,5} mod 6 shows the patterns (4,4) and (2,2) are impossible, so the *only* way to get g1 ≡ g2 mod 6 is both ≡ 0 — i.e. neither prime changed class. Hence:

> **3 divides the Eisenstein norm of the half-gap pair ⟺ three consecutive primes lie in the same class mod 6.** [fact]

**Measured** [10⁶, 5×10⁶]: P = 17.408%, against 18.492% for independent transitions and 12.500% for even odds. So repeats are strongly favoured over even odds (LOS) *and* mildly anti-cluster with each other.

**Wheel surrogate** (pool ratios per N8): 17.457% at Q=30, 17.400% at Q=100, 17.465% at Q=317, 17.512% at Q=600. Fully reproduced at every depth, including a very shallow one — as expected once the effect is known to be a mod-6 statement.

**Verdict.** The prettiest thing found today, and still not new physics: the form's one arithmetic invariant is a doubled LOS event, and the rate is the wheel. Filed into [the balance-ratio paper §2.1](../2_One_Wheel_Many_Shadows/PG_Balance_Ratio_And_Koide.md).

---

## R7 — Is the windowed memory fully the wheel? · **done**

**Idea.** [Angle Wobble §4.1](../2_One_Wheel_Many_Shadows/PG_Angle_Wobble.md) verified the *lag-1* covariance is 100% wheel. The [Differencing Trap](../2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md) left the *windowed* +1.97pp at "plausibly the wheel." Nobody had run §4.1's test on the windowed statistic. **The one open route today whose answer I did not know in advance.**

**Method.** For real primes and for wheel-only surrogates at several depths Q, compute the excess of each series *against its own matched null*: R2(diff(g)) − R2(diff(shuffle(g))). Compare excesses. Real primes [10^6, 5×10^6], three seeds per Q, four shuffles per series.

| Q | pool | pool/π(x) | excess | share of real | |
|---|---|---|---|---|---|
| 30 | 631,801 | 2.34 | +1.496 pp | 76.0% | power check |
| **100** | **481,525** | **1.78** | **+1.950 pp** | **99.0%** | |
| 200 | 418,982 | 1.55 | +1.916 pp | 97.3% | |
| 317 | 386,014 | 1.43 | +1.803 pp | 91.6% | |
| 600 | 342,150 | 1.27 | +1.936 pp | 98.3% | borderline |
| 1000 | 305,298 | 1.13 | +2.021 pp | 102.7% | **circular** |
| 1732 | 274,556 | 1.02 | +1.948 pp | 98.9% | **circular** |

Real: +1.969 pp. Seed-to-seed scatter ≈0.13 pp (≈±6% of the excess).

**Result [emp].** From Q = 100 the wheel reproduces the excess within noise. The 91.6–102.7% spread across Q is consistent with seed scatter alone — no trend, no residual. Q = 30 reaching only 76% shows the test can detect a shortfall.

**Verdict.** The windowed memory is the wheel, in full. **Both** surviving lines of gap memory are now attributed with nothing left over.

**The methodological catch, and the reason for the pool column.** My first run used only Q = 317 and Q = 1732 and read the Q = 1732 row (99.9%) as the answer. **It is circular.** An integer below 5×10^6 coprime to every prime ≤ 1732 is prime, or one of a thin sliver of semiprimes — at that depth the surrogate pool is 1.7% larger than π(x), so the "wheel model" *is* the primes. Sweeping Q and printing the pool ratio is what exposed it. Carried forward as N8.

*(The first run also showed a +2.1 sd residual at Q = 317 that vanished on the sweep — 5 seeds gave 93.9%, 3 seeds gave 91.6%. Noise. Worth remembering before calling 2 sd a finding.)*

---

## Running log

**2026-09-20** — Read the new note plus [PG_Angle_Wobble](../2_One_Wheel_Many_Shadows/PG_Angle_Wobble.md), [Differencing Trap](../2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md), [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md). Opened R1–R6.

R1, R2, R3 all closed the same day, and they close in the same direction: **the balance ratio is the wheel, entirely.** R1 made it an exact gap identity, R2 predicted the pooled wheel signal to within the null's own noise, R3 found nothing left over in any residue class while demonstrating the test could see LOS.

R3 also produced the one genuinely transferable thing so far — the null had to be swapped, because a gap-shuffle produces arithmetically impossible triples once you condition on residue. That rule (a shuffle null is only valid where it preserves every hard constraint the statistic conditions on) is a sharpening of the [Differencing Trap](../2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md) discipline and probably belongs in that note rather than here.

Then ran R5 the same day. It did produce something new — but by **refuting the premise I opened it with**, not by confirming it. The claim "structure is cheap to use and expensive to carry" is backwards: the program is linear, the territory quadratic, so the wheel is a compression that improves with scale, and the Budget's "for free" survives intact. What survives from the note's generation-time section is sharper than what I was chasing — the period overtakes the territory at p = 7 and never comes back, so the wheel is never seen to repeat inside its own domain. Logged as N6, with the wrong version preserved as N7 so it does not get re-derived.

Set up [NOTES_Carry_Forward.md](NOTES_Carry_Forward.md) and moved the keepers there (N1–N7). This file is the log from here on.

Remaining open: R4 (verify the angle coefficient range), R6 (hexagonal norm, charm only), and N6's placement — own note or Budget appendix.

Then wrote five documents filing N1–N7 (all new files; originals untouched), and verified N5's coefficient before filing — **the "27 to 47" range recorded earlier was wrong**, mixed normalizations; correct range 46.78–54.02, measured median 48.01 over 70,433 triples.

**Finally ran the prior-art check on N6 — and it failed.** [`FS_primorial_epochs` §2.2](../1_Factor_Skyline/FS_primorial_epochs.md), in the Archive, already has the period-outgrows-the-window result with a "periods per epoch" table and the same reading, measured against the **activation epoch** rather than cumulative territory — the better denominator, crossover at p = 5 rather than p = 7. And [`FSPapers_02.1` §13.2–13.3](../1_Factor_Skyline/FSPapers_02.1_correlations_and_randomness.md) already has the cheap-rule/random-output gap in the stronger form K = O(log N) vs H ~ 0.26N, under the heading "the randomness paradox resolved."

So the drafted note was a restatement, and it was **deleted** the same day. The dependent sections in [Budget §5](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) and [balance ratio §8](../2_One_Wheel_Many_Shadows/PG_Balance_Ratio_And_Koide.md) were rewritten to cite the Factor Skyline papers instead. [`FS_primorial_epochs.md`](../1_Factor_Skyline/FS_primorial_epochs.md) was promoted out of the untracked Archive into the curated collection, and [`DERIVATION_MODULES.md`](../1_Factor_Skyline/DERIVATION_MODULES.md) written to index the other 17 upstream modules so the next grep finds them.

**Lesson, and it is the useful output of the day:** run the prior-art check against your own collection *before* drafting. The check cost one search; the note cost a draft. The collection is now large enough that "is this already written down here?" is a real question — the thing rediscovered was in the Archive, not in the active folders.

**Then ran R7**, the one question whose answer I did not know going in — and it came back the same way as everything else: the wheel, in full. The +1.97pp windowed memory is now measured rather than presumed, which closes the Differencing Trap's last loose end. Two process catches on the way: a circular surrogate at deep Q (N8), and a 2-sd "residual" that evaporated when swept properly.

Also corrected the balance-ratio paper's §5 framing across four documents. It had been written up as "predicted in advance and confirmed"; the agreement is forced by the definition of covariance, so it is a *reduction* (the statistic is redundant), not a prediction. The measurement checks arithmetic, not a hypothesis.

**Then R6**, which had been parked as "low priority, high charm." It turned out to be the one genuinely pretty result of the day: the hexagonal form's divisibility by 3 is *exactly* the event that three consecutive primes share a residue mod 6. Not a pun — an equivalence, provable in two lines. The rate is, of course, the wheel.

**Day's tally: eight statistics, one mechanism, no residual anywhere.**

**2026-09-20, later.** Answered a direct question — *four wheels, 90%, how many slots by decade?* — and it turned into the session's cleanest result plus two bug fixes.

The measurement went wrong first: a fixed 1.5M-wide window at every decade meant the $10^4$ row spanned to 1.5 million. The user's own expectation caught it. Redone over $[N, 2N]$, the counts are 3, 4, 5, 7, 8, 9, 10, 11 from $10^3$ to $10^{10}$ — and $k = \lceil \ln(0.1)/\ln(1-q)\rceil$ with $q = 210/(48\ln N)$ reproduces every one of them with nothing fitted. Written up as [The Ninety Percent Rule](../4_Philosophy_Ontology/The_Ninety_Percent_Rule.md), logged as N14, cross-referenced from the Budget, The Movie, What We Found and RESULTS. The Budget's “~7–8 candidates” had been a single-scale number reading as a constant; it now says so.

The prettier half is the corollary: carrying more wheels cuts the slots you test but leaves the *road* fixed at $2.303\ln N$ numbers, because the open fraction cancels. The wheel never moves the prime.

Then N15, found while sweeping for something else: five **invisible control bytes** had shipped in tracked markdown — `\approx` and `\arctan` written through a non-raw Python string, where `\a` becomes BEL rather than a dropped backslash. Invisible in a diff. Third appearance of this bug class in one session, so it is now a check rather than a memory: [`check_repo_health.py`](check_repo_health.py), which also covers broken links and the `.gitignore`-allowlist trap. It found a fourth problem on its first run (a figure README linking into the untracked Archive) and **two bugs in itself** — Windows backslash paths and git's space-quoting silently made the ignore check pass on everything — before coming back clean.

**2026-09-21.** Allen proposed a look-back heuristic: read the wobble of the last few primes and guess which way the next angle turns. Tested it directly. Direction is the differencing artifact (68.6% real vs 69.2% shuffled). Size carries a real sliver (0.18 slots), which is **zero** against four-wheel fakes and recovered to ~85% by fakes sieved to 300–700; the rest sits in the circular pool-ratio-to-1 zone and is left open. Filed as a “Looking back” section in The Ninety Percent Rule with [`lookback_test.py`](../4_Philosophy_Ontology/repro/lookback_test.py), logged as N16.

Process note: the numbers quoted in conversation shifted slightly when the test was rewritten as a script (the big/small split moved from the median of the *next* gap to the median of the *last* gap, which is the right one). The 11 and 13 rows moved most, 24%→13% and 34%→23%. The conclusion didn't change. The note carries the script's numbers.

**2026-09-21, later.** Closed N16's open 15%. Two tries. (1) Exact expectation instead of simulated fakes — real starting primes, wheels to y, coin flips for survivors: 82% at y = 100, 89% at 300, but it still climbs as the coin density goes to 1, so the same circularity in milder form. (2) Group the real walks by the wheel-struck pattern of the next 12 open slots and compare big vs small last gap within groups — no fakes, no chosen density. On [10⁷, 2×10⁷]: leftover **−0.001 ± 0.006** at y = 300 with the in-group spread still 2.56 of 3.11. The sliver is the wheel. Filed in The Ninety Percent Rule and as `lookback_test.py` part 4.

**Method lesson:** when a generative null goes circular as it approaches the real thing, stop generating. Condition the *real* data on the structure instead, and show with a spread column that the conditioning hasn't reconstructed the answer.

Scratch code lives outside the repo.
