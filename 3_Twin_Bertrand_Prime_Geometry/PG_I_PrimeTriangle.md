# The Prime Triangle

### PG I — Prime Geometry

Allen Proxmire

> **Converted from LaTeX, 2026-09-20.** This markdown was produced with `pandoc` from `papers/PG_I_PrimeTriangle.tex` in the upstream `twin-bertrand` repository (commit `ddc4cca`), not retyped from the PDF — so the mathematics is the author's own source, not a transcription. Two mechanical changes were made for GitHub's MathJax: `\label{...}` markers and nested `equation` environments were stripped. **[PG_I_PrimeTriangle.pdf](PG_I_PrimeTriangle.pdf) remains authoritative for typesetting**, figures and page layout.

---

# Introduction

Prime gaps exhibit rich structure that is invisible at the level of the primes alone. This paper introduces a minimal geometric construction which encodes consecutive primes as right triangles and records prime-gap dynamics in the associated angles. The construction is elementary, and most of its identities are algebraically routine. Its value lies not in depth but in *angle*: by shifting the viewpoint from gaps to triangles, one discovers quantities whose record structure encodes non-trivial density information about the primes.

The Prime Triangle framework can be thought of as a *geometric microscope* on prime gaps. Consecutive-prime pairs produce triangles whose angles cluster near $`45^\circ`$, with twin primes approaching the limit fastest. Asking which pairs set new records in the angle sequence turns out to be equivalent to asking about the density of twin primes in dyadic intervals — an observation developed fully in PG II and generalized in PG III. The present note establishes the geometric objects and identities on which those companion papers rest.

Three themes run through the paper:

1.  *Geometric encoding.* The triangle $`(p_n, p_{n+1}, C_n)`$ records a prime pair; the angle $`\alpha_n = \arctan(p_n/p_{n+1})`$ records the asymmetry between the pair’s members.

2.  *Derived quantities.* Elementary algebra yields an exact identity $`C_2^{\,2} - C_1^{\,2} = p_{n+2}^{\,2} - p_n^{\,2}`$ and an always-integer quantity $`\mathrm{PSD}_n`$. Gap-scaled approximations produce a discrete energy $`E_n`$, curvature $`K_n`$, and normalized shape curvature $`\chi_n`$.

3.  *Dyadic interpretation.* The sequence of angle-records among consecutive prime pairs satisfies an elementary comparison rule that translates directly into a dyadic density statement on twin primes and, more generally, on admissible prime constellations. This is the hinge between the geometric object (the Prime Triangle) and the arithmetic statements of PG II–III.

Throughout, $`\mathbb{P}`$ denotes the primes, $`(p_n)_{n\ge 1}`$ the ordered list of primes (so $`p_1 = 2`$, $`p_2 = 3`$, $`\ldots`$), and $`\pi(x) = \#\{p \in \mathbb{P} : p \le x\}`$ the prime-counting function. For pair-constellation $`\mathcal{C} = \{0, g\}`$ with $`g \ge 2`$ even, the counting function $`\pi_{\mathcal{C}}(x) = \#\{p \le x : p \in \mathbb{P},\;p+g \in \mathbb{P}\}`$ specializes to $`\pi_2(x)`$ when $`g = 2`$.

# The Prime Triangle

## Construction

<div class="definition">

**Definition 1** (Prime Triangle). *For consecutive primes $`p_n < p_{n+1}`$, the *Prime Triangle* at index $`n`$ is the right triangle with legs $`p_n`$ and $`p_{n+1}`$ and hypotenuse
``` math
C_n \;:=\; \sqrt{p_n^{\,2} + p_{n+1}^{\,2}}.
```
We record the pair’s geometric parameters as
``` math
\alpha_n \;:=\; \arctan\!\left(\frac{p_n}{p_{n+1}}\right),
\qquad
\rho_n \;:=\; \frac{p_n}{p_{n+1}}.
```
The quantity $`\alpha_n`$ is the angle at the base of the leg of length $`p_{n+1}`$, and $`\rho_n = \tan \alpha_n`$.*

</div>

<div id="prop:basic" class="proposition">

