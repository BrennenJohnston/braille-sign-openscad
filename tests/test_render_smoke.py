"""
Render Smoke Tests for the Braille Sign Generator

Renders representative configurations through the OpenSCAD CLI and asserts each
export is a printable solid:

- watertight,
- the expected number of connected bodies (raised letters, dots, fins, bridges,
  and border all fused into their plate — the historical failure mode was dots
  and letters exporting as hundreds of floating shells).

These tests auto-skip when OpenSCAD is not installed. render_quality=Medium is
passed via -D to keep render times low; quality only affects tessellation
density, not the body count.

License: PolyForm Noncommercial 1.0.0
"""

import re
from pathlib import Path

import pytest
import trimesh

from conftest import SCAD_FILE
from openscad_runner import OpenSCADNotFoundError, OpenSCADRunner


@pytest.fixture(scope="module")
def runner():
    try:
        return OpenSCADRunner()
    except OpenSCADNotFoundError:
        pytest.skip("OpenSCAD not installed - skipping render smoke tests")


def render(
    runner, tmp_path: Path, name: str, parameters: dict, scad_file=SCAD_FILE
) -> trimesh.Trimesh:
    output = tmp_path / f"{name}.stl"
    params = {"render_quality": "Medium", **parameters}
    result = runner.generate_stl(scad_file, output, parameters=params)
    assert result.success, (
        f"OpenSCAD render failed (rc={result.returncode}):\n{result.stderr}"
    )
    return trimesh.load(output, force="mesh")


def assert_printable(mesh: trimesh.Trimesh, bodies=1):
    assert mesh.is_watertight, "exported STL is not watertight"
    assert mesh.body_count == bodies, (
        f"exported STL has {mesh.body_count} disconnected bodies, expected "
        f"{bodies}; letters, dots, fins, bridges, and border must fuse into "
        "printable solids"
    )


@pytest.mark.requires_openscad
def test_sign_both_plates(runner, tmp_path):
    """Default sign: letter plate + angled braille plate = two solids."""
    mesh = render(runner, tmp_path, "sign_both", {})
    assert_printable(mesh, bodies=2)


@pytest.mark.requires_openscad
def test_sign_braille_plate_angled(runner, tmp_path):
    """Angled braille plate with fins exports as one fused solid."""
    mesh = render(
        runner,
        tmp_path,
        "sign_braille_angled",
        {"sign_part": "Braille plate"},
    )
    assert_printable(mesh, bodies=1)


@pytest.mark.requires_openscad
def test_sign_letter_plate(runner, tmp_path):
    """
    Letter plate alone: the raised characters and the split border must fuse
    into the plate rather than exporting as separate letter shells.
    """
    mesh = render(
        runner,
        tmp_path,
        "sign_letters",
        {"sign_part": "Letter plate"},
    )
    assert_printable(mesh, bodies=1)


@pytest.mark.requires_openscad
def test_warnings_never_exported(runner, tmp_path):
    """
    show_warnings draws problems as preview-only text. With a warning firing
    (a braille line that is not braille), the export is the same two solids
    with the warnings on and off: the text never reaches the STL.
    """
    source = SCAD_FILE.read_text(encoding="utf-8")
    assert re.search(r'^show_warnings\s*=\s*"(Yes|No)"\s*;', source, re.MULTILINE), (
        "show_warnings is not a Customizer dial"
    )
    meshes = {}
    for choice in ("Yes", "No"):
        output = tmp_path / f"warnings_{choice}.stl"
        result = runner.generate_stl(
            SCAD_FILE,
            output,
            parameters={
                "render_quality": "Medium",
                "braille_line_1": "Room 101",
                "show_warnings": choice,
            },
        )
        assert result.success, f"render failed (rc={result.returncode}):\n{result.stderr}"
        assert "contains non-braille characters" in result.stdout + result.stderr, (
            "the test sign must fire a warning"
        )
        meshes[choice] = trimesh.load(output, force="mesh")
    on, off = meshes["Yes"], meshes["No"]
    assert on.body_count == off.body_count == 2, (
        f"bodies with warnings on {on.body_count}, off {off.body_count}; expected 2"
    )
    assert round(on.volume, 6) == round(off.volume, 6), "the warning text changed the volume"
    assert round(on.area, 6) == round(off.area, 6), "the warning text changed the area"
    assert (on.bounds.round(6) == off.bounds.round(6)).all(), "the warning text changed the bounds"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
