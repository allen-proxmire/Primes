# The Primes in Plain Language

### What is going on with the primes, without notation

Every claim here is carried by a technical paper; the pointers are at the end. For every result with its formula, see [Results](../RESULTS.md).

---

## 1. Every prime is a wheel

Give each prime a wheel with one mark on its rim, and roll it along the number line. The 2-wheel's mark touches down on every second number, the 3-wheel's on every third, the 5-wheel's on every fifth. A number is prime when **no wheel's mark touches it** — that is the definition, restated.

The wheels are **independent**: where the 3-wheel is in its turn says nothing about where the 5-wheel is (the Chinese Remainder Theorem). That is why the combined pattern looks scrambled even though each part is trivially simple.

## 2. Each wheel joins at its own square

The 7-wheel rolls from the start, but below 49 every number its mark touches (14, 21, 28, 35, 42) has already been touched by 2, 3 or 5. **At 49 it marks something no smaller wheel has**, and from then on it matters. Walking up the number line you pass 4, 9, 25, 49, 121 — and at each square a new wheel starts having something of its own to say.

## 3. The rhythm is fully determined — and astronomically long

Each new wheel does not add a tooth to the pattern. It **multiplies its length**:

- the 2-3-wheel: the pattern repeats every **6**
- add 5: every **30**
- add 7: every **210**
- add 11: every **2,310**
- add 13: every **30,030**

## 4. The punchline

Put where each wheel joins next to how long the pattern is:

| wheels in play | pattern repeats every | the rule holds only until |
|---|---|---|
| through 3 | 6 | 25 |
| through 5 | 30 | 49 |
| **through 7** | **210** | **121** |
| through 11 | 2,310 | 169 |
| through 13 | 30,030 | 289 |

**From 7 onward the pattern is longer than the stretch of road where it applies**, and the gap never closes — near the prime 8,000 the pattern is longer than its road by a factor with eleven thousand digits.

> The rhythm is never heard to repeat. Before the pattern can come round again, a new wheel has joined and the pattern has changed — many times over.

**That is why the primes look random.** Not because the rule is complicated — "no wheel marks this number" fits on a napkin — but because the view is permanently inside the first verse of a song that changes key before the verse ends.

---

## 5. Carrying the wheels

All the marks touch together at zero, then drift apart; the four smallest do not coincide again until $2\times3\times5\times7 = 210$. **[See them rolling](figures/rolling_wheels.svg)** — the stretch from 100 to 130.

**Carry four.** Walk forward and look down: if any mark is touching, skip; if none is, the position is **open** — a candidate. Four wheels remove **77% of the number line** with no testing. Each further wheel buys less: 11 takes it to 79%, 13 to 81%, 17 to 82%.

**Open is not prime.** An open position is one no *carried* wheel has struck. In the animation, **121** is open to all four wheels and is $11^2$ — exactly where the 11-wheel starts striking what the smaller wheels miss. Below 121, four wheels are exact; from 121 they are not. To be exact up to $n$ you need the wheels up to $\sqrt n$: near a million that is 168 wheels, not the 78,498 primes below it.

**How far to walk.** From a prime, test only open positions:

| open slots tested, near $10^6$ | 1 | 2 | 3 | 4 | 5 | 6 | **7** |
|---|---|---|---|---|---|---|---|
| chance the next prime is caught | 30% | 51% | 66% | 77% | 84% | 89% | **93%** |

Seven tests, and nine times in ten the next prime is among them. That seven grows by about one per decade — 4 near $10^4$, 11 near $10^{10}$ — and a two-line formula predicts it ([Predicting the Next Prime](../2_One_Wheel_Many_Shadows/Predicting_the_Next_Prime.md)). It does not say an open slot is 90% likely to be prime; any single one is about 30%.

**Walking in order cannot be beaten.** The chance the next prime is exactly the $k$-th open slot falls: 30.0%, 21.3%, 14.9%, 10.5%, 7.7%, 5.0%, 3.5%. It must fall — for slot 7 to win, all six before it have to fail. Every other pattern in the collection is already spent once the wheels are respected.

---

## 6. Where doubling comes in

The wheels are the local picture: which slots are eligible. Doubling is the scale picture. Primes thin out slowly — about one in every $\ln x$ numbers — so doubling your position leaves the neighbourhood nearly the same, slightly sparser. A doubling window $(x, 2x]$ is the natural unit: big enough to contain what you are looking for, small enough that the density has hardly moved. That is why the twin conjecture is about $(x, 2x]$, why consecutive-prime sums live at the $2p$ scale, and why the Seven Sisters are about $2p + k$.

> The wheels decide which slots, doubling decides which neighbourhood, and everything interesting happens where a doubled object has to get past the wheels.

**The traffic rule** is the 2-wheel and the 3-wheel together, seen from the gaps: a 6-beat pattern with two live lanes, in which the same lane change can never happen twice in a row — so gaps changing by 6 turn up half as often as they otherwise would.

**And every rhythm measured in the gaps** — how often each gap appears, how neighbouring gaps relate, how the primes diffract — is the wheels. Nothing is left over.

---

## 7. What this picture does not explain

The wheels say which slots are **eligible**. They do not say which eligible slot is **prime**. Near a million the 30-wheel removes 73% of positions for free, and about 29% of what is left is prime — which ones is provably beyond reach of any method built from the wheels. That is the parity barrier.

So the picture explains the *appearance* of randomness completely and the *actual* unpredictability not at all.

> **Simple rule, infinite pattern, finite view — and the pattern always outruns the view.**

---

## Where each piece comes from

| in this picture | in the work |
|---|---|
| wheels join at squares; the rule is fixed between squares | [Factor Skyline §2](../1_Factor_Skyline/Factor_Skyline.md) |
| a new wheel multiplies the period | [Factor Skyline §2](../1_Factor_Skyline/Factor_Skyline.md) |
| the pattern outruns the road | [Factor Skyline §4](../1_Factor_Skyline/Factor_Skyline.md) |
| simple rule, random-looking output | [Factor Skyline §5](../1_Factor_Skyline/Factor_Skyline.md) |
| doubling as the natural window | [Twin Bertrand](../3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md), [Consecutive-Prime Sums](../2_One_Wheel_Many_Shadows/Consecutive_Prime_Sums.md) |
| four wheels and how far to walk | [Predicting the Next Prime](../2_One_Wheel_Many_Shadows/Predicting_the_Next_Prime.md) |
| the traffic rule | [The Traffic Law](../2_One_Wheel_Many_Shadows/Traffic_Law.md) |
| every gap rhythm is the wheels | [One Wheel, Many Shadows](../2_One_Wheel_Many_Shadows/One_Wheel_Many_Shadows.md) |
| the wall | the parity barrier — [Predicting the Next Prime §10](../2_One_Wheel_Many_Shadows/Predicting_the_Next_Prime.md) |
