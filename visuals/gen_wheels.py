"""Draws wheel_30.svg and wheel_210.svg: the open spokes of a wheel, its twin-open pairs and its mirror line. Standard library only."""
from math import cos, sin, radians, gcd

TEAL_LINE, TEAL_FILL, TEAL_EDGE = "#1D9E75", "#9FE1CB", "#0F6E56"
CORAL, GRAY, TEXT, INK = "#D85A30", "#888780", "#5F5E5A", "#2C2C2A"

def wheel(M, R, label_all, struck_by=None, fname=None):
    cx, cy = 340, R + 100
    pt = lambda k, r: (cx + r * cos(radians(-90 + 360 * k / M)), cy + r * sin(radians(-90 + 360 * k / M)))
    opn = [k for k in range(M) if gcd(k, M) == 1]
    out = [f'<line x1="{cx}" y1="{cy-R+10}" x2="{cx}" y2="{cy+R-10}" stroke="{GRAY}" stroke-width="0.5" stroke-dasharray="4 4"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{GRAY}" stroke-width="1"/>']
    for a in opn:
        if gcd(a + 2, M) == 1:
            x1, y1 = pt(a, R + 8); x2, y2 = pt(a + 2, R + 8)
            out.append(f'<path d="M{x1:.1f} {y1:.1f} A{R+8} {R+8} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{CORAL}" stroke-width="4" stroke-linecap="round"/>')
    sw = 2.5 if M <= 30 else 1.2
    for k in opn:
        x, y = pt(k, R)
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{TEAL_LINE}" stroke-width="{sw}" stroke-linecap="round"/>')
    for i, k in enumerate(opn):
        x, y = pt(k, R)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{6 if M <= 30 else 3.5}" fill="{TEAL_FILL}" stroke="{TEAL_EDGE}" stroke-width="0.5"/>')
        lx, ly = pt(k, R + (32 if label_all else (24 if i % 2 == 0 else 42)))
        fs = 14 if M <= 30 else 11
        out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="{fs}" font-weight="500" fill="{INK}" text-anchor="middle" dominant-baseline="central">{k}</text>')
    if label_all:
        for k in range(M):
            if k in opn: continue
            x, y = pt(k, R); lx, ly = pt(k, R + 26)
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.5" fill="{GRAY}" opacity="0.6"/>')
            out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="12" fill="{TEXT}" text-anchor="middle" dominant-baseline="central">{k}</text>')
    if struck_by:
        for k in range(M):
            if gcd(k, M // struck_by) == 1 and k % struck_by == 0:
                x, y = pt(k, R)
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#ffffff" stroke="{CORAL}" stroke-width="1.2"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{GRAY}"/>')
    ly = cy + R + 70
    leg = [(f'<line x1="90" y1="{ly}" x2="120" y2="{ly}" stroke="{TEAL_LINE}" stroke-width="2.5"/>', f'open spoke ({len(opn)})'),
           (f'<line x1="330" y1="{ly}" x2="360" y2="{ly}" stroke="{CORAL}" stroke-width="4" stroke-linecap="round"/>',
            f'twin-open pair ({sum(1 for a in opn if gcd(a+2, M) == 1)})')]
    out.append(leg[0][0] + f'<text x="128" y="{ly}" font-size="12" fill="{TEXT}" dominant-baseline="central">{leg[0][1]}</text>')
    out.append(leg[1][0] + f'<text x="368" y="{ly}" font-size="12" fill="{TEXT}" dominant-baseline="central">{leg[1][1]}</text>')
    ly2 = ly + 26
    out.append(f'<line x1="90" y1="{ly2}" x2="120" y2="{ly2}" stroke="{GRAY}" stroke-width="0.5" stroke-dasharray="4 4"/>'
               f'<text x="128" y="{ly2}" font-size="12" fill="{TEXT}" dominant-baseline="central">mirror line: slot r matches slot {M} − r</text>')
    if struck_by:
        out.append(f'<circle cx="345" cy="{ly2}" r="4" fill="#ffffff" stroke="{CORAL}" stroke-width="1.2"/>'
                   f'<text x="368" y="{ly2}" font-size="12" fill="{TEXT}" dominant-baseline="central">30-wheel spoke struck by {struck_by}</text>')
    H = ly2 + 34
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="680" height="{H}" viewBox="0 0 680 {H}" font-family="Helvetica, Arial, sans-serif">'
           f'<rect width="680" height="{H}" fill="#ffffff"/>' + "".join(out) + "</svg>")
    open(fname, "w").write(svg)

wheel(30, 150, True, fname="wheel_30.svg")
wheel(210, 200, False, struck_by=7, fname="wheel_210.svg")
