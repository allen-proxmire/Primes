# The Offset-Correlation Curve

### Sampling the primes against a shifted mirror — and hearing the wheel

Allen Proxmire · July 2026

> **What this is.** A clean empirical result (the primes' pair-correlation as a function of offset), together with a clearly-flagged *interpretive* reading (the quantum-mechanical "sample the mirror" picture). The result is standard Hardy–Littlewood; the value here is arriving at it from the offset/Born side and confirming it directly. Tags: **[fact]** established, **[emp]** measured here, **[interp]** interpretation.

---

## 1. The object

Ask the pattern to **sample a copy of itself, shifted by an offset $g$**: count the $n \le x$ for which *both* $n$ and $n+g$ are prime. Analytically this is the **autocorrelation of the primes at lag $g$**,
$$\sum_{n \le x} \Lambda(n)\,\Lambda(n+g),$$
the von Mangoldt function multiplied by a copy of itself retarded by $g$. **[fact]** Twin primes are the special case $g=2$; every prime constellation is this pattern-times-shifted-mirror at some lag. This is the exact object the quantum-mechanical instinct points at — a *retarded self-correlation*, $\psi$ against $\psi^*$ a little late.

## 2. The result: the curve is the wheel

Hardy–Littlewood predicts the offset-correlation, relative to the twin ($g=2$) rate, is the **singular series ratio**
$$\frac{C(g)}{C(2)} \;=\; \prod_{\substack{p \mid g \\ p > 2}} \frac{p-1}{p-2} \qquad (g \text{ even; } 0 \text{ for } g \text{ odd}).$$
Measured to $N = 10^7$, the empirical curve matches this to about **1%** across every even offset $g \le 70$ (Figure `figures/offset_correlation.png`).

| $g$ | empirical | HL $C(g)/C(2)$ | why |
|---|---|---|---|
| 2, 4, 8, 16, 32, 64 | ≈ 1.00 | 1.000 | powers of 2 — no odd-prime resonance (**baseline**) |
| 6, 12, 18, 24, 36, 48, 54 | ≈ 1.99 | 2.000 | divisible by 3 → $\times\tfrac{2}{1}$ |
| 10, 20, 40, 50 | ≈ 1.33 | 1.333 | divisible by 5 → $\times\tfrac{4}{3}$ |
| 30, 60 | ≈ 2.65 | 2.667 | $2\cdot3\cdot5$ → $\times\tfrac{8}{3}$ (**tallest teeth**) |
| 42 | ≈ 2.39 | 2.400 | $2\cdot3\cdot7$ → $\times 2\cdot\tfrac{6}{5}$ |
| 66 | ≈ 2.21 | 2.222 | $2\cdot3\cdot11$ → $\times 2\cdot\tfrac{10}{9}$ |

**[emp]** The offset-correlation is a **comb**: baseline at offsets that are powers of 2, a tooth of height $\prod_{p\mid g,\,p>2}\frac{p-1}{p-2}$ at every other even offset. That comb *is* the wheel — and it *is* the jumping-champion story drawn as a function of lag: offset 6 is twice as resonant as offset 2, which is exactly why 6 is the most common gap, and 30 tops it because it carries the extra factor 5.

## 3. Two faces in one graph

**[fact/emp]** The dots land *on* the Hardy–Littlewood line — that is the **mean**, the singular series, the **wheel** ($C(g)$). They scatter around it by ~1% — that is the **fluctuation**, the zero-driven / pair-correlation part (Montgomery). So a single measured curve shows *both* faces the offset-sampling was expected to surface: the deterministic wheel in the comb, the zeros in the wiggle.

## 4. The Born / retarded reading

**[interp]** The quantum-mechanical picture that motivated this — *sample the wave, multiply by its mirror a little late* — is now grounded, with its honest boundary intact:

- A **same-time** $\psi\psi^*$ is a Born probability; a **two-time** $\psi(t)\psi^*(t-\tau)$ is a **propagator**. This offset-correlation is the two-time object: the primes correlated with their own retarded copy, the lag $g$ playing $\tau$. That is consistent with the finitist *speed-of-influence* sieve (influence arrives with a delay; the self-correlation is therefore retarded).
- It is a **pair** correlation, **not** a single-amplitude $|\psi|^2$. This is not a new caveat — the companion QM Amplitude work already closed it: the twin kernel is irreducibly bilinear ("one object sampled twice," non-separable). The curve here is fully consistent with that: what the retarded mirror returns is $C(g)$, a *two-point* object.
- **The echo the mirror hears is the wheel.** For every lag $g$, the value of the retarded self-correlation is the singular series $C(g)$ — tuned by which small primes divide $g$. Sample the mirror at offset 6 and hear $\times 2$; at 30, hear $\times 8/3$; at a power of 2, hear the baseline.

So the Born-side instinct, made concrete, **is the Hardy–Littlewood pair correlation**, reached from the offset/quantum direction and confirmed directly.

## 5. One more shadow

This is the offset-correlation shadow of the same object that runs through the rest of the collection. The comb is the **wheel**; the jumping champions are its tallest teeth; the twin count is its $g=2$ value; the consecutive-gap anti-correlation measured in the [angle note](PG_Angle_Wobble.md) is a neighbouring piece of the same structure. *One wheel, now heard as an echo.*

---

## Appendix. Reproduction

```python
import math
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
N=10**7; B=sieve(N); P=[i for i in range(2,N+1) if B[i]]
gs=range(2,71,2); counts={g:0 for g in gs}
for p in P:
    if p+70>N: break
    for g in gs:
        if B[p+g]: counts[g]+=1                     # both p and p+g prime
def hl(g):                                          # HL singular-series ratio C(g)/C(2)
    gg=g
    while gg%2==0: gg//=2
    r=1.0; d=3
    while d*d<=gg:
        if gg%d==0:
            r*=(d-1)/(d-2)
            while gg%d==0: gg//=d
        d+=2
    return r*((gg-1)/(gg-2) if gg>1 else 1)
c2=counts[2]
for g in gs: print(g, round(counts[g]/c2,3), round(hl(g),3))   # empirical vs HL, ~1%
```

## References

- G. H. Hardy, J. E. Littlewood, *Some problems of 'Partitio numerorum' III* (1923) — the singular series $C(g)$.
- H. L. Montgomery, *The pair correlation of zeros of the zeta function* (1973) — the fluctuation side.
- A. Proxmire, *Template and Amplitude: … the Prime Escape as a Quantum-Mechanical Form* and the *Bilinearity* open-question memo (this repository) — the pair-vs-single-amplitude boundary.
- A. Proxmire, *The Prime-Triangle Angle* (this repository) — the neighbouring consecutive-gap correlation.
- A. Proxmire, *One Wheel, Many Shadows* (Primes collection) — the unifying frame.
- Figure: `figures/offset_correlation.png`.
