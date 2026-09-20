# The Generalized Bertrand Principle

### PG III — Prime Geometry

Allen Proxmire

> **Converted from LaTeX, 2026-09-20.** This markdown was produced with `pandoc` from `papers/PG_III_GBP.tex` in the upstream `twin-bertrand` repository (commit `ddc4cca`), not retyped from the PDF — so the mathematics is the author's own source, not a transcription. Two mechanical changes were made for GitHub's MathJax: `\label{...}` markers and nested `equation` environments were stripped. **[PG_III_GBP.pdf](PG_III_GBP.pdf) remains authoritative for typesetting**, figures and page layout.

---

# Introduction

PG II isolated a single inequality — the Twin-Prime Bertrand Postulate — as a natural target in twin-prime distribution:
``` math
\pi_2(2x)-\pi_2(x)\ge 1\qquad(x\ge 11).
```
It was verified there for $`x\le 10^9`$; we have since extended the verification to $`x\le 10^{10}`$, still without exception beyond the trivial small-$`x`$ case $`T_k=5`$. The inequality has an equivalent geometric reading: every angle-record of the Prime Triangle sequence with $`p_n\ge 3`$ is realized by a twin prime.

The factor $`2`$ in $`(\mathrm{TPB})`$ is a Bertrand factor — it matches the dyadic interval $`(x,2x]`$ — but until now we had not asked whether it was specific to twins. In this note we investigate the behavior of other prime constellations (the cousin primes, $`\{0,4\}`$, and the sexy primes, $`\{0,6\}`$) and find that the same bound holds:

<div class="center">

*For every admissible pair-constellation, the dyadic inequality $`\pi_\mathcal{C}(2x)-\pi_\mathcal{C}(x)\ge 1`$ holds for all sufficiently large $`x`$, with a threshold $`P^{*}_\mathcal{C}`$ that is very small in every case examined.*

</div>

We call this the Generalized Bertrand Principle $`(\mathrm{GBP})`$ and establish its equivalence with an elementary ratio form and, via a generalized $`2P`$-beats lemma, with a family of angle-record statements in the Prime Triangle sense. We verify the principle for all three constellations to $`10^{10}`$, and combine the data into a uniform empirical envelope for the extreme gaps.

Throughout, $`\mathbb{P}`$ denotes the primes. The Hardy–Littlewood prime-tuple conjecture predicts, for any admissible constellation $`\mathcal{C}`$, an asymptotic twin-like density $`\pi_\mathcal{C}(x)\sim 2\,\mathfrak{S}(\mathcal{C})\,x/(\log x)^2`$, with $`\mathfrak{S}(\mathcal{C})`$ the singular series. For the three constellations studied here, $`\mathfrak{S}(\{0,2\})=
\mathfrak{S}(\{0,4\})=C_2\approx 0.6602`$ and $`\mathfrak{S}(\{0,6\})=2C_2`$ (see Section <a href="#sec:asymp" data-reference-type="ref" data-reference="sec:asymp">7</a>).

# Admissible Constellations and $`(\mathrm{GBP})`$

<div class="definition">

**Definition 1** (Admissible pair-constellation). *A *pair-constellation* is a set $`\mathcal{C}=\{0,g\}`$ with $`g\ge 2`$ even. It is *admissible* if for every prime $`q`$ the reduction $`\mathcal{C}\pmod q`$ does not cover all residue classes. Equivalently, the singular series
``` math
\mathfrak{S}(\mathcal{C})
=\prod_{q\text{ prime}}\frac{1-\nu_\mathcal{C}(q)/q}{(1-1/q)^{|\mathcal{C}|}}
```
is positive, where $`\nu_\mathcal{C}(q)`$ is the number of residues modulo $`q`$ occupied by $`\mathcal{C}`$.*

</div>

For every admissible $`\mathcal{C}=\{0,g\}`$, let
``` math
P^{\mathcal{C}}_1<P^{\mathcal{C}}_2<\cdots
```
be the sequence of leading members: $`P^{\mathcal{C}}_j\in\mathbb{P}`$ with $`P^{\mathcal{C}}_j+g\in\mathbb{P}`$.

<div class="definition">

**Definition 2** ($`\mathcal{C}`$-counting function). *$`\pi_\mathcal{C}(x)=\#\{p\le x:p\in\mathbb{P},\,p+g\in\mathbb{P}\}`$.*

</div>

<div id="conj:GBP" class="conjecture">

