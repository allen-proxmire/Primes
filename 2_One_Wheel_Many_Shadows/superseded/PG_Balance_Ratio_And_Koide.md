# The balance ratio: consecutive primes, and where Koide sits

*Written 2026-09-18 with Claude, from Allen's Copilot exchange. Side note, not part of the ED ledger. Everything below is checked arithmetic or standard results; the honest verdict is at the end.*

## The quantity

For three positive numbers a, b, c:

> **K = (a² + b² + c²) / (a + b + c)²**, and its inverse **1/K = (a + b + c)² / (a² + b² + c²)**

Applied to consecutive primes p₁, p₂, p₃, it's the ratio that drifts toward 1/3 (inverse 3).

Koide's relation is **the same quantity applied to the square roots of the lepton masses:**

> **Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² ≈ 2/3**

So if the primes play the role of the square roots of masses, the two live on the same scale. That's why they're comparable at all.

## What K actually measures (exact)

Write the three numbers as a mean m times (1 + εᵢ), where the εᵢ are relative deviations that sum to zero. Then, exactly:

> **K = 1/3 + (ε₁² + ε₂² + ε₃²)/9**, and to first order **1/K ≈ 3 − (ε₁² + ε₂² + ε₃²)**

- **Checked** on 5, 7, 11: the identity gives 0.3686200378071833 against 195/529 = 0.3686200378071834.
- **So K is a spread measure,** nothing more: the squared relative spread of the three numbers, shifted by 1/3.
- **It knows nothing about primality.** Any three numbers that get relatively closer together will march toward 1/3.

## The geometric reading (why 45° turns up)

Put the three numbers in a vector and compare it with the "all equal" direction (1, 1, 1). Then

> **cos²θ = 1 / (3K)**

| K | 1/K | angle to the all-equal direction | meaning |
|---|---|---|---|
| **1/3** | 3 | 0° | all three equal |
| **2/3** | 1.5 | **45°** | **Koide** |
| **1** | 1 | 54.7356° | one number is everything |

- **Koide's 2/3 is exactly the 45° condition,** and it sits at the midpoint of K's allowed range [1/3, 1].
- **With measured lepton masses:** Q = 0.666661 and the angle is **44.9997°**.
- **This is the same 45° that shows up in the prime-triangle angles** ([PG_Angle_Wobble.md](PG_Angle_Wobble.md)), for a different reason: both are built from the same comparison of a sum of squares with a square of a sum. Shared coordinates, not a shared cause.

## Consecutive primes, computed

| triple | K | 1/K | 3 − 1/K | Σ(relative deviation)² | angle |
|---|---|---|---|---|---|
| 2, 3, 5 | 0.380000 | 2.63158 | 0.368421 | 0.420000 | 20.51° |
| 3, 5, 7 | 0.368889 | 2.71084 | 0.289157 | 0.320000 | 18.09° |
| 5, 7, 11 | 0.368620 | 2.71282 | 0.287179 | 0.317580 | 18.02° |
| 11, 13, 17 | 0.344438 | 2.90328 | 0.096718 | 0.099941 | 10.34° |
| 17, 19, 23 | 0.338696 | 2.95250 | 0.047498 | 0.048262 | 7.23° |
| 101, 103, 107 | 0.333526 | 2.99826 | 0.001736 | 0.001737 | 1.38° |
| 547, 557, 563 | 0.333380 | 2.99958 | 0.000423 | 0.000423 | 0.68° |
| 3581, 3583, 3593 | 0.333334 | 2.99999 | 0.000006 | 0.000006 | 0.08° |
| 17393, 17401, 17417 | 0.333333 | 3.00000 | 0.000001 | 0.000001 | 0.03° |

- **The fourth and fifth columns track each other,** as the identity says they must.
- **The approach to 3 is set by the gaps:** the distance from 3 is about the squared relative gaps, so it falls like (gap/p)², which is roughly (ln p / p)². At p ≈ 101 that predicts about 0.002, and the table shows 0.0017.
- **So this statistic is a gap measure in disguise,** and belongs with the gap work rather than apart from it.

