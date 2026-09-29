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
touching, letters above braille, their split borders form one continuous tactile
frame.

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

---

## 1. What to include

A sign says one thing. The 2010 ADA Standards ask for **uppercase** raised
characters at least **16 mm (5/8 in)** tall, which sets the scale: at the
default `letter_height_mm` of 16 and `letter_line_spacing_pct` of 135, each line
of letters takes 21.6 mm of plate height before margins.

- If your sign is one of the samples, pick it: `sample_sign` offers Restroom,
  Exit, Stairs and Room 101, each with its own wording and braille, so you can
  skip section 2.
- Otherwise `text_line_1` to `text_line_6` hold up to six lines of raised
  letters, and `braille_line_1` to `braille_line_6` hold the matching braille.
  **They pair up**: `text_line_2` and `braille_line_2` are the same line of the
  sign in two scripts.
- Leave `auto_fit` on `Yes` and the plates grow to fit whatever you enter, so
  there is no fixed capacity to plan around. The default `sign_width_mm` of
  160 mm and plate heights of 70 mm (letters) and 40 mm (braille) become minimums.
- Keep it to what a person needs at a doorway: a room number, a room name, a
  direction. `Room 101`. `Exit`. `Staff Only`. Long sentences belong on a
  document, not a sign.
- At the default letter height, a line of raised letters is more than twice as
  wide as its braille (RESTROOM: about 144 mm of letters over 43 mm of braille),
  so the letters are what make a long sign wider.

## 2. Translate your text

Skip this section if you picked a sample sign: it brings its own braille.

MakerWorld's customizer cannot translate English for you. You type your plain
text into `text_line_1` to `text_line_6` for the raised letters, and separately
paste **pre-translated Unicode braille (U+2800–U+28FF)**, the characters that
look like patterns of dots, into `braille_line_1` to `braille_line_6`.

