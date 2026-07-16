# Primes — Results

A running list of what this work actually shows. Scan it, jump to what interests you. Tags: **[thm]** proven · **[conj]** conjecture (verified far, open) · **[emp]** empirical law · **[deriv]** derivation from known theory.

*(The organizing thesis: [`One_Wheel_Many_Shadows.md`](One_Wheel_Many_Shadows.md). Folder/paper inventory: [`PRIMES_MAP.md`](PRIMES_MAP.md).)*

## Headlines

- **[conj] A Bertrand postulate for twins.** Every dyadic interval $(x,2x]$ past $x=11$ contains a twin prime: $\pi_2(2x)-\pi_2(x)\ge1$. Verified to $10^{10}$ (27.4M twins). → [Twin Bertrand / PG II](Twin%20Bertrand/papers/PG_II_AngleRecord.pdf)
- **[thm] Forbidden gap-widths $\{2,4,6,10\}$.** These are exactly the prime-gap widths that can *never* contain two consecutive-prime sums. → [FS / Consecutive-Prime Sums](Factor%20Skyline/papers/FS_Consecutive_Prime_Sums_In_Gaps.pdf)
- **[thm] One polytope generates the Exponent Database.** Every EXPDB output is a projection/envelope of a single $\mathcal{P}\subset\mathbb{R}^5$. → [X5D](X5D%20EXPDB%20Framework/papers/X5D_Polyhedral-Reinterpretation.pdf)
- **[deriv] Two operations run the primes:** *doubling* ($p\mapsto2p$) and *the wheel* (primorials). On the Factor Skyline, doubling is the top ray and the wheel is the fan; primes are what escape both. → [FS / Synthesis](Factor%20Skyline/papers/FS_Synthesis_Doubling_and_Wheel.pdf)

## Twin Bertrand

