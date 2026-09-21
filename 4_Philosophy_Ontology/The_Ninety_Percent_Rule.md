# The Ninety Percent Rule

### A simple rule that predicts primes, and the exact formula behind it

*Companion to [The Movie](The_Movie.md), which is the whole picture. This note is one piece of it, in full.*

*Written 2026-09-20. Every number below comes from [`repro/ninety_percent_table.py`](repro/ninety_percent_table.py); run it and you get this page back.*

---

## The question this whole exercise was for

Can you predict primes with a simple rule, and put a percentage on it?

Not "find a formula that outputs primes" — nobody can do that, and this note will say clearly why not. Something more modest and more useful:

> **Stand on a prime. Point at a small handful of numbers ahead of you. Say: the next prime is one of these, and I'm right nine times in ten.**

That is a real prediction with a real success rate. It turns out you can do it, the handful is small, you need almost nothing to carry, and **the size of the handful is given by a formula that matches measurement at every scale tested.**

Here is the whole thing.

---

## 1. The rule

Carry four wheels: **2, 3, 5, 7.**

Each wheel has one mark on its rim, and it rolls along the number line — wheel $p$'s mark touches down every $p$ steps. Where a mark touches, the number is divisible by that prime, so it is composite. ([See them rolling.](figures/rolling_wheels.svg))

A position no mark touches is **open**.

That's it. Four wheels, and the rule is *look down; if nothing is touching, this one is worth testing.*

**Open is not prime.** It means "no wheel *you carry* has struck it." Bigger primes are still out there, and one of them may land exactly there. Open means *candidate*.

Four wheels repeat every $2 \times 3 \times 5 \times 7 = 210$ steps, and inside those 210 positions exactly **48 are open**. So:

> **77.1% of the number line is eliminated for free** — no testing, no arithmetic, just four wheels and a glance.

## 2. The walk

Stand on a prime. Walk forward. Skip everything the wheels strike. Test the open positions in order.

**How many do you test before you hit the next prime?**

---

# The table

**Four wheels (2, 3, 5, 7) throughout. 90% throughout. Only the slot count moves.**

| standing near | **open slots to test** | actually caught | mean gap ahead | chance the *first* slot is prime | average slots tested |
|---|---|---|---|---|---|
| 10³ | **3** | 91.8% | 7.4 | 59.0% | 1.69 |
| 10⁴ | **4** | 91.2% | 9.7 | 44.0% | 2.21 |
| 10⁵ | **5** | 90.3% | 11.9 | 35.5% | 2.72 |
| 10⁶ | **7** | 92.9% | 14.2 | 30.0% | 3.25 |
| 10⁷ | **8** | 92.3% | 16.2 | 26.1% | 3.70 |
| 10⁸ | **9** | 91.6% | 18.4 | 23.0% | 4.21 |
| 10⁹ | **10** | 90.9% | 20.7 | 20.3% | 4.74 |
| 10¹⁰ | **11** | 90.4% | 23.0 | 18.2% | 5.26 |

Measured over every prime in the window $[N, 2N]$ — one doubling, so the neighbourhood is genuinely local. 70,434 starting primes at 10⁶; 86,816 at 10¹⁰.

**Read it correctly**, because it is easy to flip. It does **not** say an open slot is 90% likely to be prime — near 10¹⁰ any single one is 18%. It says that after **eleven** of them you have almost certainly *caught* the next prime.

**The pattern is: about one extra slot per decade.**

That is the answer to the original question. To find the next prime after a ten-digit number, you have eleven candidates and a nine-in-ten guarantee. You carry four wheels to do it.

---

# And it's predicted exactly

This is the part worth pausing on. The table above is measured. The table below is **computed from two facts, with nothing fitted** — and it lands on the same integer at every one of the eight decades.

## The two facts

**Fact one:** the wheels leave 48 of every 210 positions open. That is 22.9%, and it is exact and permanent — arithmetic, not an observation.