## The verdict

**What's real:**
- The identity K = 1/3 + (relative spread)/9, exactly.
- Koide's 2/3 is the 45° condition, and the midpoint of the possible range.
- Consecutive primes march to the equality end (1/3, inverse 3), and the rate is governed by the gaps.

**What isn't:**
- **There's no prime–lepton connection here.** The primes head to the "nothing distinguishes them" corner; the leptons sit far from it, at 45°.
- **"2/3 is twice 1/3" isn't the meaningful fact.** The meaningful facts are the range [1/3, 1], the midpoint, and the angle.

**The question worth keeping,** in Copilot's framing and sharpened:
> 1/3 is where three quantities land when nothing distinguishes them. The leptons sit exactly halfway between that and "only one of them exists." **What picks the midpoint?**

**Caveats on Koide:** it holds to about one part in 10⁵ with measured pole masses and has no accepted explanation; masses run with energy scale, and the relation is not as clean at other scales, so whether 2/3 is fundamental is open.

## Generation time: the wheel as the state, the verdicts as the events

*Allen's framing: the numbers don't all exist yet; what arrives is the decision. Refined here.*

**An ordering alone isn't a dynamics.** "13 after 11" says nothing about 11 causing 13. Dynamics needs the current state to constrain what comes next. **The sieve has that, and the wheel is the state.**

| | in the sieve | what it is |
|---|---|---|
| **State at step k** | The surviving pattern of residues modulo p₁p₂…p_k | The wheel |
| **Event** | The next prime: the smallest survivor above 1 | A verdict, not a number coming into being |
| **Update** | Switching that prime on refines the wheel to the next primorial | The wheel turns over |

**The settled region and the frontier.**
- **Everything below p_k² is already decided** by the first k primes. That's the settled part.
- **The frontier advances like p_k², while the wheel's period grows like the primorial p₁p₂…p_k,** which is exponentially larger.
- **So the decided part of the line grows quadratically while the state needed to describe the rule explodes.** That gap is where the apparent randomness lives. It's Allen's "collecting new pegs at p²."

**Two corrections worth keeping.**
- **It's the verdicts that arrive, not the numbers.** Every integer is an address as soon as you can count to it. What happens in order is prime-or-composite.
- **The sieve's time sits outside the integers.** The number line doesn't grow; only the annotation does. In a growth model like ED, the pattern itself is what grows, and time is its own order. That's the real difference, sharper than "primes have no time."

**What this buys for the balance ratio.** In the generative reading, the distance from 1/3 is **how irregular the unfolding is near the frontier**, and its size is set by the gaps: it falls like (gap/p)², about (ln p / p)². **So irregularity relaxes as the wheel gains filters, without ever reaching equilibrium.**

**The measurable question** (open, and checkable in this repo): the drift toward 1/3 is guaranteed, so the content is in the **fluctuations around it.**
- Compute the deviation from 1/3 for every consecutive triple.
- **Divide out the (ln p / p)² trend.**
- Look at what's left, sorted by residue class modulo 6 and modulo 30.
- **The question:** does the leftover look like a random model predicts, or does it carry the wheel's fingerprints? The Lemke Oliver–Soundararajan bias in consecutive primes' last digits says the second is worth a look.

## Checked

| claim | how |
|---|---|
| The identity and the table | Computed 2026-09-18 (sieve to 20,000; the identity checked against the exact fraction for 5, 7, 11) |
| Koide's value and angle | Pole masses m_e = 0.51099895, m_μ = 105.6583755, m_τ = 1776.86 MeV: Q = 0.666661, angle 44.9997° |
| Range and geometry | cos²θ = 1/(3K); K = 1/3 at equality, 1 at full concentration (54.7356°) |
