# The Switchback Law

### What survives is a hard mod-6 traffic law on consecutive gaps. What doesn't is the run-length law — that one is generic.

Allen Proxmire · July 2026 · **v2, revised September 2026**

> **What changed in v2, and it is not cosmetic.** The original paper led with a *sign* law: same-direction runs of the prime-angle change die faster than a coin, identically in the hundreds and the millions. **That headline does not survive a transform-matched null and has been demoted** (§3). The comparison was against a fair coin, and differencing already beats a coin — the precise error this collection's companion note exists to prevent.
>
> What survives is the paper's §5, now promoted to the front: a **hard combinatorial rule** on consecutive gaps mod 6 that forbids two specific transitions outright, halves the frequency of $|\Delta g| \in \{6, 12\}$ against a matched null, and is reproduced by the wheel to a tenth of a point. That result is stronger than the one it replaces, because it is a *rule*, not a bias.
>
> Tags: **[fact]** exact · **[emp]** measured · **[null]** against a stated null · **[mirage]** demoted. Companions: [*Prime-Gap Memory and the Differencing Trap*](Prime_Gap_Memory_Differencing_Trap.md) (the null that broke §3), [*The Null-Model Discipline*](Null_Model_Discipline.md) (the failure mode, named), [*The Prime-Triangle Angle*](PG_Angle_Wobble.md) (the wobble and its ceiling). Reproduce with [`repro/`](repro/).

---

## 1. The object: switchbacks

For consecutive primes, the Prime-Triangle angle is $\alpha_n = \arctan(p_n/p_{n+1}) \approx 45° - \tfrac{90}{\pi}\,g_n/p_{n+1}$ — a rescaled gap, pinned just under $45°$. Its **change** $\Delta\alpha_n = \alpha_n-\alpha_{n-1}$ carries a sign: **up** (the gap shrank, the angle rose toward the ceiling) or **down** (the gap grew). Reading only that sign, the sequence is a string of switchbacks: $-\,-\,+\,-\,+\,+\,-\,\dots$

On the ordinary number line this sign-structure is invisible — "this gap, then subtract that gap, then the next" has no picture. The triangle is what renders it. **That much stands**; what the rendering *shows* is the subject of §2 and §3, and they part company.

---

## 2. The result: a hard mod-6 traffic law

### 2.1 The rule

Every prime past 3 sits in one of two residue classes mod 3 — call them **teams**. A gap is the step between consecutive primes, so it either **stays** on a team ($g \equiv 0 \bmod 6$) or **switches** — up ($1\!\to\!2$, $g \equiv 4$) or down ($2\!\to\!1$, $g \equiv 2$).

You cannot make the same switch twice running. After a down-switch you are *on* team 1, so the next step starts from team 1: it can stay, or switch up, but it can never switch down again.

> **Two consecutive gaps can never both be $\equiv 2$, nor both $\equiv 4 \pmod 6$.** **[fact]**

Not a bias — a prohibition. The transition matrix over $[10^6, 3\times10^6)$ carries the zeros exactly:

| current gap | → next $\equiv 0$ | → next $\equiv 2$ | → next $\equiv 4$ |
|---|---|---|---|
| $\equiv 0$ (stay) | 40.4% | 29.8% | 29.8% |
| $\equiv 2$ (switch down) | 44.8% | **0.0%** | 55.2% |
| $\equiv 4$ (switch up) | 44.7% | 55.3% | **0.0%** |

Under a gap-shuffle those zeros become $28.4\%$ and $28.5\%$ — the shuffle destroys the rule, which is exactly why it is the right null here.

A clean corollary, measured and exceptionless: **the only gaps that can repeat immediately are multiples of 6.** Over this range $3.39\%$ of steps repeat a gap, and the number of repeats by a gap *not* divisible by 6 is **zero**.

### 2.2 The dip, against the correct null

The rule shows up as a suppression of $|\Delta g|$ at multiples of 6. Against a **gap-shuffled null** — same multiset of gaps, order destroyed, then differenced:

| $\lvert\Delta g\rvert$ | real | gap-shuffled null | ratio |
|---|---|---|---|
| 2 | 16.80% | 12.64% | 1.33 |
| 4 | 13.29% | 11.70% | 1.14 |
| **6** | **5.14%** | **10.29%** | **0.50** |
| 8 | 11.35% | 8.67% | 1.31 |
| 10 | 8.78% | 7.30% | 1.20 |
| **12** | **2.98%** | **6.57%** | **0.45** |
| 14 | 6.57% | 5.17% | 1.27 |

