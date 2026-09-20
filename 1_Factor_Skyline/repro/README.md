# Reproducing the Factor Skyline numbers

```bash
python entropy_budget.py      # ~2 min, standard library only
```

## Why this exists

The upstream repo has a `reproducibility/tables/` tree with nine scripts named after the paper tables — `table_06_entropy_budget.py` and friends. **They are stubs.** Each is 28 lines and returns, in its own words, "a dictionary with deterministic placeholder values… this structure will later be replaced with real computations." Nothing in it computes anything.

So the collection's most-quoted numbers had no working reproduction. This script is the real one, for the entropy budget at least.

## What it found

**All four published numbers reproduce exactly — at N = 10⁴.**

| | script | FSPapers_03 §3.7 |
|---|---|---|
| H(dx) | 2.4827 | 2.48 |
| template | 1.6999 | 1.70 |
| escape | 0.2653 | 0.26 |
| activation | 0.5175 | 0.52 |

**But the range is not stated in the papers, and the components do not scale alike:**

| N | H(dx) | template | escape | activation | wheel share |
|---|---|---|---|---|---|
| 1,000 | 2.2011 | 1.6941 | 0.2536 | 0.2533 | 77.0% |
| **10,000** | **2.4827** | **1.6999** | **0.2653** | **0.5175** | **68.5%** |
| 100,000 | 2.7080 | 1.7000 | 0.2513 | 0.7568 | 62.8% |
| 1,000,000 | 2.8894 | 1.6998 | 0.2331 | 0.9565 | 58.8% |
| 3,000,000 | 2.9642 | 1.6998 | 0.2248 | 1.0396 | 57.3% |

- **template is rock stable at 1.70** — a genuine invariant of the 5#-wheel, and the number the collection leans on hardest.
- **escape peaks near 10⁴** and declines slowly. The paper's "≈0.26 bits (its peak)" is literally right; the parenthesis was doing more work than it looked.
- **activation grows without bound** — it counts *which* least prime factor a composite has, and there are more distinct values as N grows.
- **H(dx) therefore grows too**, dragged up by activation alone.

## What that does and doesn't undermine

**Does not undermine:** the 1.70 bits. That is stable to four decimal places across three orders of magnitude, and it is what the wheel actually buys.

**Does undermine, mildly:** the framing *"1.70 of 2.48 — about 68% of everything knowable."* That ratio holds at N = 10⁴. At 10⁶ it is 59%, and it keeps falling — **not because the wheel weakens but because the denominator grows.**

**The sharper point:** "activation" — which lpf a composite has — is irrelevant to locating the next prime, which needs only prime/not-prime. Including it inflates the denominator with information nobody was trying to acquire. The quantity that actually bears on the [Prediction Budget](../../2_One_Wheel_Many_Shadows/Prime_Prediction_Budget.md)'s question is the binary one:

> the wheel kills **73.3%** of positions for free (22/30), and an open slot still carries **0.84 bits** of genuine uncertainty.

That framing is stable and needs no range attached.

## Not covered

Everything else in series 1 — coverage protection, template persistence, the correlation and universality theorems, Erdős–Kac and the divisor averages. Those are derivations rather than measurements, but the numerical claims among them are unverified here.
