# One Wheel, Many Shadows

### The thesis, and its audit: ten probes at consecutive prime gaps, six of them independent, no residual anywhere

Allen Proxmire

> **What this is.** The collection's central claim, stated once and audited. A single object — the **primorial wheel**, equivalently the **Hardy–Littlewood singular series** — generates a family of prime phenomena that look unrelated on the number line and are one picture on the **Factor Skyline**. Every statistic in this collection aimed at consecutive prime gaps is accounted for by that wheel, with no residual detectable against a matched null.
>
> The claim is weaker than it sounds, for a reason stated up front rather than buried: **the ten probes are not ten independent tests.** Four are provably the same quantity in different notation. Sorting the six that count from the four that don't is half the content.
>
> **Nothing here is new deep mathematics.** "Gap statistics follow the singular series" is the field's working model. What is supplied is the lens, the unification with the identities written out, a catalogue with the nulls attached, and a negative control.
>
> For the same picture without notation, see [The Movie](../4_Philosophy_Ontology/The_Movie.md).

Tags: **[fact]** exact · **[emp]** measured · **[null]** against a stated null · **[interp]**.

---

## 1. The thesis

Two operations run the program:

- **Doubling** ($p \mapsto 2p$) — geometrically the **top width-2 ray** of the Factor Skyline. Everything even lives here: $2p$, consecutive-prime sums, twin sums, the doubling ladders.
- **The wheel** ($2, 3, 5, 7, \dots$ — the primorials) — geometrically the **fan of width-rays**. It decides which candidates survive.

Primes are exactly what **escape both**: dodge every width-ray, reach the diagonal. The detailed geometry is in [Synthesis — Doubling and the Wheel](FS_Synthesis_Doubling_and_Wheel.md).

## 2. The shadows

Each is a facet of the same wheel. On the number line they read as different subjects; on the skyline they are one.

| shadow | in one line | the mechanism | where |
|---|---|---|---|
| **Jumping champions** | the commonest gap is $6$, then $30$, then $210$ | primorial gaps fit the wheel stencil — both ends dodge the small primes at once | classical (Odlyzko–Rubinstein–Wolf 1999) |
| **Forbidden widths $\{2,4,6,10\}$** | the only gap widths that can never hold two consecutive-prime sums | the wheel forbids stacking small gaps | [Consecutive-Prime Sums](FS_Consecutive_Prime_Sums_In_Gaps.md) |
| **Seven Sisters** | $2p+k$ lands on a prime ~2× as often when $3\mid k$ (or $15\mid k$) | those offsets can never be killed by 3 (or 5) | [Seven Sisters](FS_Seven_Sisters_Wheel_Asymptote.md) |
| **Offset-correlation comb** | the count $C(g)$ of $n, n+g$ both prime | $C(g)/C(2)=\prod_{p\mid g,\,p>2}\frac{p-1}{p-2}$ — the singular series itself | [Offset-Correlation Curve](Offset_Correlation_Curve.md) |
| **The prime crystal** | the primes diffract like a quasicrystal | Bragg peaks at $k=a/m$ of height $(\mu(m)/\varphi(m))^2$ — the wheel in frequency space | [Prime Structure Factor](Prime_Structure_Factor.md) |
| **Lag-1 anti-correlation** | consecutive gaps anti-correlate at $-0.05$ | reproduced by building the wheel prime by prime | [Angle Wobble](PG_Angle_Wobble.md) |
| **Mod-6 traffic law** | two consecutive gaps never both $\equiv2$ nor both $\equiv4 \pmod 6$ | the mod-3 lane structure | [Switchback Law](Switchback_Law.md) |
| **Twin Bertrand** | a twin prime in every $(x,2x]$ past 11 | twins are the tightest wheel survivors; the doubling window always catches one | [PG II](../3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md) |
| **Consecutive-sum density** | $\approx W/(2\ln(x/2))$ sums per gap of width $W$ | the "2" is doubling — sums live at the $2p$ scale | [Consecutive-Prime Sums](FS_Consecutive_Prime_Sums_In_Gaps.md) |
| **Escape ridge** | $x_{FS}(N)\sim 4e^{-\gamma}N^{3/2}/\ln^2 N$ | the extra $\sqrt N$ is the sieve's $p^2$ activation | [Escape Ridge](FS_Escape_Ridge.md) |

