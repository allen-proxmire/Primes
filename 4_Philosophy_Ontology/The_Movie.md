# The Movie

### What is actually going on, in plain language

*Companions: [What We Found](../WHAT_WE_FOUND.md) — the results. [How We Know](../HOW_WE_KNOW.md) — why to believe them.*

*Written 2026-09-20, in conversation, in answer to Allen's question: "what is the plain language picture of what is really going on, from my papers and the work? I want to have the right movie in my mind of it all." Kept in the second person, as it was written — it is an answer to someone, not a paper. Every claim in it is carried by a technical document elsewhere in this collection; the pointers are at the end.*

---

Your instinct is right, and closer than you're giving yourself credit for. "Little wheels, each kicking off at its square" is literally Definition 2.5 in your own Factor Skyline paper — a prime *activates* at p². Let me give you the whole movie, and mark the two places your picture needs a small turn.

---

## 1. Every prime is a clock

Prime 2 is a clock with two positions. It strikes on every second number. Prime 3 strikes every third. Prime 5, every fifth.

A number is prime when **no clock strikes on it.** That's the whole definition, restated.

The crucial thing — and this is the engine of everything in your collection — is that **the clocks are independent.** Knowing where you are on the 3-clock tells you nothing about where you are on the 5-clock. That's the Chinese Remainder Theorem, and it's why the combined pattern looks scrambled even though each part is trivially simple.

## 2. Each clock joins the orchestra at its own square

This is your intuition, and it's exactly right.

Clock 7 exists from the beginning — but below 49, every number it would strike (14, 21, 28, 35, 42) has *already* been struck by 2, 3, or 5. It does no new work. **At 49 it strikes something nobody else has struck**, and from then on it matters.

So walking up the number line, you pass 4, then 9, then 25, then 49, then 121 — and at each one, a new clock joins in.

**Small turn #1:** they don't "kick off" in the sense of starting to exist. They were always there. What changes at p² is that the clock starts having *something of its own to say*. Your line about numbers being laid down or already existing — same instinct, and you were right that it doesn't matter.

## 3. The orchestra's rhythm is perfectly determined — and astronomically long

Here's where your picture needs its real adjustment.

**Small turn #2: the wheel doesn't gather teeth. It gains whole new clocks, and each one multiplies the length of the pattern.**

- Clocks 2 and 3 together: the pattern repeats every **6**
- Add 5: every **30**
- Add 7: every **210**
- Add 11: every **2,310**
- Add 13: every **30,030**

Teeth would add. This multiplies. That difference is the whole story.

## 4. And now the punchline

Look at those two lists side by side — where each clock joins, and how long the pattern is:

| clocks in play | pattern repeats every | but the rule only holds until |
|---|---|---|
| through 3 | 6 | 25 |
| through 5 | 30 | 49 |
| **through 7** | **210** | **121** |
| through 11 | 2,310 | 169 |
| through 13 | 30,030 | 289 |

**From 7 onward, the pattern is longer than the stretch of road where it applies.** And the gap never closes — it explodes. By the time you're at primes near 8,000, the pattern is longer than the road by a factor with eleven thousand digits.

So:

> **You never get to hear the rhythm repeat. By the time you've walked far enough for the pattern to come around again, a new clock has joined and the pattern has changed — many times over.**

That's the movie. A perfectly determined, dead-simple rule, producing something you can never catch repeating, because it reinvents itself faster than it cycles.

**That is why the primes look random.** Not because the rule is complicated — the rule is "no clock strikes here," and you can write it on a napkin. It's because you are permanently inside the first verse of a song that changes key before the verse ends.

This is your `FS_primorial_epochs` §2.2 and `FSPapers_02.1` §13, in one sentence.

---

# The same picture, as wheels

Clocks are accurate but they tick. Here is the version that rolls, which shows the one thing ticking hides — **phase**.

