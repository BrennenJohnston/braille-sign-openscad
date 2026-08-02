# Braille Sign STL Generator (OpenSCAD)

[![CI](https://github.com/BrennenJohnston/braille-sign-openscad/actions/workflows/ci.yml/badge.svg)](https://github.com/BrennenJohnston/braille-sign-openscad/actions/workflows/ci.yml)
[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-blue)](LICENSE)
[![Live demo](https://img.shields.io/badge/live%20demo-OpenSCAD%20Assistive%20Forge-brightgreen)](https://openscad-assistive-forge.pages.dev/?example=braille-sign)

A parametric OpenSCAD generator for **two-part tactile signs**: a plate of
raised uppercase letters above a plate of the same wording in braille, following
the 2010 ADA Standards (section 703) recommendations.

One self-contained `.scad` file, MakerWorld-ready, no `include`/`use`.

| File | What it makes |
|------|---------------|
| `Braille_Sign_STL_Generator.scad` | The generator — open in OpenSCAD and use the Customizer |
| `Braille_Sign_STL_Generator.json` | Customizer presets, auto-loaded by OpenSCAD |

## What it makes

- **Letter plate** — raised Liberation Sans characters, uppercase by default,
  16 mm character height (5/8 in minimum per 703.2.5), raised 0.8 mm (1/32 in
  per 703.2.1), 135% line spacing. Prints flat, letters up.
- **Braille plate** — the same wording in braille (`Line_1`…`Line_6`, Unicode
  braille). Prints leaning back at 75° with break-away support fins by default,
  or flat.
- **Split raised border** — the letter plate carries the top + side rails and
  the braille plate the bottom + sides, so the mounted pair forms one continuous
  tactile frame around the whole sign.

The braille plate leans back at **75°** from the print bed by default — the
angle a [CHI 2024 study](https://doi.org/10.1145/3613904.3642719) found
significantly faster and more comfortable to read than flat-printed braille,
because near-vertical printing moves the layer seams off the finger-contact
surface. Triangular **break-away support fins** stand behind the plate, joined
by tiny snap-off bridges and grounded by a built-in brim, so it prints
support-free as one fused STL. The fins snap off after printing.

> **ADA disclaimer:** the defaults follow the published 703 figures, but this
> tool does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

## Try it in your browser (no install)

**Live demo:
[OpenSCAD Assistive Forge](https://openscad-assistive-forge.pages.dev/?example=braille-sign)**

The Forge is an accessibility-first web customizer that runs entirely in your
browser — no account, no uploads, no OpenSCAD install. It ships this generator
as a built-in tool and translates plain text to Grade 1 or Grade 2 Unicode
braille on your device via liblouis, so you can skip the manual translation
step below.

The rest of this README covers the desktop OpenSCAD workflow.

## Quick start

1. **Type the wording** into `sign_text_1`…`sign_text_6` (regular text — this
   becomes the raised letters).
2. **Translate the same wording** at
   <https://www.branah.com/braille-translator>:
   - Choose Grade 1 or Grade 2 braille.
   - Make sure the output is **Unicode Braille** (dot patterns like `⠓⠑⠇⠇⠕`),
     NOT ASCII Braille.
   - Paste it into `Line_1`…`Line_6`.
3. **Open `Braille_Sign_STL_Generator.scad`** in [OpenSCAD](https://openscad.org/)
   (2024.x or newer; nightly builds render fastest) and open the Customizer
   panel (View → Customizer).
4. Leave `auto_fit` = **Yes** and the plates grow so every row of letters and
   braille fits. The effective size prints to the console — the Customizer
   cannot display computed values in its sliders.
5. Pick `sign_part`: **Both** lays the plates side by side on the bed;
   **Letter plate** / **Braille plate** export one at a time.
6. **Render (F6)**, then **File → Export → Export as STL**.
7. **Print as modeled** — no slicer supports, no rotation.

## What the parameters do

| Tab | What it controls |
|-----|------------------|
| Sign Text - Raised Letters | `sign_text_1`…`sign_text_6`, plain text |
| Text Input - Pre-Translated Braille | `Line_1`…`Line_6`, Unicode braille |
| Sign Layout | `sign_part` (Both / Letter plate / Braille plate), auto-fit, plate sizes |
| Raised Letters | Character height, raise height, letter/line spacing, uppercase toggle |
| Border | Border width and raise, split between the two plates |
| Print Orientation | Angled (75°, default) or Flat for the braille plate |
| Support Fins | Fin spacing/offset/thickness, bridge count/size/contact, brim |
| Braille Dot Shape | `Rounded` (ADA-friendly dome, default) or `Cone` dots and their dimensions |
| Braille Spacing | Cell/line/dot spacing |
| Rendering Quality | Sphere quality and cone segments |

The default dot (Rounded, 1.6 mm base, 0.7 mm total height) stays inside the
2010 ADA Standards envelope. `font` is pinned to **Liberation Sans**, which is
in MakerWorld's installed font inventory, so the raised letters render
identically on the desktop, in CI, and on MakerWorld.

## Loading the included presets

`Braille_Sign_STL_Generator.json` sits next to the `.scad`, so OpenSCAD
auto-loads its parameter sets into the Customizer preset dropdown:

- **Default Sign (both plates)** — the first-run defaults.
- **Braille Plate Only (flat)** — one plate, printed dots-up.

Your own saved parameter sets go in the same dropdown via the Customizer's `+`
button. If you keep personal presets (names, contact info in braille), save them
to a file ending in `.local.json` — that pattern is gitignored so they never end
up in a public commit.

## Print guidance

- **Print as modeled.** With `sign_part` = Both, the letter plate lies flat and
  the braille plate leans back at 75° with its fins behind it. No slicer
  supports; a slicer brim is optional (a built-in brim is already modeled under
  each fin).
- **Layer height:** 0.1 mm gives noticeably smoother dots and crisper letters.
  PLA and PETG both work.
- **Slow the outer wall** (≤ 30–40 mm/s) and keep acceleration modest — a thin
  leaning plate is sensitive to ringing/vibration. Input shaping helps a lot.
- **Bridge contact tuning:** `bridge_contact_mm` (default 0.3) is how far each
  snap-off bridge merges into the plate. 0.3–0.4 mm connects reliably during the
  print and still snaps off clean. If bridges detach mid-print, increase it; if
  they're hard to remove, decrease it.
- **After printing:** flex or snip the fins off the braille plate's back, then
  deburr the small nubs the bridges leave with a fingernail or fine sandpaper.
- **Contrast** matters for the letter plate: ADA expects the characters to
  contrast with their background. Printing the plate in one colour and painting
  or filament-swapping the raised letters is the usual approach.

## Troubleshooting

| Symptom | Cause / fix |
|---------|-------------|
| `INVALID CHARACTERS` warning in the console | A `Line_N` contains regular text instead of Unicode braille. Re-translate at Branah with Unicode Braille output; the console says which line. |
| `TEXT TOO LONG` / plates keep growing | With `auto_fit` = Yes the plates grow to fit; long wording produces a large sign. Shorten the rows or split across more rows. |
| Sign bigger than my print bed | Check the effective size the console reports. Reduce the character height, shorten rows, or export the plates one at a time with `sign_part`. |
| Letters look thin or fused together | Raise `letter_spacing`, or increase `char_height_mm` — very small characters at 0.4 mm nozzle width lose definition. |
| Fins fall over / bridges break mid-print | Increase `bridge_contact_mm` (up to 0.4), add more `bridge_count`, or reduce `fin_interval_mm` so more fins share the load. |
| Fins won't snap off cleanly | Decrease `bridge_contact_mm` (down to 0.2) or reduce `bridge_width_mm` / `bridge_height_mm`. |
| Dots feel rough | Print at 0.1 mm layers, slow the outer wall, and consider the `Cone` dot shape, which some printers render more cleanly. |

## Upload to MakerWorld (Parametric Model Maker)

This is a single `.scad` file with no `include`/`use`, so it uploads to
[MakerWorld](https://makerworld.com/)'s Parametric Model Maker as-is:

1. Go to MakerWorld → **Create** → **Parametric Model Maker** (the
   OpenSCAD-based customizer).
2. Upload **only** `Braille_Sign_STL_Generator.scad`.
3. In the generated parameter panel, type the wording into `sign_text_1`… and
   paste Unicode braille into `Line_1`….
4. Generate / render and download the STL.

Notes:

- Customizer **`.json` presets do not upload** — MakerWorld only takes the
  `.scad`. The file's built-in defaults are the first-run experience there.
- Invalid-character feedback goes to `echo()`, and MakerWorld's Parametric Model
  Maker has **no visible OpenSCAD console** — so on MakerWorld that feedback is
  not reachable. The quick start's troubleshooting section is written around the
  visible symptom instead: an invalid character renders as a blank patch with no
  dots.
- **License choice at upload (owner decision):** this repository is under
  PolyForm Noncommercial 1.0.0, but MakerWorld requires choosing from its own
  license list (Creative Commons variants etc.), which does not offer PolyForm.
  Pick the closest match deliberately at upload time (e.g. a CC NonCommercial
  variant) — whatever is chosen governs the MakerWorld listing.

### Release documentation

- [`docs/MAKERWORLD_LISTING.md`](docs/MAKERWORLD_LISTING.md) — upload fields,
  description body, print profile notes, gallery plan with alt text, and the
  pre-publish checklist including the licensing gate and the ADA disclaimer.
- [`docs/MAKERWORLD_QUICK_START.md`](docs/MAKERWORLD_QUICK_START.md) — the user
  guide: what to include, Grade 2 translation, the customizer, the two-part
  print workflow, the ADA §703 evidence, troubleshooting, and the OpenSCAD
  Assistive Forge alternative.

Both are written to the shared
[Accessible MakerWorld Documentation Standard](https://github.com/BrennenJohnston/accessible-makerworld-doc-standard/blob/main/ACCESSIBLE_MAKERWORLD_DOC_STANDARD.md).

## Development / tests

```bash
pip install -r tests/requirements.txt
pytest tests -v
```

- `tests/test_customizer.py` — Customizer dropdown hygiene (no `value:Label`
  format, defaults match options, no duplicates) and preset/parameter
  consistency.
- `tests/test_source_guards.py` — source invariants read straight from the
  `.scad`: no `include`/`use` (MakerWorld single-file requirement), `sign_part`
  can export the plates together or separately, every row of raised letters has
  a matching braille row, and the font stays pinned to Liberation Sans.
- `tests/test_render_smoke.py` — renders the two-plate sign, the angled braille
  plate, and the letter plate through the OpenSCAD CLI and asserts each STL is
  watertight with the expected body count (auto-skips if OpenSCAD is not
  installed).

CI (GitHub Actions) runs lint + the quick tests on every push/PR and the render
smoke tests on Ubuntu with an OpenSCAD nightly AppImage.

## Research background

| Reference | Takeaway |
|-----------|----------|
| [Puerta et al., CHI 2024](https://doi.org/10.1145/3613904.3642719) — "The Effect of Orientation on the Readability and Comfort of 3D-Printed Braille" | Braille printed at 75–90° reads significantly faster and more comfortably than flat; 75° also reduces dot overhangs vs. 90°. The angled braille plate exists for this reason. |
| [masukomi, "Manual Support Fins for 3D Printing"](https://weblog.masukomi.org/2024/03/11/manual-support-fins-for-3d-printing/) | ~1 mm fin offset, a column of small sprues, side fins so edges don't float, 0.3–0.4 mm contact — the fin/bridge defaults follow this. |
| [2010 ADA Standards](https://archive.ada.gov/), section 703 | Character height, raise height, and dot dimension envelope behind the defaults. |
| [BANA size and spacing](https://brailleauthority.org/size-and-spacing-braille-characters) | Cell geometry and clear-space guidance behind the spacing defaults. |

## Related projects

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

## Credits

- **Brennen Johnston** — project owner; braille dot system and the leaning /
  break-away fin geometry.
- **Puerta, Crnovrsanin, South, Dunne (CHI 2024)** — the orientation research
  the angled braille plate is built on.
- **masukomi** and **Slant3D** — break-away support fin technique.

## License

**PolyForm Noncommercial 1.0.0** — free for personal, educational, and other
noncommercial use; modification and redistribution allowed under the same
terms; **no commercial use**. See [LICENSE](LICENSE).