The through-line in one sentence: **the reason gaps can't cluster is the reason small gaps can't repeat is the reason primorial gaps dominate is the reason the primes diffract like a crystal is the reason $2p+3k$ keeps hitting primes.** One wheel, many shadows.

And a **control**: a non-arithmetic exclusion process diffracts as a **liquid** — no Bragg peaks, flat exactly where the primes tower. The crystal takes *divisibility*, not merely exclusion ([ED as the Negative Control](ED_Negative_Control.md)).

---

## 3. The claim, stated precisely

> **Over consecutive prime gaps, every statistic measured in this collection is reproduced by a wheel-only model — integers coprime to the small primes, thinned to prime density, with no other structure — to within the noise of the measurement.**

Three qualifications, all load-bearing:

- **"Consecutive prime gaps."** Not the primes. The *escape* — which wheel-open slot is actually prime — is untouched and remains the parity barrier, irreducible at $\approx 0.26$ bits ([Prime Prediction Budget](Prime_Prediction_Budget.md)).
- **"Measured in this collection."** An empirical regularity over a specific catalogue, not a theorem about all statistics. Section 7 says what would break it.
- **"To within the noise."** Every entry below has a stated null and a stated precision.

---

## 4. The audit: which probes are independent

If the ten probes were counted as ten confirmations, one result would be inflated tenfold. The algebra says exactly which are distinct.

### The six that are genuinely distinct

| probe | why it is a different question | verdict |
|---|---|---|
| **Forbidden widths $\{2,4,6,10\}$** | combinatorial — which configurations are *possible*, not how often | wheel, and **proven** |
| **Jumping champions $6, 30, 210$** | the gap-frequency distribution itself | wheel (classical) |
| **Offset comb $C(g)$** | pair correlation at *fixed offset* — the direct HL prediction | *is* the singular series, to ~1% |
| **Structure factor $S(k)$** | frequency domain — sees the template, not the sign | Bragg peaks at $(\mu(m)/\varphi(m))^2$ |
| **Seven Sisters ($2p+k$)** | a different construction at the doubled scale | wheel eligibility |
| **Lag-1 anti-correlation $-0.05$** | how neighbouring gaps relate | wheel, 100%, plateau at $Q\approx300$ |

Six questions: what is *possible*, what is *common*, what correlates at *fixed offset*, what the *spectrum* looks like, what happens at the *doubled scale*, how *neighbouring gaps* relate. Agreement across those is meaningful.

### The four that are restatements

| probe | what it actually is | the algebra |
|---|---|---|
| **Prime-triangle $45°$ angle** | the relative gap $g/p$ | $\alpha_n = 45° - \frac{90}{\pi}\frac{g_n}{p_{n+1}} + O(\varepsilon^2)$ |
| **Balance ratio $K \to 1/3$** | $\operatorname{cov}(g_n, g_{n+1})$ | $K - \frac13 = \frac{2}{27}\frac{g_1^2+g_1g_2+g_2^2}{m^2}$; shuffling moves only the cross-term, and $E[g_1g_2] - E[g]^2$ **is** the covariance |
| **Hexagonal 3-divisibility** | the mod-6 residue repeat | $3 \mid (h_1^2+h_1h_2+h_2^2) \iff g_1 \equiv g_2 \equiv 0 \pmod 6$, with $h=g/2$ |
| **Windowed memory $+1.97$ pp** | the same gap sequence, longer window | not identical to lag-1, but the same data and mechanism — a *partial* restatement |

**[fact]** The first three are exact identities. The balance ratio does not *behave like* the gap covariance; it **is** the gap covariance.

### What the split means

Neither half is the weak one. The six independent probes are the evidence. The four restatements are a separate result, and arguably the more surprising one:

> Quantities arising from trigonometry, from a lepton-mass formula, and from the Eisenstein integers turn out to be the prime gaps written in different notation.

That is the thesis doing what it says. **The headline is two sentences:** *six independent probes of consecutive prime gaps all land on the wheel with no residual; four further statistics that look independent are provably the same objects, which is why they agree.*

---

## 5. The catalogue

