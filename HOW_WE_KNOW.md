# How We Know

### Why any of this should be believed — and the two times it shouldn't have been

*Companion to [What We Found](WHAT_WE_FOUND.md). No notation.*

---

## The problem, in one sentence

**You cannot tell whether a pattern is real until you know what "no pattern" would have looked like.**

That sounds obvious. It is the single easiest thing to get wrong in this entire subject, and this collection got it wrong twice — both times in ways that looked completely convincing for two months.

## Why it's hard

Suppose you measure something about the primes and find structure. Is it *about the primes*?

The only way to answer is to compare against a version with the interesting part removed — shuffle the data, or build a fake sequence that has some properties and not others — and see whether the structure survives. That comparison is called a **null**, and it does all the work.

Here's the trap: **a null that's too easy to beat makes anything look like a discovery.**

---

## Worked example 1: prime weather

Look at how prime gaps *change* from one to the next and the sequence seems alive:

- big changes arrive in bursts, like storms
- after a big jump, the next move reverses about 82% of the time
- feed the last five changes into a simple predictor and it explains **44%** of what happens next

Forty-four percent. That reads like a discovery. Prime weather.

**It's almost entirely an illusion, and the illusion is forced by arithmetic.**

Here's why. If you take *any* list of numbers — genuinely random ones — and look at the differences between consecutive entries, those differences are guaranteed to anti-correlate. Not usually. **Always**, by a fixed exact amount. It's a consequence of neighbouring differences sharing a term, nothing more.

So the storms, the reversals, and most of the 44% are what subtraction does to any spread-out list. Shuffle the prime gaps into random order, redo the whole analysis, and you get nearly the same numbers back.

**Of the 44%, about 42 points are arithmetic and 2 points are real.** Those 2 points are genuine and traceable to the small primes. But you would never have found them without asking what a shuffled version does first.

→ [Prime-Gap Memory and the Differencing Trap](2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md)

## Worked example 2: the coin that was never the opponent

This one is worse, because the collection *had already written down* the lesson above.

A paper here observed that the direction of the prime-gap wobble — just up or down, throwing away everything else — flips more often than a coin would. Runs of the same direction die fast: about 63% of runs are length one, where a coin gives 50%. And the distribution is **identical** in the hundreds and in the millions, even though the thing being measured shrinks ten-thousand-fold. That scale-invariance was the headline.

Every number in it was correctly measured.

**But a coin was never the alternative.** By example 1, differencing *forces* extra alternation onto any sequence at all. Beating a coin proves nothing whatsoever.

Compared against the right baseline — shuffle the gaps, then redo the identical calculation — the effect vanishes completely:

| | run of 1 | run of 2 | run of 3 | run of 4 |
|---|---|---|---|---|
| real primes | 64.0% | 27.3% | 7.2% | 1.3% |
| **shuffled** | **64.7%** | **27.3%** | **6.7%** | **1.1%** |
| a coin | 50% | 25% | 12.5% | 6.3% |

The shuffled version is, if anything, *slightly more* extreme than the primes.

So the switchback law describes **any increasing sequence with bounded steps.** It isn't about primes. The scale-invariance is real, but it holds because the effect is generic — and generic things have no scale in them.

**The painful detail:** the paper defended itself with a shuffle. Just the wrong one. It shuffled the thing that tests whether the sequence increases (it does, that matters) rather than the thing that tests whether *the primes* matter (they don't, here). Two nulls, two different questions, and it reached for the wrong one — a distinction its own companion paper had already spelled out.

→ [The Switchback Law](2_One_Wheel_Many_Shadows/Switchback_Law.md) §3

---

## The rules that came out of it

Five, each learned the hard way:

1. **Do the transform after shuffling, never before.** If you're studying differences, shuffle the original numbers and then difference them. Shuffling the differences destroys the very thing you're trying to account for.

2. **Name what you shuffled.** Shuffling different things tests different claims. Get this backwards and a real structural fact reads as noise — or a generic one reads as arithmetic.

3. **Check your null can actually produce the data.** Sometimes a shuffle creates arrangements that are *arithmetically impossible* — a gap that can't follow a particular prime. Comparing against impossible arrangements is comparing against nothing. When that happens, you need a null you *build* rather than one you shuffle.

4. **Check your built null isn't secretly the answer.** The opposite failure. Build a model that's too good and it stops being a model of the primes and *becomes* the primes — at which point "the model explains it" means "the primes explain the primes." Two tables here had exactly this problem. The fix is to report how much *looser* your model is than reality, every time.

5. **Prove your test can find something before trusting it when it finds nothing.** A null result from a blind instrument is worthless. Before reporting "no effect," show the same setup detecting an effect you already know is there — or deliberately cripple the model and confirm the test notices.

→ [The Null-Model Discipline](2_One_Wheel_Many_Shadows/Null_Model_Discipline.md) has all five with the technical detail.

---

## What actually catches these

Not thinking harder. **Building something that re-runs the measurements.**

There's now a script that regenerates every measured table in the main papers from scratch — sieve the primes, redo the statistics, compare against the published numbers. It found:

- one table row that didn't reproduce, which turned out to have been computed two different ways
- one entire paper's headline claim, which evaporated against the correct baseline
- two tables whose deepest row was circular
- and a widely-quoted percentage that's only correct at one particular range

**All in a single day. All from papers that had stood unchallenged for two months.**

None of it required new ideas. It required running the checks, which nobody had done, because until the script existed there was nothing to run.

→ [`2_One_Wheel_Many_Shadows/repro/`](2_One_Wheel_Many_Shadows/repro/)

---

## So why believe the rest?

Fair question, and the honest answer has three parts.

**Because the failures were found here, by this collection, using this collection's own method.** Not by a reviewer. The instrument that broke the switchback paper is the paper published alongside it.

**Because the surviving results were checked the same way and held.** The traffic rule on consecutive gaps isn't "a tendency we noticed" — it survives the correct baseline by a factor of two, with exact zeros where the rule says there must be zeros. The crystal result has a genuine control that came out negative. The claims that survived, survived a process that killed two others on the same day.

**And because the labels are honest.** [What We Found](WHAT_WE_FOUND.md) marks each item proven, verified-not-proven, measured, or a reading. The retractions are on the page. The unverified parts — series 3 and 5, which haven't had this treatment — are named as unverified rather than quietly included.

**Series 3 has since had the same scrutiny, and the guess was right.** Four claims checked: one clean, one clean-with-an-off-by-one, and **both curve fits failed** — an exponent that measures 2 rather than the published 1.866, and a bound violated 204 times because it was fitted to one extreme quantity and asserted about another.

That last one is worth keeping as a sixth rule, since it is not about nulls at all:

> **6. Fit the quantity you are going to make a claim about.** Extremes are not interchangeable. The largest gap *relative to its prime* happens at small primes; the largest gap outright happens at large ones. Fitting the first tells you nothing about the second — and a high goodness-of-fit will not warn you, especially if the points you fitted overlap each other.

**Series 5 remains unverified**, and on the record so far it would be strange to assume it is clean.

---

## The one-paragraph version

You cannot tell a real pattern from an arithmetic artifact without knowing what "nothing here" looks like — and in this subject the artifacts are unusually convincing, because subtracting one number from the next manufactures structure out of nothing, every time, by a fixed exact amount. This collection fell for that twice, and caught itself twice, using a method it had written down itself and finally got around to running. **What makes the surviving results trustworthy isn't that they're clever. It's that they were put through something that demonstrably kills things.**
