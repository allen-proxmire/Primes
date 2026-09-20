# PRIMES — Master Map

*Lives at `GitHub/Primes/PRIMES_MAP.md`.*

> **Read §0 first.** Everything from §1 onward is the **July 2026 consolidation record** — how the four project repos were merged and what was decided. It describes a folder layout (`Primes/Factor Skyline/`, `Primes/Twin Bertrand/`, …) that **no longer exists**: the collection was reorganised into five numbered reading series, and the original repos now sit untracked in `Archive/`. The history is kept because the decisions in it still bind; the current inventory is §0.

---

## 0. Current inventory (2026-09-20)

**Structure.** Five numbered reading series, tracked; three upstream project repos in `Archive/`, deliberately untracked (see [`.gitignore`](.gitignore)).

```
GitHub/Primes/
├── README.md · RESULTS.md · PRIMES_MAP.md
├── 1_Factor_Skyline/              the coordinate system and its theory
├── 2_One_Wheel_Many_Shadows/      the main arc (most active)
│   ├── repro/                     regenerates every measured table
│   └── superseded/                pre-September versions of 4 papers
├── 3_Twin_Bertrand_Prime_Geometry/
├── 4_Philosophy_Ontology/
├── 5_X5D_EXPDB/
└── Archive/                       upstream repos — UNTRACKED, and grep misses them
```

### 1_Factor_Skyline

| paper | formats |
|---|---|
| FSPapers_01_architectural_foundation — *The Architectural Foundation* | md, pdf |
| FSPapers_02_correlation_theory — *The Correlation Theory* | md, pdf |
| FSPapers_02.1_correlations_and_randomness — *Correlations and Randomness* | md, pdf |
| FSPapers_03_information_dynamics_universality | md, pdf |
| FSPapers_04_meta_structure — *The Meta-Structure* | md, pdf |
| FS_Framework_Explanatory — *An Architectural Language for Dynamical Systems* | md ❌ |
| FS_primorial_epochs — *Primorial Epochs and the Tiling Structure* | md ❌ · promoted from Archive 2026-09 |
| DERIVATION_MODULES — 📄 index of the 18 untracked upstream modules | md |

### 2_One_Wheel_Many_Shadows — the main arc

| paper | formats |
|---|---|
| One_Wheel_Many_Shadows — 📄 the thesis | md |
| **The_Wheel_Is_The_Whole_Story** — the claim, audited *(new 2026-09)* | md ❌ |
| **Null_Model_Discipline** — five failure modes *(new 2026-09)* | md ❌ |
| Prime_Prediction_Budget | md, pdf |
| Prime_Gap_Memory_Differencing_Trap | md, pdf |
| PG_Angle_Wobble — *The Prime-Triangle Angle* | md ❌ |
| PG_Balance_Ratio_And_Koide | md ❌ |
| Switchback_Law — *the mod-6 traffic law* (rewritten 2026-09) | md ❌ |
| Prime_Structure_Factor | md ❌ (pdf lives in `3_`) |
| Offset_Correlation_Curve | md ❌ |
| ED_Negative_Control | md ❌ |
| FS_Consecutive_Prime_Sums_In_Gaps | md, pdf |
| FS_Seven_Sisters_Wheel_Asymptote | md, pdf |
| FS_2p_Bracket_Construction | md, pdf |
| FS_Synthesis_Doubling_and_Wheel | md, pdf |
| FS_Escape_Ridge | md, pdf |
| WORKLOG_2026-09, NOTES_Carry_Forward — 📄 working docs | md |
| `repro/regenerate_tables.py` — regenerates every measured table | py |
| `superseded/` — pre-September PG_Angle_Wobble, PG_Balance_Ratio, Differencing_Trap, Prediction_Budget | md, 2 pdf |

### 3_Twin_Bertrand_Prime_Geometry

| paper | formats |
|---|---|
| PG_I_PrimeTriangle — *The Prime Triangle* | md, pdf ✅ *converted from tex 2026-09* |
| PG_II_AngleRecord — *Angle-Record Theorem & TPB* | md, pdf ✅ *converted from tex 2026-09* |
| PG_III_GBP — *Generalized Bertrand Principle* | md, pdf ✅ *converted from tex 2026-09* |
| Prime_Structure_Factor | pdf (md in `2_`) |
| FS_TB_Bridge | md ❌ |
| FS_TB_DeltaX_Analysis | md ❌ |

