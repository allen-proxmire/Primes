# The Null-Model Discipline

### Five ways to fool yourself, each caught in the act — and why the primes are an unusually good place to catch them

Allen Proxmire · September 2026

> **What this is.** A methods note. Every empirical claim in this collection has the same shape — *a statistic, measured against a null* — and the null is where the claims live or die. Five distinct failure modes turned up while building those claims, each one caught on real data, each one having first produced a convincing-looking result that was not there. This note states them, gives the worked example, and ends with a checklist.
>
> **None of the five is new to statistics.** They are the surrogate-data and constrained-null-model literatures, rediscovered from the inside. What the primes add is unusual and worth the note: **here the failure modes have exact, closed-form magnitudes.** Elsewhere you estimate how much a bad null inflates your result; here you can often write it down. That makes prime gaps a clean test bed for a problem most fields can only simulate.
>
> Tags: **[fact]** exact · **[emp]** measured · **[method]**. Worked examples: [*Differencing Trap*](Prime_Gap_Memory_Differencing_Trap.md), [*Angle Wobble §4.1*](PG_Angle_Wobble.md), [*Balance Ratio*](PG_Balance_Ratio_And_Koide.md), [*ED Negative Control*](ED_Negative_Control.md).

---

## 0. The shape of the problem

A structure claim about a sequence is always comparative: *this sequence has property P more than it should.* "Than it should" is the null, and it does all the work. Get it wrong and the statistic measures the null's defects instead of the data's structure.

The five failures below are ordered by how hard they are to notice. The first is visible once you know to look. The last is invisible unless you deliberately test for it.

---

## 1. The transform manufactures the structure

**The failure.** You compute a statistic *through a transform* — a difference, a ratio, a moving window — and compare it to a null built on the *transformed* series. The transform's own algebra then reads as signal.

**The exact form.** For any i.i.d. sequence $X$ with variance $\sigma^2$, the first difference $Y_n = X_{n+1} - X_n$ satisfies

$$\operatorname{cov}(Y_n,Y_{n-1}) = -\operatorname{Var}(X_n) = -\sigma^2, \qquad \operatorname{Var}(Y) = 2\sigma^2 \;\Longrightarrow\; \boxed{\operatorname{corr}(Y_n,Y_{n-1}) = -\tfrac12}$$

**[fact]** A hard $-0.5$ "spike and return," with no memory in $X$ whatsoever. Likewise $|Y_n|$ and $|Y_{n-1}|$ share the term $X_n$, forcing positive correlation of magnitudes — "volatility clustering" out of nothing.

**Caught in the act.** Prime-gap jitter looked alive: volatility clustering $+0.31$, big-jump recoil $82\%$, a windowed wobble $43.7\%$ predictable. Against the correct null — *shuffle the gaps, then difference* — the clustering was $+0.319$ (artifact, entirely), the recoil $79.2\%$ (almost entirely artifact), and of the $43.7\%$, **$41.7$ points were the transform**. What remained was $+1.97$ pp.

> **The rule.** Apply the transform to the shuffled data. Never shuffle the transformed data. $\Delta g^{\text{null}} = \operatorname{diff}(\operatorname{shuffle}(g))$, not $\operatorname{shuffle}(\operatorname{diff}(g))$.

**Why the primes are a good test bed.** The $-\tfrac12$ is not an estimate. It is an identity, so you can subtract the pedestal exactly and know precisely what you have left.

---

## 2. Shuffling the wrong layer

**The failure.** A sequence has structure at several levels. A shuffle destroys some and preserves others, so *which* object you permute silently decides *which* hypothesis you are testing — and the two tests can give opposite answers about the same data.

**Caught in the act.** Prime gaps are positive, so shuffling the **gaps** keeps the reconstructed sequence increasing: the monotonic skeleton survives, and everything it forces survives with it — including the $45°$ angle ceiling and the tight change-cancellation beneath it. Only the fine wheel *ordering* dies. Shuffle the **changes** instead and let them free-float, and the reconstructed walk wanders straight through the $45°$ ceiling and far below.

So the same data, two nulls, two different facts:

| you shuffle | what survives | what you are testing |
|---|---|---|
| the **gaps** | monotone skeleton, bounded steps, the ceiling | *"is it the wheel?"* |
| the **changes** | neither | *"is it the skeleton?"* |

**[fact]** The ceiling is *not* a free property of the change-values; it is held in place by the sequence being genuinely increasing with bounded steps. Match the null to the layer, or a real structural fact reads as "generic noise" — or a generic fact reads as structure.

---

## 3. Conditioning invalidates the shuffle

**The failure.** A shuffle that is perfectly valid pooled becomes **invalid the moment you condition on something the shuffle destroys** — because the null then generates configurations that *cannot exist*, and the excess reads as signal.

**Caught in the act.** Testing whether a gap statistic carries structure beyond the wheel, the natural move is to break it out by residue class and compare each class against gap-shuffled primes. That comparison is meaningless. **A gap of 4 cannot follow $p \equiv 5 \pmod 6$** — $5+4=9$ is divisible by 3. Conditioned on residue, the shuffled triples are not merely improbable, they are **arithmetically impossible**, so the comparison has no referent.

Note the asymmetry that makes this hard to spot: *the pooled version of the same test is fine.* Validity is a property of the null **and the statistic together**, never of the null alone.

> **The rule.** A shuffle null is only valid where the shuffle preserves every hard constraint the statistic conditions on. When it doesn't, the null must stop being a permutation and become **generative** — a model that satisfies the constraint by construction.

**Why the primes are a good test bed.** The constraint is not a modelling assumption to be argued over. It is a congruence, and you can enumerate the possibilities exhaustively. Most fields have to *guess* which constraints their null should respect; here you can prove it.

