# The Wheel Is the Whole Story

### Ten probes at consecutive prime gaps, six of them independent, no residual anywhere — and an audit of which ones actually count

Allen Proxmire · September 2026

> **What this is.** The collection's actual result, stated once and audited. Every statistic anyone here has aimed at consecutive prime gaps is accounted for by the primorial wheel — equivalently the Hardy–Littlewood singular series — with no residual detectable against a matched null. That claim is stronger than any single paper in this collection makes, and it is also weaker than it sounds, for a reason this note leads with rather than buries: **the ten probes are not ten independent tests.** Four of them are provably the same quantity in different clothes. Sorting the six that count from the four that don't is half the content, and it is the half that makes the claim honest.
>
> **Nothing here is new mathematics.** The wheel is Hardy–Littlewood; "gap statistics follow the singular series" is the field's working model. What this note supplies is a *catalogue with the nulls attached* — ten measurements, each against a stated and defended null, with the redundancies identified by algebra rather than assumed away. Tags: **[fact]** exact · **[emp]** measured · **[null]** against a stated null · **[interp]**.

---

## 1. The claim, stated precisely

> **Over consecutive prime gaps, every statistic measured in this collection is reproduced by a wheel-only model — integers coprime to the small primes, thinned to prime density, with no other structure — to within the noise of the measurement.**

Three qualifications, all load-bearing:

- **"Consecutive prime gaps."** Not the primes. The *escape* — which wheel-open slot is actually prime — is untouched and remains the parity barrier, irreducible at $\approx 0.26$ bits ([*Prime Prediction Budget*](Prime_Prediction_Budget.md)). Nothing here bears on it.
- **"Measured in this collection."** An empirical regularity over a specific catalogue, not a theorem about all possible statistics. The next statistic someone invents could break it. Section 5 says what would.
- **"To within the noise."** Every entry below has a stated null and a stated precision. A null result at low precision is not the same as no effect.

---

## 2. The audit: which probes are independent

This is the section that decides whether the paper is worth anything. **If the ten probes were counted as ten confirmations, one result would be inflated tenfold.** They are not independent, and the algebra says exactly which.

### The six that are genuinely distinct

| probe | why it is a different question | verdict |
|---|---|---|
| **Forbidden widths $\{2,4,6,10\}$** | combinatorial, not statistical — asks which configurations are *possible*, not how often they occur | wheel, and **proven**, not measured |
| **Jumping champions $6, 30, 210$** | the gap-frequency distribution itself | wheel (classical, Odlyzko–Rubinstein–Wolf) |
| **Offset-correlation comb $C(g)$** | pair correlation at *fixed offset* — a different object from consecutive-gap statistics, and the direct HL prediction | *is* the singular series, to ~1% |
| **Prime structure factor $S(k)$** | frequency domain — Fourier dual, sees the template and not the sign | wheel as Bragg peaks at $(\mu(m)/\varphi(m))^2$ |
| **Seven Sisters ($2p+k$)** | a different construction at the doubled scale | wheel eligibility |
| **Consecutive-gap anti-correlation $-0.05$** | the lag-1 statistic — the core consecutive-gap question | wheel, 100%, plateau at $Q\approx300$ |

Six probes, six different questions: what is *possible*, what is *common*, what correlates at *fixed offset*, what the *spectrum* looks like, what happens at the *doubled scale*, and how *neighbouring gaps* relate. Agreement across those is meaningful.

### The four that are restatements

| probe | what it actually is | the algebra |
|---|---|---|
| **Prime-triangle $45°$ angle** | the relative gap $g/p$ | $\alpha_n = 45° - \frac{90}{\pi}\frac{g_n}{p_{n+1}} + O(\varepsilon^2)$ — arctangent, nothing else |
| **Balance ratio $K \to 1/3$** | $\operatorname{cov}(g_n, g_{n+1})$ | $K - \frac13 = \frac{2}{27}\frac{g_1^2+g_1g_2+g_2^2}{m^2}$; shuffling moves only the cross-term, and $E[g_1g_2] - E[g]^2$ **is** the covariance |
| **Hexagonal 3-divisibility** | the mod-6 residue repeat | $3 \mid (h_1^2+h_1h_2+h_2^2) \iff g_1 \equiv g_2 \equiv 0 \pmod 6$ |
| **Windowed memory $+1.97$ pp** | the same gap sequence, longer window | not identical to lag-1, but the same data and the same mechanism — a *partial* restatement |

**[fact]** The first three are exact identities. The balance ratio does not *behave like* the gap covariance; it **is** the gap covariance, and no measurement could have shown otherwise.

### What the split means

**Neither half is the embarrassing one.** The six independent probes are the evidence. The four restatements are a *separate result*, and arguably the more surprising one:

> Quantities arising from trigonometry, from a lepton-mass formula, and from the Eisenstein integers turn out to be the prime gaps written in different notation.

That is the unification thesis of this collection — "one wheel, many shadows" — doing exactly what it says. The shadows are not ten independent witnesses; they are one object seen from ten angles, and showing that they are one object is the work.

**The honest headline is therefore two sentences, not one:** *Six independent probes of consecutive prime gaps all land on the wheel with no residual. Four further statistics that look independent are provably the same objects, which is why they agree.*

---

## 3. The catalogue

Each entry: the statistic, the null, the result, the precision.

