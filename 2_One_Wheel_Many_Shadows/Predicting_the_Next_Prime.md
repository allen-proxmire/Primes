# Predicting the Next Prime

### Four wheels, eleven guesses, ninety percent, ten billion — and the wall behind them

Allen Proxmire

---

## Summary

Stand on a prime, carry the wheels 2, 3, 5, 7, and test only the positions none of them strikes, in order. The number of tests needed to catch the next prime 90% of the time is

| $N$ | $10^3$ | $10^4$ | $10^5$ | $10^6$ | $10^7$ | $10^8$ | $10^9$ | $10^{10}$ |
|---|---|---|---|---|---|---|---|---|
| slots | 3 | 4 | 5 | 7 | 8 | 9 | 10 | 11 |

and that count is **predicted with nothing fitted** by
$$q = \frac{210}{48\ln N} = \frac{4.375}{\ln N}, \qquad k = \left\lceil \frac{\ln 0.1}{\ln(1-q)} \right\rceil .$$
Every other regularity in the collection adds nothing to this, because walking the open slots in order is already optimal. Which open slot is prime is the parity barrier.

The ingredients are classical (prime number theorem, Hardy–Littlewood, Cramér, the parity barrier). What is added is the calibration: one rule, one formula, measured at eight decades.

---

## 1. The rule

Each wheel $p$ strikes every $p$-th position, marking it composite. A position no carried wheel strikes is **open** — a candidate, not a prime. The four wheels repeat every $2\cdot3\cdot5\cdot7 = 210$ steps and leave exactly 48 positions open:
$$1 - \frac{48}{210} = 77.1\% \text{ of the number line eliminated with no test.}$$
([See them rolling.](../4_Philosophy_Ontology/figures/rolling_wheels.svg))

---

## 2. The measurement

Over every prime in $[N, 2N]$ (70,434 starting primes at $10^6$; 86,816 at $10^{10}$):

| near | slots for 90% | caught | mean gap ahead | first slot prime | mean slots tested |
|---|---|---|---|---|---|
| $10^3$ | **3** | 91.8% | 7.4 | 59.0% | 1.69 |
| $10^4$ | **4** | 91.2% | 9.7 | 44.0% | 2.21 |
| $10^5$ | **5** | 90.3% | 11.9 | 35.5% | 2.72 |
| $10^6$ | **7** | 92.9% | 14.2 | 30.0% | 3.25 |
| $10^7$ | **8** | 92.3% | 16.2 | 26.1% | 3.70 |
| $10^8$ | **9** | 91.6% | 18.4 | 23.0% | 4.21 |
| $10^9$ | **10** | 90.9% | 20.7 | 20.3% | 4.74 |
| $10^{10}$ | **11** | 90.4% | 23.0 | 18.2% | 5.26 |

About one extra slot per decade. The table does not say an open slot is 90% likely to be prime — near $10^{10}$ a single one is 18%. It says that after eleven, the next prime has almost certainly been caught.

With the mod-30 wheel (2, 3, 5) instead, near $10^6$ the count is 8 (mean 3.79 tests).

---

## 3. The formula

**Two facts.** The wheels leave $48/210$ of positions open (exact). Primes near $N$ have density $1/\ln N$ (prime number theorem). So the chance an open slot is prime is
$$q = \frac{1/\ln N}{48/210} = \frac{4.375}{\ln N} .$$
Treat each open slot as an independent shot at $q$; 90% needs $(1-q)^k < 0.1$:

| near | $q$ predicted | $q$ measured | $k$ predicted | $k$ measured |
|---|---|---|---|---|
| $10^3$ | 63.3% | 59.0% | **3** | **3** |
| $10^4$ | 47.5% | 44.0% | **4** | **4** |
| $10^5$ | 38.0% | 35.5% | **5** | **5** |
| $10^6$ | 31.7% | 30.0% | **7** | **7** |
| $10^7$ | 27.1% | 26.1% | **8** | **8** |
| $10^8$ | 23.8% | 23.0% | **9** | **9** |
| $10^9$ | 21.1% | 20.3% | **10** | **10** |
| $10^{10}$ | 19.0% | 18.2% | **11** | **11** |

Eight for eight on the integer. The predicted $q$ runs 1–4 points high throughout — the slack between $x/\ln x$ and the true prime count — so the claim is the right slot count, not the exact probability.