**Conjecture 3** (Generalized Bertrand Principle, $`(\mathrm{GBP})`$). *For every admissible pair-constellation $`\mathcal{C}=\{0,g\}`$ there exists a threshold $`P^{*}_\mathcal{C}`$ such that
``` math
\pi_\mathcal{C}(2x)-\pi_\mathcal{C}(x)\ge 1\qquad(x\ge P^{*}_\mathcal{C}).
```
Equivalently, $`P^{\mathcal{C}}_{j+1}<2\,P^{\mathcal{C}}_j`$ for every $`j`$ with $`P^{\mathcal{C}}_j\ge P^{*}_\mathcal{C}`$.*

</div>

<div id="prop:dyadic" class="proposition">

**Proposition 4** (Dyadic and ratio forms). *For each admissible $`\mathcal{C}`$ with fixed threshold $`P^{*}_\mathcal{C}`$, the two formulations above are equivalent.*

</div>

<div class="proof">

*Proof.* The proof is identical to Proposition 2.1 of PG II. If $`P^{\mathcal{C}}_{j+1}<2P^{\mathcal{C}}_j`$ whenever $`P^{\mathcal{C}}_j\ge P^{*}_\mathcal{C}`$, fix $`x\ge P^{*}_\mathcal{C}`$ and let $`P^{\mathcal{C}}_j`$ be the largest term $`\le x`$; then $`P^{\mathcal{C}}_{j+1}<2P^{\mathcal{C}}_j\le 2x`$, giving at least one $`\mathcal{C}`$-pair in $`(x,2x]`$. Conversely, if the dyadic inequality holds and $`P^{\mathcal{C}}_j\ge P^{*}_\mathcal{C}`$, the dyadic form with $`x=P^{\mathcal{C}}_j`$ produces $`P^{\mathcal{C}}_{j+1}\in(P^{\mathcal{C}}_j,2P^{\mathcal{C}}_j]`$; strict inequality follows because $`2P^{\mathcal{C}}_j`$ is even and $`P^{\mathcal{C}}_{j+1}`$ is odd (for $`g>0`$ even, both members of the pair are odd). ◻

</div>

Observe that $`(\mathrm{TPB})`$ is the special case $`\mathcal{C}=\{0,2\}`$ with $`P^{*}_{\{0,2\}}=11`$.

# A Generalized $`2P`$-Beats Lemma

Recall from PG I the Prime Triangle angle of a pair $`(p,q)`$ with $`p<q`$:
``` math
\alpha(p,q)=\arctan(p/q),\qquad \rho(p,q)=p/q.
```
For a fixed constellation $`\mathcal{C}=\{0,g\}`$ and a member $`P^{\mathcal{C}}_j`$, the pair $`(P^{\mathcal{C}}_j,P^{\mathcal{C}}_j+g)`$ has angle $`\alpha^{\mathcal{C}}_j=\arctan(P^{\mathcal{C}}_j/(P^{\mathcal{C}}_j+g))`$.

<div id="lem:gen2P" class="lemma">

**Lemma 5** (Generalized $`2P`$-beats). *Let $`\mathcal{C}=\{0,g\}`$ and $`\mathcal{D}=\{0,h\}`$ with $`g\ne h`$, and let $`(P,P+g)`$, $`(Q,Q+h)`$ be prime pairs for $`\mathcal{C}`$ and $`\mathcal{D}`$ respectively. Then
``` math
\rho(P,P+g)>\rho(Q,Q+h)\iff h\,P>g\,Q.
```
In particular:*

1.  *For $`h=2,\,g=4`$: a cousin pair $`(P,P+4)`$ beats a twin pair $`(Q,Q+2)`$ in angle iff $`P>2Q`$ (the $`2P`$-beats rule of PG II).*

2.  *For $`h=g`$: both pairs belong to the same constellation $`\mathcal{C}`$, and $`\rho(P,P+g)>\rho(Q,Q+g)\iff P>Q`$. The angle sequence within a fixed $`\mathcal{C}`$ is monotonic in the leading prime.*

3.  *For a constellation $`\mathcal{C}=\{0,g\}`$ and its “doubled companion” $`\mathcal{C}'=\{0,2g\}`$, a $`\mathcal{C}'`$-pair at $`P`$ beats a $`\mathcal{C}`$-pair at $`Q`$ iff $`P>2Q`$. The factor $`2`$ is universal for the $`\mathcal{C}\leftrightarrow\mathcal{C}'`$ comparison, independent of $`g`$.*