✅ **The PG trilogy now has markdown**, converted with pandoc from the author's own `.tex` in the upstream `twin-bertrand` repo — recovered from git, not retyped from the PDFs. The PDFs are kept as the authoritative typeset version (figures, layout). **This was the collection's last pdf-only-in-substance gap in series 3.**

### 4_Philosophy_Ontology

| paper | formats |
|---|---|
| **The_Movie** — *the plain-language picture of the whole collection* (new 2026-09) | md ❌ |
| FS_TB_QM_Amplitude_Memo — *Template and Amplitude* | md ❌ |
| OPEN_QUESTION_FS_TB_QM_AMP_02_Bilinearity | md ❌ |
| Counting_Into_Existence | md ❌ |
| The_Wolves_and_the_Clock | md ❌ |

### 5_X5D_EXPDB

| paper | formats |
|---|---|
| X5D_Polyhedral-Reinterpretation | **pdf only** ⚠️ (md is `X5D_EXPDB_Reinterpretation`) |
| X5D_EXPDB_Reinterpretation | md ❌ |
| Theta_Gap2_Refinement | **pdf only** ⚠️ |

### Standing gaps

1. **~~PDFs~~ — resolved by going markdown-native (2026-09).** The 13 PDFs that merely mirrored a markdown source were removed; git retains them. Remaining PDFs are the ones that are the *only* copy of something: the PG trilogy's typeset version, `Prime_Structure_Factor.pdf`, and the two X5D papers. **No new PDFs are generated.**
2. **X5D is still pdf-only** — `X5D_Polyhedral-Reinterpretation.pdf` and `Theta_Gap2_Refinement.pdf` have no markdown and, unlike the PG trilogy, **no recoverable `.tex`** in the upstream repo. Converting them means transcription, with the attendant risk of silent formula errors.
3. **Reproducibility** — series 2 is fully covered (`2_One_Wheel_Many_Shadows/repro/`, every table regenerated and checked). Series 1 has `repro/entropy_budget.py` for the headline numbers only. Series 3 now ships the upstream scripts, **unverified**. Series 5 has a note saying what reproduction would require and why it is not a script. The remaining gap is series 1 beyond the entropy budget, and series 3 verification.
4. **Prior art** — the Archive is untracked, so an ordinary repo grep misses 18 derivation modules that the live papers cite. Search it explicitly before drafting; see [`DERIVATION_MODULES.md`](1_Factor_Skyline/DERIVATION_MODULES.md). This has already cost one draft.

---

## 1. The July 2026 consolidation (historical record)

**Status (2026-07-13):** consolidation executed — **all four projects now in `Primes/`.** Twin Bertrand, Prime Geometry precursor, and X5D EXPDB Framework were *moved* in; **Factor Skyline was *copied* in** (full repo incl. `.git`, HEAD `536c72a`, same GitHub remote) because it was the live session cwd and can't be moved from within itself. The Claude Code memory folder was pre-staged to the new project key `C--Users-allen-GitHub-Primes-Factor-Skyline`, so continuity carries over when you open `Primes\Factor Skyline`. `expdb-env` (venv) and `expdb-fresh` (Tao contributor clone) intentionally left outside `Primes/`; `Archives/Erdos Tao` stays in the Archive. **Remaining manual step:** delete the old `C:\Users\allen\GitHub\Factor Skyline` once you've confirmed the copy (see §7).

Legend: ✅ has PDF · ❌ needs PDF · ⚠️ source/issue to resolve · 📄 note/plan (not a standalone paper) · 🔗 duplicate/overlap

---

### 1a. The seven prime-related folders → nested target

