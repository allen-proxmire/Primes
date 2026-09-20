# Carry-forward notes

*Durable findings and general rules that came out of the September 2026 work, each with the note it lives in. The blow-by-blow of how each was found is in [WORKLOG_2026-09.md](WORKLOG_2026-09.md) — this file is only the keepers.*

**Status key:** **FILED** = written into a v2 · **file it** = ready, not yet placed · **needs work** = right idea, still owes a check · **correction** = fixes something currently written down.

> **2026-09-20: N1–N7 are all filed.** Five documents written, all new files — the originals are untouched:
> | document | holds |
> |---|---|
> | [PG_Balance_Ratio_And_Koide.md](PG_Balance_Ratio_And_Koide.md) | N2, N3, N4, N5, N6/N7 (§8) |
> | [Prime_Gap_Memory_Differencing_Trap.md](Prime_Gap_Memory_Differencing_Trap.md) | N1 (new §8) |
> | [PG_Angle_Wobble.md](PG_Angle_Wobble.md) | N3 as the fifth shadow (new §5.1) |
> | [Prime_Prediction_Budget.md](Prime_Prediction_Budget.md) | N7 (new §5), balance ratio added to the Tier-2 table |

---

## N1 — When a shuffle null is valid · **FILED** (new §8) · → [Prime_Gap_Memory_Differencing_Trap.md](Prime_Gap_Memory_Differencing_Trap.md)

> **A shuffle null is only valid where the shuffle preserves every hard constraint the statistic conditions on.**

The Differencing Trap note already establishes *which* thing to shuffle (gaps vs changes) and that the transform must be applied after the shuffle. This adds the next layer: even the correct shuffle becomes invalid once you condition on something the shuffle destroys.

**The concrete case.** Sorting a gap statistic by residue class and comparing against gap-shuffled primes is meaningless, because shuffled gaps do not respect residue consistency — a gap of 4 cannot follow p ≡ 5 (mod 6), since 5 + 4 = 9 is divisible by 3. The shuffled triples are arithmetically *impossible*, so the per-class comparison has no referent.

**The fix.** When the shuffle breaks a hard constraint, the null must become **generative rather than permutational** — build a surrogate that satisfies the constraint by construction. Here that is the wheel-only surrogate of [PG_Angle_Wobble §4.1](PG_Angle_Wobble.md): integers coprime to all primes ≤ Q, thinned independently to prime density.

**Why it matters for the collection.** The Differencing Trap's lesson is "match the null to the layer." This is the sharper form: *the null must be able to produce the data.* A null that generates impossible configurations will credit arithmetic necessity to the primes.

---

## N2 — The balance ratio is exactly the hexagonal norm of the gap pair · **FILED** (§2) · → [PG_Balance_Ratio_And_Koide.md](PG_Balance_Ratio_And_Koide.md)

For any three numbers a < b < c with gaps g1 = b−a, g2 = c−b and mean m = (a+b+c)/3:

> **K − 1/3 = (2/27) · (g1² + g1·g2 + g2²) / m²**

Exact, verified as a rational identity — not a small-spread approximation. Holds on the lopsided 7-100-1000 as well as on prime triples.

This replaces the note's "K is a spread measure" with something stronger and better aimed: K is a statistic **in the gaps**, which is the currency the rest of the folder trades in. The cross-term g1·g2 is the only place prime-specific information can enter, and that fact is what makes N3 predictable in advance.