**Proposition 2** (Basic properties). *For every $`n\ge 1`$:*

1.  *$`0 < \alpha_n < 45^\circ`$, equivalently $`0 < \rho_n < 1`$.*

2.  *$`\rho`$ and $`\alpha`$ are strictly monotone: for pairs $`(p,q)`$ and $`(p',q')`$ with $`p<q`$ and $`p'<q'`$, $`\rho(p,q) > \rho(p',q') \iff \alpha(p,q) > \alpha(p',q')`$.*

3.  *For a twin pair $`(p, p+2)`$, $`\rho(p,p+2) = p/(p+2)`$ and $`\alpha(p,p+2) \to 45^\circ`$ as $`p \to \infty`$.*

4.  *For any fixed gap $`g \ge 2`$, $`\alpha(p, p+g) \to 45^\circ`$ as $`p \to \infty`$; twin pairs achieve this limit fastest, followed by cousin pairs, sexy pairs, and so on.*

</div>

<div class="proof">

*Proof.* (i) follows from $`p_n < p_{n+1}`$, giving $`\rho_n < 1`$ and hence $`\alpha_n < 45^\circ`$. (ii) is immediate since $`\arctan`$ is strictly increasing on $`\mathbb{R}_{>0}`$. (iii) is direct computation: for twins, $`\rho(p,p+2) = 1 - 2/(p+2) \to 1`$. (iv) For gap $`g`$, $`\rho(p,p+g) = 1 - g/(p+g)`$; for fixed $`g`$ and large $`p`$, $`1 - \rho(p,p+g) \sim g/p`$, so smaller $`g`$ gives faster convergence. ◻

</div>

## Numerical illustration

The first few Prime Triangles:

<div class="center">

| $`n`$ | $`p_n`$ | $`p_{n+1}`$ | gap |     $`\alpha_n`$ |
|------:|--------:|------------:|----:|-----------------:|
|     1 |       2 |           3 |   1 | $`33.690^\circ`$ |
|     2 |       3 |           5 |   2 | $`30.964^\circ`$ |
|     3 |       5 |           7 |   2 | $`35.538^\circ`$ |
|     4 |       7 |          11 |   4 | $`32.471^\circ`$ |
|     5 |      11 |          13 |   2 | $`40.236^\circ`$ |
|     6 |      13 |          17 |   4 | $`37.405^\circ`$ |
|     7 |      17 |          19 |   2 | $`41.820^\circ`$ |
|     8 |      19 |          23 |   4 | $`39.558^\circ`$ |
|     9 |      23 |          29 |   6 | $`38.428^\circ`$ |
|    10 |      29 |          31 |   2 | $`43.091^\circ`$ |

</div>

Observe the behavior: twin pairs consistently produce the largest angles at each scale, with the angle monotonically approaching $`45^\circ`$ along the twin subsequence. Non-twin pairs interleave between twin records and always fall short of the preceding twin angle. This empirical pattern is made precise by the $`2P`$-beats lemma (Section <a href="#sec:angle-records" data-reference-type="ref" data-reference="sec:angle-records">4</a>) and the angle-record theorem of PG II.

# Derived Quantities

The Prime Triangle construction extends naturally to triples of consecutive primes, producing the identities and derived invariants collected in this section. Throughout, fix three consecutive primes $`p_n < p_{n+1} < p_{n+2}`$ and write
``` math
C_1 \;=\; \sqrt{p_n^{\,2} + p_{n+1}^{\,2}},
\qquad
C_2 \;=\; \sqrt{p_{n+1}^{\,2} + p_{n+2}^{\,2}}.
```

## The Prime Square-Difference Identity

<div id="thm:psd" class="theorem">

**Theorem 3** (PSD identity). *For every triple of consecutive primes,
``` math
C_2^{\,2} - C_1^{\,2} \;=\; p_{n+2}^{\,2} - p_n^{\,2}.
```
Equivalently, writing $`G_n := p_{n+2} - p_n`$ for the skip-one gap,
``` math
C_2^{\,2} - C_1^{\,2} \;=\; G_n\,(2 p_n + G_n).
```*

</div>