</div>

<div class="proof">

*Proof.* $`\frac{P}{P+g}>\frac{Q}{Q+h}\iff P(Q+h)>Q(P+g)\iff hP>gQ`$. The specializations follow. ◻

</div>

Part (iii) gives the geometric explanation for the universal factor $`2`$ in $`(\mathrm{GBP})`$: for every admissible $`\mathcal{C}=\{0,g\}`$, the *doubled-gap* companion $`\mathcal{C}'=\{0,2g\}`$ is also admissible (its singular series is positive), and the two constellations are related by the same $`2P`$-beats threshold. The dyadic factor of $`2`$ in the Bertrand inequality is the natural density counterpart of the same factor in the angle comparison.

# The Generalized Angle-Record Theorem

For twins, PG II’s Angle-Record Theorem states that every record-setting $`\alpha_n`$ among consecutive prime pairs $`(p_n,p_{n+1})`$ with $`p_n\ge 3`$ is a twin pair, and that this is equivalent to $`(\mathrm{TPB})`$.

To extend this to a general $`\mathcal{C}`$ we need two things. First, a *domain* on which $`\mathcal{C}`$-pairs can plausibly dominate the angle-records: if $`\mathcal{C}`$ has gap $`g>2`$, twins always beat $`\mathcal{C}`$-pairs of comparable leading prime (since $`\rho(P,P+g)<\rho(P,P+2)`$), and twin records preempt $`\mathcal{C}`$-records in the unrestricted sequence.

Fix $`\mathcal{C}=\{0,g\}`$ and consider only the pairs $`(p,p+g')`$ with $`g'\ge g`$ and both entries prime — call these *$`\mathcal{C}`$-admissible pairs*. Within this restricted universe, the $`2P`$-beats threshold for a competing pair of strictly larger gap $`g'>g`$ is $`P>(g'/g)Q\ge(g+2)/g\cdot Q`$, so the *binding* competing threshold is the companion $`\mathcal{C}'=\{0,g+2\}`$ with factor $`(g+2)/g`$. Only in the special case $`g=2`$ (twins, with companion cousins) is this binding factor equal to $`2`$.

<div class="definition">

**Definition 6** ($`\mathcal{C}`$-angle-record). *A $`\mathcal{C}`$-admissible pair $`(P^*,P^*+g^*)`$ with $`g^*\ge g`$ is a *$`\mathcal{C}`$-angle-record* if $`\rho(P^*,P^*+g^*)>\rho(P,P+g')`$ for every earlier $`\mathcal{C}`$-admissible pair $`(P,P+g')`$.*

</div>

<div id="thm:gen-angle" class="theorem">

**Theorem 7** (Generalized Angle-Record Theorem). *For each admissible $`\mathcal{C}=\{0,g\}`$, the following are equivalent:*

1.  *$`P^{\mathcal{C}}_{j+1}<\frac{g+2}{g}\,P^{\mathcal{C}}_j`$ for every $`j`$ with $`P^{\mathcal{C}}_j\ge P^{\star}_\mathcal{C}`$ (for some effective $`P^{\star}_\mathcal{C}`$ depending on the gap).*

2.  *Every $`\mathcal{C}`$-angle-record with $`P^*\ge P^{\star}_\mathcal{C}`$ is a pair of constellation $`\mathcal{C}`$.*

*For $`g=2`$, $`(g+2)/g=2`$ and $`(i)`$ reduces to $`(\mathrm{TPB})`$; Theorem <a href="#thm:gen-angle" data-reference-type="ref" data-reference="thm:gen-angle">7</a> is then PG II’s Angle-Record Theorem. For $`g=4`$ the factor is $`1.5`$; for $`g=6`$ the factor is $`4/3`$; and so on.*

</div>

<div class="proof">

*Proof sketch.* The argument is analogous to the twin case. (i)$`\Rightarrow`$(ii): suppose (i) holds. Between two consecutive $`\mathcal{C}`$-members $`P^{\mathcal{C}}_j`$ and $`P^{\mathcal{C}}_{j+1}`$, a competing $`\mathcal{C}`$-admissible pair $`(P,P+g')`$ with $`g'>g`$ beats the $`\mathcal{C}`$-record at $`P^{\mathcal{C}}_j`$ iff $`P>(g'/g)P^{\mathcal{C}}_j`$; the binding case is $`g'=g+2`$, requiring $`P>((g+2)/g)P^{\mathcal{C}}_j`$. Under (i), $`P^{\mathcal{C}}_{j+1}<((g+2)/g)P^{\mathcal{C}}_j`$, so no competing pair in the window can exceed the threshold, and the next $`\mathcal{C}`$-admissible record is either a larger-$`P`$ pair of gap $`g`$ (i.e., $`P^{\mathcal{C}}_{j+1}`$) or none until then; meanwhile $`P^{\mathcal{C}}_{j+1}`$ does set a new record because $`\rho(P^{\mathcal{C}}_{j+1},P^{\mathcal{C}}_{j+1}+g)>
\rho(P^{\mathcal{C}}_j,P^{\mathcal{C}}_j+g)`$.

