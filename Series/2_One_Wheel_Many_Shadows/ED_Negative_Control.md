# ED as the Negative Control

### Exclusion vs. *arithmetic* exclusion — what actually builds the wheel

Allen Proxmire · July 2026

> **What this is.** A controlled contrast, computed twice independently (an ED-framework session and a number-theory session) and in agreement. It answers a specific question — *is the primes' "wheel" diffraction generic to exclusion processes, or specific to arithmetic exclusion?* — and lands a clean negative result. **Standing rail (from the finite-memory-ceiling corpus, `Paper_FiniteMemoryCeiling_Primes`, run `aa0f545`): this is a structural/class parallel only — ED does not generate, explain, or support the primes.** Tags: **[fact]** established · **[emp]** measured · **[interp]** framing.

---

## 1. The question

The prime numbers, as a point process, **diffract like a crystal**: the structure factor $S(k)=\frac1M|\sum_p e^{2\pi i k p}|^2$ has sharp Bragg peaks at every rational $k=a/m$ of height $(\mu(m)/\varphi(m))^2$ (see [`Prime_Structure_Factor.md`](Prime_Structure_Factor.md)). This "wheel" is built by **exclusion** — each prime forecloses its own multiples. The natural hypothesis: *maybe any exclusion process produces this signature.* If so, it would be a domain-general law, not a fact about arithmetic.

To test it we need a **non-arithmetic exclusion process** as a control. ED supplies one.

## 2. The two processes

- **The sieve (arithmetic exclusion).** A prime excludes its multiples — a *periodic, divisibility* rule (mod $p$); stacking these over the small primes builds the wheel. Output: the primes.
- **ED commitment (causal exclusion).** ED's commitment (the irreversible arrow; no-erasure) forecloses incompatible future states as a **hard-core, finite-reach** relation on the participation graph — *no modulus, no divisibility, no "every $m$-th event."* It is **aperiodic** exclusion with finite memory. The ED session supplied a concrete, deterministic generator (a hard-core dead-time + finite-memory AR(1) log-gap renewal; no arithmetic input) producing $50{,}000$ event positions along the arrow of time, mean spacing $1$.

Both belong to the same abstract **finite-memory exclusion class**; they differ in the *kind* of exclusion — and that is the whole experiment.

## 3. The result: liquid vs. crystal

Computing $S(k)$ on ED's process (independently reproduced from the generator) versus the primes (Figure `figures/ed_vs_primes_structure.png`):

| | ED commitment process | the primes |
|---|---|---|
| low $k$ | **suppressed**, $S\approx0.18$ (correlation hole, hyperuniform-leaning) | — |
| rational $k=a/m$ | **flat**, $S\approx0.01$–$0.17$ (diffuse baseline) | **Bragg peaks** $0.25$–$1.0$ |
| main feature | one **broad liquid peak** near mean-spacing, height $O(10)$ — *does not grow with $N$* | sharp peaks scaling with $M$ |
| verdict | a **disordered liquid** — neither wheel nor GUE | a **quasicrystal** |

**[emp]** ED is flat exactly where the primes tower. The two computations — the ED session's and this one — agree: **no Bragg peaks at any rational.** ED carries none of the prime fingerprint.

## 4. The conclusion

**The wheel is not generic to exclusion. It is specific to *arithmetic* (divisibility) exclusion.** Generic causal exclusion (ED) gives a liquid; the "every $m$-th" divisibility rule is what turns the liquid into a crystal. ED is a **clean negative control** that isolates the source of the wheel — not repulsion, but **divisibility**.

This is the honest resolution of the whole "does ED share a layer with the primes?" thread:

- **The only shared layer** is the abstract *finite-memory exclusion class*.
- **Within that class**, arithmetic exclusion (primes) and causal exclusion (ED) produce **opposite** fingerprints — crystal vs. liquid.
- So ED's true relation to the primes is **contrast, not support.** It does not generate or explain them; it *controls* for them, and the contrast names precisely what is special about the primes. (A negative control is often worth more than a confirmation — it tells you what the effect actually depends on.)

## 5. Two framing notes that keep it honest

- **Diffraction sees the template, not the parity barrier.** The peak heights are $(\mu(m)/\varphi(m))^2$; the squaring reduces $\mu(m)^2$ to a bare squarefree indicator, so the **sign** of $\mu$ — the parity / Möbius-randomness / Sarnak-hard layer — is invisible to $S(k)$. The structure factor probes exactly the **finite-memory-reachable wheel**, never the hard wall. This is why the comparison is fair: both ED and the sieve are being asked only about the *reachable* layer.
- **Native ED vs. ED-fed-arithmetic.** *Native* ED (causal exclusion, no arithmetic) is the liquid above. An ED-*class* process **fed an imposed arithmetic exclusion** would instead reproduce the wheel's Bragg peaks *up to its finite-memory horizon* and fade above — the corpus's "template yes" result, in Fourier space. These are different objects with opposite fingerprints; this note tests **native ED**, and the answer is *liquid*.

---

## Appendix. Reproduction

```python
import math, numpy as np
# ED commitment process (from the ED session) — deterministic, no arithmetic input
def lcg(seed):
    s=seed & 0xFFFFFFFF
    while True:
        s=(1103515245*s+12345)&0x7FFFFFFF; yield s/0x7FFFFFFF
def gen(N=50000, dead=0.3, rho=0.5, seed=12345, sig=0.55):
    u=lcg(seed); L=0.0; xs=[0.0]
    for _ in range(N-1):
        a=next(u); b=next(u)
        z=math.sqrt(-2*math.log(a+1e-12))*math.cos(2*math.pi*b)
        L=rho*L+math.sqrt(1-rho*rho)*sig*z
        xs.append(xs[-1]+dead+math.exp(L-sig*sig/2)*(1-dead))
    return np.array(xs)
X=gen(); M=len(X); dens=M/(X[-1]-X[0])
S=lambda k: abs(np.sum(np.exp(2j*np.pi*k*X)))**2/M
print([round(S((1/m)*dens),3) for m in (2,3,4,5,6)])   # all diffuse (~0.01-0.17): no wheel
```

## References

- ED session handoff (2026-07-14) — mechanism, generator, and independent $S(k)$; grounded in `Paper_FiniteMemoryCeiling_Primes` (run `aa0f545`).
- A. Proxmire, *The Prime Structure Factor* (this repository) — the crystal side.
- S. Torquato, G. Zhang, M. de Courcy-Ireland (2018) — the prime structure factor.
- Figure: `figures/ed_vs_primes_structure.png`.
