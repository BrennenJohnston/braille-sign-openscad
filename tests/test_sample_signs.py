"""
Sample-Sign Data Tests

The sample_sign dial's wording and braille come from scripts/sample_signs.json,
which scripts/generate_sample_braille.mjs writes from liblouis (UEB Grade 2,
the table chain the OpenSCAD Assistive Forge uses). Braille in this repository
is never typed by hand; these tests lock the file's shape so the sample tables
built from it stay valid.

License: PolyForm Noncommercial 1.0.0
"""

import json

from conftest import PROJECT_ROOT

SAMPLES_FILE = PROJECT_ROOT / "scripts" / "sample_signs.json"

# The sample_sign dropdown's options after "Type my own", in dropdown order.
SAMPLE_NAMES = ["Restroom", "Exit", "Stairs", "Room 101"]

# The sign has six text lines and six braille lines.
MAX_ROWS = 6

# Loose sanity limit; auto-fit grows the plate for any real sign wording.
MAX_CELLS = 30


def load_samples():
    assert SAMPLES_FILE.exists(), f"sample data not found: {SAMPLES_FILE}"
    return json.loads(SAMPLES_FILE.read_text(encoding="utf-8"))


def test_sample_file_parses():
    samples = load_samples()
    assert isinstance(samples, dict), "sample_signs.json must hold one object"


def test_samples_are_the_dropdown_options_in_order():
    assert list(load_samples()) == SAMPLE_NAMES


def test_every_text_line_has_a_braille_line():
    for name, sample in load_samples().items():
        text = sample["text"]
        braille = sample["braille"]
        assert 1 <= len(text) <= MAX_ROWS, (
            f"{name}: {len(text)} text lines; a sign holds 1 to {MAX_ROWS}"
        )
        assert all(line.strip() for line in text), f"{name}: empty text line"
        assert len(braille) == len(text), (
            f"{name}: {len(text)} text lines but {len(braille)} braille lines"
        )
        assert all(braille), f"{name}: empty braille line"


def test_braille_is_unicode_braille_only():
    for name, sample in load_samples().items():
        for line in sample["braille"]:
            bad = [f"U+{ord(c):04X}" for c in line if not 0x2800 <= ord(c) <= 0x28FF]
            assert not bad, (
                f"{name}: braille line {line!r} holds non-braille characters {bad}"
            )
            assert len(line) <= MAX_CELLS, (
                f"{name}: braille line is {len(line)} cells; the limit is {MAX_CELLS}"
            )