<div class="proof">

*Proof.* Direct expansion:
``` math
C_2^{\,2} - C_1^{\,2}
= \big[p_{n+2}^{\,2} + p_{n+1}^{\,2}\big]
- \big[p_n^{\,2} + p_{n+1}^{\,2}\big]
= p_{n+2}^{\,2} - p_n^{\,2}
= (p_{n+2} - p_n)(p_{n+2} + p_n)
= G_n(2p_n + G_n). \qedhere
```
 ◻

</div>

<div class="definition">

**Definition 4** (PSD factor). *The *Prime Square-Difference factor* at index $`n`$ is
``` math
\mathrm{PSD}_n \;:=\; \frac{p_{n+2}^{\,2} - p_n^{\,2}}{12}
\;=\; \frac{G_n\,(2 p_n + G_n)}{12}.
```*

</div>

<div id="thm:psd-int" class="theorem">

**Theorem 5** (Integrality and last-digit structure). *For every $`n`$ with $`p_n \ge 5`$:*

1.  *$`\mathrm{PSD}_n \in \mathbb{Z}`$.*

2.  *The last decimal digit of $`\mathrm{PSD}_n`$ is one of $`\{0, 4, 6\}`$.*

</div>

> **⚠️ Correction to part 2 (verified 2026-09-20). The threshold is wrong by one prime.**
>
> Part 2 is **false at $`p_n = 5`$**: the triple $`(5, 7, 11)`$ gives $`\mathrm{PSD} = (121-25)/12 = 8`$, whose last digit is $`8`$. That is the **only** counterexample — checked over all 348,511 consecutive-prime triples below $`5\times10^6`$. **Part 2 holds for $`p_n \ge 7`$, with no exceptions found.**
>
> **Where the proof slips.** The mod-6 step is sound, and it gives integrality (part 1) for $`p_n \ge 5`$ correctly — that threshold *is* sharp, since $`(2,3,5)`$ gives $`7/4`$ and $`(3,5,7)`$ gives $`10/3`$. But the last-digit claim additionally needs $`p^2 \equiv \pm 1 \pmod 5`$, which holds for every prime **except 5 itself**. At $`p_n = 5`$ the mod-5 argument has nothing to stand on.
>
> **Part 1 and Theorem 3 are confirmed as stated.** (Theorem 3 in fact requires no primality at all — the shared $`p_{n+1}`$ terms cancel for any three numbers.)
>
> **A further observation, not in the original.** Among $`p_n \ge 7`$ the three last digits are far from equidistributed: $`0`$ appears $`48.97\%`$ of the time against $`25.51\%`$ each for $`4`$ and $`6`$. The equality of $`4`$ and $`6`$ is **exact** (they count the two directions of one transition, which interleave, so the counts differ by at most one — measured difference: zero). The ratio of $`0`$ to the others is $`1.92`$, close to but *not* the $`2`$ a uniform model predicts; the shortfall is finite-range plus Lemke Oliver–Soundararajan residue correlations.
>
> Reproduce: [`scripts/check_psd.py`](scripts/check_psd.py).

<div class="proof">

*Proof.* Every prime $`p \ge 5`$ satisfies $`p \equiv \pm 1 \pmod 6`$. Writing $`p_n = 6a \pm 1`$, $`p_{n+2} = 6b \pm 1`$, a four-case expansion gives
``` math
(6b \pm 1)^{2} - (6a \pm 1)^{2} = 12(b - a)\big[3(a+b) \pm 1\big],
```
so $`12 \mid p_{n+2}^{\,2} - p_n^{\,2}`$ and $`\mathrm{PSD}_n`$ is an integer. For (ii), reducing modulo $`120 = \mathrm{lcm}(12, 10)`$ gives $`p_{n+2}^{\,2} - p_n^{\,2} \in \{0, 48, 72\} \pmod{120}`$, so $`\mathrm{PSD}_n \in \{0, 4, 6\} \pmod{10}`$. ◻

</div>

<div id="rem:psd-twin" class="remark">

