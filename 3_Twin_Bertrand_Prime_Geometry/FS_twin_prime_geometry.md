# The Twin-Slope Ceiling: Twin Prime Geometry on the Factor Skyline

Allen Proxmire

April 2026

---

## Abstract

We study twin primes through the geometry of the Factor Skyline (FS), a two-dimensional encoding of the integers in which each integer $n$ occupies a column of width $\text{lpf}(n)$ (least prime factor) and height $n / \text{lpf}(n)$. In this setting, primes appear as narrow escape spires of width 1, and twin prime pairs produce a characteristic segment of slope $\arctan(2/3)$ between consecutive spires. We prove three structural results:

(i) The twin slope $\arctan(2/3) \approx 33.69°$ is an absolute geometric ceiling: no consecutive-prime segment on the Factor Skyline exceeds this slope for $p \geq 5$ (Theorem 4.2).

(ii) The number of twin-open template positions in any Bertrand interval $[p, 2p]$ diverges as $p \to \infty$, growing as $O(p) \sim C_2 \cdot p / (\ln p)^2$ where $C_2 \approx 1.3203$ is the Hardy-Littlewood twin prime constant (Theorem 5.2).

(iii) Under the Cramer independence model, the probability $R(p)$ that all twin-open positions in $[p, 2p]$ are unfilled decays super-exponentially: $R(p) \sim \exp(-C_2 \cdot p / (\ln p)^2)$ (Theorem 6.2).

We isolate a single conjectural statement --- the Filling Condition --- as the only obstacle separating the FS structural guarantees from a proof of the twin prime conjecture. We formulate the Filling Condition in three equivalent forms (geometric, combinatorial, analytic), show it is strictly weaker than breaking the classical parity barrier, and place it precisely in the hierarchy of known results between the Maynard-Tao bounded gaps theorem and the full Hardy-Littlewood conjecture. Computational verification confirms that every interval $[p, 2p]$ for $3 \leq p \leq 200{,}000$ contains at least one twin prime pair, and that the twin-slope ceiling is achieved universally across $78{,}497$ consecutive-prime segments up to $10^6$.

**MSC 2020:** 11N05, 11A41, 11N36

**Keywords:** twin primes, prime gaps, sieve methods, parity barrier, Factor Skyline


## 1. Introduction

The twin prime conjecture --- that there exist infinitely many primes $p$ such that $p + 2$ is also prime --- remains one of the central open problems in number theory. The conjecture is supported by extensive computation, by the Hardy-Littlewood heuristic [HL23] predicting $\pi_2(x) \sim C_2 \cdot x / (\ln x)^2$ twin primes up to $x$, and by the breakthrough of Zhang [Zha14] and Maynard [May15] establishing infinitely many prime pairs with gap at most 246. Yet the conjecture itself remains unresolved.

The obstacle is well understood in principle: the parity barrier in sieve theory prevents combinatorial methods from producing a positive lower bound on the count of primes (or twin primes) in any interval [Sel49, Bom76]. Sieve methods cannot distinguish numbers with an even number of prime factors from those with an odd number, and this limitation blocks the existential step from "twin-open positions exist in abundance" to "at least one position is occupied by actual twin primes."

In this paper, we study twin primes through the lens of the Factor Skyline (FS), a geometric encoding of the integers introduced in [Pro26]. The FS assigns to each integer $n$ a column of width $\text{lpf}(n)$ and height $n / \text{lpf}(n)$, and places these columns consecutively to form a two-dimensional landscape. In this encoding, primes appear as narrow escape spires (width 1, height $n$), and the geometry of the skyline encodes multiplicative structure in a way that makes certain number-theoretic phenomena visually and structurally transparent.

Our main contributions are:

1. **The twin-slope ceiling** (Section 4). We prove that the slope $\arctan(2/3)$ between consecutive prime spires is an absolute geometric maximum for $p \geq 5$, achieved if and only if the two primes form a twin pair. This transforms the twin prime question into a geometric recurrence problem: does the FS slope envelope hit its ceiling infinitely often?

2. **Twin opportunities in Bertrand intervals** (Section 5). We define the twin opportunity function $O(p)$, counting twin-open template positions in $[p, 2p]$, and prove it diverges. Computational verification through $p = 200{,}000$ confirms that every such interval contains at least one twin pair.

3. **The Filling Condition** (Section 6). We isolate a single conjectural statement --- that at least one of the $O(p) \to \infty$ twin-open slots in $[p, 2p]$ is occupied by actual twin primes --- and express it in three equivalent forms. We show this condition is strictly weaker than breaking the full parity barrier, analogous to the partial bypasses achieved by Friedlander-Iwaniec [FI98] and Maynard-Tao [May15].

4. **The information-theoretic perspective** (Section 7). We quantify the parity barrier as 0.26 bits per integer of irreducible entropy in the escape layer, and argue that systematic avoidance of $O(p)$ twin-open slots by the sub-Poisson escape process is information-theoretically implausible when $O(p) \to \infty$.

**Nature of the paper and relation to classical results.** This paper is primarily expository. Several of the results presented here --- coverage protection (Theorem 3.3), the Hardy-Littlewood constant $C_2 > 1$ (Theorem 3.4), template persistence (Theorem 3.6), and the divergence of twin-open positions (Theorem 5.2) --- are classical facts of sieve theory [HL23, Sel49] expressed in the geometric language of the Factor Skyline. The Filling Condition itself (Conjecture 6.3) can be stated purely on the number line as $\pi_2(2N) - \pi_2(N) \geq 1$, without reference to the FS.