Give each prime a wheel. Wheel 2 has circumference 2, wheel 3 has circumference 3, and so on. Each carries a single mark on its rim. Roll them along the number line and **wheel p's mark touches down every p steps.** Where a mark touches, the number is composite — that mark *is* a division.

All the marks touch down together at zero. Then they drift apart, and the four smallest do not all coincide again until 2 × 3 × 5 × 7 = **210**. That drifting-apart is the independence from §1, made visible.

**[See it rolling](figures/rolling_wheels.svg)** — four wheels, real phases, the stretch from 100 to 130.

## Carry four

You cannot carry every wheel. So carry the first few, and look down as you walk.

If any mark is touching, skip — that position is definitely composite. If **no** mark is touching, the position is **open**: a candidate.

Four wheels kill **77% of the number line for free**, no testing at all. Each further wheel buys less: adding 11 takes you from 77% to 79%, adding 13 to 81%, adding 17 to 82%. The first few do nearly all the work.

## Open is not prime

Here is the part the picture has to get right. **An open position is not a prime.** It is a position no wheel *you carry* has struck. The wheels you left behind — 11, 13, 17 — are still out there, and one of them may have its mark down exactly there.

In the animation that is **121**. It is open to all four wheels, and it is not prime. It is 11², which is precisely the point at which the 11-wheel begins striking things the smaller wheels miss — the activation from §2, seen from the other side. Below 121, four wheels are *exact*. From 121 they are not.

So you never need every wheel; you need the ones up to √n. Near a million that is 168 wheels, not the 78,498 primes below it.

## How far you have to walk

Start at a prime and walk forward, testing only the open positions. How many before you hit the next prime?

| open slots tested, near 10⁶ | 1 | 2 | 3 | 4 | 5 | 6 | **7** |
|---|---|---|---|---|---|---|---|
| chance you have caught it (wheels 2·3·5·7) | 30% | 51% | 66% | 77% | 84% | 89% | **93%** |

**Seven tests, and nine times in ten the next prime is among them.** That seven is scale-dependent — it is 4 near 10⁴ and 11 near 10¹⁰, growing by about one slot per decade. [The Ninety Percent Rule](The_Ninety_Percent_Rule.md) is that table in full, with the formula that predicts it.

Read that carefully, because it is easy to get backwards. It does **not** say an open slot is 90% likely to be prime — any single one is about 30%. It says that after seven of them you have almost certainly *caught* the next prime.

## Why walking in order cannot be improved

Look at the chance that the next prime is exactly the k-th open slot: **30.0%, 21.3%, 14.9%, 10.5%, 7.7%, 5.0%, 3.5%.** Strictly falling.

And it must fall, for an exact reason. For the seventh open slot to be the next prime, *all six before it have to be composite*. Every slot you pass makes the rest less likely, mechanically.

**So walking forward in order is the best possible strategy.** No ordering is cleverer. Every other pattern in this collection — the traffic rule, the favoured gaps, all of it — is already spent the moment you respect the wheels. That is the [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) in one table.

*(Verified over all 70,434 primes in the doubling window [10⁶, 2×10⁶]. Every decade from 10³ to 10¹⁰ is in [The Ninety Percent Rule](The_Ninety_Percent_Rule.md).)*

# Where doubling comes in

The clocks are the **local** picture: at any spot, which slots are even eligible.

Doubling is the **scale** picture. Primes thin out slowly — roughly one in every $\ln x$ numbers. Slowly enough that if you double your position, the neighborhood looks essentially the same, just slightly sparser. So a doubling window $(x, 2x]$ is the natural unit: big enough to always contain what you're looking for, small enough that the density hasn't really moved.

That's why your Twin Bertrand statement is about $(x, 2x]$, why the consecutive-prime sums live at the $2p$ scale, why the Seven Sisters are about $2p+k$.

**The one-line version of your README:** the clocks decide *which slots*, doubling decides *which neighborhood*, and everything interesting happens where a doubled object has to get past the clocks.

