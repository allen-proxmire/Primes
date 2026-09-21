# The Ninety Percent Rule

### A simple rule that predicts primes, and the exact formula behind it

*Companion to [The Movie](The_Movie.md), which is the whole picture. This note is one piece of it, in full.*

*Written 2026-09-20; "Far out" and "Looking back" added 2026-09-21. Every number below comes from [`repro/ninety_percent_table.py`](repro/ninety_percent_table.py) or, for the look-back section, [`repro/lookback_test.py`](repro/lookback_test.py). Run them and you get this page back.*

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

At 10¹⁰, holding 90% fixed, here is what carrying more wheels does (computed from the formula above, which the eight-for-eight table vouches for, rather than walked):

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

# Far out: the largest known prime

*Added 2026-09-21. This is the formula carried far past anything measured. It's a prediction, not a result.*

The largest known prime is $2^{136{,}279{,}841} - 1$. As a power of ten it's about $10^{41{,}024{,}319.9}$, a number with **41,024,320 digits**. The table above stops at ten digits.

The formula doesn't care. Same two facts, same steps:

- $\ln N = 136{,}279{,}841 \times \ln 2 \approx 94{,}461{,}988$
- $q = 4.375/\ln N$: about **1 open slot in 21.6 million** is prime
- slots for 90%: **49,715,831, about $10^{7.7}$**

| standing near | slots for 90%, four wheels |
|---|---|
| 10¹⁰ | 11 |
| $10^{41{,}024{,}320}$ | **~49.7 million** |

The "one extra slot per decade" rule is only a small-$N$ approximation. In general the slot count grows like about $0.53 \times \ln N$, and here $\ln N$ is 94 million.

**This is where the road result matters most.** The stretch you walk is $2.303 \ln N \approx$ **217 million numbers**, however many wheels you carry. Carrying more only cuts how much of it you test:

| wheels carried | slots to test for 90% |
|---|---|
| 2, 3, 5, 7 | ~49.7 million |
| every prime up to 10⁶ | ~8.8 million |
| every prime up to 10⁹ | ~5.9 million |
| every prime up to 10¹² | ~4.4 million |

*(Deeper-sieve rows use Mertens' theorem for the fraction left open, so they're approximations too.)*

At this size a million wheels are cheap to carry and well worth it. That's what real prime searches do: they sieve out small factors very deeply before running any expensive test.

**Two honest caveats.**

1. **Nobody can check this.** It extends the table across 41 million orders of magnitude. The two facts still hold out there: the wheel's 48/210 is exact arithmetic, and the Prime Number Theorem is proven. What's assumed is that open slots act like independent coin flips. That held to within a few tenths of a point up to 10¹⁰, but it's a heuristic (the Cramér model), not a theorem.
2. **Each slot is a huge test.** A single primality test on a 41-million-digit number takes something like a day on a fast GPU (a rough figure). Even the best case above, ~4.4 million tests, would take thousands of GPU-years. The rule says how many candidates there are, not that anyone can afford to test them. That's why nobody knows the next prime after this one, even though we can say with some confidence that 9 times in 10 it's within the next ~217 million numbers.

For scale: 217 million is about $10^{-41{,}024{,}312}$ of the prime itself. On that scale the next prime is practically touching it, and still nobody knows which number it is.

---

# Looking back: can the last few primes help?

*Added 2026-09-21. Numbers from [`repro/lookback_test.py`](repro/lookback_test.py), over all 70,435 primes in [10⁶, 2×10⁶].*

A natural extra heuristic. Before walking forward, look at the handful of primes *behind* you. The prime-triangle angle wobbles and changes direction often, so guess which way it turns next, and use that to decide where to look.

It splits into two questions. Does the **direction** of the last step help? Does its **size** help?

## Direction: no

The guess "the next move reverses the last one" is right **68.6%** of the time. That sounds useful. But shuffle the same gaps into random order, make the same guess, and it's right **69.2%** of the time.

Shuffled numbers zig-zag just as much, for a plain reason: after a big value the next is probably smaller, because big values are rare, and after a small one the next is probably bigger. Any random sequence reverses direction about two-thirds of the time. That's the [Differencing Trap](../2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md), and the zig-zag is arithmetic, not primes.

A guess that uses *no history at all*, just "the next gap moves back toward a typical size," does better: **77.1%**.

And direction doesn't change the walk:

| what you know before walking | average slots | caught within 7 | 90% at |
|---|---|---|---|
| nothing | 3.25 | 92.9% | 7 |
| last move was **up** | 3.22 | 92.9% | 7 |
| last move was **down** | 3.27 | 92.8% | 7 |
| last gap was **big** | 3.15 | 93.6% | **6** |
| last gap was **small** | 3.32 | 92.3% | 7 |

## Size: a sliver

The last two rows are different. After a big gap, the next prime comes slightly sooner: **0.18 fewer slots on average**, and 90% arrives one slot earlier. It's small, but it's real in this data.

## Is the sliver the wheel?

To find out, build fake primes that contain *only* wheel structure. Strike the multiples of every prime up to some limit, then keep survivors at random, matched to the real prime count. Walk them with the same four wheels and measure the same sliver.

| fake primes built from | sliver | share of the real one | pool ratio |
|---|---|---|---|
| **real primes** | **0.178** | 100% | — |
| wheels 2, 3, 5, 7 | 0.001 | **1%** | 3.25 |
| wheels up to 11 | 0.023 | 13% | 2.95 |
| wheels up to 13 | 0.041 | 23% | 2.72 |
| wheels up to 31 | 0.111 | 63% | 2.17 |
| wheels up to 100 | 0.127 | 71% | 1.71 |
| wheels up to 300 | 0.151 | **85%** | 1.38 |
| wheels up to 700 | 0.150 | 84% | 1.15 |
| wheels up to 1000 | 0.167 | 94% | 1.05 *(nearly the real primes, so it proves nothing)* |