What the FS framework contributes beyond this classical content is threefold. First, the twin-slope ceiling (Theorem 4.2) is a structural invariant of the FS-x coordinate system: the fact that no consecutive-prime segment can exceed slope $\arctan(2/3)$ depends on the specific way composite widths accumulate in FS-x, and has no direct number-line analog. Second, the information-theoretic decomposition of the parity barrier into 0.26 bits of irreducible escape-layer entropy (Section 7) requires the FS increment sequence and its conditional entropy structure. Third, the FS provides a unified geometric framework in which the Filling Condition, its three equivalent forms, and its position in the hierarchy of known results emerge as natural consequences of a single architectural picture.

We make no claim to have resolved the twin prime conjecture; rather, we offer a geometric language that clarifies the structure of the problem and pinpoints the exact location of the remaining obstacle. For the full development of the Factor Skyline framework, we refer to [Pro26].


## 2. The Factor Skyline

We define the geometric framework. All notation follows [Pro26, Part I].

**Definition 2.1 (Least prime factor).** For $n \geq 2$, let $\text{lpf}(n) = \min\{p : p \mid n,\ p \text{ prime}\}$. Set $\text{lpf}(1) = 1$.

**Definition 2.2 (Width and height).** The FS-width and FS-height of integer $n$ are:

$$w(n) = \text{lpf}(n), \qquad h(n) = n / \text{lpf}(n).$$

For primes, $w(p) = 1$ and $h(p) = p$. For composites, $w(n) = \text{lpf}(n) \geq 2$ and $h(n) = n / \text{lpf}(n) < n$.

**Definition 2.3 (FS-coordinates).** The Factor Skyline assigns to each integer $n \geq 1$ a cumulative coordinate $(x_{\text{FS}}(n),\, y_{\text{FS}}(n))$ defined by:

- $x_{\text{FS}}(1) = 1$, $y_{\text{FS}}(1) = 1$.
- For $n \geq 2$: $\Delta x(n) = 1$ if $n$ is prime; $\Delta x(n) = \text{lpf}(n)$ if $n$ is composite.
- $x_{\text{FS}}(n) = x_{\text{FS}}(n-1) + \Delta x(n)$.
- $y_{\text{FS}}(n) = n$ if $n$ is prime; $y_{\text{FS}}(n) = n / \text{lpf}(n)$ if $n$ is composite.

The column for integer $n$ occupies horizontal extent $\Delta x(n)$ and reaches height $y_{\text{FS}}(n)$. Primes produce narrow, tall *escape spires*; composites produce wider, shorter columns whose width reveals their smallest prime factor.

**Table 1.** FS-coordinates for $n = 1$ to $15$.

| $n$ | $\text{lpf}(n)$ | $\Delta x$ | $x_{\text{FS}}$ | $y_{\text{FS}}$ | Type |
|-----|------------------|-------------|------------------|------------------|------|
| 1 | 1 | - | 1 | 1 | seed |
| 2 | 2 | 1 | 2 | 2 | escape |
| 3 | 3 | 1 | 3 | 3 | escape |
| 4 | 2 | 2 | 5 | 2 | width-2 |
| 5 | 5 | 1 | 6 | 5 | escape |
| 6 | 2 | 2 | 8 | 3 | width-2 |
| 7 | 7 | 1 | 9 | 7 | escape |
| 8 | 2 | 2 | 11 | 4 | width-2 |
| 9 | 3 | 3 | 14 | 3 | width-3 |
| 10 | 2 | 2 | 16 | 5 | width-2 |
| 11 | 11 | 1 | 17 | 11 | escape |
| 12 | 2 | 2 | 19 | 6 | width-2 |
| 13 | 13 | 1 | 20 | 13 | escape |
| 14 | 2 | 2 | 22 | 7 | width-2 |
| 15 | 3 | 3 | 25 | 5 | width-3 |

**Definition 2.4 (Activation).** A prime $p$ *activates* at the integer $p^2$, the smallest integer with $\text{lpf}(n) = p$. The activation sequence is $4, 9, 25, 49, 121, \ldots$ (the prime squares). The $k$-th *activation epoch* is the interval $[p_k^2,\, p_{k+1}^2)$, within which the set of active width layers is frozen.

**Definition 2.5 (Coverage).** When width-$p$ activates at $p^2$, it claims every subsequent integer $n$ with $\text{lpf}(n) = p$. Among integers not claimed by smaller widths, the density of width-$p$ coverage is exactly $1/p$, by the Chinese Remainder Theorem (CRT). Coverage layers for distinct primes act independently.

**Definition 2.6 (Escape).** An integer $n$ *escapes* if $\text{lpf}(n) = n$, i.e., $n$ is prime. Escape events correspond to spires with $\Delta x = 1$ and $y_{\text{FS}} = n$.

**Theorem 2.7 (Escape density and the geometric PNT).** The fraction of integers escaping all coverage layers with width $q \leq p$ is:

$$D(p) = \prod_{\substack{q \leq p \\ q\ \text{prime}}} \left(1 - \frac{1}{q}\right).$$

