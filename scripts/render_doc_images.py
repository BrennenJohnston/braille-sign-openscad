"""Render the pictures the guides show into docs/images/.

Each picture is a preview of Braille_Sign_STL_Generator.scad from the
canonical OpenSCAD binary, framed with --autocenter --viewall. A plain PNG
export is a preview, so the warning text the generator draws beside the sign
shows in it just as it does on screen; that text never reaches an STL. Dials
a picture does not set keep their defaults.

Run from the repository root:

    python scripts/render_doc_images.py
    python scripts/render_doc_images.py --only sign-warning-preview   (one picture; repeatable)

The OpenSCAD binary comes from the OPENSCAD_EXE environment variable, else
the canonical nightly path below.

License: PolyForm Noncommercial 1.0.0
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAD = ROOT / "Braille_Sign_STL_Generator.scad"
OUT_DIR = ROOT / "docs" / "images"
EXE = os.environ.get("OPENSCAD_EXE", r"C:\Program Files\OpenSCAD (Nightly)\openscad.com")

VIEW = ["--imgsize=1200,900", "--autocenter", "--viewall", "--colorscheme", "Cornfield"]
THREE_QUARTER = "--camera=0,0,0,60,0,45,0"
TOP = "--camera=0,0,0,0,0,0,0"

# Picture name: its -D settings and its camera.
PICTURES = {
    "sign-default-three-quarter": ([], THREE_QUARTER),
    "sign-both-plates-top": ([], TOP),
    "sign-warning-preview": (['braille_line_1="Room 101"'], THREE_QUARTER),
    "sign-sample-restroom": (['sample_sign="Restroom"'], THREE_QUARTER),
}


def render(name, defines, camera):
    out = OUT_DIR / f"{name}.png"
    # Render beside the picture and swap it in only on success, so a failed run keeps the old one.
    tmp = OUT_DIR / f"{name}.tmp.png"
    tmp.unlink(missing_ok=True)
    cmd = [EXE, *VIEW, camera]
    for define in defines:
        cmd += ["-D", define]
    cmd += ["-o", str(tmp), str(SCAD)]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    # OpenSCAD's own messages start the line; the generator's echoed warnings start with ECHO:.
    problems = [ln for ln in (proc.stdout + proc.stderr).splitlines() if ln.startswith(("WARNING:", "ERROR:"))]
    if proc.returncode != 0 or problems or not tmp.exists():
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"{out.name}: exit {proc.returncode}; {problems or 'no PNG written'}")
    tmp.replace(out)
    return out


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", action="append", default=[], metavar="NAME",
                        help="render one picture, named without .png (repeatable)")
    args = parser.parse_args(argv)
    unknown = [n for n in args.only if n not in PICTURES]
    if unknown:
        parser.error(f"unknown picture {unknown}; choose from {list(PICTURES)}")
    if shutil.which(EXE) is None:
        parser.error(f"OpenSCAD not found at {EXE}; install the nightly there or set OPENSCAD_EXE")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name in args.only or PICTURES:
        out = render(name, *PICTURES[name])
        print(f"{out.relative_to(ROOT).as_posix()} {out.stat().st_size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
