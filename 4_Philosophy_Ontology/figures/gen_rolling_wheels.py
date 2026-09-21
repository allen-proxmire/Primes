#!/usr/bin/env python3
"""Generate the rolling-wheels animation as an animated SVG.

    python gen_rolling_wheels.py   ->  rolling_wheels.svg

Four wheels -- circumference 2, 3, 5 and 7 -- roll along the number line,
each with one tick mark that touches down every p units. A position any
mark touches is composite. A position none of them touches is OPEN.

The window is 100..130 deliberately, because it contains 121. That is the
one open position in this stretch that is NOT prime, and it is 11-squared
-- the exact point where the first wheel you did not carry starts doing
work. Below 121 the 11-wheel strikes nothing the smaller wheels have not
already struck.

Phases are real: at position x, wheel p has rolled x units from zero, so
its rotation is 360*x/p degrees. All four marks touch down together at 0
and do not all coincide again until 210.

Open in a browser to see it roll. Standard library only; no dependencies.
"""
import math

LO, HI = 100, 130
U = 30                      # pixels per integer
MARGIN = 56
W = (HI - LO) * U
WHEELS = [2, 3, 5, 7]
DUR = 24                    # seconds for one pass
ROW_H = 96
TOP = 96
RES_H = 92

BG, FG, MUTE, GRID = "#fbfbfd", "#1c1c22", "#6b6b78", "#e6e6ee"
COL = {2: "#2f6fb5", 3: "#c0442e", 5: "#2e7d5b", 7: "#8455a8"}
OPEN_P, OPEN_C, STRUCK = "#2e7d5b", "#c0442e", "#c9c9d4"


def is_prime(n):
    if n < 2: return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0: return False
    return True


def x_of(n):
    return MARGIN + (n - LO) * U


def txt(x, y, s, size=12, fill=FG, anchor="middle", weight="normal", style="normal", fam="Georgia,serif"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
            f'font-style="{style}">{s}</text>')


def wheel_row(p, top):
    """One wheel rolling on its own copy of the line."""
    r = p * U / (2 * math.pi)
    line_y = top + ROW_H - 26
    o = [f'<line x1="{MARGIN}" y1="{line_y}" x2="{MARGIN+W}" y2="{line_y}" '
         f'stroke="{FG}" stroke-width="1.2"/>']

    # ticks, and the positions this wheel strikes
    for n in range(LO, HI + 1):
        x = x_of(n)
        hit = (n % p == 0)
        o.append(f'<line x1="{x:.1f}" y1="{line_y}" x2="{x:.1f}" y2="{line_y+5}" '
                 f'stroke="{MUTE}" stroke-width="1"/>')
        if hit:
            o.append(f'<circle cx="{x:.1f}" cy="{line_y}" r="4" fill="{COL[p]}"/>')

    o.append(txt(MARGIN - 14, line_y + 4, f"{p}", 15, COL[p], "end", "bold"))
    o.append(txt(MARGIN - 14, line_y + 19, "wheel", 9, MUTE, "end"))

    # the rolling wheel: translate across, rotate about its own centre
    phase = (360.0 * LO / p) % 360.0
    turns = (HI - LO) / p
    o.append(f'''<g>
  <animateTransform attributeName="transform" type="translate"
    from="0 0" to="{W} 0" dur="{DUR}s" repeatCount="indefinite"/>
  <g transform="translate({MARGIN},{line_y - r:.2f})">
    <g transform="rotate({phase:.2f})">
      <animateTransform attributeName="transform" type="rotate"
        from="0 0 0" to="{360*turns:.2f} 0 0" dur="{DUR}s"
        repeatCount="indefinite" additive="sum"/>
      <circle cx="0" cy="0" r="{r:.2f}" fill="{COL[p]}" fill-opacity="0.09"
              stroke="{COL[p]}" stroke-width="1.8"/>
      <line x1="0" y1="0" x2="0" y2="{r:.2f}" stroke="{COL[p]}" stroke-width="2"/>
      <circle cx="0" cy="{r:.2f}" r="3.6" fill="{COL[p]}"/>
      <circle cx="0" cy="0" r="1.8" fill="{COL[p]}"/>
    </g>
  </g>
</g>''')
    return o


def build():
    H = TOP + len(WHEELS) * ROW_H + RES_H + 76
    TOTAL_W = MARGIN * 2 + W
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{TOTAL_W}" height="{H}" '
         f'viewBox="0 0 {TOTAL_W} {H}">',
         f'<rect width="{TOTAL_W}" height="{H}" fill="{BG}"/>']

    o.append(txt(TOTAL_W/2, 36, "Four wheels rolling on the number line", 19, FG, weight="bold"))
    o.append(txt(TOTAL_W/2, 58, "Each wheel has one mark. It touches down every p steps — and where it touches, the number is composite.", 12, MUTE))
    o.append(txt(TOTAL_W/2, 76, "A position no mark touches is OPEN. Open is a candidate, not a guarantee.", 12, MUTE, style="italic"))

    for i, p in enumerate(WHEELS):
        o += wheel_row(p, TOP + i * ROW_H)

    # combined result row
    ry = TOP + len(WHEELS) * ROW_H + 30
    o.append(f'<line x1="{MARGIN}" y1="{ry}" x2="{MARGIN+W}" y2="{ry}" stroke="{FG}" stroke-width="1.6"/>')
    o.append(txt(MARGIN - 14, ry + 4, "all", 13, FG, "end", "bold"))
    o.append(txt(MARGIN - 14, ry + 18, "four", 9, MUTE, "end"))

    for n in range(LO, HI + 1):
        x = x_of(n)
        struck = any(n % p == 0 for p in WHEELS)
        if struck:
            o.append(f'<circle cx="{x:.1f}" cy="{ry}" r="4.5" fill="{STRUCK}"/>')
        else:
            pr = is_prime(n)
            c = OPEN_P if pr else OPEN_C
            o.append(f'<circle cx="{x:.1f}" cy="{ry}" r="7.5" fill="{c}" fill-opacity="0.16" stroke="{c}" stroke-width="2"/>')
            o.append(txt(x, ry - 16, str(n), 12, c, weight="bold"))
            if not pr:
                o.append(txt(x, ry + 34, "121 = 11²", 11, c, weight="bold"))
                o.append(txt(x, ry + 48, "open, but not prime —", 10, c))
                o.append(txt(x, ry + 61, "the 11-wheel you didn't carry", 10, c))

    o.append(txt(MARGIN, H - 40, "grey = struck by a wheel you carry   ·   green = open and prime   ·   red = open and composite",
                 11, MUTE, anchor="start"))
    o.append(txt(MARGIN, H - 22,
                 "Wheel p strikes nothing new below p² — so four wheels are exact until 121, and 121 is where that stops.",
                 11, MUTE, anchor="start", style="italic"))
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    with open("rolling_wheels.svg", "w", encoding="utf-8") as f:
        f.write(build())
    print("wrote rolling_wheels.svg")
