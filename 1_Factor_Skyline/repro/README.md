# Reproduction — Factor Skyline

```bash
python entropy_budget.py      # ~2 min, standard library only
```

Computes the information budget of the step sequence $dx(n)$ ([Factor Skyline §5](../Factor_Skyline.md)):

| N | H(dx) | template | escape | activation | template share |
|---|---|---|---|---|---|
| 1,000 | 2.2011 | 1.6941 | 0.2536 | 0.2533 | 77.0% |
| 10,000 | 2.4827 | 1.6999 | 0.2653 | 0.5175 | 68.5% |
| 100,000 | 2.7080 | 1.7000 | 0.2513 | 0.7568 | 62.8% |
| 3,000,000 | 2.9642 | 1.6998 | 0.2248 | 1.0396 | 57.3% |

The template is stable; activation grows; the share is range-specific. The prime/not-prime quantity that bears on prediction is stable: the mod-30 wheel removes 73.3% of positions and an open slot carries $\approx 0.84$ bits.

```bash
python active_template.py     # under a minute, numpy + matplotlib
```

Draws `figures/FS_active_template.png` and runs the fair-template test of [Factor Skyline §4](../Factor_Skyline.md): neighbouring windows of wide-column length at $5\times10^6$–$5\times10^7$ correlate −0.26 ($10^5$) and −0.31 ($2\times10^5$), against −0.08 to +0.21 for templates to 13–41 (20 seeds each, pool ratio printed).
