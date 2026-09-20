# The Prime Prediction Budget

### How far structure gets you toward the next prime, and the wall it hits

Allen Proxmire · July 2026

> **What this is.** A synthesis — an honest ledger, not a discovery. It stacks *every* usable regularity for locating a prime, sorts what actually pays from what is the same fact in disguise, and reads off the information-theoretic ceiling that caps the whole game. **Every ingredient is classical** — the prime number theorem, the Hardy–Littlewood wheel, the Cramér model, the parity barrier (Sarnak's Möbius randomness). What this note adds is the *assembly*: one calibrated budget, anchored to the Factor Skyline entropy numbers, that says precisely how far you can get and where you provably stop. Tags: **[deriv]** from known theory · **[emp]** measured here · **[interp]** synthesis. Companions: [*Switchback Law*](Switchback_Law.md), [*Prime-Gap Memory and the Differencing Trap*](Prime_Gap_Memory_Differencing_Trap.md), [*The Prime-Triangle Angle*](PG_Angle_Wobble.md), [*Seven Sisters*](FS_Seven_Sisters_Wheel_Asymptote.md).

---

## 1. The question, posed so it has an answer

"Predict the next prime" is the wrong target — the exact prime is not predictable, and the whole point of this note is *why*. The right target is bounded: **from a known prime $p$, how few candidates must you test to be, say, $90\%$ sure you have caught the next prime — and what stops you from doing better?** That question has a clean, quantitative answer, and the answer is almost entirely *one* structure.

## 2. The budget, in three tiers

**Tier 1 — load-bearing (this is essentially all of it).**

- **Base rate (PNT).** Near $x$, an integer is prime with probability $\sim 1/\ln x$; the expected gap is $\ln x$. This sets the scale — look near $p+\ln p$.
- **The wheel (admissibility).** Only positions coprime to the small primes can be prime: the mod-30 wheel leaves $8/30$ of integers open, mod-210 leaves $48/210$ — killing $73$–$77\%$ of all positions *for free*, with no test. This is the singular series / Hardy–Littlewood structure, and in Factor-Skyline entropy terms it is worth **$\approx 1.70$ bits** of the $\approx 2.48$-bit local uncertainty — about $68\%$ of everything knowable.

**Tier 2 — real, but not extra bits (the wheel wearing hats).**

Each of these is a genuine, measured regularity; none of them *adds* predictive power beyond Tier 1, because each is a face of the same wheel:

| regularity | what it is | (established in) |
|---|---|---|
| jumping champions $6,30,210$ | the wheel's favoured gaps | classical (Odlyzko–Rubinstein–Wolf) |
| gap anti-correlation $-0.05$ | big gap → smaller next | wheel's consecutive-gap memory |
| switchback sign-law (reversal $63\!\to\!82\%$) | runs die faster than a coin | [Switchback Law](Switchback_Law.md) |
| mod-6 / LOS bias | consecutive gaps avoid a shared residue | Lemke Oliver–Soundararajan |
| Seven Sisters ($2p+k$, $\sim80\%$) | the wheel at the doubled scale | [Seven Sisters](FS_Seven_Sisters_Wheel_Asymptote.md) |

**Tier 3 — the wall.**

- **The escape / parity barrier.** After the wheel, the residual — *which* open slot is actually prime — is genuinely random: the Möbius/Cramér noise, the parity barrier. In the FS entropy budget this irreducible core is only about **$0.26$ bits** (its peak). It is not hard to compute; it is *impossible* to predict. This is the wall, and it is what "the information theory of primes" means.

## 3. The number: ~7–8 candidates for 90%

Put Tier 1 to work — from $p$, walk *up the wheel-open slots* and test them in order — and measure how many you need. Over the primes near $10^6$:

| open slots tested | 1 | 2 | 3 | 4 | 5 | 6 | **7** | **8** |
|---|---|---|---|---|---|---|---|---|
| P(next prime caught), mod-210 | 30% | 52% | 67% | 77% | 85% | **90%** | 93% | 95% |
| P(next prime caught), mod-30 | 25% | 45% | 60% | 71% | 79% | 85% | 89% | **92%** |

**[emp]** So: **the next prime is within the next ~7 (mod-210) or ~8 (mod-30) wheel-open slots about $90\%$ of the time** — a mean of ~3.2–3.7 tests. That $90\%$ is bought *entirely* by base rate + wheel.

## 4. Why the rest of the list doesn't help — and why that's the point

It is tempting to think the Tier-2 biases should tighten the list. They do not, and the reason is exact: to land on the $k$-th open slot, every earlier open slot must be composite, so $P(\text{next prime}=k\text{-th slot})$ **strictly decreases in $k$** — *walking up in order is already the Bayes-optimal search.* Reweighting the candidates by gap-frequency never moves a different slot to the front ($0\%$ of cases), and the full recent-history "regime" lever — given every advantage — shifts the mean rank by $+0.0007$. The biases are real physics of the wheel; they are simply *already spent* the moment you respect admissibility. Everything past the wheel is the $0.26$-bit escape, and the escape is, by theorem-strength heuristic, unbeatable.

So the honest ceiling is not "predict the prime." It is: **pin it to ~7–8 candidates with $90\%$ confidence, and know that no cleverness — no bias, no history, no lens — does better, because the remainder is the parity barrier.** The wheel alone already touches that ceiling; the entire rest of this collection is the wheel proving, six different ways, that it is the whole story.

## 5. Honest ledger

Nothing here is new mathematics. The wheel is Hardy–Littlewood; the ceiling is Cramér and Sarnak; "primes are unpredictable past the density" is the working assumption of the whole field. The contribution of this note is **calibration and assembly** — one page that separates the load-bearing structure from its many disguises, attaches the FS entropy numbers ($1.70$ bits captured, $\sim0.26$ irreducible), and states the reachable target as a number ($\sim8$ candidates for $90\%$) rather than a hope. Its value is knowing *exactly* how far to trust structure, and exactly where to stop trying.

---

## Appendix. Reproduction

```python
import bisect
from math import gcd
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
B=sieve(2_000_000)
primes=[i for i in range(1_000_000,1_500_000) if B[i]]
def slots_for_90(wm):
    ranks=[]
    for p in primes:
        k=0; n=p
        while True:
            n+=1
            if gcd(n,wm)!=1: continue     # skip non-wheel-open positions
            k+=1
            if B[n]: ranks.append(k); break
    ranks.sort()
    for k in range(1,20):
        if sum(1 for r in ranks if r<=k)/len(ranks) >= 0.90: return k
print('mod-30:', slots_for_90(30), ' mod-210:', slots_for_90(210))   # 8, 7
```

## References

- Prime number theorem; G. H. Hardy & J. E. Littlewood, *Partitio numerorum III* (1923) — the singular series (the wheel).
- A. M. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions* (Exp. Math., 1999).
- R. J. Lemke Oliver & K. Soundararajan, *Unexpected biases in consecutive primes* (PNAS, 2016).
- H. Cramér, *On the order of magnitude of the difference between consecutive prime numbers* (1936); P. Sarnak, *Möbius randomness and dynamics* (2011) — the escape / parity barrier.
- A. Proxmire, *Factor Skyline* (this collection) — the entropy budget ($H\approx2.48$ bits, template $\approx1.70$, escape $\approx0.26$); *Switchback Law*, *Differencing Trap*, *Seven Sisters* — the Tier-2 regularities and the Bayes-optimality of walking the wheel.