| # | statistic | null used | result | residual |
|---|---|---|---|---|
| 1 | forbidden widths | — (proof) | $\{2,4,6,10\}$ exactly | none — theorem |
| 2 | jumping champions | HL singular series | $6 \to 30 \to 210$ | classical |
| 3 | offset comb $C(g)$ | uniform density | matches $\prod_{p\mid g,p>2}\frac{p-1}{p-2}$ | ~1% |
| 4 | structure factor | non-arithmetic exclusion control | Bragg peaks exactly $(\mu(m)/\varphi(m))^2$ | control diffracts as **liquid** |
| 5 | Seven Sisters | uniform offsets | $3\mid k$ hits ~2× as often | wheel eligibility, exact |
| 6 | lag-1 gap correlation | wheel surrogate, swept $Q$ | $-0.044$ model vs $-0.041$ to $-0.057$ real | none at $Q=317$ (pool ratio 1.39) |
| 7 | windowed gap memory | wheel surrogate, swept $Q$ | $+1.950$ pp model vs $+1.969$ pp real | none from $Q=100$; $Q=30$ gives 76% |
| 8 | LOS mod-6 bias | wheel surrogate | 21.58% model vs 21.48% real | $0.1$ pp |
| 9 | balance ratio, pooled | gap-shuffle | $-0.708\%$ vs $-0.719\%$ implied | inside null spread |
| 10 | balance ratio, by residue | wheel surrogate | 14 classes | none above $1.3\sigma$ |

Entries 6–10 follow [The Null-Model Discipline](Null_Model_Discipline.md): transform after shuffling; match the null to the layer; go generative when conditioning breaks the shuffle; keep the generative model strictly weaker than the data (pool ratios reported); demonstrate power before reporting absence. Entry 4's null is a genuine negative control.

---

## 6. Why this is not surprising, and still worth writing

**Not surprising.** The Hardy–Littlewood $k$-tuple conjecture *is* the statement that constellation densities follow the singular series, and a Cramér model on the wheel is the field's default heuristic.

**Worth writing anyway:**

1. **The nulls are published.** The usual failure in this territory is not a wrong answer but an unstated null.
2. **The redundancies are proven, not assumed.** Section 4 derives them — three exact identities, one partial.
3. **A negative control exists.** Without entry 4, "the wheel explains everything" risks being a story flexible enough to fit any result. The control shows it is not.

---

## 7. What would break the claim

- **A gap statistic with a residual** — any consecutive-gap quantity where a wheel surrogate at pool ratio $\ge 1.4$ falls measurably short. Entry 7 was the most recent live candidate; it closed at ~99%.
- **Scale dependence.** Everything is measured near $10^6$–$5\times10^6$. The lag-1 correlation already weakens with scale ($-0.10$ near $10^{3.5}$, $-0.05$ near $10^6$). A statistic whose wheel-share *drifted* rather than plateaued would need a range attached.
- **A deeper-wheel effect.** All effects saturate by $Q \approx 300$. A statistic still climbing at $Q = 1000$, pool ratio honestly reported, would mean structure in the medium primes.
- **The escape.** If any statistic of *which slot is prime* proved wheel-reproducible, that would contradict the parity barrier.

---

## 8. Honest ledger

**Classical:** the wheel, the singular series, jumping champions, the Cramér-on-the-wheel heuristic, Lemke Oliver–Soundararajan, the parity barrier, Sophie Germain's $2p+1$.

**Contributed:** the lens (doubling as the top ray, the wheel as the fan, primes as the escapes); the unification, with the identities written out; the elementary forbidden-width classification $\{2,4,6,10\}$; the negative control; the audit; the null discipline.

**Not claimed:** any new theorem about the deep structure of the primes, or any advance on the hard directions — twin primes, Goldbach, Cramér, wide-gap existence for consecutive sums, the parity barrier. The wheel is the whole story *of the gap statistics measured here*. It is not the whole story of the primes, and the distance between those two sentences is the entire open problem.

---

## References

- G. H. Hardy, J. E. Littlewood, *Some problems of 'Partitio numerorum' III* (1923).
- A. M. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experimental Math. **8** (1999).
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS (2016).
- H. Cramér (1936); P. Sarnak, *Möbius randomness and dynamics* (2011).
- This collection: [Synthesis](FS_Synthesis_Doubling_and_Wheel.md), [Prime Prediction Budget](Prime_Prediction_Budget.md), [Null-Model Discipline](Null_Model_Discipline.md), [ED as the Negative Control](ED_Negative_Control.md), [Results](../RESULTS.md).
