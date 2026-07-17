# The Switchback Law

### The prime-angle sign sequence is scale-invariant — the same seesaw in the hundreds and the millions

Allen Proxmire · July 2026

> **What this is.** An empirical regularity with a clean lens and one open thread. The Prime-Triangle angle wobbles under its $45°$ ceiling; strip away the *size* of the wobble and keep only the **sign** of each change (up or down), and that sign-sequence — how often it flips, how long same-direction runs last — is **the same at every scale**, even as the wobble itself shrinks by orders of magnitude. It also yields a usable **betting rule** for the next sign, and its fine structure is the wheel. Tags: **[emp]** measured · **[null]** shuffle-controlled · **[interp]** placement · **[resolved]** the $\bmod 6$ dip = leading-order Hardy–Littlewood, matched to $0.1$ point (§5). Companion: [*The Prime-Triangle Angle*](PG_Angle_Wobble.md) (the wobble and its ceiling); [*Prime-Gap Memory and the Differencing Trap*](Prime_Gap_Memory_Differencing_Trap.md) (the two-null discipline used here).

*Placement up front (no inflation): this is a fresh, visual face of something number theory already expects — the **scale-invariance of the normalized local statistics of primes** (the Cramér / Hardy–Littlewood picture). It is not a new theorem. Its value is the lens (it makes that invariance graspable and turns it into a rule you can use) and the $\bmod 6$ fine structure (§5). It sits alongside the other shadows in this collection, not above them.*

---

## 1. The object: switchbacks

For consecutive primes, the Prime-Triangle angle is $\alpha_n = \arctan(p_n/p_{n+1}) \approx 45° - \tfrac{90}{\pi}\,g_n/p_{n+1}$ — a rescaled gap, pinned just under $45°$. Its **change** $\Delta\alpha_n = \alpha_n-\alpha_{n-1}$ carries a sign: **up** (the gap shrank, the angle rose toward the ceiling) or **down** (the gap grew). Reading only that sign, the sequence is a string of switchbacks: $-\,-\,+\,-\,+\,+\,-\,\dots$

On the ordinary number line this sign-structure is invisible — "this gap, then subtract that gap, then the next" has no picture. The triangle is what renders it; that is why the pattern is *seeable* at all.

## 2. The run-length law

Same-direction runs are short, and they die **faster than a coin.** Over the primes in $[10^6,3\times10^6]$:

| run of length | share of runs | a fair coin would give |
|---|---|---|
| 1 | 63.1% | 50% |
| 2 | 27.3% | 25% |
| 3 | 7.7% | 12.5% |
| 4 | 1.6% | 6.25% |
| 5 | 0.3% | 3.1% |
| 6–7 | 0.07% | 1.6% |

**[emp]** Each extra same-sign step is ~4–5× less likely than the last — the sequence *over-alternates* relative to random. Equivalently, the **reversal probability climbs with run length**:

| after a run of… | the next change flips |
|---|---|
| 1 | 63% |
| 2 | 74% |
| 3 | 80% |
| 4 | 82% |

