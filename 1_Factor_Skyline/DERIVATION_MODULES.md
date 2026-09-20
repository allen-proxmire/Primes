# The derivation modules — where they are, and why grep misses them

**Read this before drafting anything new.** The five FS papers in this folder are the canon. They cite **18 derivation modules** as supporting documents, and those modules sit in `Archive/` — the **discontinued** Factor Skyline repo, kept as reference while it was unclear what in it was worth keeping. `Archive/` is untracked and not public; **this repository and folders 1–5 are the canon.**

> **Resolved 2026-09-20 — all 17 are now here.** The [Archive Survey](../meta/ARCHIVE_SURVEY.md) promoted the whole derivation layer into [`modules/`](modules/), so the collection no longer cites documents it does not contain. **This page is now an index of what is present, not a pointer into a dead repo.** The rule that produced it — *when something in the Archive matters, promote it, don't cite it* — still stands for anything found later.

> **2026-09-20.** A note was drafted deriving "the wheel's period outgrows the window in which it is the operative rule," presented as a new structural result. It was already in `FS_primorial_epochs.md` §2.2 — stated earlier, with a better-chosen denominator (the activation epoch rather than cumulative territory), and put to work explaining why gap-6 dominates for so long. The draft was deleted. **The search that would have prevented it takes one command.**

## The search that prevents this

```bash
grep -rn -i "your phrase here" "Archive/Factor Skyline/modules/" "Archive/Factor Skyline/archive/" 1_Factor_Skyline/
```

## Promoted into this folder

- [`FS_primorial_epochs.md`](FS_primorial_epochs.md) — *Primorial Epochs and the Tiling Structure of the Factor Skyline.* Promoted out of the Archive because §2.2 contains a live result the collection keeps reaching for: activation epochs and primorial periods are two different partitions of the integers, and from p ≥ 5 the period outgrows the epoch, so **the full primorial structure is never "seen" within a single epoch** — it is trans-epochal. Also the reason gap-6 dominates so long: the 5#-template is the last where epoch length ≈ period length (24 vs 30).

## The rest, in `Archive/Factor Skyline/modules/` (untracked)

| module | subject |
|---|---|
| `FS_ontology.md` | Formal definitions, classical correspondences, and the PNT |
| `FS_sieve_geometry.md` | The Sieve of Eratosthenes as FS-geometry |
| `FS_PNT_derivation.md` | The Prime Number Theorem as an FS theorem |
| `FS_prime_gaps.md` | Prime gaps in FS-geometry |
| `FS_Cramer.md` | Cramér's conjecture in FS-geometry |
| `FS_short_intervals.md` | Square windows and the Chebyshev–Bertrand corridor |
| `FS_Chebyshev.md` | The Chebyshev functions θ(x) and ψ(x) |
| `FS_residue_classes.md` | Residue classes and Dirichlet structure |
| `FS_constellations.md` | Prime constellations |
| `FS_twin_primes.md` | Twin primes in FS-geometry |
| `FS_Goldbach.md` | Goldbach's conjecture in FS-geometry |
| `FS_Mobius.md` | The Möbius function and Möbius randomness |
| `FS_smooth_numbers.md` | Smooth numbers |
| `FS_divisors.md` | Divisor functions τ(n) and σ(n) |
| `FS_explicit_formula.md` | The explicit formula |
| `FS_RH_analogue.md` | The Riemann Hypothesis in FS-geometry |
| `FS_zero_geometry.md` | The nontrivial zeros of zeta in the skyline |

Further supporting documents (`FS_universality.md`, `FS_meta_mathematics.md`, `FS_entropy.md`, `FS_ergodicity.md`, the research-program synthesis) are cited by `FSPapers_02.1` and `FSPapers_04` and live in the same upstream repo.

## Two results in the FS papers that keep getting rediscovered

Both are in this folder, both are easy to re-derive from scratch without noticing:

- **`FSPapers_02.1` §13.2–13.3** — the escape layer has Kolmogorov complexity **K = O(log N)** against Shannon entropy **H ~ 0.26N**: "the hallmark of pseudo-randomness… a simple rule that passes statistical tests." §13.3 is titled *The randomness paradox resolved.* Any new argument of the form "the primes look random because the rule is cheap but the output is complex" **is this**, and should cite it.
- **`FSPapers_01` Def. 2.7 + Thm 3.3** — the activation epoch [p_k², p²_{k+1}) and the primorial template's period p_k#. Any new argument comparing what the sieve *decides* against what the sieve's pattern *would need in order to repeat* is [`FS_primorial_epochs`](FS_primorial_epochs.md) §2.2.