**Remark 6** (Twin-structure specialization). *When $`G_n = 6`$, the three consecutive primes take one of the forms $`(p_n, p_n+2, p_n+6)`$ or $`(p_n, p_n+4, p_n+6)`$; in either case $`p_{n+1}`$ is a member of a twin prime pair. A direct computation from the identity gives
``` math
\mathrm{PSD}_n \;=\; \frac{6(2p_n + 6)}{12}
\;=\; \frac{p_n + p_{n+2}}{2} \;=\; p_{n+1} \pm 1,
```
where the sign encodes which adjacent pair forms the twin. This is the simplest case in which $`\mathrm{PSD}_n`$ pinpoints twin-prime structure within a triple.*

</div>

## Energy, curvature, and angle drift

<div class="definition">

**Definition 7** (Energy and skip-one gap). *For three consecutive primes, define the *energy transition*
``` math
E_n \;:=\; C_2 - C_1,
```
and recall $`G_n = p_{n+2} - p_n = g_n + g_{n+1}`$ with $`g_n = p_{n+1} - p_n`$.*

</div>

<div id="prop:energy" class="proposition">

**Proposition 8** (First-order expansion of $`E_n`$). *With $`g_n, g_{n+1} \ll p_n`$,
``` math
E_n \;=\; \frac{\sqrt{2}}{2}\,G_n \;+\; O\!\left(\frac{G_n^{\,2}}{p_n}\right),
```
and more precisely
``` math
\frac{E_n}{G_n} \;\approx\; \frac{\sqrt{2}}{2}
- \frac{g_n - g_{n+1}}{2\sqrt{2}\,(2p_n + G_n)}.
```*

</div>

<div class="proof">

*Proof sketch.* Taylor-expand $`\sqrt{(p_{n+1}+g_{n+1})^2 + p_{n+1}^{\,2}}
- \sqrt{p_n^{\,2} + p_{n+1}^{\,2}}`$ in $`g_{n+1}/p_{n+1}`$ and $`g_n/p_n`$ and collect first-order terms. ◻

</div>

<div class="definition">

**Definition 9** (Discrete curvature and shape curvature).
*``` math
\begin{align*}
K_n &:= E_{n+1} - E_n \qquad \text{(discrete curvature)},\\
\chi_n &:= K_n / E_n \qquad \text{(normalized shape curvature)}.
\end{align*}
```*

</div>

<div id="prop:chi" class="proposition">

**Proposition 10**. *Under the same first-order approximation,
``` math
K_n \;\approx\; \frac{\sqrt{2}}{2}\,(g_{n+2} - g_n),
\qquad
\chi_n \;\approx\; \frac{g_{n+2} - g_n}{g_n + g_{n+1}}.
```*

</div>

The quantity $`\chi_n`$ is a dimensionless, scale-free measure of how the prime-gap sequence bends at index $`n`$. It will be the central object of PG II and PG III’s empirical sections when examining sign-coherence and long-range structure; for the present paper it is enough to record its definition.

## Angle drift

<div class="definition">

**Definition 11** (Angle drift).
*``` math
\Delta \alpha_n \;:=\; \alpha_{n+1} - \alpha_n.
```*

</div>

<div id="prop:hierarchy" class="proposition">

**Proposition 12** (Derivative hierarchy). *In the first-order approximation, $`\Delta \alpha_n`$ behaves as a discrete first derivative of the sequence $`\{\alpha_n\}`$, and $`\chi_n`$ as a normalized discrete second derivative. Schematically,
``` math
\chi_n \;\longrightarrow\; \Delta \alpha_n \;\longrightarrow\; \alpha_n,
```
with each arrow indicating discrete integration.*

</div>

The hierarchy explains, in an elementary way, why the angle sequence $`\alpha_n`$ exhibits long coherent phases and suppressed extremes: curvature $`\chi_n`$ is small on average, so $`\Delta\alpha_n`$ is well-controlled, so $`\alpha_n`$ drifts smoothly toward its $`45^\circ`$ limit.

# Angle Dynamics and Records

## The angle-record sequence

<div class="definition">