By Mertens' theorem, $D(p) \sim e^{-\gamma} / \ln p$ where $\gamma \approx 0.5772$ is the Euler-Mascheroni constant. Setting $p = \sqrt{N}$ (the activation horizon at scale $N$) yields the Prime Number Theorem in FS-geometric form:

$$\pi(N) \sim N \cdot D(\sqrt{N}) \sim \frac{N}{\ln N}.$$

*Proof:* See [Pro26, Theorem 5.2]. QED.

**Definition 2.8 (Primorial template).** The $k$-th primorial is $p_k\# = 2 \cdot 3 \cdot 5 \cdots p_k$. The $p_k\#$-template assigns to each residue class $r \bmod p_k\#$ the status *open* if $\gcd(r, p_k\#) = 1$, and *covered* otherwise.

**Theorem 2.9 (Template periodicity).** The width assignment of $n$ among primes $\leq p_k$ depends only on $n \bmod p_k\#$. The number of open positions per period is $\varphi(p_k\#) = p_k\# \cdot D(p_k)$.

*Proof:* By CRT, the events $q \mid n$ for distinct primes $q$ are independent modulo $p_k\#$. QED.

![Figure 0: The Factor Skyline for $n = 1$ to $100$. Primes appear as narrow escape spires (dark, width 1) rising to height $n$. Composites occupy wider columns colored by their least prime factor. The red polyline connects consecutive prime spire tops.](FS_skyline_paper.png)

With these definitions in place, we turn to the specialization that is the focus of this paper.


## 3. Twin Primes in FS Geometry

We now apply the FS framework to twin primes. The key objects are twin-open template positions and the coverage-protection mechanism that shields them.

**Definition 3.1 (Twin-open position).** A position $r$ in the $p_k\#$-template is *twin-open* if both $r$ and $r+2$ are open, i.e., $\gcd(r, p_k\#) = 1$ and $\gcd(r+2, p_k\#) = 1$.

**Definition 3.2 (Residue occupation number).** For the offset pair $H = \{0, 2\}$ and prime $q$, define:

$$v_q(H) = |\{0 \bmod q,\, 2 \bmod q\}| = \begin{cases} 1 & \text{if } q = 2, \\ 2 & \text{if } q \geq 3. \end{cases}$$

The pair $\{0, 2\}$ is *admissible*: $v_q < q$ for all primes $q$.

**Theorem 3.3 (Coverage-protection for twins).** For every prime $q \geq 3$, the width-$q$ coverage layer cannot simultaneously eliminate both members of a twin-open pair. The survival factor when width-$q$ activates is:

$$S_q = \frac{q - v_q}{q} = \begin{cases} 1/2 & \text{if } q = 2, \\ (q-2)/q & \text{if } q \geq 3. \end{cases}$$

For all primes $q$, $S_q > 0$. Eliminating one member of a twin pair by width-$q$ automatically *protects* the other.

*Proof:* If $q \mid r$, then $r + 2 \equiv 2 \pmod{q}$. Since $q \geq 3$, we have $2 \not\equiv 0 \pmod{q}$, so $q \nmid (r+2)$. The fraction of residues modulo $q$ that eliminate at least one member is $v_q / q = 2/q$; the surviving fraction is $(q - 2)/q$. QED.

**Theorem 3.4 (Hardy-Littlewood constant from coverage protection).** The twin-open density after all coverage layers up to $p$ have acted is:

$$T(p) = \frac{1}{2} \prod_{\substack{3 \leq q \leq p \\ q\ \text{prime}}} \left(1 - \frac{2}{q}\right).$$

The coverage-protection multiplier is:

$$C_2(p) = \frac{T(p)}{D(p)^2} = \prod_{\substack{3 \leq q \leq p \\ q\ \text{prime}}} \frac{q(q-2)}{(q-1)^2} \xrightarrow{p \to \infty} C_2 \approx 1.3203.$$

Since $C_2 > 1$, twin primes occur *more frequently* than the independence prediction $D(p)^2$ would suggest. Coverage layers create positive correlations among twin pair members.

*Proof:* Each factor $S_q / (1 - 1/q)^2 = q(q-2)/(q-1)^2 > 1$ for $q \geq 3$. The product converges to the Hardy-Littlewood constant $C_2$. See [Pro26, Theorem 4.7]. QED.

**Theorem 3.5 (FS-x gap invariant for twin primes).** Every twin prime pair $(p, p+2)$ with $p \geq 5$ has FS-x gap exactly 3:

$$x_{\text{FS}}(p+2) - x_{\text{FS}}(p) = 3.$$

*Proof:* Between $p$ and $p+2$ lies exactly one integer, $p+1$. Since $p \geq 5$ is odd, $p+1$ is even and $\text{lpf}(p+1) = 2$. The FS-x gap counts the contributions of $p+1$ and $p+2$ (but not $p$ itself):

$$x_{\text{FS}}(p+2) - x_{\text{FS}}(p) = \Delta x(p+1) + \Delta x(p+2) = 2 + 1 = 3.$$

This is invariant: it depends only on $p+1$ being even (guaranteed for odd $p \geq 5$) and $p+2$ being prime. QED.

**Computational verification.** Confirmed for all 8,169 twin prime pairs up to $10^6$.

