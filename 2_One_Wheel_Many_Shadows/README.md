# 2 — One Wheel, Many Shadows

**The main arc.** The primorial wheel — equivalently the Hardy–Littlewood singular series — generates every gap phenomenon measured here, and the same wheel sets how close the next prime can be pinned.

**Start with:** [One Wheel, Many Shadows](One_Wheel_Many_Shadows.md) — the thesis and its audit: ten probes, six independent, four provably the same quantity in other notation, no residual.

**The wheel and the gaps**

| file | result |
|---|---|
| [Switchback Law](Switchback_Law.md) | consecutive gaps never both $\equiv2$ nor both $\equiv4 \pmod 6$ |
| [Consecutive-Prime Sums](FS_Consecutive_Prime_Sums_In_Gaps.md) | forbidden widths $\{2,4,6,10\}$; density $W/(2\ln(x/2))$ |
| [Offset-Correlation Curve](Offset_Correlation_Curve.md) | $C(g)/C(2)=\prod_{p\mid g,p>2}\frac{p-1}{p-2}$ to ~1% |
| [Prime Structure Factor](Prime_Structure_Factor.md) ([pdf](Prime_Structure_Factor.pdf)) | Bragg peaks of height $(\mu(m)/\varphi(m))^2$ |
| [ED as the Negative Control](ED_Negative_Control.md) | non-arithmetic exclusion diffracts as a liquid |
| [Seven Sisters](FS_Seven_Sisters_Wheel_Asymptote.md) | $2p+k$ with $3\mid k$ hits primes ~2× as often; climb along multiples of 15 |
| [Angle Wobble](PG_Angle_Wobble.md) | $\alpha_n\approx45°-\frac{90}{\pi}\frac{g_n}{p_{n+1}}$; the lag-1 $-0.05$ is the wheel |
| [Differencing Trap](Prime_Gap_Memory_Differencing_Trap.md) | gap "weather" is differencing; the $+1.97$ pp residue is the wheel |
| [Balance Ratio and Koide](PG_Balance_Ratio_And_Koide.md) | $K-\frac13=\frac{2}{27}\frac{g_1^2+g_1g_2+g_2^2}{m^2}$; no prime–lepton link |
| [2p Bracket Construction](FS_2p_Bracket_Construction.md) | sum = average; mirror law; doubling ladders |
| [Escape Ridge](FS_Escape_Ridge.md) | $x_{FS}(N)\sim4e^{-\gamma}N^{3/2}/\ln^2N$ |
| [Synthesis](FS_Synthesis_Doubling_and_Wheel.md) | doubling as the top ray, the wheel as the fan |

**Predicting the next prime**

| file | result |
|---|---|
| [The Ninety Percent Rule](The_Ninety_Percent_Rule.md) | slots for 90%: $3\ldots11$ over $10^3\ldots10^{10}$, predicted by $q=4.375/\ln N$ |
| [Prime Prediction Budget](Prime_Prediction_Budget.md) | $2.48$ bits: template $1.70$, escape $0.26$; the wall |

**Method**

| file | contents |
|---|---|
| [The Null-Model Discipline](Null_Model_Discipline.md) | five ways to fool yourself with a null, and the checklist |

**Reproduction:** [`repro/`](repro/) regenerates every measured table in the gap papers (`regenerate_tables.py`) and the ninety-percent and look-back results (`ninety_percent_table.py`, `lookback_test.py`). Figures in [`figures/`](figures/).
