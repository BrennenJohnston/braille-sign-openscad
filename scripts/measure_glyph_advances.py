"""Measure Liberation Sans glyph metrics for the sign's text width estimate.

Run by hand from the repository root (never in CI) whenever the font or the
estimate changes:

    python scripts/measure_glyph_advances.py

For every character from chr(32) to chr(126) it measures three numbers per
unit of text() size: the advance, and the left and right edges of the glyph's
ink measured from its origin. It writes them to scripts/glyph_advances.json
and prints the GLYPH_METRICS table that Braille_Sign_STL_Generator.scad
carries, so the .scad can work out how wide a centred line prints without
textmetrics(), which MakerWorld and the desktop Customizer do not enable.

The numbers come from OpenSCAD's textmetrics() (the binary runs with
--enable=textmetrics). If that is unavailable, or with --fallback, each
character is rendered alone and doubled at text size 10 and measured from the
meshes instead (slower; needs trimesh).

The OpenSCAD binary comes from the OPENSCAD_EXE environment variable, else
the canonical nightly path below.

License: PolyForm Noncommercial 1.0.0
"""

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXE = os.environ.get("OPENSCAD_EXE", r"C:\Program Files\OpenSCAD (Nightly)\openscad.com")
FONT = "Liberation Sans"
CODES = range(32, 127)
JSON_PATH = ROOT / "scripts" / "glyph_advances.json"
NUMBER = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"


def vector(name, text):
    match = re.search(rf"{name} = \[({NUMBER}), ({NUMBER})\]", text)
    if not match:
        raise ValueError(f"no {name} in {text!r}")
    return float(match.group(1)), float(match.group(2))


def by_textmetrics(work):
    """Every glyph's metrics from one textmetrics() run; None if unavailable."""
    scad = work / "metrics.scad"
    lines = [f'echo(str("CAP|", textmetrics(text = "I", size = 1, font = "{FONT}")));']
    lines += [f'echo(str("ADV|", {c}, "|", textmetrics(text = chr({c}), size = 1, font = "{FONT}")));'
              for c in CODES]
    scad.write_text("\n".join(lines) + "\ncube(1);\n", encoding="utf-8")
    out = work / "metrics.echo"
    proc = subprocess.run([EXE, "--enable=textmetrics", "-o", str(out), str(scad)],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    echoed = out.read_text(encoding="utf-8") if out.exists() else ""
    if proc.returncode != 0 or "is not enabled" in echoed or "unknown function" in echoed:
        return None
    cap = None
    glyphs = {}
    for line in echoed.splitlines():
        if line.startswith('ECHO: "CAP|'):
            cap = vector("size", line)[1]
        elif line.startswith('ECHO: "ADV|'):
            code = int(line.split("|")[1])
            left = vector("position", line)[0]
            glyphs[code] = (vector("advance", line)[0], left, left + vector("size", line)[0])
    if cap is None or sorted(glyphs) != list(CODES):
        return None
    return cap, glyphs


def by_rendering(work):
    """Every glyph's metrics from rendered meshes: text size 10, the origin at x = 0."""
    import trimesh

    size = 10.0
    scad = work / "glyph.scad"
    stl = work / "glyph.stl"

    def ink(text):
        scad.write_text(f'linear_extrude(1) text({json.dumps(text)}, size = {size}, font = "{FONT}");\n',
                        encoding="utf-8")
        subprocess.run([EXE, "-o", str(stl), str(scad)], capture_output=True, check=True)
        v = trimesh.load(stl, force="mesh").vertices
        return v[:, 0].min() / size, v[:, 0].max() / size, (v[:, 1].max() - v[:, 1].min()) / size

    # The advance is read from the character followed by H, which kerns with
    # nothing; a doubled character would fold pair kerning into it ("11" does).
    h_right = ink("H")[1]
    glyphs = {}
    for c in CODES:
        if c == 32:
            continue
        left, right, _ = ink(chr(c))
        glyphs[c] = (ink(chr(c) + "H")[1] - h_right, left, right)
    glyphs[32] = (ink("I I")[1] - ink("II")[1], 0.0, 0.0)
    return ink("I")[2], dict(sorted(glyphs.items()))


def main(argv):
    with tempfile.TemporaryDirectory() as tmp:
        measured = None if "--fallback" in argv else by_textmetrics(Path(tmp))
        source = "textmetrics"
        if measured is None:
            measured = by_rendering(Path(tmp))
            source = "rendered meshes"
    cap, glyphs = measured
    payload = {
        "font": FONT,
        "unit": "per unit of text() size",
        "source": f"scripts/measure_glyph_advances.py, from {source}",
        "cap_height_I": round(cap, 6),
        "glyphs": {str(c): {"char": chr(c), "advance": round(a, 6), "ink_left": round(lo, 6),
                            "ink_right": round(hi, 6)}
                   for c, (a, lo, hi) in sorted(glyphs.items())},
    }
    JSON_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8", newline="\n")
    print(f"Wrote {JSON_PATH.relative_to(ROOT)} from {source}: {len(glyphs)} glyphs, "
          f"capital I height {cap:g} per unit size")
    print("// [advance, ink left edge, ink right edge] per unit of text() size, chr(32) to chr(126),")
    print("// Liberation Sans, from scripts/glyph_advances.json (scripts/measure_glyph_advances.py).")
    print("GLYPH_METRICS = [")
    codes = list(CODES)
    for i in range(0, len(codes), 5):
        row = codes[i:i + 5]
        cells = ", ".join(f"[{glyphs[c][0]:g}, {glyphs[c][1]:g}, {glyphs[c][2]:g}]" for c in row)
        chars = " ".join("space" if c == 32 else chr(c) for c in row)
        print(f"    {cells}{'' if i + 5 >= len(codes) else ','}  // {chars}")
    print("];")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