| folder | what it is | outcome |
|---|---|---|
| **Factor Skyline** | repo `allen-proxmire/factor-skyline` | ✅ in `Primes/` (copied; delete the old `GitHub\Factor Skyline`) |
| **Twin Bertrand** | repo `allen-proxmire/twin-bertrand` — hosts **Prime Geometry I/II/III** (PDFs) | ✅ moved into `Primes/` |
| **Prime Geometry** | un-versioned folder, only **PG_I** (already in Twin Bertrand) | 🗑️ **deleted** (redundant) |
| **X5D EXPDB Framework** | repo `allen-proxmire/expdb-5d-polyhedral` | ✅ moved into `Primes/` |
| **Archives/Erdos Tao** | 10-section draft of the X5D paper (same title) | stays in `Archives/` |
| **expdb-fresh** | your **contributor clone** of Tao's `teorth/expdb` | kept outside `Primes/` |
| **expdb-env** | Python **virtualenv** | 🗑️ delete (regenerable) |

**Final structure (executed 2026-07-13, flat — you chose this over the theory/expdb grouping)**
```
GitHub/Primes/
├── PRIMES_MAP.md
├── Factor Skyline/        (repo — copied in; delete the old GitHub\Factor Skyline)
├── Twin Bertrand/         (repo — hosts Prime Geometry I/II/III as PDFs)
└── X5D EXPDB Framework/   (repo)
```
*Prime Geometry precursor deleted (held only PG_I, already in Twin Bertrand). Loose `.tex` removed where a PDF already exists (PG I/II/III, FS twin-geometry). `expdb-fresh` and `expdb-env` left outside `Primes/`; Tao's expdb is also **vendored** inside X5D at `compute/vendor/expdb/`.*

---

## 2. Paper inventory

### 2a. Factor Skyline — `theory/factor-skyline/papers/`

| paper | title | formats | PDF |
|---|---|---|---|
| FSPapers_01_architectural_foundation | The Architectural Foundation of the Factor Skyline | md, pdf | ✅ |
| FSPapers_02_correlation_theory | The Correlation Theory of the Factor Skyline | md | ❌ |
| FSPapers_02.1_correlations_and_randomness | Correlations and Randomness in the Factor Skyline | md | ❌ |
| FSPapers_03_information_dynamics_universality | Information, Dynamics, and Universality… | md | ❌ |
| FSPapers_04_meta_structure | The Meta-Structure of the Factor Skyline | md | ❌ |
| FS_Framework_Explanatory | The Factor Skyline Framework: An Architectural Language for Dynamical Systems | md | ❌ 🔗 (title ≈ X5D_Framework) |
| FS_twin_prime_geometry | The Twin-Slope Ceiling: Twin Prime Geometry on the FS | md, tex, pdf | ✅ 🔗 (relates to PG trilogy) |
| FS_Consecutive_Prime_Sums_In_Gaps | *(this session)* density law + forbidden widths | md, pdf | ✅ |
| FS_2p_Bracket_Construction | *(this session)* signature = Seven Sisters, mirror law | md, pdf | ✅ |
| FS_Seven_Sisters_Wheel_Asymptote | *(this session)* wheel + 100% asymptote | md, pdf | ✅ |
| FS_Seven_Sisters_2p_plus_k | *(imported)* the original 2p+k note | pdf | ⚠️ pdf-only, no md source in repo |
| FS_Synthesis_Doubling_and_Wheel | *(this session)* the synthesis | md, pdf | ✅ |
| FS_Escape_Ridge | *(this session)* x_FS ~ N^{3/2}/ln²N, p² sweeps | md, pdf | ✅ |
| Archive/monograph/FS_monograph | Factor Skyline monograph | md, pdf | ✅ (archived) |
| Archive/… (2 original papers, glossary, manuscript) | early drafts | pdf / md | archived |

*Also: 17 `modules/*.md` (building-block notes) and 9 `archive/FS_0X_*.md` (old program drafts) — components, not standalone papers.*

**Compile target:** FSPapers **02, 02.1, 03, 04** are the rest of the main series (01 is already a PDF) → render all four. Plus FS_Framework_Explanatory.

### 2b. Twin Bertrand — `theory/twin-bertrand/papers/`

