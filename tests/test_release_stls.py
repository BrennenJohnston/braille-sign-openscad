"""
Release STL Library Tests

stl/ holds a ready-to-print STL for each plate of each sample sign, made by
scripts/build_release_stls.py and listed in stl/README.md. These tests keep
the README and the folder in step, and check that a shipped file still
matches a fresh render of the generator.

License: PolyForm Noncommercial 1.0.0
"""

import re

import pytest
import trimesh

from conftest import PROJECT_ROOT, SCAD_FILE
from openscad_runner import OpenSCADNotFoundError, OpenSCADRunner

STL_DIR = PROJECT_ROOT / "stl"
README = STL_DIR / "README.md"


def readme_files():
    assert README.exists(), f"{README} not found"
    text = README.read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*`?([\w.-]+\.stl)`?\s*\|", text, re.MULTILINE))


def test_readme_lists_every_shipped_stl():
    listed = readme_files()
    shipped = {p.name for p in STL_DIR.glob("*.stl")}
    assert listed, "stl/README.md lists no STL files"
    assert listed == shipped, (
        f"listed but missing: {sorted(listed - shipped)}; "
        f"shipped but not listed: {sorted(shipped - listed)}"
    )


@pytest.fixture(scope="module")
def runner():
    try:
        return OpenSCADRunner()
    except OpenSCADNotFoundError:
        pytest.skip("OpenSCAD not installed - skipping the release STL render test")


@pytest.mark.requires_openscad
def test_shipped_restroom_letter_plate_matches_a_fresh_render(runner, tmp_path):
    """The shipped file is what the generator makes today, within 0.1 %."""
    shipped = STL_DIR / "restroom-letter-plate.stl"
    assert shipped.exists(), f"{shipped} not found"
    fresh_path = tmp_path / "restroom-letter-plate.stl"
    result = runner.generate_stl(
        SCAD_FILE,
        fresh_path,
        parameters={"sample_sign": "Restroom", "sign_part": "Letter plate"},
    )
    assert result.success, f"render failed (rc={result.returncode}):\n{result.stderr}"
    fresh = trimesh.load(fresh_path, force="mesh")
    old = trimesh.load(shipped, force="mesh")
    assert abs(fresh.volume / old.volume - 1) <= 0.001, (
        f"volume: shipped {old.volume:.3f} mm3, fresh {fresh.volume:.3f} mm3; "
        "rebuild with scripts/build_release_stls.py"
    )
    assert abs(fresh.area / old.area - 1) <= 0.001, (
        f"area: shipped {old.area:.3f} mm2, fresh {fresh.area:.3f} mm2; "
        "rebuild with scripts/build_release_stls.py"
    )
