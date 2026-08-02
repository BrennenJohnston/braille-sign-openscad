# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-08-01

### Changed

- **Overflow warnings now report measured size against available space**, in the
  counted style the sibling cylinder generator uses for `TEXT TOO LONG: n/capacity`.
  The four warnings previously said only that something was too tall or too wide,
  which told you a problem existed but not how big it was or how much to change —
  so fixing it by hand meant guessing, rendering, and guessing again. They now
  read e.g. `WARNING: BRAILLE TOO WIDE: 242.1/156 mm (longest line is 35 cells).
  Turn on auto_fit, raise sign_width_mm to at least 246.1, or shorten the line.`
  The thresholds themselves are unchanged, so nothing warns that did not warn
  before; only the message is more useful. Geometry is untouched.
- Added a `mm1()` helper so millimetre figures print to one decimal instead of
  as raw floats like `47.32499999999999`, and hoisted the repeated
  `border_on ? border_width_mm : 0` inset into named `_inner_w` /
  `_letter_inner_h` / `_braille_inner_h` values shared by the checks and their
  messages — the warning can no longer describe a different limit than the one
  that triggered it.

## [1.0.0] - 2026-07-27

First release as a standalone repository.

**Commit history lives in
[braille-wedge-card-openscad](https://github.com/BrennenJohnston/braille-wedge-card-openscad),**
where this generator was introduced in v1.1.0 (2026-07-12) alongside the wedge
card and the charm. That repo now holds the wedge card only. This repository
starts with fresh history; nothing about the generator itself changed in the
move.

### Added

- **`Braille_Sign_STL_Generator.scad`** — two-part ADA-style tactile sign:
  raised-letter plate (Liberation Sans, uppercase, 16 mm, 0.8 mm raise) plus a
  braille plate (flat or 75° angled with break-away fins), a split raised border
  that joins into one continuous frame when the plates are mounted together,
  auto-fit sizing, and `sign_part` = Both / Letter plate / Braille plate.
- **`Braille_Sign_STL_Generator.json`** presets: Default Sign (both plates) and
  Braille Plate Only (flat).
- **Test suite and CI.** Customizer dropdown hygiene and preset/parameter
  consistency tests, source-invariant guards (single-file MakerWorld
  requirement, `sign_part` export options, matching letter/braille row pairs,
  pinned font), and OpenSCAD render smoke tests asserting watertight exports
  with the expected body count for the two-plate sign, the angled braille plate,
  and the letter plate. GitHub Actions runs lint + quick tests + render smoke on
  Ubuntu.
- **README** covering the desktop workflow, print guidance, troubleshooting,
  MakerWorld upload steps, and the ADA disclaimer.
- **PolyForm Noncommercial 1.0.0 LICENSE.**

### Changed (vs. the wedge card repo)

- The test suite is scoped to this one generator: `conftest.py` declares a single
  `.scad`, and the card-only guards (20 `Line_N` parameters, `_all_lines`
  wiring, preview-only warnings, the `text()`-outside-`warning_slot` guard, and
  the de-embossing mission guard) are gone. Sign-specific structural guards
  replace them.
- The `.scad` header records that this generator now lives in its own repo.

[1.0.0]: https://github.com/BrennenJohnston/braille-sign-openscad/releases/tag/v1.0.0
