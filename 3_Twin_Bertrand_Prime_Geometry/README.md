# 3 — Twin Bertrand & Prime Geometry

**One conjecture, and the geometry that makes it visible.**

The conjecture: past 11, every doubling window contains a twin prime pair. Verified to 10 billion — 27.4 million twins, no exceptions. It is weaker than the twin prime conjecture, stronger than the bounded-gaps results, and immediate if Hardy–Littlewood holds.

The geometry: draw a right triangle from each consecutive prime pair. The angles climb toward 45° but never reach it, and **every record-setting angle is a twin pair** — which is the conjecture above, restated.

**Start with [the Field Guide](PG_FieldGuide.md)** — a plain-language narrative tour of PG I–III, no notation required. Then [PG II](PG_II_AngleRecord.md), which carries the conjecture and the angle-record theorem; [PG I](PG_I_PrimeTriangle.md) builds the triangle and its identities; [PG III](PG_III_GBP.md) extends to cousins and sexy primes.

**Also here, recovered from the Archive in September 2026** (see the [survey](../meta/ARCHIVE_SURVEY.md)):

- **[The Twin-Slope Ceiling](FS_twin_prime_geometry.md)** — a complete paper, and a *different* geometry from the PG trilogy: it works on the Factor Skyline, where the twin slope arctan(2/3) is an absolute ceiling. It isolates **the Filling Condition** as the one conjectural step between FS structure and the twin prime conjecture. **Read, assessed and reframed 2026-09-20:** the geometry holds — Theorem 4.2 verified to 10⁶ with zero exceptions, though its proof needed repair — but **the Filling Condition turns out to be TPB itself**, Form 3 being verbatim PG II's Conjecture 2, reached independently from the skyline side. The parity-barrier claim was withdrawn. **The paper has been rewritten around what survives** — a second, independent geometric route to TPB — and [PG II](PG_II_AngleRecord.md) now carries the cross-reference back. Two unrelated geometries, one conjecture: the triangle angle rising to 45°, the skyline slope capped at arctan(2/3).
- **[Literature review](literature_review.md)** — where TPB and GBP sit against Ramanujan primes, Zhang–Maynard, and Heath-Brown. The support for calling any of this new.
- **[`results/`](results/)** — the verification reports, including the 10¹⁰ run: 27,412,679 twins, zero exceptions.

**On the markdown:** PG I–III were converted from the author's original LaTeX in September 2026 — not retyped from the PDFs, so the mathematics is the original source. The PDFs remain authoritative for typesetting and figures.

**Reproducibility — read this before trusting anything here.** [`scripts/`](scripts/) holds the original analysis code, carried over so the papers' citations resolve. **Apart from one check, it has not been re-run or verified in this repository.**

**Two claims have now been checked:**

- [`check_angle_records.py`](scripts/check_angle_records.py) — PG II's **angle-record theorem**, which by Theorem 6 is *logically equivalent* to the Twin-Prime Bertrand Postulate and is therefore the load-bearing claim of the series. **Clean.** Exact integer arithmetic over every consecutive pair to $10^8$: 440,312 records, 440,312 twins, zero non-twin records — the two sequences coincide exactly. The converse inclusion is now written up as **Proposition 6A**, and it is *unconditional*: every twin is a record whether or not TPB holds. TPB is exactly the statement that there are no *other* records.
- [`check_psd.py`](scripts/check_psd.py) — PG I's square-difference results. **Found an off-by-one.** The last-digit theorem is published for $p_n \ge 5$ and is false there; $(5,7,11)$ is the sole counterexample and the statement should read $p_n \ge 7$. The identity and integrality claims are confirmed. See [PG I](PG_I_PrimeTriangle.md) at Theorem 5.

**On verification.** The 10¹⁰ evidence sits in [`results/`](results/) — it existed all along and had never been promoted. **The two curve fits have now been checked, and neither survives:** the twin-gap exponent measures ~2 (the Hardy–Littlewood value), not the claimed 1.866; and the GBP envelope $G<0.171(\log P)^{3.22}$ is violated 204 times below $10^8$, worst $1.87\times$, because it was fitted on $\sup(G/T)$ and then stated as a bound on $\sup(G)$. See [`check_envelope_fits.py`](scripts/check_envelope_fits.py).

**Scorecard for this series:** angle-record theorem clean; PSD identity clean but its last-digit theorem off by one prime; twin-gap exponent not reproduced; GBP envelope violated. The 10¹⁰ TPB verification itself has not been independently re-run.

*Plain-language versions: [The Movie](../4_Philosophy_Ontology/The_Movie.md) · [What We Found](../WHAT_WE_FOUND.md)*