**The walk is memoryless.** If the shots are independent, the next prime sits at exactly slot $k$ with probability $q(1-q)^{k-1}$. Near $10^6$:

| slot | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| measured | 30.0% | 21.3% | 14.9% | 10.5% | 7.7% | 5.0% | 3.5% |
| geometric | 30.0% | 21.0% | 14.7% | 10.3% | 7.2% | 5.1% | 3.5% |

Once the wheel is taken out, what remains behaves like a fair coin — the [no-residual result](One_Wheel_Many_Shadows.md) seen from another side.

---

## 4. Walking in order is optimal

For slot $k$ to be the answer, all earlier open slots must be composite, so the chance the next prime is at slot $k$ strictly decreases in $k$. Walking the open slots in order is Bayes-optimal, and no other regularity can reorder it. Tested directly on 26,723 primes near $3\times10^6$:

| ranking | mean tests | first test right | within 3 |
|---|---|---|---|
| walk the open slots in order | 3.99 | 23.5% | 56.8% |
| reweighted by gap frequencies | 3.99 | 23.5% | 56.8% |
| conditioned on recent gap history | 3.99 | 23.5% | 56.8% |

Gap-frequency reweighting never puts a different slot first. Conditioning on recent history moves the mean by $+0.0007$.

**The regularities that add nothing** — all real, all the wheel in another form: jumping champions $6, 30, 210$; the lag-1 gap anti-correlation $-0.05$; the [traffic law](Traffic_Law.md); the Lemke Oliver–Soundararajan residue bias; the [Seven Sisters](Seven_Sisters.md); the balance ratio. Each is already spent once admissibility is respected.

---

## 5. What the wheels buy, and what they don't

At $10^{10}$, holding 90% fixed (from the formula):

| wheels carried | eliminated free | slots to test | road covered |
|---|---|---|---|
| 2 | 50.0% | 26 | 52 |
| 2·3 | 66.7% | 17 | 51 |
| 2·3·5 | 73.3% | 13 | 49 |
| **2·3·5·7** | **77.1%** | **11** | **48** |
| through 11 | 79.2% | 10 | 48 |
| through 13 | 80.8% | 9 | 47 |
| through 31 | 84.7% | 7 | 46 |

The road covered does not move. Slots times spacing is
$$k \cdot \frac{1}{\text{open fraction}} \approx \frac{\ln 0.1}{-q}\cdot\frac{1}{\text{open fraction}} = 2.303\,\ln N ,$$
and the open fraction cancels. **The wheels decide how much of the road is tested, never where the prime is.** Four wheels take 48 tests down to 11; seven more take 11 to 7.

---

## 6. The information budget

On the Factor Skyline, at $N = 10^4$, the next-step uncertainty is
$$H(dx) = 2.48 \text{ bits} = \underbrace{1.70}_{\text{template (the wheel)}} + \underbrace{0.26}_{\text{escape}} + \underbrace{0.52}_{\text{activation}} .$$
The template's 1.70 bits is stable across three decades; activation (which least prime factor a composite has) grows with $N$ and is irrelevant to locating a prime. The binary statement that bears on prediction is stable: the mod-30 wheel removes 73.3% of positions for free, and an open slot still carries $\approx 0.84$ bits. The 0.26-bit escape — which open slot is prime — is the parity barrier. → [`entropy_budget.py`](../1_Factor_Skyline/repro/entropy_budget.py)

**The wheel is cheap to carry.** Three sizes get called "the wheel":

| | what it is | size in $p_k$ |
|---|---|---|
| program | bits to write the rule, $\sum_{i\le k}\log_2 p_i$ | $\approx 1.4427\,p_k$ — linear |
| territory | integers it decides, everything below $p_{k+1}^2$ | $p_k^2$ — quadratic |
| period | the unrolled pattern, the primorial | $2^{1.4427\,p_k}$ — exponential |

What is carried is the program, linear against a quadratic territory, so the cost per decided integer is $1.4427/p_k$ bits and falls to zero:

| $p_k$ | cost of one more prime | new integers decided | integers per bit |
|---|---|---|---|
| 29 | 4.95 bits | 408 | 82 |
| 7,919 | 12.95 bits | 95,160 | 7,346 |
| 1,299,709 | 20.31 bits | 57,188,208 | 2,815,797 |