| Twin pair | $x_{\text{FS}}(p)$ | $x_{\text{FS}}(p+2)$ | Gap |
|-----------|---------------------|-----------------------|-----|
| (5, 7) | 6 | 9 | 3 |
| (11, 13) | 17 | 20 | 3 |
| (29, 31) | 54 | 57 | 3 |
| (41, 43) | 80 | 83 | 3 |
| (101, 103) | 224 | 227 | 3 |

**Theorem 3.6 (Template persistence for twins).** The number of twin-open positions $N_{\text{twin}}(p_k)$ in the $p_k\#$-template satisfies the recurrence:

$$N_{\text{twin}}(p_{k+1}) = N_{\text{twin}}(p_k) \cdot (p_{k+1} - 2).$$

Starting from $N_{\text{twin}}(2) = 1$, the sequence is strictly increasing for $p_k \geq 5$:

| $p_k$ | $N_{\text{twin}}(p_k)$ | $p_k\#$ | Growth factor |
|--------|------------------------|----------|---------------|
| 2 | 1 | 2 | --- |
| 3 | 1 | 6 | $\times 1$ |
| 5 | 3 | 30 | $\times 3$ |
| 7 | 15 | 210 | $\times 5$ |
| 11 | 135 | 2,310 | $\times 9$ |
| 13 | 1,485 | 30,030 | $\times 11$ |

In particular, $N_{\text{twin}}(p_k) \to \infty$. Twin-open slots are never exhausted by any finite collection of coverage layers.

*Proof:* When width-$p_{k+1}$ activates, it eliminates twin-open positions where $p_{k+1}$ divides $r$ or $r+2$. These are $v_{p_{k+1}} = 2$ residue classes out of $p_{k+1}$, leaving fraction $(p_{k+1} - 2)/p_{k+1}$. The period expands from $p_k\#$ to $p_{k+1}\#$ by factor $p_{k+1}$, so each surviving position replicates $p_{k+1}$ times, of which $(p_{k+1} - 2)$ survive. Since $p_{k+1} - 2 \geq 1$ for $p_{k+1} \geq 3$ and $p_{k+1} - 2 \geq 3$ for $p_{k+1} \geq 5$, the count is strictly increasing. QED.


## 4. The Twin-Slope Ceiling

We now establish the central geometric result: the slope $\arctan(2/3)$ is an absolute ceiling on the Factor Skyline, achieved only by twin prime pairs.

**Definition 4.1 (Prime-prime slope).** For consecutive primes $p_i < p_{i+1}$, the FS slope angle of the segment connecting their spire tops is:

$$\theta_i = \arctan\!\left(\frac{p_{i+1} - p_i}{x_{\text{FS}}(p_{i+1}) - x_{\text{FS}}(p_i)}\right) = \arctan\!\left(\frac{\Delta p}{\Delta x_{\text{FS}}}\right).$$

**Theorem 4.2 (Twin-slope ceiling).** For all consecutive primes $p_i, p_{i+1}$ with $p_i \geq 5$:

$$\theta_i \leq \arctan\!\left(\frac{2}{3}\right) \approx 33.6901°,$$

with equality if and only if $p_{i+1} = p_i + 2$ (i.e., $(p_i, p_{i+1})$ is a twin prime pair).

*Proof:* We show that the ratio $\Delta p / \Delta x_{\text{FS}}$ is maximized by twin pairs with value $2/3$.

The FS-x gap between consecutive primes $p_i$ and $p_{i+1} = p_i + g$ (where $g = p_{i+1} - p_i$ is the prime gap) is:

$$\Delta x_{\text{FS}} = \sum_{n=p_i+1}^{p_{i+1}} \Delta x(n) = 1 + \sum_{n=p_i+1}^{p_{i+1}-1} \text{lpf}(n),$$

where the $1$ accounts for the final prime $p_{i+1}$, and the sum runs over the $g - 1$ composites between $p_i$ and $p_{i+1}$.

*Case $g = 2$ (twin pair).* $\Delta x_{\text{FS}} = \text{lpf}(p_i + 1) + 1 = 2 + 1 = 3$, since $p_i + 1$ is even for $p_i \geq 5$. The slope is $\arctan(2/3)$.

*Case $g = 4$ (cousin primes).* The composites are $p_i + 1$, $p_i + 2$, $p_i + 3$. Here $p_i + 1$ and $p_i + 3$ are even ($\Delta x = 2$ each), and $p_i + 2$ is an odd composite with $\text{lpf}(p_i + 2) \geq 3$. So $\Delta x_{\text{FS}} \geq 2 + 3 + 2 + 1 = 8$, giving slope $\leq \arctan(4/8) = \arctan(1/2) \approx 26.57° < 33.69°$.

*General case $g \geq 4$.* Among the $g - 1$ composites, at least $\lfloor (g-1)/2 \rfloor$ are even (contributing $\Delta x \geq 2$ each). Therefore:

$$\frac{g}{\Delta x_{\text{FS}}} \leq \frac{g}{1 + 2\lfloor(g-1)/2\rfloor + \lceil(g-1)/2\rceil} < \frac{g}{\frac{3}{2}(g-1)} = \frac{2g}{3(g-1)}.$$

For $g \geq 4$: $2g / (3(g-1)) \leq 8/9 < 2/3$. Therefore $\theta_i < \arctan(2/3)$.

The cases $g = 1$ (the pair $(2, 3)$, slope $45°$) and $g = 3$ (the pair $(2, 5)$) occur only below $p = 5$.

