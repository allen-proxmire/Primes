# The Next Twin

### Which wheel to roll so the next twin pair turns up in its first turn

Allen Proxmire

---

## Summary

Stand on a prime $p$ and roll a wheel of size $W$ forward from it. The chance that the next twin pair falls within the first turn is
$$1 - e^{-W\cdot 2C_2/\ln^2 p}, \qquad C_2 = 0.6601\ldots,$$
so a chance $s$ needs
$$W \;\ge\; \frac{-\ln(1-s)}{2C_2}\,\ln^2 p, \qquad \text{for 90\%:}\quad W \ge 1.74\,\ln^2 p .$$
The wheel has to grow to hold the same chance, but only like $\ln^2 p$, while the wheel sizes multiply by the next prime at each step. Each wheel therefore lasts enormously longer than the one before:

| next twin within one turn | 30-wheel | 210-wheel | 2,310-wheel | 30,030-wheel | 510,510-wheel |
|---|---|---|---|---|---|
| **90%** | to ~60 | to **~60,000** | to **~6 × 10¹⁵** | to ~10⁵⁷ | to ~10²³⁵ |
| 99% | to ~20 | to ~2,500 | to ~10¹¹ | to ~10⁴⁰ | to ~10¹⁶⁶ |
| 50% | to ~2,000 | to ~5 × 10⁸ | to ~10²⁹ | to ~10¹⁰⁴ | to ~10⁴²⁸ |

The 2,310-wheel is the 90% wheel for every prime that can be listed.

The ingredients are classical (Hardy–Littlewood's twin density $2C_2/\ln^2 x$ and the exponential spacing of rare events). What is added is the calibration: the rule in wheel terms, checked against every prime to $4\times10^7$. The companion for single primes is [Predicting the Next Prime](Predicting_the_Next_Prime.md).

---

## 1. The rule

Twin pairs near $p$ arrive at an average spacing of
$$\bar g_2 = \frac{\ln^2 p}{2C_2}$$
(about 145 near $10^6$, 197 near $10^7$), and the wait from a prime to the next pair behaves like a wait between random arrivals at that rate: the usual wait is $\ln 2\cdot\bar g_2 \approx 0.53\ln^2 p$. A turn of length $W$ therefore misses with chance
$$f = e^{-W/\bar g_2} = e^{-W\cdot 2C_2/\ln^2 p},$$
and holds the next twin with chance $1 - f$. Setting $1 - f \ge s$ gives the rule.

The same rule for single primes, with average spacing $\ln p$, reads $W \ge 2.30\ln p$ for 90%: the 30-wheel holds the next prime in one turn to $\approx 4.5\times10^5$ (seen 94.1% there against 90.0% predicted — gaps are less spread than random arrivals), the 210-wheel to $\approx10^{39}$.

## 2. Checked against the primes

Share of primes whose next twin pair lies within one turn:

| $p$ near | wheel | seen | predicted | primes |
|---|---|---|---|---|
| 2,500 | 210 | 100% | 98.9% | 164 |
| 50,000 | 210 | **90.6%** | **90.6%** | 2,435 |
| 100,000 | 210 | 91.1% | 87.7% | 4,597 |
| 1,000,000 | 210 | 79.4% | 76.6% | 38,346 |
| 10,000,000 | 210 | 66.5% | 65.6% | 328,837 |
| 10,000,000 | 2,310 | 100.0% | 100.0% | 328,837 |

The 210-wheel holds 90% up to about $5\times10^4$–$10^5$, as the rule says; the rule runs slightly cautious, real twins doing a little better.

## 3. Turn by turn

When the first turn misses, each later turn holds the same fraction of what is left:
$$\text{share in turn } k = (1-f)\,f^{\,k-1}.$$

| $p$ near | turn 1 | turn 2 | turn 3 | turn 4 |
|---|---|---|---|---|
| $10^5$ | 89.8% (87.7%) | 8.9% (10.8%) | 1.1% (1.3%) | 0.1% (0.2%) |
| $10^6$ | 78.6% (76.6%) | 17.6% (17.9%) | 3.1% (4.2%) | 0.7% (1.0%) |
| $10^7$ | 66.1% (65.6%) | 23.1% (22.6%) | 7.4% (7.8%) | 2.4% (2.7%) |

(210-wheel; predicted in brackets.) The first turn is always the most likely, and loses ground as $p$ grows: it falls below half near $p \approx 10^9$, where the average spacing passes 300.

## 4. Where in the turn

The 210-wheel has fifteen twin slots (11, 17, 29, 41, 59, 71, 101, 107, 137, 149, 167, 179, 191, 197, 209). All twins split evenly among them; the *first* twin after a prime leans slightly toward the slots that follow the long twin-free runs of the turn (71→101, 107→137) — 7.1% at 179 against 6.3% at 29, for primes $10^3$–$4\times10^7$ — because those slots have more open spokes, and so more primes, behind them. The lean fades as $p$ grows and more of the turn is crossed before the next twin arrives.


## 5. Why the window is never empty

Between $p$ and $2p$ lie about $p/\ln p$ primes, and from each a small wheel finds a twin within one turn 90% of the time. The chances from neighbouring primes overlap — a prime a few steps past one that missed shares almost the same stretch — so the honest count uses separate turns: $(p, 2p]$ holds $p/W$ of them, each missing with chance $f = e^{-W\cdot2C_2/\ln^2 p}$, and all of them miss with chance
$$f^{\,p/W} = e^{-\,p\cdot 2C_2/\ln^2 p} = e^{-E},$$
where $E$ is the expected number of twins in the window. The wheel size cancels.

| $p$ | 101 | 1,009 | 10,007 | 1,000,003 |
|---|---|---|---|---|
| expected twins in $(p, 2p]$, $E = 2C_2\sum_{p<t\le 2p} 1/\ln^2 t$ | 5.4 | 25.0 | 143.6 | 6,550 |
| actual | 6 | 26 | 136 | 6,702 |
| chance of none if twins arrived at random, $e^{-E}$ | $10^{-2.3}$ | $10^{-10.9}$ | $10^{-62}$ | $10^{-2845}$ |

This is the Hardy–Littlewood heuristic in wheel terms, and it is why [Twin Bertrand](../3_Twin_Bertrand_Prime_Geometry/Twin_Bertrand.md) is expected to hold. It is not a proof: the density $2C_2/\ln^2 p$ is itself the Hardy–Littlewood conjecture, and the primes are fixed, not random — a proof has to exclude every arrangement in which they dodge a window, which is the parity barrier.

---

## Reproduction

[`repro/twin_wheel_rule.py`](repro/twin_wheel_rule.py) — §1–§3 against every prime to $4\times10^7$ (numpy, ~30 s).

## References

- G. H. Hardy, J. E. Littlewood, *Some problems of 'Partitio numerorum' III*, Acta Math. **44** (1923).
