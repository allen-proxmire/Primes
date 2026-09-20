# Archive Survey

### What was in the discontinued repos, what came out, and what stays buried

*2026-09-20. The `Archive/` folder holds three repos Allen discontinued, kept because he knew something in them was worth saving without knowing what. This is that question answered. Everything named here as promoted is now in folders 1–5 and is canon; everything named as left is reference only.*

---

## The headline

**One complete, publishable paper was sitting in the Archive, uncited by anything in canon.**

> **[The Twin-Slope Ceiling: Twin Prime Geometry on the Factor Skyline](../3_Twin_Bertrand_Prime_Geometry/FS_twin_prime_geometry.md)** — 5,700 words, nine sections, abstract, MSC codes, three theorems and a named conjecture.

It proves the twin slope $\arctan(2/3) \approx 33.69°$ is an absolute ceiling on the Factor Skyline; that twin-open template positions in every Bertrand interval $[p, 2p]$ diverge like $C_2 p/(\ln p)^2$; and that under Cramér the probability all of them stay unfilled decays super-exponentially. It then isolates **the Filling Condition** as the single conjectural step between those structural guarantees and the twin prime conjecture, gives it in three equivalent forms, and places it in the hierarchy strictly between Maynard–Tao bounded gaps and full Hardy–Littlewood.

**It is not a duplicate of the PG trilogy.** PG II is about the *triangle* angle $\arctan(p/q) \to 45°$. This is about the *skyline* slope $\arctan(2/3)$ as a ceiling. Different construction, different geometry, same subject. [`PRIMES_MAP.md`](../PRIMES_MAP.md) §7 flagged this exact question in July — *"confirm they're distinct papers, not divergent copies"* — and it was never resolved. **They are distinct.**

---

## What came out

### Series 1 — Factor Skyline

| promoted | what it is |
|---|---|
| [`modules/`](../1_Factor_Skyline/modules/) — 17 files | The derivation layer the five FS papers cite by name: PNT, sieve geometry, prime gaps, Cramér, Goldbach, Möbius, twin primes, constellations, residue classes, short intervals, Chebyshev, divisors, smooth numbers, explicit formula, RH analogue, zero geometry, ontology. Promoted as a block, so the collection no longer cites anything it does not contain. |
| [`FS_glossary.md`](../1_Factor_Skyline/FS_glossary.md) | Definitions of the core terms. The collection had none. |
| [`FS_architectural_map.md`](../1_Factor_Skyline/FS_architectural_map.md) | Navigational map of the architecture. |

### Series 3 — Twin Bertrand

| promoted | what it is |
|---|---|
| [`FS_twin_prime_geometry.md`](../3_Twin_Bertrand_Prime_Geometry/FS_twin_prime_geometry.md) | The Twin-Slope Ceiling — see above. |
| [`PG_FieldGuide.md`](../3_Twin_Bertrand_Prime_Geometry/PG_FieldGuide.md) | **A plain-language narrative tour of PG I–III**, April 2026, 4,000 words. Series 3's equivalent of what [The Movie](../4_Philosophy_Ontology/The_Movie.md) does for the wheel work — and it already existed. *(It also already knew about the Definition 5 wrinkle rediscovered today: "the only exception across the first hundred million primes is the very first pair, (2,3).")* |
| [`literature_review.md`](../3_Twin_Bertrand_Prime_Geometry/literature_review.md) | **The prior-art check for TPB and GBP.** Positions them against Ramanujan primes (Sondow), Zhang–Maynard bounded gaps, and Heath-Brown short intervals, and concludes the dyadic form does not appear in the literature as a named conjecture. This is the support for every "possibly new" in the collection, and it was not in canon. |
| [`results/`](../3_Twin_Bertrand_Prime_Geometry/results/) — 6 reports | **The verification evidence.** Including `comparison_1e9_vs_1e10.md`: 455,052,511 primes, 27,412,679 twin pairs, **zero TPB exceptions through 10¹⁰**, 285 seconds. Also the twin-Ramanujan computation, the uniform envelope fits across twins/cousins/sexy, the structural 10¹⁰ extension, and the QM-probe verdict. |

**This last one matters for how the collection describes itself.** Series 3's README said the 10¹⁰ verification "remains unverified here." That was true of *re-running* it, but the evidence report existed and had simply never been promoted. Corrected.

---

## What stays buried, and why

