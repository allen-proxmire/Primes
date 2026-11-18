# Primes

[![DOI](https://zenodo.org/badge/1302667725.svg)](https://doi.org/10.5281/zenodo.21626683)

**The Factor Skyline** stands every integer $n$ up as a column: width $\mathrm{lpf}(n)$, its least prime factor, and height $n/\mathrm{lpf}(n)$. On that picture two operations run the primes. **Doubling** ($p\mapsto2p$) is the top ray. **The wheel** — the small primes $2,3,5,7,\dots$ blocking their multiples — is the fan of rays below it. **Primes are what escape both.** Facts that look unrelated on the flat number line — the common gaps, the forbidden widths, the $45°$ angle, the prime crystal — become one picture.

**What goes in.** The engine is classical: the wheel *is* the Hardy–Littlewood singular series, and "gap statistics follow the singular series" is the field's working model. No new theory of the deep structure of the primes is claimed.

**What comes out.** The lens itself; a unification — every gap statistic measured here reduces to the wheel with no residual, confirmed by a negative control; a few clean elementary theorems; one conjecture verified to $10^{10}$; a prediction rule derived with nothing fitted; and a null-model discipline every empirical claim is measured against. The hard problems — twin primes, Goldbach, the parity barrier — remain open.

## Results

| | result | |
|---|---|---|
| [thm] | **Forbidden widths.** A prime gap of width $W\in\{2,4,6,10\}$ never holds two consecutive-prime sums $p_k+p_{k+1}$; the list is complete. | [→](2_One_Wheel_Many_Shadows/FS_Consecutive_Prime_Sums_In_Gaps.md) |
| [thm] | **A traffic law.** Two consecutive gaps are never both $\equiv2$ nor both $\equiv4 \pmod 6$ — measured $0.0\%$ against $28.4\%$ under a shuffle. | [→](2_One_Wheel_Many_Shadows/Switchback_Law.md) |
| [conj] | **Twin Bertrand.** Every $(x,2x]$ with $x\ge11$ holds a twin prime, $\pi_2(2x)-\pi_2(x)\ge1$. Verified to $10^{10}$; equivalent to "every angle record of the prime triangle is a twin" — 440,312 records and 440,312 twins below $10^8$, the same list. | [→](3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md) |
| [emp/null] | **The wheel is the whole story of the gaps.** Ten gap statistics, six independent and four provably the same quantity in other notation; all reproduced by a wheel-only model, no residual. | [→](2_One_Wheel_Many_Shadows/One_Wheel_Many_Shadows.md) |
| [emp] | **The primes are a crystal.** Bragg peaks at every $k=a/m$ of height $(\mu(m)/\varphi(m))^2$; a non-arithmetic exclusion process diffracts as a liquid. | [→](2_One_Wheel_Many_Shadows/Prime_Structure_Factor.md) |
| [emp/deriv] | **The ninety percent rule.** Walking mod-210 open slots, the next prime is caught 90% of the time within $3, 4, 5, 7, 8, 9, 10, 11$ slots at $N=10^3\ldots10^{10}$ — predicted at every decade by $q=4.375/\ln N$, $k=\lceil\ln0.1/\ln(1-q)\rceil$. | [→](2_One_Wheel_Many_Shadows/The_Ninety_Percent_Rule.md) |
| [thm] | **One polytope generates the Exponent Database.** Every entry is a shadow of one $\mathcal P\subset\mathbb R^5$; Ingham meets Guth–Maynard at $\sigma=7/10$, height $30/13$, fixing $\theta=17/30$. | [→](5_X5D_EXPDB/) |

**Every result, with formulas:** [RESULTS.md](RESULTS.md) · **The picture in plain language:** [The Movie](4_Philosophy_Ontology/The_Movie.md)

## Layout

| folder | contents |
|---|---|
| [`1_Factor_Skyline/`](1_Factor_Skyline/) | the lens — the coordinate system and its theory |
| [`2_One_Wheel_Many_Shadows/`](2_One_Wheel_Many_Shadows/) | the wheel and the gaps, prediction, and the null-model method |
| [`3_Twin_Bertrand_Prime_Geometry/`](3_Twin_Bertrand_Prime_Geometry/) | the twin conjecture and the prime triangle |
| [`4_Philosophy_Ontology/`](4_Philosophy_Ontology/) | readings — interpretation, never cited as evidence |
| [`5_X5D_EXPDB/`](5_X5D_EXPDB/) | the Exponent Database polytope — a separate subject |
| [`records/`](records/) | corrections, worklogs, and the repo health check |

Reproduction scripts sit in each folder's `repro/` or `scripts/`.

---

[Corrections](records/CORRECTIONS.md) · Writing under [CC BY 4.0](LICENSE), code under MIT · [Citation](CITATION.cff) · DOI [10.5281/zenodo.21626683](https://doi.org/10.5281/zenodo.21626683) · Standalone releases: Factor Skyline ([DOI](https://doi.org/10.5281/zenodo.18275273)), X5D EXPDB ([DOI](https://doi.org/10.5281/zenodo.19454867))
