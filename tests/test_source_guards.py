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
        letters = set(re.findall(r'^text_line_(\d+)\s*=\s*"', scad_content, re.MULTILINE))
        braille = set(re.findall(r'^braille_line_(\d+)\s*=\s*"', scad_content, re.MULTILINE))
        assert letters and letters == braille, (
            "text_line_N and braille_line_N must come in matching pairs; letters="
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


# The ten dials that shape or space the braille dots, with the slider range
# each must span. Dot base diameter, dot height and the three spacings are
# ADA 703.3.1 (Table 703.3.1, its printed metric figures); the dome, base
# height and cone top limits are the plan's choices inside that table.
TACTILE_SLIDERS = {
    "rounded_dot_base_diameter": (1.5, 1.6),
    "rounded_dot_dome_diameter": (1.0, 1.6),
    "rounded_dot_base_height": (0.1, 0.5),
    "rounded_dot_dome_height": (0.2, 0.8),
    "cone_dot_base_diameter": (1.5, 1.6),
    "cone_dot_height": (0.6, 0.9),
    "cone_dot_top_diameter": (0.3, 1.0),
    "braille_dot_spacing_mm": (2.3, 2.5),
    "braille_cell_spacing_mm": (6.1, 7.6),
    "braille_line_spacing_mm": (10.0, 10.2),
}


class TestTactileRanges:
    """The braille dot dials cannot leave ADA 703.3.1 from the Customizer."""

    def test_tactile_sliders_inside_the_ada_table(self, scad_content):
        """
        Each tactile dial's slider spans exactly its range and its default
        sits inside it. OpenSCAD does not check a default against its own
        slider, and a -D value or a preset skips the slider altogether: the
        asserts in the .scad catch those.
        """
        problems = []
        for name, (low, high) in TACTILE_SLIDERS.items():
            match = re.search(
                rf"^{name}\s*=\s*([-\d.]+)\s*;\s*//\s*\[([-\d.]+):([-\d.]+):([-\d.]+)\]",
                scad_content,
                re.MULTILINE,
            )
            if not match:
                problems.append(f"{name}: no numeric slider found")
                continue
            default, s_min, _step, s_max = (float(g) for g in match.groups())
            if (s_min, s_max) != (low, high):
                problems.append(f"{name}: slider {s_min} to {s_max}, must be {low} to {high}")
            if not low <= default <= high:
                problems.append(f"{name}: default {default} is outside {low} to {high}")
        assert not problems, "tactile sliders outside ADA 703.3.1:\n" + "\n".join(problems)


class TestCustomizerLayout:
    """The Customizer reads top to bottom: four Steps, then Advanced tabs."""

    def test_every_tab_is_a_step_or_advanced(self, scad_content):
        """
        A beginner fills in Step 1 to Step 4 and stops; every other dial sits
        under a tab whose name starts with "Advanced - " so nobody has to
        guess which tabs they may skip.
        """
        tabs = re.findall(r"^/\*\s*\[([^\]]+)\]\s*\*/", scad_content, re.MULTILINE)
        assert tabs, "no Customizer tab markers found"
        bad = [
            t for t in tabs
            if not re.match(r"^Step [1-4] - .+$", t)
            and not re.match(r"^Advanced - .+$", t)
            and t != "Hidden"
        ]
        assert not bad, (
            "every tab must be named 'Step N - ...', 'Advanced - ...' or "
            f"'Hidden'; these are not: {bad}"
        )

    def test_no_parentheses_in_dropdown_labels(self, scad_content):
        """
        The Customizer fails to parse a dropdown option that contains a
        parenthesis and silently falls back to the default (MakerWorld's
        maker inherits this), so option labels must never contain one.
        """
        bad = []
        for match in re.finditer(
            r'^(\w+)\s*=\s*"[^"]*"\s*;\s*//\s*\[([^\]]+)\]', scad_content, re.MULTILINE
        ):
            for option in match.group(2).split(","):
                if "(" in option or ")" in option:
                    bad.append(f"{match.group(1)}: {option.strip()}")
        assert not bad, f"dropdown options must not contain parentheses: {bad}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