The exponential size is the period, not a cost: from $p \ge 5$ the period outruns the epoch in which the rule is fixed, so the template is never seen to repeat ([Factor Skyline](../1_Factor_Skyline/Factor_Skyline.md)).

---

## 7. Looking back adds nothing beyond the wheel

Over the 70,435 primes in $[10^6, 2\times10^6]$:

**Direction carries nothing.** "The next move reverses the last" is right 68.6% of the time — and 69.2% on shuffled gaps. Any sequence zig-zags (the $-\frac12$ identity of [Gap Correlations §2](Gap_Correlations.md)).

| known before walking | mean slots | caught within 7 | 90% at |
|---|---|---|---|
| nothing | 3.25 | 92.9% | 7 |
| last move up | 3.22 | 92.9% | 7 |
| last move down | 3.27 | 92.8% | 7 |
| last gap big | 3.15 | 93.6% | 6 |
| last gap small | 3.32 | 92.3% | 7 |

**Size carries a sliver, and the sliver is the wheel.** After a big gap the next prime comes 0.18 slots sooner. Group the real walks by which of the next 12 open slots the wheels up to $Q$ strike, and compare big-last-gap against small-last-gap inside each group. On $[10^7, 2\times10^7]$ (606,028 starting primes):

| grouped by wheels up to | sliver left | explained | spread left inside groups |
|---|---|---|---|
| — | 0.148 | 0% | 3.11 |
| 11 | 0.122 | 18% | 3.09 |
| 31 | 0.039 | 74% | 2.96 |
| 100 | 0.011 | 92% | 2.79 |
| **300** | $\mathbf{-0.001 \pm 0.006}$ | **100%** | 2.56 |

Nothing is left at $Q = 300$, and the walks still vary almost as much inside each group (2.56 against 3.11), so the grouping has not rebuilt the primes. The size of the last gap is a blurred readout of the wheels 11 to ~300 not being carried. Sieve them directly and the look-back has nothing to add; it never changes the strategy.

---

## 8. Far out

The largest known prime, $2^{136{,}279{,}841} - 1 \approx 10^{41{,}024{,}319.9}$, has $\ln N \approx 94{,}461{,}988$. The formula gives $q \approx 1/21.6$ million and **about 49.7 million slots** for 90% with four wheels; in general $k \approx 0.53\ln N$. The road is $2.303\ln N \approx 217$ million numbers whatever is carried; deeper sieving (Mertens' theorem for the open fraction) cuts the tests to ~8.8 million with every prime up to $10^6$, ~4.4 million up to $10^{12}$.

This is extrapolation across 41 million orders of magnitude: the 48/210 and the prime number theorem hold, but independence of open slots is the Cramér heuristic, checked only to $10^{10}$.

---

## 9. A worked example

From the 1000th prime, 7919: 7920 is struck by 2, 3, 5; **7921** is open — test: $89 \times 89$, composite; 7922–7926 struck; **7927** open — prime. Two tests. 7921 is open to all four wheels and struck by the 89-wheel, which is not carried: open is a candidate.

---

## 10. The wall

This predicts **effort, not identity**. Near $10^{10}$ eleven open slots lie ahead and about one is prime; which one is out of reach. Sieve methods cannot distinguish a prime from a product of two primes (the parity barrier), and more wheels say only what is ruled out, never what is ruled in. The 90% is a rate over many starting points; prime gaps are unbounded, so somewhere thirty slots will find nothing.

---

## Reproduction

```bash
python 2_One_Wheel_Many_Shadows/repro/ninety_percent_table.py   # §2, §3, §8 — standard library, a few minutes
python 2_One_Wheel_Many_Shadows/repro/lookback_test.py          # §7 — numpy, a minute or two
python 1_Factor_Skyline/repro/entropy_budget.py                 # §6
```

The sieve is segmented (base primes to $\sqrt{2N}$), so the $10^{10}$ row needs a sieve only to 150,000.

## References

- G. H. Hardy, J. E. Littlewood, *Partitio numerorum III* (1923).
- A. M. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experimental Math. **8** (1999).
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS (2016).
- H. Cramér, *On the order of magnitude of the difference between consecutive prime numbers*, Acta Arith. **2** (1936); P. Sarnak, *Möbius randomness and dynamics* (2011).