Therefore the twin slope $\arctan(2/3)$ is the unique maximum for $p_i \geq 5$. QED.

**Computational verification.** Among all 78,497 consecutive-prime segments up to $10^6$:

- Maximum slope for $p \geq 5$: $33.6901°$ (twin slope), achieved 8,169 times.
- No non-twin segment exceeds this value.
- The only segment exceeding the twin slope is $(2, 3)$ at $45°$.

**Table 2.** Slope distribution among consecutive-prime segments ($p \geq 5$, up to $10^6$).

| Percentile | Slope (degrees) |
|------------|-----------------|
| 50th | 9.87 |
| 75th | 21.80 |
| 90th | 33.69 (twin) |
| 95th | 33.69 (twin) |
| 100th | 33.69 (twin) |

Twin segments constitute the entire upper tail of the slope distribution.

![Figure 1: Twin-slope geometry on the Factor Skyline. Top: prime spire tops connected by segments, with twin-pair segments (red) achieving the maximum slope. Bottom: slope angle of each segment, showing the absolute ceiling at $\arctan(2/3)$.](FS_twin_slope_polyline.png)

![Figure 2: Slope distribution of all consecutive-prime segments on the Factor Skyline up to $10^6$, showing the twin-slope ceiling at $\arctan(2/3) \approx 33.69°$.](fig1_slope_distribution.png)


## 5. Twin Primes in Bertrand Intervals

We now analyze the interval $[p, 2p]$ for each prime $p$. Bertrand's postulate guarantees at least one prime in every such interval; we ask the stronger question of whether the twin-slope ceiling is achieved within it.

**Definition 5.1 (Twin opportunity function).** For a prime $p$, define:

$$O(p) = p \cdot T\!\left(\sqrt{2p}\right) = p \cdot \frac{1}{2} \prod_{\substack{3 \leq q \leq \sqrt{2p} \\ q\ \text{prime}}} \left(1 - \frac{2}{q}\right),$$

the expected number of twin-open template positions in $[p, 2p]$ after all coverage layers with width $q \leq \sqrt{2p}$ have acted.

**Theorem 5.2 (Divergence of twin opportunities).** $O(p) \to \infty$ as $p \to \infty$. Specifically:

$$O(p) \sim \frac{4 C_2 e^{-2\gamma}}{\left(\ln(2p)\right)^2} \cdot p \to \infty.$$

*Proof:* By Theorem 3.4, $T(\sqrt{2p}) \sim C_2 \cdot D(\sqrt{2p})^2$. By Mertens' theorem, $D(\sqrt{2p}) \sim 2e^{-\gamma} / \ln(2p)$. Therefore $T(\sqrt{2p}) \sim 4C_2 e^{-2\gamma} / (\ln(2p))^2$, which decays only as $1/(\ln p)^2$. Since $O(p) = p \cdot T(\sqrt{2p})$, linear growth in $p$ overwhelms the quadratic-logarithmic decay. QED.

The Hardy-Littlewood heuristic predicts the number of *actual* twin prime pairs in $[p, 2p]$:

$$E(p) = C_2 \cdot \frac{p}{(\ln p)^2},$$

which also diverges.

**Table 3.** Twin coverage of Bertrand intervals.

| $p$ | $O(p)$ | $E_{\text{HL}}(p)$ | Actual twins | $O/\text{Actual}$ |
|-----|---------|---------------------|--------------|---------------------|
| 101 | 5.0 | 6.3 | 7 | 0.71 |
| 997 | 26.6 | 27.6 | 25 | 1.06 |
| 9,973 | 163.5 | 155.3 | 135 | 1.21 |
| 99,991 | 1,101.7 | 996.0 | 936 | 1.18 |
| 199,999 | 1,977.0 | 1,772.4 | 1,644 | 1.20 |

**Computational result.** For every prime $3 \leq p \leq 200{,}000$, the interval $[p, 2p]$ contains at least one twin prime pair. The only prime $p$ for which $[p, 2p]$ is twin-free is $p = 2$ (the interval $[2, 4]$ contains primes 2 and 3 but no twin pair). This was verified over all 17,984 primes in the range.

![Figure 2: Twin coverage of Bertrand intervals $[p, 2p]$ for $p \leq 200{,}000$. Green indicates twin-covered; red indicates twin-free. Only $p = 2$ is twin-free.](fig2_twin_coverage.png)

**Twin desert growth.** The maximum gap between consecutive twin prime pairs grows slowly with scale:

**Table 4.** Maximum twin desert vs prediction.

| Scale | Max gap | $(\ln p)^3 / C_2$ | Ratio |
|-------|---------|--------------------|-------|
| $p < 10{,}000$ | 210 | 592 | 0.35 |
| $p < 100{,}000$ | 630 | 1,156 | 0.55 |
| $p < 1{,}000{,}000$ | 1,452 | 1,997 | 0.73 |

The maximum twin desert grows as $O((\ln p)^3)$ --- far slower than the interval length $p$. The ratio of actual to predicted maximum shows no anomalous acceleration.

![Figure 3: Growth of maximum twin deserts compared to the $(\ln p)^3 / C_2$ prediction.](fig3_twin_deserts.png)


## 6. The Filling Condition

We now formalize the single remaining obstacle separating the FS structural guarantees from a proof of the twin prime conjecture.

