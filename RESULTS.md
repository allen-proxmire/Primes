# Results

Every result in the collection, once each, with its formula and a link to the paper that carries it.

**Tags:** **[thm]** proven · **[conj]** conjecture, verified far, open · **[emp]** measured · **[null]** measured against a stated null model · **[deriv]** derived from known theory, heuristic where marked · **[fact]** exact identity · **[interp]** a reading, not a claim about arithmetic.

---

## 1. The wheel and the gaps

The organizing result. Thesis and full audit: [One Wheel, Many Shadows](2_One_Wheel_Many_Shadows/One_Wheel_Many_Shadows.md).

**The wheel accounts for every gap statistic measured — six independent probes, no residual.** [emp/null]
Every statistic aimed at consecutive prime gaps is reproduced by a wheel-only model (integers coprime to the primes up to $Q$, thinned to prime density). Six probes ask genuinely different questions; four further statistics are provably the same quantity in other notation.

| probe | kind | result |
|---|---|---|
| forbidden widths $\{2,4,6,10\}$ | independent | proven |
| jumping champions $6, 30, 210$ | independent | classical |
| offset comb $C(g)$ | independent | singular series to ~1% |
| structure factor $S(k)$ | independent | Bragg peaks at $(\mu(m)/\varphi(m))^2$ |
| Seven Sisters $2p+k$ | independent | wheel eligibility |
| lag-1 gap correlation $-0.05$ | independent | 100% wheel, plateau at $Q\approx300$ |
| windowed gap memory $+1.97$ pp | partial restatement | 99% wheel from $Q=100$ |
| Lemke Oliver–Soundararajan mod-6 bias | partial restatement | reproduced to 0.1 pp |
| prime-triangle $45°$ angle | restatement | $\alpha$ *is* $g/p$ |
| balance ratio $K\to\tfrac13$ | restatement | *is* $\mathrm{cov}(g_n,g_{n+1})$ |

**A traffic law on consecutive gaps.** [thm]
Every prime past 3 sits in one of two lanes mod 3, and a step cannot change lanes the same way twice running:
$$g_n \equiv g_{n+1} \equiv 2 \pmod 6 \quad\text{and}\quad g_n \equiv g_{n+1} \equiv 4 \pmod 6 \quad\text{never occur.}$$
Measured: those transitions are $0.0\%$ against $28.4\%$ under a gap-shuffle. $|\Delta g| = 6$ runs at half its null rate ($5.14\%$ vs $10.29\%$), $|\Delta g| = 12$ likewise ($2.98\%$ vs $6.57\%$), every non-multiple of 6 is elevated, and no gap outside the multiples of 6 ever repeats immediately. → [The Traffic Law](2_One_Wheel_Many_Shadows/Traffic_Law.md)

**Four gap widths can never hold two consecutive-prime sums.** [thm]
With $S_k = p_k + p_{k+1}$, a prime gap of width $W \in \{2,4,6,10\}$ contains at most one $S_k$, and that list is complete. Width 10 is the non-obvious member (a mod-6 argument). Verified to $2\times10^8$. → [Consecutive-Prime Sums §3](2_One_Wheel_Many_Shadows/Consecutive_Prime_Sums.md)

**Consecutive-prime-sum density.** [emp]
A gap of width $W$ near $x$ holds on average
$$\frac{W}{2\ln(x/2)}$$
sums $S_k$ — about 55% of gaps hold none and 37% exactly one. No width guarantees a sum: a width-140 gap with expected count 4 is empty. → [Consecutive-Prime Sums §2, §4](2_One_Wheel_Many_Shadows/Consecutive_Prime_Sums.md)

**Sum = average, the mirror law, and doubling ladders.** [thm]
On the Factor Skyline $S_k$ stands at height $\tfrac12(p_k+p_{k+1})$, its average. The bracket signature takes the form $(-x,+y,-y,+x)$ exactly when the sum is centred between its neighbouring primes, which happens iff $2S_k$ is again a consecutive-prime sum; centred sums chain under doubling ($30\to60\to120\to240$). → [Consecutive-Prime Sums §5](2_One_Wheel_Many_Shadows/Consecutive_Prime_Sums.md)

