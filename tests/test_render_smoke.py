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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
