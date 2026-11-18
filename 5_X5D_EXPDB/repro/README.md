# Reproduction — X5D

```bash
python check_x5d_arithmetic.py    # standard library, instant; exits non-zero on any failure
```

Checks every closed-form number in [X5D](../X5D.md) as exact rational arithmetic:

| section | checked |
|---|---|
| §6.1 | Ingham and Guth–Maynard meet at $\sigma=\frac{7}{10}$ with height $\frac{30}{13}$; $\theta_{\mathrm{PNT}}\le\frac{17}{30}$, $\theta_{\mathrm{PNT\text{-}AA}}\le\frac{2}{15}$, sensitivity $\frac{169}{900}$; the Ingham–Huxley crossing at $\frac34$, height $\frac{12}{5}$ |
| §6.2 | the exponent pair $(\frac{1}{100},\frac{14}{15})$; Bourgain's conditions and threshold $\frac{290}{303}$; the closed forms of $\alpha$ and $\beta$; $\alpha(\frac{59}{60})=\frac{16043}{11670}$; $\lim\alpha=\frac{33}{23}$ against $\frac32$; $\beta<\alpha$ |

Not reproduced here: the region $\mathcal P$ itself and the database's envelopes, which need the database code ([teorth.github.io/expdb](https://teorth.github.io/expdb/)). The value $\approx1.375$ on $[\frac{41}{42},\frac{59}{60})$ quoted in §6.2 is from a database run.