**The offset comb is the singular series.** [emp]
Counting $n$ with both $n$ and $n+g$ prime gives
$$\frac{C(g)}{C(2)} = \prod_{p\mid g,\ p>2}\frac{p-1}{p-2}$$
to ~1% — baseline at powers of 2, $\times2$ at multiples of 6, $\times\tfrac83$ at 30. Jumping champions are its tallest teeth. → [The Prime Crystal §1](2_One_Wheel_Many_Shadows/Prime_Crystal.md)

**The primes diffract like a crystal; a look-alike does not.** [emp/null]
The structure factor $S(k)$ has sharp Bragg peaks at every rational $k = a/m$ of height
$$\left(\frac{\mu(m)}{\varphi(m)}\right)^2 .$$
A non-arithmetic exclusion process run through the same analysis diffracts as a liquid — flat exactly where the primes tower — so the crystal takes divisibility, not mere exclusion. → [The Prime Crystal §2–§3](2_One_Wheel_Many_Shadows/Prime_Crystal.md)

**Seven Sisters and the wheel.** [thm/emp]
For the offsets $k\in\{+1,+3,-3,-5,+7,+9,-9\}$, $2p+k$ is prime about twice as often when $3\mid k$, because then $3\nmid 2p+k$ (and when $15\mid k$, neither 3 nor 5 divides it). No finite offset set covers every prime; climbing along multiples of 15, then 105, a dozen additions reach 99%. Verified to $6\times10^7$. → [Seven Sisters](2_One_Wheel_Many_Shadows/Seven_Sisters.md)

**The prime-triangle angle is a rescaled gap.** [fact/emp]
$$\alpha_n = \arctan\frac{p_n}{p_{n+1}} \approx 45° - \frac{90}{\pi}\frac{g_n}{p_{n+1}}$$
Angles rise to a $45°$ ceiling in gap-family arcs, twins on top. The wobble is ~99% what differencing does to any sequence; the rest is the lag-1 anti-correlation below. → [Gap Correlations §1–§2](2_One_Wheel_Many_Shadows/Gap_Correlations.md)

**Gap memory is the wheel.** [emp/null]
$\mathrm{corr}(g_n, g_{n+1}) \approx -0.05$, reproduced by a small-primes-only surrogate ($-0.044$ at $Q=317$, pool ratio 1.39). Of the 43.7% apparent predictability of gap changes, 41.7 points are the differencing artifact; the $+1.97$ pp that survives is reproduced at 99% from $Q=100$ ($Q=30$ reaches only 76%). → [Gap Correlations §3–§4](2_One_Wheel_Many_Shadows/Gap_Correlations.md)

**The balance ratio: an exact gap identity.** [fact]
For $a<b<c$ with gaps $g_1, g_2$ and mean $m$, and $K = (a^2+b^2+c^2)/(a+b+c)^2$:
$$K - \tfrac13 = \tfrac{2}{27}\,\frac{g_1^2+g_1g_2+g_2^2}{m^2}.$$
With half-gaps $h=g/2$, $3 \mid h_1^2+h_1h_2+h_2^2 \iff g_1\equiv g_2 \pmod 6$, so the Eisenstein norm of the half-gap pair is divisible by 3 exactly when three consecutive primes share a residue mod 6 (measured 17.408%, wheel-reproduced). The deviation of $K$ from a shuffle null is $\mathrm{cov}(g_n,g_{n+1})$ by definition. → [Gap Correlations §5](2_One_Wheel_Many_Shadows/Gap_Correlations.md)

**No prime–lepton connection.** [fact]
Koide's $K = 2/3$ is exactly the $45°$ condition, $\cos^2\theta = 1/(3K)$, and the midpoint of $K$'s range $[\tfrac13, 1]$. The primes run to the opposite corner ($K\to\tfrac13$). → [Gap Correlations §5.4](2_One_Wheel_Many_Shadows/Gap_Correlations.md)

---

## 2. Predicting the next prime

**The ninety percent rule.** [emp/deriv]
Carry the mod-210 wheel (primes 2, 3, 5, 7) and test only open slots, in order. The number of tests needed to catch the next prime 90% of the time, measured over $[N, 2N]$:

| $N$ | $10^3$ | $10^4$ | $10^5$ | $10^6$ | $10^7$ | $10^8$ | $10^9$ | $10^{10}$ |
|---|---|---|---|---|---|---|---|---|
| slots | 3 | 4 | 5 | 7 | 8 | 9 | 10 | 11 |

Predicted with nothing fitted: the chance an open slot is prime is
$$q = \frac{210}{48\ln N} = \frac{4.375}{\ln N}, \qquad k = \left\lceil \frac{\ln 0.1}{\ln(1-q)} \right\rceil,$$
which gives the measured integer at all eight decades ($q$ runs 1–4 points high — the right integer, not the exact probability). The walk is geometric to within a few tenths of a point. **Corollary:** the road length $\approx 2.303\ln N$ does not depend on how many wheels are carried. → [Predicting the Next Prime §2–§5](2_One_Wheel_Many_Shadows/Predicting_the_Next_Prime.md)

**Walking in order is optimal, and the wall.** [deriv/emp]
The chance the next prime is the $k$-th open slot strictly decreases in $k$, so walking in order is Bayes-optimal; reweighting by gap frequencies or recent history changes nothing (mean rank $+0.0007$). At $N = 10^4$ the step carries $2.48$ bits: wheel template $1.70$, escape $0.26$. Which open slot is prime is the parity barrier. → [Predicting the Next Prime §4, §6](2_One_Wheel_Many_Shadows/Predicting_the_Next_Prime.md)

**Looking back adds nothing beyond the wheel.** [emp/null]
The direction of the last step carries nothing (zig-zag guess 68.6% real vs 69.2% shuffled). Its size carries a sliver (0.148 slots at $[10^7, 2\times10^7]$); grouping walks by where the wheels up to 300 strike the next 12 open slots leaves $-0.001 \pm 0.006$. → [Predicting the Next Prime §7](2_One_Wheel_Many_Shadows/Predicting_the_Next_Prime.md)

**The wheel is cheap to carry.** [emp]
Program $\approx 1.4427\,p_k$ bits (linear) against a territory of $p_k^2$ (quadratic): the cost per decided integer, $1.4427/p_k$ bits, falls to zero. → [Predicting the Next Prime §6](2_One_Wheel_Many_Shadows/Predicting_the_Next_Prime.md)

---

## 3. Twins in every doubling window