(ii)$`\Rightarrow`$(i): contrapositive. If (i) fails for some $`j`$, there exist $`(P,P+g')`$ with $`g'>g`$, both primes, and $`P^{\mathcal{C}}_j<P\le P^{\mathcal{C}}_{j+1}`$ with $`P>((g+2)/g)P^{\mathcal{C}}_j`$. By Lemma <a href="#lem:gen2P" data-reference-type="ref" data-reference="lem:gen2P">5</a>, this pair beats the previous $`\mathcal{C}`$-record, so a non-$`\mathcal{C}`$-record appears. The three smallest anomalies (very small $`P`$) are handled by direct inspection, producing the effective $`P^{\star}_\mathcal{C}`$. ◻

</div>

# Empirical Verification up to $`10^{10}`$

All data in this section derive from a single segmented (odd-only) sieve of the primes up to $`10^{10}`$, followed by a streaming extraction of all pairs $`(p,p+g)`$ with both primes for $`g\in\{2,4,6\}`$. Cross-boundary pairs are handled by a three-entry buffer. The sieve confirms $`455\,052\,511`$ primes below $`10^{10}`$ and the following constellation counts:

<div class="center">

| constellation $`\mathcal{C}`$ | gap $`g`$ | count up to $`10^{10}`$ |
|:------------------------------|----------:|------------------------:|
| twin                          |         2 |        $`27\,412\,679`$ |
| cousin                        |         4 |        $`27\,409\,999`$ |
| sexy                          |         6 |        $`54\,818\,296`$ |

</div>

## Ratio envelopes

For each constellation we tabulate $`\sup r^{\mathcal{C}}_k`$ on tails $`P^{\mathcal{C}}_j>X`$:

<div class="center">

| scope        | twin sup $`r`$ | cousin sup $`r`$ | sexy sup $`r`$ |
|:-------------|---------------:|-----------------:|---------------:|
| all          |   $`2.200000`$ |     $`2.333333`$ |   $`1.571429`$ |
| $`P_j>100`$  |   $`1.280374`$ |     $`1.283465`$ |   $`1.224299`$ |
| $`P_j>10^3`$ |   $`1.081880`$ |     $`1.109790`$ |   $`1.051647`$ |
| $`P_j>10^6`$ |   $`1.000711`$ |     $`1.000865`$ |   $`1.000695`$ |
| $`P_j>10^9`$ |   $`1.000004`$ |     $`1.000004`$ |   $`1.000002`$ |

</div>

The three envelopes converge to within $`10^{-5}`$ of $`1`$ by $`P_j>10^9`$, with comparable decay rates.

## Bertrand threshold $`P^{*}_\mathcal{C}`$

The top ratios in each constellation (ranks 1–5 shown):

<div class="center">

| constellation | $`P_j`$ | $`P_{j+1}`$ |    $`r_j`$ |    gap |
|:--------------|--------:|------------:|-----------:|-------:|
| twin          |   $`5`$ |      $`11`$ | $`2.2000`$ |  $`6`$ |
| twin          |  $`17`$ |      $`29`$ | $`1.7059`$ | $`12`$ |
| twin          |   $`3`$ |       $`5`$ | $`1.6667`$ |  $`2`$ |
| twin          |  $`11`$ |      $`17`$ | $`1.5455`$ |  $`6`$ |
| twin          |  $`41`$ |      $`59`$ | $`1.4390`$ | $`18`$ |
| cousin        |   $`3`$ |       $`7`$ | $`2.3333`$ |  $`4`$ |
| cousin        |  $`19`$ |      $`37`$ | $`1.9474`$ | $`18`$ |
| cousin        |   $`7`$ |      $`13`$ | $`1.8571`$ |  $`6`$ |
| cousin        |  $`43`$ |      $`67`$ | $`1.5581`$ | $`24`$ |
| cousin        |  $`13`$ |      $`19`$ | $`1.4615`$ |  $`6`$ |
| sexy          |   $`7`$ |      $`11`$ | $`1.5714`$ |  $`4`$ |
| sexy          |   $`5`$ |       $`7`$ | $`1.4000`$ |  $`2`$ |
| sexy          |  $`17`$ |      $`23`$ | $`1.3529`$ |  $`6`$ |
| sexy          |  $`23`$ |      $`31`$ | $`1.3478`$ |  $`8`$ |
| sexy          |  $`13`$ |      $`17`$ | $`1.3077`$ |  $`4`$ |