| paper | title | formats | PDF |
|---|---|---|---|
| PG_I_PrimeTriangle | Prime Geometry I: (Prime Triangle) | pdf | ✅ (tex removed) |
| PG_II_AngleRecord | Prime Geometry II: (Angle Record) | pdf | ✅ (tex removed) |
| PG_III_GBP | Prime Geometry III: (GBP) | pdf | ✅ (tex removed) |
| FS_TB_Bridge | The Factor Skyline – Twin Bertrand Bridge | md | ❌ (note-style) |
| FS_TB_DeltaX_Analysis | The Δx / Cascade Analysis | md | ❌ |
| FS_TB_QM_Amplitude_Memo | Template and Amplitude: …Quantum-Mechanical Form | md | ❌ |
| FS_TB_Integration_Plan | integration plan | md | 📄 plan |
| OPEN_QUESTION_FS_TB_QM_AMP_02_Bilinearity | open-question memo | md | 📄 open Q |
| PG_FieldGuide (root) | field guide | md | 📄 |

**The Prime Geometry trilogy (I/II/III) lives here, compiled.** These are the most publication-ready, likely Zenodo candidates.

### 2c. Prime Geometry (standalone folder) — DELETED

The precursor folder held only PG_I, which already lives in Twin Bertrand, so it was **deleted 2026-07-13**. The Prime Geometry work remains fully present in Twin Bertrand (PG I/II/III PDFs, analysis scripts, datasets).

### 2d. X5D EXPDB Framework — `expdb/x5d-expdb-framework/`

| paper | title | formats | PDF |
|---|---|---|---|
| X5D_EXPDB_Reinterpretation / X5D_Polyhedral-Reinterpretation | X5D: A Polyhedral Reinterpretation of the Exponent Database as a 5-D Geometric Flow | md, pdf | ✅ (md & pdf names differ) |
| Theta_Gap2_Refinement | Θ / Gap-2 refinement | pdf | ⚠️ pdf-only, no md/tex source found |
| GuthMaynard_BindingConstraints | Guth–Maynard binding constraints | md, pdf | ✅ |
| GuthMaynard_BindingConstraints_v2 | (v2) | md, tex | ❌ |
| GuthMaynard_EXPDB_Analysis | analysis | md | 📄 |
| X5D_Framework | The X5D Framework: An Architectural Language for Dynamical Systems | md | 🔗 (≈ FS_Framework_Explanatory) |