---

## 4. The generative null is too strong

**The failure.** Having gone generative (failure 3), the model can drift toward the data until it *becomes* the data. Then "the model explains the effect" means only that the data explain the data — and it looks like a triumph, because agreement is perfect.

**Caught in the act.** The wheel surrogate keeps integers coprime to every prime $\le Q$, then thins to prime density. As $Q \to \sqrt{x}$ that stops modelling and starts coinciding: over $[10^6, 3\times10^6)$, **every integer coprime to all primes $\le 1732$ is prime.** The pool ratio — candidates divided by $\pi(x)$ — is exactly $1.00$.

| wheel to $Q$ | pool $/\ \pi(x)$ | status |
|---|---|---|
| 30 | 2.34 | model |
| 100 | 1.78 | model |
| 317 | 1.43 | model |
| 600 | 1.27 | borderline |
| 1000 | 1.13 | **circular** |
| 1732 | 1.00 | **circular — it *is* the primes** |

**[emp]** Two published tables in this collection carried a $Q \approx \sqrt{x}$ row. Both conclusions survive, because both effects plateau near $Q \approx 300$ where the pool is still $1.4\times$ — but the deep rows were carrying no evidence and did not say so.

> **The rule.** A generative null must stay strictly weaker than the thing it models. "Coprime to all primes up to $\sqrt{x}$" is not weaker — **it is a definition of primality.** Report the pool ratio beside every surrogate result, and sweep the model's strength rather than trusting a single setting.

Sweeping has a second payoff: it separates a trend from noise. A single $Q$ once showed a $2.1\sigma$ residual here that vanished entirely under the sweep.

---

## 5. No power check

**The failure.** The null reproduces the data, you report "no residual," and you never establish that your test could have found one. A null result from a blind instrument is not evidence of absence.

**Caught in the act, twice, both times deliberately.**

- Testing the balance ratio by residue class and finding nothing above $1.3\sigma$: does the setup see *anything*? Yes — the Lemke Oliver–Soundararajan bias is enormous and immediate (consecutive primes repeat their mod-6 residue $14\%$ less often than even odds), and the wheel surrogate reproduces it to within $0.1$ percentage point. Instrument has power; there is simply nothing extra.
- Testing whether the wheel explains the windowed gap memory: a deliberately **too-shallow** wheel ($Q=30$) reproduces only $76\%$ of the excess, while $Q \ge 100$ reproduces it all. The shortfall at $Q=30$ is the power check — the method can detect a gap when one exists.

> **The rule.** Before believing a null result, show the test detecting something you already know is there — a published bias in the same data, or a deliberately crippled model.

---

## 6. The checklist

1. **Transform after shuffling, never before.** Know the transform's own algebra; if it has a closed form, subtract it exactly.
2. **Name the layer.** State which object you permuted and therefore which hypothesis you tested.
3. **Check the shuffle can produce the data.** If the statistic conditions on a hard constraint the shuffle breaks, go generative.
4. **Check the generative model is weaker than the data.** Report the strength ratio; sweep it; never quote a single setting.
5. **Demonstrate power.** Find a known effect, or cripple the model on purpose, before reporting absence.

A sixth, which is not about nulls but caused as much trouble as any of them: **check whether the result already exists in your own prior work** before writing it up.

---

## 7. Honest ledger

**Not new.** Failure 1 is the surrogate-data problem (Theiler et al., 1992) — the surrogate must be matched to the statistic's transform. Failures 2 and 3 are the constrained-null-model debate that ecology conducted publicly and at length (Connor & Simberloff 1979; Gotelli 2000): which features a null holds fixed determines what it tests, and a null that generates impossible communities inflates every result computed against it. Failure 4 is overfitting the null, familiar wherever surrogate models are tuned. Failure 5 is statistical power, which is a century old.

**A working mathematician or statistician will find nothing here they did not know.** This note is a re-derivation from the inside, by someone who hit all five while trying to make honest claims about prime gaps.

**What may be worth something.** In this domain the failure modes are **exactly computable**, and that is rare:

| failure | elsewhere | here |
|---|---|---|
| transform artifact | estimated by simulation | $\operatorname{corr} = -\tfrac12$, an identity |
| broken constraint | argued over | a congruence, enumerable exhaustively |
| null too strong | judged by feel | pool ratio, computable to three decimals |

So prime gaps make a clean pedagogical test bed for null-model failure: one can state exactly how large each artifact is, rather than arguing about it. **That is the note's only claim to originality, and it is a claim about exposition, not about mathematics.**

**What the discipline bought, concretely.** Applied to this collection it removed a $44\%$-predictable "prime weather" that was $42$ points artifact; it demoted a statistic that appeared to carry new structure and provably does not; it caught two circular rows in already-written papers; and it converted one "plausibly the wheel" into a measured $99\%$. Every one of those was, first, a result that looked real.

---

## References

- J. Theiler, S. Eubank, A. Longtin, B. Galdrikian, J. D. Farmer, *Testing for nonlinearity in time series: the method of surrogate data*, Physica D **58** (1992) — the transform-matched surrogate.
- E. F. Connor, D. Simberloff, *The assembly of species communities: chance or competition?*, Ecology **60** (1979) — constrained null models.
- N. J. Gotelli, *Null model analysis of species co-occurrence patterns*, Ecology **81** (2000) — which constraints a null should hold fixed.
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS (2016) — the known effect used as the power check.
- A. Proxmire, *Prime-Gap Memory and the Differencing Trap*, *The Prime-Triangle Angle*, *The balance ratio*, *ED as the Negative Control* (this collection) — the worked examples.
