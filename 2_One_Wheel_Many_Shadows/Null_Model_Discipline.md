# The Null-Model Discipline

### Five rules for measuring structure in a sequence — each with an exact magnitude on the primes

Allen Proxmire

---

Every empirical claim in this collection has the same shape: a statistic, measured against a null. Five rules govern whether the null is the right one. None is new to statistics (surrogate data, constrained null models, power). What the primes add is that each failure has an exact, closed-form size — an identity, a congruence, a computable ratio — rather than one estimated by simulation.

---

## 1. Transform after shuffling, never before

**The failure.** A statistic computed through a transform (a difference, a window) is compared with a null built on the transformed series, and the transform's own algebra reads as signal.

**The exact size.** For i.i.d. $X$ and $Y_n = X_{n+1} - X_n$,
$$\mathrm{cov}(Y_n, Y_{n-1}) = -\mathrm{Var}(X), \qquad \mathrm{Var}(Y) = 2\,\mathrm{Var}(X) \quad\Longrightarrow\quad \mathrm{corr}(Y_n, Y_{n-1}) = -\tfrac12 .$$
$|Y_n|$ and $|Y_{n-1}|$ share the term $X_n$, so their magnitudes correlate positively as well.

**On prime gaps.** Gap changes show volatility clustering $+0.315$, big-jump recoil $\approx 82\%$, and a five-step regression explaining 43.67% of the variance. Against shuffle-then-difference: $+0.319$, $\approx 82\%$, and 41.69%. What survives is $+1.97$ pp ([Gap Correlations §4](Gap_Correlations.md)).

> $\Delta g^{\text{null}} = \mathrm{diff}(\mathrm{shuffle}(g))$, not $\mathrm{shuffle}(\mathrm{diff}(g))$.

---

## 2. Name the layer you shuffled

A shuffle destroys some structure and keeps the rest, so the object permuted decides the hypothesis tested.

| shuffle | what survives | what it tests |
|---|---|---|
| the **gaps** | positive steps, the increasing skeleton, the $45°$ angle ceiling | is it the wheel? |
| the **changes** | neither — the walk wanders through the ceiling | is it the skeleton? |

**On prime gaps.** Sign-runs of the angle change die faster than a coin, but the gap-shuffled null shows the same run lengths (real $64.00/27.25/7.18/1.34\%$, null $64.66/27.31/6.74/1.13\%$ for lengths 1–4). The run structure is a property of any increasing, bounded-gap sequence. To call a feature arithmetic, the null must keep the skeleton and destroy only the order.

---

## 3. A shuffle must be able to produce the data

**The failure.** A shuffle valid on the pooled statistic becomes invalid once the statistic is conditioned on something the shuffle destroys: the null then produces configurations that cannot exist.

**On prime gaps.** Broken out by residue class, shuffled gaps produce impossible triples — a gap of 4 cannot follow $p \equiv 5 \pmod 6$, since $5 + 4 = 9$. The pooled test is fine; the per-class test has no referent. Validity belongs to the null and the statistic together.

> When a shuffle breaks a hard constraint, the null must be **generative**: a model that satisfies the constraint by construction. Here, the wheel surrogate — integers coprime to every prime $\le Q$, thinned to prime density.

---

## 4. A generative null must stay weaker than the data

**The failure.** As the generative model strengthens it converges on the data, and "the model explains it" becomes "the data explain the data."

**The exact size: the pool ratio** (candidates ÷ $\pi(x)$). Over $[10^6, 3\times10^6)$ every integer coprime to all primes $\le 1732$ is prime:

| wheel to $Q$ | pool ÷ $\pi(x)$ | status |
|---|---|---|
| 30 | 2.34 | model |
| 100 | 1.78 | model |
| 317 | 1.43 | model |
| 600 | 1.27 | borderline |
| 1000 | 1.13 | circular |
| 1732 | 1.00 | the primes themselves |

> Report the pool ratio beside every surrogate result and sweep $Q$; below $\approx 1.25$ the comparison is circular. "Coprime to all primes up to $\sqrt x$" is a definition of primality, not a model of it.

Sweeping also separates trend from noise: a single-$Q$ residual of $2.1\sigma$ vanishes under the sweep, and results here are averaged over three seeds.

---

## 5. Show the instrument has power

A null result from a blind test is not evidence of absence.

**On prime gaps.**
- Per-class balance ratio: nothing above $1.3\sigma$ — and the same setup detects the Lemke Oliver–Soundararajan bias at once (mod-6 residues repeat 14% less often than even odds), with the wheel surrogate reproducing it to 0.1 pp.
- Windowed gap memory: a deliberately shallow wheel ($Q = 30$) reproduces only 76%, while $Q \ge 100$ reproduces it all — so the method sees a shortfall when there is one.

> Before reporting absence, detect something known, or cripple the model on purpose.

---

## Checklist

1. Shuffle first, then transform. If the transform has a closed-form artifact, subtract it.
2. State which object was permuted, and so which hypothesis was tested.
3. If the statistic conditions on a hard constraint the shuffle breaks, go generative.
4. Report the generative model's strength (pool ratio) and sweep it.
5. Demonstrate power.
6. Search your own earlier work before writing a result up.

---

## Ledger

| failure | in general | on the primes |
|---|---|---|
| transform artifact | estimated by simulation | $\mathrm{corr} = -\frac12$, an identity |
| broken constraint | argued over | a congruence, enumerable |
| null too strong | judged by feel | the pool ratio, computable |

Prior art: Theiler et al. (1992) for transform-matched surrogates; Connor & Simberloff (1979) and Gotelli (2000) for constrained nulls. The contribution is exposition — a domain where every failure has an exact size.

## References

- J. Theiler, S. Eubank, A. Longtin, B. Galdrikian, J. D. Farmer, *Testing for nonlinearity in time series: the method of surrogate data*, Physica D **58** (1992).
- E. F. Connor, D. Simberloff, *The assembly of species communities: chance or competition?*, Ecology **60** (1979).
- N. J. Gotelli, *Null model analysis of species co-occurrence patterns*, Ecology **81** (2000).
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS (2016).
