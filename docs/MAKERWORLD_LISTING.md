# MakerWorld Listing — Braille Sign STL Generator

Status: ready to upload once the gallery photos are shot.

Written to the shared
[Accessible MakerWorld Documentation Standard](https://github.com/BrennenJohnston/accessible-makerworld-doc-standard/blob/main/ACCESSIBLE_MAKERWORLD_DOC_STANDARD.md).

---

## Upload fields

| Field | Value |
|-------|-------|
| Model title | `Braille Sign Generator - Two-Part Tactile Room Signs, ADA 703 Dimensions (Parametric)` |
| Designer | Brennen Johnston |
| Category | Education > Other Education Models |
| License | CC BY-NC 4.0 (the repository is PolyForm Noncommercial 1.0.0; MakerWorld does not offer it; the owner's pick, 2026-09-28, Q-10) |
| Upload file | `Braille_Sign_STL_Generator.scad` — this one file only |
| Tags | `braille`, `accessibility`, `assistive-technology`, `blindness`, `vision-impairment`, `tactile`, `signage`, `ada`, `room-sign`, `wayfinding`, `customizable`, `parametric`, `openscad` |
| External link 1 | <https://openscad-assistive-forge.pages.dev/?example=braille-sign> |
| External link 2 | <https://github.com/BrennenJohnston/braille-sign-openscad> |

MakerWorld's license list does not offer PolyForm Noncommercial 1.0.0, the
repository's license, so the owner chose CC BY-NC 4.0 (Creative Commons
Attribution-NonCommercial 4.0 International) on 2026-09-28. Pick it deliberately
at upload time rather than accepting the form's default. The first external link
is the accessible browser version of the same generator; the second is the source
repository.

## Summary

A parametric generator for two-part tactile room signs, read by touch or by
sight, following the 2010 ADA Standards §703 dimensional figures: a letter plate
with raised uppercase characters that prints flat, and a braille plate carrying
the same wording that prints leaning back at 75° for the crispest dots. Pick one
of four sample signs, or type your own wording and paste pre-translated braille,
and both plates size themselves to fit. Mounted touching, letters above braille,
their split raised border joins into one continuous tactile frame.

This tool does **not** guarantee ADA compliance — see the note in the
description.

## Description

*Paste into MakerWorld's description body.*

**What this makes**

Two plates that together form one sign.

The **letter plate** carries raised uppercase characters in Liberation Sans. It
prints flat, letters up, and it carries the top and side rails of the sign's
raised border.

The **braille plate** carries the same wording in braille. It prints leaning back
75 degrees on modeled break-away support fins, and it carries the bottom and
side rails of the border.

Mounted touching, letters above braille, the two sets of border rails join into
one continuous frame — which is both how the sign should look and a tactile
boundary a hand can find before it starts reading.

At the shipped defaults the sign is 160 millimeters wide with a 70 millimeter
letter plate and a 40 millimeter braille plate, both 3 millimeters thick.
Auto-fit is on by default, so those become minimums: the plates grow to fit
whatever wording you enter, up to six lines.

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

With the plates mounted touching, the braille sits about 43 millimeters below the
raised letters on the default sign, more than the 9.5 millimeters (3/8 inch) that
§703.3.2 asks.

**An automatic translator is not a certified transcriber.** For a sign going into
a public building, have the braille checked by a transcriber certified in Unified
English Braille (UEB) first.

**What dimensions the defaults follow**

| Default | §703 figure |
|---|---|
| Character height 16.0 mm, on the capital I | §703.2.5, 16 mm (5/8 in) minimum |
| Character relief 0.8 mm | §703.2.1, 0.8 mm (1/32 in) minimum |
| Line spacing 135% of character height | §703.2.8, 135 to 170% |
| Uppercase characters | §703.2.2 |
| Liberation Sans, sans-serif | §703.2.3 |
| Braille dot 1.6 mm base, 0.7 mm tall, domed | §703.3.1, and the ADA / ISO 17049 overlap |
| Cell spacing 6.5 mm, line spacing 10.0 mm, dot spacing 2.5 mm | §703.3.1, and BANA *Size and Spacing of Braille Characters* |
| Braille 9.5 mm from the border | §703.3.2 |

Below 16 millimeters, desktop OpenSCAD flags the letters in its preview and its
console; MakerWorld shows neither, so keep `letter_height_mm` at 16 or more. The
slider goes down to 12 because a smaller sign has uses outside the ADA Standards,
but below 16 the sign no longer matches the published figure and should not be
described as following it.

**What you need to supply**

Your wording as plain text, and the same wording as pre-translated Unicode
braille, because MakerWorld's customizer cannot translate. A sample sign needs
neither: it brings its own.

Translate at the Branah braille translator
(https://www.branah.com/braille-translator): choose **Grade 2 Braille**
(contracted braille, which §703.3 asks for on signs) and **Unicode Braille**
output, which looks like dot patterns such as ⠑⠭⠊⠞ (Exit), rather than
ASCII or BRF braille, which looks like ordinary letters. Branah's own page says
its Grade 2 is still a work in progress, so check what it gives you. Type each
line in lowercase, keeping a capital only at the start of a sentence and for
names, single letters, initials and acronyms. Translate each line separately so
the braille lines match the text lines.

If you would rather skip the translator, the accessible browser version linked
above translates for you on your own device, with UEB Grade 2 as its default.

**Using the customizer**

1. Under **Step 1 - Pick a sample sign or type your own**, pick a sample sign in
   `sample_sign`, or leave it on `Type my own`. A sample brings its own wording
   and braille: skip to step 4.
2. With `Type my own`, type your wording into `text_line_1` through
   `text_line_6`, one line of the sign per dial.
3. Under **Step 2 - Braille, pasted from a translator**, paste the matching
   Unicode braille into `braille_line_1` through `braille_line_6`. The dials
   pair up: `text_line_2` and `braille_line_2` are the same line of the sign in
   two scripts.
4. Under **Step 3 - What to export**, set `sign_part` to `Letter plate`: the two
   plates need different layer heights, so you export them one at a time. Leave
   `print_orientation` on `Angled`; it affects the braille plate only.
5. Under **Step 4 - Size**, leave `auto_fit` on `Yes`. The plates grow to fit
   both scripts and the size sliders become minimums.
6. Generate the model.
7. Download the STL: this is the letter plate.
8. Set `sign_part` to `Braille plate`.
9. Generate the model again.
10. Download the STL: this is the braille plate.

**Important: MakerWorld does not show this model's warnings.** Desktop OpenSCAD
shows each problem as red words beside the sign in its preview and as a line in
its console; MakerWorld's customizer shows neither. Leaving `auto_fit` on `Yes`
prevents every size problem it would warn about. Two to watch for by eye: a
braille line with blank cells or no dots at all means that line is not Unicode
braille, and a sign that shows a sample's wording instead of yours means
`sample_sign` is not on `Type my own`. The quick start guide linked below lists
every symptom.

**Print settings**

The two plates want different settings, so print them as two jobs.

*Letter plate:* flat, letters up. 0.2 millimeter layers are fine — the characters
rise 0.8 millimeters and stand 16 millimeters tall, coarse features that print
cleanly at ordinary resolution. No supports.

*Braille plate:* exactly as modeled, leaning back 75 degrees. 0.1 millimeter
layers. Braille standards cap dot height at 0.9 millimeters, so layer height is
essentially the only lever on how smooth a dot feels. No slicer supports — the
fins are already modeled with a brim underneath. Slow the outer wall to 30–40
millimeters per second; a thin leaning plate rings badly at speed, and input
shaping helps a lot. After printing, flex the fins off the back and deburr the
small nubs the bridges leave.

If the fins fall over or the bridges break mid-print, raise `bridge_contact_mm`
toward 0.4 millimeters or add more `bridge_count`. If the fins will not snap off
cleanly, lower `bridge_contact_mm` toward 0.2 millimeters.

PLA and PETG both work.

**Contrast.** ADA signage requires characters that contrast with their
background, and a single-color print does not. If your printer can change
filament mid-print, the raised characters and the border are the parts to change
color. Otherwise plan to paint them.

**Why the sign is two plates**

Braille printed on a face angled 75–90 degrees from the print bed reads
significantly faster and more comfortably than flat-printed braille, because
near-vertical printing moves the layer seams off the surface your finger reads.
That result is from Puerta, Crnovrsanin, South and Dunne, "The Effect of
Orientation on the Readability and Comfort of 3D-Printed Braille," CHI 2024
(https://doi.org/10.1145/3613904.3642719).

That finding applies to braille dots and not to raised letters. A braille dot is
1.6 millimeters wide, so a layer seam across its crown is a large fraction of the
feature and a reading finger feels it. A 16 millimeter raised character is coarse
enough that seams do not matter, and printing it flat gives a cleaner top face
than any angle would.

One plate would force both scripts into the same orientation. Two plates let each
script print the way it wants to. That is the whole reason for the design.

Seventy-five degrees rather than ninety, because on a near-vertical face the dots
stick sideways out of a wall and the underside of every dot is an overhang. At 90
degrees that overhang is nearly horizontal; at 75 the face tilts back 15 degrees
and the dot undersides become gentle cones that print support-free.

**An accessible alternative**

This generator also runs as a built-in tool in **OpenSCAD Assistive Forge**, an
accessibility-first browser customizer:
https://openscad-assistive-forge.pages.dev/?example=braille-sign

It translates plain English to braille on your device with liblouis (UEB Grade 2
by default, which is the signage convention), is built for screen readers and
keyboard navigation, saves presets, works offline once installed, and names your
downloads after their content. Use it if the customizer here is difficult with
your screen reader. The Forge renders on your own device; MakerWorld renders on
its servers.

**Quick start guide**

Step-by-step help, and what each problem looks like on MakerWorld:
https://github.com/BrennenJohnston/braille-sign-openscad/blob/main/docs/MAKERWORLD_QUICK_START.md

**Credits**

- Design and code: Brennen Johnston.
- Orientation research: Puerta, Crnovrsanin, South, Dunne (CHI 2024).
- Break-away support fin technique: masukomi, "Manual Support Fins for 3D
  Printing," and Slant3D.
- Braille dot system and the leaning / fin geometry from the braille wedge card
  generator, this project's parent.

Sibling generators using the same technique: a braille card generator for longer
text, and a braille charm, pendant and bracelet-clip generator.

## Print profile notes

There is no `.3mf` to attach — this is a parametric model and the geometry depends
on the user's wording. The settings are stated as text in the description.

If print profiles are added later there should be **two**, one per plate, because
they differ in layer height. Each needs its own photograph of the actual printed
result.

| Setting | Letter plate | Braille plate |
|---------|--------------|---------------|
| Layer height | 0.2 mm | 0.1 mm |
| Material | PLA Basic or PETG | PLA Basic or PETG |
| Supports | none | none (fins modeled) |
| Brim | not needed | optional (one is modeled per fin) |
| Orientation | as modeled, flat | as modeled, leaning 75° |
| Outer wall speed | normal | 30–40 mm/s |

## Gallery plan

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
MakerWorld requires at least one real print photo per model and per print
profile.

## Pre-publish checklist

- [x] **License pick recorded.** CC BY-NC 4.0, the owner's pick on 2026-09-28
      (Q-10): MakerWorld does not offer the repository's PolyForm Noncommercial
      1.0.0. Select it deliberately on the upload form.
- [ ] **ADA disclaimer present in the description.** Non-negotiable. The note is
      written above — keep it, and keep it near the top rather than buried at the
      end.
- [ ] **Single-file requirement verified.** Run `pytest tests -v` —
      `test_source_guards.py::TestMakerWorldSingleFile` asserts there is no
      `include`/`use` in the `.scad`, and the same file pins the font to
      Liberation Sans.
- [ ] **Customizer dropdown hygiene verified.** Same run: `test_customizer.py`
      checks for `value:Label` option syntax, defaults missing from their own
      option list, and duplicate options.
- [ ] **Font availability confirmed in the Creator Portal.** The `.scad` hardcodes
      Liberation Sans. Render on MakerWorld and confirm the letters appear — a
      missing font renders as nothing, and there is no console to tell you why.
- [ ] **Creator Portal smoke test.** Upload, render `sign_part = Both` at the
      defaults, then render each plate separately and confirm the two exports have
      matching widths. Pick one sample sign in `sample_sign` and confirm its
      braille dots appear.
- [ ] **Warning-blindness acknowledged in the description.** MakerWorld shows
      neither the console nor the desktop preview's red warning words, so the
      description must tell the user to leave `auto_fit` on and what to look for
      on the model. That paragraph is written above — keep it.
- [ ] **Every gallery image has alt text pasted into MakerWorld's field.**
- [ ] **Cover photo is a real printed object,** and ideally a mounted one, since
      mounting is the part the generator cannot do for the user.
- [ ] **Quick start linked from the description** — the description carries the
      GitHub link to [`MAKERWORLD_QUICK_START.md`](MAKERWORLD_QUICK_START.md);
      keep it, or paste the guide's content into the instructions area.