*Plus `framework/methodology/**` (process docs) and `compute/vendor/expdb/**` (Tao's vendored clone — reference).*

### 2e. Archives/Erdos Tao — superseded

10 markdown sections (`section1…section10`) titled **"The EXPDB Skyline: A Polyhedral Reinterpretation…"** — the **sectioned earlier draft** of the X5D paper above. No PDF. → archive; the X5D repo version supersedes it (unless it has content the single-file version dropped — worth a diff before discarding).

---

## 3. Cross-folder overlaps to reconcile

1. 🔗 **Prime Geometry trilogy** — canonical in Twin Bertrand; PG folder duplicates only PG_I. **Pick one home.**
2. 🔗 **X5D polyhedral paper** — single-file + PDF in X5D repo; sectioned draft in Erdős-Tao. **Diff, then archive the draft.**
3. 🔗 **Tao's expdb** — appears twice: `expdb-fresh` (your contributor clone) and `X5D/compute/vendor/expdb` (vendored for builds). Both legitimate; label them so it's clear which is which.
4. 🔗 **Framework doc** — `FS_Framework_Explanatory` (FS) and `X5D_Framework` (X5D) share the subtitle "An Architectural Language for Dynamical Systems." **Same doc in two programs?** Reconcile or cross-reference.
5. 🔗 **Twin-prime geometry** — FS's "Twin-Slope Ceiling" vs the PG trilogy: related twin-prime-geometry threads; confirm they're distinct papers, not divergent copies.

---

## 4. What needs building / PDFs

**Compile to PDF (source exists, PDF missing):**
- Factor Skyline: FSPapers_02, 02.1, 03, 04; FS_Framework_Explanatory
- Twin Bertrand: FS_TB_Bridge, FS_TB_DeltaX_Analysis, FS_TB_QM_Amplitude_Memo *(if you want them as papers, not just notes)*
- X5D: GuthMaynard_BindingConstraints_v2 (tex→pdf)
- Erdős-Tao: assemble 10 sections → one doc → PDF *(only if it has unique content vs the X5D version)*

**Missing source (pdf-only — locate or regenerate .md/.tex):**
- FS_Seven_Sisters_2p_plus_k.pdf (source is your `seven-sisters` GitHub repo)
- X5D Theta_Gap2_Refinement.pdf

The pandoc/xelatex pipeline in `factor-skyline` (`make papers`) works and can be reused everywhere.

---

## 5. Zenodo / DOI — resolved for this repo

**Settled 2026-07:** this collection took a **repo-level DOI** via the GitHub→Zenodo release hook, tagged `v1.0`, badge in the README.

- **Primes (this repo):** [10.5281/zenodo.21626683](https://doi.org/10.5281/zenodo.21626683) — tag `v1.0`
- **Factor Skyline** (upstream repo): [10.5281/zenodo.18275273](https://doi.org/10.5281/zenodo.18275273)
- **X5D EXPDB** (upstream repo): [10.5281/zenodo.19454867](https://doi.org/10.5281/zenodo.19454867)

**What this settles.** The repo-level DOI snapshots the whole collection at a tag, so the archived record is frozen and reorganising the live repo cannot break it. Filenames were rearranged in September 2026 (v2 papers promoted to canonical names, originals to `2_One_Wheel_Many_Shadows/superseded/`) with no effect on the `v1.0` snapshot — which is the point of tagging.

**Still open — standalone paper DOIs.** Not done, and not obviously needed while the repo DOI covers the collection. If pursued, the candidates remain:
- Prime Geometry I / II / III (polished tex→pdf) — **note the asymmetry: these exist in the curated collection only as PDFs, with no markdown source.** They are the most citable and the least editable work here.
- X5D Polyhedral Reinterpretation
- FS Architectural Foundation (or the FS monograph as an umbrella)
- *New candidate (Sept 2026):* [*The Null-Model Discipline*](2_One_Wheel_Many_Shadows/Null_Model_Discipline.md) — the only material here whose audience is plausibly outside number theory.

**Cut a new tag before the next DOI pass.** `v1.0` predates the September work (balance ratio, the wheel-is-the-whole-story audit, the null discipline, the RESULTS.md rebuild).

---

## 6. Which repo is public?

You said "just one public." `gh` lookup returned empty this session — **verify** visibility of `factor-skyline`, `twin-bertrand`, `expdb-5d-polyhedral` before any publish/DOI step (it affects what a Zenodo hook would expose).

---

## 7. Phased checklist

- [x] **Prime Geometry's fate** — keep the precursor folder *and* keep PG I–III in Twin Bertrand.
- [x] **Create `Primes/`** and move Twin Bertrand, Prime Geometry precursor, X5D in (done, repos intact).
- [x] **Factor Skyline in `Primes/`** — copied in full (incl. `.git`), verified identical (HEAD `536c72a`, same remote). Memory pre-staged to the new project key for continuity.
- [ ] **Delete the OLD `Factor Skyline`** — after you've opened `Primes\Factor Skyline` and confirmed it's good, remove the original so there aren't two working copies of the same repo:
  ```powershell
  Remove-Item -Recurse -Force "C:\Users\allen\GitHub\Factor Skyline"
  ```
  (Claude won't hard-delete; this one's on you. Until then, two copies point at the same GitHub remote — just work in the `Primes` copy.)
- [ ] **Delete `expdb-env`** yourself (regenerable venv; Claude won't hard-delete): `Remove-Item -Recurse -Force "C:\Users\allen\GitHub\expdb-env"`.
- [x] **Update path references** in memory (Twin Bertrand, Prime Geometry done; Factor Skyline pending its move).
- [x] **Compile the PDF gaps** — FSPapers 02, 02.1, 03, 04 done. Remaining: FS_Framework_Explanatory, TB notes, GuthMaynard_v2 (§4).
- [x] **Zenodo pass** (§5) — repo-level DOI live (10.5281/zenodo.21626683, tag `v1.0`). Standalone paper DOIs still open; cut a new tag first, `v1.0` predates the September work.
- [x] **Reconcile overlaps** (§3) — PG kept as precursor + in TB; Erdős-Tao stays archived; framework-doc dup left as-is.
