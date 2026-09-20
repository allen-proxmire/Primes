#!/usr/bin/env python3
"""Generate the two X5D figures as SVG.

    python gen_svg.py

  fig1_dimension_ladder.svg   the schematic specified but never drawn in
                              X5D_EXPDB_Reinterpretation.md ("[Figure 1: The
                              dimension ladder and upstream generators.]")
  fig2_guth_maynard_cusp.svg  the binding constraint: Ingham (1940) meeting
                              Guth-Maynard (2024) at sigma = 7/10

Everything plotted is exact rational arithmetic, verified before drawing:
    A_Ingham(s) = 3/(2-s)          rising limb, binding on [1/2, 7/10)
    A_GM(s)     = 15/(5s+3)        falling limb, binding on [7/10, 19/25)
    A_Ing(7/10) = A_GM(7/10)       = 30/13          exactly
    theta       = 1 - 1/||A||      = 17/30          exactly
    dtheta/dA   = 1/||A||^2        = 169/900        exactly

SVG is used rather than PNG so the figures are text, diffable, and render
natively on GitHub -- consistent with the collection going markdown-native.
A light background panel is drawn explicitly so the figures stay legible
in both light and dark themes.

Standard library only.
"""
from fractions import Fraction as F

BG, FG, MUTE = "#fbfbfd", "#1c1c22", "#6b6b78"
BLUE, RED, GREEN = "#2f6fb5", "#c0442e", "#2e7d5b"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=13, fill=FG, anchor="middle", weight="normal", style="normal"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="Georgia,serif" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}" font-style="{style}">{esc(s)}</text>')


def box(x, y, w, h, label, sub=None, stroke=FG, fill="none"):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" '
         f'fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>']
    if sub:
        o.append(txt(x + w/2, y + h/2 - 3, label, 14, FG, weight="bold"))
        o.append(txt(x + w/2, y + h/2 + 13, sub, 11, MUTE))
    else:
        o.append(txt(x + w/2, y + h/2 + 5, label, 14, FG, weight="bold"))
    return o


def arrow(x1, y1, x2, y2, label=None, side="right", color=FG):
    o = [f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
         f'stroke="{color}" stroke-width="1.4" marker-end="url(#ah)"/>']
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if side == "right":
            o.append(txt(mx + 8, my + 4, label, 12, color, anchor="start", style="italic"))
        else:
            o.append(txt(mx - 8, my + 4, label, 12, color, anchor="end", style="italic"))
    return o


DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{FG}"/></marker></defs>')


# ----------------------------------------------------------------- figure 1

