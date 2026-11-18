# 1 — The Factor Skyline

**The lens.** Each integer $n$ is a column of width $\mathrm{lpf}(n)$ and height $n/\mathrm{lpf}(n)$. Primes escape to the diagonal; composites fall onto a fan of width-rays. The coordinate system and the theory built on it.

**Start with:** [FSPapers I](FSPapers_01_architectural_foundation.md). The one idea to take away is in [FSPapers 02.1 §13](FSPapers_02.1_correlations_and_randomness.md): the escape layer has Kolmogorov complexity $K=O(\log N)$ but Shannon entropy $H\sim0.26N$ bits — a napkin rule whose output passes every randomness test.

| file | contents |
|---|---|
| [FSPapers I](FSPapers_01_architectural_foundation.md) | the architecture; coverage protection $C_H>1$; template persistence |
| [FSPapers II](FSPapers_02_correlation_theory.md) | correlation theory |
| [FSPapers 02.1](FSPapers_02.1_correlations_and_randomness.md) | correlations and randomness — why the primes look random |
| [FSPapers III](FSPapers_03_information_dynamics_universality.md) | information, dynamics, universality |
| [FSPapers IV](FSPapers_04_meta_structure.md) | the meta-structure |
| [Primorial Epochs](FS_primorial_epochs.md) | §2.2: from $p\ge5$ the epoch $[p_k^2,p_{k+1}^2)$ is shorter than one template period |
| [Framework, explanatory](FS_Framework_Explanatory.md) | the skyline as an architectural language for dynamical systems |
| [Architectural map](FS_architectural_map.md) · [Glossary](FS_glossary.md) | reference |
| [`modules/`](modules/) · [index](DERIVATION_MODULES.md) | the 17 derivation notes the papers cite — PNT, Chebyshev, Möbius, Cramér, Goldbach, twins, constellations, smooth numbers, … |
| [`repro/`](repro/) | `entropy_budget.py` — the headline entropy numbers |
