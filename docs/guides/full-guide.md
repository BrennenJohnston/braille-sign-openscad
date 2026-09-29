# Full guide

This guide explains how the Braille Sign STL Generator builds a sign, what
every dial does, and every message it can show you. It is for makers who want
to change more than the four Steps. If you are making your first sign, start
with the [quick start](quick-start.md) instead.

Every dial is named exactly as it appears in the Customizer, OpenSCAD's panel
of settings. Sizes are in millimeters, with inches where the ADA Standards
state inches.

## How the sign is built

A sign is two plates that print separately and hang one above the other.

The **letter plate** is a flat plate `plate_thickness_mm` thick (3 mm by
default) with the raised letters on top, `letter_raise_mm` high (0.8 mm). The
lines of letters form one block centered on the plate, and each line is
centered on its own. It always prints flat, letters up.

The **braille plate** is first built flat: the plate, its raised border and
the braille dots. For printing it is spun around to face the other way and
leaned back to `face_angle_deg` (75 degrees by default), which keeps the
braille reading left to right and its bottom rail at the bottom. A plate leaned onto the bed would touch it along a knife edge, so
the generator sinks it 0.6 mm into the bed and cuts it flat there, which gives
the bottom edge a real strip of first layer. With `print_orientation` set to
`Flat`, the plate prints dots up instead.

Behind the leaning plate stand break-away **support fins**: thin triangles,
one at each end and more at a steady interval between. Each fin joins the
back of the plate through a few small **bridges**, which snap when you flex
the fin, and sits on a thin **brim** that holds it to the bed. The brim stops
just short of the plate, so the two never touch in the file.

The raised border is **split** between the plates: the letter plate carries
the top rail and both side rails, and the braille plate carries the bottom
rail and both side rails. When you mount the plates touching, letters above
braille, the rails join into one frame around the whole sign.

**Auto-fit.** With `auto_fit` on `Yes`, the three size dials are minimums and
the plates grow to fit what you typed. The letters keep 4 mm of space inside
the border rails, and the braille keeps `braille_clearance_mm` (9.5 mm), the
space ADA 703.3.2 asks between braille and a raised border. Both plates always
share one width, so their side rails line up: the wider of the letters' and
the braille's needs sets it. The letters' width is an estimate, worked out
from a table of every character's width in Liberation Sans, the font the file
uses; on the two test lines it measured, it came out 0.45 % and 1.16 % wider
than the printed letters, never narrower.

Seen from straight above, the default sign's two plates lie on the bed the way
they hang on the wall: the letter plate at the back and the braille plate in
front, leaning on its fins. From this angle the braille shows as a row of dots,
and the flat tops of the raised letters barely stand out from the plate.

