# Results

Every result in the collection, once each, with its formula and a link to the paper that carries it.

**Tags:** **[thm]** proven · **[conj]** conjecture, verified far, open · **[emp]** measured · **[null]** measured against a stated null model · **[deriv]** derived from known theory · **[fact]** exact identity · **[interp]** a reading, not a claim about arithmetic.

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
Every prime past 3 sits in one of two lanes mod 6, and a step cannot change lanes the same way twice running:
$$g_n \equiv g_{n+1} \equiv 2 \pmod 6 \quad\text{and}\quad g_n \equiv g_{n+1} \equiv 4 \pmod 6 \quad\text{never occur.}$$
Measured: those transitions are exactly $0.0\%$ against $28.4\%$ under a gap-shuffle. $|\Delta g| = 6$ runs at half its null rate ($5.14\%$ vs $10.29\%$), $|\Delta g| = 12$ likewise ($2.98\%$ vs $6.57\%$), every non-multiple of 6 is elevated, and no gap outside the multiples of 6 ever repeats immediately. → [Switchback Law](2_One_Wheel_Many_Shadows/Switchback_Law.md)

**Four gap widths can never hold two consecutive-prime sums.** [thm]
Call $s_k = p_k + p_{k+1}$ a consecutive-prime sum. A prime gap of width $W \in \{2,4,6,10\}$ contains at most one $s_k$, and that list is complete. Width 10 is the non-obvious member (a mod-6 argument). Verified to $2\times10^8$. → [Consecutive-Prime Sums](2_One_Wheel_Many_Shadows/FS_Consecutive_Prime_Sums_In_Gaps.md)

**Consecutive-prime-sum density.** [emp]
A gap of width $W$ near $x$ holds on average
$$\frac{W}{2\ln(x/2)}$$
sums $s_k$ — so about 55% of gaps hold none and 37% exactly one. → [Consecutive-Prime Sums](2_One_Wheel_Many_Shadows/FS_Consecutive_Prime_Sums_In_Gaps.md)

**Sum = average, the mirror law, and doubling ladders.** [thm]
On the Factor Skyline a consecutive-prime sum sits at height equal to its average $\tfrac12(p_k+p_{k+1})$; the $-x,+y,-y,+x$ mirror fires exactly when the sum is centred; centred sums chain under doubling ($30\to60\to120\to240$). → [2p Bracket Construction](2_One_Wheel_Many_Shadows/FS_2p_Bracket_Construction.md)

**The offset comb is the singular series.** [emp]
Counting $n$ with both $n$ and $n+g$ prime gives
$$\frac{C(g)}{C(2)} = \prod_{p\mid g,\ p>2}\frac{p-1}{p-2}$$
to ~1% — baseline at powers of 2, $\times2$ at multiples of 6, $\times\tfrac83$ at 30. Jumping champions are its tallest teeth. → [Offset-Correlation Curve](2_One_Wheel_Many_Shadows/Offset_Correlation_Curve.md)

**The primes diffract like a crystal; a look-alike does not.** [emp/null]
The structure factor $S(k)$ has sharp Bragg peaks at every rational $k = a/m$ of height
$$\left(\frac{\mu(m)}{\varphi(m)}\right)^2 .$$
The primes are a quasicrystal whose lattice is the wheel. A non-arithmetic exclusion process run through the same analysis diffracts as a **liquid** — flat exactly where the primes tower — so the crystal takes divisibility, not mere exclusion. → [Prime Structure Factor](2_One_Wheel_Many_Shadows/Prime_Structure_Factor.md), [ED as the Negative Control](2_One_Wheel_Many_Shadows/ED_Negative_Control.md)

