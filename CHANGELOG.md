# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
