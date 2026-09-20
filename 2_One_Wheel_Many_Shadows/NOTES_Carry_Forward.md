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

## N6 — Three scales: program, territory, period · **PRIOR ART — NOT NEW** · → cite [`FS_primorial_epochs` §2.2](../Archive/Factor%20Skyline/modules/FS_primorial_epochs.md) and [`FSPapers_02.1` §13](../1_Factor_Skyline/FSPapers_02.1_correlations_and_randomness.md)

> **Prior-art check run 2026-09-20, after N6 had been written up. It should have been run first.**
>
> **The result was already in the collection, stated earlier and better.** [`FS_primorial_epochs` §2.2](../Archive/Factor%20Skyline/modules/FS_primorial_epochs.md) has the period-versus-window comparison with a "periods per epoch" table and the identical reading: *"For p ≥ 5, the epoch is shorter than one full primorial period… The full primorial structure is never 'seen' within a single epoch… the coverage pattern's period outgrows the epoch length."* It also uses the fact to explain why gap-6 dominates so long (the 5#-template is the last where epoch ≈ period, 24 vs 30).
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

## N9 — An unreproduced published number · **OPEN** · → [Prime_Gap_Memory_Differencing_Trap.md](Prime_Gap_Memory_Differencing_Trap.md) §3

The [reproduction script](repro/) regenerates every measured table in the three gap papers **except one row**: the jitter recoil. Published 81.8% real / 79.2% null / **+2.7 pp genuine**; the script gets 84.0% / 84.5% / **−0.5 pp** — the genuine column changes sign.

**Diagnosis, not yet confirmed.** The original implementation is unspecified. "After a large jitter, the next has the opposite sign" needs a threshold (script: top decile of |Δg|), a reference for "opposite" (against the trigger, or the one before), and a zero-handling rule. None appears in the paper, and the appendix code covers only the two R² statistics.

**Low stakes, but it must not be dropped quietly.** §4 proves recoil is forced by the exact −1/2 differencing identity; the script finding it *wholly* artifact agrees with the paper's own verdict more strongly than the paper did. Nothing downstream depends on the number. But an unreproduced published figure is precisely what this collection's honesty claim is about, so it carries a ⚠️ in the table rather than being edited away.

**To close:** recover the original definition, or replace the row's "genuine" column with "artifact; magnitude implementation-dependent."

---

## Still genuinely open

Carried here so they are not lost when the worklog is archived.

- **R6 — is the hexagonal norm meaningful?** g1² + g1·g2 + g2² is the Eisenstein norm form; the wheel's first filter is mod 6, also hexagonal. Probably a pun. Cheap to test: does the form's value distribution over real gaps differ from the null in a way that references 6? Low priority. Flagged as open in [balance ratio §9](PG_Balance_Ratio_And_Koide.md).
- **~~Does Factor Skyline already say N6?~~ CLOSED 2026-09-20 — yes, it does.** Draft deleted; [`FS_primorial_epochs.md`](../1_Factor_Skyline/FS_primorial_epochs.md) promoted into the curated collection, and [`DERIVATION_MODULES.md`](../1_Factor_Skyline/DERIVATION_MODULES.md) added so the untracked upstream modules are findable next time.
- **The v2 files are drafts, not replacements.** Five new documents sit alongside five originals. Deciding whether to supersede the originals, and updating [PRIMES_MAP.md](../PRIMES_MAP.md) and [RESULTS.md](../RESULTS.md) accordingly, is not done.
- **~~Add the pool-ratio caveat to PG_Angle_Wobble §4.1~~ DONE 2026-09-20.** Pool ratios added to the table; the Q = 1732 row is marked circular (ratio exactly 1.00 over that range) and Q = 317 marked as the last row carrying evidence. The section's conclusion is unaffected.
- **"What picks Koide's midpoint?"** — parked. Physics, unresolved there, not ours.