**Seven Sisters and the wheel.** [thm/emp]
For the offsets $k\in\{+1,+3,-3,-5,+7,+9,-9\}$, $2p+k$ is prime about twice as often when $3\mid k$, because then $3\nmid 2p+k$ (and when $15\mid k$, neither 3 nor 5 can divide it). 100% coverage by any finite offset set is impossible, since gaps are unbounded; the efficient way to climb is along multiples of 15, then 105 — a dozen additions reach 99%. Verified to $6\times10^7$. → [Seven Sisters](2_One_Wheel_Many_Shadows/FS_Seven_Sisters_Wheel_Asymptote.md)

**The prime-triangle angle is a rescaled gap.** [fact/emp]
$$\alpha_n = \arctan\frac{p_n}{p_{n+1}} \approx 45° - \frac{90}{\pi}\frac{g_n}{p_{n+1}}$$
Angles rise to a $45°$ ceiling in gap-family arcs, twins on top. The wobble is ~99% universal; the remaining ~1% is the lag-1 anti-correlation $-0.05$, which a small-primes-only surrogate reproduces ($-0.044$ at $Q=317$, pool ratio 1.39). → [Angle Wobble](2_One_Wheel_Many_Shadows/PG_Angle_Wobble.md)

**Prime-gap "weather" is a differencing effect; the residue is the wheel.** [emp/null]
The volatility clustering ($+0.31$), big-jump recoil and 44% windowed predictability of gap *changes* vanish under the matched null (shuffle the gaps, then difference). What survives is $+1.97$ pp of windowed memory, which a wheel-only surrogate reproduces at 99% from $Q=100$ ($Q=30$ reaches only 76%, so the test can see a shortfall). → [Differencing Trap](2_One_Wheel_Many_Shadows/Prime_Gap_Memory_Differencing_Trap.md)

**The balance ratio: an exact gap identity.** [fact]
For $a<b<c$ with gaps $g_1, g_2$ and mean $m$, and $K = (a^2+b^2+c^2)/(a+b+c)^2$:
$$K - \tfrac13 = \tfrac{2}{27}\,\frac{g_1^2+g_1g_2+g_2^2}{m^2}.$$
With half-gaps $h=g/2$, $3 \mid (h_1^2+h_1h_2+h_2^2) \iff g_1\equiv g_2 \pmod 6$, and for consecutive primes the traffic law forces both $\equiv 0$: the Eisenstein norm of the half-gap pair is divisible by 3 exactly when three consecutive primes share a residue mod 6 — measured $17.408\%$, reproduced by wheel surrogates from $Q=30$. Its deviation from a shuffle null is $\mathrm{cov}(g_n,g_{n+1})$ by definition ($-0.708\%$ measured vs $-0.719\%$ implied). → [Balance Ratio](2_One_Wheel_Many_Shadows/PG_Balance_Ratio_And_Koide.md)

**No prime–lepton connection.** [fact]
Koide's $K = 2/3$ is exactly the $45°$ condition and the midpoint of $K$'s range $[\tfrac13, 1]$. The primes run to the opposite corner ($K\to\tfrac13$); the leptons sit at $45°$. The shared $45°$ is shared coordinates, not shared physics. → [Balance Ratio §3, §7](2_One_Wheel_Many_Shadows/PG_Balance_Ratio_And_Koide.md)

**The escape ridge.** [deriv]
$$x_{FS}(N)\sim \frac{4e^{-\gamma}N^{3/2}}{\ln^2 N}$$
— the extra $\sqrt N$ is the sieve's $p^2$ activation. → [Escape Ridge](2_One_Wheel_Many_Shadows/FS_Escape_Ridge.md)

---

## 2. Predicting the next prime

**The ninety percent rule.** [emp/deriv]
Carry the mod-210 wheel (primes 2, 3, 5, 7) and test only open slots, in order. The number of tests needed to catch the next prime 90% of the time, measured over $[N, 2N]$:

| $N$ | $10^3$ | $10^4$ | $10^5$ | $10^6$ | $10^7$ | $10^8$ | $10^9$ | $10^{10}$ |
|---|---|---|---|---|---|---|---|---|
| slots | 3 | 4 | 5 | 7 | 8 | 9 | 10 | 11 |