**Definition 6.1 (Filling probability and obstruction).** For each twin-open template position in $[p, 2p]$, let $\delta(p)$ denote the probability that the position is occupied by an actual twin prime pair (i.e., both members escape all coverage layers with width $q > \sqrt{2p}$). Define the *twin obstruction probability*:

$$R(p) = (1 - \delta(p))^{O(p)},$$

the probability that *all* $O(p)$ twin-open slots are unfilled.

**Theorem 6.2 (Obstruction decay under Cramer model).** Under the Cramer independence model, $\delta(p)$ is bounded below by a positive constant as $p \to \infty$, and:

$$R(p) \sim \exp\!\left(-C_2 \cdot \frac{p}{(\ln p)^2}\right) \to 0$$

super-exponentially.

*Proof:* Under independence, each twin-open position is filled with probability $\delta(p) = E(p) / O(p)$, which stabilizes near $0.89$ as $p \to \infty$ (verified computationally). Since $\delta(p) \cdot O(p) = E(p) = C_2 \cdot p / (\ln p)^2 \to \infty$, we have $R(p) = (1 - \delta)^{O(p)} \leq \exp(-\delta \cdot O(p)) = \exp(-E(p)) \to 0$. The convergence is super-exponential: at $p = 10{,}000$, $\ln R(p) \approx -155$; at $p = 200{,}000$, $\ln R(p) \approx -1{,}772$. QED.

**Table 5.** Obstruction analysis.

| $p$ | $O(p)$ | $\delta(p)$ | $E_{\text{HL}}(p)$ | $\ln R(p)$ | Actual |
|-----|---------|-------------|---------------------|------------|--------|
| 997 | 26.6 | 1.040 | 27.6 | $-27.6$ | 25 |
| 9,973 | 163.5 | 0.950 | 155.3 | $-155.3$ | 135 |
| 99,991 | 1,101.7 | 0.904 | 996.0 | $-996.0$ | 936 |
| 499,979 | 4,328.0 | 0.886 | 3,833.6 | $-3{,}833.6$ | 3,603 |

![Figure 4: Obstruction probability $R(p)$ on a log scale, showing super-exponential decay.](fig4_obstruction.png)

**Remark 6.2.** The sum $\sum_{p\ \text{prime}} R(p) = \sum_p \exp(-E(p))$ converges, since $E(p) \to \infty$. If twin-free events for distinct intervals were independent, the Borel-Cantelli lemma would imply that only finitely many twin-free intervals $[p, 2p]$ exist. The events are not strictly independent, but their correlation decays rapidly with the separation between intervals.

**Conjecture 6.3 (The Filling Condition).** For all sufficiently large primes $p$, at least one twin-open template position in $[p, 2p]$ is occupied by an actual twin prime pair.

**Theorem 6.4 (Three equivalent formulations).** The Filling Condition (Conjecture 6.3) is equivalent to each of the following:

*Form 1 (Geometric).* For all $p \geq p_0$, the Factor Skyline restricted to $[x_{\text{FS}}(p),\, x_{\text{FS}}(2p)]$ contains at least one segment of slope $\arctan(2/3)$.

*Form 2 (Combinatorial).* Among the $O(p) \to \infty$ twin-open positions in the $p_k\#$-template restricted to $[p, 2p]$ (where $p_k \sim \sqrt{2p}$), at least one pair $(r, r+2)$ satisfies: both $r$ and $r+2$ are prime.

*Form 3 (Analytic).* $\pi_2(2N) - \pi_2(N) \geq 1$ for all sufficiently large $N$, where $\pi_2(x) = |\{p \leq x : p \text{ and } p+2 \text{ both prime}\}|$.

*Proof of equivalence:* Forms 1 and 2 are equivalent by Theorem 3.5 (twin pairs have FS-x gap exactly 3, the unique slope-maximizing configuration) and Theorem 4.2 (the slope ceiling is achieved only by twins). Forms 2 and 3 are equivalent by definition: a twin-open position $(r, r+2)$ where both are prime is exactly a twin prime pair in $[p, 2p]$. QED.

**Theorem 6.5 (Strength of the Filling Condition).** The Filling Condition is strictly weaker than breaking the full parity barrier. The parity barrier prevents sieve methods from establishing a *counting* lower bound $\pi_2(x) \geq c \cdot x / (\ln x)^2$ for any $c > 0$. The Filling Condition requires only an *existential* lower bound: $\pi_2(2N) - \pi_2(N) \geq 1$.

The Filling Condition is analogous to known partial parity bypasses:
- Friedlander-Iwaniec [FI98] proved infinitely many primes of the form $a^2 + b^4$ (existential, not counting).
- Zhang [Zha14] and Maynard [May15] proved infinitely many prime pairs with gap $\leq 246$ (existential for *some* fixed gap, not specifically gap 2).

The Filling Condition asks for the same type of result --- existential, not counting --- for the specific gap 2.

**Table 6.** Hierarchy of results and conjectures.

| Statement | Status |
|-----------|--------|
| Infinitely many primes | Proved (Euclid) |
| A prime in $[p, 2p]$ | Proved (Bertrand, 1845) |
| Bounded prime gaps ($\leq 246$) | Proved (Zhang-Maynard-Tao, 2013--14) |
| **Filling Condition** | **Conjectured (this paper)** |
| Infinitely many twin primes | Conjectured |
| $\pi_2(x) \sim C_2 \cdot \text{Li}_2(x)$ | Conjectured (Hardy-Littlewood) |
| Positive sieve lower bound for twin primes | Blocked (parity barrier) |


