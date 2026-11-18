# The Traffic Law

### Two consecutive prime gaps can never both be ≡ 2, nor both ≡ 4 (mod 6)

Allen Proxmire

---

## 1. The rule

Every prime past 3 is $\equiv 1$ or $\equiv 2 \pmod 3$ — call these the two **lanes**. A gap $g$ between consecutive primes either stays in its lane ($g \equiv 0 \pmod 6$) or changes lane: up, $1 \to 2$ ($g \equiv 4$), or down, $2 \to 1$ ($g \equiv 2$). After a down-change the next prime is in lane 1, so the next gap can stay or change up but cannot change down again.

> **Theorem.** For consecutive primes past 3,
> $$g_n \equiv g_{n+1} \equiv 2 \pmod 6 \quad\text{and}\quad g_n \equiv g_{n+1} \equiv 4 \pmod 6$$
> never occur. **[fact]**

**Corollary.** The only gaps that can repeat immediately are multiples of 6. Over $[10^6, 3\times10^6)$, $3.39\%$ of steps repeat a gap, and none of those repeats is by a gap outside $6\mathbb Z$.

Transition frequencies over $[10^6, 3\times10^6)$:

| current gap | next $\equiv 0$ | next $\equiv 2$ | next $\equiv 4$ |
|---|---|---|---|
| $\equiv 0$ (stay) | 40.4% | 29.8% | 29.8% |
| $\equiv 2$ (down) | 44.8% | **0.0%** | 55.2% |
| $\equiv 4$ (up) | 44.7% | 55.3% | **0.0%** |

Under a gap-shuffle the two zeros become $28.4\%$ and $28.5\%$.

---

## 2. The signature in gap changes

$|\Delta g| = 6$ needs two gaps in the same residue class differing by 6. The $(2,2)$ and $(4,4)$ routes ($2\,\&\,8$, $4\,\&\,10$) are forbidden, leaving only $(0,0)$ ($6\,\&\,12$, $12\,\&\,18$, …). Against a gap-shuffled null (same gaps, order destroyed, then differenced):

| $\lvert\Delta g\rvert$ | real | null | ratio |
|---|---|---|---|
| 2 | 16.80% | 12.64% | 1.33 |
| 4 | 13.29% | 11.70% | 1.14 |
| **6** | **5.14%** | **10.29%** | **0.50** |
| 8 | 11.35% | 8.67% | 1.31 |
| 10 | 8.78% | 7.30% | 1.20 |
| **12** | **2.98%** | **6.57%** | **0.45** |
| 14 | 6.57% | 5.17% | 1.27 |

**[emp/null]** Multiples of 6 run at half the null rate; every other value is elevated.

---

## 3. Larger moduli

The same lane argument mod 5, 7, … forbids more repeats as the modulus grows:

| modulus | gap residues that occur | can repeat | forbidden to repeat | same-residue rate vs chance |
|---|---|---|---|---|
| 6 | 3 | 1 | **2** | 17% vs 35% |
| 30 | 15 | 5 | **10** | 4% vs 9% |
| 210 | 66 | 23 | **43** | 3.3% vs 7.5% |

---

## 4. It is the wheel

A wheel-Cramér surrogate — divisibility by the small primes exact, everything else independent — reproduces the dip depths: $|\Delta g| = 6$ at $5.09\%$ against $5.09\%$, $|\Delta g| = 12$ at $2.99\%$ against $3.01\%$. Respecting divisibility by 3, it inherits the zeros for free.

On top of the hard rule rides the **Lemke Oliver–Soundararajan lean**: among allowed moves, primes prefer changing lane to staying (the $55/45$ split above). The residual same-residue deficit fades like $1/\log$: $-0.193$ at $10^4$, $-0.171$ at $10^7$. So the mod-6 suppression is a hard mod-3 rule with the LOS lean layered over it, and the wheel model, respecting both, lands on the measured depths.

---

## 5. The same rule from the Eisenstein integers

With half-gaps $h = g/2$, the Loeschian form satisfies
$$3 \mid h_1^2 + h_1h_2 + h_2^2 \iff g_1 \equiv g_2 \pmod 6,$$
and by §1 that forces both $\equiv 0$. So "3 divides the Eisenstein norm of the half-gap pair" and "two consecutive gaps are both multiples of 6" are the same event. → [Gap Correlations §4](Gap_Correlations.md)

---

## 6. Ledger

**Classical:** the mod-3 lane structure, the wheel (Hardy–Littlewood), the LOS lean (2016).

**Contributed:** the rule stated as a transition prohibition with exact zeros, its measurement against a matched null, the tiering with the modulus, and the Eisenstein identification.

---

## Reproduction

```python
import random, collections
def sieve(n):
    b=bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i<=n:
        if b[i]: b[i*i::i]=bytearray(len(b[i*i::i]))
        i+=1
    return b
B=sieve(3_000_000); P=[i for i in range(1_000_000,3_000_000) if B[i]]
g=[P[i+1]-P[i] for i in range(len(P)-1)]

# §1 the zeros
T=collections.Counter((g[i]%6,g[i+1]%6) for i in range(len(g)-1))
for a in (0,2,4):
    tot=sum(T[(a,b)] for b in (0,2,4))
    print(a,[round(100*T[(a,b)]/tot,1) for b in (0,2,4)])

# §2 the dip against the gap-shuffled null
d=lambda s: collections.Counter(abs(s[i+1]-s[i]) for i in range(len(s)-1))
real=d(g); gs=list(g); random.shuffle(gs); null=d(gs); n=len(g)-1
for k in (2,4,6,8,10,12,14):
    print(k, round(100*real[k]/n,2), round(100*null[k]/n,2))
```

Full tables: [`repro/regenerate_tables.py`](repro/).

## References

- G. H. Hardy, J. E. Littlewood, *Partitio numerorum III* (1923).
- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS (2016).
