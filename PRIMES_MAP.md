# PRIMES — Master Map

*Lives at `GitHub/Primes/PRIMES_MAP.md`.*

**Status (2026-07-13):** consolidation executed — **all four projects now in `Primes/`.** Twin Bertrand, Prime Geometry precursor, and X5D EXPDB Framework were *moved* in; **Factor Skyline was *copied* in** (full repo incl. `.git`, HEAD `536c72a`, same GitHub remote) because it was the live session cwd and can't be moved from within itself. The Claude Code memory folder was pre-staged to the new project key `C--Users-allen-GitHub-Primes-Factor-Skyline`, so continuity carries over when you open `Primes\Factor Skyline`. `expdb-env` (venv) and `expdb-fresh` (Tao contributor clone) intentionally left outside `Primes/`; `Archives/Erdos Tao` stays in the Archive. **Remaining manual step:** delete the old `C:\Users\allen\GitHub\Factor Skyline` once you've confirmed the copy (see §7).

Legend: ✅ has PDF · ❌ needs PDF · ⚠️ source/issue to resolve · 📄 note/plan (not a standalone paper) · 🔗 duplicate/overlap

---

## 1. The seven prime-related folders → nested target

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

## 5. Zenodo / DOI — open items (needs your input or a Zenodo lookup)

You said "a couple papers on Zenodo" — **which two aren't recorded here yet.** To resolve:
- Search Zenodo for "Allen Proxmire" and list existing DOIs → tag each paper *on-Zenodo? / DOI*.
- Decide **repo-level DOI** (GitHub→Zenodo release hook, one DOI per repo) vs **standalone paper DOI**.

**Standalone-DOI candidates (most publication-ready):**
- Prime Geometry I / II / III (polished tex→pdf)
- X5D Polyhedral Reinterpretation
- FS Architectural Foundation (or the FS monograph as an umbrella)

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
- [ ] **Zenodo pass** (§5) — deferred (you'll hide/republish later).
- [x] **Reconcile overlaps** (§3) — PG kept as precursor + in TB; Erdős-Tao stays archived; framework-doc dup left as-is.
