# Reproducing X5D — what it would take

**There is no reproduction script here, and adding a token one would misrepresent the situation.** This note says honestly what reproducing the X5D results requires.

## Why it is different from the other series

Series 1–3 are measurements over the integers: sieve, count, compare against a null. A few hundred lines of standard library suffices, and [`2_One_Wheel_Many_Shadows/repro/`](../../2_One_Wheel_Many_Shadows/repro/) does exactly that.

X5D is not that. Its claims are about a **polytope in ℝ⁵** derived from the Tao–Trudgian–Yang Exponent Database, and reproducing them needs:

- the **EXPDB framework itself** — `polytope.py`, `region.py`, `derived.py`, `literature.py`, `hypotheses.py`, `zero_density_estimate.py` and the rest, which the papers cite by module name throughout
- a **vendored copy of Tao's `expdb`**, which the upstream repo carries at `compute/vendor/expdb/`
- exact rational / polyhedral arithmetic, not floating-point sieving

All of it lives in the untracked `Archive/X5D EXPDB Framework/`, which is the upstream repo with its own git history.

## The claims that would need checking

| claim | how hard |
|---|---|
| Master polytope: every EXPDB output is a projection/envelope of one 𝒫 ⊂ ℝ⁵ | needs the full framework |
| X5D invariant, monotone contraction flow, fixed-point theorem | derivations, not measurements |
| Guth–Maynard cusp at σ = 7/10; Ingham 1940 meets GM 2024 at A = 30/13 | **checkable by hand** — two line intersections |
| θ_PNTALL = 17/30 | follows from the cusp |
| sensitivity dθ/d‖A‖ = 169/900, attack surface ≈ 0.006 wide | small rational computation |

**The bottom three are arithmetic on a handful of rationals and could be verified in an afternoon without the framework.** That is the sensible first step if this series is ever brought up to the standard of series 2.

## Also missing

`X5D_Polyhedral-Reinterpretation.pdf` and `Theta_Gap2_Refinement.pdf` are **pdf-only** and, unlike the PG trilogy, have **no recoverable `.tex`** in the upstream repo — so converting them to markdown would mean transcription, with the attendant risk of silent formula errors. Left alone deliberately.