def figure1():
    W, H = 860, 560
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS,
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']

    o.append(txt(W/2, 34, "The dimension ladder, and where the constraints come from", 17, FG, weight="bold"))
    o.append(txt(W/2, 54, "X5D — every EXPDB bound is a shadow of one five-dimensional region", 12, MUTE))

    # left column: descending chain
    bx, bw, bh = 120, 230, 52
    ys = [90, 182, 274, 366, 458]
    o.append(txt(bx + bw/2, 78, "DOWNSTREAM — bounds flow out", 11, MUTE, weight="bold"))
    specs = [("𝒫 ⊂ ℝ⁵", "the master region (LVER)"),
             ("R ⊂ ℝ³", "large-value / energy region"),
             ("f(σ)", "a rational function"),
             ("f*(σ)", "the lower envelope"),
             ("θ ∈ ℝ⁰", "one number")]
    for (lab, sub), y in zip(specs, ys):
        o += box(bx, y, bw, bh, lab, sub, stroke=BLUE if y == ys[0] else FG)
    labels = ["π   (drop coordinates)", "sup_τ ρ/τ", "env⁻   (pointwise min)", "sup_σ"]
    for i, lab in enumerate(labels):
        o += arrow(bx + bw/2, ys[i] + bh, bx + bw/2, ys[i+1] - 4, lab, "right", MUTE)

    # right column: upstream generators
    gx, gw, gh = 560, 200, 46
    gys = [150, 226, 302]
    o.append(txt(gx + gw/2, 78, "UPSTREAM — constraints flow in", 11, MUTE, weight="bold"))
    gens = [("𝒞_EP ⊂ ℝ²", "exponent pairs", "ep_to_lver"),
            ("β* ⊂ ℝ¹", "beta envelope", "beta_to_zlv"),
            ("𝒞_μ ⊂ ℝ²", "mu hull", "mu_to_zlv")]
    for (lab, sub, fn), y in zip(gens, gys):
        o += box(gx, y, gw, gh, lab, sub, stroke=GREEN)
        o.append(f'<path d="M {gx} {y+gh/2} C {gx-70} {y+gh/2}, '
                 f'{bx+bw+70} {ys[0]+bh/2}, {bx+bw+6} {ys[0]+bh/2}" '
                 f'fill="none" stroke="{GREEN}" stroke-width="1.3" '
                 f'stroke-dasharray="4 3" marker-end="url(#ah)"/>')
        o.append(txt(gx - 14, y + gh/2 - 6, fn, 10, GREEN, anchor="end", style="italic"))

    o.append(txt(gx + gw/2, 372, "these sit in ℝ², below 𝒫 — but they feed", 11, MUTE))
    o.append(txt(gx + gw/2, 388, "UP into it, not down from it", 11, MUTE, weight="bold"))

    o.append(txt(W/2, 524, "Drawn 2026-09-20 from the figure specification in X5D_EXPDB_Reinterpretation.md §1.", 10, MUTE))
    o.append('</svg>')
    return "\n".join(o)


# ----------------------------------------------------------------- figure 2