![The default sign's two plates seen from straight above, as they lie on the print bed. The letter plate is at the top; its raised ROOM 101 shows only as faint outlines from this angle. Below it the braille plate, leaning back on its fins, shows its raised border and one row of braille dots across the middle.](../images/sign-both-plates-top.png)

## The four Steps

The Customizer opens with four tabs a beginner fills in from top to bottom.
Every tab after them starts with "Advanced -".

**Step 1 - Pick a sample sign or type your own.** `sample_sign` picks one of
the built-in signs (Restroom, Exit, Stairs or Room 101), which brings its own
wording and braille, or `Type my own`, which uses the six text lines below it.
Each text line becomes one line of raised letters, top to bottom.

**Step 2 - Braille, pasted from a translator.** Each braille line holds the
braille for the text line with the same number, as Unicode braille
characters. A sample sign ignores these lines. See
[The sample signs](#the-sample-signs) for where the samples' braille comes
from, and the quick start's
[Translating your wording](quick-start.md#translating-your-wording) for how to
make your own.

**Step 3 - What to export.** `sign_part` chooses both plates together or one
at a time, and `print_orientation` chooses whether the braille plate leans on
fins or lies flat. The plates print best with different settings, so export
them one at a time for a real print.

**Step 4 - Size.** This tab holds `auto_fit` and three size dials. Left on
`Yes`, auto-fit makes the plates as big as the wording needs, and the
console's first line reports the final size.

## Every dial

Each dial below is in the Customizer's order, with what it changes, its
default and range, and the ADA figure where one applies. The Customizer keeps
a dial inside its range. A value set outside it from the command line or a
preset file renders without any check, except for the braille dials, whose
checks stop the render with the message quoted under each one.

The dials of **Step 1 - Pick a sample sign or type your own**:

### `sample_sign`

Picks a ready-made sign or your own wording. A sample replaces all six text
lines and all six braille lines with its own; every other dial still applies.

- Default: `Type my own`. Options: `Type my own`, `Restroom`, `Exit`, `Stairs`,
  `Room 101`.
- With a sample picked, the preview shows SAMPLE SIGN IN USE in orange and the
  console prints a note naming the sample.

### `text_line_1`

The first line of raised letters. `force_uppercase` turns a to z into
capitals as the letters are made; the font is Liberation Sans, a sans serif,
as ADA 703.2.3 asks.

- Default: `Room 101`. Any text; ignored while a sample is picked.
- The line is centered on the plate. With auto-fit on, a line too wide for the
  plate widens both plates instead.

### `text_line_2`

The second line of raised letters, below the first.

- Default: empty.
- An empty line after the last filled line adds nothing. An empty line between
  two filled lines keeps its place, so it leaves a gap in the sign.

### `text_line_3`

The third line of raised letters. Works as `text_line_2` does. Default: empty.

### `text_line_4`

The fourth line of raised letters. Works as `text_line_2` does. Default: empty.

### `text_line_5`

The fifth line of raised letters. Works as `text_line_2` does. Default: empty.

### `text_line_6`

The sixth line of raised letters. Works as `text_line_2` does. Default: empty.

The dials of **Step 2 - Braille, pasted from a translator**:

### `braille_line_1`

The braille for `text_line_1`, as Unicode braille: the dot-pattern characters
U+2800 to U+28FF, one character per braille cell. The blank cell, U+2800, is
the space between words.

- Default: the braille for "Room 101", starting with a capital sign. The
  Room 101 sample's braille has none; see [The sample signs](#the-sample-signs).
- Any other character, including an ordinary space or ASCII braille, prints no
  dots, and the preview shows NOT BRAILLE IN LINE 1.
- The braille lines line up on their left ends, and the block they make is
  centered on the plate by its longest line.

### `braille_line_2`

The braille for `text_line_2`. Works as `braille_line_1` does. Default: empty.
An empty line between two filled lines keeps its place, as with the text
lines.

### `braille_line_3`

The braille for `text_line_3`. Works as `braille_line_1` does. Default: empty.

### `braille_line_4`

The braille for `text_line_4`. Works as `braille_line_1` does. Default: empty.

### `braille_line_5`

The braille for `text_line_5`. Works as `braille_line_1` does. Default: empty.

### `braille_line_6`

The braille for `text_line_6`. Works as `braille_line_1` does. Default: empty.

The dials of **Step 3 - What to export**:

### `sign_part`

Which plates the render holds.

- Default: `Both`. Options: `Both`, `Letter plate`, `Braille plate`.
- `Both` lays the letter plate at the back and the braille plate in front,
  `plate_gap_mm` apart, the way they hang on the wall. Export each plate alone
  to print it with its own settings.

### `print_orientation`

How the braille plate prints. The letter plate always prints flat.

- Default: `Angled`. Options: `Angled`, `Flat`.
- `Angled` leans the plate back to `face_angle_deg` on break-away fins, which
  gives the crispest dots. `Flat` prints the plate dots up, with no fins.

The dials of **Step 4 - Size**:

### `auto_fit`

Whether the plates grow to fit the wording.

- Default: `Yes`. Options: `Yes`, `No`.
- `Yes` treats the three size dials as minimums and grows the plates so every
  line fits with its space (4 mm for letters, `braille_clearance_mm` for
  braille) inside the border. `No` keeps the exact sizes and warns when
  something does not fit.

### `sign_width_mm`

The width of both plates, or with auto-fit on, the smallest width they may
have.

- Default: 160. Range: 60 to 300 mm, in steps of 1.
- With auto-fit on, the width is the largest of this dial, the widest line of
  letters plus its space each side, and the widest braille line plus its space
  each side.

### `letter_plate_height_mm`

The height of the letter plate, or with auto-fit on, its smallest height.

- Default: 70. Range: 30 to 200 mm, in steps of 1.
- With auto-fit on, the plate grows to the block of letters plus 4 mm inside
  the border, top and bottom. The block is one letter height plus one line
  spacing for each extra line.

### `braille_plate_height_mm`

The height of the braille plate, or with auto-fit on, its smallest height.

- Default: 40. Range: 25 to 150 mm, in steps of 1.
- With auto-fit on, the plate grows to the braille block plus
  `braille_clearance_mm` inside the border, top and bottom.

The dials of **Advanced - Plates and border**:

### `plate_thickness_mm`

The thickness of both plates, not counting the letters, dots or border on top.

- Default: 3. Range: 2 to 8 mm, in steps of 0.5.
- The raised letters and the border start at this height, which is where a
  filament change for contrast goes.

### `plate_gap_mm`

The space on the print bed between the letter plate and the braille plate
when `sign_part` is `Both`.

- Default: 8. Range: 2 to 30 mm, in steps of 1.
- It changes nothing when you export one plate at a time.

### `add_border`

Whether the plates get the split raised border.

- Default: `Yes`. Options: `Yes`, `No`.
- With `No`, neither plate has rails, and auto-fit measures its spaces from
  the plate edges instead of the rails.

### `border_width_mm`

The width of each border rail.

- Default: 2. Range: 0.5 to 6 mm, in steps of 0.5.
- Auto-fit adds it to the letters' and the braille's spaces, so a wider rail
  makes the plates bigger.

### `border_height_mm`

How far the border rails rise above the plate face.

- Default: 0.8. Range: 0.2 to 2 mm, in steps of 0.1.
- ADA 703.3.2 asks 9.5 mm (3/8 in) between braille and a raised border;
  `braille_clearance_mm` keeps it.

The dials of **Advanced - Raised letters, ADA 703.2**:

### `force_uppercase`

Turns the letters a to z into capitals as the sign is made. Accented letters
and other characters stay as typed.

- Default: `Yes`. Options: `Yes`, `No`.
- ADA 703.2.2: characters shall be uppercase.

### `letter_height_mm`

The height of the raised capital letters, measured on the printed capital I,
as ADA measures it. Liberation Sans draws its I at 0.9555 of the font size,
so the file divides this dial by 0.9555 before it sets the size.

- Default: 16. Range: 12 to 50 mm, in steps of 0.5.
- Measured at 16: the I and the other flat-topped capitals tried (E, H, M, R,
  T) print 16.000 mm tall, and round ones (O, S) about 0.47 mm taller; the O is
  99.2 % as wide as the I is tall, and the I's stroke is 13.6 % of its height.
- ADA 703.2.5: 16 mm (5/8 in) minimum and 51 mm (2 in) maximum, on the
  uppercase I; 13 mm (1/2 in) is allowed where separate raised and visual
  characters carry the same information. ADA 703.2.4 asks the O's width to be
  55 to 110 % of the I's height, and 703.2.6 the I's stroke at most 15 %.
- Under 16 on a sign with text: the preview shows LETTERS UNDER 16 MM and the
  console prints a note. The sign still renders.

### `letter_raise_mm`

How far the letters rise off the plate.

- Default: 0.8. Range: 0.4 to 2 mm, in steps of 0.05.
- ADA 703.2.1: 0.8 mm (1/32 in) minimum.
- Under 0.8 on a sign with text: the console prints a note.

### `letter_line_spacing_pct`

The distance from one line's baseline to the next, as a percent of the letter
height.

- Default: 135. Range: 100 to 200 percent, in steps of 5.
- ADA 703.2.8: 135 to 170 percent of the raised character height.
- Outside 135 to 170 on a sign with two or more lines of letters: the console
  prints a note.

### `letter_spacing_factor`

Spreads or tightens the letters. 1 is the font's own spacing; 1.1 adds a
little air.

- Default: 1.1. Range: 0.8 to 2, in steps of 0.05.
- ADA 703.2.7: for letters with square sides, as these are, 3.2 mm (1/8 in)
  minimum and four times the stroke width maximum between the closest points
  of two neighbors. Measured at 1.1 and 16 mm: two capital I's sit 4.939 mm
  apart, inside 3.2 to 8.68 mm. The generator does not check other letter
  pairs.

The dials of **Advanced - Braille spacing, ADA 703.3**:

### `braille_cell_spacing_mm`

The distance between the centers of matching dots in neighboring cells.

- Default: 6.5. Range: 6.1 to 7.6 mm, in steps of 0.1. 6.5 is inside the
  range of ISO 17049, the international standard for braille on signs, too.
- ADA Table 703.3.1: 6.1 to 7.6 mm (0.241 to 0.300 in).
- Outside the range, the render stops:
  `braille_cell_spacing_mm must be 6.1 to 7.6 mm (ADA 703.3.1)`

### `braille_line_spacing_mm`

The distance between the centers of matching dots in a cell and the cell
directly below it, on the next braille line.

- Default: 10. Range: 10.0 to 10.2 mm, in steps of 0.1.
- ADA Table 703.3.1: 10 to 10.2 mm (0.395 to 0.400 in).
- Outside the range, the render stops:
  `braille_line_spacing_mm must be 10.0 to 10.2 mm (ADA 703.3.1)`

### `braille_dot_spacing_mm`

The distance between the centers of two dots in the same cell.

- Default: 2.5. Range: 2.3 to 2.5 mm, in steps of 0.1.
- ADA Table 703.3.1: 2.3 to 2.5 mm (0.090 to 0.100 in).
- Outside the range, the render stops:
  `braille_dot_spacing_mm must be 2.3 to 2.5 mm (ADA 703.3.1)`

### `braille_clearance_mm`

The clear space auto-fit keeps between the outer edges of the braille dots
and the border rails. The braille plate's top edge has no rail, so the braille
sits the rail's width farther from it.

- Default: 9.5. Range: 9.5 to 20 mm, in steps of 0.5.
- ADA 703.3.2: braille 9.5 mm (3/8 in) minimum from raised borders and from
  any other tactile characters. Measured on a six-line sign: 9.505 mm from the
  bottom rail.
- With auto-fit off, braille that fits the plate but not with this space shows
  BRAILLE TOO CLOSE TO BORDER.
- Under 9.5, the render stops:
  `braille_clearance_mm is below the ADA 703.3.2 minimum of 9.5 mm`

The dials of **Advanced - Braille dot shape**:

### `dot_shape`

The shape of every braille dot.

- Default: `Rounded`. Options: `Rounded`, `Cone`.
- `Rounded` is a short base topped by a dome: the domed or rounded dot ADA
  703.3.1 asks for. `Cone` is a pointed dot with a small flat top, which is
  not the ADA shape; use it only if Rounded prints badly on your printer. Each
  shape ignores the other shape's dials.

### `rounded_dot_base_diameter`

For Rounded dots: the diameter where the dot meets the plate.

- Default: 1.6. Range: 1.5 to 1.6 mm, in steps of 0.01.
- ADA Table 703.3.1: dot base diameter 1.5 to 1.6 mm (0.059 to 0.063 in).
- Outside the range, the render stops:
  `rounded_dot_base_diameter must be 1.5 to 1.6 mm (ADA 703.3.1 dot base diameter)`

### `rounded_dot_base_height`

For Rounded dots: the height of the base below the dome. The base narrows
from `rounded_dot_base_diameter` to `rounded_dot_dome_diameter`.

- Default: 0.35. Range: 0.1 to 0.5 mm, in steps of 0.01.
- ADA Table 703.3.1: the whole dot, base plus dome, 0.6 to 0.9 mm (0.025 to
  0.037 in) tall. The default dot is 0.7 mm; it sinks 0.02 mm into the face to
  fuse with it, and measured on the plate it stands 0.676 mm proud.
- Outside the range, the render stops:
  `rounded_dot_base_height must be 0.1 to 0.5 mm`
- If base plus dome falls outside 0.6 to 0.9, the render stops:
  `rounded dot total height must be 0.6 to 0.9 mm (ADA 703.3.1 dot height)`

### `rounded_dot_dome_diameter`

For Rounded dots: the diameter of the dome where it sits on the base.

- Default: 1.4. Range: 1.0 to 1.6 mm, in steps of 0.01.
- Outside the range, the render stops:
  `rounded_dot_dome_diameter must be 1.0 to 1.6 mm`
- Wider than the base, the render stops:
  `rounded_dot_dome_diameter must not exceed rounded_dot_base_diameter`

### `rounded_dot_dome_height`

For Rounded dots: the height of the dome.

- Default: 0.35. Range: 0.2 to 0.8 mm, in steps of 0.01.
- Base plus dome must total 0.6 to 0.9 mm, the ADA 703.3.1 dot height.
- Outside the range, the render stops:
  `rounded_dot_dome_height must be 0.2 to 0.8 mm`

### `cone_dot_base_diameter`

For Cone dots: the diameter where the dot meets the plate.

- Default: 1.5. Range: 1.5 to 1.6 mm, in steps of 0.01.
- ADA Table 703.3.1: dot base diameter 1.5 to 1.6 mm.
- Outside the range, the render stops:
  `cone_dot_base_diameter must be 1.5 to 1.6 mm (ADA 703.3.1 dot base diameter)`

### `cone_dot_height`

For Cone dots: the height of the dot.

- Default: 0.8. Range: 0.6 to 0.9 mm, in steps of 0.01.
- ADA Table 703.3.1: dot height 0.6 to 0.9 mm.
- Outside the range, the render stops:
  `cone_dot_height must be 0.6 to 0.9 mm (ADA 703.3.1 dot height)`

### `cone_dot_top_diameter`

For Cone dots: the diameter of the small flat top.

- Default: 0.4. Range: 0.3 to 1.0 mm, in steps of 0.01.
- Outside the range, the render stops:
  `cone_dot_top_diameter must be 0.3 to 1.0 mm`
- As wide as the base or wider, the render stops:
  `cone_dot_top_diameter must be smaller than cone_dot_base_diameter`

The dials of **Advanced - Braille plate lean and support fins**. They change
nothing when `print_orientation` is `Flat`.

### `face_angle_deg`

The angle between the braille plate and the bed when it prints leaning.

- Default: 75. Range: 60 to 90 degrees, in steps of 1.
- 75 to 90 reads best, and 75 needs no slicer supports. This is the print
  angle only: the plate hangs flat on the wall.

### `support_fins`

Whether break-away fins hold the leaning plate up.

- Default: `Yes`. Options: `Yes`, `No`.
- With `No`, the plate leans with nothing behind it, so your slicer would need
  supports.

### `fin_interval_mm`

The space between fins across the plate. A fin always stands at each end.

- Default: 25. Range: 1 to 200 mm, in steps of 0.5.
- The default 160 mm sign gets eight fins. More fins hold the plate more
  firmly.

### `fin_offset_mm`

The gap between the back of the leaning plate and the fins. The bridges cross
it.

- Default: 1.0. Range: 0.2 to 10 mm, in steps of 0.05.

### `fin_thickness_mm`

The thickness of each fin.

- Default: 1.2. Range: 0.2 to 10 mm, in steps of 0.05.

### `fin_height_frac`

The height of each fin as a fraction of the leaning plate's height above the
bed. 1 is full height.

- Default: 1.0. Range: 0.05 to 1, in steps of 0.01.

### `bridge_count`

The number of small bridges joining each fin to the plate. They spread evenly
from about 2 mm above the bed to just below the top of the fin.

- Default: 4. Range: 1 to 60, in steps of 1.

### `bridge_width_mm`

The width of each bridge, measured across the plate.

- Default: 0.5. Range: 0.2 to 8 mm, in steps of 0.05.

### `bridge_height_mm`

The height of each bridge.

- Default: 0.5. Range: 0.2 to 8 mm, in steps of 0.05.

### `bridge_contact_mm`

How far each bridge reaches into the back of the plate.

- Default: 0.3. Range: 0.1 to 3 mm, in steps of 0.05.
- 0.3 to 0.4 snaps off clean. Raise it toward 0.4 if fins fall during a
  print; lower it toward 0.2 if they will not snap off.

### `brim_width_mm`

The width of the brim around the foot of each fin. 0 turns the brims off.

- Default: 2.0. Range: 0 to 25 mm, in steps of 0.25.

### `brim_thickness_mm`

The thickness of the fin brims, about one or two printed layers.

- Default: 0.2. Range: 0.1 to 3 mm, in steps of 0.05.

The dials of **Advanced - Warnings and rendering**:

### `show_warnings`

Whether problems show as text beside the sign in the preview. The text is
drawn as background, so it never reaches a render or an export.

- Default: `Yes`. Options: `Yes`, `No`.
- The console prints the same problems either way.

### `render_quality`

How smooth the rounded dots' domes are: the number of sides each dome is
drawn with.

- Default: `Medium`. Options: `Low` (24), `Medium` (32), `High` (64).
- High renders a little slower. The letters' curves use a fixed 32 sides.

### `dot_segments`

How many flat sides draw each dot's round outline, for both dot shapes: the
base of a Rounded dot and the whole of a Cone dot.

- Default: 40. Range: 8 to 64, in steps of 1.
- Higher is smoother and slower.

## The sample signs

`sample_sign` offers these four signs. Their braille is Unified English
Braille (UEB) Grade 2 from liblouis, an open-source braille translator,
written into `scripts/sample_signs.json` by
`scripts/generate_sample_braille.mjs`; a test checks that the file's own
tables match that data.

| Sample | Raised letters | Braille | Cells |
|---|---|---|---|
| Restroom | RESTROOM | ⠗⠑⠌⠗⠕⠕⠍ | 7 |
| Exit | EXIT | ⠑⠭⠊⠞ | 4 |
| Stairs | STAIRS | ⠌⠁⠊⠗⠎ | 5 |
| Room 101 | ROOM 101 | ⠗⠕⠕⠍⠀⠼⠁⠚⠁ | 9 |

The raised letters are capitals, as ADA 703.2.2 asks. The braille has no
capital sign, because ADA 703.3.1 allows the braille capital sign only before
the first word of a sentence, a name, a single letter, initials or an acronym,
and a room name on a sign is none of those.

**An automatic translator is not a certified transcriber.** For a sign in a
public building, have a transcriber certified in UEB check the braille before
you print.

## Warnings and notes

When something is wrong, the generator says so in two places. In the desktop
preview (F5), red words lie flat just beyond the far edge of the sign, 5 mm
tall and one line per problem; they disappear when you render with F6 and
never reach an export. The console under the preview prints the same problem
with its numbers. `show_warnings` turns the preview words off; the console
lines stay. MakerWorld's Parametric Model Maker shows neither the preview
words nor the console, so the [MakerWorld quick
start](../MAKERWORLD_QUICK_START.md#7-troubleshooting) lists what each problem
looks like there.

In the console texts below, a word in braces, such as `{n}`, stands for the
number or name the console prints.

### Not braille in a braille line

- Preview: `NOT BRAILLE IN LINE {n}`, with the line's number.
- Console: `WARNING: braille_line_{n} contains non-braille characters. Use Unicode braille (U+2800-U+28FF).`
- When: a braille line holds a character outside U+2800 to U+28FF, such as a
  typed letter, ASCII braille or an ordinary space. That character prints no
  dots.
- Fix: paste Unicode braille from a translator. For a space between words, use
  the blank braille cell, U+2800.

### Text too wide

- Preview: `TEXT TOO WIDE`.
- Console: `WARNING: TEXT TOO WIDE: {estimate}/{space} mm (estimated from character advances, so treat it as approximate). Turn on auto_fit, raise sign_width_mm to at least {width}, or shorten the line.`
- When: `auto_fit` is `No` and the widest line of letters is estimated wider
  than the space inside the border.
- Fix, in order: set `auto_fit` to `Yes`; raise `sign_width_mm` to the width
  given; shorten the line.

### Text too tall

- Preview: `TEXT TOO TALL`.
- Console: `WARNING: TEXT TOO TALL: {block}/{space} mm. The raised text block is taller than the letter plate's usable height. Turn on auto_fit, raise letter_plate_height_mm to at least {height}, or remove a line.`
- When: `auto_fit` is `No` and the block of letters is taller than the space
  inside the border.
- Fix, in order: set `auto_fit` to `Yes`; raise `letter_plate_height_mm` to the
  height given; remove a line.

### Braille too wide

- Preview: `BRAILLE TOO WIDE`.
- Console: `WARNING: BRAILLE TOO WIDE: {block}/{space} mm (longest line is {cells} cells). Turn on auto_fit, raise sign_width_mm to at least {width}, or shorten the line.`
- When: `auto_fit` is `No` and the longest braille line is wider than the
  space inside the border.
- Fix, in order: set `auto_fit` to `Yes`; raise `sign_width_mm` to the width
  given; shorten the line.

### Braille too tall

- Preview: `BRAILLE TOO TALL`.
- Console: `WARNING: BRAILLE TOO TALL: {block}/{space} mm. The braille block is taller than the braille plate's usable height. Turn on auto_fit, raise braille_plate_height_mm to at least {height}, or remove a line.`
- When: `auto_fit` is `No` and the braille block is taller than the space
  inside the border.
- Fix, in order: set `auto_fit` to `Yes`; raise `braille_plate_height_mm` to the
  height given; remove a line.

### Braille too close to the border

- Preview: `BRAILLE TOO CLOSE TO BORDER`.
- Console, when the height is short: `WARNING: BRAILLE TOO CLOSE TO BORDER: {block}/{space} mm. ADA 703.3.2 asks {clearance} mm of clear space. Turn on auto_fit, raise braille_plate_height_mm to at least {height}, or remove a line.`
- Console, when the width is short: `WARNING: BRAILLE TOO CLOSE TO BORDER: {block}/{space} mm (longest line is {cells} cells). ADA 703.3.2 asks {clearance} mm of clear space. Turn on auto_fit, raise sign_width_mm to at least {width}, or shorten the line.`
- When: `auto_fit` is `No` and the braille fits inside the border but not with
  `braille_clearance_mm` of space on both sides. Braille that does not fit at
  all shows BRAILLE TOO TALL or BRAILLE TOO WIDE instead.
- Fix, in order: set `auto_fit` to `Yes`; raise the size the console names to
  the value given; remove or shorten a line.

### Letters under 16 mm

- Preview: `LETTERS UNDER 16 MM`.
- Console: `NOTE: letter_height_mm is under 16 mm (5/8 in); ADA 703.2.5 asks raised characters at least that tall, measured on the capital I.`
- When: the sign has text and `letter_height_mm` is under 16.
- Fix: raise `letter_height_mm` to 16 or more. The sign still renders, so a
  smaller sign for a use outside the ADA Standards is your call.

### Sample sign in use

- Preview: `SAMPLE SIGN IN USE`, in orange.
- Console: `NOTE: sample_sign is {name}; text_line_N and braille_line_N are ignored.`
- When: `sample_sign` is set to a sample.
- Fix, if you want your own wording: set `sample_sign` to `Type my own`.

### Notes in the console only

These print to the console and draw nothing in the preview:

- `NOTE: letter_raise_mm is under 0.8 mm (1/32 in); ADA 703.2.1 asks raised characters at least that high.`
  When the sign has text and `letter_raise_mm` is under 0.8.
- `NOTE: letter_line_spacing_pct is outside 135 to 170; ADA 703.2.8 asks the baselines of raised letter lines 135 to 170 percent of the letter height apart.`
  When the sign has two or more lines of letters and the spacing is outside
  135 to 170.
- `NOTE: ADA defaults are recommendations only - this tool does not guarantee compliance. Mount the braille plate at least 9.5 mm (3/8 in) below the raised text.`
  On every render.

Every render also prints the sign's size, and a sign with text prints its
width estimate:

- `Braille sign: {t} text line(s), {b} braille line(s), {w} mm wide, plates {h1} + {h2} mm tall`
- `Text width estimate: {w} mm`

## Old names

Some dials were renamed so that each name says what the dial holds. If you
have a saved preset or a command-line script, change these names:

| Old name | New name | What changed |
|---|---|---|
| `sign_text_1` to `sign_text_6` | `text_line_1` to `text_line_6` | the name only |
| `Line_1` to `Line_6` | `braille_line_1` to `braille_line_6` | the name only |
| `char_height_mm` | `letter_height_mm` | now the printed capital I; multiply an old value by 0.9555 for the same print |
| `line_spacing_pct` | `letter_line_spacing_pct` | the name only |
| `letter_spacing` | `letter_spacing_factor` | the name only |
| `cell_spacing` | `braille_cell_spacing_mm` | default 6.5, was 7.0; range now 6.1 to 7.6 |
| `line_spacing` | `braille_line_spacing_mm` | range now 10.0 to 10.2 |
| `dot_spacing` | `braille_dot_spacing_mm` | range now 2.3 to 2.5 |
| `part_gap_mm` | `plate_gap_mm` | the name only |
| `cone_dot_flat_hat` | `cone_dot_top_diameter` | the name only |
| `cone_segments` | `dot_segments` | the name only; it shapes both dot types |

Three dials are new: `sample_sign`, `braille_clearance_mm` and
`show_warnings`. Two dials changed their values: `add_border` takes `Yes` or
`No` where it took lowercase `yes` or `no`, and `support_fins` takes `Yes` or
`No` where it took `On` or `Off`. The old values count as `No`: an old
preset's `yes` leaves both plates without a border, and its `On` leaves the
braille plate without fins.

OpenSCAD ignores a name it does not know, without any message: an old name in
a preset file or on the command line leaves that dial at its default. Check
the console's size line after you convert a preset.

## The command line

OpenSCAD can make a sign without its window. On Windows, run the console
program, `openscad.com`, from the OpenSCAD folder; on other systems the
command is `openscad`.

Set a dial with `-D name=value`. A text value needs double quotes inside the
argument, so wrap the whole argument in single quotes in a Bash shell:

```bash
openscad -D 'sample_sign="Restroom"' -D 'sign_part="Letter plate"' -o restroom-letter-plate.stl Braille_Sign_STL_Generator.scad
openscad -D 'sample_sign="Exit"' -D letter_height_mm=20 -o exit-20-mm.stl Braille_Sign_STL_Generator.scad
```

Windows PowerShell 5.1 splits a `-D` value that has a space in it into two
arguments, and OpenSCAD then prints its help instead of a sign; use Git Bash
or another Bash shell for those.

The presets file, `Braille_Sign_STL_Generator.json`, holds named sets of
dials. Pick one with `-p` for the file and `-P` for the set's name:

```bash
openscad -p Braille_Sign_STL_Generator.json -P "Default Sign (both plates)" -o sign.stl Braille_Sign_STL_Generator.scad
```

`--check-parameter-ranges=true` checks the values given to OpenSCAD's own
building blocks, not the Customizer's sliders: a `-D` value outside a slider
renders without a message. The braille dials are held instead by checks in
the file that stop the render, quoted under each dial above.

Two more options help in scripts. `--hardwarnings` stops the render on any
warning from OpenSCAD itself (the generator's own messages start with `ECHO:`
and do not count), and `--export-format binstl` writes a smaller, binary STL.

The console's `Text width estimate` line gives the width auto-fit planned for
the widest line of letters, from the character table described in
[How the sign is built](#how-the-sign-is-built). It errs on the wide side, so
the plate is never too narrow for the letters.

## Tests and CI

The tests live in `tests/` and run with `python -m pytest tests`. The ones
marked `requires_openscad` render the sign and need OpenSCAD installed; the
rest only read files.

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
- `tests/test_full_guide_covers_every_dial.py`: this guide names every dial,
  quotes every warning and note, and matches the sample data.

`scripts/scad-check.ps1` renders the default sign with strict warnings and
prints `CHECK PASSED` or `CHECK FAILED`. `scripts/README.md` lists the other
scripts. The continuous integration workflow, `.github/workflows/ci.yml`,
runs on every pull request: a lint check, then `tests/test_customizer.py` and
`tests/test_source_guards.py`, then `tests/test_render_smoke.py` with the
OpenSCAD nightly. Run the other test files yourself before you open a pull
request.

## What the generator does not do

The generator makes two plates. It cannot see where you put them, what color
they are, or whether the braille says what you meant:

- **Where the sign goes.** ADA 703.4 sets the height and place: the bottom row
  of braille at least 1220 mm (48 in) above the floor, the baseline of the top
  line of letters at most 1525 mm (60 in), and rules about which side of the
  door and the clear floor space in front of the sign.
- **Where the plates sit on the wall.** The plates are meant to touch, side
  rails meeting. ADA 703.3.2 asks 9.5 mm (3/8 in) between the braille and the
  raised letters; touching plates give 43.473 mm on the default sign and
  17.505 mm on a six-line sign, measured in the files.
- **Contrast and glare.** ADA 703.5.1 asks light letters on a dark background
  or dark on light, with a non-glare finish. A print in one color has no
  contrast; paint the letters or change filament.
- **Checked braille.** The samples come from liblouis and your own braille
  from whatever translator you use; neither is checked by a person.
- **Other fonts.** The letters are always Liberation Sans, whose proportions
  are measured above.

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.