**Definition 13** (Angle-record). *A consecutive prime pair $`(p_n, p_{n+1})`$ is an *angle-record* if $`\rho_n > \rho_m`$ for every $`m < n`$, equivalently $`\alpha_n > \alpha_m`$ for every $`m < n`$.*

</div>

By Proposition <a href="#prop:basic" data-reference-type="ref" data-reference="prop:basic">2</a>, the angle-record sequence is an infinite subsequence of the consecutive-prime-pair sequence. Its first few terms are:

<div class="center">

|  record \# |    $`p_n`$ | $`p_{n+1}`$ |     $`\alpha_n`$ |               type |
|-----------:|-----------:|------------:|-----------------:|-------------------:|
|          1 |          2 |           3 | $`33.690^\circ`$ | gap-1 initial pair |
|          2 |          5 |           7 | $`35.538^\circ`$ |               twin |
|          3 |         11 |          13 | $`40.236^\circ`$ |               twin |
|          4 |         17 |          19 | $`41.820^\circ`$ |               twin |
|          5 |         29 |          31 | $`43.091^\circ`$ |               twin |
|          6 |         41 |          43 | $`43.636^\circ`$ |               twin |
|          7 |         59 |          61 | $`44.045^\circ`$ |               twin |
|          8 |         71 |          73 | $`44.204^\circ`$ |               twin |
| $`\vdots`$ | $`\vdots`$ |  $`\vdots`$ |       $`\vdots`$ |         $`\vdots`$ |

</div>

## The $`2P`$-beats lemma

The key elementary observation governing the record structure is the following comparison rule.

<div id="lem:2P" class="lemma">

**Lemma 14** ($`2P`$-beats). *Let $`(p, p+g)`$ and $`(q, q+h)`$ be prime pairs with $`g, h \ge 2`$. Then
``` math
\rho(p, p+g) \;>\; \rho(q, q+h)
\quad\Longleftrightarrow\quad
h\, p \;>\; g\, q.
```
In particular, a gap-$`g`$ pair at $`p`$ beats a twin pair $`(q, q+2)`$ in angle if and only if $`p > (g/2)\, q`$; the binding case (smallest $`g`$ larger than $`2`$) is $`g = 4`$, requiring $`p > 2q`$.*

</div>

<div class="proof">

*Proof.* $`\rho(p, p+g) > \rho(q, q+h)`$ $`\iff p(q+h) > q(p+g)`$ $`\iff hp > gq`$. ◻

</div>

<div id="cor:angle-record-preview" class="corollary">

**Corollary 15** (Preview of the angle-record theorem). *Let $`(T_k)_{k\ge 1}`$ be the twin-prime subsequence (smaller members). Suppose that for every $`k`$ with $`T_k \ge 11`$, $`T_{k+1} < 2 T_k`$. Then every angle-record with leading prime $`p_n \ge 3`$ is a twin prime.*

</div>

<div class="proof">

*Proof sketch.* If a non-twin pair $`(p, p+g)`$ with $`g \ge 4`$ were to set a record after the twin $`T_k`$ and before $`T_{k+1}`$, Lemma <a href="#lem:2P" data-reference-type="ref" data-reference="lem:2P">14</a> would require $`p > (g/2) T_k \ge 2 T_k`$. But $`p \le T_{k+1} < 2 T_k`$ by hypothesis; contradiction. ◻

</div>

The converse direction and the full equivalence with the dyadic density inequality $`\pi_2(2x) - \pi_2(x) \ge 1`$ are developed in PG II.

# Geometric Interpretation of Dyadic Density

The $`2P`$-beats lemma reveals a direct equivalence between angle dynamics and dyadic density. Corollary <a href="#cor:angle-record-preview" data-reference-type="ref" data-reference="cor:angle-record-preview">15</a> asserts that the factor-$`2`$ bound on twin-prime ratios $`T_{k+1} < 2 T_k`$ is exactly what guarantees twins dominate the angle-record sequence. Conversely, if the angle-record sequence omits a twin prime (i.e., some non-twin pair sets a record), then some ratio $`T_{k+1}/T_k \ge 2`$ must occur.

## Bertrand factors, revisited geometrically

