# The Prime Structure Factor

### The primes diffract like a crystal — and the crystal is the wheel

Allen Proxmire · July 2026

> **What this is.** A clean empirical/exact result (the diffraction pattern of the primes) with a clearly-flagged interpretive reading (the ED "interrupted wave = particle" picture). The object is standard — the prime *structure factor*, a.k.a. "primes as a quasicrystal" (Torquato–Zhang–de Courcy-Ireland, 2018); the value here is arriving at it from the particle/point-process side and reading its peaks directly as the wheel. Tags: **[fact]** established/exact · **[emp]** measured here · **[interp]** interpretation. Companion (position-space dual): [`Offset_Correlation_Curve.md`](Offset_Correlation_Curve.md).

---

## 1. The object

Treat the primes as a **point process** — a stream of discrete events on the line — and ask what pattern they would make in a diffraction experiment. That is the **structure factor**
$$S(k) \;=\; \frac{1}{M}\left|\sum_{p \le N} e^{2\pi i k\,p}\right|^2 ,$$
the squared coherent amplitude at spatial frequency $k$ (cycles per integer), over the $M$ primes in the window. A featureless (Poisson) point process gives $S(k)\approx 1$; sharp peaks that **grow with $M$** signal genuine crystalline order at that frequency.

## 2. The result: Bragg peaks at every rational, with height $(\mu(m)/\varphi(m))^2$

Measured over the $148{,}932$ odd primes below $2\times10^6$ (Figure `figures/prime_structure_factor.png`), the primes produce **sharp Bragg peaks at rational frequencies**, and the peak at $k = a/m$ (lowest terms) has height

$$\frac{S(a/m)}{M} \;=\; \left(\frac{\mu(m)}{\varphi(m)}\right)^2 \qquad \text{[fact, exact].}$$

**[emp]** matching to the digit:

| $k = a/m$ | $S/M$ | $(\mu(m)/\varphi(m))^2$ | what it is |
|---|---|---|---|
| $1/2$ | 1.0000 | $(-1/1)^2 = 1$ | all-odd — *perfect* period-2 order (tallest possible) |
| $1/3,\,2/3,\,1/6,\,5/6$ | 0.2500 | $(\mp1/2)^2 = 1/4$ | the **$2\cdot3$ wheel** |
| $1/5,\dots,1/10,\dots$ | 0.0625 | $(1/4)^2 = 1/16$ | the factor-5 structure |
| $5/14,\dots$ | 0.0278 | $(1/6)^2 = 1/36$ | the factor-7 structure |
| $1/4,\,1/8,\,3/8,\dots$ | **0.00000** | $\mu(4)=\mu(8)=0$ | **suppressed** — powers of 2 add no order |

Two things make this remarkable:

- **The heights scale with $M$** (the $1/2$ peak is literally $S=M$), so these are *true Bragg peaks* — real crystalline order, not noise. The primes have **no period whatsoever, yet diffract like a crystal**: the definition of a **quasicrystal** (effectively limit-periodic).
- **The height law is the wheel — and *only* the wheel.** The height is $(\mu(m)/\varphi(m))^2 = \mu(m)^2/\varphi(m)^2$, so what survives the squaring is $\mu(m)^2 \in \{0,1\}$ — a bare **squarefree indicator** (powers of 2, and $9, 25, \dots$ give **no** peak) — times $1/\varphi(m)^2$. That is the coprimality/singular-series *template*, written in frequency space. **The *sign* of $\mu(m)$ — the parity / Möbius-randomness / Sarnak-hard layer — is squared away and does not appear in $S(k)$ at all.** So the structure factor probes exactly the **wheel/template** (the finite-memory-*reachable* layer) and is **blind to the parity barrier**: it sees the order the sieve builds, never the hard randomness it hides. *(Correction noted 2026-07-14, prompted by the ED-session diffraction analysis.)*

## 3. The Fourier dual of the offset comb

The [offset-correlation comb](Offset_Correlation_Curve.md) and this structure factor are **Fourier transforms of each other** (Wiener–Khinchin): the diffraction pattern is the transform of the pair correlation. So the same wheel shows twice, once in each space:

| | position space (the comb) | frequency space (this) |
|---|---|---|
| **multiples of 6** | tall teeth | peaks at $1/6, 1/3, 2/3, 5/6$ |
| **factor 5 (30)** | tallest teeth | peaks at fifths/tenths |
| **powers of 2** | flat baseline | **silence** at $1/4, 1/8, \dots$ |

You can read the wheel off either side of the Fourier mirror.

## 4. The structure factor splits order from randomness

The diffraction pattern separates the two faces of the primes cleanly, in one image:

- the **sharp Bragg peaks = the ordered part = the wheel** — deterministic, crystalline, exact;
- the **diffuse background = the disordered part = the pseudo-randomness** — the zero-side, the Cramér noise.

Everything deterministic about the primes lives in the spikes; everything random lives in the haze. This is the sharpest statement of the collection's thesis — *wheel order plus pseudo-random disorder* — now as a physical diffraction pattern.

## 5. The particle reading (ED)

**[interp]** The picture that led here: *an interrupted wave is a particle; the primes are the interruptions (the "did-happen" commitments); show me their particle spectrum.* This is that spectrum. Treated as a stream of particles, the primes are not scattered at random — they sit on a **hidden quasicrystalline lattice, and the lattice is the wheel.** Each prime is a commitment event; the events, collectively, diffract.

Honest boundary, as always: this is a **structural** result about a point process, not a claim that primes are physical particles. What is shared with the ED/particle picture is the *point-process form* — a continuous intensity (the wave, $1/\log x$) punctuated by discrete events (the particles/primes), whose collective arrangement has a diffraction pattern. That form is exact and measured; the physics vocabulary is a lens, not an identity.

## 6. The sixth shadow

The wheel, once more — now as a crystal. The shadows so far: jumping champions, the Seven Sisters, the forbidden widths $\{2,4,6,10\}$, the angle-wobble $1\%$, the offset-correlation comb, and this **diffraction pattern**. Six faces, one wheel; this one is the primes revealed as a quasicrystal made of commitments.

---

## Appendix. Reproduction

```python
import numpy as np
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
N=2_000_000; B=sieve(N)
P=np.array([i for i in range(3,N+1) if B[i]],dtype=float)   # odd primes
M=len(P)
def SN(k): return abs(np.sum(np.exp(2j*np.pi*k*P)))**2/M/M   # structure factor / M
from math import gcd
# Bragg peak at a/m has height (mu(m)/phi(m))^2 ; compare:
for m in (2,3,4,5,6,7,10):
    a=1
    print(m, round(SN(a/m),4))   # 1, 0.25(if m=3), 0(m=4), 0.0625(m=5), 0.25(m=6)...
```

## References

- S. Torquato, G. Zhang, M. de Courcy-Ireland, *Uncovering multiscale order in the prime numbers via scattering* (J. Stat. Mech., 2018) — the prime structure factor / "prime quasicrystal."
- Wiener–Khinchin: the structure factor is the Fourier transform of the pair correlation.
- A. Proxmire, *The Offset-Correlation Curve* (this repository) — the position-space dual.
- A. Proxmire, *One Wheel, Many Shadows* and *The Wolves and the Clock* (Primes collection) — the unifying frame and the point-process reading.
- Figure: `figures/prime_structure_factor.png`.
