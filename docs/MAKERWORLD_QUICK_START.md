# MakerWorld Quick Start — Braille Sign

This guide takes you from "I need a room sign with braille on it" to two
downloadable, print-ready STLs, using
[`Braille_Sign_STL_Generator.scad`](../Braille_Sign_STL_Generator.scad) on
[MakerWorld](https://makerworld.com/)'s Parametric Model Maker. That one file is
the whole upload.

The generator makes a **two-part sign**: a **letter plate** carrying raised
uppercase characters, and a **braille plate** carrying the same wording in
braille. They are separate plates because they want opposite print orientations —
raised letters print best flat, braille prints best leaning back. Mounted
together with the letters above the braille, their split borders form one
continuous tactile frame.

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

---

## 1. What to include

A sign says one thing. The 2010 ADA Standards require **uppercase** raised
characters at least **15.9 mm (5/8 in)** tall, which sets the scale: at the
default 16 mm character height and 135% line spacing, each line of text is about
21.6 mm of plate height before margins.

- `sign_text_1` through `sign_text_6` hold up to six lines of raised text.
  `Line_1` through `Line_6` hold the matching braille. **They pair up** —
  `sign_text_2` and `Line_2` are the same line of the sign in two scripts.
- Leave `auto_fit` on `Yes` and the plates grow to fit whatever you enter, so
  there is no fixed capacity to plan around. The default `sign_width_mm` of
  160 mm and plate heights of 70 mm (letters) and 40 mm (braille) become minimums.
- Keep it to what a person needs at a doorway: a room number, a room name, a
  direction. `Room 101`. `Exit`. `Staff Only`. Long sentences belong on a
  document, not a sign.
- Braille takes roughly three times the space of print, so the braille plate is
  usually the one that forces the sign wider.

## 2. Translate your text

MakerWorld's customizer cannot translate English for you. You type your plain
text into `sign_text_N` for the raised letters, and separately paste
**pre-translated Unicode braille** — the dot characters in the range
U+2800–U+28FF — into `Line_N`.

1. Open a braille translator such as
   <https://www.branah.com/braille-translator>.
2. Choose **Grade 2** (contracted braille, where common words and letter groups
   are shortened) for signage. Grade 2 is the convention for permanent tactile
   signs and it is what most adult braille readers read fluently. Grade 1
   (uncontracted) is available and is not wrong, just longer.
3. Make sure the output is **Unicode braille**, not ASCII/BRF braille. Unicode
   braille looks like dot patterns (`⠠⠗⠕⠕⠍`); ASCII braille looks like ordinary
   letters and punctuation and will not work.
4. Translate **each line separately** so the braille lines match the text lines.
5. Copy each result into the matching `Line_N`.

The shipped default is `sign_text_1` = `Room 101` with `Line_1` =
`⠠⠗⠕⠕⠍⠀⠼⠁⠚⠁`. Replace both.

**An automatic translator is not a certified transcriber.** For a sign that will
be installed in a public building, have the braille checked by a UEB-certified
transcriber before you print a set.

## 3. Using the customizer

1. Go to MakerWorld → **Create** → **Parametric Model Maker** and upload
   **only** `Braille_Sign_STL_Generator.scad`.
2. Type your wording into `sign_text_1` … `sign_text_6` under **Sign Text -
   Raised Letters**. Leave unused lines empty.
3. Paste the matching Unicode braille into `Line_1` … `Line_6` under **Text
   Input - Pre-Translated Braille**.
4. Leave `auto_fit` on `Yes` under **Sign Layout**. The plates then grow to fit
   both scripts, treating `sign_width_mm`, `letter_plate_height_mm`, and
   `braille_plate_height_mm` as minimums. Turning it off means you are
   responsible for the sign being big enough.
5. Leave `sign_part` on `Both` to lay both plates side by side on the bed with
   `part_gap_mm` (default 8 mm) between them. Set it to `Letter plate` or
   `Braille plate` to export one at a time — useful when you want different print
   settings per plate, which you usually do.
6. Leave `print_orientation` on `Angled` and `face_angle_deg` on 75. This affects
   the **braille plate only**; the letter plate always prints flat.
7. Leave `force_uppercase` on `Yes`. ADA §703.2.2 requires uppercase raised
   characters.
8. Generate and render, then download the STL.

Everything else has a working default. The parameters worth knowing about:

| Section | What it controls |
|---------|------------------|
| Raised Lettering - ADA 703 | `char_height_mm` (16), `letter_raise_mm` (0.8), `line_spacing_pct` (135), `letter_spacing` (1.1), `force_uppercase` |
| Border | Split raised border: `add_border`, `border_width_mm` (2), `border_height_mm` (0.8) |
| Support Fins (Angled) | Fin interval, offset, thickness, height; bridge count, size, contact; brim |
| Braille Dot Shape | `dot_shape` (`Rounded` default or `Cone`), `cell_spacing` (7.0), `line_spacing` (10.0), `dot_spacing` (2.5) |
| Braille Dot Shape - Rounded / Cone | Dot dimensions for the selected shape |
| Rendering Quality | `render_quality` (default `Medium`) and `cone_segments` |

The font is fixed at Liberation Sans and is not a parameter. It is a sans-serif
face, which is what §703.2.3 asks for, and it is a font MakerWorld's renderer
reliably has.

## 4. The two-part workflow

This is the part that surprises people, so it is worth being explicit: **the two
plates want different print settings, so print them as two jobs.**

| | Letter plate | Braille plate |
|--|--------------|---------------|
| Orientation | flat, letters up | leaning back 75° |
| Supports | none | none (modelled fins) |
| Layer height | 0.2 mm is fine | 0.1 mm |
| Carries | top and side border rails | bottom and side border rails |

The raised characters are 0.8 mm tall and 16 mm across — coarse features that
print cleanly flat at ordinary layer heights. The braille dots are 0.7 mm tall
and 1.6 mm across, which is why they get the angled orientation and the fine
layer height.

`sign_part = Both` puts both plates on one bed for convenience, but if you print
them together you have to compromise on layer height. Exporting them separately
and slicing each with its own settings gives a better sign.

**Mounting them.** The letter plate goes above the braille plate. ADA §703.3.2
wants the braille at least **9.5 mm (3/8 in)** below the raised characters —
this generator does **not** model that offset, so it is on you when you mount.
The split border is the alignment aid: the letter plate carries the top and side
rails, the braille plate carries the bottom and side rails, so when the vertical
rails line up the two plates are square to each other and the frame reads as one
continuous edge under a hand.

§703.4 also governs where the sign goes — mounting height and position relative
to the door. This generator has nothing to say about that; read the standard.

## 5. Printing it

**Print each plate exactly as modeled.** Do not rotate them, and do not add
slicer supports.

| Setting | Letter plate | Braille plate |
|---------|--------------|---------------|
| Layer height | 0.2 mm | 0.1 mm |
| Material | PLA or PETG | PLA or PETG |
| Supports | none | none |
| Brim | not needed | optional (one is modelled under each fin) |
| Outer wall speed | normal | 30–40 mm/s or slower |

Why 0.1 mm on the braille plate: braille standards cap dot height at 0.9 mm, so
the number of layers in a dot — and therefore how smooth it feels — is set almost
entirely by layer height. There is no other lever.

Why to slow the outer wall on the braille plate: it is a thin plate leaning at
75° and it rings badly at speed. Input shaping helps a lot if your printer has
it.

After printing the braille plate: flex or snip the fins off the back, then deburr
the small nubs the bridges leave with a fingernail or fine sandpaper.

**Contrast.** ADA signage requires the characters to contrast with their
background. A single-colour print does not do that. If your printer can change
filament mid-print, the raised characters and the border are the parts to change
colour; otherwise plan to paint them.

## 6. Why we designed it this way

### The braille plate leans back 75°; the letter plate lies flat

**The decision:** `print_orientation = Angled` at `face_angle_deg = 75` for the
braille plate. The letter plate always prints flat.

**The evidence:**

> **Puerta, Crnovrsanin, South, Dunne — "The Effect of Orientation on the
> Readability and Comfort of 3D-Printed Braille," CHI 2024.** DOI
> [10.1145/3613904.3642719](https://doi.org/10.1145/3613904.3642719)
>
> Why it matters: braille printed on a face angled **75°–90°** from the print
> bed was read significantly faster and more comfortably than flat-printed
> braille, because near-vertical printing moves the layer seams off the surface
> the finger reads. **75°** rather than 90° is the working choice here because it
> reduces the overhang under each dot.

**Why not put both scripts on one plate?** Because the finding above applies to
braille dots and not to raised letters. A braille dot is 1.6 mm wide, so a layer
seam across its crown is a large fraction of the feature and a reading finger
feels it. A 16 mm-tall raised character is coarse enough that seams do not
matter, and printing it flat gives a cleaner top face than any angle would. One
plate would force both scripts into whichever orientation you chose, so the sign
is two plates instead. This is the whole reason for the two-part design.

**Why 75° rather than 90°.** On a near-vertical face the dots stick sideways out
of a wall, so the underside of every dot is an overhang. At 90° that overhang is
nearly horizontal and needs support or prints rough; at 75° the face tilts back
15° and the dot undersides become gentle cone-shaped overhangs that print
support-free. The fins, the bridges, and the brim all exist to make that angle
printable in one pass.

### The letter dimensions come from ADA §703.2

**The decision:** `char_height_mm` 16 mm, `letter_raise_mm` 0.8 mm,
`line_spacing_pct` 135, `letter_spacing` 1.1, `force_uppercase` = `Yes`, a
sans-serif font.

**The evidence:**

> **2010 ADA Standards for Accessible Design, §703.** <https://archive.ada.gov/>
>
> Why it matters: §703.3 fixes the braille dot envelope (base 1.5–1.6 mm, height
> 0.6–0.9 mm, domed not pointed); §703.2 fixes raised-character height (minimum
> 15.9 mm / 5/8 in) and relief (minimum 0.8 mm / 1/32 in).

The specific figures each default answers:

| Default | §703 requirement |
|---------|------------------|
| `char_height_mm = 16` | §703.2.5, minimum 15.9 mm (5/8 in) |
| `letter_raise_mm = 0.8` | §703.2.1, minimum 0.8 mm (1/32 in) |
| `line_spacing_pct = 135` | §703.2.8, 135% of character height |
| `letter_spacing = 1.1` | §703.2.8, clear space between characters |
| `force_uppercase = Yes` | §703.2.2, uppercase characters |
| Liberation Sans | §703.2.3, sans-serif |

The generator warns if you set `char_height_mm` below 15.9. The slider allows
values down to 12 mm because a smaller sign is sometimes what you need — but
below 15.9 mm you are no longer inside the figure the standard publishes, and the
sign should not be described as following it.

### The braille dot geometry and spacing

**The decision:** the default `Rounded` dot is a 1.6 mm base tapering to a
1.4 mm dome, 0.35 mm of base plus 0.35 mm of dome — **0.7 mm total height on a
1.6 mm base**. Spacing is `cell_spacing` 7.0 mm, `line_spacing` 10.0 mm,
`dot_spacing` 2.5 mm.

**The evidence:**

> **2010 ADA Standards for Accessible Design, §703.3.** <https://archive.ada.gov/>
>
> Why it matters: braille dots must be domed, not pointed, within a base of
> 1.5–1.6 mm and a height of 0.6–0.9 mm.

> **ISO 17049:2013, *Accessible design — Application of braille on signage,
> equipment and appliances*.** <https://www.iso.org/standard/58090.html>
>
> Why it matters: where ADA and ISO 17049 overlap — dot base **1.5–1.6 mm**, dot
> height **0.6–0.7 mm**, cell pitch **6.1–6.8 mm**, line pitch
> **10.0–10.2 mm** — is the safest target for a sign that may be read by someone
> trained on either standard.

> **BANA, *Size and Spacing of Braille Characters*.**
> <https://brailleauthority.org/size-and-spacing-braille-characters>
>
> Why it matters: the source for cell spacing, line spacing, and within-cell dot
> spacing. Dots that are geometrically legal but spaced wrong are unreadable.

> **Barros, Correia, Teixeira — "Towards the Effectiveness of 3D Printing on
> Tactile Content Creation," Polymers 2023, 15(9):2180.** DOI
> [10.3390/polym15092180](https://doi.org/10.3390/polym15092180)
>
> Why it matters: measured FDM tactile output on a 0.4 mm nozzle at 0.1 mm
> layers. This is the basis for the 0.1 mm layer-height guidance — dot height is
> capped at 0.9 mm by the braille standards, so layer height is the only lever
> left for how smooth a dot feels.

**Why a base under the dome.** A pure spherical dome on a 1.6 mm base physically
cannot exceed 0.8 mm tall — a hemisphere is as tall as it gets. The tapered base
section is what lets the dot reach the upper part of the legal height range while
keeping the legal base width, and it is also what turns the dot's underside into a
printable overhang when the plate leans.

**Why the layer height matters more than it looks like it should.** Because the
standards cap the dot at 0.9 mm, the only remaining control over how a dot feels
is how finely it is sliced. A 0.7 mm dome is seven layers at 0.1 mm and three at
0.2 mm, and three layers is a staircase the fingertip notices instead of the dot.

### The border is split between the plates

The letter plate carries the top and side rails; the braille plate carries the
bottom and side rails. Mounted with the letters above the braille, they read as
one continuous frame. Beyond looking right, the frame is a tactile boundary: a
hand sweeping the sign finds the edge and knows where the content starts.
`border_height_mm` defaults to 0.8 mm, matching the letter relief.

### What this generator does not do

Being explicit about the gaps is part of the design:

- **Mounting height and location (§703.4)** — not modelled. Read the standard.
- **The 9.5 mm braille offset below the raised text (§703.3.2)** — not modelled.
  You set it when you mount the plates.
- **Contrast and glare (§703.5)** — a single-colour print has no contrast.
- **Character width ratios (§703.2.4)** — the font's proportions are the font's.
- **Verified translation** — an automatic translator is not a certified
  transcriber.

### Why a parametric upload at all

> **Siu, Kim, Miele, Follmer — "shapeCAD: An Accessible 3D Modelling Workflow
> for the Blind and Visually-Impaired Via 2.5D Shape Displays," ASSETS 2019.**
> DOI [10.1145/3308561.3353782](https://doi.org/10.1145/3308561.3353782)
>
> Why it matters: identifies that mainstream CAD is visually dependent enough to
> force blind designers to work through sighted intermediaries, and builds its
> accessible workflow **on OpenSCAD** specifically because the design is text.

> **Zhang, Li, Yu, Faruqi, Xie, Kim, Fan, Forbes, Wobbrock, Guo, He —
> "A11yShape: AI-Assisted 3-D Modeling for Blind and Low-Vision Programmers,"
> ASSETS 2025.** DOI
> [10.1145/3663547.3746362](https://doi.org/10.1145/3663547.3746362)
>
> Why it matters: four blind and low-vision programmers independently produced
> 12 models in OpenSCAD — "tasks that were previously impossible without
> assistance from sighted individuals."

The person who most needs a braille sign should be able to make one without
asking a sighted person to drive the software. That is why this is a script with
a parameter panel and not a mesh.

## 7. Troubleshooting

**Read this first.** This model has no on-model warning text. Every problem it
detects is reported as an OpenSCAD `echo()` in the console, and **MakerWorld's
Parametric Model Maker does not show you a console.** The entries below give the
visible symptom to look for in the preview alongside the exact console string you
would see in desktop OpenSCAD.

The single best defence: **leave `auto_fit` on `Yes`.** Every "too tall" and "too
wide" warning below is only reachable with `auto_fit` off.

### A braille cell renders as a blank patch with no dots

**Console string:** `WARNING: braille Line_N contains non-braille characters. Use
Unicode braille (U+2800-U+28FF).`

**What you can see:** a gap in the braille line where dots should be. An invalid
character decodes to an empty dot pattern, so the plate still renders — just
without those dots.

**Fix:** you pasted typed English or ASCII/BRF braille into a `Line_N` field.
Re-translate at <https://www.branah.com/braille-translator> with **Unicode
braille** output. Unicode braille characters look like dot patterns; nothing else
does.

### Text or braille overflows the plate

**Console strings:** `WARNING: TEXT TOO TALL: …`, `WARNING: BRAILLE TOO TALL: …`,
`WARNING: BRAILLE TOO WIDE: …`, `WARNING: TEXT TOO WIDE: …`. Each reports the
measured size against the available size and the minimum you would need.

**What you can see:** letters or dots running past the border, or overlapping it.

**Fix, in order of preference:**

1. Set `auto_fit` to `Yes` — this cannot happen in auto-fit mode.
2. Raise `sign_width_mm`, `letter_plate_height_mm`, or
   `braille_plate_height_mm`.
3. Shorten or remove a line.

Note that the text-width check is estimated from character advances rather than
measured, so treat a marginal case as marginal and look at the preview.

### The characters are smaller than the standard allows

**Console string:** `NOTE: ADA 703.2.5 requires raised characters at least
15.9 mm (5/8 in) tall.`

**What you can see:** nothing — the sign renders fine. This is the warning you
are most likely to miss on MakerWorld, so check the number directly:
`char_height_mm` must be at least **15.9** for the sign to match the published
figure. It defaults to 16.

### The braille plate's fins fall over, or the bridges break mid-print

Raise `bridge_contact_mm` toward 0.4 mm, raise `bridge_count` (default 4), or
lower `fin_interval_mm` (default 25 mm) so more fins share the load.

### The fins will not snap off cleanly

Lower `bridge_contact_mm` toward 0.2 mm, or reduce `bridge_width_mm` /
`bridge_height_mm` (both default 0.5 mm).

### The dots feel rough

Print the braille plate at 0.1 mm layers and slow the outer wall to 30–40 mm/s.
If they are still rough, try `dot_shape` = `Cone`, which some printers render
more cleanly than a dome.

### The two plates do not line up when mounted

The split border is the alignment aid — the vertical side rails should be
continuous from the letter plate down through the braille plate. If they are not,
the plates were rendered at different `sign_width_mm` values, or `auto_fit`
resized one of them. Render both plates from the same parameter set, and if you
are exporting them separately, change nothing except `sign_part` between the two
exports.

## 8. Alternative: OpenSCAD Assistive Forge

If the MakerWorld customizer is hard to use with your screen reader — or you
would rather not create an account — the same generator runs in
**[OpenSCAD Assistive Forge](https://openscad-assistive-forge.pages.dev/)**,
an accessibility-first browser customizer. Deep link straight to this model:

<https://openscad-assistive-forge.pages.dev/?example=braille-sign>

What the Forge does that MakerWorld cannot:

- **It translates your braille for you.** Type plain English and liblouis —
  compiled to WebAssembly and running on your own device — produces Unicode
  braille. MakerWorld's customizer has no translator, so there you must paste
  braille you translated elsewhere. This model's Forge default is
  **UEB Grade 2** (`en-ueb-g2.ctb`), the contracted grade conventional for
  permanent signage; UEB Grade 1 and US Grade 1 and 2 are in the same picker, and
  there is a manual Unicode braille editor if you want to override a translation
  by hand.
- **The interface is built for screen readers and keyboards.** Live status
  announcements, a documented keyboard map matching OpenSCAD desktop (F4
  preview, F5/F6 render, F7 download), light/dark/high-contrast themes, and a
  Basic mode that hides the advanced parameters.
- **Presets** you can save, reload, and share as a link.
- **It works offline.** Installable as a desktop app; after the first visit the
  renderer, the braille tables, and this model are cached locally.
- **Filenames describe the model.** A sign reading "Exit" downloads as
  `Braille Sign Exit.stl` rather than a hash.

Nothing leaves your device in either tool: MakerWorld renders on its servers,
the Forge renders in your browser with OpenSCAD compiled to WebAssembly.

The braille card and braille charm generators are in the Forge too, under the same
**Braille Card Customizer** program.

## 9. Resources

- [2010 ADA Standards for Accessible Design](https://archive.ada.gov/) — §703 is
  the signage section
- [Branah braille translator](https://www.branah.com/braille-translator) — set
  the output to Unicode braille and choose Grade 2 for signage
- [BANA *Size and Spacing of Braille Characters*](https://brailleauthority.org/size-and-spacing-braille-characters)
- [The Rules of Unified English Braille (ICEB)](https://iceb.org/ueb.html)
- [ISO 17049:2013 — Application of braille on signage, equipment and appliances](https://www.iso.org/standard/58090.html)
- [Round Table *Guidelines for Producing Accessible 3D Prints* (2024)](https://printdisability.org/guidelines/3d-prints/)
  — the published standard for tactile print design, including a Blind Makers
  section
- [Smith-Kettlewell *3D Printing for Blind & Low Vision Makers*](https://www.ski.org/technical-file/3d-printing-for-bvi-makers/)
  — printer and slicer guidance for the part of the workflow this model cannot
  cover
- [This project on GitHub](https://github.com/BrennenJohnston/braille-sign-openscad)
- For a sign that will be installed in a public building, work with a
  **UEB-certified transcriber** and verify the installation against §703
  yourself.