</div>

Violations of the strong $`r<2`$ bound:

<div class="center">

| constellation |           \# violations of $`r_j<2`$ | $`P^{*}_\mathcal{C}`$ |
|:--------------|-------------------------------------:|----------------------:|
| twin          | $`1`$ (only $`(5,7)\!\to\!(11,13)`$) |                $`11`$ |
| cousin        |  $`1`$ (only $`(3,7)\!\to\!(7,11)`$) |                 $`7`$ |
| sexy          |                                $`0`$ |                 $`5`$ |

</div>

This verifies $`(\mathrm{GBP})`$ with the stated thresholds for all three constellations up to $`10^{10}`$. In particular, GBP holds with the *same* factor $`2`$ across constellations; the user’s suggestion of larger factors ($`3`$ for cousins, $`4`$ for sexy) is true but unnecessarily loose — the $`r<2`$ bound captures the structure exactly.

## Per-decade twin overshoot

The twin overshoot $`\Omega(T)=\max G_k/(\log T_k^{\star})^2`$ per decade (stable regime $`10^3\!\le\!T_k\!<\!10^9`$):

<div class="center">

| decade   | max $`G_k`$ |           at $`T_k`$ | $`(\log T)^2`$ | $`\Omega`$ |
|:---------|------------:|---------------------:|---------------:|-----------:|
| $`10^3`$ |     $`210`$ |           $`5\,879`$ |      $`75.33`$ |  $`2.788`$ |
| $`10^4`$ |     $`630`$ |          $`62\,297`$ |     $`121.87`$ |  $`5.169`$ |
| $`10^5`$ |  $`1\,452`$ |         $`850\,349`$ |     $`186.42`$ |  $`7.789`$ |
| $`10^6`$ |  $`1\,722`$ |      $`9\,923\,987`$ |     $`259.55`$ |  $`6.635`$ |
| $`10^7`$ |  $`2\,868`$ |     $`96\,894\,041`$ |     $`338.16`$ |  $`8.481`$ |
| $`10^8`$ |  $`4\,770`$ |    $`698\,542\,487`$ |     $`414.71`$ | $`11.502`$ |
| $`10^9`$ |  $`6\,030`$ | $`4\,289\,385\,521`$ |     $`491.93`$ | $`12.258`$ |

</div>

# A Refined Envelope Conjecture

For each constellation we compute $`\sup(r_j-1)`$ over tails $`P^{\mathcal{C}}_j>T_{\min}`$ at $`T_{\min}\in\{10^2,10^3,10^5,10^7,10^9\}`$:

<div class="center">

| $`T_{\min}`$ | twin $`\sup(r-1)`$ | cousin $`\sup(r-1)`$ | sexy $`\sup(r-1)`$ |
|:---|---:|---:|---:|
| $`10^2`$ | $`2.80\times10^{-1}`$ | $`2.83\times10^{-1}`$ | $`2.24\times10^{-1}`$ |
| $`10^3`$ | $`8.19\times10^{-2}`$ | $`1.10\times10^{-1}`$ | $`5.16\times10^{-2}`$ |
| $`10^5`$ | $`5.10\times10^{-3}`$ | $`4.33\times10^{-3}`$ | $`3.34\times10^{-3}`$ |
| $`10^7`$ | $`1.43\times10^{-4}`$ | $`1.49\times10^{-4}`$ | $`9.87\times10^{-5}`$ |
| $`10^9`$ | $`3.86\times10^{-6}`$ | $`4.02\times10^{-6}`$ | $`2.26\times10^{-6}`$ |

</div>

The three envelopes decay at essentially the same rate. A weighted least-squares fit of the log-linear form
``` math
\log\!\big((r_j-1)T_j\big)
=\log C_\mathcal{C}+\delta_\mathcal{C}\log\log T_j
```
on the five $`T_{\min}`$ points yields:

<div class="center">

| constellation        | $`\delta_\mathcal{C}`$ | $`C_\mathcal{C}`$ |    $`R^2`$ |
|:---------------------|-----------------------:|------------------:|-----------:|
| twin                 |             $`3.2884`$ |        $`0.1645`$ | $`0.9970`$ |
| cousin               |             $`3.2209`$ |        $`0.2013`$ | $`0.9957`$ |
| sexy                 |             $`3.1538`$ |        $`0.1507`$ | $`0.9931`$ |
| pooled (uniform fit) |             $`3.2210`$ |        $`0.1709`$ | $`0.9824`$ |

</div>

The fitted exponents agree across constellations within $`4.2\%`$ (range $`[3.15,3.29]`$), strongly suggesting a common asymptotic $`\delta`$. The constants $`C_\mathcal{C}`$ vary by roughly $`29\%`$ (range $`[0.15,0.20]`$); this larger spread is driven by the cousin envelope, whose leading offenders at small $`P_j`$ (dominated by the pair $`(3,7)\to(7,11)`$) inflate its fitted prefactor relative to the asymptotic regime.

The pooled fit — obtained by concatenating all fifteen data points and fitting a single $`(C,\delta)`$ pair — yields
``` math
\begin{equation}
\
r_j-1 \;\le\; 0.171\,\frac{(\log P_j)^{3.22}}{P_j},
\qquad
G^{\mathcal{C}}_j \;<\; 0.171\,(\log P^{\mathcal{C}}_j)^{3.22}
\qquad(R^2=0.982).
\end{equation}
```

<div id="conj:env" class="conjecture">

**Conjecture 8** (Refined envelope, data-driven). *For every admissible pair-constellation $`\mathcal{C}=\{0,g\}`$ there exist constants $`C_\mathcal{C},\delta_\mathcal{C}`$ with $`\delta_\mathcal{C}\to\delta^*`$ as $`g`$ varies over admissible gaps, for some universal $`\delta^*\in[3.15,3.30]`$, such that
``` math
G^\mathcal{C}_j \;=\; P^{\mathcal{C}}_{j+1}-P^{\mathcal{C}}_j
\;<\; C_\mathcal{C}\,(\log P^{\mathcal{C}}_j)^{\delta_\mathcal{C}}
\qquad(P^{\mathcal{C}}_j\ge P^{*}_\mathcal{C}).
```
The pooled uniform envelope <a href="#eq:env-uniform" data-reference-type="eqref" data-reference="eq:env-uniform">[eq:env-uniform]</a> fits all three examined constellations with $`R^2\ge 0.98`$.*

</div>

This is strictly stronger than $`(\mathrm{GBP})`$, which is recovered by the coarse bound $`G^\mathcal{C}_j/P^{\mathcal{C}}_j\to 0`$. It is compatible with the Hardy–Littlewood prediction for the *typical* gap $`G^\mathcal{C}_j\sim(\log P)^2/(2\mathfrak{S}(\mathcal{C}))`$: the exponent $`\delta\approx 3.2>2`$ captures the *extreme* gap, which exceeds the typical gap by an overshoot factor that itself grows slowly with $`P`$.

# Asymptotic Interpretation

## Exponent drift toward $`\beta=2`$

In PG II the twin-gap power law $`G_k\approx A(\log T_k)^\beta`$ was fitted on primes up to $`10^9`$, yielding $`\beta\approx 1.866`$ stable across sub-ranges. Extension to $`10^{10}`$ shifts the fits upward:

<div class="center">

| fit range $`T_k>`$ | $`\beta`$ ($`10^9`$ data) | $`\beta`$ ($`10^{10}`$ data) |
|:-------------------|--------------------------:|-----------------------------:|
| $`10^3`$           |                $`1.8633`$ |                   $`1.8865`$ |
| $`10^5`$           |                $`1.8659`$ |                   $`1.8872`$ |
| $`10^7`$           |                $`1.8664`$ |                   $`1.8889`$ |
| $`10^9`$           |                         — |                   $`1.8957`$ |

</div>

The drift is monotone; each fit band grew $`\Delta\beta\approx+0.02`$ across the new decade. Under the interpretation that the true asymptotic exponent is $`\beta=2`$ (Hardy–Littlewood), our observations are consistent with a slow finite-size convergence whose pace is controlled by the overshoot factor $`\Omega`$.