**[emp/null]** The multiples of 6 are cut to **half** the null's rate; every other value is *elevated*. The mechanism is visible in the table above: $|\Delta g| = 6$ requires two same-residue gaps differing by 6, and the $(2,2)$ and $(4,4)$ routes ($2\,\&\,8$, $4\,\&\,10$) are forbidden. Every observed $|\Delta g| = 6$ comes through the one surviving $(0,0)$ channel — $6\,\&\,12$, $12\,\&\,18$.

**This is the test the original paper never ran on its headline.** Run here on the fine structure, it passes by a factor of two.

### 2.3 The rule tiers with the modulus

The same team logic applied to $5, 7, \dots$ forbids progressively more:

| clock | gap-sizes that occur | can repeat | **forbidden to repeat** | same-residue rate vs chance |
|---|---|---|---|---|
| mod 6 | 3 | 1 | **2** | 17% vs 35% |
| mod 30 | 15 | 5 | **10** | 4% vs 9% |
| mod 210 | 66 | 23 | **43** | 3.3% vs 7.5% |

### 2.4 It is the wheel, to the digit

The wheel-Cramér surrogate — small-prime divisibility exact, everything else independent random — reproduces the whole $|\Delta g|$ distribution, dip depths and all: $6$: $5.09$ vs $5.09\%$; $12$: $2.99$ vs $3.01\%$ — within $0.1$ point. Precisely *because* it respects divisibility by 3, it inherits the hard zeros for free.

**[resolved: hard rule + soft tail]** On top of the hard skeleton rides a **Lemke Oliver–Soundararajan** lean: among the *allowed* moves, primes prefer to keep switching teams over staying (the $55/45$ split above), and the residual same-residue deficit fades slowly with scale — $-0.193$ at $10^4$ to $-0.171$ at $10^7$, the $\sim\!1/\log$ LOS decay. So the mod-6 suppression is **mostly a hard mod-3 traffic law with the LOS lean layered over it**, and the wheel model, respecting both, lands on the measured depths.

### 2.5 The same rule, found again from the other side

In September 2026 this rule was rediscovered independently, from the Eisenstein integers, while examining an unrelated statistic. With half-gaps $h = g/2$, the Loeschian form satisfies $3 \mid (h_1^2 + h_1h_2 + h_2^2) \iff g_1 \equiv g_2 \pmod 6$ — and by §2.1 that forces both $\equiv 0$. So **"3 divides the Eisenstein norm of the half-gap pair" and "two consecutive gaps are both multiples of 6" are the same event**, and both are this section's rule. See [*The balance ratio* §2.1](PG_Balance_Ratio_And_Koide.md). Two routes, one traffic law.

---

## 3. What was demoted: the run-length law is generic

### 3.1 The original claim

Same-direction runs are short and die *faster than a coin*. Over $[10^6, 3\times10^6)$ the original reported $63.1 / 27.3 / 7.7 / 1.6\%$ for run lengths $1$–$4$ against a coin's $50 / 25 / 12.5 / 6.25\%$, with reversal odds climbing $63 \to 74 \to 80 \to 82\%$. Headline: the sign is **predictable**, and the distribution is **identical in the hundreds and the millions** even as the amplitude collapses by $10^4$.

### 3.2 The coin is the wrong baseline

Differencing forces $\operatorname{corr}(\Delta g_n, \Delta g_{n-1}) = -\tfrac12$ on **any** sequence — an exact identity, proved in [*Differencing Trap* §4](Prime_Gap_Memory_Differencing_Trap.md). A coin was never the alternative. Against the transform-matched null — shuffle the gaps, *then* difference — over $[10^6, 5\times10^6)$:

| | run 1 | run 2 | run 3 | run 4 |
|---|---|---|---|---|
| real primes | 64.00% | 27.25% | 7.18% | 1.34% |
| **gap-shuffled null** | **64.66%** | **27.31%** | **6.74%** | **1.13%** |
| a fair coin | 50% | 25% | 12.5% | 6.25% |

Reversal odds: real $64.0 \to 75.7 \to 82.1 \to 85.5$, null $64.7 \to 77.3 \to 83.9 \to 87.6$ — **the null is if anything slightly higher.**

**[mirage] The run-length law is a property of any increasing, bounded-gap sequence, not of the primes.**

### 3.3 The mechanism was right; the attribution was wrong

The original §4 explained the over-alternation correctly: $\alpha$ is trapped in a shrinking band below $45°$, so its changes cannot run the same way for long without being pulled back, and the return overshoots, seeding the next reversal.

**That mechanism is real — and it is a property of the *skeleton*, not the wheel.** A gap-shuffle keeps the gaps positive, so the shuffled sequence still increases with bounded steps and still has the ceiling. The mechanism therefore applies to the null too, which is why the null shows the same run structure.

