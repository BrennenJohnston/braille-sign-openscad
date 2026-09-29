# Maker Guide

This guide takes you from the words on a door to a tactile sign on the wall:
raised capital letters on one plate, the same words in braille on a second
plate below it. You choose how to make the files, prepare the wording and its
braille, fill in four Customizer steps, print each plate, mount the two plates
touching, and check the result by touch. The [quick start](quick-start.md) is
the same path on one page, and the [full guide](full-guide.md) explains every
dial.

1. [Choose a way](#1-choose-a-way)
2. [Prepare the wording](#2-prepare-the-wording)
3. [Customize](#3-customize)
4. [Print](#4-print)
5. [Mount](#5-mount)
6. [Check it](#6-check-it)

## 1. Choose a way

There are four ways to get the two STL files, the files your printer's slicer
reads:

- **Desktop OpenSCAD.** Free software for Windows, macOS and Linux, 2021.01 or
  newer, from [the OpenSCAD downloads page](https://openscad.org/downloads.html).
  You get every dial, and the preview shows problems as red words beside the
  sign. The quick start's [Way 1](quick-start.md#way-1-desktop-openscad) walks
  through each click.
- **In your browser with the Forge.** The
  [OpenSCAD Assistive Forge](https://openscad-assistive-forge.pages.dev/) runs
  the generator in a panel built for screen readers and keyboards, and
  translates your wording into braille for you with liblouis, an open-source
  braille translator. [Open this sign in the
  Forge](https://openscad-assistive-forge.pages.dev/?example=braille-sign). The
  Forge updates its own copy of the generator separately, so its dial names
  and defaults can differ from this guide's.
- **MakerWorld.** Once the sign is listed there, MakerWorld's Parametric Model
  Maker runs the same file in your browser. It cannot translate braille and
  shows no warnings; [the MakerWorld quick
  start](../MAKERWORLD_QUICK_START.md) covers it.
- **A ready-made sample.** Restroom, Exit, Stairs and Room 101 are ready to
  print in [the stl folder](../../stl/README.md). There is nothing to
  customize: go straight to [4. Print](#4-print).

## 2. Prepare the wording

Each line you type becomes one line of raised capital letters, and each line
gets its own line of braille below. A sign can have up to six lines.

1. Write the sign's wording, one line of the sign per line of text.
2. Translate each line into Unicode braille, Grade 2, in lowercase except for
   names, single letters, initials and acronyms. The quick start's
   [Translating your wording](quick-start.md#translating-your-wording) has the
   steps; the Forge does this for you.
3. Keep each braille line beside its text line: braille line 1 goes with text
   line 1, and so on.

Unicode braille is the set of dot-pattern characters from U+2800 to U+28FF.
Grade 2, or contracted braille, shortens common words and letter groups, and
it is what ADA 703.3 asks for on signs.

**An automatic translator is not a certified transcriber.** For a sign in a
public building, have a transcriber certified in Unified English Braille (UEB)
check the braille before you print.

## 3. Customize

Open `Braille_Sign_STL_Generator.scad` and show the Customizer. The first four
tabs are the steps; fill them in from top to bottom.

1. In **Step 1 - Pick a sample sign or type your own**, set `sample_sign` to a
   sample, or leave it on `Type my own` and type your lines into
   `text_line_1` to `text_line_6`.
2. In **Step 2 - Braille, pasted from a translator**, paste each braille line
   into the matching `braille_line_1` to `braille_line_6`. A sample needs none.
3. In **Step 3 - What to export**, set `sign_part` to `Letter plate` for the
   first file. Leave `print_orientation` on `Angled`.
4. In **Step 4 - Size**, leave `auto_fit` on `Yes`. `sign_width_mm`,
   `letter_plate_height_mm` and `braille_plate_height_mm` are then minimums:
   raise one only to make a plate bigger than your wording needs.
5. Look at the preview. Red words beside the sign name a problem to fix first;
   the full guide's [Warnings and notes](full-guide.md#warnings-and-notes)
   explains each one.
6. Render the letter plate (F6 in desktop OpenSCAD).
7. Export it as an STL file. The quick start's
   [Way 1](quick-start.md#way-1-desktop-openscad) names the desktop menu for
   each OpenSCAD version.
8. Set `sign_part` to `Braille plate`.
9. Repeat steps 6 and 7 for the braille plate.

Every other dial sits in a tab whose name starts with "Advanced -". The full
guide's [Every dial](full-guide.md#every-dial) says what each one changes, its
range, and the ADA figure behind it.

## 4. Print

Print each plate as its own job, exactly as the file lays it out: do not
rotate it, and do not add slicer supports.

| Setting | Letter plate | Braille plate |
|---|---|---|
| On the bed | flat, letters up | leaning back on its fins |
| Layer height | 0.2 mm | 0.1 mm |
| Material | PLA or PETG | PLA or PETG |
| Supports | none | none |
| Brim | not needed | optional; one is modeled under each fin |
| Outer wall speed | normal | 30 to 40 mm/s or slower |

In words: print the letter plate flat with its letters up, at 0.2 mm layers.
Print the braille plate as the file stands it, leaning back on its fins, at
0.1 mm layers with the outer wall at 30 to 40 mm/s or slower. Use PLA or PETG
for both, with no slicer supports; the small brim under each fin is part of
the file. The braille plate gets the fine layers because a braille dot is at
most 0.9 mm (0.037 in) tall, so the layer height decides how smooth it feels,
and the slow outer wall because a thin leaning plate shakes at speed.

<!-- photo: shot list item 4 -->
<!-- photo: shot list item 3 -->

When the braille plate is off the bed:

1. Flex or snip the fins off the back of the braille plate.
2. Smooth the small nubs left where the fins joined, with a fingernail or fine
   sandpaper.

A print in one color has no contrast, and signs need light letters on a dark
background or dark on light. Paint the raised letters, or change filament at
the top of the plate: the quick start's [Contrast](quick-start.md#contrast)
section says how.

## 5. Mount

The plates have flat backs and no holes: they go up with adhesive strips or
double-sided tape. The letter plate carries the top and side rails of the
raised border, and the braille plate carries the bottom and side rails, so
mounted touching they make one frame. Where on the wall the sign goes, and on
which side of the door, is in the User Guide's
[Where it goes](user-guide.md#where-it-goes).

1. Clean the wall where the sign goes, and let it dry.
2. Hold the two plates against the wall together, letters above braille, with
   their side rails meeting.
3. Move them until the bottom row of braille is at least 1220 mm (48 in) above
   the floor and the baseline of the top line of letters, the line the letters
   stand on, is at most 1525 mm (60 in) above the floor.
4. Mark the wall along the top edge of the letter plate.
5. Stick adhesive strips or double-sided tape to the back of each plate.
6. Press the letter plate onto the wall with its top edge on the mark.
7. Press the braille plate onto the wall right below it, pushed up until the
   side rails meet.
8. Hold both plates firmly against the wall for as long as the tape's
   instructions say.

<!-- photo: shot list item 2 -->
<!-- photo: shot list item 1 -->

ADA 703.3.2 asks for at least 9.5 mm (3/8 in) between the braille and the
raised letters. With the plates touching, the generator's spacing already
gives more than that: about 43 mm on the default sign.

## 6. Check it

1. Run a fingertip across the braille: each dot should feel round and firm,
   with no cell missing.
2. Read the braille, or, if you do not read braille, compare each cell with
   the braille your translator gave, dot by dot.
3. Measure a dot with calipers that have a depth rod, if you have them: it
   stands about 0.7 mm above the plate.
4. Measure a flat-topped capital letter, such as E, H or T, with a ruler or
   calipers: at the default `letter_height_mm` it is 16 mm tall.
5. Run your hand around the frame: it should feel like one edge, with no step
   where the plates meet.

<!-- photo: shot list item 5 -->
<!-- photo: shot list item 6 -->

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.
