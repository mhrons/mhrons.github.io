#!/usr/bin/env python3
"""Generates the Filtre_I SVG figures (style: CLAUDE.md "SVG style").

One figure per scan drawing (scan/Filtre_RC.png, scan/Filtre_RL.png):
  circuits (RC, RL), the 1+j sketch, and for each of the four filters
  (RC DPF, RC HPF, RL HPF, RL DPF) the complex-plane semicircle, the |H| plot
  and the phi plot.

Usage: python3 tools/diagrams/gen_Filtre_I.py [output_dir]   (default: docs/svg)
Stdlib only. Re-running overwrites docs/svg/Filtre_I_*.svg.
"""
import math, sys, pathlib

OUT = (pathlib.Path(sys.argv[1]) if len(sys.argv) > 1
       else pathlib.Path(__file__).resolve().parents[2] / "docs" / "svg")
OUT.mkdir(parents=True, exist_ok=True)

ROOT = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" fill="none" stroke="#222" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
        'font-family="\'Helvetica Neue\', Arial, sans-serif" font-size="16">\n')
DEFS = '''  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 1 L9 5 L0 9 z" fill="#222" stroke="none"/>
    </marker>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 1 L9 5 L0 9 z" fill="#c0392b" stroke="none"/>
    </marker>
  </defs>
'''
GUIDE = 'stroke="#888" stroke-width="1" stroke-dasharray="5 4"'
AX = 'stroke-width="1.5" marker-end="url(#ar)"'
RED = "#c0392b"


def t(x, y, s, anchor="start", size=None, italic=False, color="#222"):
    """Text element (fill set, stroke off)."""
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    z = f' font-size="{size}"' if size else ""
    i = ' font-style="italic"' if italic else ""
    return f'  <text x="{x}" y="{y}"{a}{z}{i} fill="{color}" stroke="none">{s}</text>\n'


def sub(base, s):
    return f'{base}<tspan baseline-shift="sub" font-size="70%">{s}</tspan>'


def write(name, w, h, title, body):
    (OUT / name).write_text(
        ROOT.format(w=w, h=h) + f"  <title>{title}</title>\n" + DEFS + body + "</svg>\n",
        encoding="utf-8")


# ---------------------------------------------------------------- circuits
def source(cx, cy):
    return (f'  <circle cx="{cx}" cy="{cy}" r="18"/>\n'
            f'  <path d="M{cx-9} {cy} q4.5 -9 9 0 t9 0" stroke-width="1.5"/>\n')