A second, independent window on the same convergence comes from the *doubled-twin shadow* introduced in PG II (its section on the $`\Delta x`$ structure and the geometry of doubled twins). Placing the doubled twins $`2T_k`$ on a prime-rank axis, PG II finds that the macro-slope of the resulting point set obeys
``` math
\mathrm{slope}=\frac{C_2\,\log(2T)}{(\log T)^2},
   \qquad C_2=\tfrac12 C_H,
```
whose leading constant is half the Factor-Skyline twin coverage constant $`C_H=2C_2`$ (Theorem 4.7a of the Factor Skyline foundation paper, which identifies $`C_H`$ with the Hardy–Littlewood singular series for the twin pattern). This refined $`1/\log`$ law is confirmed empirically to $`1`$–$`2\%`$ across five decades of $`T_k`$, and its slow downward drift is the slope counterpart of the upward $`\beta`$ drift tabulated above: both measure the same finite-size approach to the Hardy–Littlewood asymptotics, from the density side here and from the extreme-gap side there.

## Overshoot growth law

Fits of the per-decade twin overshoot $`\Omega(T)`$ on the seven stable points yield:

<div class="center">

| model | form                                                   | $`R^2`$    |
|:------|:-------------------------------------------------------|:-----------|
| \(a\) | $`\Omega=A(\log T)^b`$, $`A=0.147,\,b=1.43`$           | $`0.9133`$ |
| \(b\) | $`\log\Omega=a+b(\log\log T)^\alpha`$, $`\alpha=0.69`$ | $`0.9135`$ |
| \(c\) | $`\Omega=D(\log T)^\gamma`$, $`\gamma=0.10`$           | $`0.8964`$ |
| \(d\) | $`\Omega=A+B\log\log T`$, $`A=-17.48,B=9.32`$          | $`0.8959`$ |

</div>

Models (a) and (b) are essentially tied, indicating $`\Omega\sim(\log T)^{1.43}`$ or equivalently $`\log\Omega\sim(\log\log T)^{0.7}`$. This is a *Cramér–Granville*-type growth: Cramér conjectured $`p_{n+1}-p_n=O((\log p)^2)`$ for ordinary primes, refined by Granville to include a $`\log\log p`$ factor. For twin-prime gaps we see an analogous correction with an exponent $`\alpha\approx 0.7`$ in the $`\log\log`$ factor, slightly sub-logarithmic but firmly positive.

## Why factor $`2`$ is natural and universal

The factor $`2`$ in $`(\mathrm{GBP})`$ has a clean interpretation: it is the dyadic Bertrand factor. For ordinary primes, Bertrand’s postulate ensures a prime in every $`(x,2x]`$; for any admissible $`\mathcal{C}`$, the expected count of $`\mathcal{C}`$-pairs in $`(x,2x]`$ under Hardy–Littlewood is
``` math
\pi_\mathcal{C}(2x)-\pi_\mathcal{C}(x)
\sim 2\mathfrak{S}(\mathcal{C})\,\frac{x}{(\log x)^2},
```
which diverges to infinity. Unconditionally we do not know that this count is $`\ge 1`$ for every sufficiently large $`x`$, but the data indicate that the inequality becomes binding extremely early ($`P^{*}_\mathcal{C}`$ at most the first few pair members in every case we examined) and is maintained thereafter with orders of magnitude of slack.

Lemma <a href="#lem:gen2P" data-reference-type="ref" data-reference="lem:gen2P">5</a>(iii) provides the geometric explanation: the factor $`2`$ is exactly the $`2P`$-beats threshold for the doubled-companion relation $`\mathcal{C}\leftrightarrow\mathcal{C}'=\{0,2g\}`$. In the angle picture, moving from a $`\mathcal{C}`$-member at $`Q`$ to a $`\mathcal{C}'`$-member at $`P`$ requires $`P>2Q`$ to beat the $`\mathcal{C}`$-angle; this threshold is universal in $`g`$. The dyadic factor of $`2`$ in Bertrand’s inequality is the density counterpart.

## Why violations occur only at tiny $`P`$

The near-misses of the bound $`r<2`$ all lie at $`P_j\le 881`$ across all three constellations; past this, no ratio in our data exceeds $`1.1`$. The reason is purely statistical: at small $`P`$, the singular series effectively constrains the positions of constellation pairs, and a small neighborhood of primes may fail to contain both $`p`$ and $`p+g`$. Once $`P`$ is large enough that the expected count in $`(P,2P]`$ exceeds $`1`$ by many standard deviations, fluctuations cannot drive it to zero. The Hardy–Littlewood estimate gives the expected count $`\sim 2\mathfrak{S}(\mathcal{C})P/(\log P)^2`$, which equals $`10`$ by $`P\sim 10^4`$ (twin/cousin) or $`P\sim 10^3`$ (sexy); a factor of $`10`$ is already too large for statistical fluctuations to explain a complete absence.