The dyadic factor $`2`$ is, in classical terms, Bertrand’s factor: every integer $`n > 1`$ has a prime in $`(n, 2n]`$. For twin primes, the analogous dyadic statement
``` math
\pi_2(2x) - \pi_2(x) \;\ge\; 1 \qquad (x \ge 11),
```
which we formalize as the Twin-Prime Bertrand Postulate $`(\mathrm{TPB})`$ in PG II, is exactly the ratio condition $`T_{k+1} < 2 T_k`$ for $`T_k \ge 11`$ via a direct one-line argument.

Geometrically, Lemma <a href="#lem:2P" data-reference-type="ref" data-reference="lem:2P">14</a> explains the recurrence of the factor $`2`$: for a gap-$`g`$ constellation $`\mathcal{C} = \{0, g\}`$ and its *doubled companion* $`\mathcal{C}' = \{0, 2g\}`$, a $`\mathcal{C}'`$-pair at $`P`$ beats a $`\mathcal{C}`$-pair at $`Q`$ in angle if and only if $`P > 2Q`$ — independent of $`g`$. The dyadic factor $`2`$ is therefore also the universal angle-beats factor between doubled constellations, providing a geometric rationale for the uniform Bertrand factor that appears in PG III’s Generalized Bertrand Principle.

## A summary of the geometric–arithmetic correspondence

We can summarize the correspondence in one line:

<div class="center">

*Angle-records dominated by a gap-$`g`$ constellation  $`\iff`$  dyadic density $`\pi_{\mathcal{C}}(2x) - \pi_{\mathcal{C}}(x) \ge 1`$ holds for all $`x`$ past a threshold.*

</div>

For $`g = 2`$ (twins), the dominance is empirically total once we exclude the initial non-twin $`(2,3)`$; the equivalent dyadic inequality is $`(\mathrm{TPB})`$. For larger $`g`$ the statement is modified by the role of smaller-gap competitors (twins beat cousins at angle almost everywhere), but the *within-constellation* dyadic inequality
``` math
\pi_{\mathcal{C}}(2x) - \pi_{\mathcal{C}}(x) \;\ge\; 1
```
persists with the same Bertrand factor of $`2`$. The full picture is developed in PG III as the Generalized Bertrand Principle.

# The Ramanujan-Prime Context

Bertrand’s postulate $`\pi(2x) - \pi(x) \ge 1`$ for $`x \ge 1`$, proved by Chebyshev in 1852, is the $`n = 1`$ case of a broader family. Ramanujan  proved in 1919 that for every integer $`n \ge 1`$, the inequality $`\pi(x) - \pi(x/2) \ge n`$ holds for all sufficiently large $`x`$; the $`n`$-th *Ramanujan prime* is defined as
``` math
\begin{equation}
\
R_n \;=\; \min\Big\{\,R\,:\,\pi(x) - \pi(x/2) \ge n\ \text{for all}\ x \ge R\,\Big\},
\end{equation}
```
so $`R_1 = 2`$. The first several values are $`R_n = 2, 11, 17, 29,
41, 59, 67, 71, \ldots`$ (OEIS `A104272` ). Sondow  established the asymptotic $`R_n \sim p_{2n}`$ and initiated the modern study of this sequence; later work  introduced $`c`$-Ramanujan primes (for interval ratios other than $`1/2`$) and derived Ramanujan-prime iterations.

The Prime Triangle framework makes two direct analogs transparent:

- *Twin-Ramanujan primes.* Replacing $`\pi`$ by $`\pi_2`$ in <a href="#eq:Rn-classical" data-reference-type="eqref" data-reference="eq:Rn-classical">[eq:Rn-classical]</a> gives the sequence
  ``` math
  R^{\mathrm{twin}}_n \;=\; \min\Big\{\,R\,:\,\pi_2(x) - \pi_2(x/2) \ge n\ \text{for all}\ x \ge R\,\Big\}.
  ```
  Here $`R^{\mathrm{twin}}_1`$ is exactly the Twin-Prime Bertrand threshold $`(\mathrm{TPB})`$, equal to $`11`$. Higher values $`R^{\mathrm{twin}}_n`$ quantify the higher-order dyadic density of twin primes.

