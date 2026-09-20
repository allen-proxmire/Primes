# 3 — Twin Bertrand & Prime Geometry

**One conjecture, and the geometry that makes it visible.**

The conjecture: past 11, every doubling window contains a twin prime pair. Verified to 10 billion — 27.4 million twins, no exceptions. It is weaker than the twin prime conjecture, stronger than the bounded-gaps results, and immediate if Hardy–Littlewood holds.

The geometry: draw a right triangle from each consecutive prime pair. The angles climb toward 45° but never reach it, and **every record-setting angle is a twin pair** — which is the conjecture above, restated.

**Start with:** [PG II](PG_II_AngleRecord.md), which carries both. [PG I](PG_I_PrimeTriangle.md) builds the triangle and its identities; [PG III](PG_III_GBP.md) extends the conjecture to cousins and sexy primes.

**On the markdown:** PG I–III were converted from the author's original LaTeX in September 2026 — not retyped from the PDFs, so the mathematics is the original source. The PDFs remain authoritative for typesetting and figures.

**Reproducibility — read this before trusting anything here.** [`scripts/`](scripts/) holds the original analysis code, carried over so the papers' citations resolve. **Apart from one check, it has not been re-run or verified in this repository.**

**Two claims have now been checked:**

- [`check_angle_records.py`](scripts/check_angle_records.py) — PG II's **angle-record theorem**, which by Theorem 6 is *logically equivalent* to the Twin-Prime Bertrand Postulate and is therefore the load-bearing claim of the series. **Clean.** Exact integer arithmetic over every consecutive pair to $10^8$: 440,312 records, 440,312 twins, zero non-twin records — and the two sequences coincide exactly rather than one merely containing the other.
- [`check_psd.py`](scripts/check_psd.py) — PG I's square-difference results. **Found an off-by-one.** The last-digit theorem is published for $p_n \ge 5$ and is false there; $(5,7,11)$ is the sole counterexample and the statement should read $p_n \ge 7$. The identity and integrality claims are confirmed. See [PG I](PG_I_PrimeTriangle.md) at Theorem 5.

**Still unverified here:** the 10-billion twin verification, the twin-gap exponent, and the GBP envelope.

*Plain-language versions: [The Movie](../4_Philosophy_Ontology/The_Movie.md) · [What We Found](../WHAT_WE_FOUND.md)*