**Fact two:** primes near $N$ have density about $1/\ln N$. That is the Prime Number Theorem, known since 1896.

## Divide them

If primes are $1/\ln N$ of *everything*, and open slots are $48/210$ of everything, then the chance that an **open slot** is prime is one over the other:

$$q = \frac{1/\ln N}{48/210} = \frac{210}{48 \ln N} = \frac{4.375}{\ln N}$$

That is the whole derivation. Prime density divided by survivor density.

## Then it is just coin flips

Each open slot is a shot with probability $q$. To be 90% sure you have hit at least once, you need enough shots that missing every time falls under 10%:

$$(1-q)^k < 0.10 \qquad\Longrightarrow\qquad k = \left\lceil \frac{\ln 0.1}{\ln(1-q)} \right\rceil$$

## Side by side

| near | $q$ predicted | $q$ measured | $k$ predicted | $k$ measured |
|---|---|---|---|---|
| 10³ | 63.3% | 59.0% | **3** | **3** |
| 10⁴ | 47.5% | 44.0% | **4** | **4** |
| 10⁵ | 38.0% | 35.5% | **5** | **5** |
| 10⁶ | 31.7% | 30.0% | **7** | **7** |
| 10⁷ | 27.1% | 26.1% | **8** | **8** |
| 10⁸ | 23.8% | 23.0% | **9** | **9** |
| 10⁹ | 21.1% | 20.3% | **10** | **10** |
| 10¹⁰ | 19.0% | 18.2% | **11** | **11** |

**Eight for eight.**

Be fair about the middle columns: the predicted $q$ runs consistently **1–4 points high**. That is the known slack in $x/\ln x$ against the true prime count, and it is worst at small $N$ where $\ln N$ is a crude estimate. The prediction is a little optimistic every single time. Rounding up absorbs it and the integer comes out right anyway — but the right claim is *"the formula gets the slot count right at every decade tested,"* not *"the formula is exact."*

## The coin flips are honest coin flips

If the walk really is memoryless — each open slot an independent shot at $q$ — then the chance the next prime sits at *exactly* the $k$-th slot should be $q(1-q)^{k-1}$, a plain geometric distribution. Near 10⁶:

| slot | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| measured | 30.0% | 21.3% | 14.9% | 10.5% | 7.7% | 5.0% | 3.5% |
| geometric | 30.0% | 21.0% | 14.7% | 10.3% | 7.2% | 5.1% | 3.5% |

Memoryless to within a few tenths of a point.

**This is the same result as everything else in the collection, arriving from a different direction.** Once the wheel has been taken out, what is left behaves like a fair coin — no further pattern to exploit, no cleverer place to look next. That is the [no-residual finding](../2_One_Wheel_Many_Shadows/The_Wheel_Is_The_Whole_Story.md), showing up here as the fact that a one-parameter coin-flip model fits the walk.

**And it is why walking forward in order cannot be improved on.** The per-slot chances strictly fall — 30.0, 21.3, 14.9, 10.5 — and they *must*, because for slot 7 to be the answer, all six before it have to fail. Every slot you pass makes the rest less likely, mechanically. No reordering beats it.

---

# What the wheels actually buy you

Here is the sharpest thing in this note, and it is not obvious.

At 10¹⁰, holding 90% fixed, here is what carrying more wheels does:

| wheels carried | killed for free | slots to test | **road covered** |
|---|---|---|---|
| 2 | 50.0% | 26 | **52** |
| 2·3 | 66.7% | 17 | **51** |
| 2·3·5 | 73.3% | 13 | **49** |
| **2·3·5·7** | **77.1%** | **11** | **48** |
| 2·3·5·7·11 | 79.2% | 10 | **48** |
| through 13 | 80.8% | 9 | **47** |
| through 19 | 82.9% | 8 | **47** |
| through 31 | 84.7% | 7 | **46** |

The last column — the actual stretch of number line you walk across — **does not move.** Roughly 48 numbers, whatever you carry.

And it cannot move, for a clean reason. The road length is the number of slots times the spacing between slots:

$$k \times \frac{1}{\text{open fraction}} \;\approx\; \frac{\ln 0.1}{-q} \times \frac{1}{\text{open fraction}} \;=\; 2.303\,\ln N$$

The open fraction cancels. **The distance to the next prime is set by $\ln N$ and nothing else.** Near 10¹⁰ that is about 53 numbers of road, and no amount of wheel-carrying shortens it.

> **The wheels don't move the prime. They only decide how much of the road you have to look at.**

Four wheels take you from testing 48 numbers to testing 11 — a **4.4× saving, for four wheels.** Carrying seven more (through 31) gets you from 11 down to 7. The first four do nearly all the work, and that is why four is the right number to hold in your head.

---

# A worked example

The 1000th prime is **7919**. Roll the four wheels forward:

| position | wheels | what happens |
|---|---|---|
| 7920 | struck by 2, 3, 5 | skip |
| **7921** | **open** | test → **composite**, $= 89 \times 89$ |
| 7922–7926 | struck | skip |
| **7927** | **open** | test → **PRIME** |

Two tests. You stepped over eight numbers and looked at two of them.

And 7921 is the honest lesson in miniature: open to all four wheels, and equal to $89^2$ — struck by the 89-wheel, which you are not carrying. **Open is a candidate.** That is the 18-to-30% showing up in a single instance.

*(This mirrors 121 = 11² in [the animation](figures/rolling_wheels.svg) — the smallest number open to four wheels and not prime.)*

---

# What this is not

The honest edge, and it is a hard one.

**This is not a formula for primes.** It predicts *effort*, not *identity*. It tells you how many candidates you need; it does not tell you which candidate. Those are different things, and the gap between them is not a matter of being clever enough.

Near 10¹⁰, eleven open slots sit in front of you and about one is prime. **Which one is genuinely, provably out of reach** — that is the parity barrier, and it is a wall, not a frontier. Sieve methods of this kind cannot in principle tell a prime apart from a product of two primes. Extra wheels do not help: wheels tell you what is *ruled out*, never what is *ruled in*.

**And the 90% is a rate, not a promise.** Nine times in ten your handful contains the next prime. One time in ten it does not, and you keep walking. Prime gaps have no upper bound — somewhere out there is a stretch where you test thirty slots and find nothing. The rule is a statistical guarantee across many starting points, not a certificate about any one of them.

So the honest summary:

> **The structure is completely understood and completely spent.** The wheels explain everything that can be explained about where to look — and then they stop, exactly at the point where you would want them to tell you the answer.

That boundary is sharp, and finding out *where* it sits is the actual result. The rule above is the structure side of it, measured to the last decade.

---

## One line to keep

> **Four wheels, eleven guesses, ninety percent, ten billion.**

And the formula that says so: $q = 4.375/\ln N$, then flip that coin until you are 90% sure.

---

## Reproducing it

```bash
python 4_Philosophy_Ontology/repro/ninety_percent_table.py
```

A couple of minutes, standard library only. It segments the sieve — base primes to $\sqrt{2N}$ — so the 10¹⁰ row needs a sieve to 150,000, not to ten billion.

## Where the pieces come from

| in this note | in the work |
|---|---|
| the wheel, and why 48/210 | [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) §2–§4 |
| four wheels exact below 121; activation at $p^2$ | [`FSPapers_01`](../1_Factor_Skyline/FSPapers_01_architectural_foundation.md) Def. 2.5 |
| the walk is memoryless once the wheel is out | [The Wheel Is the Whole Story](../2_One_Wheel_Many_Shadows/The_Wheel_Is_The_Whole_Story.md) |
| the doubling window $[N, 2N]$ as the natural unit | [Synthesis](../2_One_Wheel_Many_Shadows/FS_Synthesis_Doubling_and_Wheel.md) |
| the wall | the parity barrier — [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) §2, Tier 3 |
| the whole picture this is one piece of | [The Movie](The_Movie.md) |