**The error was using the wrong one of two nulls the companion paper had already distinguished.** The original defended the law with the *change*-shuffle, which free-floats the increments and tests whether the monotone skeleton matters — and it does. But "this is a fact about primes" requires the *gap*-shuffle, which preserves the skeleton and tests the wheel. Match the null to the claim, or a generic fact reads as arithmetic. Named as failure mode 2 in [*The Null-Model Discipline*](Null_Model_Discipline.md).

### 3.4 What is left of it

- **The scale-invariance is a genuine observation, with its explanation inverted.** The distribution *is* the same in the hundreds ($62.2/29.5/6.9/1.3\%$) and the millions ($63.1/27.3/7.7/1.6\%$) while the amplitude falls $10^4$-fold. But it is invariant **because it is a universal artifact of differencing**, which has no scale in it — not because the primes obey a law across scales. Still worth seeing; no longer a prime fact.
- **The betting rule still works.** After two or three moves the same way, bet on a reversal and you are right three or four times in five. It simply works on any such sequence, so it tells you nothing about primes and buys nothing the [*Prediction Budget*](Prime_Prediction_Budget.md) has not already spent.
- **The triangle as a *lens* survives** (§1). Rendering the sign structure is what made the mod-6 traffic law visible in the first place — §2 was found by looking at $|\Delta g|$, which is a change-space object.

---

## 4. What the correction is worth

**Two months standing, one test to fall.** The run-length law was published in July and broke in September under a null that this collection had already written down, in a companion paper, cited by this one. Nothing exotic was needed — shuffle the gaps, then difference.

**The honest reading is not "the paper was wrong" but "the paper compared against the wrong thing."** Every number in §3.1 is correctly measured. They were simply measured against a coin when the alternative was an exact $-\tfrac12$ correlation that no sequence escapes.

**And the demotion improved the paper.** What is left is a hard combinatorial rule with exact zeros, a factor-of-two effect against the correct null, reproduction by the wheel to a tenth of a point, and an independent rediscovery from a different area of mathematics. That is a better result than a sign-prediction table — it is just smaller and less exciting to look at, which is presumably why it was not the headline the first time.

---

## 5. Honest ledger

**Classical.** The mod-3 team structure is elementary and certainly known; the wheel is Hardy–Littlewood; the LOS lean is Lemke Oliver–Soundararajan (2016). The $-\tfrac12$ differencing identity is textbook.

**What this note contributes.** The traffic-law framing of the mod-6 dip — stating it as a *transition prohibition* with exact zeros rather than a statistical suppression — its verification against a matched null, and the tiering table showing how the prohibition scales with the modulus.

**What it retracts.** The run-length/scale-invariance headline as a statement about primes. Retained as an observation about monotone bounded-gap sequences, with the null on the record.

**Not claimed.** Any statement about *which* open slot is prime. The escape is untouched.

---

## Appendix. Reproduction

```python
import random, collections
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
B=sieve(3_000_000); P=[i for i in range(1_000_000,3_000_000) if B[i]]
g=[P[i+1]-P[i] for i in range(len(P)-1)]

# 2.1 the hard zeros
T=collections.Counter((g[i]%6,g[i+1]%6) for i in range(len(g)-1))
for a in (0,2,4):
    tot=sum(T[(a,b)] for b in (0,2,4))
    print(a,[round(100*T[(a,b)]/tot,1) for b in (0,2,4)])
# -> (2,2) and (4,4) are exactly 0.0

# 2.2 the dip, against the CORRECT null
d=lambda s: collections.Counter(abs(s[i+1]-s[i]) for i in range(len(s)-1))
real=d(g); gs=list(g); random.shuffle(gs); null=d(gs)
n=len(g)-1
for k in (2,4,6,8,10,12,14):
    print(k, round(100*real[k]/n,2), round(100*null[k]/n,2))
# -> 6 and 12 are halved; everything else is elevated

# 3.2 the demoted claim: runs, real vs the same null
# (see repro/regenerate_tables.py for the full comparison)
```

Full tables: [`repro/regenerate_tables.py`](repro/).

## References

- G. H. Hardy, J. E. Littlewood, *Partitio numerorum III* (1923) — the singular series.
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS (2016) — the soft lean on top of the hard rule.
- A. Proxmire, *Prime-Gap Memory and the Differencing Trap* (this collection) — the $-\tfrac12$ identity and the two-null distinction this paper originally misapplied.
- A. Proxmire, *The Null-Model Discipline* (this collection) — the failure mode, named and catalogued.
- A. Proxmire, *The Prime-Triangle Angle* (this collection) — the wobble, the ceiling, and the universal runs constant that should have been the warning.
- A. Proxmire, *The balance ratio* §2.1 (this collection) — the same rule reached from the Eisenstein integers.
