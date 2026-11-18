# 3 — Twin Bertrand & Prime Geometry

**One conjecture, and two geometries that reach it.** Every $(x,2x]$ with $x\ge11$ contains a twin prime: $\pi_2(2x)-\pi_2(x)\ge1$. Verified to $10^{10}$ — 27,412,679 twins, no exceptions.

**Start with:** [PG II](PG_II_AngleRecord.md) — the angle-record theorem, logically equivalent to the conjecture: TPB fails exactly when some angle record of the prime triangle is not a twin. Below $10^8$: 440,312 records, 440,312 twins, the same list.

| file | contents |
|---|---|
| [PG I — The Prime Triangle](PG_I_PrimeTriangle.md) ([pdf](PG_I_PrimeTriangle.pdf)) | $\mathrm{PSD}_n=(p_{n+2}^2-p_n^2)/12$; last digit 0/4/6 for $p_n\ge7$ |
| [PG II — Angle Records and TPB](PG_II_AngleRecord.md) ([pdf](PG_II_AngleRecord_TBConjecture.pdf)) | the conjecture; Proposition 6A: every twin is a record |
| [PG III — Generalized Bertrand](PG_III_GBP.md) ([pdf](PG_III_GBP.pdf)) | cousins and sexy primes, verified to $10^{10}$ |
| [Twin-Slope Ceiling](FS_twin_prime_geometry.md) | skyline slope $\le\arctan\frac23$, attained iff twin — the second route to TPB |
| [FS–TB Bridge](FS_TB_Bridge.md) | twin-open positions per primorial period $1,1,3,15,135,1485,\dots$ |
| [FS–TB Δx Analysis](FS_TB_DeltaX_Analysis.md) | the Δx cascade on a prime-rank axis |
| [Field Guide](PG_FieldGuide.md) | plain-language tour of the prime triangle |
| [Literature review](literature_review.md) | TPB and GBP against Ramanujan primes, Zhang–Maynard, Heath-Brown |
| [`results/`](results/) | verification reports, including the $10^{10}$ run |
| [`scripts/`](scripts/) | analysis code; `check_angle_records.py`, `check_psd.py` and `check_envelope_fits.py` are the independently re-run checks |

PG I–III markdown is converted from the original LaTeX; the PDFs are the typeset versions.