- *Constellation-Ramanujan primes.* For each admissible $`\mathcal{C} = \{0, g\}`$ the sequence
  ``` math
  R^{\mathcal{C}}_n \;=\; \min\Big\{\,R\,:\,\pi_{\mathcal{C}}(x) - \pi_{\mathcal{C}}(x/2) \ge n\ \text{for all}\ x \ge R\,\Big\}
  ```
  is the natural extension; the cases $`g = 4, 6`$ give $`R^{\{0,4\}}_1 = 7`$ and $`R^{\{0,6\}}_1 = 5`$.

Each of these sequences is empirically a subsequence of its defining constellation (every $`R^{\mathrm{twin}}_n`$ is a twin prime, every $`R^{\mathcal{C}}_n`$ is a member of $`\mathcal{C}`$), because the relevant counting function jumps upward only at constellation members. PG II develops $`R^{\mathrm{twin}}_n`$ explicitly and PG III generalizes to other $`\mathcal{C}`$; the present paper provides the geometric setting in which these are natural.

# Conclusion

The Prime Triangle construction is elementary. Its value is in how it organizes. The angle $`\alpha_n`$ is monotone-equivalent to the ratio $`\rho_n = p_n / p_{n+1}`$, both of which record the geometric shape of consecutive primes. The triangle’s hypotenuse difference $`C_2 - C_1`$ yields an exact identity with the skip-one square difference $`p_{n+2}^{\,2} - p_n^{\,2}`$, producing the integer-valued $`\mathrm{PSD}_n`$ factor. First-order expansions give an energy $`E_n`$, curvature $`K_n`$, normalized shape curvature $`\chi_n`$, and angle drift $`\Delta\alpha_n`$ that form a derivative hierarchy.

These objects are the geometric setting for the main conjectural content of the PG series:

- The sequence of angle-records selects, via the $`2P`$-beats lemma, a subfamily of consecutive-prime pairs that is equivalent (up to the trivial $`(2, 3)`$) to the twin primes. This equivalence is the Angle-Record Theorem of PG II.

- The equivalence extends via the same $`2P`$-beats threshold to a dyadic density statement: at least one twin prime in every $`(x, 2x]`$ with $`x`$ past an effective threshold. This is the Twin-Prime Bertrand Postulate of PG II, with threshold $`R^{\mathrm{twin}}_1 = 11`$.

- Generalization to admissible pair-constellations yields the Generalized Bertrand Principle of PG III, and a corresponding family of constellation-Ramanujan primes $`R^{\mathcal{C}}_n`$ that extends the Ramanujan-prime framework beyond ordinary primes for the first time.

The Prime Triangle is thus a small object with a long reach: from an elementary algebraic identity through an elementary geometric comparison lemma to an explicit, unproven, well-posed conjectural statement on prime-constellation density. The arithmetic consequences are developed in the companion papers.

# Acknowledgements

This paper is the first in a three-part series. PG II introduces the Twin-Prime Bertrand Postulate and proves the Angle-Record Theorem. PG III generalizes to admissible pair-constellations and establishes the Generalized Bertrand Principle, including the twin- and constellation-Ramanujan prime sequences.

<div class="thebibliography">

99

S. Ramanujan. *A proof of Bertrand’s postulate*. J. Indian Math. Soc. **11** (1919), 181–182.

J. Sondow. *Ramanujan primes and Bertrand’s postulate*. Amer. Math. Monthly **116** (2009), 630–635. arXiv:[0907.5232](https://arxiv.org/abs/0907.5232).

N. Amersi, O. Beckwith, S. J. Miller, R. Ronan, J. Sondow. *Generalized Ramanujan primes*. In: *Combinatorial and Additive Number Theory — CANT 2011 and 2012*, Springer Proc. Math. Stat. **101** (2014), 1–13.

M. B. Paksoy. *Derived Ramanujan primes: $`R'_n`$*. arXiv:[1210.6991](https://arxiv.org/abs/1210.6991) (2012).

OEIS Foundation Inc. *Entry A104272: Ramanujan primes*. Online at <https://oeis.org/A104272>.

</div>