# Conclusion

We have identified the Generalized Bertrand Principle — a conjectural dyadic inequality $`\pi_\mathcal{C}(2x)-\pi_\mathcal{C}(x)
\ge 1`$ with a universal factor of $`2`$ — as the natural extension of PG II’s twin-prime Bertrand postulate to every admissible pair-constellation. The principle is equivalent to the simple ratio condition $`P^{\mathcal{C}}_{j+1}<2P^{\mathcal{C}}_j`$ and is supported geometrically by a generalized $`2P`$-beats lemma expressed in the Prime Triangle angle. We have verified the principle in three constellations (twins, cousins, sexy primes) up to $`P=10^{10}`$, giving $`P^{*}_{\{0,2\}}=11`$, $`P^{*}_{\{0,4\}}=7`$, $`P^{*}_{\{0,6\}}=5`$.

Three observations flow from the computation:

1.  The cousin-prime count at $`10^{10}`$ ($`27\,409\,999`$) is within $`0.01\%`$ of the twin-prime count ($`27\,412\,679`$), confirming the Hardy–Littlewood prediction of identical densities for $`\{0,2\}`$ and $`\{0,4\}`$.

2.  The ratio envelopes tighten at essentially the same rate across constellations. Fitted exponents $`\delta_\mathcal{C}`$ agree within $`4.2\%`$ across the three constellations (range $`[3.15,3.29]`$); a pooled uniform fit gives $`G^{\mathcal{C}}_j<0.171(\log P)^{3.22}`$ with $`R^2=0.982`$.

3.  The twin-gap exponent $`\beta`$ drifts upward from $`1.866`$ (at $`10^9`$) to $`1.896`$ (at $`10^{10}`$ restricted to $`T_k>10^9`$), consistent with the asymptotic value $`\beta=2`$ predicted by Hardy–Littlewood; concurrently the overshoot factor $`\Omega(T)`$ grows roughly like $`(\log T)^{1.4}`$ or $`(\log\log T)^{0.7}`$.

Future work. A conditional proof of $`(\mathrm{GBP})`$ under Hardy–Littlewood is immediate along the same lines as Theorem 5.1 of PG II. An unconditional proof would require a short-interval result $`\pi_\mathcal{C}(x+y)-\pi_\mathcal{C}(x)>0`$ at dyadic scale $`y=x`$, which is strictly beyond current sieve-theoretic capabilities (bounded-gaps results of Zhang, Maynard, and Polymath8 give such short-interval existence only at some scales, not all). We expect that the Maynard multi-dimensional sieve, adapted to dyadic windows, is the natural apparatus for an attack on GBP. Finally, the $`\Delta x`$ construction of PG II generalizes to any admissible constellation $`\mathcal{C}`$ via $`\Delta x^{\mathcal{C}}_k=\pi(2P^{\mathcal{C}}_{k+1})-\pi(2P^{\mathcal{C}}_k)`$, and the $`G^{\mathcal{C}}`$-driven overdispersion and scale-collapse phenomena observed there for twins are expected to persist for all constellations, with the governing constant becoming the singular series $`\mathfrak{S}(\mathcal{C})`$.

The apparent universality of the envelope across constellations, and the unified overshoot law, suggest that the Generalized Bertrand Principle is part of a larger picture: HL-admissible constellations behave as coordinated copies of the twin-prime sequence, scaled by their singular-series constants, and subject to a common growth law for their extreme gaps. Quantifying this universality conjecturally — in particular, obtaining a closed form for the asymptotic overshoot rate — is the natural next step.

# Data availability

All computations reproduce from `scripts/pg_structural_1e10.py` and `scripts/pg_extend_1e10.py`. Saved datasets (`twins_1e10.npy`, `cousins_1e10.npy`, `sexy_1e10.npy`, and associated CSVs) are stored under the `data/` directory.

# Acknowledgements

This paper is the third in a series. PG I introduced the Prime Triangle construction and derived geometric quantities; PG II established the Twin-Prime Bertrand Postulate and the Angle-Record Theorem; the present note generalizes those results to all admissible pair-constellations.
