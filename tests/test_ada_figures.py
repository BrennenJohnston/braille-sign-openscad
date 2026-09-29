"""
ADA Figure Tests for the Braille Sign Generator

Render the sign through the OpenSCAD CLI and measure the mesh against the
figures the Customizer and the documents quote:

- letter_height_mm is the printed height of the capital I, the letter ADA
  703.2.5 measures;
- the console's text width estimate, which auto-fit uses to size the plates,
  is within 2 % of the width the letters really print;
- the .scad's GLYPH_METRICS table is the one scripts/measure_glyph_advances.py
  measured (this one reads files only and runs without OpenSCAD).

The render tests auto-skip when OpenSCAD is not installed.

License: PolyForm Noncommercial 1.0.0
"""

import json
import re
from pathlib import Path

import pytest
import trimesh

from conftest import PROJECT_ROOT, SCAD_FILE
from openscad_runner import OpenSCADNotFoundError, OpenSCADRunner

# Letter tops sit at plate_thickness_mm 3 + letter_raise_mm 0.8 = 3.8 mm.
LETTER_TOP_Z = 3.79


@pytest.fixture(scope="module")
def runner():
    try:
        return OpenSCADRunner()
    except OpenSCADNotFoundError:
        pytest.skip("OpenSCAD not installed - skipping ADA figure tests")


def render(runner, tmp_path: Path, name: str, parameters: dict):
    output = tmp_path / f"{name}.stl"
    params = {"render_quality": "Medium", **parameters}
    result = runner.generate_stl(SCAD_FILE, output, parameters=params)
    assert result.success, (
        f"OpenSCAD render failed (rc={result.returncode}):\n{result.stderr}"
    )
    return trimesh.load(output, force="mesh"), result.stdout + result.stderr


@pytest.mark.requires_openscad
def test_capital_i_height(runner, tmp_path):
    """letter_height_mm = 16 prints a capital I 16.0 mm tall."""
    mesh, _ = render(
        runner,
        tmp_path,
        "letter_I",
        {
            "sign_part": "Letter plate",
            "letter_height_mm": 16,
            "text_line_1": "I",
            "braille_line_1": "",
        },
    )
    v = mesh.vertices
    tops = v[(v[:, 2] > LETTER_TOP_Z) & (abs(v[:, 0]) < 30) & (abs(v[:, 1]) < 30)]
    height = tops[:, 1].max() - tops[:, 1].min()
    assert abs(height - 16.0) <= 0.05, (
        f"the capital I prints {height:.3f} mm tall at letter_height_mm 16; "
        "ADA 703.2.5 measures the uppercase I, so the dial must mean its height"
    )


@pytest.mark.requires_openscad
@pytest.mark.parametrize("wording", ["WWWWWWWW", "ROOM 101"])
def test_width_estimate(runner, tmp_path, wording):
    """
    The console's width estimate is within 2 % of the printed letters' width.
    The border is turned off so every vertex at letter height is a letter,
    even when the letters overhang the plate; it does not move the letters.
    """
    mesh, console = render(
        runner,
        tmp_path,
        "width",
        {
            "sign_part": "Letter plate",
            "text_line_1": wording,
            "braille_line_1": "",
            "add_border": "No",
        },
    )
    match = re.search(r'ECHO: "Text width estimate: ([\d.]+) mm"', console)
    assert match, "the console has no 'Text width estimate:' line"
    estimate = float(match.group(1))
    v = mesh.vertices
    tops = v[v[:, 2] > LETTER_TOP_Z]
    width = tops[:, 0].max() - tops[:, 0].min()
    assert abs(estimate / width - 1) <= 0.02, (
        f"{wording}: the estimate is {estimate} mm but the letters print "
        f"{width:.2f} mm wide ({(estimate / width - 1) * 100:+.1f} %)"
    )


def test_glyph_table_matches_the_json():
    """
    GLYPH_METRICS is copied from scripts/glyph_advances.json; a re-measure that
    was not pasted into the .scad, or a hand edit, shows up here.
    """
    glyphs = json.loads(
        (PROJECT_ROOT / "scripts" / "glyph_advances.json").read_text(encoding="utf-8")
    )["glyphs"]
    expected = [
        [glyphs[str(c)][k] for k in ("advance", "ink_left", "ink_right")]
        for c in range(32, 127)
    ]
    src = SCAD_FILE.read_text(encoding="utf-8")
    body = re.search(r"^GLYPH_METRICS\s*=\s*\[(.*?)\];", src, re.MULTILINE | re.DOTALL)
    assert body, "GLYPH_METRICS not found in the .scad"
    number = r"-?\d+(?:\.\d+)?(?:[eE]-?\d+)?"
    rows = [
        [float(x) for x in re.findall(number, row)]
        for row in re.findall(rf"\[({number},\s*{number},\s*{number})\]", body.group(1))
    ]
    assert len(rows) == len(expected), f"GLYPH_METRICS has {len(rows)} rows, expected 95"
    bad = [
        chr(32 + i)
        for i, (got, want) in enumerate(zip(rows, expected))
        if any(abs(g - w) > 1e-5 for g, w in zip(got, want))
    ]
    assert not bad, f"GLYPH_METRICS differs from glyph_advances.json for {bad}"
