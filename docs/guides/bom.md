# Bill of materials

A sign needs filament, something to hold it on the wall, and for contrast a
little paint or a second color of filament. There is nothing to solder and no
screws.

| Item | How many | Kind | Where it goes |
|---|---|---|---|
| Filament | see the table below | PLA or PETG | both plates |
| Double-sided mounting tape or adhesive strips | two strips per plate | removable strips or permanent tape | the back of each plate |
| Paint or a second filament | optional | matte, in a color that contrasts with the plate | the raised letters and the border |
| A 3D printer | 1 | a bed at least 170 mm wide for the default sign | both plates |
| Calipers | optional | with a depth rod for the dots | checking the letters and dots |

The plates have flat backs and no mounting holes, so tape or strips are the
only fixing the generator plans for. Contrast is needed on the letters, not
the braille: light letters on a dark plate or dark on light, with a matte
finish that does not glare. A print in one color has no contrast; the
[quick start](quick-start.md#contrast) says how to add it.

## Filament per sample

The numbers below are upper bounds: the solid volume of each shipped STL in
[the stl folder](../../stl/README.md), measured with trimesh, times 1.27 g per
cubic centimeter for PETG. A print with infill uses less. The braille plate's
grams include its fins, bridges and brims, which print with it and then snap
off.

| Sample | Letter plate | Braille plate |
|---|---|---|
| Restroom | 44.0 g | 27.3 g |
| Exit | 43.5 g | 27.3 g |
| Stairs | 43.7 g | 27.3 g |
| Room 101 | 43.9 g | 27.3 g |

Each whole sign, both plates, takes about 71 g of PETG. The solid volumes
behind these grams: the letter plates 34.64 (Restroom), 34.27 (Exit), 34.41
(Stairs) and 34.53 (Room 101) cubic centimeters, and the braille plates 21.47,
21.46, 21.46 and 21.47. For PLA, multiply the grams by 0.98. A sign of your
own at the default size lands near these numbers; a bigger plate takes more,
in step with its area.
