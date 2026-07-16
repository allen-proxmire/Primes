# Prime-Gap Memory and the Differencing Trap

### The wobble looks 44% predictable; 42 of those points are an artifact — but the last 2 are the wheel

Allen Proxmire · July 2026

> **What this is.** A methodological result with a small genuine core. The eye-catching "prime weather" one sees in the *change* of the gaps — volatility clustering, big-jump recoil, a windowed wobble that looks nearly half-predictable — is **almost entirely an artifact of differencing**, reproduced by random data. The instrument that separates signal from artifact is a specific null: *shuffle the gaps, then apply the same transform.* Under that null a genuine residual survives — roughly **+2 points of R² in the windowed wobble**, about six times the memory in the raw gaps — and it is plausibly the wheel's fingerprint on consecutive gaps. Tags: **[emp]** measured · **[null]** shuffle-control · **[fact]** exact · **[interp]** reading. Companion negative control: [`ED_Negative_Control.md`](ED_Negative_Control.md); frequency-space dual: [`Prime_Structure_Factor.md`](Prime_Structure_Factor.md).

All figures over the $269{,}\!991$ gaps between consecutive primes in $[10^6, 5\times10^6]$ (mean gap $\overline g = 14.81$, sd $12.29$).

---

## 1. The seductive picture

Write $g_n = p_{n+1}-p_n$ for the gap and $\Delta g_n = g_{n+1}-g_n$ for the **jitter** (the change in gap, i.e. the second difference of the primes; up to the damping $1/p$ this is the angle-wobble $\Delta\alpha$ of the Prime-Triangle note). Plotted in order, the jitter looks alive:

- **Volatility clustering.** Big jitters arrive in bursts. The mean $|\Delta g|$ after a *large* jitter (top decile) is $22.0$; after a *tiny* one, $10.7$ — against an overall mean of $12.9$. The autocorrelation of $|\Delta g|$ is $+0.31$.
- **Recoil.** After a large jitter, the next jitter has the *opposite* sign $81.8\%$ of the time — the "spike and return."
- **A predictable wobble.** Regress $\Delta g_n$ on its last five values: the fit explains **43.7%** of the jitter variance.

Any one of these, reported alone, reads as a discovery about the primes. All three are mirages.

## 2. The instrument: shuffle, then transform

The primes' program already carries the right reflex — the [ED negative control](ED_Negative_Control.md): a process that excludes *causally* rather than *arithmetically* diffracts as a liquid, proving the wheel's crystal is arithmetic. The same move disciplines time-series claims. The null hypothesis is *"the gaps carry no ordering memory"* — so the null sample is the **same multiset of gaps in random order**. Crucially, any statistic computed through a transform must be compared to that transform **applied to the shuffled gaps**, not to a shuffle of the transformed series.

> **The trap, stated once.** Shuffling $\Delta g$ *directly* destroys the differencing structure you are trying to account for, and so credits the artifact to the primes. The jitter must be **re-formed from shuffled gaps**: $\Delta g^{\text{null}} = \operatorname{diff}(\text{shuffle}(g))$.

## 3. What the null reveals

| statistic (window of 5, or lag 1) | real primes | correct null | genuinely prime |
|---|---|---|---|
| raw-gap memory — regress $g_n$ on last 5 | $0.32\%$ | $0.00\%$ | $\mathbf{+0.32}$ pp |
| gap autocorrelation, lag 1 | $-0.046$ | $-0.001$ | $\mathbf{-0.045}$ |
| jitter clustering, $\operatorname{corr}(|\Delta g_n|,|\Delta g_{n-1}|)$ | $+0.315$ | $+0.319$ | $-0.004$ *(artifact)* |
| jitter recoil, big $\to$ opposite sign | $81.8\%$ | $79.2\%$ | $+2.7$ pp |
| **windowed wobble — regress $\Delta g_n$ on last 5** | $43.67\%$ | $41.69\%$ | $\mathbf{+1.97}$ pp |

Two clean verdicts:

- **The clustering and most of the recoil are artifact.** The null reproduces them to within a hair. They are not prime weather; they are what differencing does to *any* spread-out sequence (§5).
- **A genuine residual survives, and it concentrates in the window of the wobble.** The raw gaps carry $+0.32$ pp of memory; the windowed jitter carries **$+1.97$ pp** — six times more — none of it reproduced by the null. On $2.7\times10^5$ samples this is overwhelmingly significant.