Predicted with nothing fitted: the chance an open slot is prime is
$$q = \frac{210}{48\ln N} = \frac{4.375}{\ln N}, \qquad k = \left\lceil \frac{\ln 0.1}{\ln(1-q)} \right\rceil,$$
which gives the measured integer at all eight decades. ($q$ runs 1–4 points high throughout — the $x/\ln x$ slack — so the claim is the right integer, not the exact probability.) The per-slot distribution is geometric to within a few tenths of a point. **Corollary:** the road length $\approx 2.303\ln N$ does not depend on how many wheels are carried; the wheel decides how much of the road is tested, never where the prime is. → [The Ninety Percent Rule](2_One_Wheel_Many_Shadows/The_Ninety_Percent_Rule.md), [`ninety_percent_table.py`](2_One_Wheel_Many_Shadows/repro/ninety_percent_table.py)

**The prediction budget, and the wall.** [deriv/emp]
At $N = 10^4$ the next-prime step carries $H = 2.48$ bits: the wheel template supplies $1.70$ (stable across three decades), the irreducible escape is $0.26$ bits, and every other regularity in the collection adds nothing, because walking the open slots in order is already Bayes-optimal. The wheel removes 73.3% of positions for free; an open slot carries $\approx 0.84$ bits. Which open slot is prime is the parity barrier, and nothing here touches it. → [Prime Prediction Budget](2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md), [`entropy_budget.py`](1_Factor_Skyline/repro/entropy_budget.py)

**Looking back adds nothing beyond the wheel.** [emp/null]
The direction of the last step carries nothing (zig-zag guess 68.6% real vs 69.2% shuffled). Its size carries a sliver (0.148 slots at $[10^7, 2\times10^7]$), and grouping walks by where the wheels up to 300 strike the next 12 open slots leaves $-0.001 \pm 0.006$ — all of it wheel. → [The Ninety Percent Rule](2_One_Wheel_Many_Shadows/The_Ninety_Percent_Rule.md), [`lookback_test.py`](2_One_Wheel_Many_Shadows/repro/lookback_test.py)

**The wheel is cheap to carry.** [emp]
Program $\approx 1.4427\,p_k$ bits (linear) against a territory of $p_k^2$ (quadratic), so cost per decided integer falls to zero. From $p \ge 5$ the period exceeds the epoch in which the rule is frozen, so the template is never seen to repeat inside its own domain. → [Budget §5](2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md), [Primorial Epochs §2.2](1_Factor_Skyline/FS_primorial_epochs.md)

---

## 3. Twins in every doubling window

**Twin-Prime Bertrand Postulate.** [conj]
Every interval $(x, 2x]$ with $x \ge 11$ contains a twin prime:
$$\pi_2(2x) - \pi_2(x) \ge 1, \qquad\text{equivalently}\quad T_{k+1} < 2T_k \ \text{for every twin } T_k \ge 11.$$
Verified to $10^{10}$ (27,412,679 twins, no exceptions). Weaker than the twin prime conjecture, stronger than bounded gaps; immediate under Hardy–Littlewood, open unconditionally. → [PG II](3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md), [verification reports](3_Twin_Bertrand_Prime_Geometry/results/)

**The angle-record theorem: the record sequence is the twin sequence.** [thm/emp]
Every closest-to-$45°$ angle record of the prime triangle is a twin pair — and this is logically equivalent to TPB. The converse is proved unconditionally (Proposition 6A: every twin beats every earlier pair), so
$$\text{TPB fails} \iff \text{some angle record is not a twin}.$$
Checked in exact integer arithmetic over every consecutive pair below $10^8$: 440,312 records, 440,312 twins, the two lists identical. → [PG II](3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md), [`check_angle_records.py`](3_Twin_Bertrand_Prime_Geometry/scripts/check_angle_records.py)

