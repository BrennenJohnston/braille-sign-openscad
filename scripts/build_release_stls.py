"""Render the ready-to-print sample sign STLs into stl/.

Each built-in sample sign (the sample_sign dial) gets two files: the letter
plate, and the braille plate leaning on its break-away fins as the generator
defaults. Every other dial stays at its default. The canonical OpenSCAD
binary renders them with --hardwarnings as binary STL; a file whose largest
body is not watertight fails the run, while the 3-vertex slivers trimesh
reports at some plate corners (OpenSCAD itself calls the mesh a manifold)
are counted and ignored. The script then writes stl/README.md with one row
per file and prints the table.

Run from the repository root:

    python scripts/build_release_stls.py
    python scripts/build_release_stls.py --out <folder>   (render elsewhere to compare)

The OpenSCAD binary comes from the OPENSCAD_EXE environment variable, else
the canonical nightly path below.

License: PolyForm Noncommercial 1.0.0
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

import trimesh

ROOT = Path(__file__).resolve().parent.parent
SCAD = ROOT / "Braille_Sign_STL_Generator.scad"
EXE = os.environ.get("OPENSCAD_EXE", r"C:\Program Files\OpenSCAD (Nightly)\openscad.com")

# The sample_sign dropdown's samples, each with the slug its file names use.
SAMPLES = [("Restroom", "restroom"), ("Exit", "exit"), ("Stairs", "stairs"), ("Room 101", "room-101")]
# sign_part value, file-name slug, and the print settings for the README.
PLATES = [
    ("Letter plate", "letter-plate", "0.2 mm layers, flat, letters up"),
    ("Braille plate", "braille-plate", "0.1 mm layers, as modeled, no supports"),
]


def render(sample, plate, out):
    cmd = [EXE, "--hardwarnings", "--export-format", "binstl",
           "-D", f'sample_sign="{sample}"', "-D", f'sign_part="{plate}"', "-o", str(out), str(SCAD)]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    problems = [ln for ln in (proc.stdout + proc.stderr).splitlines() if "WARNING:" in ln or "ERROR:" in ln]
    if proc.returncode != 0 or problems or not out.exists():
        raise RuntimeError(f"{out.name}: exit {proc.returncode}; {problems or 'no STL written'}")


def largest_body(path):
    """The largest body, the number of slivers ignored, and any other bodies."""
    parts = trimesh.load(path, force="mesh").split(only_watertight=False)
    largest = max(parts, key=lambda p: len(p.vertices))
    rest = [p for p in parts if p is not largest]
    slivers = sum(1 for p in rest if len(p.vertices) < 0.01 * len(largest.vertices))
    return largest, slivers, len(rest) - slivers


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=ROOT / "stl", help="output folder (default: stl/)")
    args = parser.parse_args(argv)
    args.out.mkdir(parents=True, exist_ok=True)

    rows = []
    failures = []
    for sample, slug in SAMPLES:
        for plate, plate_slug, settings in PLATES:
            name = f"{slug}-{plate_slug}.stl"
            out = args.out / name
            try:
                render(sample, plate, out)
            except RuntimeError as err:
                failures.append(str(err))
                continue
            body, slivers, others = largest_body(out)
            w, d, h = body.bounds[1] - body.bounds[0]
            status = "OK" if body.is_watertight and others == 0 else "FAIL"
            if status == "FAIL":
                failures.append(f"{name}: largest body watertight {body.is_watertight}, other bodies {others}")
            print(f"{status} {name}: {w:.1f} x {d:.1f} x {h:.1f} mm, largest body {len(body.vertices)} vertices, "
                  f"volume {body.volume:.1f} mm3, slivers ignored {slivers}")
            rows.append(f"| `{name}` | {sample} | {plate} | {w:.1f} × {d:.1f} × {h:.1f} | {settings} |")

    table = ["| File | Sample | Plate | Size (mm) | Print with |", "|---|---|---|---|---|", *rows]
    readme = [
        "# Sample sign STLs",
        "",
        "Ready-to-print plates for the built-in sample signs, rendered from `Braille_Sign_STL_Generator.scad` "
        "at its defaults by `scripts/build_release_stls.py`. Each sign is two plates: print both and mount "
        "the letter plate above the braille plate.",
        "",
        "- Letter plate: print it flat, letters up, at 0.2 mm layers.",
        "- Braille plate: print it as modeled, leaning back on its fins, at 0.1 mm layers with no slicer "
        "supports, then snap the fins off.",
        "",
        *table,
        "",
    ]
    if args.out.resolve() == (ROOT / "stl").resolve():
        (args.out / "README.md").write_text("\n".join(readme), encoding="utf-8", newline="\n")
    # The README keeps the multiplication sign; a Windows console may not.
    print("\n".join(table).replace("×", "x"))
    if failures:
        print("FAILED:\n  " + "\n  ".join(failures))
        return 1
    print(f"{len(rows)} files OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