def circuit(name, title, second):
    """RC or RL series circuit: source left, R above the second element on the right."""
    b = source(60, 110)
    b += '  <path d="M60 92 V40 H180 V58 M180 98 V{y0}"/>\n'.format(y0=134 if second == "C" else 110)
    b += '  <rect x="172" y="58" width="16" height="40"/>\n'
    if second == "C":
        b += '  <path d="M180 134 V134 M168 134 H192 M168 142 H192 M180 142 V180"/>\n'
        y_lo, y_hi = 134, 180
    else:
        coil = "M180 110 " + " ".join("a6 6 0 0 1 0 12" for _ in range(4)) + " V180"
        b += f'  <path d="{coil}"/>\n'
        y_lo, y_hi = 110, 158
    b += '  <path d="M180 180 H60 V128"/>\n'
    b += '  <path d="M28 88 V132" marker-end="url(#ar)" stroke-width="1.5"/>\n'
    b += t(10, 115, "U", "start", italic=True)
    b += '  <path d="M96 24 H130" marker-end="url(#ar)" stroke-width="1.5"/>\n'
    b += t(113, 18, "I", "middle", italic=True)
    b += '  <path d="M208 62 V94" marker-end="url(#ar)" stroke-width="1.5"/>\n'
    b += t(218, 84, sub("U", "R"), italic=True)
    b += f'  <path d="M208 {y_lo+4} V{y_hi-4}" marker-end="url(#ar)" stroke-width="1.5"/>\n'
    b += t(218, (y_lo + y_hi) // 2 + 6, sub("U", second), italic=True)
    b += t(150, 84, "R", "end", italic=True)
    b += t(150, (y_lo + y_hi) // 2 + 6 if second == "L" else 144, second, "end", italic=True)
    if second == "L":
        b += f'  <circle cx="180" cy="{y_lo}" r="3" fill="#222" stroke="none"/>\n'
    write(name, 260, 200, title, b)


circuit("Filtre_I_RC_obvod.svg",
        "Sériový obvod RC: zdroj napätia U, rezistor R a kondenzátor C, napätia U_R a U_C, prúd I", "C")
circuit("Filtre_I_RL_obvod.svg",
        "Sériový obvod RL: zdroj napätia U, rezistor R a cievka L, napätia U_R a U_L, prúd I", "L")


# ------------------------------------------------------------ the 1+j sketch
def one_plus_j():
    ox, oy, u = 130, 125, 80
    px, py = ox + u, oy - u
    b = f'  <circle cx="{ox}" cy="{oy}" r="{u*math.sqrt(2):.1f}" {GUIDE}/>\n'
    b += f'  <path d="M10 {oy} H250" {AX}/>\n  <path d="M{ox} 240 V10" {AX}/>\n'
    b += f'  <path d="M{px} {oy} V{py} M{ox} {py} H{px}" {GUIDE}/>\n'
    b += f'  <path d="M{ox} {oy} L{px} {py}" marker-end="url(#ar)"/>\n'
    for x, lab in ((ox + u, "1"), (ox - u, "−1")):
        b += f'  <path d="M{x} {oy-4} V{oy+4}" stroke-width="1"/>\n'
        b += t(x, oy + 20, lab, "middle", size=13)
    for y, lab in ((oy - u, "j"), (oy + u, "−j")):
        b += f'  <path d="M{ox-4} {y} H{ox+4}" stroke-width="1"/>\n'
        b += t(ox - 10, y + 5, lab, "end", size=13)
    b += f'  <path d="M{ox+34} {oy} A34 34 0 0 0 {ox+34*math.cos(math.pi/4):.1f} {oy-34*math.sin(math.pi/4):.1f}" stroke-width="1"/>\n'
    b += t(ox + 40, oy - 8, "π/4", size=13)
    b += t(ox + 20, oy - 52, "√2", "end", italic=False)
    b += t(px + 8, py - 6, "1+j")
    write("Filtre_I_1plusj.svg", 260, 250,
          "Číslo 1+j v komplexnej rovine: dĺžka √2 a uhol π/4", b)


one_plus_j()


# ------------------------------------------------------ |H| and phi plots
X0, XW, X1 = 60, 140, 560            # omega axis: origin x, pixels per omega_0, end x
NS = 160
WS = [i * 3.4 / NS for i in range(NS + 1)]


def mag_fig(name, title, kind, w0):
    """|H|(omega): kind 'dpf' or 'hpf'. w0 is the label of the corner frequency."""
    Y0, YH = 150, 110                # y(0), pixels for H = 1
    h = (lambda w: 1 / math.sqrt(1 + w * w)) if kind == "dpf" else (lambda w: w / math.sqrt(1 + w * w))
    y2 = Y0 - YH / math.sqrt(2)
    b = f'  <path d="M{X0} {Y0} H{X1}" {AX}/>\n  <path d="M{X0} {Y0} V16" {AX}/>\n'
    b += f'  <path d="M{X0} {Y0-YH} H{X1-20}" {GUIDE}/>\n'
    b += f'  <path d="M{X0} {y2:.1f} H{X0+XW}" {GUIDE}/>\n'
    b += f'  <path d="M{X0+XW} {Y0+4} V{y2:.1f}" {GUIDE}/>\n'
    b += ('  <polyline points="' + " ".join(f"{X0+XW*w:.1f},{Y0-YH*h(w):.1f}" for w in WS) + '"/>\n')
    b += f'  <circle cx="{X0+XW}" cy="{y2:.1f}" r="3.5" fill="#222" stroke="none"/>\n'
    b += t(X0 - 8, 24, "H", "end", italic=True)
    b += t(X1 + 2, Y0 + 22, "ω", "end", italic=True)
    b += t(X0 - 8, Y0 - YH + 5, "1", "end", size=13)
    b += t(X0 - 8, y2 + 5, "1/√2", "end", size=13)
    b += t(X0 - 8, Y0 + 5, "0", "end", size=13)
    b += t(X0 + XW, Y0 + 22, w0, "middle", size=13)
    write(name, 600, 180, title, b)


def phase_fig(name, title, kind, w0, quarter=True):
    """phi(omega): DPF goes 0 -> -pi/2, HPF goes pi/2 -> 0."""
    PS = 100 / (math.pi / 2)         # pixels per radian
    if kind == "dpf":
        P0, phi = 40, (lambda w: -math.atan(w))
        ytop, ybot, lab_y = 14, 165, 30
    else:
        P0, phi = 140, (lambda w: math.atan(1 / w) if w > 0 else math.pi / 2)
        ytop, ybot, lab_y = 14, 165, 160
    sg = -1 if kind == "hpf" else 1   # +y is down: dpf phi<0 goes down, hpf phi>0 goes up
    ypt = lambda p: P0 - PS * p
    yq = ypt(phi(1))
    b = f'  <path d="M{X0} {P0} H{X1}" {AX}/>\n'
    b += f'  <path d="M{X0} {ybot if kind == "dpf" else P0 + 20} V{ytop}" {AX}/>\n'
    b += ('  <polyline points="' + " ".join(f"{X0+XW*w:.1f},{ypt(phi(w)):.1f}" for w in WS) + '"/>\n')
    b += f'  <path d="M{X0+XW} {P0} V{yq:.1f}" {GUIDE}/>\n'
    b += f'  <circle cx="{X0+XW}" cy="{yq:.1f}" r="3.5" fill="#222" stroke="none"/>\n'
    half = ypt(-math.pi / 2) if kind == "dpf" else ypt(math.pi / 2)
    b += f'  <path d="M{X0} {half:.1f} H{X0+XW}" {GUIDE}/>\n'
    if quarter:
        b += f'  <path d="M{X0} {yq:.1f} H{X0+XW}" {GUIDE}/>\n'
    sign = "−" if kind == "dpf" else ""
    b += t(X0 - 8, P0 + 5, "0", "end", size=13)
    b += t(X0 - 8, half + 5, f"{sign}π/2", "end", size=13)
    if quarter:
        b += t(X0 - 8, yq + 5, f"{sign}π/4", "end", size=13)
    b += t(X0 - 8, ytop + 8, "φ", "end", italic=True)
    b += t(X1 + 2, P0 + (-10 if kind == "dpf" else 22), "ω", "end", italic=True)
    b += t(X0 + XW, P0 + (-10 if kind == "dpf" else 22), w0, "middle", size=13)
    write(name, 600, 180, title, b)


# ------------------------------------------------------------- semicircles
def semicircle(name, title, kind, *, hname, omega_labels=None, chord_label=None,
               angle=None, extra_chord=False, guide_line=False):
    """Complex-plane graph of H(omega). kind 'dpf' (lower half) or 'hpf' (upper half).

    omega_labels: dict with optional keys 'inf' (text at omega->inf end), 'zero'
    (text at omega=0 end), 'w0' (text at the omega_0 point).
    angle: label of the angle arc at the origin (chord to the omega_0 point) or 'φ'
    (arc of the extra generic chord).
    """
    ox, R = 80, 120
    cx, cy = ox + R, None
    if kind == "dpf":
        oy, py, h = 110, 110 + R, 270
        arc = f"M{ox+2*R} {oy} A{R} {R} 0 0 1 {ox} {oy}"
        ytop, ybot = oy - 90, oy + R + 25
    else:
        oy, h = 180, 230
        py = oy - R
        arc = f"M{ox} {oy} A{R} {R} 0 0 1 {ox+2*R} {oy}"
        ytop, ybot = oy - R - 40, oy + 30
    b = f'  <path d="M{ox-20} {oy} H{ox+2*R+50}" {AX}/>\n'
    b += f'  <path d="M{ox} {ybot} V{ytop}" {AX}/>\n'
    b += t(ox + 2 * R + 50, oy + (22 if kind == "hpf" else -10), "+", "end")
    b += t(ox - 8, ytop + 6, "+j", "end")
    if guide_line:                                    # horizontal level j/2 across the figure
        b += f'  <path d="M{ox} {py} H{ox+2*R+50}" {GUIDE}/>\n'
    else:
        b += f'  <path d="M{ox} {py} H{cx}" {GUIDE}/>\n'
    b += f'  <path d="M{cx} {oy} V{py}" {GUIDE}/>\n'
    # chord to the omega_0 point
    b += f'  <path d="M{ox} {oy} L{cx} {py}" stroke-width="1.5" marker-end="url(#ar)"/>\n'
    if extra_chord:                                   # generic point, omega = omega_0 / 2
        x = 0.5
        re, im = x * x / (1 + x * x), x / (1 + x * x)
        gx, gy = ox + 2 * R * re, oy - 2 * R * im
        b += f'  <path d="M{ox} {oy} L{gx:.1f} {gy:.1f}" stroke-width="1.5"/>\n'
        a = math.atan2(im, re)
        b += (f'  <path d="M{ox+36} {oy} A36 36 0 0 0 {ox+36*math.cos(a):.1f} '
              f'{oy-36*math.sin(a):.1f}" stroke-width="1"/>\n')
        b += t(ox + 34, oy - 20, "φ", size=14, italic=True)
        b += f'  <circle cx="{gx:.1f}" cy="{gy:.1f}" r="3" fill="{RED}" stroke="none"/>\n'
    b += f'  <path d="{arc}" stroke="{RED}" stroke-width="2.5" marker-end="url(#arr)"/>\n'
    b += f'  <circle cx="{cx}" cy="{py}" r="4" fill="{RED}" stroke="none"/>\n'
    # ticks and labels on the axes
    lab_y = oy - 10 if kind == "dpf" else oy + 20
    for x in (ox, cx, ox + 2 * R):
        b += f'  <path d="M{x} {oy-4} V{oy+4}" stroke-width="1"/>\n'
    b += f'  <path d="M{ox-4} {py} H{ox+4}" stroke-width="1"/>\n'
    b += t(ox - 6, oy - 8 if kind == "dpf" else oy + 20, "0", "end", size=13)
    b += t(cx, lab_y, "1/2", "middle", size=13)
    b += t(ox + 2 * R + 4, lab_y, "1", "start", size=13)
    b += t(ox - 8, py + 5, "−j/2" if kind == "dpf" else "j/2", "end", size=13)
    # angle arc at the origin for the chord to the omega_0 point
    if angle in ("π/4", "−π/4"):
        s = 1 if kind == "dpf" else -1
        ex, ey = ox + 34 * math.cos(math.pi / 4), oy + s * 34 * math.sin(math.pi / 4)
        b += f'  <path d="M{ox+34} {oy} A34 34 0 0 {1 if kind == "dpf" else 0} {ex:.1f} {ey:.1f}" stroke-width="1"/>\n'
        b += t(ox + 40, oy + s * 20 + (4 if kind == "dpf" else 0), angle, size=13)
    ol = omega_labels or {}
    if kind == "dpf":
        if "w0" in ol:
            b += t(cx, py + 22, ol["w0"], "middle", size=14, italic=True)
        if "inf" in ol:
            b += f'  <path d="M{ox-30} {oy-26} L{ox-4} {oy-4}" stroke-width="1" marker-end="url(#ar)"/>\n'
            b += t(ox - 32, oy - 32, ol["inf"], "end", size=14)
        if "zero" in ol:
            b += f'  <path d="M{ox+2*R+40} {oy+22} L{ox+2*R+6} {oy+4}" stroke-width="1" marker-end="url(#ar)"/>\n'
            b += t(ox + 2 * R + 42, oy + 38, ol["zero"], size=14)
        if chord_label:
            b += t(ox + 52, oy + 64, chord_label, "end", size=13)
        b += t(ox + 2 * R + 14, oy + 90, hname, color=RED, italic=True, size=18)
    else:
        if "w0" in ol:
            b += t(cx + 10, py - 12, ol["w0"], size=14, italic=True)
        if "inf" in ol:
            b += f'  <path d="M{ox+2*R+36} {oy-20} L{ox+2*R+4} {oy-4}" stroke-width="1" marker-end="url(#ar)"/>\n'
            b += t(ox + 2 * R + 38, oy - 26, ol["inf"], size=14)
        if chord_label:
            b += t(ox + 52, oy - 64, chord_label, "end", size=13)
        b += t(ox + 2 * R - 40, py - 20, hname, color=RED, italic=True, size=18)
    write(name, 440, h, title, b)


# ---------------------------------------------------------------- the 4 filters
# RC low-pass (scan Filtre_RC.png, top half)
semicircle("Filtre_I_RC_DPF_polkruznica.svg",
           "Prenosová funkcia DPF filtra RC v komplexnej rovine: dolná polkružnica od 1 do 0", "dpf",
           hname="ℋ<tspan baseline-shift=\"sub\" font-size=\"70%\">DPF</tspan>(ω)",
           omega_labels={"inf": "ω→∞", "zero": "ω→0", "w0": "ω=1/RC"}, chord_label="1/√2")
mag_fig("Filtre_I_RC_DPF_H.svg", "Amplitúdová charakteristika DPF filtra RC: od 1 klesá, v 1/RC je 1/√2", "dpf", "1/RC")
phase_fig("Filtre_I_RC_DPF_phi.svg", "Fázová charakteristika DPF filtra RC: od 0 klesá k −π/2, v 1/RC je −π/4", "dpf", "1/RC")
# RC high-pass (scan Filtre_RC.png, bottom half)
semicircle("Filtre_I_RC_HPF_polkruznica.svg",
           "Prenosová funkcia HPF filtra RC v komplexnej rovine: horná polkružnica od 0 do 1", "hpf",
           hname="ℋ<tspan baseline-shift=\"sub\" font-size=\"70%\">HPF</tspan>(ω)",
           omega_labels={"inf": "ω→∞", "w0": "ω=1/RC"}, extra_chord=True)
mag_fig("Filtre_I_RC_HPF_H.svg", "Amplitúdová charakteristika HPF filtra RC: od 0 rastie k 1, v 1/RC je 1/√2", "hpf", "1/RC")
phase_fig("Filtre_I_RC_HPF_phi.svg", "Fázová charakteristika HPF filtra RC: od π/2 klesá k 0, v 1/RC je π/4", "hpf", "1/RC")
# RL high-pass (scan Filtre_RL.png, top half)
semicircle("Filtre_I_RL_HPF_polkruznica.svg",
           "Prenosová funkcia HPF filtra RL v komplexnej rovine: horná polkružnica od 0 do 1", "hpf",
           hname="ℋ(ω)", angle="π/4", guide_line=True)
mag_fig("Filtre_I_RL_HPF_H.svg", "Amplitúdová charakteristika HPF filtra RL: od 0 rastie k 1, v R/L je 1/√2", "hpf", "R/L")
phase_fig("Filtre_I_RL_HPF_phi.svg", "Fázová charakteristika HPF filtra RL: od π/2 klesá k 0, v R/L je π/4", "hpf", "R/L")
# RL low-pass (scan Filtre_RL.png, bottom half)
semicircle("Filtre_I_RL_DPF_polkruznica.svg",
           "Prenosová funkcia DPF filtra RL v komplexnej rovine: dolná polkružnica od 1 do 0", "dpf",
           hname="ℋ(ω)", omega_labels={"inf": "ω→∞", "zero": "ω=0"}, angle="−π/4")
mag_fig("Filtre_I_RL_DPF_H.svg", "Amplitúdová charakteristika DPF filtra RL: od 1 klesá, v R/L je 1/√2", "dpf", "R/L")
phase_fig("Filtre_I_RL_DPF_phi.svg", "Fázová charakteristika DPF filtra RL: od 0 klesá k −π/2", "dpf", "R/L", quarter=False)

print("done:", len(list(OUT.glob("Filtre_I_*.svg"))), "files in", OUT)
