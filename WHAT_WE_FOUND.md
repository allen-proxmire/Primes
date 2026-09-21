# What We Found

### The results, in plain language — no notation

*If you want the picture of **what's going on**, read [The Movie](4_Philosophy_Ontology/The_Movie.md) first. This page is **what came out of it**. If you want to know **why any of it should be believed**, read [How We Know](HOW_WE_KNOW.md).*

Each item says how strong it is. The labels mean what they say:

- **Proven** — a proof. It's settled.
- **Verified, not proven** — checked very far, believed, still a conjecture.
- **Measured** — an experiment, compared against a stated "what if there's nothing here" baseline.
- **A reading** — an interpretation. True-ish, useful, not a claim about arithmetic.
- **Retracted** — was claimed, then withdrawn. Kept on the page deliberately.

---

## The one-paragraph version

The small primes block positions on the number line in a pattern that's utterly simple to describe and impossible to see repeat. That pattern accounts for **every measurable rhythm in the spacing of the primes** — ten statistics, no residual. It does *not* account for which of the surviving positions is actually prime, and that part is beyond reach for reasons close to proven. Along the way: one small theorem about gap widths, one hard traffic rule on consecutive gaps, a conjecture about twins in doubling windows verified to ten billion, and a demonstration that the primes diffract like a crystal while a look-alike process doesn't. **Nothing here is new deep mathematics. What's new is the lens, the unification, and the fact that it checks itself.**

## 1. The small primes explain the gaps — all of them

**Measured, ten different ways.**

The spacing between consecutive primes has structure: some gaps are far more common than others, neighboring gaps lean on each other, the whole sequence has rhythms in it.

**Every one of those rhythms traces back to the same thing** — the small primes blocking positions. Nothing is left over. Ten separate statistics were checked against a model that knows *only* about small-prime divisibility and nothing else, and the model reproduced every one.

The honest footnote, which matters: **those ten aren't ten independent confirmations.** Six genuinely ask different questions. The other four turned out to be *the same quantity written in different notation* — which sounds like a weakness and isn't. Showing that four apparently unrelated measurements are secretly the same object is the whole point of the collection.

→ [The Wheel Is the Whole Story](2_One_Wheel_Many_Shadows/The_Wheel_Is_The_Whole_Story.md)

## 2. A traffic rule on consecutive gaps

**Proven, and visible in the data.**

Every prime past 3 sits on one of two "lanes." A step from one prime to the next either stays in its lane or changes lanes — and **you cannot change the same direction twice in a row.** Change lanes left, and the next move must be stay-or-right. It's forced; there's no choice in it.

The consequence shows up plainly: gap-changes of 6 and 12 occur at **half** the rate you'd otherwise expect, while every other size occurs *more* often. And no gap that isn't a multiple of 6 ever repeats immediately — not once, anywhere checked.

**This is the prettiest concrete result in the collection.** It's a rule, not a tendency.

→ [The Switchback Law](2_One_Wheel_Many_Shadows/Switchback_Law.md)

## 3. Four gap widths can never hold two consecutive-prime sums

**Proven.** The widths are **2, 4, 6, and 10** — and that list is complete, with no exceptions anywhere checked (to 200 million).

This is the most self-contained original result here: elementary, unconditional, and quite possibly new. The width-10 case is the non-obvious one.

→ [Consecutive-Prime Sums in Prime Gaps](2_One_Wheel_Many_Shadows/FS_Consecutive_Prime_Sums_In_Gaps.md)

## 4. A twin prime in every doubling window

**Verified, not proven.** Checked to 10 billion — 27.4 million twin pairs, no exceptions.

The claim: past 11, if you take any number and double it, there's a twin prime pair somewhere in between. It's a twin-prime version of Bertrand's postulate (which says the same thing about ordinary primes and *is* proven).

Worth being clear about where this sits: it's **weaker** than the twin prime conjecture and **stronger** than the bounded-gaps results. It follows immediately if the standard Hardy–Littlewood conjecture holds. Unproven on its own.

There's a geometric restatement that's rather nice: draw a right triangle from each consecutive prime pair, and **every record-setting "most balanced" triangle is a twin pair.** Same statement, different clothes — and not loosely: the two are *logically equivalent*, so checking one checks the other.