*Averaged over 12 random fakes per row; standard errors 0.003–0.008. The pool ratio is how many survivors the fake had to throw away at random. The nearer it is to 1, the less randomness the fake has left.*

What the table shows:

1. **With your four wheels, the sliver is zero.** Those four have nothing to say about it.
2. **Each wheel you add brings more of it back.** Wheel 11 gives an eighth, 13 about a quarter, 31 nearly two-thirds, and by 300 about 85%.
3. **The fakes stall at about 85%.** They only get further as the pool ratio heads to 1, when the fake is no longer fake: it simply *is* the primes, and matching them is automatic. That's the circular-row trap from [the Null-Model Discipline](../2_One_Wheel_Many_Shadows/Null_Model_Discipline.md).

The stall is partly the fakes' own fault. Throwing survivors away at random creates artificial big gaps that carry no wheel information, and those water the effect down. So the last 15% needs a test with no fakes in it.

## Closing the gap: group the real walks

Keep the real primes and their real walks. For each starting prime, write down exactly which of the next 12 open slots the wheels up to some limit strike. Primes with the same pattern face the same wheel-struck road ahead. Now compare big-last-gap against small-last-gap **inside each group**.

If the sliver is carried by where those wheels strike, it should vanish inside the groups. Whatever survives the grouping is something the wheels don't explain.

On the bigger window [10⁷, 2×10⁷], with 606,028 starting primes:

| group by wheels up to | sliver left over | explained | spread of the walk left inside groups |
|---|---|---|---|
| — (no grouping) | 0.148 | 0% | 3.11 |
| 7 | 0.148 | 0% | 3.11 |
| 11 | 0.122 | 18% | 3.09 |
| 13 | 0.097 | 34% | 3.07 |
| 31 | 0.039 | 74% | 2.96 |
| 100 | 0.011 | 92% | 2.79 |
| 300 | **−0.001 ± 0.006** | **100%** | 2.56 |

With wheels up to 300, **nothing is left over.** The leftover is −0.001, and the error bar is ±0.006.

**The last column shows it isn't circular.** Inside each group the real walks still vary almost as much as before, 2.56 slots against 3.11. If the grouping had quietly rebuilt the primes, that spread would collapse toward zero. At this size you'd need wheels up to about 4,500 to rebuild the primes, and 300 is far short of that. Nothing is simulated and no coin density is chosen: every number is a real walk.

The same test on [10⁶, 2×10⁶] agrees but is noisier, with 0.017 ± 0.017 left over at 300. That's consistent with zero, but the error bar there is as big as the leftover, which is why the bigger window was needed.

So the answer is: **the sliver is the wheel.** All of it, within a margin of about 0.01 slots. It's specifically the wheels from 11 to about 300 that you aren't carrying, showing through the size of the last gap.

## Why the bigger wheels would do this

The grouping test shows *where* the sliver lives: in the pattern those wheels strike on the road ahead. This is the likely *why*, though it's an explanation rather than a separate test. A big last gap means the stretch behind you was full of numbers struck by wheels you weren't carrying: 11, 13, 17 and up. Each of those strikes only once every p steps. If its mark came down just behind you, it's that much further from coming down in the next few slots. So after a long empty stretch, the road ahead is slightly less likely to be struck by the big wheels, and the next prime comes a little sooner.

The size of the last gap is a rough readout of where the uncarried wheels are in their turn.

## What it means

> **Looking back is a cheap, blurry way of carrying more wheels.**

Carry them for real, by sieving out 11, 13, 17 and so on, and you get that information directly and precisely. The look-back then has nothing left to add. It also never changes the *strategy*. Even after a big gap you still walk the open slots in order, because the first one is still the most likely. History can make the forecast slightly better. It never makes the search better.

Direction carries nothing. Size carries a little, and that little is wheels you didn't bring.

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

A couple of minutes, standard library only. It also prints the largest-known-prime extrapolation. It segments the sieve — base primes to $\sqrt{2N}$ — so the 10¹⁰ row needs a sieve to 150,000, not to ten billion.

```bash
python 4_Philosophy_Ontology/repro/lookback_test.py
```

The look-back section: the zig-zag test, the conditional walk, and the fake-primes comparison. A minute or two; needs numpy.

## Where the pieces come from

| in this note | in the work |
|---|---|
| the wheel, and why 48/210 | [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) §2–§4 |
| four wheels exact below 121; activation at $p^2$ | [`FSPapers_01`](../1_Factor_Skyline/FSPapers_01_architectural_foundation.md) Def. 2.5 |
| the walk is memoryless once the wheel is out | [The Wheel Is the Whole Story](../2_One_Wheel_Many_Shadows/The_Wheel_Is_The_Whole_Story.md) |
| the zig-zag is what any random sequence does | [Differencing Trap](../2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md) |
| fake primes, pool ratios, and the circular row | [Null-Model Discipline](../2_One_Wheel_Many_Shadows/Null_Model_Discipline.md) |
| the doubling window $[N, 2N]$ as the natural unit | [Synthesis](../2_One_Wheel_Many_Shadows/FS_Synthesis_Doubling_and_Wheel.md) |
| the wall | the parity barrier — [Prediction Budget](../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md) §2, Tier 3 |
| the whole picture this is one piece of | [The Movie](The_Movie.md) |