The lesson for the whole gap program: the interesting quantity is not how predictable the wobble *looks* ($44\%$) but how much of that survives the transform-matched null ($+2\%$).

## 4. Why differencing manufactures the mirage

The artifacts are not subtle statistics; they are forced by algebra. For an i.i.d. sequence $X$ with variance $\sigma^2$, the first difference $Y_n = X_{n+1}-X_n$ has

$$\operatorname{cov}(Y_n, Y_{n-1}) = \operatorname{cov}(X_{n+1}-X_n,\; X_n-X_{n-1}) = -\operatorname{Var}(X_n) = -\sigma^2,\qquad \operatorname{Var}(Y)=2\sigma^2,$$

so $\boxed{\operatorname{corr}(Y_n,Y_{n-1}) = -\tfrac12}$ **[fact, exact]** — a hard $-0.5$ recoil, with *no* memory in $X$ at all. That single identity is the "spike and return." Likewise $|Y_n|$ and $|Y_{n-1}|$ share the term $X_n$: a large $X_n$ inflates both, forcing a positive correlation of magnitudes — the "volatility clustering." Regressing $Y$ on its past then recovers the $-\tfrac12$ structure and reports a large $R^2$. All three headline effects are consequences of the shared term, present in the shuffled gaps and absent from the primes' account.

## 5. What is genuinely prime — the wheel in the gap correlations

Strip the pedestal and the residual is real. Two shuffle-proof facts remain:

1. **Consecutive gaps are weakly anti-correlated**, $\operatorname{corr}(g_n,g_{n+1}) = -0.046$ (null $\approx 0$). A large gap is followed, a touch more often than chance, by a smaller one — a genuine reversion in the *levels*, not the differences.
2. **A window of a few gaps constrains the next**, $+1.97$ pp beyond the differencing null.

Both point at the same source. Consecutive gaps are not independent because the **wheel** forbids many gap-sequences outright and biases the rest: the residues mod $6, 30, 210$ that one gap lands on shape which gaps can follow. This is the gap-space face of the **Lemke Oliver–Soundararajan** correlations (the "unexpected biases in consecutive primes," 2016), and the same coprimality template that casts every other shadow in this collection. The memory in the wobble is small, but it is the wheel — read through the correlations of successive escapes.

## 6. Reading the record straight

This note corrects an over-eager reading (my own, made and caught while writing it): that the jitter's clustering and recoil were prime "weather," and that amplitude was the knowable structure while sign was noise. The null reverses both halves. The **amplitude** persistence is the artifact; the small **genuine** memory lives in the *ordering of the gap levels* and surfaces most in the windowed wobble. The honest one-line model of "how far to the next prime" is therefore: **the base rate $\ln p$ sets the scale, the wheel sets the admissible slots, and the last few gaps shift the odds by about two points of variance — no more.** Everything past that is the pseudo-random residual the structure factor already isolated as diffuse background; here it is the same residual in the time domain.

---

## Appendix. Reproduction

```python
import random
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
B=sieve(8_000_000)
P=[i for i in range(1_000_000,5_000_000) if B[i]]
g=[P[i+1]-P[i] for i in range(len(P)-1)]
diff=lambda s:[s[i+1]-s[i] for i in range(len(s)-1)]

def R2(series,k=5):                      # in-sample R^2 predicting next from last k
    import numpy as np
    S=np.array(series,float)
    X=np.column_stack([S[k-1-j:len(S)-1-j] for j in range(k)]); y=S[k:]
    X=np.column_stack([X,np.ones(len(y))]); b,_,_,_=np.linalg.lstsq(X,y,rcond=None)
    return 1-((y-X@b)**2).sum()/((y-y.mean())**2).sum()

gs=g[:]; random.shuffle(gs)              # shuffle the GAPS, then difference
print("levels   real",round(R2(g),4),   "null",round(R2(gs),4))
print("wobble   real",round(R2(diff(g)),4),"null",round(R2(diff(gs)),4))
# key: the null jitters are diff(gs), NOT a shuffle of diff(g).
```

## References

- A. Proxmire, *The Prime-Triangle Angle* (this collection) — the wobble $\Delta\alpha$, and the earlier runs/shuffle observation this note refines.
- A. Proxmire, *The ED Negative Control* and *The Prime Structure Factor* (this collection) — the shuffle/negative-control discipline, and the order/randomness split in frequency space.
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes* (PNAS, 2016) — residue correlations of successive primes; the mechanism behind the surviving gap memory.