def figure2():
    W, H = 860, 560
    L, R_, T, B = 95, 700, 95, 430
    s0, s1 = F(1, 2), F(39, 50)          # sigma axis 0.50 .. 0.78
    a0, a1 = F(195, 100), F(238, 100)    # A axis 1.95 .. 2.38

    def px(s): return L + (float(s) - float(s0)) / (float(s1) - float(s0)) * (R_ - L)
    def py(a): return B - (float(a) - float(a0)) / (float(a1) - float(a0)) * (B - T)

    ing = lambda s: F(3, 1) / (2 - s)
    gm = lambda s: F(15, 1) / (5 * s + 3)
    star, peak = F(7, 10), F(30, 13)
    assert ing(star) == gm(star) == peak
    assert 1 - 1 / peak == F(17, 30)
    assert 1 / peak**2 == F(169, 900)

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS,
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']
    o.append(txt(W/2, 34, "The binding constraint: a cusp at σ = 7/10", 17, FG, weight="bold"))
    o.append(txt(W/2, 54, "Ingham (1940) meets Guth–Maynard (2024). Where they cross fixes the prime-gap exponent.", 12, MUTE))
    o.append(txt(W/2, 72, "A(σ) — the zero-density exponent. Its peak is all that matters.", 11, MUTE, style="italic"))

    # grid
    for k in range(5, 9):
        s = F(k, 10) if k < 8 else F(78, 100)
        if s > s1: continue
        o.append(f'<line x1="{px(s):.1f}" y1="{T}" x2="{px(s):.1f}" y2="{B}" stroke="#e4e4ec" stroke-width="1"/>')
        o.append(txt(px(s), B + 20, f"{float(s):.2f}", 11, MUTE))
    for v in (2.0, 2.1, 2.2, 2.3):
        o.append(f'<line x1="{L}" y1="{py(F(int(v*100),100)):.1f}" x2="{R_}" y2="{py(F(int(v*100),100)):.1f}" stroke="#e4e4ec" stroke-width="1"/>')
        o.append(txt(L - 12, py(F(int(v*100), 100)) + 4, f"{v:.1f}", 11, MUTE, anchor="end"))
    o.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{B}" stroke="{FG}" stroke-width="1.3"/>')
    o.append(f'<line x1="{L}" y1="{B}" x2="{R_}" y2="{B}" stroke="{FG}" stroke-width="1.3"/>')
    o.append(txt((L+R_)/2, B + 44, "σ", 14, FG, style="italic"))
    o.append(txt(L - 46, (T+B)/2, "A(σ)", 14, FG, style="italic"))

    # limbs
    n = 120
    pts = [f"{px(s0 + (star-s0)*F(i,n)):.1f},{py(ing(s0 + (star-s0)*F(i,n))):.1f}" for i in range(n+1)]
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>')
    pts = [f"{px(star + (s1-star)*F(i,n)):.1f},{py(gm(star + (s1-star)*F(i,n))):.1f}" for i in range(n+1)]
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{RED}" stroke-width="2.6"/>')

    # continuations, dashed — each curve is NOT binding here
    pts = [f"{px(star + (s1-star)*F(i,n)):.1f},{py(ing(star + (s1-star)*F(i,n))):.1f}" for i in range(n+1)]
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.5"/>')
    pts = [f"{px(s0 + (star-s0)*F(i,n)):.1f},{py(gm(s0 + (star-s0)*F(i,n))):.1f}" for i in range(n+1)]
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{RED}" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.5"/>')

    # the cusp
    cx, cy = px(star), py(peak)
    o.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx:.1f}" y2="{B}" stroke="{FG}" stroke-width="1" stroke-dasharray="3 3"/>')
    o.append(f'<line x1="{L}" y1="{cy:.1f}" x2="{cx:.1f}" y2="{cy:.1f}" stroke="{FG}" stroke-width="1" stroke-dasharray="3 3"/>')
    o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5.5" fill="{FG}"/>')
    o.append(txt(cx + 14, cy - 26, "‖A‖∞ = 30/13", 14, FG, anchor="start", weight="bold"))
    o.append(txt(cx + 14, cy - 10, "≈ 2.3077", 11, MUTE, anchor="start"))
    o.append(txt(cx, B + 20, "7/10", 11, FG, weight="bold"))

    o.append(txt(px(F(58,100)), py(F(206,100)) - 14, "Ingham 1940", 12, BLUE, weight="bold"))
    o.append(txt(px(F(58,100)), py(F(206,100)) + 1, "3/(2−σ)", 11, BLUE))
    o.append(txt(px(F(745,1000)), py(F(222,100)) + 26, "Guth–Maynard 2024", 12, RED, weight="bold"))
    o.append(txt(px(F(745,1000)), py(F(222,100)) + 41, "15/(5σ+3)", 11, RED))

    # the payoff
    y = 470
    o.append(f'<line x1="{L}" y1="{y-24}" x2="{R_}" y2="{y-24}" stroke="#dcdce6" stroke-width="1"/>')
    o.append(txt(L, y, "θ = 1 − 1/‖A‖∞  =  1 − 13/30  =  17/30", 14, FG, anchor="start", weight="bold"))
    o.append(txt(L, y + 20, "the prime-gap exponent, fixed entirely by the height of that one point", 11, MUTE, anchor="start"))
    o.append(txt(L, y + 44, "dθ/d‖A‖ = 1/‖A‖∞²  =  169/900 ≈ 0.188", 13, FG, anchor="start"))
    o.append(txt(L, y + 62, "lower the peak by δ and θ improves by about 0.19 δ — the whole attack surface", 11, MUTE, anchor="start"))

    o.append(txt(W - 40, 524, "all values exact rational arithmetic, verified 2026-09-20", 10, MUTE, anchor="end"))
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    for name, fn in (("fig1_dimension_ladder.svg", figure1),
                     ("fig2_guth_maynard_cusp.svg", figure2)):
        with open(name, "w", encoding="utf-8") as f:
            f.write(fn())
        print("wrote", name)