**Twin-Prime Bertrand Postulate.** [conj]
Every interval $(x, 2x]$ with $x \ge 11$ contains a twin prime:
$$\pi_2(2x) - \pi_2(x) \ge 1, \qquad\text{equivalently}\quad T_{k+1} < 2T_k \ \text{for every twin } T_k \ge 11.$$
Verified to $10^{10}$ (27,412,679 twins, no exceptions). Weaker than the twin prime conjecture, stronger than bounded gaps; immediate under Hardy–Littlewood, open unconditionally. Equivalently $R^{\mathrm{twin}}_1 = 11$ for the twin analogue of the Ramanujan primes. → [Twin Bertrand §1](3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**Angle records and twins.** [thm/emp]
Every twin pair is an angle record of the prime triangle, unconditionally. Under TPB, every angle record is a twin, so the two sequences coincide:
$$\text{some angle record is not a twin} \implies \text{TPB fails}.$$
(The converse is not proved; it would need a close pair just past $2T_k$.) Checked in exact arithmetic below $10^8$: 440,312 records, 440,312 twins, the same list. → [Twin Bertrand §2](3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**A second route to the same conjecture.** [thm/emp]
On the Factor Skyline the slope between consecutive prime spires satisfies
$$\frac{\Delta p}{\Delta x_{FS}} \le \frac{2g}{5g-4} \le \frac23, \qquad \theta \le \arctan\tfrac23 \approx 33.69°,$$
with equality iff the pair is a twin (all 8,168 twin segments below $10^6$, nothing else). Asking that the ceiling be reached in every $[p,2p]$ is TPB again. → [Twin Bertrand §3](3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**Generalized Bertrand Principle.** [conj]
TPB extends to cousins $(p, p+4)$ and sexy primes $(p, p+6)$, verified to $10^{10}$ with thresholds 7 and 5. Mean twin gaps follow $\overline G \sim 0.792(\log T)^{1.978}$, matching the Hardy–Littlewood $(\log T)^2/C_2$; extreme gaps grow faster, alike across constellations. → [Twin Bertrand §4](3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**Prime square differences.** [thm]
$C_2^2 - C_1^2 = p_{n+2}^2 - p_n^2$. $\mathrm{PSD}_n = (p_{n+2}^2 - p_n^2)/12$ is an integer for $p_n \ge 5$, and for $p_n \ge 7$ its last digit is 0, 4 or 6 — 0 at $48.97\%$, 4 and 6 exactly equal at $25.51\%$. → [Twin Bertrand §2.4](3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

**The doubled-twin shadow.** [emp]
Doubled twins on a prime-rank axis lie on a line of slope $C_2\log(2T)/(\log T)^2$ (confirmed to 1–2% over five decades); the scatter is the twin gaps, and straight runs occur at the chance rate (1.95% vs 1.99%). → [Twin Bertrand §5](3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md)

---

## 4. The lens: the Factor Skyline

**The architecture.** [deriv]
Each integer $n$ is a column of width $\mathrm{lpf}(n)$ and height $n/\mathrm{lpf}(n)$. Primes escape to the diagonal; composites fall onto the fan of width-rays (the wheel); doubling is the top ray. The classical results of multiplicative number theory appear as features of the picture — restated in skyline terms, not re-proved. → [The Factor Skyline §1–§2, §7](1_Factor_Skyline/Factor_Skyline.md)

**The singular series as survival ratios.** [thm]
$$C_H = \prod_q \frac{q^{k-1}\,(q - v_q(H))}{(q-1)^k}$$
is the Hardy–Littlewood singular series; for pairs $C_{\{0,h\}} = 2C_2\prod_{p\mid h,p>2}\frac{p-1}{p-2} \ge 2C_2 > 1$. (For $k \ge 3$, $C_H > 1$ is checked numerically, not proved.) → [The Factor Skyline §3](1_Factor_Skyline/Factor_Skyline.md)

**Template persistence.** [thm]
$N_H(p_{k+1}) = N_H(p_k)\,(p_{k+1} - v_{p_{k+1}}(H))$: constellation-open positions per primorial period grow without bound for every admissible $H$ (twins $1, 1, 3, 15, 135, 1485, \dots$). → [The Factor Skyline §3](1_Factor_Skyline/Factor_Skyline.md)

**Epochs outrun the template.** [deriv]
From $p \ge 5$ the epoch $[p_k^2, p_{k+1}^2)$ is shorter than one primorial period, so the wheel is never seen to repeat where it applies. → [The Factor Skyline §4](1_Factor_Skyline/Factor_Skyline.md)

**Simple to generate, random to look at.** [fact/emp]
The escape layer is produced by a program of size $K = O(\log N)$ yet carries $H \approx 0.26N$ bits of measured entropy (at $N=10^4$). → [The Factor Skyline §5](1_Factor_Skyline/Factor_Skyline.md)

**The escape ridge.** [deriv, heuristic constant]
$$x_{FS}(N) \asymp \frac{N^{3/2}}{\ln^2 N}, \qquad y \sim X^{2/3}(\ln y)^{4/3}$$
— the extra $\sqrt N$ is the sieve's $p^2$ activation. → [The Factor Skyline §6](1_Factor_Skyline/Factor_Skyline.md)

---

## 5. Method: the null-model discipline

Five rules, each with an exact size on the primes. → [The Null-Model Discipline](2_One_Wheel_Many_Shadows/Null_Model_Discipline.md)

1. **Differencing manufactures structure.** [fact] First differences of any i.i.d. sequence have lag-1 autocorrelation exactly $-\tfrac12$. Shuffle the gaps, then difference.
2. **The shuffled layer decides the question.** [fact] A gap-shuffle tests "is it the wheel"; a change-shuffle tests "is it the skeleton".
3. **A shuffle must be able to produce the data.** [fact] Shuffled gaps sorted by residue class produce impossible triples; go generative.
4. **A generative null must stay weaker than the data.** [fact] Report the pool ratio (candidates ÷ $\pi(x)$); below $\approx 1.25$ the comparison is circular.
5. **Show the instrument has power.** [fact] Detect something known before reporting absence.

---

## 6. A separate subject: the Exponent Database

**The Exponent Database as geometry.** [deriv]
Every downstream bound of the Tao–Trudgian–Yang database comes from one computed region $\mathcal P\subset\mathbb R^5$ of exponent tuples $(\sigma,\tau,\rho,\rho^*,s)$ — their region $\mathcal E$, as the database currently bounds it — by three operations:
$$\mathcal P \xrightarrow{\ \pi\ } R\subset\mathbb R^3 \xrightarrow{\ \sup_\tau \rho/\tau\ } f(\sigma) \xrightarrow{\ \mathrm{env}^-\ } A(\sigma) \xrightarrow{\ \sup_\sigma\ } \theta .$$
The large value and energy regions are projections; $A$ and $A^*$ are lower envelopes of rational suprema of them, plus closed-form exponent-pair routes; the exponent-pair hull, $\beta^*$ and $\mu$ hull generate constraints on $\mathcal P$ rather than descending from it. The iteration descends monotonically and, with the code's truncations, stabilizes at the tightest bounds derivable from the given axioms. → [X5D §2–§5](5_X5D_EXPDB/X5D.md)

**The Ingham–Guth–Maynard cusp.** [fact]
$$\frac{3}{2-\sigma} = \frac{15}{5\sigma+3} = \frac{30}{13} \text{ at } \sigma = \tfrac{7}{10}, \qquad \theta_{\mathrm{PNT}} \le 1 - \frac{13}{30} = \frac{17}{30}, \qquad \frac{d\theta_{\mathrm{PNT}}}{d\lVert A\rVert_\infty} = \frac{169}{900}.$$
Guth and Maynard's bound for primes in all short intervals, located as the peak of the zero-density envelope. → [X5D §6.1](5_X5D_EXPDB/X5D.md), [figure](5_X5D_EXPDB/figures/fig2_guth_maynard_cusp.svg)

**The second-moment route is not monotone.** [fact/emp]
In the route $\theta_{\mathrm{gap},2} \le \max\bigl(2 - 2/\lVert A\rVert_\infty,\ \sup\max(\alpha,\beta)\bigr)$, with
$$\alpha = 4\sigma - 2 + \frac{2\bigl(B(1-\sigma)-1\bigr)}{B - A}, \qquad \beta = 4\sigma - 2 + \frac{B(1-\sigma)-1}{A},$$
a weaker zero-density input can do better: near $\sigma = 1$, $\alpha$ falls and $\beta$ rises as $A$ grows, and they balance at $A_1 = B_1/3$, giving $2 - 3/B_1 = \frac54$. The code feeds in the pointwise-best $A$ and gets $\frac32$ there; Heath-Brown's $\frac{23}{18}$ comes from choosing $A$. Not a new bound — the known bound is $\frac{123}{100}$ (Stadlmann). → [X5D §6.2](5_X5D_EXPDB/X5D.md), [`check_x5d_arithmetic.py`](5_X5D_EXPDB/repro/check_x5d_arithmetic.py), [`gap2_free_choice.py`](5_X5D_EXPDB/repro/gap2_free_choice.py)

---

## 7. Readings

Interpretation, never cited as evidence. → [Philosophy & Ontology](4_Philosophy_Ontology/)

- **[The Primes in Plain Language](4_Philosophy_Ontology/Primes_in_Plain_Language.md)** [interp] — every prime is a clock joining at its own square; from $p = 7$ the pattern is longer than the road it governs, so it is never seen to repeat. It explains the appearance of randomness completely and the actual unpredictability not at all.
- **[Readings](4_Philosophy_Ontology/Readings.md)** [interp] — the sieve as a hunt; the primes as interruptions of a doubling clock; numbers counted into existence.

---

## Open

- **Twin Bertrand** — verified to $10^{10}$, unproven; and whether "every angle record is a twin" implies it.
- **$C_H > 1$ for admissible tuples of size $k \ge 3$** — checked, not proved.
- **The parity barrier** — which open slot is prime.
- **Twin primes, Goldbach, Cramér, the Riemann Hypothesis** — untouched.
- **Whether the forbidden-width theorem is new** — it is elementary enough that it may be known.
- **Independent re-runs still owed:** the $10^{10}$ TPB computation; the series-3 analysis scripts other than `check_angle_records.py`, `check_psd.py` and `check_envelope_fits.py`; the X5D region and envelopes, which need the database code.
