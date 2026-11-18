# Reproduction — One Wheel, Many Shadows

```bash
python regenerate_tables.py                 # all gap tables, ~6 min (numpy)
python regenerate_tables.py --quick         # smaller range, ~1 min — numbers will differ
python regenerate_tables.py --only windowed # one section
python ninety_percent_table.py              # the 90% table, 10^3 to 10^10 (standard library)
python lookback_test.py                     # the look-back test (numpy)
```

Default range $[10^6, 5\times10^6)$, 270,015 primes.

| section | reproduces |
|---|---|
| `trap3` | [Gap Correlations §4](../Gap_Correlations.md) — gap memory against the matched null |
| `windowed` | [Gap Correlations §4](../Gap_Correlations.md) — the windowed excess against wheel surrogates |
| `lag1` | [Gap Correlations §3](../Gap_Correlations.md) — the lag-1 plateau |
| `hexagon` | [Gap Correlations §5.2](../Gap_Correlations.md) — the Eisenstein 3-divisibility |
| `reduction` | [Gap Correlations §5.3](../Gap_Correlations.md) — the covariance reduction |
| `residue` | [Gap Correlations §5.3](../Gap_Correlations.md) — residue classes |
| `ninety_percent_table.py` | [Predicting the Next Prime §2–§3, §8](../Predicting_the_Next_Prime.md) |
| `lookback_test.py` | [Predicting the Next Prime §7](../Predicting_the_Next_Prime.md) |

Surrogate rows print their pool ratio and are marked `CIRCULAR` below $\approx 1.25$; results are averaged over three seeds. `--quick` moves $\sqrt x$ and so changes the answers. $R^2$ values are in-sample, as in the papers. `verify_full.txt` is a saved full run.