So the sign is genuinely **predictable**: once you have seen two or three moves the same way, bet on a reversal and you are right three or four times out of five. (This is the discipline the wobble note's "runs $\approx 1/3$" constant pointed at, now read as a usable table.)

## 3. The law is scale-invariant — the headline

The *amplitude* of the wobble collapses with scale — $\mathrm{RMS}(\Delta\alpha)\approx 33\ln p/p$, four orders of magnitude smaller near $10^6$ than near $10^2$. The **sign-structure does not move at all:**

| run length | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| **hundreds** (first 1000 primes) | 62.2% | 29.5% | 6.9% | 1.3% | — | — |
| **millions** ($[10^6,3\times10^6]$) | 63.1% | 27.3% | 7.7% | 1.6% | 0.3% | 0.06% |

The two distributions are the same. In the first thousand primes there are **exactly nine** runs of length four and none longer; in the millions the identical *rate* produces occasional 5s, 6s, a rare 7 — so "four is the maximum" is a sample-size floor, not a hard ceiling, but the **law generating it is fixed across scale.** Zoom into the millions and the switchbacks look exactly like the hundreds. *This is the point of the note.*

## 4. Why the runs die fast: the ceiling, felt from the changes

The over-alternation is the boundedness of the angle seen from the change side. Because primes increase with bounded gaps, $\alpha$ is trapped in a shrinking band below $45°$; it cannot drift, so its changes cannot run the same way for long without being pulled back — an **overcorrection** that always returns the angle to the band (and, being a return, tends to overshoot, seeding the next reversal). That this is structural and not generic noise is shown in the companion note by the two-null test: shuffle the *gaps* and the band-and-cancellation survive; shuffle the *changes* and let them free-float, and the reconstructed angle wanders straight through $45°$. The switchback tightness is held in place by the primes being a real monotone, bounded-gap sequence.

## 5. The fine structure is the wheel: a $\bmod 6$ suppression

Within the sign-law lives an arithmetic fingerprint. Look at the size of the gap-change, $|\Delta g| = |g_{n+1}-g_n|$, over $[10^6,3\times10^6]$:

| $|\Delta g|$ | 2 | 4 | **6** | 8 | 10 | **12** | 14 |
|---|---|---|---|---|---|---|---|
| frequency | 16.8% | 13.3% | **5.1%** | 11.4% | 8.8% | **3.0%** | 6.6% |

**[emp]** The multiples of 6 are **suppressed** — sharp local minima at 6 and 12. Since gaps are even, $|\Delta g|\equiv 0 \pmod 6$ means two consecutive gaps are *congruent* $\bmod 6$; the dip says **consecutive gaps avoid repeating their residue $\bmod 6$.** Quantitatively the avoidance is nearly 2-to-1: the same-residue rate is $0.176$ against $0.348$ if consecutive gaps were independent.

**Does Hardy–Littlewood predict it? Yes — to the digit.** Build the leading-order singular-series local model (the wheel-Cramér surrogate: small-prime divisibility exact, everything else independent random) and read off its $|\Delta g|$ distribution:

| $|\Delta g|$ | 4 | **6** | 8 | 10 | **12** | 14 |
|---|---|---|---|---|---|---|
| real primes $>10^6$ | 12.70% | **5.09%** | 10.94% | 8.62% | **2.99%** | 6.62% |
| wheel model | 12.66% | **5.09%** | 10.85% | 8.59% | **3.01%** | 6.63% |

The model reproduces the whole distribution — **including the dip depths at 6 ($5.09$ vs $5.09$) and 12 ($2.99$ vs $3.01$)** — to within $0.1$ point. So the $\bmod 6$ suppression is a **leading-order Hardy–Littlewood effect**, exactly: the singular series forces consecutive gaps to avoid a shared residue, and the wheel model that encodes it lands on the measured depths.

**[resolved, with a small tail]** On top of the leading term sits a **Lemke Oliver–Soundararajan lower-order correction.** The same-residue bias runs slightly deeper at small scale and fades toward the wheel's asymptotic value — $-0.193$ at $10^4$, $-0.180$ at $10^5$, $-0.174$ at $10^6$, $-0.171$ at $10^7$ — the characteristic slow ($\sim 1/\log$) decay of the LOS secondary bias (the "unexpected biases in consecutive primes," 2016). So the dip is Hardy–Littlewood to leading order (matched to the digit) plus a decaying LOS tail. The thread closes where it should: it *is* the wheel.

## 6. Where it lands, and what it's good for

**Prediction.** The betting table of §2 is scale-invariant (§3), so it *transfers*: hunting the sign-rhythm around a record prime, the wobble sizes up there are meaningless, but the run-length odds you learned in the hundreds are exactly the odds in the billions. Combined with the Seven-Sisters generator ($2p+k$ for the wheel-strong offsets), this is the honest content of "how to guess where the next prime leans" — not a formula, a *rhythm with known odds*.

**Placement, plainly.** The switchback law is a real, clean, scale-invariant regularity — but it is a *consequence* of the conjectured scale-invariance of normalized prime local statistics, not a new fact about the deep structure of primes. Its contribution is the **lens** (it makes that invariance visible and usable, through the angle sign-sequence that the number line hides) and the **$\bmod 6$ fine structure** (§5), which ties it back to the wheel. It is one more shadow — the seesaw one — not a summit.

---

## Appendix. Reproduction

```python
import math, bisect
from collections import Counter, defaultdict
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
B=sieve(3_000_000); allp=[i for i in range(2,3_000_000) if B[i]]
def runs_and_reversal(P):
    a=[math.degrees(math.atan(P[i]/P[i+1])) for i in range(len(P)-1)]
    da=[a[i+1]-a[i] for i in range(len(a)-1)]
    s=[1 if d>0 else -1 if d<0 else 0 for d in da]
    runlen=Counter(); i=0
    while i<len(s):
        j=i
        while j<len(s) and s[j]==s[i] and s[i]!=0: j+=1
        if s[i]!=0: runlen[j-i]+=1
        i=max(j,i+1)
    return runlen
i1=bisect.bisect_left(allp,1_000_000); i2=bisect.bisect_left(allp,3_000_000)
print('hundreds:', runs_and_reversal(allp[:1000]))
print('millions:', runs_and_reversal(allp[i1:i2]))
# mod-6 suppression:
g=[allp[i+1]-allp[i] for i in range(i1,i2)]
print(Counter(abs(g[i+1]-g[i]) for i in range(len(g)-1)).most_common(8))
```

## References

- A. Proxmire, *The Prime-Triangle Angle* (this collection) — the wobble, the $45°$ ceiling, the $33\ln p/p$ envelope.
- A. Proxmire, *Prime-Gap Memory and the Differencing Trap* (this collection) — the two-null discipline (shuffle gaps vs shuffle changes) used in §4.
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes* (PNAS, 2016) — the residue-correlation mechanism behind the $\bmod 6$ suppression of §5.
- Empirical basis: *Prime Trigonometry Data* (author's spreadsheet, first 1000 pairs) cross-checked against a sieve to $3\times10^6$.
