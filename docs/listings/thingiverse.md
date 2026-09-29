# Thingiverse listing — Braille Sign STL Generator

Status: ready to upload once the gallery photos are shot.

Written to the listing template of the shared
[Accessible MakerWorld Documentation Standard](https://github.com/BrennenJohnston/accessible-makerworld-doc-standard/blob/main/ACCESSIBLE_MAKERWORLD_DOC_STANDARD.md).
Thingiverse's upload pages could not be read on 2026-09-28, so each field below
is named by what it holds: check the form's own label at upload.

---

## Upload fields

| Field | Label on the form | Value |
|---|---|---|
| Model title | check at upload | `Braille Sign Generator - Two-Part Tactile Room Signs, ADA 703 Dimensions` |
| Category | check at upload | a signs or accessibility category, whichever the list offers |
| License | check at upload | CC BY-NC 4.0: the owner's pick for every platform, 2026-09-28 (Q-10), closest to the repository's PolyForm Noncommercial 1.0.0 |
| Files | check at upload | `restroom-letter-plate.stl`, `restroom-braille-plate.stl`, `exit-letter-plate.stl`, `exit-braille-plate.stl`, `stairs-letter-plate.stl`, `stairs-braille-plate.stl`, `room-101-letter-plate.stl`, `room-101-braille-plate.stl`, `Braille_Sign_STL_Generator.scad`, `Braille_Sign_STL_Generator.json`, and a link to [the quick start](../guides/quick-start.md) |
| Tags | check at upload | `braille`, `accessibility`, `assistive-technology`, `blindness`, `vision-impairment`, `tactile`, `signage`, `ada`, `room-sign`, `wayfinding`, `parametric`, `openscad` |
| External link 1 | check at upload | <https://github.com/BrennenJohnston/braille-sign-openscad> |
| External link 2 | check at upload | <https://openscad-assistive-forge.pages.dev/?example=braille-sign> |

The Thingiverse Customizer app is untested with this file. The file needs
OpenSCAD's `ord()`, `chr()` and `assert()`; OpenSCAD added `ord()` and
`assert()` in version 2019.05, and the app's page does not state which OpenSCAD
version it runs. This listing makes no promise that the Customizer works, and
the tags leave out `customizable` until the checklist's last item has tried it.

CC BY-NC 4.0 is Creative Commons Attribution-NonCommercial 4.0 International.
The owner chose it on 2026-09-28 for every platform; the repository itself stays
under PolyForm Noncommercial 1.0.0. Pick it deliberately rather than accepting
the form's default, and if the form's Creative Commons list names another
version, pick Attribution-NonCommercial and record the version here. The eight
STLs come from the repository's [`stl/` folder](../../stl/README.md), and the
`.scad` and its `.json` presets from the repository's root. The first external
link is the source repository; the second is the accessible browser version of
the same generator.

## Summary

A two-part tactile room sign, read by touch or by sight: a letter plate with
raised capital letters that prints flat, and a braille plate with the same words
that prints leaning back on break-away fins, the two joining into one framed sign
on the wall. Four signs come ready to print (Restroom, Exit, Stairs and Room 101),
and the OpenSCAD file makes one with your own wording. The dimensions follow the
2010 ADA Standards §703 figures, but the generator does **not** guarantee ADA
compliance: see the ADA note in the description.

## Description

*Paste into Thingiverse's description field (check at upload).*

**What this makes**

A room sign in two parts that people can read by sight or by touch. The
**letter plate** carries the words in raised capital letters (Liberation Sans)
and prints flat, letters up. The **braille plate** carries the same words in
braille and prints leaning back at 75 degrees on break-away support fins,
because braille printed on a steep face reads faster and more comfortably than
flat-printed braille (Puerta, Crnovrsanin, South and Dunne, CHI 2024). The letter
plate carries the top and side rails of a raised border and the braille plate the
bottom and side rails, so the two plates mounted touching read as one framed
sign.

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

With the plates mounted touching, the braille sits about 43 mm below the raised
letters on the default sign, more than the 9.5 mm (3/8 in) that §703.3.2 asks.

**Ready to print: four sample signs**

Each sample is two STL files, rendered from the generator at its defaults:

- `restroom-letter-plate.stl` and `restroom-braille-plate.stl`: RESTROOM
- `exit-letter-plate.stl` and `exit-braille-plate.stl`: EXIT
- `stairs-letter-plate.stl` and `stairs-braille-plate.stl`: STAIRS
- `room-101-letter-plate.stl` and `room-101-braille-plate.stl`: ROOM 101

Each letter plate is 160.0 × 70.0 × 3.8 mm and prints flat, letters up. Each
braille plate stands 165.2 × 17.0 × 39.0 mm on the bed and prints exactly as
modeled, leaning back on its fins. The samples' braille is lowercase Unified
English Braille (UEB) Grade 2 from liblouis, an open-source braille translator.

**An automatic translator is not a certified transcriber.** For a sign in a
public building, have the braille checked by a transcriber certified in UEB
before you print.

**Make your own sign in your browser**

The OpenSCAD Assistive Forge runs this generator in a panel built for screen
readers and keyboards, and translates your wording into braille on your own
device with liblouis:

<https://openscad-assistive-forge.pages.dev/?example=braille-sign>

The Forge keeps its own copy of the generator, so its settings can have older
names than the ones below.

**Make your own sign in desktop OpenSCAD**

With OpenSCAD 2021.01 or newer and `Braille_Sign_STL_Generator.scad`:

1. Open `Braille_Sign_STL_Generator.scad` in OpenSCAD.
2. Show the Customizer panel: Window > Customizer (in OpenSCAD 2021.01, untick
   Window > Hide Customizer).
3. Under **Step 1 - Pick a sample sign or type your own**, pick a sample in
   `sample_sign`, or leave it on `Type my own`.
4. With `Type my own`, type your wording into `text_line_1` to `text_line_6`,
   one line of the sign per dial.
5. Under **Step 2 - Braille, pasted from a translator**, paste each line's
   braille into the matching `braille_line_1` to `braille_line_6`.
6. Under **Step 3 - What to export**, set `sign_part` to `Letter plate`.
7. Under **Step 4 - Size**, leave `auto_fit` on `Yes`: the plates grow to fit
   your wording.
8. Press F6 to render the plate.
9. Export it as an STL with File > Export.
10. Set `sign_part` to `Braille plate`.
11. Repeat steps 8 and 9 for the braille plate.

The braille lines take Unicode braille, dot patterns such as ⠑⠭⠊⠞ (Exit), not
ASCII braille, which looks like ordinary letters. The Branah braille translator
(https://www.branah.com/braille-translator) gives it: choose Grade 2 Braille and
Unicode Braille, and type each line in lowercase. Its own page says its Grade 2
is still a work in progress, so check what it gives you, or use the Forge.

**Print settings**

The two plates want different settings, so print them as two jobs, each exactly
as modeled, with no slicer supports:

| Setting | Letter plate | Braille plate |
|---|---|---|
| On the bed | flat, letters up | leaning back on its fins |
| Layer height | 0.2 mm | 0.1 mm |
| Material | PLA or PETG | PLA or PETG |
| Supports | none | none |
| Brim | not needed | optional; one is modeled under each fin |
| Outer wall speed | normal | 30 to 40 mm/s or slower |

The braille plate gets the fine layers because a braille dot is at most 0.9 mm
(0.037 in) tall, so the layer height decides how smooth each dot feels. After
printing, flex or snip the fins off the back of the braille plate and smooth the
small nubs they leave. For contrast, the ADA Standards ask for raised letters
that contrast with their background: add a filament change on the letter plate
at the first layer above 3 mm, or paint the raised letters.

**Mounting, in three lines**

1. Push the plates together, letters above braille, until the side rails meet
   in one frame.
2. Stick them to the wall with the bottom row of braille at least 1220 mm
   (48 in) above the floor.
3. Keep the baseline of the top line of letters at most 1525 mm (60 in) above
   the floor.

**More help**

The quick start walks through every step:
https://github.com/BrennenJohnston/braille-sign-openscad/blob/main/docs/guides/quick-start.md

**Credits**

- Design and code: Brennen Johnston.
- Orientation research: Puerta, Crnovrsanin, South, Dunne (CHI 2024).
- Break-away support fin technique: masukomi, "Manual Support Fins for 3D
  Printing," and Slant3D.
- Braille dot system and the leaning / fin geometry from the braille wedge card
  generator, this project's parent.
- The samples' braille: liblouis.

## Print settings

Short facts for the platform's print settings fields, if its form has them
(check at upload); the description carries the same as text.

| Setting | Letter plate | Braille plate |
|---------|--------------|---------------|
| Layer height | 0.2 mm | 0.1 mm |
| Material | PLA or PETG | PLA or PETG |
| Supports | none | none (fins modeled) |
| Brim | not needed | optional (one is modeled per fin) |
| Orientation | as modeled, flat | as modeled, leaning 75° |
| Outer wall speed | normal | 30–40 mm/s |

## Gallery plan

The same seven pictures as the MakerWorld listing, with the same alt texts.

1. **Cover — a mounted sign being read.** Both plates mounted on a door frame or
   wall, letters above braille, with a hand on the braille.
   **Alt text:** A two-part printed sign mounted on a wall, reading "Room 101" in
   raised uppercase letters above a braille line, with a hand reading the braille.

2. **The two plates apart.** Both plates side by side on a desk, showing the split
   border.
   **Alt text:** Two printed plates side by side. The upper plate carries raised
   uppercase letters and border rails along its top and sides; the lower plate
   carries braille and border rails along its bottom and sides.

3. **Braille plate on the bed, fins attached.** Side view showing the 75° lean and
   the row of fins.
   **Alt text:** Side view of the braille plate as it comes off the printer,
   leaning back about 75 degrees with several thin triangular support fins
   standing behind it.

4. **Letter plate printing flat.** Top view on the bed.
   **Alt text:** The letter plate lying flat on the print bed with its raised
   uppercase characters facing up.

5. **Dot close-up.** Macro of a braille cell on the finished plate.
   **Alt text:** Close-up of raised braille dots on the sign plate, each dot a
   smooth dome about 1.6 millimeters wide and 0.7 millimeters tall.

6. **Character height with a scale.** Ruler or calipers against a raised
   character.
   **Alt text:** Calipers measuring a raised character on the letter plate at
   about 16 millimeters tall.

7. **Multi-line sign.** A three- or four-line example, both plates.
   **Alt text:** A two-part printed sign with three lines of raised text above
   three matching lines of braille, the plates grown taller to fit.

The cover must be a photograph of the actual printed object, not a render.

## Pre-publish checklist

- [x] **License pick recorded.** CC BY-NC 4.0, the owner's pick for every
      platform on 2026-09-28 (Q-10). Select it deliberately on the upload form.
- [ ] **ADA note present in the description,** near the top. Keep it.
- [ ] **The eight STLs uploaded,** each named as in
      [`stl/README.md`](../../stl/README.md).
- [ ] **The `.scad` uploaded as a source file,** with
      `Braille_Sign_STL_Generator.json` beside it.
- [ ] **Every image has its alt text:** in the uploader's alt text field if it
      has one (check at upload), otherwise pasted into the description, one line
      per picture.
- [ ] **The cover is a real print photo,** ideally the mounted sign.
- [ ] **The quick start linked** from the description, and the link opens: it
      points at `main`, where `docs/guides/quick-start.md` arrives when the
      round's pull requests are merged.
- [ ] **Try the Customizer app once.** If it renders, add the `customizable` tag;
      if not, say so in the description.