Signs use contracted braille: Grade 2, where common words and letter groups are
shortened, as ADA 703.3 asks. The steps below use [the Branah braille
translator](https://www.branah.com/braille-translator). Its own page says its
Grade 2 is still a work in progress and may shorten a word where it should not,
so check what it gives you, or use the OpenSCAD Assistive Forge (section 8),
which translates with liblouis.

1. Open the Branah braille translator.
2. Choose **Grade 2 Braille**.
3. Choose **Unicode Braille**, not ASCII or BRF braille. Unicode braille looks
   like dot patterns: Room 101 is `⠗⠕⠕⠍⠀⠼⠁⠚⠁`. ASCII braille looks like
   ordinary letters and punctuation and does not work.
4. Type one line of your wording in lowercase. Keep a capital only at the start
   of a sentence and for names, single letters, initials and acronyms: those are
   the only places ADA 703.3.1 allows the braille capital sign.
5. Copy the braille.
6. Paste it into the matching braille line: `braille_line_1` for line 1,
   `braille_line_2` for line 2, and so on.
7. Repeat steps 4 to 6 for each line.

The shipped default is `text_line_1` = `Room 101`, with its braille in
`braille_line_1`. Replace both.

**An automatic translator is not a certified transcriber.** For a sign that will
be installed in a public building, have a transcriber certified in Unified
English Braille (UEB) check the braille before you print a set.

## 3. Using the customizer

The Customizer's first four tabs, **Step 1** to **Step 4**, hold everything a
first sign needs. Every tab after them starts with "Advanced", and every dial
there has a working default.

1. Go to MakerWorld → **Create** → **Parametric Model Maker** and upload
   **only** `Braille_Sign_STL_Generator.scad`.
2. Under **Step 1 - Pick a sample sign or type your own**, pick a sample sign in
   `sample_sign` (`Restroom`, `Exit`, `Stairs` or `Room 101`), or leave it on
   `Type my own`. A sample brings its own wording and braille: go on to step 5.
3. With `Type my own`, type your wording into `text_line_1` to `text_line_6`,
   one line of the sign per dial. Leave unused lines empty.
4. Under **Step 2 - Braille, pasted from a translator**, paste the matching
   Unicode braille into `braille_line_1` to `braille_line_6` (section 2).
5. Under **Step 3 - What to export**, set `sign_part` to `Letter plate`. `Both`
   lays the two plates side by side on the bed, `plate_gap_mm` (8 mm) apart, but
   the plates print best with different settings (section 4), so export them one
   at a time.
6. Leave `print_orientation` on `Angled`. This affects the **braille plate
   only**, which then prints leaning back on break-away fins; the letter plate
   always prints flat.
7. Under **Step 4 - Size**, leave `auto_fit` on `Yes`. The plates then grow to
   fit both scripts, treating `sign_width_mm`, `letter_plate_height_mm` and
   `braille_plate_height_mm` as minimums. Turning it off means you are
   responsible for the sign being big enough.
8. Generate the model.
9. Download the STL: this is the letter plate.
10. Set `sign_part` to `Braille plate`.
11. Generate the model again.
12. Download the STL: this is the braille plate.

You can leave the Advanced tabs alone. What each one holds, with its defaults:

| Tab | What it holds |
|-----|---------------|
| Advanced - Plates and border | `plate_thickness_mm` (3), `plate_gap_mm` (8), `add_border` (`Yes`), `border_width_mm` (2), `border_height_mm` (0.8) |
| Advanced - Raised letters, ADA 703.2 | `force_uppercase` (`Yes`), `letter_height_mm` (16), `letter_raise_mm` (0.8), `letter_line_spacing_pct` (135), `letter_spacing_factor` (1.1) |
| Advanced - Braille spacing, ADA 703.3 | `braille_cell_spacing_mm` (6.5), `braille_line_spacing_mm` (10.0), `braille_dot_spacing_mm` (2.5), `braille_clearance_mm` (9.5) |
| Advanced - Braille dot shape | `dot_shape` (`Rounded`), then the size of the `Rounded` and the `Cone` dot |
| Advanced - Braille plate lean and support fins | `face_angle_deg` (75), `support_fins` (`Yes`), then the fin, bridge and brim sizes |
| Advanced - Warnings and rendering | `show_warnings` (`Yes`), `render_quality` (`Medium`), `dot_segments` (40) |

The font is fixed at Liberation Sans and is not a parameter. It is a sans-serif
face, which is what §703.2.3 asks for, and it is a font MakerWorld's renderer
reliably has.

## 4. The two-part workflow

The two plates want different print settings, so print them as two jobs.

| | Letter plate | Braille plate |
|--|--------------|---------------|
| Orientation | flat, letters up | leaning back 75° |
| Supports | none | none (modeled fins) |
| Layer height | 0.2 mm is fine | 0.1 mm |
| Carries | top and side border rails | bottom and side border rails |

The raised letters stand 16 mm tall and rise 0.8 mm off the plate — coarse
features that print cleanly flat at ordinary layer heights. A braille dot is
0.7 mm tall and 1.6 mm across, which is why the braille plate gets the angled
orientation and the fine layer height.

`sign_part` = `Both` puts both plates on one bed for convenience, but if you
print them together you have to compromise on layer height. Exporting them
separately and slicing each with its own settings gives a better sign.

**Mounting them.** The two plates touch on the wall, letters above braille. The
letter plate carries the top and side rails of the raised border and the braille
plate the bottom and side rails, so when the plates meet, the rails run as one
frame around the sign, square and continuous under a hand.

1. Lay the letter plate above the braille plate, both face up.
2. Push the plates together until their side rails meet in one straight line.
3. Stick adhesive strips or double-sided tape to the back of each plate.
4. Pick the height on the wall: the bottom row of braille at least 1220 mm
   (48 in) above the floor, and the baseline of the top line of letters (the
   line the letters stand on) at most 1525 mm (60 in) above the floor.
5. Press the letter plate onto the wall.
6. Press the braille plate onto the wall right below it, with the side rails
   meeting.

ADA §703.3.2 asks for at least 9.5 mm (3/8 in) between the braille and the
raised letters. With the plates touching, the generator's spacing already gives
more than that: about 43 mm on the default sign.

§703.4 also says which side of the door the sign goes on. The
[User Guide](guides/user-guide.md#where-it-goes) gives those rules in plain words.

## 5. Printing it

**Print each plate exactly as modeled.** Do not rotate them, and do not add
slicer supports.

| Setting | Letter plate | Braille plate |
|---------|--------------|---------------|
| Layer height | 0.2 mm | 0.1 mm |
| Material | PLA or PETG | PLA or PETG |
| Supports | none | none |
| Brim | not needed | optional (one is modeled under each fin) |
| Outer wall speed | normal | 30–40 mm/s or slower |

Why 0.1 mm on the braille plate: braille standards cap dot height at 0.9 mm, so
the number of layers in a dot — and therefore how smooth it feels — is set almost
entirely by layer height. There is no other lever.

Why to slow the outer wall on the braille plate: it is a thin plate leaning at
75° and it rings badly at speed. Input shaping helps a lot if your printer has
it.

After printing the braille plate: flex or snip the fins off the back, then deburr
the small nubs the bridges leave with a fingernail or fine sandpaper.

**Contrast.** The ADA Standards ask for raised characters that contrast with
their background, and a print in one color has none. If your slicer can pause for a
filament change, add one on the letter plate at the first layer above 3 mm, the
top of the plate at the default `plate_thickness_mm`, so the raised characters
and the border print in the second color. Otherwise, paint the raised characters
in a matte color that contrasts with the plate. The braille does not need to
contrast.

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

**What you may change:** `face_angle_deg` runs from 60 to 90; 75 to 90 reads
best, and 75 needs no slicer supports. `print_orientation` = `Flat` prints the
braille plate dots up, which puts the layer seams across the dots.

### The letter dimensions come from ADA §703.2

**The decision:** `letter_height_mm` 16 mm, the printed height of the capital I;
`letter_raise_mm` 0.8 mm; `letter_line_spacing_pct` 135; `letter_spacing_factor`
1.1; `force_uppercase` = `Yes`; a sans-serif font.

**The number:** Liberation Sans draws its capital I at 0.9555 of the font size,
so the file divides `letter_height_mm` by 0.9555 before it sets the size: the
dial at 16 prints an I 16.0 mm tall, measured on the mesh. The dial means the
printed height because §703.2.5 measures the printed capital I.

**The evidence:**

> **2010 ADA Standards for Accessible Design, §703.**
> <https://archive.ada.gov/>
>
> Why it matters: §703.3 fixes the braille dot envelope (base 1.5–1.6 mm, height
> 0.6–0.9 mm, domed not pointed); §703.2 fixes raised-character height (minimum
> 15.9 mm / 5/8 in) and relief (minimum 0.8 mm / 1/32 in). Cited as a dimensional
> envelope, **never as a compliance claim** — see §5.

The block's "§5" is the documentation standard's own section on compliance
language, not section 5 of this guide. 5/8 in is 15.875 mm; the 2010 Standards
print it as "5/8 inch (16 mm)", and 16 mm is the figure this generator uses.

The specific figures each default answers:

| Default | §703 figure |
|---------|------------------|
| `letter_height_mm = 16` | §703.2.5, 16 mm (5/8 in) minimum, on the capital I |
| `letter_raise_mm = 0.8` | §703.2.1, 0.8 mm (1/32 in) minimum |
| `letter_line_spacing_pct = 135` | §703.2.8, 135 to 170% of the letter height |
| `letter_spacing_factor = 1.1` | §703.2.7, character spacing |
| `force_uppercase = Yes` | §703.2.2, uppercase characters |
| Liberation Sans | §703.2.3, sans serif |

**What you may change:** below 16 mm, desktop OpenSCAD's preview shows LETTERS
UNDER 16 MM and its console prints a note; MakerWorld shows neither. The slider
allows values down to 12 mm because a smaller sign has uses outside the ADA
Standards, but below 16 mm you are no longer inside the figure the standard
publishes, and the sign should not be described as following it.
`letter_raise_mm` and `letter_line_spacing_pct` also print a console note outside
their ADA figures; `letter_spacing_factor` has no check.

### The braille dot geometry and spacing

**The decision:** the default `Rounded` dot is a 1.6 mm base tapering to a
1.4 mm dome, 0.35 mm of base plus 0.35 mm of dome — **0.7 mm total height on a
1.6 mm base**. Spacing is `braille_cell_spacing_mm` 6.5 mm,
`braille_line_spacing_mm` 10.0 mm, `braille_dot_spacing_mm` 2.5 mm.

**The number:** measured on the plate, a dot stands 0.68 mm proud of the face,
because it sinks 0.02 mm into the plate to fuse with it.

**The evidence:** ADA Table 703.3.1, from the Standards' own text: dot base
diameter 1.5 to 1.6 mm (0.059 to 0.063 in); dot height 0.6 to 0.9 mm (0.025 to
0.037 in); dots in a cell 2.3 to 2.5 mm (0.090 to 0.100 in) apart; matching dots
in neighboring cells 6.1 to 7.6 mm (0.241 to 0.300 in); a cell and the cell
directly below 10 to 10.2 mm (0.395 to 0.400 in), all center to center; the dots
domed or rounded. And from the documentation standard's evidence library:

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

> **Barros, Correia, Teixeira — "Towards the Effectiveness of 3D Printing on
> Tactile Content Creation," Polymers 2023, 15(9):2180.** DOI
> [10.3390/polym15092180](https://doi.org/10.3390/polym15092180)
>
> Why it matters: measured FDM tactile output on a 0.4 mm nozzle at 0.1 mm
> layers. This is the basis for the 0.1 mm layer-height guidance — dot height is
> capped at 0.9 mm by the braille standards, so layer height is the only lever
> left for how smooth a dot feels.

The default dot sits inside the ADA and ISO 17049 overlap: base 1.6 mm, height
0.7 mm, cell pitch 6.5 mm, line pitch 10.0 mm.

**Why a base under the dome.** A pure spherical dome on a 1.6 mm base physically
cannot exceed 0.8 mm tall — a hemisphere is as tall as it gets. The tapered base
section is what lets the dot reach the upper part of the legal height range while
keeping the legal base width, and it is also what turns the dot's underside into a
printable overhang when the plate leans.

**Why the layer height matters more than it looks like it should.** Because the
standards cap the dot at 0.9 mm, the only remaining control over how a dot feels
is how finely it is sliced. Printed flat, a 0.7 mm dot is seven layers at 0.1 mm
and only three or four at 0.2 mm, and a few layers make a staircase the fingertip
notices instead of the dot.

**What you may change:** every braille slider spans Table 703.3.1 and no
further, and a check in the file stops the render if a value goes outside it.
`dot_shape` = `Cone` gives a pointed dot with a flat top for printers that print
`Rounded` badly; it is not the domed shape ADA asks for.

### The 9.5 mm braille clearance

**The decision:** auto-fit keeps the braille `braille_clearance_mm` (9.5 mm)
inside the border rails; the letters keep 4 mm.

**The number:** on a six-line sign, the braille sits 9.505 mm from the bottom
rail, measured where each dot meets the face. With the plates touching on the
wall, the braille sits 43.473 mm below the lowest letter on the default sign.

**The evidence:** ADA 703.3.2, from the Standards' own text: "Braille shall be
separated 3/8 inch (9.5 mm) minimum from any other tactile characters and 3/8
inch (9.5 mm) minimum from raised borders and decorative elements."

**What you may change:** `braille_clearance_mm` runs from 9.5 to 20 mm, and a
check stops the render below 9.5. With `auto_fit` off, braille that fits the
plate but not with this space sets off BRAILLE TOO CLOSE TO BORDER (section 7).

### The border is split between the plates

The letter plate carries the top and side rails; the braille plate carries the
bottom and side rails. Mounted touching, letters above braille, they read as one
continuous frame. Beyond looking right, the frame is a tactile boundary: a hand
sweeping the sign finds the edge and knows where the content starts.
`border_width_mm` defaults to 2 mm and `border_height_mm` to 0.8 mm, matching the
letter relief.

### What this generator does not do

Being explicit about the gaps is part of the design:

- **Mounting height and location (§703.4)** — not modeled. Section 4 gives the
  heights, and the User Guide the side of the door.
- **Contrast and glare (§703.5)** — a single-color print has no contrast.
- **Character width ratios (§703.2.4)** — the font's proportions are the font's.
- **Verified translation** — an automatic translator is not a certified transcriber.

### Why a parametric upload at all

> **Siu, Kim, Miele, Follmer — "shapeCAD: An Accessible 3D Modelling Workflow
> for the Blind and Visually-Impaired Via 2.5D Shape Displays," ASSETS 2019.**
> DOI [10.1145/3308561.3353782](https://doi.org/10.1145/3308561.3353782)
>
> Why it matters: identifies that mainstream CAD is visually dependent enough to
> force blind designers to work through sighted intermediaries, and builds its
> accessible workflow **on OpenSCAD** specifically because the design is text.
> Every model in this family is an OpenSCAD script for this reason.

> **Zhang, Li, Yu, Faruqi, Xie, Kim, Fan, Forbes, Wobbrock, Guo, He —
> "A11yShape: AI-Assisted 3-D Modeling for Blind and Low-Vision Programmers,"
> ASSETS 2025.** DOI
> [10.1145/3663547.3746362](https://doi.org/10.1145/3663547.3746362)
>
> Why it matters: four blind and low-vision programmers independently produced
> 12 models in OpenSCAD — "tasks that were previously impossible without
> assistance from sighted individuals." The finding that makes a parametric
> upload worth the effort: a customizer panel over a script is something a blind
> maker can drive alone, where a mesh editor is not.

The person who most needs a braille sign should be able to make one without
asking a sighted person to drive the software. That is why this is a script with
a parameter panel and not a mesh.

## 7. Troubleshooting

**Read this first.** MakerWorld shows none of this model's warnings. In desktop
OpenSCAD, the generator shows each problem twice: as red words beside the sign
in the preview, and as a line with its numbers in the console under the preview.
The red words are on while `show_warnings`, under **Advanced - Warnings and
rendering**, is `Yes`, its default. MakerWorld's Parametric Model Maker shows the
rendered model only, without the preview words and without a console. So each
entry below starts with what you can see on MakerWorld, then gives the exact
words desktop OpenSCAD shows, then the fix in order of preference. The
[full guide](guides/full-guide.md#warnings-and-notes) explains every warning and
note for desktop OpenSCAD.

In the console texts below, a word in braces, such as `{n}`, stands for the
number or name the console prints.

The best defense: **leave `auto_fit` on `Yes`.** Every "too tall", "too wide"
and "too close" warning below appears only with `auto_fit` off.

### A braille cell renders as a blank patch with no dots

- **On MakerWorld:** no message. The braille line has blank cells where dots
  should be, or no dots at all when the whole line is typed letters. A character
  that is not braille prints no dots, so the plate still renders.
- **In desktop OpenSCAD:** the preview shows `NOT BRAILLE IN LINE {n}`, and the
  console prints
  `WARNING: braille_line_{n} contains non-braille characters. Use Unicode braille (U+2800-U+28FF).`
- **Fix:** you pasted typed letters or ASCII/BRF braille into that braille line.
  Translate it again with **Unicode braille** output (section 2) and paste the
  result. An ordinary space also sets off the warning, though it prints the same
  blank cell: between braille words, use the blank braille cell, U+2800.

### Text or braille overflows the plate

- **On MakerWorld:** no message. Letters or dots run over a border rail or past
  the edge of the plate; a long line of letters can hang off both sides.
- **In desktop OpenSCAD:** the preview shows one of these red words, and the
  console prints the line beside it, with the measured size against the space
  available and the size you would need:
  - `TEXT TOO WIDE`:
    `WARNING: TEXT TOO WIDE: {estimate}/{space} mm (estimated from character advances, so treat it as approximate). Turn on auto_fit, raise sign_width_mm to at least {width}, or shorten the line.`
  - `TEXT TOO TALL`:
    `WARNING: TEXT TOO TALL: {block}/{space} mm. The raised text block is taller than the letter plate's usable height. Turn on auto_fit, raise letter_plate_height_mm to at least {height}, or remove a line.`
  - `BRAILLE TOO WIDE`:
    `WARNING: BRAILLE TOO WIDE: {block}/{space} mm (longest line is {cells} cells). Turn on auto_fit, raise sign_width_mm to at least {width}, or shorten the line.`
  - `BRAILLE TOO TALL`:
    `WARNING: BRAILLE TOO TALL: {block}/{space} mm. The braille block is taller than the braille plate's usable height. Turn on auto_fit, raise braille_plate_height_mm to at least {height}, or remove a line.`
- **Fix, in order of preference:**
  1. Set `auto_fit` to `Yes` — this cannot happen in auto-fit mode.
  2. Raise `sign_width_mm`, `letter_plate_height_mm`, or
     `braille_plate_height_mm`.
  3. Shorten or remove a line.

The text-width check is estimated from character advances rather than measured,
so treat a marginal case as marginal and look at the preview.

### The braille sits too close to the border

- **On MakerWorld:** no message. The braille fits inside the rails but sits
  closer than `braille_clearance_mm` (9.5 mm, 3/8 in) to a rail or to the top
  edge of the braille plate, which is hard to judge by eye.
- **In desktop OpenSCAD:** the preview shows `BRAILLE TOO CLOSE TO BORDER`, and
  the console prints one of these, for the height or for the width:
  - `WARNING: BRAILLE TOO CLOSE TO BORDER: {block}/{space} mm. ADA 703.3.2 asks {clearance} mm of clear space. Turn on auto_fit, raise braille_plate_height_mm to at least {height}, or remove a line.`
  - `WARNING: BRAILLE TOO CLOSE TO BORDER: {block}/{space} mm (longest line is {cells} cells). ADA 703.3.2 asks {clearance} mm of clear space. Turn on auto_fit, raise sign_width_mm to at least {width}, or shorten the line.`
- **Fix, in order of preference:**
  1. Set `auto_fit` to `Yes`.
  2. Raise `braille_plate_height_mm` or `sign_width_mm`, whichever the console
     names.
  3. Shorten or remove a line.

### The letters are shorter than 16 mm

- **On MakerWorld:** nothing — the sign renders fine. This is the problem you
  are most likely to miss on MakerWorld, so check the number directly:
  `letter_height_mm` must be at least **16** for the sign to match the published
  figure. It defaults to 16.
- **In desktop OpenSCAD:** the preview shows `LETTERS UNDER 16 MM`, and the
  console prints
  `NOTE: letter_height_mm is under 16 mm (5/8 in); ADA 703.2.5 asks raised characters at least that tall, measured on the capital I.`
- **Fix:** raise `letter_height_mm` to 16 or more.

### The sign shows a sample's wording instead of yours

- **On MakerWorld:** no message. The letter plate reads RESTROOM, EXIT, STAIRS
  or ROOM 101 whatever you typed, because a sample sign is picked.
- **In desktop OpenSCAD:** the preview shows `SAMPLE SIGN IN USE` in orange, and
  the console prints
  `NOTE: sample_sign is {name}; text_line_N and braille_line_N are ignored.`
- **Fix:** set `sample_sign` to `Type my own`.

### Letter settings outside the ADA figures

- **On MakerWorld:** nothing — the sign renders fine, so check the two dials
  directly.
- **In desktop OpenSCAD:** the preview shows nothing, and the console prints:
  - `NOTE: letter_raise_mm is under 0.8 mm (1/32 in); ADA 703.2.1 asks raised characters at least that high.`
    when `letter_raise_mm` is under 0.8.
  - `NOTE: letter_line_spacing_pct is outside 135 to 170; ADA 703.2.8 asks the baselines of raised letter lines 135 to 170 percent of the letter height apart.`
    when the sign has two or more lines of letters.
- **Fix:** set `letter_raise_mm` to 0.8 or more, and `letter_line_spacing_pct`
  from 135 to 170.

### The braille plate's fins fall over, or the bridges break mid-print

Raise `bridge_contact_mm` toward 0.4 mm, raise `bridge_count` (default 4), or
lower `fin_interval_mm` (default 25 mm) so more fins share the load.

### The fins will not snap off cleanly

Lower `bridge_contact_mm` toward 0.2 mm, or reduce `bridge_width_mm` /
`bridge_height_mm` (both default 0.5 mm).

### The dots feel rough

Print the braille plate at 0.1 mm layers and slow the outer wall to 30–40 mm/s.
If they are still rough, try `dot_shape` = `Cone`, which some printers render
more cleanly than a dome. Cone is a pointed dot with a flat top, not the domed
shape ADA 703.3.1 asks for, so use it only if `Rounded` prints badly.

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
  the output to Unicode Braille and choose Grade 2 Braille for signage; its own
  page calls its Grade 2 a work in progress
- [BANA *Size and Spacing of Braille Characters*](https://brailleauthority.org/size-and-spacing-braille-characters)
- [The Rules of Unified English Braille (ICEB)](https://iceb.org/ueb.html)
- [ISO 17049:2013 — Application of braille on signage, equipment and appliances](https://www.iso.org/standard/58090.html)
- [Round Table *Guidelines for Producing Accessible 3D Prints* (2024)](https://printdisability.org/guidelines/3d-prints/)
  — the published standard for tactile print design, including a Blind Makers
  section
- [Smith-Kettlewell *3D Printing for Blind & Low Vision Makers*](https://www.ski.org/technical-file/3d-printing-for-bvi-makers/)
  — printer and slicer guidance for the part of the workflow this model cannot
  cover
- [The full guide](guides/full-guide.md) — every dial, warning and note of this
  generator, for desktop OpenSCAD
- [This project on GitHub](https://github.com/BrennenJohnston/braille-sign-openscad)
- For a sign that will be installed in a public building, work with a
  **UEB-certified transcriber** and verify the installation against §703
  yourself.
