# Reproducing the measured tables

```bash
python regenerate_tables.py                 # everything, ~6 min
python regenerate_tables.py --quick         # smaller range, ~1 min (numbers WILL differ)
python regenerate_tables.py --only windowed # one section
```

Needs `numpy`. Nothing else. Default range is $[10^6, 5\times10^6)$ — 270,015 primes — matching the papers.

## What it covers

| section | reproduces | status |
|---|---|---|
| `trap3` | [Differencing Trap](../Prime_Gap_Memory_Differencing_Trap.md) §3 | ✅ 4 of 5 rows — **see below** |
| `windowed` | [Differencing Trap](../Prime_Gap_Memory_Differencing_Trap.md) §5.1 | ✅ exact |
| `lag1` | [Angle Wobble](../PG_Angle_Wobble.md) §4.1 | ✅ plateau confirmed |
| `hexagon` | [Balance Ratio](../PG_Balance_Ratio_And_Koide.md) §2.1 | ✅ exact |
| `reduction` | [Balance Ratio](../PG_Balance_Ratio_And_Koide.md) §5 | ✅ within shuffle spread |
| `residue` | [Balance Ratio](../PG_Balance_Ratio_And_Koide.md) §6 | ✅ within seed spread |

**Not covered:** series 1, 3 and 5 have no reproducibility layer at all.

## One row does not reproduce — the jitter recoil

This is recorded rather than quietly adjusted, because catching it is the point of having the script.

[Differencing Trap §3](../Prime_Gap_Memory_Differencing_Trap.md) publishes:

| | real | null | genuine |
|---|---|---|---|
| jitter recoil, big → opposite sign | 81.8% | 79.2% | **+2.7 pp** |

This script gets **84.0% real, 84.5% null, −0.5 pp** — a different magnitude, and the genuine column changes sign, turning a small claimed effect into no effect.

**Most likely cause: the original implementation is unspecified.** "After a large jitter" needs three choices the paper does not state — the threshold (this script uses the top decile of $|\Delta g|$), whether "opposite sign" is measured against the triggering jitter or the previous one, and how exact zeros are handled. Different reasonable choices give materially different numbers.

**What this does and does not cast doubt on.** The recoil row was never load-bearing: §4 shows that recoil is *forced* by the exact $-\tfrac12$ differencing identity, and §3's own conclusion calls it "almost entirely artifact." This script agrees more strongly than the paper did — it finds the recoil entirely artifact. **So the discrepancy pushes toward the paper's conclusion, not away from it.** Nothing downstream depends on the $+2.7$ pp.

**Open:** recover the original definition, or drop the row's "genuine" column in favour of "artifact, magnitude implementation-dependent." Logged in [`NOTES_Carry_Forward.md`](../NOTES_Carry_Forward.md).

## Notes on the numbers

- **Seeds matter more than they look.** Surrogate results move by a few tenths of a percentage point between seeds; the script averages three. A single seed once showed a $2.1\sigma$ "residual" that vanished on a sweep.
- **Pool ratios are printed on every surrogate row**, and rows below $\approx1.25$ are marked `CIRCULAR`. At $Q\to\sqrt{x}$ the surrogate *is* the primes and the comparison means nothing. Read the status column before the result column. See [*The Null-Model Discipline*](../Null_Model_Discipline.md) §4.
- **`--quick` changes the answers**, not just the runtime: a smaller range moves $\sqrt{x}$, so circularity bites at a lower $Q$. Use it to check the script runs, never to check a published number.
- **In-sample $R^2$** throughout, matching the papers. These are descriptive comparisons against a matched null, not out-of-sample predictions.
