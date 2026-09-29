"""
The full guide stays locked to the generator.

docs/guides/full-guide.md must give every Customizer dial its own heading, in
the Customizer's order; quote every warning and note the file can print to the
console or draw in the preview; show the sample signs exactly as
scripts/sample_signs.json holds them; and list every retired dial name in its
rename table, so a saved preset or a -D script written for an old name can be
translated. Reads files only (quick lane).

License: PolyForm Noncommercial 1.0.0
"""

import json
import re

import pytest

from conftest import PROJECT_ROOT, SCAD_FILE

GUIDE = PROJECT_ROOT / "docs" / "guides" / "full-guide.md"

# The names the rename retired; the guide's "Old names" table maps each to its new name.
OLD_NAMES = [
    "sign_text_1", "Line_1", "char_height_mm", "line_spacing_pct", "letter_spacing",
    "cell_spacing", "line_spacing", "dot_spacing", "part_gap_mm", "cone_dot_flat_hat",
    "cone_segments",
]

STRING = re.compile(r'"((?:[^"\\]|\\.)*)"')


def flat(text):
    """Whitespace collapsed, so a quote wrapped across Markdown lines still matches."""
    return " ".join(text.split())


@pytest.fixture(scope="module")
def scad():
    return SCAD_FILE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def guide():
    if not GUIDE.exists():
        pytest.fail(f"{GUIDE.relative_to(PROJECT_ROOT).as_posix()} not found")
    return GUIDE.read_text(encoding="utf-8")


def dials(scad):
    """The Customizer dials in file order: test_customizer.py's scad_params regex."""
    head = scad.split("CALCULATED VALUES")[0]
    return [m.group(1) for m in re.finditer(r"^(\w+)\s*=\s*[^=]", head, flags=re.MULTILINE)]


def arguments(source, start):
    """The text from start to the parenthesis that closes the one just before it.

    Walks the characters so that a ")" or ";" inside a string literal, as in
    "(5/8 in);", does not end the call early.
    """
    i, depth, in_string = start, 1, False
    while depth:
        c = source[i]
        if in_string:
            if c == "\\":
                i += 1
            elif c == '"':
                in_string = False
        elif c == '"':
            in_string = True
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        i += 1
    return source[start:i - 1]


def messages(scad):
    """Every string literal of each WARNING: or NOTE: echo, and each preview warning text."""
    found = []
    for call in re.finditer(r"\becho\(", scad):
        parts = STRING.findall(arguments(scad, call.end()))
        if parts and parts[0].startswith(("WARNING:", "NOTE:")):
            found += [p.strip() for p in parts if p.strip()]
    slots = re.search(r"_warn_slots\s*=\s*concat\(", scad)
    assert slots, "_warn_slots = concat(...) not found in the .scad"
    found += [p.strip() for p in STRING.findall(arguments(scad, slots.end()))
              if p not in ("red", "orange")]
    return found


def test_every_dial_has_its_heading_in_customizer_order(scad, guide):
    names = dials(scad)
    assert names, "no dials found above the CALCULATED VALUES marker"
    headings = re.findall(r"^### `(\w+)`\s*$", guide, flags=re.MULTILINE)
    missing = [n for n in names if n not in headings]
    assert not missing, f"no '### `name`' heading in the full guide for: {missing}"
    in_guide_order = [h for h in headings if h in names]
    if in_guide_order != names:
        i = next((i for i, (a, b) in enumerate(zip(in_guide_order, names)) if a != b),
                 min(len(in_guide_order), len(names)))
        pytest.fail(
            f"the dial headings are not in the Customizer's order (or one repeats): "
            f"heading {i + 1} is {in_guide_order[i:i + 1]}, the file has {names[i:i + 1]}"
        )


def test_every_warning_and_note_is_quoted(scad, guide):
    text = flat(guide)
    missing = [m for m in messages(scad) if flat(m) not in text]
    assert not missing, f"the full guide does not quote: {missing}"


def test_sample_table_matches_the_json(guide):
    samples = json.loads((PROJECT_ROOT / "scripts" / "sample_signs.json").read_text(encoding="utf-8"))
    assert "\n## The sample signs" in guide, "the full guide has no '## The sample signs' section"
    section = guide.split("\n## The sample signs", 1)[1].split("\n## ", 1)[0]
    rows = [line for line in section.splitlines() if line.startswith("|")]
    missing = [name for name, sample in samples.items()
               if not any(name in row and all(b in row for b in sample["braille"] if b) for row in rows)]
    assert not missing, f"the sample table has no row matching scripts/sample_signs.json for: {missing}"


def test_rename_table_lists_every_old_name(guide):
    assert "\n## Old names" in guide, "the full guide has no '## Old names' section"
    section = guide.split("\n## Old names", 1)[1].split("\n## ", 1)[0]
    table = "\n".join(line for line in section.splitlines() if line.startswith("|"))
    missing = [n for n in OLD_NAMES if f"`{n}`" not in table]
    assert not missing, f"the rename table does not list: {missing}"