**Re-verified September 2026, and it came back clean.** Over every consecutive prime pair below a hundred million: 440,312 record-setting triangles, 440,312 twin pairs, and they are *the same list*. Not merely "records are twins" but records and twins coincide exactly. This is the one substantive series-3 claim that has now been independently checked, and unlike the square-difference theorem it needed no correction.

→ [PG II](3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md), extended to cousins and sexy primes in [PG III](3_Twin_Bertrand_Prime_Geometry/PG_III_GBP.md)

## 5. The same conjecture, found twice from different directions

**A real convergence, recovered from an archive.**

Item 4's twin conjecture was reached **twice in the same month, by two geometries with nothing in common** — and the two papers didn't know about each other until September 2026, when one of them was found in a discontinued repo.

**Route one** is the triangle above: angles climbing toward 45°, twins setting every record.

**Route two** uses a different picture entirely. Stand every integer up as a column whose width is its smallest prime factor (this is the Factor Skyline of item 7). Consecutive primes are then joined by a sloping line — and **that slope has a hard ceiling**, about 33.69°, which is reached *only* by twin pairs. Ask whether the ceiling gets touched in every doubling window and you have written down the same conjecture again.

The ceiling itself is solid: checked on every consecutive prime pair below a million, **nothing exceeds it**, no exceptions. *(The published proof of that had a broken step — an inequality that runs the wrong way — which is now repaired. The theorem was never in doubt, only the argument for it.)*

**What the convergence is worth, and what it isn't.** It is *not* extra evidence that the conjecture is true — deriving a statement twice doesn't confirm it. It's evidence that the statement is **natural**: ask a sharp question about how close consecutive primes can get, and you land here whichever geometry you ask in.

*The paper originally claimed more than this — that it had located the single obstacle to the twin prime conjecture, and that this obstacle was easier than a known barrier in the field. Neither holds up, and both were withdrawn. See [How We Know](HOW_WE_KNOW.md).*

→ [The Twin-Slope Ceiling](3_Twin_Bertrand_Prime_Geometry/FS_twin_prime_geometry.md), [PG II](3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md)

## 6. The primes diffract like a crystal

**Measured.**

Shine the mathematical equivalent of an X-ray through the primes and you get **sharp peaks at predictable places** — the signature of a crystal, not a liquid. The peaks sit exactly where the small-prime structure says they should, at heights you can write down in advance.

What makes this more than a curiosity is the **control**. A process that excludes things for non-arithmetic reasons — a completely different kind of "some positions are blocked" — was run through the same analysis. It came out a **liquid**: no sharp peaks at all, flat exactly where the primes spike.

So the crystal isn't a generic feature of "things get blocked." **It takes divisibility specifically.** That control is the most under-appreciated piece of work in the collection.

→ [The Prime Structure Factor](2_One_Wheel_Many_Shadows/Prime_Structure_Factor.md), [ED as the Negative Control](2_One_Wheel_Many_Shadows/ED_Negative_Control.md)

## 7. You can narrow the next prime to a handful of candidates — and no further

**Synthesis of known results, calibrated here.**

Start from a known prime and walk forward, skipping every position the small primes have already ruled out. **The next prime is among the next seven open slots about 90% of the time near a million — and among the next eleven near ten billion.**

That count grows by about one slot per decade, and **it is predicted, not fitted.** Divide the prime density by the fraction of positions the wheel leaves open, treat each open slot as a coin flip, and the formula lands on the measured whole number at every decade from a thousand to ten billion — eight for eight.

Two things make this worth stating:

**The small primes do essentially all the work.** They eliminate roughly three-quarters of positions for free, no testing required. Every other pattern in the collection — the traffic rule, the favored gaps, the lot — adds *nothing on top*, because walking forward in order is already the best possible strategy. The extra structure is real and already spent.

**And then there's a wall.** Which of the remaining candidates is actually prime is not a hard problem — it's an *impossible* one, in a sense that's close to proven. That's the parity barrier, and nothing in this collection touches it.

→ [**The Ninety Percent Rule**](4_Philosophy_Ontology/The_Ninety_Percent_Rule.md) (the full table, the formula, and the honest limits) · [The Prime Prediction Budget](2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) (the technical ledger)

## 8. The lens — which is the actual contribution

**A reading, and the thing everything else rests on.**

Stand every integer up as a column, with its width set by its smallest prime factor. Set the width of primes to one, since their smallest prime factor are themselves. Primes escape to a diagonal; everything else falls onto one of a fan of rays (other diagonals).