**A second, independent route to the same conjecture.** [thm/emp]
On the Factor Skyline, consecutive primes form a segment whose slope is bounded by
$$\arctan\tfrac23 \approx 33.69°,$$
attained exactly when the pair is a twin (verified on every segment below $10^6$). Asking that the ceiling be touched in every doubling window is TPB again. Two unrelated geometries — an angle rising to $45°$, a slope capped at $\arctan\frac23$ — reach the same inequality, which says the conjecture is natural, not that it is true. → [Twin-Slope Ceiling](3_Twin_Bertrand_Prime_Geometry/FS_twin_prime_geometry.md)

**Generalized Bertrand Principle.** [conj]
TPB extends to cousins $(p, p+4)$ and sexy primes $(p, p+6)$, all verified to $10^{10}$. Extreme constellation gaps grow faster than the typical $(\log T)^2$, alike across constellations; mean twin gaps follow $G \sim 0.792(\log T)^{1.978}$, matching the Hardy–Littlewood $(\log T)^2/C_2$. → [PG III](3_Twin_Bertrand_Prime_Geometry/PG_III_GBP.md), [envelope fits](3_Twin_Bertrand_Prime_Geometry/results/uniform_envelope_fits.md)

**Prime square differences.** [thm]
$C_2^2 - C_1^2 = p_{n+2}^2 - p_n^2$ (no primality needed — the $p_{n+1}$ terms cancel). $\mathrm{PSD}_n = (p_{n+2}^2 - p_n^2)/12$ is an integer for $p_n \ge 5$, and for $p_n \ge 7$ its last digit is 0, 4 or 6 — with 0 at $48.97\%$ and 4 and 6 exactly equal at $25.51\%$ each. → [PG I](3_Twin_Bertrand_Prime_Geometry/PG_I_PrimeTriangle.md), [`check_psd.py`](3_Twin_Bertrand_Prime_Geometry/scripts/check_psd.py)

**The template over-supplies twin candidates.** [deriv]
Twin-open positions per primorial period run $1, 1, 3, 15, 135, 1485, \dots$ — more than enough candidates in every doubling window. → [FS–TB Bridge](3_Twin_Bertrand_Prime_Geometry/FS_TB_Bridge.md)

**The Δx cascade.** [emp]
Doubled twins $2p_k$ on a prime-rank axis: the step $\Delta x_k$ counts primes in $(2p_k, 2p_{k+1}]$, is a Poisson mixture, and is macro-linear ($R^2\approx0.996$) with chance-level micro-collinearity. → [FS–TB Δx Analysis](3_Twin_Bertrand_Prime_Geometry/FS_TB_DeltaX_Analysis.md)

---

## 4. The lens: the Factor Skyline

**The architecture.** [deriv]
Each integer $n$ is a column of width $\mathrm{lpf}(n)$ (its least prime factor) and height $n/\mathrm{lpf}(n)$. Primes escape to the diagonal; composites fall onto the fan of width-rays (the wheel); doubling is the top ray. PNT, Chebyshev's conservation law, Mertens, the Dickman function, Erdős–Kac and divisor averages all appear as geometric features. → [FSPapers I–IV](1_Factor_Skyline/)

**Coverage protection.** [thm]
The Hardy–Littlewood $k$-tuple constants satisfy $C_H > 1$ for every admissible $H$, with an explicit product formula. → [FSPapers I](1_Factor_Skyline/FSPapers_01_architectural_foundation.md)

**Template persistence.** [thm]
Constellation-open positions per primorial period grow without bound for every admissible $k$-tuple. → [FSPapers I](1_Factor_Skyline/FSPapers_01_architectural_foundation.md)

**Why the primes look random.** [thm]
The escape layer is algorithmically simple and statistically random at once:
$$K = O(\log N) \quad\text{against}\quad H \sim 0.26\,N \text{ bits}.$$
→ [FSPapers 02.1 §13](1_Factor_Skyline/FSPapers_02.1_correlations_and_randomness.md)