- **[conj] Twin-Prime Bertrand Postulate (TPB):** $T_{k+1}<2T_k$ for every twin $T_k\ge11$. Weaker than the twin-prime conjecture, stronger than bounded gaps; immediate under Hardy–Littlewood, open unconditionally.
- **[emp] Angle-record theorem:** every closest-to-$45°$ angle record of the Prime Triangle (with $p_n\ge3$) is a twin prime — a geometric restatement of TPB. → [PG II](Twin%20Bertrand/papers/PG_II_AngleRecord.pdf)
- **[conj] Generalized Bertrand Principle (GBP):** TPB extends to cousins $(p,p+4)$ and sexy primes $(p,p+6)$, all verified to $10^{10}$; uniform envelope $G<0.171(\log P)^{3.22}$. → [PG III](Twin%20Bertrand/papers/PG_III_GBP.pdf)
- **[thm] Prime-Square-Difference identity:** $C_2^2-C_1^2=p_{n+2}^2-p_n^2$, with $\mathrm{PSD}_n=(p_{n+2}^2-p_n^2)/12$ always an integer ending in 0/4/6. → [PG I](Twin%20Bertrand/papers/PG_I_PrimeTriangle.pdf)
- **[emp] Twin-gap exponent:** $G_k\sim0.70(\log T_k)^{1.866}$ (below the Hardy–Littlewood $\beta=2$).
- **[emp] Δx cascade:** doubled twins $2p_k$ placed on a prime-rank axis; the step $\Delta x_k$ counts primes in $(2p_k,2p_{k+1}]$ and is a Poisson mixture, macro-linear ($R^2\approx0.996$) with chance-level micro-collinearity. → [FS–TB Δx Analysis](Twin%20Bertrand/papers/FS_TB_DeltaX_Analysis.md)
- **[verified/emp] Prime-triangle angle is a rescaled gap:** $\alpha_n = \arctan(p_n/p_{n+1}) \approx 45° - \frac{90}{\pi}\frac{g_n}{p_{n+1}}$ — angles rise to a $45°$ ceiling in gap-family arcs (twins on top, never reaching it). The wobble is ~99% universal (a $33\ln p/p$ envelope, a $1/3$ runs constant); the lone ~1% prime signal is consecutive-gap anti-correlation $-0.05$ = the Hardy–Littlewood wheel, built prime-by-prime. → [Angle Wobble](Twin%20Bertrand/papers/PG_Angle_Wobble.md)
- **[emp] Offset-correlation curve:** counting when both $n$ and $n+g$ are prime (the primes sampled against a copy shifted by $g$) reproduces the Hardy–Littlewood singular series $C(g)/C(2)=\prod_{p\mid g,p>2}\frac{p-1}{p-2}$ to ~1% — a comb with baseline at powers of 2, $\times2$ at multiples of 6, $\times8/3$ at 30. The "sample the mirror at lag $g$" echo *is* the wheel; jumping champions are its tallest teeth. → [Offset-Correlation Curve](Twin%20Bertrand/papers/Offset_Correlation_Curve.md)
- **[fact/emp] Primes diffract like a crystal:** the structure factor $S(k)=\frac1M|\sum_p e^{2\pi ikp}|^2$ has sharp Bragg peaks at every rational $k=a/m$ of exact height $(\mu(m)/\varphi(m))^2$ — tallest at $1/2$ (all-odd, =1), $1/4$ at the $2\cdot3$ wheel ($1/3,1/6,\dots$), zero at powers of 2. The primes are a **quasicrystal** whose lattice is the wheel; it's the Fourier dual of the offset comb, splitting order (Bragg peaks = wheel) from disorder (diffuse background = randomness). Diffraction sees only the squarefree *template* (the $\mu$ sign / parity barrier is squared away, invisible). → [Prime Structure Factor](Twin%20Bertrand/papers/Prime_Structure_Factor.md)
- **[emp] ED is the negative control (the wheel is *arithmetic* exclusion):** a non-arithmetic causal-exclusion process (ED's commitment generator) diffracts as a **liquid** — suppressed low-$k$, one broad $O(1)$ peak, **no Bragg spikes at rationals** — flat exactly where the primes tower. Verified independently by two sessions. So the wheel is *not* generic to exclusion; it takes *divisibility* (mod $p$) to turn the liquid into a crystal. ED's relation to the primes is **contrast, not support**. → [ED as the Negative Control](Twin%20Bertrand/papers/ED_Negative_Control.md)

## Factor Skyline

**The architecture** — each integer is a column (width $=\mathrm{lpf}$, height $=n/\mathrm{lpf}$); primes escape to the diagonal, composites fall to width-rays (the wheel).

- **[deriv] Classical multiplicative NT as structure:** PNT, Chebyshev's conservation law, Mertens, the Dickman function, Erdős–Kac, divisor averages — all as geometric features. → [FSPapers I–IV](Factor%20Skyline/papers/)
- **[thm] Coverage protection:** the Hardy–Littlewood $k$-tuple constants satisfy $C_H=2C_2>1$ exactly (Theorem 4.7a). → [FSPapers I](Factor%20Skyline/papers/FSPapers_01_architectural_foundation.pdf)
- **[emp] Consecutive-prime-sum density law:** a gap of width $W$ near $x$ holds $\approx W/(2\ln(x/2))$ sums $p_k+p_{k+1}$ — so ~55% of gaps hold none, ~37% exactly one. → [Consecutive-Prime Sums](Factor%20Skyline/papers/FS_Consecutive_Prime_Sums_In_Gaps.pdf)
- **[thm] Forbidden widths $\{2,4,6,10\}$** contain at most one such sum, no exceptions (verified to $2\times10^8$). Width 10 is the non-obvious straggler (a mod-6 argument).
- **[thm/emp] Seven Sisters & the wheel:** offsets $2p+k$ divisible by 3 never die to 3, so they land on primes ~2× as often; 100% coverage is impossible (unbounded gaps); extend along multiples of 15, 105. → [Seven Sisters: Wheel & Asymptote](Factor%20Skyline/papers/FS_Seven_Sisters_Wheel_Asymptote.pdf)
- **[thm] Sum = average, mirror law, doubling ladders:** on the skyline a consecutive-prime sum sits at height = its average; the "$-x,+y,-y,+x$" mirror fires iff the sum is centered; centered sums chain under doubling ($30\to60\to120\to240$). → [2p Bracket Construction](Factor%20Skyline/papers/FS_2p_Bracket_Construction.pdf)
- **[deriv] The escape ridge:** $x_{FS}(N)\sim4e^{-\gamma}N^{3/2}/\ln^2N$ — the extra $\sqrt N$ is the sieve's $p^2$ activation; explains the empirical escape-curve regression. → [The Escape Ridge](Factor%20Skyline/papers/FS_Escape_Ridge.pdf)
- **[emp] Twin-slope ceiling:** twin-prime geometry on the FS ($\alpha\to45°$ coherence). → [Twin-Slope Ceiling](Factor%20Skyline/papers/FS_twin_prime_geometry.md)

## X5D EXPDB Framework

- **[thm] Master polytope:** the Tao–Trudgian–Yang Exponent Database is generated by one $\mathcal{P}\subset\mathbb{R}^5$, with an X5D invariant, a monotone contraction flow, and a fixed-point theorem.
- **[emp] Guth–Maynard binding constraints:** a cusp at $\sigma=7/10$ (Ingham 1940 meets GM 2024 at $A=30/13$) fixes $\theta_{\mathrm{PNTALL}}=17/30$; sensitivity $d\theta/d\lVert A\rVert=169/900$; the attack surface is only ~0.006 wide. → [X5D](X5D%20EXPDB%20Framework/examples/GuthMaynard/)

---

*Add results as they land. Keep each a one-line claim + a tag + a pointer.*
