"""Draws wheel_30_roll.svg and wheel_210_roll.svg: a wheel at the moment the next wheel joins, the part of its rim it
has used, the part it never uses, and the open spokes past the handover that land on non-primes. Standard library only."""
from math import cos, sin, radians, gcd, pi

TEAL, CORAL, GRAY, TEXT, INK, PALE = "#1D9E75", "#D85A30", "#888780", "#5F5E5A", "#2C2C2A", "#B4B2A9"

def is_prime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))

def roll(M, start, end, U, fname, label_all):
    X0, GY = 50, 230
    R = M * U / (2 * pi); CY = GY - R
    X = lambda n: X0 + (n - start) * U
    cx = X(end)
    pt = lambda n, r=R: (cx + r * sin(radians((n - end) * 360 / M)), CY + r * cos(radians((n - end) * 360 / M)))
    arc = lambda a, b: " ".join(("M" if i == 0 else "L") + "%.1f %.1f" % pt(a + (b - a) * i / 120) for i in range(121))
    o = [f'<line x1="{X0-10}" y1="{GY}" x2="{X(start+M)+10:.1f}" y2="{GY}" stroke="{GRAY}" stroke-width="1"/>',
         f'<circle cx="{cx:.1f}" cy="{CY:.1f}" r="{R:.1f}" fill="none" stroke="{GRAY}" stroke-width="1"/>',
         f'<path d="{arc(start, end)}" fill="none" stroke="{TEAL}" stroke-width="7" opacity="0.4"/>',
         f'<path d="{arc(end, start + M)}" fill="none" stroke="{CORAL}" stroke-width="7" opacity="0.55"/>']
    false = []
    for n in range(start, start + M):
        if gcd(n, M) != 1:
            continue
        x, y = pt(n); p = is_prime(n)
        col = TEAL if n < end else (PALE if p else CORAL)
        o.append(f'<line x1="{cx:.1f}" y1="{CY:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="{2 if M <= 30 else (1.6 if not p else 1)}" stroke-linecap="round"/>')
        r = 5 if M <= 30 else 3
        if p and n < end:
            o.append(f'<circle cx="{X(n):.1f}" cy="{GY}" r="{r}" fill="{TEAL}"/>')
        elif p:
            o.append(f'<circle cx="{X(n):.1f}" cy="{GY}" r="{r-0.5}" fill="#ffffff" stroke="{PALE}" stroke-width="1.2"/>')
        else:
            false.append(n); o.append(f'<circle cx="{X(n):.1f}" cy="{GY}" r="{r+0.5}" fill="{CORAL}"/>')
    o.append(f'<circle cx="{cx:.1f}" cy="{CY:.1f}" r="4" fill="{GRAY}"/>')
    txt = lambda x, y, s, col=TEXT, w=400: f'<text x="{x:.1f}" y="{y}" font-size="12" font-weight="{w}" fill="{col}" text-anchor="middle">{s}</text>'
    if label_all:
        for n in range(start, start + M + 1):
            o.append(txt(X(n), GY + 20, n, CORAL if n in false else TEXT, 500 if n in false else 400))
    else:
        for n in (start, start + M):
            o.append(txt(X(n), GY + 20, n))
        for i, n in enumerate(false):
            o.append(txt(X(n), GY + (20 if i % 2 == 0 else 35), n, CORAL, 500))
    by = GY + 46
    o.append(f'<rect x="{X(start):.1f}" y="{by}" width="{X(end)-X(start):.1f}" height="5" rx="2" fill="{TEAL}"/>')
    o.append(f'<rect x="{X(end):.1f}" y="{by}" width="{X(start+M)-X(end):.1f}" height="5" rx="2" fill="{CORAL}"/>')
    used, rest = end - start, start + M - end
    o.append(txt((X(start) + X(end)) / 2, by + 24, f"in charge: {used} of {M} slots ({100*used/M:.0f}%)"))
    o.append(txt((X(end) + X(start + M)) / 2, by + 24, f"never used: {rest} of {M}" + (f"; {len(false)} open spokes land on non-primes" if len(false) > 1 else "")))
    H = by + 44
    open(fname, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="680" height="{H}" viewBox="0 0 680 {H}" font-family="Helvetica, Arial, sans-serif">'
                           f'<rect width="680" height="{H}" fill="#ffffff"/>' + "".join(o) + "</svg>")
    return false

print(roll(30, 25, 49, 18, "wheel_30_roll.svg", True))
print(roll(210, 49, 121, 2.75, "wheel_210_roll.svg", False))