*(g1² + g1·g2 + g2² is the Loeschian form — the norm form of the Eisenstein integers, the quadratic form of the triangular lattice. Whether that connects to the wheel's mod-6 filter or is a pun is open; see R6 in the worklog. Do not claim it means anything yet.)*

---

## N3 — The balance ratio is a fifth shadow, fully accounted for · **FILED** (§5–§6) · → [PG_Balance_Ratio_And_Koide.md](PG_Balance_Ratio_And_Koide.md)

The note ends by asking whether the leftover, after detrending, carries the wheel's fingerprints. **It does — and the amount is forced by algebra, not predicted.**

By N2 the mean of K−1/3 depends on the gaps only through E[g1² + g1·g2 + g2²], and the only term a gap-shuffle can move is the cross-term. So the shift from the null is **exactly cov(g_n, g_n+1)** — which is the *definition* of covariance, hence a reduction (the statistic is redundant), not a prediction. Corrected 2026-09-20 after the first write-up overstated it.

Measured on all 270,014 gaps in [10^6, 5×10^6]: predicted −0.719%, measured −0.708%, inside the null's own run-to-run spread.

Residue-resolved (2 classes mod 6, 8 mod 30, 4 LOS residue pairs), against a wheel-only surrogate: **no class exceeds 1.3σ.** The same test sees the LOS residue-repetition bias immediately — consecutive primes repeat their mod-6 residue 14% less often than even odds — and the wheel surrogate reproduces that to within 0.1 percentage point. So the instrument has power; there is simply nothing left over.

**The claim to write:** the balance ratio carries the wheel, the wheel carries all of it, pooled and per class. It is the *same* −0.05 consecutive-gap anti-correlation already attributed to the wheel in [PG_Angle_Wobble §4.1](PG_Angle_Wobble.md) — **not a new signal, a fifth shadow.** Which also means the note's closing "measurable question" is answered and should be rewritten as a result rather than left open.

---

## N4 — K is a level statistic, so the −1/2 pedestal does not apply · **FILED** (§5.1) · → [PG_Balance_Ratio_And_Koide.md](PG_Balance_Ratio_And_Koide.md), cross-ref [Differencing Trap](Prime_Gap_Memory_Differencing_Trap.md)

Worth saying out loud because the collection has been burned here before. The balance ratio is built from the gaps themselves, **not from differences of them.** So the exact corr = −1/2 differencing artifact — the one that accounted for 42 of the 44 apparent points in the windowed wobble — **has no analogue here at all.**

K needs the gap-shuffle null (pooled) or the wheel surrogate (per class), and nothing more. It is a cleaner instrument than Δg. That is a point in the balance ratio's favour and should be stated, not assumed.

---

## N5 — The two prime angles share one driver · **FILED** (§7 of the v2) · → [PG_Balance_Ratio_And_Koide.md](PG_Balance_Ratio_And_Koide.md)

> **Corrected 2026-09-20 before filing.** The range first recorded here, "27 to 47," was **wrong** — it mixed normalizations, using one gap in one limit and the mean of two in the other. Redone consistently in terms of the mean gap ḡ = (g1+g2)/2, the coefficient runs **46.78 to 54.02**, and 70,433 real triples near 10⁶ measure min 46.78 / median 48.01 / max 53.62 — bracketed by the algebra. The true range is far *tighter* than the erroneous one, so θ ≈ 48·ḡ/p to about ±7%. The algebra: with s = g1+g2 and d = g1−g2, the Loeschian form is (3s²+d²)/4, giving 46.78 at d = 0 and 54.02 as d/s → 1.

The note says the prime-triangle 45° and Koide's 45° are "shared coordinates, not a shared cause." **Right about Koide, but it leaves the wrong impression about the other pair.** The balance-ratio angle θ and the prime-triangle angle α are not independent — both are linear in g/p:

- prime-triangle: α → 45° **from below**, distance = (90/π)·g/p ≈ 28.65·g/p degrees
- balance-ratio: θ → 0° **from above**, size ≈ (46.78 to 54.02)·ḡ/m degrees

Same driver, opposite directions, because α measures one gap while θ measures the *asymmetry* of two. Koide is the genuine outsider — that part of the note's verdict stands and should be kept.

---

## N6 — Three scales: program, territory, period · **PRIOR ART — NOT NEW** · → cite [`FS_primorial_epochs` §2.2](../1_Factor_Skyline/FS_primorial_epochs.md) and [`FSPapers_02.1` §13](../1_Factor_Skyline/FSPapers_02.1_correlations_and_randomness.md)

> **Prior-art check run 2026-09-20, after N6 had been written up. It should have been run first.**
>
> **The result was already in the collection, stated earlier and better.** [`FS_primorial_epochs` §2.2](../1_Factor_Skyline/FS_primorial_epochs.md) has the period-versus-window comparison with a "periods per epoch" table and the identical reading: *"For p ≥ 5, the epoch is shorter than one full primorial period… The full primorial structure is never 'seen' within a single epoch… the coverage pattern's period outgrows the epoch length."* It also uses the fact to explain why gap-6 dominates so long (the 5#-template is the last where epoch ≈ period, 24 vs 30).
>
> **And its comparison is the better one.** It measures the period against the **activation epoch** [p_k², p²_{k+1}) — where the coverage configuration is actually frozen — not against cumulative territory below p²_{k+1}, which spans epochs where coarser templates ruled. That is the right denominator, and it puts the crossover at **p = 5**, not the p = 7 recorded below.
>
> **The cost half is subsumed too.** [`FSPapers_02.1` §13.2–13.3](../1_Factor_Skyline/FSPapers_02.1_correlations_and_randomness.md) and `FSPapers_04` Thm 4.4 give **K = O(log N)** against H ~ 0.26N — stronger than the 1.4427·p_k program bound below, since O(log N) beats linear — under the heading "the randomness paradox resolved."
>
> **What is left:** the measured 1/ln 2 slope, the integers-per-bit table, and the link to the Budget's "for free" phrasing. A paragraph. **The draft note was deleted 2026-09-20**; the surviving paragraph lives in [Budget §5](Prime_Prediction_Budget.md).
>
> **Process lesson worth keeping:** run the prior-art check against your own collection *before* writing the note, not after. The check cost one search; the note cost a draft.

The original N6 entry follows, uncorrected, for the record.

The generation-time half of the balance-ratio note says "the state needed to describe the rule explodes." **Three different things were being collapsed into the word "state," and they scale differently:**

| | size | in p_k |
|---|---|---|
| **program** — bits to write the rule (= Σ log2 p_i = log2 of the primorial) | 1.4427 · p_k | linear |
| **territory** — integers the rule decides (everything below p_{k+1}²) | p_k² | quadratic |
| **period** — length of the unrolled pattern (the primorial) | 2^(1.4427 · p_k) | exponential |

Program slope measured converging to 1/ln2 = 1.4427 (as θ(x) ~ x requires): 1.3489 at p_k = 541, rising to 1.4417 at p_k = 2×10^6.

**The exact consequence worth keeping [fact]:**

> **From p = 7 onward, forever, the wheel's period exceeds the territory it decides.**

Crossover is at k = 4 — primorial 210 against territory 121 — and the gap never closes again (by p_k = 7,919 the period exceeds the territory by a factor of 2^11,245).

**So the wheel never completes a single period inside the region where it is the operative rule.** It is always in its first period, always partial, never seen to repeat. A fully determined, cheaply described object that is *structurally incapable of looking periodic in its own domain of validity*. **That is a mechanism for apparent randomness, stated exactly** — and it is the defensible core of the note's generation-time section.

**Placement:** none. The draft note was deleted; only the short §5 rebuttal in [Budget v2](Prime_Prediction_Budget.md) survives, and it cites the Factor Skyline papers rather than restating them.

---

## N7 — Correction: the wheel is cheap to carry · **correction** · → applies to N6's framing and to anything written from it

Recorded so the wrong version does not get re-derived later.

**Wrong (mine, 2026-09-20, from misreading the note's generation-time section):** *"The structure is cheap to use and exponentially expensive to carry, and that gap is where the apparent randomness lives."*

**Right:** the thing you carry is the program — the list of primes up to p_k — which is **linear** in p_k, while the territory it decides is **quadratic**. Cost per decided integer is 1.4427/p_k bits and **falls to zero**. Return per bit spent grows without bound:

| p_k | cost of one more prime | new integers decided | integers per bit |
|---|---|---|---|
| 29 | 4.95 bits | 408 | 82 |
| 541 | 9.10 bits | 11,040 | 1,213 |
| 7,919 | 12.95 bits | 95,160 | 7,346 |
| 104,729 | 16.68 bits | 3,352,032 | 201,003 |
| 1,299,709 | 20.31 bits | 57,188,208 | 2,815,797 |

**The wheel is a compression that improves with scale.** The Budget's phrase "for free, with no test" is therefore *more* defensible than the challenge to it, not less — there is no missing cost column in the sense originally claimed. The exponential scale is real but it is the **period**, not a cost, and its consequence is N6.

---

## N8 — A generative null must stay strictly weaker than what it models · **FILED** (§5.1 box) · → [Prime_Gap_Memory_Differencing_Trap.md](Prime_Gap_Memory_Differencing_Trap.md)

> **The companion to [N1]. N1 says when a *shuffle* null fails. This says when a *generative* null fails.**

**The rule.** A wheel-only surrogate is built by keeping integers coprime to every prime ≤ Q. As Q approaches √x that construction stops being a model of the primes and **becomes** the primes: below 5×10⁶, an integer coprime to every prime ≤ 1732 is prime, or one of a thin sliver of semiprimes. At Q = 1732 the surrogate pool is only **1.7% larger than π(x)**. "The wheel explains 98.9% of the effect" then means only that the primes reproduce the primes.

> **A generative null must stay strictly weaker than the thing it is modelling — and "coprime to all primes up to √x" is not weaker, it is a definition of primality.**

**How to keep yourself honest.** Report the **pool ratio** (surrogate candidates ÷ π(x)) beside every surrogate result, and sweep Q rather than picking one value. At pool/π(x) ≈ 1.4–1.8 the model is genuinely weaker than the primes; below ≈1.25 it is not evidence. Sweeping is also what reveals whether a result is a trend or noise.

**Why this matters beyond one test.** [PG_Angle_Wobble §4.1](PG_Angle_Wobble.md) uses Q = 1732 as its top row. Its *conclusion* is safe because the lag-1 value already plateaued at Q ≈ 300, where the pool is still 1.43× — the deep row only confirms no further movement. But the row carries no independent weight, and the paper does not say so. **Worth a sentence there.**

---

## N9 — An unreproduced published number · **CLOSED — the paper was wrong** · → [Prime_Gap_Memory_Differencing_Trap.md](Prime_Gap_Memory_Differencing_Trap.md) §3

The [reproduction script](repro/) regenerates every measured table in the three gap papers **except one row**: the jitter recoil. Published 81.8% real / 79.2% null / **+2.7 pp genuine**; the script gets 84.0% / 84.5% / **−0.5 pp** — the genuine column changes sign.

**Diagnosis, not yet confirmed.** The original implementation is unspecified. "After a large jitter, the next has the opposite sign" needs a threshold (script: top decile of |Δg|), a reference for "opposite" (against the trigger, or the one before), and a zero-handling rule. None appears in the paper, and the appendix code covers only the two R² statistics.

**Low stakes, but it must not be dropped quietly.** §4 proves recoil is forced by the exact −1/2 differencing identity; the script finding it *wholly* artifact agrees with the paper's own verdict more strongly than the paper did. Nothing downstream depends on the number. But an unreproduced published figure is precisely what this collection's honesty claim is about, so it carries a ⚠️ in the table rather than being edited away.

**CLOSED 2026-09-20.** Thirty definitions tested (thresholds: top decile/quintile/quartile/5%, 1 and 2 sd, fixed |Δg| ≥ 12/18/24/30; three zero-handling rules each). Several reproduce the published *real* value, several the published *null* value, **none reproduces both**, and all thirty give a genuine column in [−0.7, +0.2] pp. Conclusion: the published pair was computed at two different thresholds, so the +2.7 pp was never a measurement. The row now reads ≈0 (artifact), which is what §4's exact −1/2 identity predicts.

---

## N10 — The Switchback Law compared against the wrong null · **CLOSED — paper revised 2026-09-20** · → [Switchback_Law.md](Switchback_Law.md)

Found while closing N9, using the same machinery.

**Switchback §2–§3 compare the run-length distribution to a fair coin.** Differencing forces corr = −1/2 on any sequence, so a coin was never the alternative. Against the transform-matched null (shuffle gaps, then difference), over [10⁶, 5×10⁶]:

| | run 1 | run 2 | run 3 | run 4 |
|---|---|---|---|---|
| real primes | 64.00% | 27.25% | 7.18% | 1.34% |
| gap-shuffled null | 64.66% | 27.31% | 6.74% | 1.13% |

Reversal odds: real 64.0→75.7→82.1→85.5, null 64.7→77.3→83.9→87.6 — **the null is slightly higher.**

**The error is the paper using the wrong one of its own two nulls.** §4 defends the law with the *change*-shuffle, which tests the monotone skeleton. "This is a prime fact" needs the *gap*-shuffle, which tests the wheel. This is failure mode 2 of [Null_Model_Discipline.md](Null_Model_Discipline.md), committed inside the collection that documents it.

**What survives:** §5's mod-6 suppression (separately validated against wheel-Cramér, matched to 0.1 point) — the paper's real result. §3's scale-invariance is a genuine observation whose *explanation* inverts: it is scale-invariant because it is a universal differencing artifact. §6's betting rule works, but on any increasing bounded-gap sequence.

**CLOSED 2026-09-20 — paper revised.** The mod-6 rule is now §2 and leads; the run-length law is §3 and is explicitly demoted to "a property of any increasing, bounded-gap sequence." Title and abstract rewritten to match. RESULTS.md updated.

**The revision strengthened the paper.** Tested against the *correct* null (gap-shuffle, then difference), §2 comes out decisively: the (2,2) and (4,4) transitions are exactly 0.0% in real primes against 28.4%/28.5% under the shuffle; $|\Delta g|=6$ is halved (5.14% vs 10.29%) and $|\Delta g|=12$ likewise (2.98% vs 6.57%), while every non-multiple of 6 is *elevated*. Zero gap-repeats by a gap not divisible by 6, exceptionless. The paper now has a hard rule with exact zeros where it used to have a sign-prediction table that any monotone sequence satisfies.

---

## N11 — PG I Theorem 5.2 is off by one prime · **CLOSED — corrected in place** · → [PG_I_PrimeTriangle.md](../3_Twin_Bertrand_Prime_Geometry/PG_I_PrimeTriangle.md)

**The first series-3 claim to be independently re-verified, and it came back with a correction.**

PG I Theorem 5 states, for p_n >= 5: (1) PSD_n = (p_{n+2}^2 - p_n^2)/12 is an integer, and (2) its last decimal digit is in {0,4,6}.

- **(1) confirmed**, and the threshold is sharp: (2,3,5) gives 7/4, (3,5,7) gives 10/3.
- **(2) is FALSE at p_n = 5.** The triple (5,7,11) gives PSD = 96/12 = 8, last digit 8. It is the *only* counterexample among all 348,511 consecutive-prime triples below 5x10^6. **True for p_n >= 7.**
- **Theorem 3 confirmed** — and it needs no primality whatever; the shared p_{n+1} terms cancel for any three numbers.

**Where the proof slips.** The mod-6 step is sound and carries integrality. The last-digit claim additionally needs p^2 = +/-1 (mod 5), true for every prime *except 5 itself*. At p_n = 5 the mod-5 argument has nothing to stand on, so the threshold should have been 7.

**Bonus observation, not in the original.** For p_n >= 7 the digits are far from equidistributed: 0 at 48.97%, 4 and 6 at 25.51% each. **4 and 6 are exactly equal** (measured difference: zero) — forced, since they count the two directions of one transition, which interleave. The 0-to-others ratio is 1.92, *not* the 2 a uniform model predicts; the shortfall is finite-range plus LOS residue correlations.

*(I briefly wrote "exactly 2:1:1" in the script and caught it on the output — the same overclaim pattern as the rest of the day. Recorded because the habit is the point.)*

Reproduce: [`check_psd.py`](../3_Twin_Bertrand_Prime_Geometry/scripts/check_psd.py). Corrections filed in PG I, RESULTS.md, WHAT_WE_FOUND.md and the series-3 README.

---

## N12 — The angle-record theorem is clean · **CLOSED — confirmed, no correction** · → [PG_II_AngleRecord.md](../3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md)

**The load-bearing claim of series 3, and the first thing today to come back needing nothing.**

PG II Theorem 6 makes three statements equivalent: the Twin-Prime Bertrand Postulate in dyadic form, the twin-gap form T_{k+1} < 2·T_k, and the geometric form "every angle-record with p_n >= 3 is a twin pair." Because they are *equivalent*, checking the geometric one checks TPB.

**Verified over every consecutive prime pair below 10^8**, with exact integer cross-multiplication (no floating point anywhere):

| | |
|---|---|
| angle-records with p_n >= 3 | 440,312 |
| of those, non-twin | **0** |
| twin pairs with p >= 3 | 440,312 |
| twins that fail to set a record | **0** |
| violations of T_{k+1} < 2·T_k | **0** (worst ratio 1.7059, at T_k = 17) |

**The result is stronger than the theorem states, and the gap is now closed.** PG II claimed records ⊆ twins. Measurement gives records **=** twins, element for element.

**Written up as Proposition 6A + Corollary 6B (2026-09-20), and the converse turns out to be *unconditional*.** Let (T,T+2) be a twin, T ≥ 3, and (P,P+g) any earlier pair, so P < T. If g = 2 then P/(P+2) < T/(T+2) since x/(x+2) increases. If g ≥ 4 then Lemma 4 says the earlier pair wins only when P > (g/2)T ≥ 2T — impossible, since P < T. Either way the twin beats it. No conjecture used.

**So the right framing is an asymmetry, and it is nicer than the original:** the angle-record sequence *always* contains every twin, and TPB is exactly the assertion that it contains nothing else —

> TPB fails ⟺ some angle-record is not a twin pair.

A single non-twin record would be a finitely-checkable witness against TPB, which is precisely what the verification searches for. Prop 6A also brute-forced independently: for the first 4,000 twins, all 67,686,681 twin-vs-earlier-pair comparisons go the right way.

**One definitional wrinkle, benign.** Def. 5 says "for all m < n" without excluding the pair (2,3), whose ratio 2/3 exceeds 3/5. Under the literal reading (3,5) is therefore *not* a record, and the proof's line "the first such record is (3,5)" presumes the record sequence starts at (3,5). Both readings were tested; neither produces a non-twin record. The only difference is whether (3,5) appears in the list. **Not an error — but one clarifying clause in Def. 5 would remove the ambiguity.**

Reproduce: [`check_angle_records.py`](../3_Twin_Bertrand_Prime_Geometry/scripts/check_angle_records.py).

---

## N13 — X5D's historical comparison is wrong · **CLOSED — reference material, not canon** · → upstream `Archive/X5D EXPDB Framework/examples/GuthMaynard/`

Found 2026-09-20 while drawing the cusp figure.

`GuthMaynard_BindingConstraints.md` states that before Guth–Maynard *"the analogous cusp was at σ ≈ 5/7 ≈ 0.714, where Ingham met Huxley at ‖A‖∞ = 12/5."* **The two halves of that sentence contradict each other on the document's own Ingham curve:**

- A_Ing(5/7) = 3/(2 − 5/7) = 3/(9/7) = **7/3 ≈ 2.333**, not 12/5 = 2.4.
- If the peak height was 12/5, Ingham forces σ **exactly** 3/4: 3/(2−σ) = 12/5 ⟹ 2−σ = 5/4 ⟹ σ = 3/4.
- The Huxley form coded in the upstream `gen_figures.py`, `A_huxley(s) = 12(1−s)/5`, **never crosses Ingham in (1/2, 1)** — solving gives σ = (3 ± √6)/2, i.e. 0.275 or 2.72. That expression equals 12/5 only at σ = 0.
- The textbook Ingham–Huxley crossover uses A_Hux(σ) = 3/(3σ−1), which meets 3/(2−σ) at exactly σ = 3/4 with height 12/5 — consistent with the quoted peak. **Likely the intended statement, offered as a reading, not asserted.**

**Scope checked, and it is contained.** The error appears in four files, all in `Archive/X5D EXPDB Framework/examples/GuthMaynard/` (`BindingConstraints.md`, `_v2.md`, `_v2.tex`, `Pipeline_Report.txt`). It is **not** in the curated `X5D_EXPDB_Reinterpretation.md`, and **not** in the published `X5D_Polyhedral-Reinterpretation.pdf` — whose only Huxley references concern *Huxley subdivision*, an unrelated unimplemented EXPDB technique. So nothing tracked or published here carries it.

**Why it is closed.** `Archive/` holds **discontinued** repos, kept as reference while it was still unclear what in them was worth saving. They are not canon and are not public. The canon is this repository — `README`, `RESULTS`, `PRIMES_MAP` and folders 1–5 — and none of it carries the error. **So there is nothing to fix.** If the historical comparison is ever wanted in the live collection, the correct statement is σ = 3/4 with height 12/5 via A_Hux(σ) = 3/(3σ−1), and it should be written fresh into a canon document rather than corrected in a dead one.

**The main chain is unaffected** and was verified exactly: cusp at σ = 7/10, ‖A‖∞ = 30/13, θ = 17/30, dθ/d‖A‖ = 169/900. Neither figure draws the Huxley curve.

---

## Still genuinely open

Carried here so they are not lost when the worklog is archived.

- **R6 — is the hexagonal norm meaningful?** g1² + g1·g2 + g2² is the Eisenstein norm form; the wheel's first filter is mod 6, also hexagonal. Probably a pun. Cheap to test: does the form's value distribution over real gaps differ from the null in a way that references 6? Low priority. Flagged as open in [balance ratio §9](PG_Balance_Ratio_And_Koide.md).
- **~~Does Factor Skyline already say N6?~~ CLOSED 2026-09-20 — yes, it does.** Draft deleted; [`FS_primorial_epochs.md`](../1_Factor_Skyline/FS_primorial_epochs.md) promoted into the curated collection, and [`DERIVATION_MODULES.md`](../1_Factor_Skyline/DERIVATION_MODULES.md) added so the untracked upstream modules are findable next time.
- **The v2 files are drafts, not replacements.** Five new documents sit alongside five originals. Deciding whether to supersede the originals, and updating [PRIMES_MAP.md](../PRIMES_MAP.md) and [RESULTS.md](../RESULTS.md) accordingly, is not done.
- **~~Add the pool-ratio caveat to PG_Angle_Wobble §4.1~~ DONE 2026-09-20.** Pool ratios added to the table; the Q = 1732 row is marked circular (ratio exactly 1.00 over that range) and Q = 317 marked as the last row carrying evidence. The section's conclusion is unaffected.
- **"What picks Koide's midpoint?"** — parked. Physics, unresolved there, not ours.
