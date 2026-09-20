# Verification reports

The computational evidence behind PG II and PG III. Promoted out of the discontinued Twin Bertrand repo on 2026-09-20 — these existed all along and had simply never been brought into the collection, which is why series 3's claims read as unsupported.

| report | what it establishes |
|---|---|
| `comparison_1e9_vs_1e10.md` | **The 10¹⁰ run.** 455,052,511 primes, 27,412,679 twin pairs, **zero TPB exceptions**, 285 s. Twin growth 8.005× against the Hardy–Littlewood prediction of ~8.100×. |
| `summary.md` | The 10⁹ analysis — counts, sup rₖ, and the angle-record structure. |
| `report_structural_1e10.md` | Structural extension of PG II to 10¹⁰. |
| `twin_ramanujan_report.md` | The twin-Ramanujan primes $R^{\mathrm{twin}}_n$, and TPB as the identity $R^{\mathrm{twin}}_1 = 11$. |
| `uniform_envelope_fits.md` | The GBP envelope fits across twins (g=2), cousins (g=4) and sexy primes (g=6), all to 10¹⁰. |
| `qm_amplitude_probe.md` | Verdict on the bilinearity open question in [Philosophy & Ontology](../../4_Philosophy_Ontology/OPEN_QUESTION_FS_TB_QM_AMP_02_Bilinearity.md). |

**Status.** These are the author's original reports, promoted so the claims have visible support. **They have not been independently re-run in this repository** — that is a separate matter from the evidence existing. Two series-3 claims *have* been re-verified here in September ([`scripts/`](../scripts/)): the angle-record theorem, which came back clean, and PG I's last-digit theorem, which came back off by one prime.

The envelope fits in particular are curve fits rather than exact checks, and fits are where overclaiming is easiest — they remain the most attractive target for the next verification pass.
