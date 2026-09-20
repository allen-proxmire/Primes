# One Wheel, Many Shadows

*The organizing thesis of the Primes collection. A manifesto with pointers — the full arguments live in the linked papers.*

## Thesis

A single object — the **primorial wheel**, equivalently the **Hardy–Littlewood singular series** — generates a family of prime phenomena that look unrelated on the number line but are one picture on the **Factor Skyline**. Two operations run the whole program:

- **Doubling** ($p \mapsto 2p$) — geometrically the **top width-2 ray** of the Factor Skyline. Everything even lives here: $2p$, consecutive-prime sums, twin sums, the doubling ladders.
- **The wheel** ($2, 3, 5, 7, \dots$ — the primorials) — geometrically the **fan of width-rays**. It decides which candidates survive as primes.

Primes are exactly what **escape both**: dodge every width-ray, reach the diagonal.

## The shadows

Each of these is a facet of the same wheel. On the number line they read as different subjects; on the skyline they're one.

| shadow | in one line | the mechanism (the wheel) | where |
|---|---|---|---|
| **Jumping champions** | the commonest prime gap is $6$, then $30$, then $210$ | primorial gaps *fit the wheel stencil* — both ends dodge the small primes at once | *classical* (Odlyzko–Rubinstein–Wolf 1999) |
| **Seven Sisters** | $2p+k$ lands on a prime ~2× more often when $3\mid k$ (or $15\mid k$) | wheel eligibility — those offsets can never be killed by 3 (or 5) | [FS / Seven Sisters](FS_Seven_Sisters_Wheel_Asymptote.md) |
| **Forbidden widths $\{2,4,6,10\}$** | the only gap widths that can *never* hold two consecutive-prime sums | the wheel forbids stacking small gaps (no $2,2$ past $3,5,7$) | [FS / Consecutive-Prime Sums](FS_Consecutive_Prime_Sums_In_Gaps.md) |
| **Angle wobble's 1%** | consecutive prime gaps anti-correlate at $-0.05$ | the singular series, reproduced by building the wheel prime-by-prime | [TB / Angle Wobble](PG_Angle_Wobble.md) |
| **Offset-correlation comb** | sample the primes against a copy shifted by $g$ → the count $C(g)$ | the correlation at lag $g$ *is* the singular series; jumping champions are its tallest teeth | [TB / Offset-Correlation Curve](Offset_Correlation_Curve.md) |
| **The prime crystal** | the primes diffract like a quasicrystal | Bragg peaks at rationals $a/m$ of height $(\mu(m)/\varphi(m))^2$ — the wheel written in frequency space | [TB / Prime Structure Factor](Prime_Structure_Factor.md) |
| **Twin Bertrand (TPB)** | a twin prime in every interval $(x, 2x]$ past 11 | twins are the tightest wheel-survivors; the doubling window $p\to2p$ always catches one | [TB / PG II](../3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md) |
| **Consecutive-sum density** | $\approx W/(2\ln(x/2))$ sums per gap of width $W$ | the "$2$" is doubling — sums live at the $2p$ scale | [FS / Consecutive-Prime Sums](FS_Consecutive_Prime_Sums_In_Gaps.md) |
| **Escape ridge** | $x_{FS}(N)\sim 4e^{-\gamma}N^{3/2}/\ln^2 N$ | the extra $\sqrt N$ is the sieve's $p^2$ activation — the wheel switching on | [FS / Escape Ridge](FS_Escape_Ridge.md) |

**Six faces stand out** — jumping champions, the Seven Sisters, the forbidden widths, the angle $1\%$, the offset comb, and the prime crystal — with the Twin-Bertrand postulate, the density law, and the escape ridge as further facets. And a **control**: a *non*-arithmetic exclusion process (ED's commitment stream) diffracts as a **liquid**, not a crystal — no Bragg peaks — confirming the wheel is specifically *arithmetic* exclusion, not exclusion in general ([TB / ED as the Negative Control](ED_Negative_Control.md)).

The through-line, in one sentence: **the reason gaps can't cluster (the angle $1\%$, the offset comb) is the reason small gaps can't repeat (forbidden widths) is the reason primorial gaps dominate (jumping champions) is the reason the primes diffract like a crystal (the structure factor) is the reason $2p+3k$ keeps hitting primes (Seven Sisters).** One wheel, many shadows.

## What is classical, and what is new (the honest ledger)

This distinction is the whole point — it's what keeps the ambition credible.

**Classical — the engine is not new.** The wheel = Hardy–Littlewood singular series is *the* central object of analytic prime-gap theory. Jumping champions are a known HL consequence. Sophie Germain's $2p+1$ is two centuries old. None of the underlying mechanism is claimed as a discovery.

**The contribution — the lens and the collection.**
1. **Unification.** Showing that these six-plus phenomena are *one object*, with **elementary, visual, reproducible** derivations — and confirming it with a negative control (ED, above) — is not something the literature presents together.
2. **The canvas.** The Factor Skyline gives the two operations a geometric home — doubling is the top ray, the wheel is the fan, primes are the escapes — so the unity is *seen*, not just asserted.
3. **Clean elementary results that may be fresh.** Most notably the **complete forbidden-width classification $\{2,4,6,10\}$** (an unconditional theorem), and the reframings (sum = average on the skyline; the angle as a rescaled gap).

**Not claimed.** No new theorem about the deep structure of the primes. The hard directions — wide-gap existence for consecutive sums, the $6\to30$ jumping-champion crossover rigor, 100% Seven-Sisters coverage — are all Goldbach/Cramér-strength and remain open. Where a result is empirical, it is tagged empirical.

## The takeaway

On the number line these look like different hobbies — a fact about gaps here, a prime-generating formula there, a note on primorials, a triangle of angles. On the Factor Skyline they are **one line resonating against a diagonal, refereed by a fan.** The wheel casts the shadows; doubling holds the light.

---

*Full inventory: [`PRIMES_MAP.md`](../PRIMES_MAP.md). Results list: [`RESULTS.md`](../RESULTS.md). The detailed synthesis lives in [Factor Skyline / Synthesis](FS_Synthesis_Doubling_and_Wheel.md).*

---

## Since this manifesto was written (September 2026)

Two papers now carry the load this page only asserts:

- **[The Wheel Is the Whole Story](The_Wheel_Is_The_Whole_Story.md)** — the thesis above, audited. Ten probes at consecutive prime gaps, each against a stated null, no residual anywhere. Crucially it sorts the **six genuinely independent probes** from the **four that are provably the same quantity in other notation** (the $45°$ angle *is* $g/p$; the balance ratio *is* the gap covariance; the hexagonal form's 3-divisibility *is* the mod-6 repeat). Counting all ten as independent would inflate one result tenfold — so the audit is what makes the claim honest, and the redundancies are themselves the unification thesis doing its job.
- **[The Null-Model Discipline](Null_Model_Discipline.md)** — the method behind every "[emp]" in this collection, as five named failure modes each caught in the act: the transform artifact, the wrong shuffle layer, conditioning that invalidates a shuffle, a generative null that becomes the data, and the missing power check. The most transferable material here; none of it is specific to primes.

**Two further shadows** joined the table above in September: the **windowed gap memory** ($+1.97$ pp, now measured at ~99% wheel rather than presumed) and the **balance ratio** (Koide's quantity on prime triples — which turned out to be the gap covariance wearing a lepton-physics coat, and so is a restatement rather than a new face).