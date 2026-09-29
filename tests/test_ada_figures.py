"""
ADA Figure Tests for the Braille Sign Generator

Render the sign through the OpenSCAD CLI and measure the mesh against the
figures the Customizer and the documents quote:

- letter_height_mm is the printed height of the capital I, the letter ADA
  703.2.5 measures;
- the console's text width estimate, which auto-fit uses to size the plates,
  is within 2 % of the width the letters really print;
- braille keeps the 9.5 mm of ADA 703.3.2 from the border rail and the plate
  edge on a six-line sign;
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

# A six-line sign built from the liblouis sample data (braille is never typed).
SIX_SAMPLES = ["Restroom", "Exit", "Stairs", "Room 101", "Restroom", "Exit"]


def six_line_parameters():
    samples = json.loads(
        (PROJECT_ROOT / "scripts" / "sample_signs.json").read_text(encoding="utf-8")
    )
    params = {}
    for i, name in enumerate(SIX_SAMPLES, start=1):
        params[f"text_line_{i}"] = samples[name]["text"][0]
        params[f"braille_line_{i}"] = samples[name]["braille"][0]
    return params


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


@pytest.mark.requires_openscad
def test_braille_clearance_six_lines(runner, tmp_path):
    """
    On a six-line sign the braille keeps 9.5 mm (ADA 703.3.2) from the
    bottom border rail and from the top edge of the braille plate. Measured
    where each dot meets the face, its widest point: vertices above the face
    start at the dot base's narrower top ring and would read about 0.1 mm
    generous.
    """
    mesh, _ = render(
        runner,
        tmp_path,
        "six_braille_flat",
        {
            "sign_part": "Braille plate",
            "print_orientation": "Flat",
            "plate_thickness_mm": 3,
            "border_width_mm": 2,
            **six_line_parameters(),
        },
    )
    half_w, half_h = mesh.bounds[1][0], mesh.bounds[1][1]
    v = mesh.vertices
    rail_edge = -half_h + 2
    ring = v[
        (abs(v[:, 2] - 3.0) < 0.001)
        & (abs(v[:, 0]) < half_w - 2 - 0.01)
        & (v[:, 1] > rail_edge + 0.01)
        & (v[:, 1] < half_h - 0.01)
    ]
    assert len(ring), "no dot outlines found on the braille face"
    to_rail = ring[:, 1].min() - rail_edge
    to_edge = half_h - ring[:, 1].max()
    assert to_rail >= 9.5 and to_edge >= 9.5, (
        f"the braille sits {to_rail:.3f} mm from the bottom rail and "
        f"{to_edge:.3f} mm from the top edge; ADA 703.3.2 asks 9.5 mm"
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