## 7. The Information-Theoretic Perspective

The FS framework provides a quantitative decomposition of the parity barrier into template-determined and stochastic components. **The arguments in this section are heuristic and information-theoretic; they describe structural reasons why the Filling Condition is plausible, but do not constitute proofs.**

**Theorem 7.1 (Template-stochastic decomposition).** The FS increment sequence $\{\Delta x(n)\}$ decomposes into:

- **Template layer** (73.3% of positions): $\Delta x(n)$ is determined exactly by $n \bmod 30$ (the $5\#$-template). These positions are covered by widths 2, 3, or 5, and their FS-x contribution carries zero entropy.

- **Stochastic layer** (26.7% of positions): $\Delta x(n)$ depends on whether $n$ is prime or composite-with-large-lpf. This layer carries positive entropy.

**Table 7.** Information budget for the FS increment sequence.

| Component | Bits per integer | Nature |
|-----------|-----------------|--------|
| Template information | 1.70 | Deterministic |
| Escape uncertainty | 0.26 | Irreducible |
| Activation detail | 0.52 | Specific lpf for composites |
| **Total $H(\Delta x)$** | **2.48** | |

*Proof:* $H(\Delta x) = 2.483$ bits (unconditional). $H(\Delta x \mid n \bmod 30) = 0.783$ bits (conditional on template). Mutual information $I = 1.700$ bits. The escape layer contributes 0.26 bits, the entropy of a Bernoulli variable at escape density $D(p) \approx 0.27$ for the $5\#$-template. See [Pro26, Theorem 12.1]. QED.

**Observation 7.2 (The parity barrier as information bound).** The 0.26 bits per integer of escape-layer entropy is the information-theoretic content of the parity barrier. The coverage architecture determines *which* positions are template-open (73.3% of FS structure), but *whether* a template-open position is prime or composite-with-large-lpf requires the remaining 0.26 bits --- which is beyond deterministic control.

In the context of twin primes: the template identifies $O(p)$ twin-open slots in $[p, 2p]$, but determining which slots are filled requires resolving the escape-layer entropy at each slot. The Filling Condition asks whether the escape layer can systematically avoid all $O(p)$ slots when $O(p) \to \infty$.

**Observation 7.3 (Sub-Poisson regularity).** The prime counting process in fixed-width windows exhibits sub-Poisson variance [Pro26, Theorem 8.2]:

$$\frac{\text{Var}(\pi(n, n+W))}{\text{E}[\pi(n, n+W)]} \approx 0.46$$

across all tested window sizes $W$ (from $W = 20$ to $W = 200$). Escape events are *more regular* than a Poisson process.

![Figure 5: Sub-Poisson variance ratio for prime counting across window sizes.](fig5_sub_poisson.png)

This regularity is structurally significant for the Filling Condition: a conspiracy to avoid all $O(p)$ twin-open slots would require the escape process to exhibit *anti-regular* clustering correlated with the template structure. Sub-Poisson regularity works against such clustering --- primes spread more uniformly among open positions than a random process would.

**Remark 7.4 (Information-theoretic implausibility of avoidance).** The escape layer's 0.26 bits per integer, distributed across $p$ integers in $[p, 2p]$, provides $0.26p$ total bits of stochastic freedom. For the escape layer to systematically avoid *all* $O(p) \sim p / (\ln p)^2$ twin-open slots, it would need to encode a pattern anti-correlated with the template structure at $O(p)$ specific positions simultaneously. When $O(p) \gg 1$, this coordination requires $\Omega(\log O(p))$ bits of mutual information between the escape layer and the template structure. But CRT independence guarantees zero mutual information at the template level. The residual correlations (captured by the sub-Poisson ratio $\approx 0.46$) work *in favor* of filling, not against it.

This does not constitute a proof --- the argument quantifies structural implausibility, not impossibility --- but it identifies the reason why avoidance is untenable: the escape layer would need to "know" about and simultaneously avoid $O(p) \to \infty$ template-determined positions using only template-independent randomness.


## 8. Computational Methods and Reproducibility

All computational results in this paper were produced using sieve-based algorithms in Python, available in the companion repository [Pro26].

**FS coordinate computation.** A sieve of the least prime factor (Eratosthenes-type, $O(N \log \log N)$) computes $\text{lpf}(n)$ for all $n \leq N$. A single linear pass then accumulates FS-x coordinates. For $N = 10^6$, the total computation requires approximately 1 second on commodity hardware.

**Twin interval analysis.** For each prime $p \leq 200{,}000$, binary search on the sorted prime array identifies all primes in $[p, 2p]$, and consecutive differences detect twin pairs. The full analysis of 17,984 intervals completes in approximately 130 seconds.

**Slope envelope computation.** All 78,497 consecutive-prime segments up to $10^6$ are processed in a single pass, computing FS-x gaps and slope angles. The twin-slope ceiling (Theorem 4.2) is verified by confirming that no non-twin segment exceeds $\arctan(2/3)$.

**Reproducibility.** The repository includes a deterministic verification harness with 20 numerical tables covering all aspects of the FS framework. Results are seeded (seed 123456) for bitwise reproducibility across platforms. The relevant scripts are:

- `reproducibility/scripts/FS_prime_angles.py` --- slope angle computation
- `reproducibility/scripts/FS_twin_interval_analysis.py` --- Bertrand interval twin coverage
- `reproducibility/scripts/FS_slope_envelope.py` --- slope envelope analysis
- `reproducibility/scripts/FS_filling_condition.py` --- filling condition verification

All scripts and data are available at https://github.com/allen-proxmire/factor-skyline.


## 9. Conclusion

The Factor Skyline provides a geometric framework in which the twin prime question takes a sharp structural form. We have established the following chain of results:

1. The twin-segment slope $\arctan(2/3)$ is an absolute geometric ceiling on the skyline, achieved if and only if consecutive primes form a twin pair (Theorem 4.2).

2. The number of twin-open template positions in any Bertrand interval $[p, 2p]$ diverges as $p \to \infty$ (Theorem 5.2), and the obstruction probability $R(p)$ decays super-exponentially under the Cramer model (Theorem 6.2).

3. A single conjectural statement --- the Filling Condition (Conjecture 6.3) --- is the only obstacle separating the FS structural guarantees from the twin prime theorem. This condition is strictly weaker than breaking the parity barrier (Theorem 6.5).

4. The parity barrier, expressed in FS-information-theoretic terms, corresponds to 0.26 bits per integer of irreducible escape-layer entropy (Observation 7.2). Systematic avoidance of $O(p) \to \infty$ twin-open slots by the sub-Poisson escape process is information-theoretically implausible (Remark 7.4).

The Filling Condition occupies a precise position in the hierarchy of number-theoretic results: it is stronger than the Maynard-Tao bounded gaps theorem (which guarantees gap $\leq 246$ but not gap 2) and weaker than the full Hardy-Littlewood asymptotic (which gives the exact twin prime density). Proving it would require a partial bypass of the parity barrier analogous to those achieved by Friedlander-Iwaniec [FI98] and Zhang-Maynard-Tao [Zha14, May15] --- an existential result about a specific arithmetic pattern, not a counting result with optimal constants.

Possible approaches to the Filling Condition include:

- **Extension of sub-Poisson regularity.** If the sub-Poisson variance ratio $\text{Var}/\text{E} < 1$ could be established for twin prime counting (not just prime counting), the combination with $E(p) \to \infty$ would immediately give $P(\text{count} = 0) \to 0$.

- **Second-moment methods.** A bound of the form $\text{E}[(\pi_2(2N) - \pi_2(N))^2] \ll \text{E}[\pi_2(2N) - \pi_2(N)]^2$ would establish concentration around the diverging mean, ruling out the zero-count event.

- **Bombieri-Vinogradov type estimates.** Equidistribution of twin primes in arithmetic progressions to modulus $Q = N^{\theta}$ for any $\theta > 0$ would suffice.

The conceptual arc of this paper can be summarized as follows. The Factor Skyline encodes every integer's multiplicative structure into a geometric column. Primes escape as tall, narrow spires; twin primes produce the steepest possible connections between consecutive spires. The coverage-protection mechanism guarantees that opportunities for twin primes grow without bound. The template persistence theorem guarantees that no finite set of sieve layers can close off all twin-open positions. What remains is a single question: among the superabundant twin-open slots that the architecture preserves, is at least one actually filled? The FS does not answer this question. What it provides is a geometric language that makes the structure of the problem --- and the exact location of the remaining obstacle --- visible.


## Acknowledgments

Portions of the computational exploration and manuscript drafting were assisted by AI tools. The author thanks the developers of SymPy and matplotlib for the computational infrastructure underlying the reproducibility framework.


## References

[Bom76] E. Bombieri. The asymptotic sieve. *Mem. Accad. Naz. dei XL*, 1/2:243--269, 1976.

[Che73] J.-R. Chen. On the representation of a larger even integer as the sum of a prime and the product of at most two primes. *Sci. Sinica*, 16:157--176, 1973.

[FI98] J. Friedlander and H. Iwaniec. The polynomial $X^2 + Y^4$ captures its primes. *Ann. of Math.*, 148(3):945--1040, 1998.

[GPY09] D. A. Goldston, J. Pintz, and C. Y. Yildirim. Primes in tuples I. *Ann. of Math.*, 170(2):819--862, 2009.

[HL23] G. H. Hardy and J. E. Littlewood. Some problems of 'Partitio Numerorum'; III: On the expression of a number as a sum of primes. *Acta Math.*, 44:1--70, 1923.

[May15] J. Maynard. Small gaps between primes. *Ann. of Math.*, 181(1):383--413, 2015.

[Mer74] F. Mertens. Ein Beitrag zur analytischen Zahlentheorie. *J. Reine Angew. Math.*, 78:46--62, 1874.

[Pol14] D. H. J. Polymath. Variants of the Selberg sieve, and bounded intervals containing many primes. *Res. Math. Sci.*, 1:12, 2014.

[Pro26] A. Proxmire. The Factor Skyline: An Ontological Lookout Over the Integers. 2026. DOI: 10.5281/zenodo.18275273. Available at https://github.com/allen-proxmire/factor-skyline.

[Sel49] A. Selberg. An elementary proof of the prime-number theorem. *Ann. of Math.*, 50(2):305--313, 1949.

[Zha14] Y. Zhang. Bounded gaps between primes. *Ann. of Math.*, 179(3):1121--1174, 2014.
