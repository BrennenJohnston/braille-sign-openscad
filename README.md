# Braille Sign STL Generator (OpenSCAD)

[![CI](https://github.com/BrennenJohnston/braille-sign-openscad/actions/workflows/ci.yml/badge.svg)](https://github.com/BrennenJohnston/braille-sign-openscad/actions/workflows/ci.yml)
[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-blue)](LICENSE)
[![Live demo](https://img.shields.io/badge/live%20demo-OpenSCAD%20Assistive%20Forge-brightgreen)](https://openscad-assistive-forge.pages.dev/?example=braille-sign)

## Overview

A parametric OpenSCAD generator for **two-part tactile signs**: a plate of
raised uppercase letters above a plate of the same wording in braille, following
the 2010 ADA Standards (section 703) recommendations. It is for anyone who needs
a room sign that reads by touch as well as by sight, and for the makers who
print them. The letter plate prints flat and the braille plate prints leaning
back at 75 degrees on break-away fins, because braille printed at 75 to 90
degrees reads faster and more comfortably than flat-printed braille; mounted
touching, the two plates' split borders join into one frame.

One self-contained `.scad` file, MakerWorld-ready, no `include`/`use`.

The picture below shows the default sign the way the printer makes it: the
letter plate lies flat with ROOM 101 in raised letters inside a raised border,
and the braille plate leans back on a row of thin support fins that snap off
after printing. This view shows the back of the braille plate, so its dots face
away from you.

![The default sign as it prints, seen from above and in front. The letter plate lies flat with ROOM 101 in raised capital letters inside a raised border. In front of it the braille plate leans back on a row of thin support fins; this view shows its back and fins, and its braille dots face away.](docs/images/sign-default-three-quarter.png)

The two guides to read first: the [quick start](docs/guides/quick-start.md)
(one page, from your wording to a sign on the wall) and the
[Maker Guide](docs/guides/maker-guide.md) (the same path in more depth).

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

## How to obtain the device

### In your browser with the Forge

<https://openscad-assistive-forge.pages.dev/?example=braille-sign>

The Forge is an accessibility-first web customizer that runs entirely in your
browser — no account, no uploads, no OpenSCAD install. It ships this generator
as a built-in tool and translates plain text to Grade 1 or Grade 2 Unicode
braille on your device via liblouis, so you can skip the manual translation
step. It updates its own copy of the generator separately, so its dial names
and defaults can differ from this repository's.

### On your computer with OpenSCAD

Open `Braille_Sign_STL_Generator.scad` in [OpenSCAD](https://openscad.org/)
2021.01 or newer (a development snapshot renders fastest) and show the
Customizer (Window > Customizer; in 2021.01, untick Window > Hide Customizer).
Fill in the four Steps from the top: in **Step 1 - Pick a sample sign or type
your own**, pick a `sample_sign` or type your wording into `text_line_1` to
`text_line_6`; in **Step 2 - Braille, pasted from a translator**, paste Unicode
braille into `braille_line_1` to `braille_line_6`; in **Step 3 - What to
export**, choose `sign_part` and leave `print_orientation` on `Angled`; in
**Step 4 - Size**, leave `auto_fit` on `Yes`. Press F6 to render and export each
plate as an STL. The [quick start](docs/guides/quick-start.md) has every click,
and red words beside the sign in the preview name a problem that the full
guide's [Warnings and notes](docs/guides/full-guide.md#warnings-and-notes)
explains.

`Braille_Sign_STL_Generator.json` sits next to the `.scad`, so OpenSCAD
auto-loads its parameter sets into the Customizer preset dropdown:

- **Default Sign (both plates)** — the first-run defaults.
- **Braille Plate Only (flat)** — one plate, printed dots-up.

Your own saved parameter sets go in the same dropdown via the Customizer's `+`
button. If you keep personal presets (names, contact info in braille), save them
to a file ending in `.local.json` — that pattern is gitignored so they never end
up in a public commit.

### A ready-to-print sample

No OpenSCAD needed: the [`stl/`](stl) folder holds both plates of the Restroom,
Exit, Stairs and Room 101 signs, ready to print. [`stl/README.md`](stl/README.md)
lists each file with its size and print settings.

### MakerWorld

The listing is prepared in
[`docs/MAKERWORLD_LISTING.md`](docs/MAKERWORLD_LISTING.md) and goes live when
the owner publishes it. MakerWorld's Parametric Model Maker takes only the
`.scad` (the `.json` presets do not upload), and it shows no OpenSCAD console,
so [`docs/MAKERWORLD_QUICK_START.md`](docs/MAKERWORLD_QUICK_START.md) describes
each problem by what you can see instead. Both are written to the shared
[Accessible MakerWorld Documentation Standard](https://github.com/BrennenJohnston/accessible-makerworld-doc-standard/blob/main/ACCESSIBLE_MAKERWORLD_DOC_STANDARD.md).

## Build instructions

The [Maker Guide](docs/guides/maker-guide.md), section by section:

1. [Choose a way](docs/guides/maker-guide.md#1-choose-a-way)
2. [Prepare the wording](docs/guides/maker-guide.md#2-prepare-the-wording)
3. [Customize](docs/guides/maker-guide.md#3-customize)
4. [Print](docs/guides/maker-guide.md#4-print)
5. [Mount](docs/guides/maker-guide.md#5-mount)
6. [Check it](docs/guides/maker-guide.md#6-check-it)

What to buy besides filament is in the [bill of materials](docs/guides/bom.md).

## How to use it

The [User Guide](docs/guides/user-guide.md) is for the people who put the sign
up, read it and look after it: who it is for, where ADA 703.4 puts it, how it
reads, care, and its limits.

## How to improve this device

The [full guide](docs/guides/full-guide.md) explains how the sign is built,
every dial, every warning and note, the renamed dials, and the command line.
The [design rationale](docs/guides/design-rationale.md) gives the reason and the
measured number behind each default.

```bash
pip install -r tests/requirements.txt
pytest tests -v
```

- `tests/test_customizer.py`: the dropdowns are well formed, and the presets
  file names only real dials and holds no personal text.
- `tests/test_source_guards.py`: one self-contained file, the pinned font, the
  three export choices, six text and braille line pairs, the tab layout,
  dropdown labels without parentheses, and the braille sliders inside ADA
  Table 703.3.1.
- `tests/test_sample_signs.py`: the sample data is well formed and matches the
  dropdown and the file's tables.
- `tests/test_ada_figures.py`: the capital I height, the width estimate within
  2 %, the braille's 9.5 mm clearance, and the character table against its
  data file.
- `tests/test_render_smoke.py`: each plate renders as one solid, and the
  preview warnings never reach an export.
- `tests/test_release_stls.py`: `stl/README.md` lists every shipped STL, and
  the shipped Restroom letter plate still matches a fresh render.
- `tests/test_full_guide_covers_every_dial.py`: the full guide names every
  dial, quotes every warning and note, and matches the sample data.
- `tests/test_docs_gate.py`: this README and every page under `docs/` meet the
  documentation rules that `scripts/check_docs.py` checks.

The tests marked `requires_openscad` render the sign and need OpenSCAD
installed. `powershell -ExecutionPolicy Bypass -File scripts\scad-check.ps1`
renders the default sign with strict warnings and prints `CHECK PASSED` or
`CHECK FAILED`; [`scripts/README.md`](scripts/README.md) lists every script.
CI (GitHub Actions) runs a lint check, every test that needs no OpenSCAD, and
the render smoke tests on Ubuntu with an OpenSCAD nightly AppImage, on every
pull request.

### Related projects

- [braille-wedge-card-openscad](https://github.com/BrennenJohnston/braille-wedge-card-openscad)
  — directly readable braille cards on the same 75° leaning technique. **This
  generator's commit history lives there**, where it shipped as part of v1.1.0
  before moving to this repo.
- [braille-charm-openscad](https://github.com/BrennenJohnston/braille-charm-openscad)
  — braille charms, pendants, and bracelet clips; split out of the same repo.
- [OpenSCAD Assistive Forge](https://github.com/BrennenJohnston/openscad-assistive-forge)
  — accessibility-first browser customizer that ships all three as built-in
  tools with automatic braille translation
  ([live demo](https://openscad-assistive-forge.pages.dev/)).
- [braille-cylinder-stl-generator-openscad](https://github.com/BrennenJohnston/braille-cylinder-stl-generator-openscad)
  — braille **embossing plates** (emboss + counter pairs) for cylindrical
  objects. The dot geometry here traces back to it.

## Files

Documentation:

| File | What it is |
|---|---|
| `README.md` | this page |
| `docs/guides/quick-start.md` | the whole path on one page |
| `docs/guides/maker-guide.md` | how to make the sign |
| `docs/guides/user-guide.md` | how to place, read and look after it |
| `docs/guides/full-guide.md` | every dial, warning and note |
| `docs/guides/bom.md` | what to buy, and filament per sample |
| `docs/guides/design-rationale.md` | why each default is what it is |
| `docs/MAKERWORLD_LISTING.md` | the MakerWorld listing, ready to paste |
| `docs/MAKERWORLD_QUICK_START.md` | using the file on MakerWorld |
| `CHANGELOG.md` | what changed in each version |
| `okh.yml` | the Open Know-How manifest |

Design files:

| File | What it is |
|---|---|
| `Braille_Sign_STL_Generator.scad` | the generator: open it in OpenSCAD and use the Customizer |
| `Braille_Sign_STL_Generator.json` | Customizer presets, auto-loaded by OpenSCAD |
| `scripts/sample_signs.json` | the sample signs' wording and braille, from liblouis |
| `scripts/glyph_advances.json` | the letter widths behind the width estimate |

Build files:

| File | What it is |
|---|---|
| `stl/*.stl` | both plates of each sample sign, ready to print |
| `stl/README.md` | each STL with its size and print settings |
| `docs/images/*.png` | the preview pictures the guides show |

## License

**PolyForm Noncommercial 1.0.0** — free for personal, educational, and other
noncommercial use; modification and redistribution allowed under the same
terms; **no commercial use**. See [LICENSE](LICENSE). MakerWorld, Printables
and Thingiverse do not offer PolyForm, so the copies there carry the closest
license they do offer, Creative Commons Attribution-NonCommercial 4.0
(CC BY-NC 4.0), chosen by the owner.

## Attribution

- **Brennen Johnston** — project owner; braille dot system and the leaning /
  break-away fin geometry.
- **Puerta, Crnovrsanin, South, Dunne (CHI 2024)** — the orientation research
  the angled braille plate is built on.
- **masukomi** and **Slant3D** — break-away support fin technique.

The research behind the defaults:

- [Puerta et al., CHI 2024](https://doi.org/10.1145/3613904.3642719), "The
  Effect of Orientation on the Readability and Comfort of 3D-Printed Braille":
  braille printed at 75–90° reads significantly faster and more comfortably than
  flat; 75° also reduces dot overhangs vs. 90°. The angled braille plate exists
  for this reason.
- [masukomi, "Manual Support Fins for 3D Printing"](https://weblog.masukomi.org/2024/03/11/manual-support-fins-for-3d-printing/):
  ~1 mm fin offset, a column of small sprues, side fins so edges don't float,
  0.3–0.4 mm contact — the fin/bridge defaults follow this.
- [2010 ADA Standards](https://archive.ada.gov/), section 703: character
  height, raise height, and dot dimension envelope behind the defaults.
- [BANA size and spacing](https://brailleauthority.org/size-and-spacing-braille-characters):
  cell geometry and clear-space guidance behind the spacing defaults.

The documentation and repository structure follow the OpenAT Template created by
Makers Making Change / Neil Squire Society, used under a CC BY-SA 4.0 license:
[github.com/makersmakingchange/OpenAT-Template](https://github.com/makersmakingchange/OpenAT-Template).
