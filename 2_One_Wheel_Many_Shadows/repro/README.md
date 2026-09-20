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
| `trap3` | [Differencing Trap](../Prime_Gap_Memory_Differencing_Trap.md) §3 | ✅ all 5 rows — one **corrected the paper**, see below |
| `windowed` | [Differencing Trap](../Prime_Gap_Memory_Differencing_Trap.md) §5.1 | ✅ exact |
| `lag1` | [Angle Wobble](../PG_Angle_Wobble.md) §4.1 | ✅ plateau confirmed |
| `hexagon` | [Balance Ratio](../PG_Balance_Ratio_And_Koide.md) §2.1 | ✅ exact |
| `reduction` | [Balance Ratio](../PG_Balance_Ratio_And_Koide.md) §5 | ✅ within shuffle spread |
| `residue` | [Balance Ratio](../PG_Balance_Ratio_And_Koide.md) §6 | ✅ within seed spread |

**Not covered:** series 1, 3 and 5 have no reproducibility layer at all.

## One row did not reproduce — and the paper was wrong

Recorded because catching this is the whole point of having the script.

[Differencing Trap §3](../Prime_Gap_Memory_Differencing_Trap.md) used to publish **81.8% real / 79.2% null / +2.7 pp genuine** for the jitter recoil. Measured consistently, there is **no genuine effect**.

**Thirty definitions were tested** — thresholds at the top decile, quintile, quartile and 5%; at one and two standard deviations; at fixed cutoffs |Δg| ≥ 12, 18, 24, 30 — each with three rules for exact zeros.

- Several reproduce the published **real** value (81.7% top quintile, 81.6% top quartile).
- Several reproduce the published **null** value (79.2–79.3% at one sd, or |Δg| ≥ 12).
- **None reproduces both**, and all thirty give a genuine column between −0.7 and +0.2 pp.

So the published pair was almost certainly computed at **two different thresholds** — likely the null added after the fact. The paper's row now reads ≈81.7% / ≈81.8% / ≈0 (artifact), and the script uses the top quintile.

**This strengthened the paper.** §4 proves recoil is *forced* by the exact −½ identity; it should be pure artifact, and now it reports as one.

### The same check broke a second paper

Running the matched null on the sign structure showed that [*The Switchback Law*](../Switchback_Law.md) compares its run-length distribution against **a fair coin** — the wrong baseline, for exactly the reason the Differencing Trap exists. Against the gap-shuffled null the effect vanishes: real 64.00/27.25/7.18/1.34% versus null 64.66/27.31/6.74/1.13%. That paper now carries a warning box and needs revision. Its §5 mod-6 result is unaffected.

## Notes on the numbers

- **Seeds matter more than they look.** Surrogate results move by a few tenths of a percentage point between seeds; the script averages three. A single seed once showed a $2.1\sigma$ "residual" that vanished on a sweep.
- **Pool ratios are printed on every surrogate row**, and rows below $\approx1.25$ are marked `CIRCULAR`. At $Q\to\sqrt{x}$ the surrogate *is* the primes and the comparison means nothing. Read the status column before the result column. See [*The Null-Model Discipline*](../Null_Model_Discipline.md) §4.
- **`--quick` changes the answers**, not just the runtime: a smaller range moves $\sqrt{x}$, so circularity bites at a lower $Q$. Use it to check the script runs, never to check a published number.
- **In-sample $R^2$** throughout, matching the papers. These are descriptive comparisons against a matched null, not out-of-sample predictions.
