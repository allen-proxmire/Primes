# PRIMES — Master Map

*Lives at `GitHub/Primes/PRIMES_MAP.md`.*

> **This file is the current inventory.** The July 2026 consolidation record — how four project repos became one collection — has moved to [`meta/CONSOLIDATION_2026-07.md`](meta/CONSOLIDATION_2026-07.md). It described a folder layout that no longer exists and kept being mistaken for the inventory. Its decisions still bind; it simply is not this.

---

## 0. Current inventory (2026-09-20)

**Structure.** Five numbered reading series — **these plus the root files are the canon, and the only thing public.** `Archive/` holds three **discontinued** project repos (Factor Skyline, Twin Bertrand, X5D EXPDB), kept as reference while it was unclear what in them was worth saving. They are untracked by design (see [`.gitignore`](.gitignore)), not authoritative, and nothing in them should be cited as canon. **When something in there matters, promote it into folders 1–5** — as was done with `FS_primorial_epochs.md`, the PG trilogy's LaTeX, seven figures and six analysis scripts in September 2026.

```
GitHub/Primes/
├── README.md · RESULTS.md · PRIMES_MAP.md
├── 1_Factor_Skyline/              the coordinate system and its theory
├── 2_One_Wheel_Many_Shadows/      the main arc (most active)
│   ├── repro/                     regenerates every measured table
│   └── superseded/                pre-September versions of 4 papers
├── 3_Twin_Bertrand_Prime_Geometry/
├── 4_Philosophy_Ontology/
│   ├── figures/                   the rolling-wheels animation
│   └── repro/                     regenerates The Ninety Percent Rule
├── 5_X5D_EXPDB/
└── Archive/                       DISCONTINUED repos — reference only, not canon
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
| **The_Ninety_Percent_Rule** — *the prediction result: four wheels, slots for 90% by decade, the formula that predicts it* (new 2026-09) | md ❌ · reproduced by `repro/` |
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
4. **Prior art** — an ordinary repo grep misses the Archive, where 18 derivation modules the live papers cite still sit. Search it explicitly before drafting; see [`DERIVATION_MODULES.md`](1_Factor_Skyline/DERIVATION_MODULES.md). This has already cost one draft. **Reference, not canon** — if something in there proves load-bearing, promote it rather than cite it.
5. **The Archive has not been surveyed.** It was kept because *something* in it was worth saving, without a decision on what. Four promotions happened in September 2026 by accident, each because a live paper turned out to need something. A deliberate pass has never been made.

---