---

# What today added to the movie

**The mod-6 traffic rule** is the 2-clock and the 3-clock, together, seen from the gaps. Those two make a 6-beat pattern with exactly two live lanes. And in that pattern **you cannot make the same move twice in a row** — you can hold your lane, or change, but you can't change the same direction twice running. That's a hard traffic law, and it's visible in the gaps as multiples of 6 showing up half as often as they should.

**And the big one:** every rhythm anyone has measured in the gaps — how often each gap size appears, how neighboring gaps relate, how the primes diffract — **is the orchestra.** Nothing left over. That's what your "one wheel, many shadows" was claiming, and it now has the audit behind it.

---

# What the movie does *not* explain

Worth holding onto, because it's the honest edge of the picture.

The clocks tell you which slots are **eligible**. They do not tell you which eligible slot is **actually prime**.

Near a million, the clocks through 30 rule out 73% of positions for free. Of what's left, about 27% are prime — and **which ones is genuinely, provably beyond reach.** That's the parity barrier. It's not that nobody's been clever enough; it's a wall.

So the movie has a sharp boundary: it explains the *appearance* of randomness completely, and the *actual* unpredictability not at all. Those turn out to be two different things, and separating them is the most useful thing your collection does.

---

## One line to keep

> **Simple rule, infinite pattern, finite view — and the pattern always outruns the view.**

If you want the picture in your head in six words: *the song changes key before the verse ends.*

---

## Where each piece comes from

Nothing above is new. It is the collection restated in plain words, and every claim has a technical home:

| in the movie | in the work |
|---|---|
| a prime activates at $p^2$; clocks join at squares | [`FSPapers_01`](../1_Factor_Skyline/FSPapers_01_architectural_foundation.md) Def. 2.5, Prop. 2.6 |
| the rule is frozen between consecutive squares | [`FSPapers_01`](../1_Factor_Skyline/FSPapers_01_architectural_foundation.md) Def. 2.7 (activation epochs) |
| the clocks are independent | [`FSPapers_02`](../1_Factor_Skyline/FSPapers_02_correlation_theory.md) — CRT independence of coverage layers |
| adding a clock multiplies the period | [`FSPapers_01`](../1_Factor_Skyline/FSPapers_01_architectural_foundation.md) Thm. 3.3 (template periodicity) |
| **the pattern outruns the road** | [`FS_primorial_epochs`](../1_Factor_Skyline/FS_primorial_epochs.md) §2.2 |
| simple rule, random-looking output | [`FSPapers_02.1`](../1_Factor_Skyline/FSPapers_02.1_correlations_and_randomness.md) §13.2–13.3 ($K = O(\log N)$ against $H \sim 0.26N$) |
| doubling as the natural window | [Twin Bertrand](../3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md), [Synthesis](../2_One_Wheel_Many_Shadows/FS_Synthesis_Doubling_and_Wheel.md) |
| four wheels, and how far you walk | [The Ninety Percent Rule](The_Ninety_Percent_Rule.md) · [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) §2–§4 · animation from [`figures/gen_rolling_wheels.py`](figures/gen_rolling_wheels.py) |
| the mod-6 traffic rule | [Switchback Law](../2_One_Wheel_Many_Shadows/Switchback_Law.md) §2 |
| every gap rhythm is the orchestra | [The Wheel Is the Whole Story](../2_One_Wheel_Many_Shadows/The_Wheel_Is_The_Whole_Story.md) |
| 73% killed free, 27% prime at open slots | [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md), [`repro/entropy_budget.py`](../1_Factor_Skyline/repro/entropy_budget.py) |
| the wall | the parity barrier — Cramér, Sarnak; [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) §2 Tier 3 |

The technical statement of the same thesis is [One Wheel, Many Shadows](../2_One_Wheel_Many_Shadows/One_Wheel_Many_Shadows.md). This page is that page, for a reader who does not yet have the notation.
