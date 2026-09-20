# Primes

Prime-number research. Several strands that turn out to be **one story**: the primes seen through *doubling* ($p \mapsto 2p$) and *the wheel* (the primorials $2,3,5,7,\dots$), on a coordinate system that gives the number line back a dimension it was hiding. [![DOI](https://zenodo.org/badge/1302667725.svg)](https://doi.org/10.5281/zenodo.21626683)

## Start here — no notation required

| | |
|---|---|
| [**The Movie**](4_Philosophy_Ontology/The_Movie.md) | what's actually going on — the whole picture in plain language |
| [**What We Found**](WHAT_WE_FOUND.md) | the results, with honest labels: proven / verified / measured / retracted |
| [**How We Know**](HOW_WE_KNOW.md) | why any of it should be believed — and the two times it shouldn't have been |

Each of the five series folders also has a short README saying what's in it and where to start.

## Headlines

- **[conjecture] A Bertrand postulate for twins.** Every dyadic interval $(x,2x]$ past $x=11$ contains a twin prime: $\pi_2(2x)-\pi_2(x)\ge1$. Verified to $10^{10}$ (27.4M twins). Equivalent to a purely geometric statement — every record-setting prime-triangle angle is a twin — **independently re-verified 2026-09 over every consecutive prime pair below $10^8$: 440,312 records, 440,312 twins, the two lists identical.** → [PG II](3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md)
- **[theorem] Forbidden gap-widths $\{2,4,6,10\}$.** These are exactly the prime-gap widths that can *never* contain two consecutive-prime sums. → [Consecutive-Prime Sums](2_One_Wheel_Many_Shadows/FS_Consecutive_Prime_Sums_In_Gaps.md)
- **[theorem] A traffic law on consecutive gaps.** Two consecutive prime gaps can never both be $\equiv2$, nor both $\equiv4\pmod6$ — a prohibition, not a bias. Measured: those transitions are exactly $0.0\%$ against $28.4\%$ under a matched null; $|\Delta g|\in\{6,12\}$ occur at **half** their expected rate while every other value is elevated; and no gap outside the multiples of 6 ever repeats immediately. → [Switchback Law](2_One_Wheel_Many_Shadows/Switchback_Law.md)
- **[theorem] One polytope generates the Exponent Database.** Every EXPDB output is a projection or envelope of a single $\mathcal{P}\subset\mathbb{R}^5$. The binding constraint is a cusp at $\sigma=7/10$, where Ingham (1940) meets Guth–Maynard (2024) at exactly $30/13$ — fixing the prime-gap exponent $\theta=17/30$. → [X5D](5_X5D_EXPDB/X5D_Polyhedral-Reinterpretation.pdf), [figure](5_X5D_EXPDB/figures/fig2_guth_maynard_cusp.svg)
- **[derivation] Two operations run the primes:** *doubling* ($p\mapsto2p$) and *the wheel* (primorials). On the Factor Skyline, doubling is the top ray and the wheel is the fan; primes are what escape both. → [Synthesis](2_One_Wheel_Many_Shadows/FS_Synthesis_Doubling_and_Wheel.md)
- **[empirical/null] Every statistic aimed at consecutive prime gaps reduces to the wheel, with no measured residual.** Ten probes, each against a matched null — **and six are genuinely independent while four are provably the same quantity in different notation.** Both halves are the result. → [The Wheel Is the Whole Story](2_One_Wheel_Many_Shadows/The_Wheel_Is_The_Whole_Story.md)

## The idea in one paragraph

**The lens is the contribution; the number line is hiding the picture.** The number line is a 1-D shadow that scrambles multiplicative structure — squash it flat and prime facts scatter into unrelated-looking messes. The **Factor Skyline** gives back the dimension that makes it legible: stand each integer up as a column, width set by its smallest prime factor. In that view, *doubling* is the top layer and *the wheel* (the small primes, foreclosing their multiples) is the fan of lower layers, and **primes are what escape both**. Everything else — the common gaps, the forbidden widths, the Seven Sisters, the twin postulate, the 45° angle, the prime "crystal" — is *consequence*. The lens is the thing.

## How this collection is organized

The papers are grouped into five numbered reading series:

1. **[The Factor Skyline](1_Factor_Skyline/)** — the coordinate system and its four-part theory (the foundation).
2. **[One Wheel, Many Shadows](2_One_Wheel_Many_Shadows/)** — the wheel and its shadows: jumping champions, forbidden widths, the Seven Sisters, the 45° angle, the offset comb, the prime crystal (the main arc) — plus the angle's scale-invariant *switchback law*, the *prime prediction budget* (how far structure gets you, and the wall), and two synthesis papers: **[The Wheel Is the Whole Story](2_One_Wheel_Many_Shadows/The_Wheel_Is_The_Whole_Story.md)** (ten probes, six of them independent, no residual anywhere — with the audit of which ones actually count) and **[The Null-Model Discipline](2_One_Wheel_Many_Shadows/Null_Model_Discipline.md)** (five ways to fool yourself with a null, each caught in the act).
3. **[Twin Bertrand / Prime Geometry](3_Twin_Bertrand_Prime_Geometry/)** — the Twin-Prime Bertrand Postulate and the prime-triangle work.
4. **[Philosophy & Ontology](4_Philosophy_Ontology/)** — [**The Movie**](4_Philosophy_Ontology/The_Movie.md) (the plain-language picture of the whole thing), finitism, the sieve as a hunt, the quantum-mechanical reading.
5. **[X5D / EXPDB](5_X5D_EXPDB/)** — the exponent-database strand (a separate analytic-number-theory subject).

- **Every result, tagged** ([thm]/[conj]/[emp]/[deriv]/[mirage]): [`RESULTS.md`](RESULTS.md) — the technical version of [What We Found](WHAT_WE_FOUND.md)
- **Full inventory** (what's compiled, what's a draft, what's on Zenodo): [`PRIMES_MAP.md`](PRIMES_MAP.md)

## One move, twice

The two halves of this collection were built years and a subject apart, and they run the same move.

**The Factor Skyline** says a pile of unrelated-looking prime facts — the common gaps, the forbidden widths, the 45° angle, the crystal — are **one wheel seen from several angles**. **[X5D](5_X5D_EXPDB/)** says a pile of unrelated-looking exponent bounds, accumulated across a century of analytic number theory, are **one polytope seen from several angles**. Neither paper mentions the other, and the subjects have nothing in common.

Even the machinery rhymes. X5D has an explicit *dimension ladder* — ℝ⁵ → ℝ³ → ℝ¹ → ℝ⁰ — where each step is a projection that discards information irreversibly, and the scattered results of the literature are what you get at the bottom. The Factor Skyline makes the same claim about the number line: it is the lossy 1-D shadow of a 2-D picture, and prime facts look unrelated *because* they have been flattened. Both say the mess is real and is what projection does to something simpler.

**The shared instinct is: find the single object the mess is shadows of.** It is worth naming, because it is a method rather than a result — and because a method that always finds a single object is one that needs a way of telling a real shape from an expected one. That is what the nulls and the [reproduction scripts](2_One_Wheel_Many_Shadows/repro/) are for; [How We Know](HOW_WE_KNOW.md) is the account of the times they earned their keep.

## Honest ledger

The **engine** is classical — the wheel *is* the Hardy–Littlewood singular series, and even the information-theoretic view of primes-as-structure-plus-randomness is an active field. 
What's contributed here is the **lens** (the Factor Skyline), the **unification** (unrelated-looking facts shown to be one wheel, confirmed by a negative control), a couple of **clean elementary results** — most notably the forbidden-width classification $\{2,4,6,10\}$ — and the **null-model discipline** that the empirical claims are measured against. 
No new theory of the deep structure of primes is claimed; the hard directions remain open and are tagged as such.

## Elsewhere

The individual projects are also published as standalone, citable repositories — **Factor Skyline** ([DOI](https://doi.org/10.5281/zenodo.18275273)) and **X5D EXPDB** ([DOI](https://doi.org/10.5281/zenodo.19454867)) carry Zenodo DOIs. Plain-language NotebookLM audio/video one-pagers are kept in a separate working folder.