| # | statistic | null used | result | residual |
|---|---|---|---|---|
| 1 | forbidden widths | — (proof) | $\{2,4,6,10\}$ exactly | none — theorem |
| 2 | jumping champions | HL singular series | $6 \to 30 \to 210$ | classical |
| 3 | offset comb $C(g)$ | uniform density | matches $\prod_{p\mid g,p>2}\frac{p-1}{p-2}$ | ~1% |
| 4 | structure factor | ED causal-exclusion control | Bragg peaks exactly $(\mu(m)/\varphi(m))^2$ | control diffracts as **liquid** |
| 5 | Seven Sisters | uniform offsets | $3\mid k$ hits ~2× as often | wheel eligibility, exact |
| 6 | lag-1 gap correlation | wheel surrogate, swept $Q$ | $-0.044$ model vs $-0.041$ to $-0.057$ real | none at $Q=317$ (pool 1.39) |
| 7 | windowed gap memory | wheel surrogate, swept $Q$ | $+1.950$ pp model vs $+1.969$ pp real | none from $Q=100$; $Q=30$ gives 76% |
| 8 | LOS mod-6 bias | wheel surrogate | 21.58% model vs 21.48% real | $0.1$ pp |
| 9 | balance ratio, pooled | gap-shuffle | $-0.708\%$ vs $-0.719\%$ implied | inside null spread |
| 10 | balance ratio, by residue | wheel surrogate | 14 classes | none above $1.3\sigma$ |

**On the nulls.** Entries 6–10 use the discipline set out in [*The Null-Model Discipline*](Null_Model_Discipline.md): transform after shuffling; match the null to the layer; go generative when conditioning breaks the shuffle; keep the generative model strictly weaker than the data (pool ratios reported); and demonstrate power before reporting absence. Entry 4's null is a genuine negative control — a non-arithmetic exclusion process, which diffracts as a liquid with no Bragg peaks, establishing that the crystal requires *divisibility* and not merely exclusion.

---

## 4. Why this is not surprising, and why it is still worth writing

**Not surprising.** The Hardy–Littlewood $k$-tuple conjecture *is* the statement that prime constellation densities follow the singular series. A Cramér model on the wheel is the field's default heuristic. Finding that ten gap statistics obey it is finding that the standard model works.

**Worth writing anyway, for three reasons.**

1. **The nulls are published.** The usual failure mode in this territory is not a wrong answer but an unstated null. Every entry above names its comparison and its precision, and four of them name a null that was *rejected* on the way ([*Null-Model Discipline*](Null_Model_Discipline.md)).
2. **The redundancies are proven, not assumed.** "These are all the same thing really" is easy to assert. Section 2 derives it — three exact identities, one partial.
3. **A negative control exists.** Entry 4 is the load-bearing one: a process that excludes *causally* rather than *arithmetically* produces a liquid, not a crystal. Without it, "the wheel explains everything" risks being unfalsifiable — a story flexible enough to fit any result. The control shows it is not.

---

## 5. What would break the claim

Stated so the claim is falsifiable rather than decorative.

- **A gap statistic with a residual.** Any consecutive-gap quantity where a wheel surrogate at pool ratio $\ge 1.4$ falls measurably short. Entry 7 was the most recent live candidate and it closed at ~99%.
- **Scale dependence.** Everything here is measured near $10^6$–$5\times10^6$. The lag-1 correlation already weakens with scale ($-0.10$ near $10^{3.5}$, $-0.05$ near $10^6$). If some statistic's wheel-share *drifted* with scale rather than plateauing, the claim would need a range attached.
- **A deeper-wheel effect.** All effects here saturate by $Q \approx 300$. A statistic still climbing at $Q = 1000$ — with the pool ratio honestly reported — would mean structure living in the medium primes, which nothing here has found.
- **The escape.** If any statistic of *which slot is prime*, rather than of the gaps, proved wheel-reproducible, that would contradict the parity barrier and be far more interesting than anything in this note.

---

## 6. Honest ledger

**Classical:** the wheel, the singular series, jumping champions, the Cramér-on-the-wheel heuristic, LOS, the parity barrier. All of it.

**This collection's contribution:** the unification (showing the shadows are one object, with the identities written out), the elementary forbidden-width classification, the negative control, and the null discipline.

**This note's contribution:** the audit. Ten probes sorted into six independent and four redundant, with the redundancies *proved*; the catalogue with nulls and precisions attached; and a falsification list.

**Not claimed:** any new theorem, any statement about the primes beyond their consecutive gaps, or any advance on the hard directions — twin primes, Goldbach, Cramér, the parity barrier. The wheel is the whole story *of the gap statistics measured here*. It is not the whole story of the primes, and the distance between those two sentences is the entire open problem.

---

## References

- G. H. Hardy, J. E. Littlewood, *Some problems of 'Partitio numerorum' III* (1923) — the singular series.
- A. M. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experimental Math. **8** (1999).
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS (2016).
- H. Cramér (1936); P. Sarnak, *Möbius randomness and dynamics* (2011) — the escape.
- A. Proxmire (this collection): [*One Wheel, Many Shadows*](One_Wheel_Many_Shadows.md) (the thesis), [*Prime Prediction Budget*](Prime_Prediction_Budget.md) (the entropy ledger), [*Null-Model Discipline*](Null_Model_Discipline.md) (the method), [*ED Negative Control*](ED_Negative_Control.md) (the control), and the ten probes as catalogued in [`RESULTS.md`](../RESULTS.md).
