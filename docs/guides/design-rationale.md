# Design rationale

Every default in the generator has a reason. This page gives each one in the
same shape: the decision, the number, the evidence, and what you may change.
The numbers were measured on the files in this repository, and each one names
where it came from.

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

## Two plates, and the braille plate leans back 75°

**The decision.** The sign is two plates. The letter plate prints flat,
letters up. The braille plate prints leaning back on break-away fins:
`print_orientation` is `Angled` and `face_angle_deg` is 75.

**The number.** 75 degrees from the bed. The leaning plate is sunk 0.6 mm into
the bed and cut flat there, so its bottom edge has a real first-layer strip
instead of a knife edge. A fin stands at each end and every 25 mm between
(`fin_interval_mm`): eight fins on the default 160 mm sign. All of these are
in `Braille_Sign_STL_Generator.scad`.

**The evidence.** The Accessible MakerWorld Documentation Standard, section 2,
copied here as it stands:

> **Puerta, Crnovrsanin, South, Dunne — "The Effect of Orientation on the
> Readability and Comfort of 3D-Printed Braille," CHI 2024.** DOI
> [10.1145/3613904.3642719](https://doi.org/10.1145/3613904.3642719)
>
> Why it matters: braille printed on a face angled **75°–90°** from the print
> bed was read significantly faster and more comfortably than flat-printed
> braille, because near-vertical printing moves the layer seams off the surface
> the finger reads. **75°** rather than 90° is the working choice here because it
> reduces the overhang under each dot.

That finding is about braille dots, not raised letters. A dot is 1.6 mm
across, so a layer seam over its crown is a large part of it, and a finger
feels it. A raised letter 16 mm tall is coarse enough that seams do not
matter, and printing it flat gives a cleaner top than any angle would. One
plate would force both kinds of text into one orientation, so the sign is two
plates. At 90 degrees the underside of every dot would be a flat overhang; at
75 degrees the face tilts back and each dot's underside becomes a gentle slope
that prints without supports. The fins, bridges and brims exist to make that
angle printable in one pass.

**What you may change.** `face_angle_deg` runs from 60 to 90; 75 to 90 reads
best, and 75 needs no slicer supports. `print_orientation` `Flat` prints the
braille plate dots up, which puts the layer seams across the dots. The fin,
bridge and brim dials change how the fins hold and how easily they snap off.

## The letter dimensions

**The decision.** `letter_height_mm` is the printed height of the capital I,
16 mm by default. The letters rise 0.8 mm (`letter_raise_mm`), the lines sit
135 % of the letter height apart (`letter_line_spacing_pct`), the spacing
factor is 1.1 (`letter_spacing_factor`), `force_uppercase` is `Yes`, and the
font is Liberation Sans, a sans serif.

**The number.** Liberation Sans draws its capital I at 0.9555 of the font
size: 15.288 mm at size 16, measured before this dial changed meaning. The file
divides `letter_height_mm` by 0.9555 before it sets the size, so the dial at
16 prints an I 16.000 mm tall, at 12 prints 12.000 mm and at 50 prints
49.999 mm. At 16 the O is 99.2 % as wide as the I is tall, the I's stroke is
13.6 % of its height, and two I's sit 4.939 mm apart. Auto-fit's width
estimate came out 0.45 % and 1.16 % wider than the printed letters on its two
test lines, never narrower. All measured on meshes rendered from the file
(`tests/test_ada_figures.py` checks the I and the estimate).

**The evidence.** The standard's section 2, copied as it stands:

> **2010 ADA Standards for Accessible Design, §703.**
> <https://archive.ada.gov/>
>
> Why it matters: §703.3 fixes the braille dot envelope (base 1.5–1.6 mm, height
> 0.6–0.9 mm, domed not pointed); §703.2 fixes raised-character height (minimum
> 15.9 mm / 5/8 in) and relief (minimum 0.8 mm / 1/32 in). Cited as a dimensional
> envelope, **never as a compliance claim** — see §5.

The block's "§5" is the documentation standard's own section on compliance
language. 5/8 in is 15.875 mm; the 2010 Standards print it as "5/8 inch
(16 mm)", and 16 mm is the figure this generator uses. The rest of 703.2, from the Standards'
own text: characters uppercase (703.2.2) and sans serif (703.2.3); the O's
width 55 to 110 % of the I's height (703.2.4); height 16 mm (5/8 in) minimum
and 51 mm (2 in) maximum on the uppercase I, or 13 mm (1/2 in) where separate
raised and visual characters carry the same information (703.2.5); the I's
stroke at most 15 % of its height (703.2.6); 3.2 mm (1/8 in) minimum and four
times the stroke maximum between letters with square sides (703.2.7); lines
135 to 170 % of the letter height apart (703.2.8); relief 0.8 mm (1/32 in)
minimum (703.2.1).

The dial means the printed height because 703.2.5 measures the printed capital
I. When the dial set the font size instead, 16 printed an I 15.288 mm tall,
under the figure, while every document said 16 mm.

**What you may change.** `letter_height_mm` runs from 12 to 50 mm; under 16
the preview shows LETTERS UNDER 16 MM and the console prints a note, but the
sign still renders, because a smaller sign has uses outside the ADA Standards.
`letter_raise_mm` and `letter_line_spacing_pct` stay wide too, and print a
console note outside the ADA figures; `letter_spacing_factor` has no check.
The font is fixed.

## The dot geometry and the 6.5 mm cell pitch

**The decision.** The default Rounded dot is a base 1.6 mm across narrowing to
a 1.4 mm dome, 0.35 mm of base plus 0.35 mm of dome: 0.7 mm tall. Cells are
6.5 mm apart (`braille_cell_spacing_mm`), dots in a cell 2.5 mm
(`braille_dot_spacing_mm`), braille lines 10.0 mm (`braille_line_spacing_mm`).

**The number.** Measured on the plate, a dot stands 0.676 mm proud of the face
on a base ring 1.589 mm across: the 0.7 mm dot sinks 0.02 mm into the face to
fuse with it. At the 6.5 mm pitch, the default ten-cell braille line is
57.4 mm wide.

**The evidence.** ADA Table 703.3.1, from the Standards' own text: dot base
diameter 1.5 to 1.6 mm (0.059 to 0.063 in); dot height 0.6 to 0.9 mm (0.025 to
0.037 in); dots in a cell 2.3 to 2.5 mm (0.090 to 0.100 in) apart; matching
dots in neighboring cells 6.1 to 7.6 mm (0.241 to 0.300 in); a cell and the
cell directly below 10 to 10.2 mm (0.395 to 0.400 in), all center to center;
the dots domed or rounded. And from the standard's section 2, as they stand:

> **ISO 17049:2013, *Accessible design — Application of braille on signage,
> equipment and appliances*.**
> <https://www.iso.org/standard/58090.html>
>
> Why it matters: the international dot geometry range. Where ADA and ISO 17049
> overlap — dot base **1.5–1.6 mm**, dot height **0.6–0.7 mm**, cell pitch
> **6.1–6.8 mm**, line pitch **10.0–10.2 mm** — is the safest target for a model
> that may be read by someone trained on either standard.

> **BANA, *Size and Spacing of Braille Characters*.**
> <https://brailleauthority.org/size-and-spacing-braille-characters>
>
> Why it matters: the source for cell spacing, line spacing, and within-cell dot
> spacing. Dots that are geometrically legal but spaced wrong are unreadable.

The default dot sits inside the overlap: base 1.6 mm, height 0.7 mm, pitch
6.5 mm, line pitch 10.0 mm. The pitch was 7.0 mm, inside ADA but outside the
overlap, and the owner's braille rulebook says 6.5, so the default moved.

The base under the dome is there because a dome alone, kept within a 1.6 mm
base, can be at most 0.8 mm tall: a half sphere is as tall as it gets. The
base lets the dot reach the upper part of the height range at the full base
width, and on the leaning plate it turns the dot's underside into a slope
that prints.

**What you may change.** Every braille slider spans Table 703.3.1 and no
further, and a check in the file stops the render if a preset or a
command-line value goes outside it. `dot_shape` `Cone` gives a pointed dot
with a flat top for printers that print Rounded badly; it is not the domed
shape ADA asks for.

## The 9.5 mm braille clearance

**The decision.** Auto-fit keeps the braille `braille_clearance_mm` (9.5 mm)
inside the border rails; the letters keep 4 mm.

**The number.** On a six-line sign, the braille sits 9.505 mm from the bottom
rail, measured where each dot meets the face (`tests/test_ada_figures.py`
checks it). Before the dial existed it sat 4.005 mm away.

**The evidence.** ADA 703.3.2, from the Standards' own text: "Braille shall be
separated 3/8 inch (9.5 mm) minimum from any other tactile characters and 3/8
inch (9.5 mm) minimum from raised borders and decorative elements." With the
plates touching on the wall, the braille sits 43.473 mm below the lowest
letter on the default sign and 17.505 mm on the six-line sign, measured in the
files.

**What you may change.** `braille_clearance_mm` runs from 9.5 to 20 mm; a
check stops the render below 9.5. With `auto_fit` off, braille that fits the
plate but not with this space shows BRAILLE TOO CLOSE TO BORDER.

## The split border

**The decision.** The letter plate carries the top rail and both side rails;
the braille plate carries the bottom rail and both side rails.

**The number.** Rails 2 mm wide (`border_width_mm`) and 0.8 mm high
(`border_height_mm`), the same height as the letters' relief.

**The evidence.** Mounted touching, letters above braille, the rails join
into one continuous frame. The frame is a tactile boundary: a hand sweeping
the sign finds its edge and knows where the content starts and stops. Both
plates always share one width, so the side rails line up.

**What you may change.** `add_border` `No` leaves both plates without rails;
`border_width_mm` and `border_height_mm` change their size, and auto-fit
counts the width in its spaces.

## The sample signs

**The decision.** `sample_sign` offers Restroom, Exit, Stairs and Room 101.
Their braille is Unified English Braille (UEB) Grade 2 from liblouis, the
open-source translator the OpenSCAD Assistive Forge also uses, written into
`scripts/sample_signs.json` by `scripts/generate_sample_braille.mjs` and never
typed by hand. The braille is lowercase.

**The number.** 7, 4, 5 and 9 braille cells.

**The evidence.** ADA 703.3 asks for contracted braille, Grade 2, on signs.
ADA 703.3.1 allows the braille capital sign only before the first word of a
sentence, proper nouns and names, single letters, initials and acronyms, and a
room name on a sign is none of those, so the owner chose lowercase braille for
the samples. The raised letters are capitals regardless, as 703.2.2 asks.
Tests keep the file's sample tables and the full guide's sample table the
same as the data file.

**An automatic translator is not a certified transcriber.** The samples'
braille has not been checked by one; for a sign in a public building, have a
transcriber certified in UEB check the braille.

**What you may change.** Leave `sample_sign` on `Type my own` and type your
own wording and braille. To change a sample, change the generator script's
input and run it again; the tests fail until the file's tables match.

## Warnings in the preview only

**The decision.** When the generator finds a problem, it draws red words
beside the sign in the desktop preview (orange for the sample note) and
prints the same problem to the console. The words are drawn with OpenSCAD's
background modifier, so they never reach a render or an STL. The owner chose
this over a red tag printed on the bed and over console messages alone.

**The number.** Each message is a line of text 5 mm tall, lying flat 10 mm
beyond the sign's far edge, one line per problem.

**The evidence.** `tests/test_render_smoke.py` renders a sign with a warning
firing, with the words on and off, and finds the two exports identical in
volume, area and bounds to six decimals. MakerWorld's Parametric Model Maker
shows the rendered model, not OpenSCAD's preview or console, so it shows none
of the words; the MakerWorld quick start describes what each problem looks
like there instead.

**What you may change.** `show_warnings` `No` hides the words; the console
still prints every problem.

## 0.1 mm layers for the braille plate

**The decision.** Print the braille plate at 0.1 mm layers; 0.2 mm is fine for
the letter plate.

**The evidence.** The standard's section 2, copied as it stands:

> **Barros, Correia, Teixeira — "Towards the Effectiveness of 3D Printing on
> Tactile Content Creation," Polymers 2023, 15(9):2180.** DOI
> [10.3390/polym15092180](https://doi.org/10.3390/polym15092180)
>
> Why it matters: measured FDM tactile output on a 0.4 mm nozzle at 0.1 mm
> layers. This is the basis for the 0.1 mm layer-height guidance — dot height is
> capped at 0.9 mm by the braille standards, so layer height is the only lever
> left for how smooth a dot feels.

Printed flat, a 0.7 mm dot is seven layers at 0.1 mm and only three or four at
0.2 mm, and a few layers make a staircase a fingertip notices before the dot.

**What you may change.** Layer height is your slicer's setting, not the
file's.

## Print settings as text

**The decision.** Every print setting is written out in words, in the quick
start's [Printing](quick-start.md#printing) section and the Maker Guide's
[4. Print](maker-guide.md#4-print), never only in a slicer profile or a
picture.

**The evidence.** The standard's section 2, copied as it stands:

> **Ballarin, Stangl, Oswal, Whiting — "A Framework-Informed Analysis of
> Accessibility Barriers in Desktop 3D Printing Software," DIS 2025 Companion,
> pp. 477–482.** DOI
> [10.1145/3715668.3736342](https://doi.org/10.1145/3715668.3736342)
>
> Why it matters: measured with NVDA that Cura, PrusaSlicer, and Bambu Studio
> hide much of their interface from the accessibility APIs screen readers use —
> print settings unreachable, controls unlabelled, print errors unannounced.
> This is why a listing must state print settings **as text** and why a
> ready-sliced print profile is an accessibility feature: it removes a step the
> user may not be able to complete.

**What you may change.** Nothing in the file: the settings are advice for
your slicer.