| left in Archive | reason |
|---|---|
| `Factor Skyline/archive/FS_01…09_*.md` (9 files) | Early program drafts — research program, paper draft, correlations, randomness, entropy, ergodicity, universality, meta-structure, meta-mathematics. **Superseded** by FSPapers 01–04, which are the polished versions of the same material. |
| `Factor Skyline/papers/Archive/monograph/` | The monograph and manuscript. Superseded by the same five papers. |
| `X5D EXPDB Framework/framework/` + `methodology/` (12 files) | "Architectural Distillation" — a **generic methodology** for dynamical systems, not number theory. Arguably a separate project rather than part of this collection. Left deliberately; promote it only if it becomes its own thing. |
| `X5D EXPDB Framework/examples/GuthMaynard/*.md` | Contains the historical error recorded as N13 (pre-GM cusp stated at σ ≈ 5/7 with height 12/5, which cannot both hold). X5D is retired; the main chain is already verified and figured in [`5_X5D_EXPDB/figures/`](../5_X5D_EXPDB/figures/). |
| `X5D EXPDB Framework/docs/`, `examples/EXPDB/invariant.md` | Documentation for a retired codebase. |
| `compute/vendor/expdb/` | Tao's `expdb`, vendored. Not ours. |
| `Twin Bertrand/papers/PG_II_AngleRecord_TBConjecture.md` | An older markdown of PG II. **Ours is now longer and current** — converted from the author's LaTeX and carrying the new Proposition 6A/6B. Superseded. |
| `Twin Bertrand/papers/FS_TB_Integration_Plan.md` | A planning document, not a result. |
| All `.py`, `.csv`, `.json`, data | The scripts that mattered were promoted in September; the rest is infrastructure for retired pipelines. The Twin Bertrand data alone is ~900 MB of sieve output, regenerable. |

---

## What this changes about the collection

**Series 3 is much better supported than it looked this morning.** It now has a plain-language field guide, a literature review establishing novelty, and six verification reports including the 10¹⁰ run. The "unverified" label was about re-running, not about evidence existing.

**Series 1 is now self-contained.** It no longer cites 17 documents it does not contain. [`DERIVATION_MODULES.md`](../1_Factor_Skyline/DERIVATION_MODULES.md) becomes an index of what is present rather than a pointer into a dead repo.

**The Archive can probably be retired.** After this pass, what remains is superseded drafts, a separate methodology project, a retired codebase, vendored third-party code, and regenerable data. Nothing in it is load-bearing for anything in folders 1–5.

**And the original inventory was nearly right.** Allen's recollection — *consecutive-prime sums, X5D, Twin Bertrand, Factor Skyline, the wheel work* — accounts for everything substantive. The one omission was the Twin-Slope Ceiling, which is FS-and-twin-primes and fell between two of those categories.

---

## Standing question

**The Filling Condition deserves attention.** The Twin-Slope Ceiling paper isolates one conjectural statement as the sole obstacle between the Factor Skyline's structural guarantees and the twin prime conjecture, claims it is strictly weaker than breaking the parity barrier, and locates it between Maynard–Tao and Hardy–Littlewood.

**Resolved the same day. It is the Twin-Prime Bertrand Postulate.** Form 3 of its equivalence theorem is verbatim PG II's Conjecture 2, and the Twin-Slope paper never mentions PG II or TPB — both dated April 2026. So it is not a new obstacle; it is the collection's own conjecture reached independently from the Factor Skyline side.

That makes "the only obstacle separating the FS guarantees from the twin prime conjecture" **vacuous** — TPB implies the twin prime conjecture on its own, with the FS structure doing no work. And the *strictly weaker than the parity barrier* argument does not hold: parity blocks the existential statement too, Friedlander–Iwaniec proved a count rather than an existence result, and Zhang–Maynard stops at 246 rather than 2 **because of** parity — the barrier biting, cited as precedent for escaping it.

**Theorem 4.2 is true** (verified to 10⁶, zero exceptions), though its proof is broken in the general case and is repaired in place. **The honest version of the paper is a better one:** a geometric route from the Factor Skyline to TPB, independent of the prime-triangle route in PG II. Two unrelated derivations of one conjecture is a real result. **The paper has since been rewritten around that surviving claim** — abstract, §1, §6 and §9 reframed, §4's proof repaired, the parity theorem withdrawn — and [PG II](../3_Twin_Bertrand_Prime_Geometry/PG_II_AngleRecord.md) now carries the cross-reference back. Full record at the head of [the paper](../3_Twin_Bertrand_Prime_Geometry/FS_twin_prime_geometry.md).
