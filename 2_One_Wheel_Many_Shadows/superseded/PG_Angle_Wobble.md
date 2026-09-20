# The Prime-Triangle Angle: a Lens on Gaps, its Ceiling, and its Wheel

Allen Proxmire

July 2026

---

## Abstract

The Prime Triangle assigns each consecutive prime pair $(p_n, p_{n+1})$ an angle $\alpha_n = \arctan(p_n/p_{n+1})$. This note shows that the angle is, to leading order, a **rescaled prime gap**, and reads the entire behavior of the angle sequence off of the gaps. Three things fall out: (i) $\alpha_n \approx 45° - \frac{90}{\pi}\cdot\frac{g_n}{p_{n+1}}$, so the angle sequence rises to $45°$ in **gap-family arcs** — twins on top — and $45°$ is a ceiling it approaches from below but never reaches; (ii) the *wobble* of the angle is ~99% what any random sequence does (a $\log p/p$ envelope, a $1/3$ run constant, a $2/3$ self-cancellation — the last being the exact $-\tfrac12$ recoil that differencing forces on any sequence); (iii) the one genuine prime signal — a ~1% excess self-correction — is a **wheel-driven consecutive-gap anti-correlation**, reproduced by building the primorial wheel up prime-by-prime. (This is the *derived* form of the wheel's structure, consistent with but not identical to the Hardy–Littlewood pair-correlation, which is a separate, *positive* object; §4 keeps the two apart.) The angle picture thus has two named imperfections: a *geometric* ceiling and an *arithmetic* wheel — the latter the same wheel behind jumping champions, the Seven Sisters, and the forbidden gap-widths $\{2,4,6,10\}$.

---

## 1. The angle is a rescaled gap

For consecutive primes with gap $g_n = p_{n+1}-p_n$, write $p_n/p_{n+1} = 1 - g_n/p_{n+1}$. Since $\arctan(1-\varepsilon) = \tfrac{\pi}{4} - \tfrac{\varepsilon}{2} + O(\varepsilon^2)$,

$$\boxed{\ \alpha_n \;\approx\; 45° \;-\; \frac{90}{\pi}\cdot\frac{g_n}{p_{n+1}}\ } \tag{1}$$

**[verified]** to a fraction of a degree for all but the tiniest primes. So $\alpha$ is a direct readout of the **relative gap** $g/p$: twins ($g=2$) sit closest to $45°$, and each larger gap sits proportionally lower.

Consequently the angle sequence, plotted in order, rises to $45°$ along **gap-family arcs** — one curve $\alpha = 45° - \frac{90}{\pi}g/p$ per gap value $g$, fanning open with $p$ (Figure `figures/PG_alpha_gap_arcs.png`). The twins form the topmost arc; cousins the next; and so on. The "cloud approaching $45°$" is a *stack of gap-curves*, not a single trend line.

## 2. The ceiling

Because $p_n < p_{n+1}$ always, $\alpha_n < 45°$ **strictly, for every pair** — the angle approaches $45°$ from below and never reaches or crosses it. This is a one-sided ceiling, not a center. That the ceiling — and the tight change-cancellation beneath it (§3) — is *structural*, not a statistical accident, has a one-line proof: shuffle the gaps and it survives (they stay positive, so the sequence still climbs); but shuffle the *changes* and let them free-float, and the reconstructed angle wanders straight through $45°$ (and far below). The balancing is held in place only by the primes being a genuine increasing, bounded-gap sequence — which is why on the ordinary number line, where that sign-structure of successive gaps is invisible, the effect cannot be seen at all; the triangle is what renders it. The band of angles lives entirely underneath it, at mean distance

$$45° - \overline{\alpha} \;\approx\; \frac{90}{\pi}\cdot\frac{\overline{g}}{p} \;\approx\; \frac{90}{\pi}\cdot\frac{\log p}{p} \;\to\; 0,$$

shrinking but never closing (measured: $0.46°$ at $p\sim300$, $0.0003°$ at $p\sim1.6\times10^6$). The tightest triangles — the top of the band — are exactly the twin primes, which connects (1) to the **Angle-Record Theorem** (PG II): every angle record with $p_n\ge3$ is a twin, equivalent to the Twin-Prime Bertrand Postulate.

A small directional consequence: the change $\Delta\alpha_n$ is **up 52% / down 48%** of the time (**[empirical]**), a hair off $50/50$. The excess is entirely the ~4% of steps where the gap *repeats* ($\Delta g=0$): a repeated gap on a larger prime is a tighter triangle, so those steps all tick the angle up. Standing still counts as creeping toward the ceiling.

### 2.1 The same story in Factor Skyline units (trig-free)

The angle carries no information the **relative gap** does not: by (1), $\alpha_n = \arctan(p_n/p_{n+1})$ is just $r_n = g_n/p_n$ wearing a trig coat. Drop the coat and work with $r_n$ directly — the Factor-Skyline-native quantity, since on the skyline a gap is a *vertical step on the escape diagonal* and $r_n$ is that step measured against the height already climbed. Then the $45°$ ceiling becomes the plain statement $r_n \to 0$ (steps vanish relative to $p$); the gap-family arcs become the level sets $r = g/p$; and the twins are the **record-small** relative gaps.

In these units the interleave observation loses its trigonometry and reads directly: *twins are the record-small relative gaps, and between two twin records every step is relatively larger — every non-twin "falls short"* — which is exactly the Angle-Record Theorem, hence the Twin-Prime Bertrand Postulate. The payoff of dropping the arctan is that $r = g/p$ snaps straight onto the wheel: the reason non-twins cannot out-tighten the last twin (small relative gaps cannot cluster) is the *same* $-0.05$ gap anti-correlation of §4, the same singular series, the same forbidden-width obstruction — no longer reached *through* a transcendental function but read off the gaps themselves. PG draws the prettiest picture (the bounded ceiling, the arcs); FS states the cleanest mechanism (relative gap + wheel). Same theorem, two sets of clothes.

## 3. The wobble is (mostly) universal

Differencing (1), $\Delta\alpha_n \approx -\frac{90}{\pi}\cdot\frac{\Delta g_n}{p_n}$ — the change in angle is *minus the change in gap*, damped by $1/p$. Three consequences, all **[empirical]** and all generic:

- **Envelope.** The wobble amplitude decays as $\mathrm{RMS}(\Delta\alpha)\approx 33\,\dfrac{\log p}{p}$ degrees — a hair slower than $1/p$ because gaps themselves grow like $\log p$. This is the damped-oscillation envelope of the change-in-angle plot.
- **Net drift $\approx 0$.** The signed changes telescope to $(\alpha_{\text{last}}-\alpha_{\text{first}})/N$; over the first 1000 pairs the mean change is $+0.0113°$ — negligible next to typical steps of $\sim0.15°$.
- **Runs.** Given the angle just moved up, it moves up again only $\approx 1/3$ of the time — the **universal runs constant** for differences of any near-independent sequence (two of six orderings of three values are monotone). Equivalently, the next block of a few pairs *undoes* the last block $\approx 2/3$ of the time. Shuffling the gaps into random order reproduces both to within ~1%.

None of §3 is special to primes; it is what differences of a random-ish, bounded sequence always look like. The hard core of this universality is exact: the first difference of *any* i.i.d. sequence has lag-1 autocorrelation $-\tfrac12$ (it shares the term $g_n$ with its neighbor), which *is* the "spike-and-return" recoil — no prime memory required. The companion note [*Prime-Gap Memory and the Differencing Trap*](Prime_Gap_Memory_Differencing_Trap.md) isolates what the wobble carries *beyond* this artifact, using the transform-matched null (shuffle the gaps, **then** difference).

## 4. The 1% signal: a wheel-driven gap anti-correlation

The one place the primes deviate from a random-ordered surrogate is a **~1% excess self-correction**, and it is a real gap statistic: consecutive prime gaps are **anti-correlated**,

$$\mathrm{corr}(g_n, g_{n+1}) \approx -0.05 \quad (\text{shuffled}: \approx 0),$$

**[empirical]** — a big gap tends to be followed by a smaller one. This is *not* the geometric ceiling (the shuffle keeps the ceiling and gives $\approx 0$); it is arithmetic. Building a "Cramér-on-the-wheel" surrogate (random primes respecting divisibility by $2,3,5,\dots$ but no other memory) reproduces it, prime by prime:

| wheel through prime | $\mathrm{corr}(g_n,g_{n+1})$ | % of real |
|---|---|---|
| 7 | −0.020 | 40% |
| 11 | −0.024 | 48% |
| 13 | −0.030 | 60% |
| 17 | −0.031 | 62% |
| 19 | −0.037 | 74% |
| **real primes** | **−0.050** | 100% |

Each prime added to the wheel deepens the anti-correlation with steps that show no decay; through prime 19 the pure-wheel model already reaches three-quarters of the real value, and the tail supplies the rest. The effect weakens with scale ($-0.10$ near $10^{3.5}$ to $-0.05$ near $10^6$), as the small-prime constraints matter relatively less on larger gaps.

**A caution on the label.** Three things are easily — and were, in an earlier draft — collapsed into the word "Hardy–Littlewood"; they must be kept apart:

- **Hardy–Littlewood proper** is a statement about prime *pairs at a fixed offset* — the singular series $\mathfrak S(g)$, which is *positive* and offset-dependent (offset 6 twice baseline, offset 30 higher still). That is the object measured directly in the [Offset-Correlation Curve](Offset_Correlation_Curve.md), and it is what "HL" actually asserts.
- **This $-0.05$** is a *derived consecutive-gap* statistic: it requires "next prime" (nothing prime in between), so it follows from the tuple structure only through inclusion–exclusion, not from $\mathfrak S(g)$ directly. It is *reproduced by the wheel* (the table above), hence **wheel-consistent** — but it is not the direct HL prediction and should not be written "$=$ Hardy–Littlewood."
- **The change-space recoil** — "a big *change* is followed by a big opposite *change*," $\mathrm{corr}(\Delta g_n,\Delta g_{n-1})\approx-0.51$ — is neither. It is the $-\tfrac12$ differencing artifact of §3 (any sequence) plus a tiny wheel excess; that excess, $\approx-0.01$, is the *same* $-0.05$ seen in change-coordinates. See [Prime-Gap Memory and the Differencing Trap](Prime_Gap_Memory_Differencing_Trap.md).

So the honest statement is: the 1% self-correction is the **wheel's fingerprint on consecutive gaps, consistent with — but not the direct form of — the Hardy–Littlewood singular series.** Whether the full HL/wheel prediction lands *exactly* on the measured $-0.05$ is an empirical match to model, tested in §4.1.

### 4.1 Does the wheel actually predict the measured value? (test)

To check the attribution without circularity, build exactly the model the label claims — **small-prime divisibility exact, everything else independent random** — and read off its consecutive-gap correlation. Concretely: keep the integers coprime to all primes $\le Q$ (the exact wheel through $Q$), thin them independently to prime density, and measure $\mathrm{corr}(g_n,g_{n+1})$. The question is *where the correlation is built, and whether the wheel-only model lands on the real value.*

| wheel to $Q$ | model $\mathrm{corr}(g_n,g_{n+1})$ | share of the effect |
|---|---|---|
| 7 | $-0.016$ | 39% |
| 19 | $-0.031$ | 74% |
| 43 | $-0.038$ | 87% |
| 317 | $-0.044$ | ~100% |
| $1732\ (\approx\!\sqrt{3\times10^6})$ | $-0.044$ | ~100% |

The model climbs and **plateaus at $-0.044$ by $Q\approx300$** (three random seeds, $\pm0.0005$). The real value, measured over three decades near $10^6$, is $-0.057,\,-0.041,\,-0.047$ (band-to-band scatter $\approx\pm0.006$). So the wheel-only model lands **squarely inside the real range**: to measurement precision, the wheel *fully* accounts for the consecutive-gap anti-correlation, with no detectable residual. **[emp]**

Two things this settles. (i) The $-0.05$ is genuinely the **wheel** — a model with *no* structure but small-prime divisibility reproduces it — so the attribution holds; the earlier draft's "through prime 19 reaches 74%, the tail supplies the rest" is confirmed and completed (the bulk is the small primes; it finishes by $Q\sim$ a few hundred and stops). (ii) It is **not** a deviation-from-HL story: the primes are neither more nor less gap-correlated than the wheel predicts. What was wrong was only the *word* — this is the wheel's derived consecutive-gap signature, not the direct Hardy–Littlewood pair-correlation — not the mechanism.

The lag-1 correlation understates the accessible signal. A *windowed* read is sharper: regressing $\Delta g_n$ on its last five values retains $\approx +2$ percentage points of $R^2$ **beyond** the transform-matched null — roughly six times the raw-gap memory — so the wheel's fingerprint on consecutive gaps is most visible in the windowed wobble, exactly the object this note is built from. The separation of that genuine residual from the $-\tfrac12$ differencing pedestal is carried out in [*Prime-Gap Memory and the Differencing Trap*](Prime_Gap_Memory_Differencing_Trap.md).

## 5. Two imperfections, one wheel

The Prime-Triangle angle is therefore **random-looking jitter pinned under a $45°$ ceiling, corrected by the wheel at the ~5% level, tightening like $\log p/p$**. Its only two prime-specific features are:

1. a **geometric imperfection** — the untouchable $45°$ ceiling (the $52/48$ lean), because the smaller prime is always the shorter leg; and
2. an **arithmetic imperfection** — the ~1% self-correction, i.e. a consecutive-gap anti-correlation reproduced by the **primorial wheel** (the derived form of the wheel's structure, consistent with — not identical to — the Hardy–Littlewood pair-correlation).

The second is the load-bearing one, and it is not new here: it is the *same* wheel that makes $6, 30, 210$ the jumping champions, that decides which Seven-Sisters offsets survive, and that forbids two consecutive-prime sums from a gap of width $\{2,4,6,10\}$. The reason gaps cannot cluster (this anti-correlation) is the reason small gaps cannot repeat (forbidden widths) is the reason primorial gaps dominate (jumping champions). **One mechanism, four shadows** — the angle wobble is the newest of them.

---

## Appendix. Reproduction

```python
import math
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
P=[i for i in range(2,3_000_000) if sieve(3_000_000)[i]]      # (sieve once in practice)
alpha=[math.degrees(math.atan(P[i]/P[i+1])) for i in range(len(P)-1)]
gap  =[P[i+1]-P[i] for i in range(len(P)-1)]
# (1) angle = 45 - (90/pi) gap/p ;  change-in-angle = -(90/pi) d(gap)/p
# corr(gap_n, gap_n+1) ~ -0.05 (real) vs ~0 (shuffled) — the Hardy-Littlewood signal
```

## References

- A. Proxmire, *Prime Geometry II: Angle Record* (this repository) — the Angle-Record Theorem and TPB.
- A. Proxmire, *The FS–TB Δx / Cascade Analysis* (this repository) — the doubled-twin gap statistics and Cramér modeling.
- A. Proxmire, *Consecutive-Prime Sums in Prime Gaps* / *Seven Sisters* / *Synthesis* (Factor Skyline) — the same wheel in three other shadows.
- G. H. Hardy, J. E. Littlewood, *Some problems of 'Partitio numerorum' III* (1923) — the singular series.
- A. M. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experimental Math. 8 (1999).
- Figure: `figures/PG_alpha_gap_arcs.png`.