**Activation epochs outrun the template.** [deriv]
From $p \ge 5$ the epoch $[p_k^2, p_{k+1}^2)$ is shorter than one primorial period, so the full template is never seen inside a single epoch. This is also why gap 6 dominates so long (5#-template: epoch 24 against period 30). → [Primorial Epochs §2.2](1_Factor_Skyline/FS_primorial_epochs.md)

---

## 5. Method: the null-model discipline

Five rules, each learned on a measurement in this collection. → [The Null-Model Discipline](2_One_Wheel_Many_Shadows/Null_Model_Discipline.md)

1. **Differencing manufactures structure.** [fact] First differences of any i.i.d. sequence have lag-1 autocorrelation exactly $-\tfrac12$. Shuffle the gaps, then difference; never shuffle the differences.
2. **The shuffled layer decides the question.** [fact] A gap-shuffle tests "is it the wheel"; a change-shuffle tests "is it the monotone skeleton".
3. **A shuffle is valid only if it keeps every hard constraint the statistic conditions on.** [fact] Shuffled gaps sorted by residue class produce arithmetically impossible triples; go generative instead.
4. **A generative null must stay strictly weaker than the data.** [fact] Report the pool ratio (candidates ÷ $\pi(x)$) beside every surrogate; below $\approx 1.25$ the comparison is circular.
5. **Show the instrument has power before believing a null result.** [fact] Confirm it still detects something known — the LOS bias, or a deliberately shallow wheel.

---

## 6. A separate subject: the Exponent Database

**One polytope generates the Exponent Database.** [thm]
Every output of the Tao–Trudgian–Yang Exponent Database is a projection or envelope of a single $\mathcal{P}\subset\mathbb{R}^5$, with an invariant, a monotone contraction flow and a fixed-point theorem. → [X5D](5_X5D_EXPDB/X5D_Polyhedral-Reinterpretation.pdf)

**The Guth–Maynard cusp fixes $\theta = 17/30$.** [fact]
Ingham (1940) and Guth–Maynard (2024) meet at $\sigma = 7/10$:
$$\frac{3}{2-\sigma} = \frac{15}{5\sigma+3} = \frac{30}{13}, \qquad \theta = 1 - \frac{13}{30} = \frac{17}{30}, \qquad \frac{d\theta}{d\lVert A\rVert} = \left(\frac{13}{30}\right)^2 = \frac{169}{900}.$$
All four values checked as exact rationals; the attack surface is about 0.006 wide. → [Reinterpretation](5_X5D_EXPDB/X5D_EXPDB_Reinterpretation.md), [figure](5_X5D_EXPDB/figures/fig2_guth_maynard_cusp.svg)

---

## 7. Readings

Interpretation, kept apart from the results and never cited as evidence. → [Philosophy & Ontology](4_Philosophy_Ontology/)

- **[The Movie](4_Philosophy_Ontology/The_Movie.md)** [interp] — every prime is a clock; each clock joins at its own square and multiplies the pattern's length; from $p = 7$ the pattern is longer than the stretch of road it governs, so it can never be caught repeating. That explains the *appearance* of randomness completely and the actual unpredictability not at all.
- **The sieve as a hunt; counting into existence** [interp] — finitist readings, and the open question of why infinite mathematics pays rent in a finite world.
- **The quantum-mechanical reading** [interp] — with its own open question on bilinearity.

---

## Open

- **Twin Bertrand** — verified to $10^{10}$, unproven.
- **The parity barrier** — which open slot is prime. The collection stops here on purpose.
- **Twin primes, Goldbach, Cramér, the Riemann Hypothesis** — untouched; several results here would follow from them, which is the wrong direction.
- **Whether the forbidden-width theorem is new** — it is elementary enough that it may be known.
- **Independent re-runs still owed:** the $10^{10}$ TPB computation; the series-3 analysis scripts other than `check_angle_records.py`, `check_psd.py` and `check_envelope_fits.py`; X5D beyond the cusp arithmetic.
