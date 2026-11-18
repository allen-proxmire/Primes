# Seven Sisters

### Primes from the doubled scale $2p + k$, and why the wheel decides which offsets win

Allen Proxmire

---

## 1. The offsets

The **Seven Sisters** are the offsets
$$k \in \{+1,\ +3,\ -3,\ -5,\ +7,\ +9,\ -9\}$$
applied to $2p$ for a prime $p$. Offset $k$ **covers** $p$ if $2p + k$ is prime; a set covers $p$ if some member does. Offsets are odd, since $2p$ is even. (The original note and data: [seven-sisters](https://github.com/allen-proxmire/seven-sisters).)

---

## 2. The wheel decides eligibility

**Lemma 2.1.** For a prime $p > 3$:
- if $3 \mid k$, then $3 \nmid 2p + k$;
- if $15 \mid k$ and $p > 5$, then neither 3 nor 5 divides $2p + k$.

*Proof.* $2p \not\equiv 0 \pmod 3$ for $p > 3$, and adding $k \equiv 0$ keeps it so; likewise mod 5 for $p > 5$. $\square$

An offset with $3 \nmid k$ is forced composite for about half of all primes (those with $2p + k \equiv 0 \pmod 3$). So offsets divisible by 3 hit primes about **twice** as often, and multiples of 15 more often still:

| offset class | killed by 3? | killed by 5? | eligible share |
|---|---|---|---|
| $15 \mid k$ ($\pm15, \pm45, \pm75$) | never | never | highest |
| $3 \mid k$, $5 \nmid k$ ($\pm21, \pm63$) | never | $\approx \tfrac14$ of $p$ | middle |
| $3 \nmid k$ ($+1, -5, +7$) | $\approx \tfrac12$ of $p$ | some | lowest |

Among the seven, $\pm3$ and $\pm9$ are the strong members; $+1, -5, +7$ are the conditional ones.

---

## 3. Coverage falls with scale

| prime band | covered by the seven | largest $\lvert k\rvert$ needed | mean $\lvert k\rvert$ |
|---|---|---|---|
| $10^3$–$3\times10^3$ | 91.60% | 15 | 3.59 |
| $10^4$–$3\times10^4$ | 83.68% | 29 | 4.42 |
| $10^5$–$3\times10^5$ | 73.99% | 51 | 5.70 |
| $10^6$–$3\times10^6$ | 67.32% | 73 | 6.79 |
| $10^7$–$3\times10^7$ | 61.52% | 99 | 7.89 |

The mean offset needed grows like $\ln 2p$, the average distance from $2p$ to the nearest prime; the largest grows like the maximal local gap, $\sim(\ln 2p)^2$.

**No finite offset set covers every prime.** A set with largest offset $M$ misses $p$ whenever $[2p - M,\ 2p + M]$ holds no prime, and prime gaps are unbounded. (That such $2p$ actually occur for every $M$ is certain in practice but not proved here; it is of the same character as the wide-gap problem in [Consecutive-Prime Sums §4](Consecutive_Prime_Sums.md).) 100% is an asymptote.

---

## 4. Climbing along the wheel

Greedy additions beyond the seven (primes to $2\times10^6$) are exactly the eligibility order — multiples of 15 first, then multiples of 3; the conditionals never appear:

| add | coverage | | add | coverage |
|---|---|---|---|---|
| (the seven) | 70.29% | | $-75$ | 95.46% |
| $+15$ | 78.25% | | $-21$ | 96.54% |
| $-15$ | 84.21% | | $+21$ | 97.39% |
| $+45$ | 88.46% | | $+63$ | 98.04% |
| $-45$ | 91.61% | | $-63$ | 98.54% |
| $+75$ | 93.85% | | $-39$ | 98.88% |
| | | | $-27$ | 99.14% |

A dozen additions reach 99%. For comparison, using *every* odd offset within $\pm M$:

| $M$ | 9 | 15 | 21 | 31 | 45 | 63 |
|---|---|---|---|---|---|---|
| coverage | 81.5% | 94.3% | 98.0% | 99.6% | 99.98% | 100% on this sample |

The natural extended family is the odd multiples of 3, weighted toward 15 and 105:
$$\{\pm3, \pm9, \pm15, \pm21, \pm27, \pm33, \pm39, \pm45, \pm63, \pm75, \pm105, \dots\}.$$

Doubling picks the neighbourhood; the wheel picks the winners. Verified by sieve to $6\times10^7$.

---

## Reproduction

```python
def sieve(n):
    b = bytearray([1])*(n+1); b[0]=b[1]=0; i=2
    while i*i <= n:
        if b[i]: b[i*i::i] = bytearray(len(b[i*i::i]))
        i += 1
    return b
B = sieve(60_000_000)
sisters = [1, 3, -3, -5, 7, 9, -9]
covers = lambda p, K: any(B[2*p+k] for k in K)
def nearest(p):
    x = 2*p; du = 1
    while not B[x+du]: du += 1
    dd = 1
    while not B[x-dd]: dd += 1
    return min(du, dd)
for lo, hi in [(10**3,3*10**3),(10**6,3*10**6),(10**7,3*10**7)]:
    ps = [i for i in range(lo, hi) if B[i]]
    print(lo, f"{100*sum(covers(p,sisters) for p in ps)/len(ps):.2f}%", max(map(nearest, ps)))
```

## References

- A. M. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experimental Math. **8** (1999).