The claim isn't that this proves anything new. It's that **facts which look unrelated on the number line become one picture here** — the common gaps, the forbidden widths, the 45° angle, the crystal. Squash the picture flat into a number line and they scatter into unrelated-looking messes.

**The lens is the contribution.** The rest is consequence.

→ [The Factor Skyline papers](1_Factor_Skyline/), [Synthesis](2_One_Wheel_Many_Shadows/FS_Synthesis_Doubling_and_Wheel.md)

## 9. A useful negative: Koide's relation

**Measured, and the answer is no.**

There's a famous unexplained coincidence in particle physics — Koide's formula — and the quantity behind it can be applied to prime numbers. It seemed worth checking.

It's not a connection. The quantity, applied to primes, turns out to be an **exact restatement** of something already measured here — it contains no new information at all, provably. And the primes and the particles run toward *opposite* ends of the scale.

Recorded because negative results of this kind are worth more than they look. "These two things are not related, and here is exactly why" saves everyone the trip.

→ [The balance ratio](2_One_Wheel_Many_Shadows/PG_Balance_Ratio_And_Koide.md)

## 10. A separate subject: the exponent database

**Proven, and unrelated to everything above.**

A large table of results from analytic number theory turns out to be generated by a **single geometric object** in five dimensions — every entry is a shadow of one shape. This is its own line of work with its own audience.

→ [X5D](5_X5D_EXPDB/)

---

## What was retracted

Kept on the page on purpose. A collection that hides its retractions isn't worth reading.

**The switchback law's headline.** The claim was that the *direction* of the prime-gap wobble flips more often than a coin would, identically at every scale. True, but meaningless: the way the quantity is built makes it flip more than a coin **for any sequence of numbers whatever.** The coin was never the thing to beat. What survives is item 2 above — which is better.

**One row of a table.** A claimed small effect turned out to have been computed two different ways and compared against itself.

**Two curve fits that don't hold.** A formula for how fast the gaps between twin primes grow was published with an exponent of 1.866, described as sitting *below* the value the standard theory predicts. Measured over four decades, the exponent is **essentially 2** — exactly the standard value. The apparent shortfall was an artefact of fitting over too short a range.

And a bound claimed to cap the largest gaps is **violated 204 times** below a hundred million, missing by up to 1.87×. The cause is subtle and worth stating: the bound was fitted to one extreme quantity (the largest gap *relative to* the prime) and then asserted about a different one (the largest gap, full stop). The first extreme happens at small primes, the second at large ones. Fitting one doesn't constrain the other.

*What survives there is the shape of the observation — the biggest twin gaps do grow faster than typical ones, and all the prime constellations behave alike — but the specific numbers don't, and neither does the 98% goodness-of-fit, which came from fitting two parameters to five overlapping data points.*

**An off-by-one in a theorem.** A result about the last digit of a derived quantity was stated as holding from the prime 5 upward. It holds from 7 upward — the triple (5, 7, 11) is the single exception, and the proof's argument genuinely has nothing to stand on at 5 itself. Small, but it is a *theorem*, so the statement matters.

**And one caveat.** A widely-quoted figure — "the small primes give you 68% of everything knowable" — is correct at one particular range and drifts downward at larger ones. The underlying quantity is rock-stable; the *percentage* isn't, because what it's a percentage *of* keeps growing.

**All three were found the same way, in one day, by building something that re-runs the measurements.** See [How We Know](HOW_WE_KNOW.md).

---

## What's still open

- **The twin prime conjecture, Goldbach, the Riemann Hypothesis.** Untouched. Several results here would follow immediately from them, which is the wrong direction.
- **Twin Bertrand itself** (item 4) — verified to 10 billion, unproven.
- **The parity barrier** (item 6) — the wall is where this collection stops, and it stops there on purpose.
- **Whether the forbidden-width theorem is actually new.** It's elementary enough that someone may well have it.
- **Series 3 has now been checked, and it is mixed.** Four claims examined: the angle-record theorem came back clean; the square-difference identity clean but its last-digit theorem off by one prime; and the two curve fits both failed. The 10-billion twin verification itself has still not been independently re-run — its evidence report exists, but nobody has redone the computation.
- **Series 5 is still unverified.** The first series-3 claim to get the treatment — the square-difference theorem — came back with an off-by-one in its threshold. That is one claim of many. Given the hit rate so far, the rest is a real gap rather than a formality.

---


