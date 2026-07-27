"""
Source Invariant Guards for the Braille Sign Generator

These tests read the .scad source (no OpenSCAD required) and pin down the
invariants that keep this generator on-mission:

1. MAKERWORLD GUARD: the generator stays a single self-contained file — no
   include <> / use <> (MakerWorld's Parametric Model Maker takes one .scad).
2. The letter plate's raised characters are the one legitimate use of text() in
   this project, so text() is allowed here — but it must stay inside the letter
   geometry rather than leaking into the braille plate, which would export
   solid text onto a surface meant to be read by touch.

License: PolyForm Noncommercial 1.0.0
"""

import re

import pytest

from conftest import ALL_SCAD_FILES, SCAD_FILE


def strip_comments(scad_source: str) -> str:
    """Remove // line comments and /* */ block comments from OpenSCAD source."""
    no_block = re.sub(r"/\*.*?\*/", "", scad_source, flags=re.DOTALL)
    no_line = re.sub(r"//[^\n]*", "", no_block)
    return no_line


@pytest.fixture(scope="module")
def scad_content():
    return SCAD_FILE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def scad_code(scad_content):
    """Sign source with comments stripped: only real code remains."""
    return strip_comments(scad_content)


class TestMakerWorldSingleFile:
    """The generator must stay one self-contained .scad file."""

    @pytest.mark.parametrize(
        "scad_file", ALL_SCAD_FILES, ids=[f.stem for f in ALL_SCAD_FILES]
    )
    def test_no_include_or_use(self, scad_file):
        """
        MakerWorld's Parametric Model Maker accepts a single .scad upload, so
        the generator may not pull in other files via include <> or use <>.
        """
        code = strip_comments(scad_file.read_text(encoding="utf-8"))
        offending = re.findall(r"^\s*(include|use)\s*<[^>]*>", code, flags=re.MULTILINE)
        assert not offending, (
            f"{scad_file.name} uses include/use statements ({offending}); the "
            "generator must remain a single self-contained file for MakerWorld."
        )


class TestSignStructure:
    """Structural invariants of the two-plate sign."""

    def test_sign_part_offers_both_and_each_plate(self, scad_content):
        """
        sign_part must let a user export the plates together or one at a time:
        the plates print in different orientations, so a single combined export
        is not always usable.
        """
        match = re.search(
            r"^sign_part\s*=\s*\"([^\"]+)\"\s*;\s*//\s*\[([^\]]+)\]",
            scad_content,
            flags=re.MULTILINE,
        )
        assert match, "sign_part dropdown declaration not found"
        options = [opt.strip() for opt in match.group(2).split(",")]
        assert "Both" in options, f"sign_part must offer 'Both', got {options}"
        assert len(options) >= 3, (
            "sign_part must also allow exporting each plate on its own, got "
            f"{options}"
        )

    def test_six_text_and_braille_rows_declared(self, scad_content):
        """
        Every row of raised letters needs a matching braille row, or the two
        plates say different things.
        """
        letters = set(re.findall(r'^sign_text_(\d+)\s*=\s*"', scad_content, re.MULTILINE))
        braille = set(re.findall(r'^Line_(\d+)\s*=\s*"', scad_content, re.MULTILINE))
        assert letters == braille, (
            "sign_text_N and Line_N must come in matching pairs; letters="
            f"{sorted(letters)}, braille={sorted(braille)}"
        )

    def test_font_is_pinned_to_a_makerworld_available_font(self, scad_code):
        """
        The raised letters are ADA-relevant geometry, so the font cannot be
        left to whatever the host has installed. Liberation Sans is present on
        MakerWorld's render farm and on CI, so renders match everywhere.
        """
        match = re.search(r'font\s*=\s*"([^"]+)"', scad_code)
        assert match, "font assignment not found"
        assert "Liberation Sans" in match.group(1), (
            f"font must be pinned to Liberation Sans, got '{match.group(1)}'"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
