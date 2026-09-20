# Reproduction scripts — Twin Bertrand / Prime Geometry

Brought across from the upstream `twin-bertrand` repository (2026-09-20), because the papers here cite them by name and the collection previously shipped neither the scripts nor the figures they produce.

| script | what it does | cited by |
|---|---|---|
| `pg_deltax_unified.py` | the Δx cascade — doubled twins on a prime-rank axis, Poisson-mixture fit, macro-linearity | [FS_TB_DeltaX_Analysis](../FS_TB_DeltaX_Analysis.md) |
| `pg_twin_angle_analysis.py` | prime-triangle angles and the angle-record structure | [PG II](../PG_II_AngleRecord.md) |
| `pg_structural_1e10.py` | the structural TPB verification run | [PG II](../PG_II_AngleRecord.md) |
| `pg_extend_1e10.py` | extends the twin-gap verification to 10¹⁰ | [PG II](../PG_II_AngleRecord.md), [PG III](../PG_III_GBP.md) |
| `pg_twin_ramanujan.py` | the Ramanujan-prime comparison | [PG II](../PG_II_AngleRecord.md) |
| `pg_qm_amplitude_probe.py` | the amplitude probe | [QM Amplitude Memo](../../4_Philosophy_Ontology/FS_TB_QM_Amplitude_Memo.md) |

## Status — read before trusting

**These have not been re-run or verified in this repository.** They are the author's originals, carried over so the papers' citations resolve and so the work is *inspectable*. That is a weaker guarantee than [`2_One_Wheel_Many_Shadows/repro/`](../../2_One_Wheel_Many_Shadows/repro/), where every table was regenerated and checked against what the papers print — a process that found two wrong numbers.

**The headline claims in this series are therefore still unverified here**, including:

- TPB verified to 10¹⁰ (27.4M twins) — the 10¹⁰ runs are expensive and were not repeated
- the angle-record theorem (every record with p ≥ 3 is a twin)
- the twin-gap exponent $G_k \sim 0.70(\log T_k)^{1.866}$
- the GBP envelope $G < 0.171(\log P)^{3.22}$
- the PSD identity and its integrality — *this one is pure algebra and cheap to check; it is the obvious first target*

Series 2's experience suggests the cheap checks are worth doing: the Switchback run-length law and the Differencing Trap's recoil row both stood for two months and both failed on first re-run.
