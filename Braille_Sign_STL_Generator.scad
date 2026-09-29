// =============================================================================
// Braille Sign STL Generator (OpenSCAD)
// =============================================================================
// VERSION = 1.0.1
// License: PolyForm Noncommercial 1.0.0
//          https://polyformproject.org/licenses/noncommercial/1.0.0
//
// A two-part tactile sign following the 2010 ADA Standards (section 703)
// recommendations:
//  • LETTER PLATE (top): raised Latin characters (Liberation Sans,
//    sans-serif), uppercase by default, 16 mm character height (5/8 in
//    minimum per 703.2.5), raised 0.8 mm (1/32 in per 703.2.1), 135% line
//    spacing. Prints flat, letters up.
//  • BRAILLE PLATE (bottom): the same text in braille (a sample sign's own,
//    or Unicode braille pasted into braille_line_1..braille_line_6). Prints
//    leaning back at face_angle_deg with break-away support fins by default
//    (the wedge-card technique, crispest dots), or Flat.
//
// SPLIT RAISED BORDER: the letter plate carries the top + side border
// segments and the braille plate carries the bottom + side segments, so
// when the finished plates are mounted with the letters above the braille
// they form ONE continuous tactile frame around the whole sign.
//
// IMPORTANT — ADA disclaimer: these defaults follow the published 703
// figures but this tool does NOT guarantee compliance. Real signage has
// requirements this generator does not model (mounting height and
// location, contrast, glare, character width ratios, braille position
// 9.5 mm (3/8 in) minimum below the raised text, and more). Verify
// against the standard before installing.
//
// =============================================================================
// HOW TO USE: the four Steps at the top of the Customizer
// =============================================================================
//  Step 1 - Pick a sample sign or type your own: pick Restroom, Exit,
//     Stairs or Room 101 under sample_sign, or leave it on Type my own and
//     type your wording into text_line_1..text_line_6 (it becomes the raised
//     letters).
//  Step 2 - Braille, pasted from a translator: for your own wording,
//     translate each line (for example at
//     https://www.branah.com/braille-translator, Unicode braille output, not
//     ASCII braille) and paste it into the matching braille_line_N. A sample
//     sign brings its own braille, so skip this Step. An automatic translator
//     is not a certified transcriber: have a sign for a public building
//     checked.
//  Step 3 - What to export: sign_part Both lays the two plates side by side;
//     Letter plate or Braille plate exports one plate at a time.
//     print_orientation Angled (the default) leans the braille plate back
//     with break-away fins for the crispest dots; Flat prints it dots up.
//  Step 4 - Size: leave auto_fit on Yes and the plates grow so every line of
//     letters and braille fits; the size dials are then minimums, and the
//     size is reported in the console.
//  Then render (F6) and export (File > Export > STL). Print as modeled: no
//  slicer supports needed. Every tab after Step 4 starts with "Advanced".
//
// Lineage: the braille dot system is adapted from the Braille Wedge Card STL
// Generator by Brennen Johnston
// (https://github.com/BrennenJohnston/braille-wedge-card-openscad); the dot
// geometry traces back to the Braille Cylinder STL Generator
// (https://github.com/BrennenJohnston/braille-cylinder-stl-generator-openscad).
// This generator lived in the wedge card repo through v1.1.0 and now has its
// own home at
// https://github.com/BrennenJohnston/braille-sign-openscad
// =============================================================================

/* [Step 1 - Pick a sample sign or type your own] */
// Pick a ready-made sign, or Type my own to use your wording below. A sample ignores the text and braille lines.
sample_sign = "Type my own"; // [Type my own, Restroom, Exit, Stairs, Room 101]
// Line 1 of your wording, as raised letters. Used when sample_sign is Type my own.
text_line_1 = "Room 101";
// Line 2 of your wording. Leave it empty if the sign has fewer lines.
text_line_2 = "";
// Line 3 of your wording. Leave it empty if the sign has fewer lines.
text_line_3 = "";
// Line 4 of your wording. Leave it empty if the sign has fewer lines.
text_line_4 = "";
// Line 5 of your wording. Leave it empty if the sign has fewer lines.
text_line_5 = "";
// Line 6 of your wording. Leave it empty if the sign has fewer lines.
text_line_6 = "";

/* [Step 2 - Braille, pasted from a translator] */
// Braille for text line 1, pasted from a translator as Unicode braille dots, not ASCII letters.
braille_line_1 = "⠠⠗⠕⠕⠍⠀⠼⠁⠚⠁";
// Braille for text line 2. Leave it empty when text line 2 is empty.
braille_line_2 = "";
// Braille for text line 3. Leave it empty when text line 3 is empty.
braille_line_3 = "";
// Braille for text line 4. Leave it empty when text line 4 is empty.
braille_line_4 = "";
// Braille for text line 5. Leave it empty when text line 5 is empty.
braille_line_5 = "";
// Braille for text line 6. Leave it empty when text line 6 is empty.
braille_line_6 = "";

/* [Step 3 - What to export] */
// Which plate to export. Both lays the two plates side by side on the bed.
sign_part = "Both";           // [Both, Letter plate, Braille plate]
// Lean the braille plate back for the crispest dots (Angled) or print it flat (Flat). The letter plate always prints flat.
print_orientation = "Angled"; // [Angled, Flat]

/* [Step 4 - Size] */
// Grow the plates so every line fits (Yes), or keep the exact sizes below (No).
auto_fit = "Yes";             // [Yes, No]
// Width of both plates (mm). When auto_fit is Yes, this is the minimum.
sign_width_mm = 160;          // [60:1:300]
// Height of the letter plate (mm). When auto_fit is Yes, this is the minimum.
letter_plate_height_mm = 70;  // [30:1:200]
// Height of the braille plate (mm). When auto_fit is Yes, this is the minimum.
braille_plate_height_mm = 40; // [25:1:150]

/* [Advanced - Plates and border] */
// Thickness of both plates, not counting the raised letters, dots or border (mm).
plate_thickness_mm = 3;       // [2:0.5:8]
// Space between the two plates on the print bed when sign_part is Both (mm).
plate_gap_mm = 8;             // [2:1:30]
// Add the raised frame: top and sides on the letter plate, bottom and sides on the braille plate.
add_border = "Yes";           // [Yes, No]
// Width of the raised border rails (mm).
border_width_mm = 2;          // [0.5:0.5:6]
// How far the border rises above the plate face (mm).
border_height_mm = 0.8;       // [0.2:0.1:2]

/* [Advanced - Raised letters, ADA 703.2] */
// Turn a to z into capital letters, as ADA 703.2.2 asks. Accented letters stay as typed.
force_uppercase = "Yes";      // [Yes, No]
// Height of the raised capital letters (mm). ADA 703.2.5 asks 15.9 mm (5/8 in) or more.
letter_height_mm = 16;        // [12:0.5:50]
// How far the letters rise off the plate (mm). ADA 703.2.1 asks 0.8 mm (1/32 in) or more.
letter_raise_mm = 0.8;        // [0.4:0.05:2]
// Baseline-to-baseline spacing of the letter lines, as a percent of the letter height (percent). ADA 703.2.8 asks 135 to 170.
letter_line_spacing_pct = 135; // [100:5:200]
// Spreads or tightens the letters. 1 is the font's own spacing; 1.1 adds a little air.
letter_spacing_factor = 1.1;  // [0.8:0.05:2]

/* [Advanced - Braille spacing, ADA 703.3] */
// Center-to-center distance between braille cells (mm). ADA 703.3.1 asks 6.1 to 7.6.
braille_cell_spacing_mm = 7.0; // [2:0.01:15]
// Center-to-center distance between braille lines (mm). ADA 703.3.1 asks 10.0 to 10.2.
braille_line_spacing_mm = 10.0; // [5:0.01:25]
// Center-to-center distance between the dots of one cell (mm). ADA 703.3.1 asks 2.3 to 2.5.
braille_dot_spacing_mm = 2.5; // [1:0.01:5]

/* [Advanced - Braille dot shape] */
// A rounded dome dot, the ADA profile (Rounded), or a pointed dot with a flat top (Cone).
dot_shape = "Rounded";        // [Rounded, Cone]
// Rounded dots: diameter where the dot meets the plate (mm). ADA 703.3.1 asks 1.5 to 1.6.
rounded_dot_base_diameter = 1.6; // [0.5:0.01:3]
// Rounded dots: height of the base below the dome (mm). Base plus dome height is the dot height.
rounded_dot_base_height   = 0.35; // [0:0.01:2]
// Rounded dots: diameter of the dome where it sits on the base (mm). Keep it no wider than the base.
rounded_dot_dome_diameter = 1.4; // [0.5:0.01:3]
// Rounded dots: height of the dome (mm). ADA 703.3.1 asks 0.6 to 0.9 mm for the whole dot.
rounded_dot_dome_height   = 0.35; // [0.1:0.01:2]
// Cone dots: diameter where the dot meets the plate (mm). ADA 703.3.1 asks 1.5 to 1.6.
cone_dot_base_diameter = 1.5; // [0.5:0.01:3]
// Cone dots: height of the dot (mm). ADA 703.3.1 asks 0.6 to 0.9.
cone_dot_height        = 0.8; // [0.3:0.01:2]
// Cone dots: diameter of the small flat top (mm).
cone_dot_top_diameter  = 0.4; // [0.1:0.01:2]

/* [Advanced - Braille plate lean and support fins] */
// Angle between the braille plate and the bed in Angled mode (degrees). 75 to 90 reads best; 75 needs no slicer supports.
face_angle_deg = 75;          // [60:1:90]
// Add break-away fins behind the leaning braille plate so it prints without slicer supports (Angled only).
support_fins = "Yes";         // [Yes, No]
// Space between fins across the plate width; a fin is always added at each end (mm).
fin_interval_mm = 25;         // [1:0.5:200]
// Gap between the back of the leaning plate and the fins (mm).
fin_offset_mm = 1.0;          // [0.2:0.05:10]
// Thickness of each fin (mm).
fin_thickness_mm = 1.2;       // [0.2:0.05:10]
// Fin height as a fraction of the plate height, 1 is full height.
fin_height_frac = 1.0;        // [0.05:0.01:1]
// Number of small break-away bridges joining each fin to the plate.
bridge_count = 4;             // [1:1:60]
// Width of each bridge, measured across the plate (mm).
bridge_width_mm = 0.5;        // [0.2:0.05:8]
// Height of each bridge (mm).
bridge_height_mm = 0.5;       // [0.2:0.05:8]
// How far each bridge reaches into the back of the plate (mm). 0.3 to 0.4 snaps off clean.
bridge_contact_mm = 0.3;      // [0.1:0.05:3]
// Width of the brim around the foot of each fin; 0 turns the brims off (mm).
brim_width_mm = 2.0;          // [0:0.25:25]
// Thickness of the fin brims, about one or two printed layers (mm).
brim_thickness_mm = 0.2;      // [0.1:0.05:3]

/* [Advanced - Warnings and rendering] */
// How smooth the rounded dot domes are. High is smoother but renders slower.
render_quality = "Medium";    // [Low, Medium, High]
// How many flat sides draw each dot's round outline, for both dot shapes. Higher is smoother and slower.
dot_segments = 40;            // [8:1:64]

/* [Hidden] */
$fn = 32;

// =============================================================================
// CALCULATED VALUES
// =============================================================================

use_rounded_dots = (dot_shape == "Rounded");
angled_on = (print_orientation == "Angled");
fins_on = angled_on && ((support_fins == "Yes") || (support_fins == true));
border_on = (add_border == "Yes");
uppercase_on = (force_uppercase == "Yes");

show_letter_plate  = (sign_part == "Both") || (sign_part == "Letter plate");
show_braille_plate = (sign_part == "Both") || (sign_part == "Braille plate");

quality_fn = (render_quality == "Low")    ? 24 :
             (render_quality == "Medium") ? 32 :
             (render_quality == "High")   ? 64 : 32;

// Sample signs for the sample_sign dial. Copied from scripts/sample_signs.json,
// which scripts/generate_sample_braille.mjs writes with liblouis (UEB Grade 2):
// regenerate and copy, never hand-edit the braille. Padded to six lines so
// every loop below walks the same rows as a typed sign.
SAMPLE_NAMES = ["Restroom", "Exit", "Stairs", "Room 101"];
SAMPLE_TEXT = [
    ["Restroom", "", "", "", "", ""],
    ["Exit", "", "", "", "", ""],
    ["Stairs", "", "", "", "", ""],
    ["Room 101", "", "", "", "", ""]
];
SAMPLE_BRAILLE = [
    ["⠗⠑⠌⠗⠕⠕⠍", "", "", "", "", ""],
    ["⠑⠭⠊⠞", "", "", "", "", ""],
    ["⠌⠁⠊⠗⠎", "", "", "", "", ""],
    ["⠗⠕⠕⠍⠀⠼⠁⠚⠁", "", "", "", "", ""]
];
_sample_idx = search([sample_sign], SAMPLE_NAMES)[0];
_sample_on = (sample_sign != "Type my own") && (_sample_idx != []);

// Text content metrics
_text_lines = _sample_on ? SAMPLE_TEXT[_sample_idx]
    : [text_line_1, text_line_2, text_line_3,
       text_line_4, text_line_5, text_line_6];
_braille_lines = _sample_on ? SAMPLE_BRAILLE[_sample_idx]
    : [braille_line_1, braille_line_2, braille_line_3,
       braille_line_4, braille_line_5, braille_line_6];
_line_count = len(_text_lines);
_text_nonempty = [for (i = [0:_line_count-1]) if (len(_text_lines[i]) > 0) i];
_braille_nonempty = [for (i = [0:_line_count-1]) if (len(_braille_lines[i]) > 0) i];
text_rows    = len(_text_nonempty) == 0 ? 0 : _text_nonempty[len(_text_nonempty) - 1] + 1;
braille_rows = len(_braille_nonempty) == 0 ? 0 : _braille_nonempty[len(_braille_nonempty) - 1] + 1;

// Letter layout
text_line_pitch = letter_height_mm * letter_line_spacing_pct / 100;

// Braille dot metrics
dot_total_height = use_rounded_dots
    ? (rounded_dot_base_height + rounded_dot_dome_height)
    : cone_dot_height;
DOT_FACE_EMBED = 0.02;

// Braille block extent (centre-to-centre) on the braille plate
braille_max_len = max([for (l = _braille_lines) len(l)]);
braille_block_w = braille_max_len <= 1 ? 0 : (braille_max_len - 1) * braille_cell_spacing_mm;
braille_block_h = braille_rows  <= 1 ? 0 : (braille_rows - 1) * braille_line_spacing_mm;

// Effective sign size. In auto-fit mode (default) the plates grow so every
// row of letters, braille dots, and the plate heights always fit.
// Manual mode keeps the exact size set above. Uppercase Liberation Sans
// advances average ~0.94 x size per character (measured with textmetrics).
auto_fit_on = (auto_fit == "Yes");
_plate_pad = (border_on ? border_width_mm : 0) + 4;
_dot_base_d = (dot_shape == "Rounded")
    ? rounded_dot_base_diameter : cone_dot_base_diameter;
CHAR_ADVANCE_FACTOR = 0.94;
_est_text_w = text_rows == 0 ? 0
    : max([for (l = _text_lines) len(display_text(l))])
      * letter_height_mm * CHAR_ADVANCE_FACTOR * letter_spacing_factor;
_braille_block_total_w = braille_max_len == 0 ? 0
    : braille_block_w + braille_dot_spacing_mm + _dot_base_d;
sign_w = auto_fit_on
    ? max(sign_width_mm, _est_text_w + 2 * _plate_pad,
          _braille_block_total_w + 2 * _plate_pad)
    : sign_width_mm;
_letter_block_h = text_rows == 0 ? 0
    : (text_rows - 1) * text_line_pitch + letter_height_mm;
letter_plate_h = (auto_fit_on && text_rows > 0)
    ? max(letter_plate_height_mm, _letter_block_h + 2 * _plate_pad)
    : letter_plate_height_mm;
_braille_block_total_h = braille_rows == 0 ? 0
    : braille_block_h + 2 * braille_dot_spacing_mm + _dot_base_d;
braille_plate_h = (auto_fit_on && braille_rows > 0)
    ? max(braille_plate_height_mm, _braille_block_total_h + 2 * _plate_pad)
    : braille_plate_height_mm;

// Space actually available to content once the raised border is deducted.
// The overflow diagnostics below compare against these.
_border_inset    = border_on ? border_width_mm : 0;
_inner_w         = sign_w - 2 * _border_inset;
_letter_inner_h  = letter_plate_h - 2 * _border_inset;
_braille_inner_h = braille_plate_h - 2 * _border_inset;

// Leaning-plate geometry (Angled mode; wedge-card technique). The braille
// plate leans back at face_angle_deg; the reading face is the leaning edge
// of length braille_plate_h.
bp_height   = braille_plate_h * sin(face_angle_deg);
bp_base_run = braille_plate_h * cos(face_angle_deg);

// =============================================================================
// HELPER FUNCTIONS
// =============================================================================

// One decimal place, for millimetre figures in console warnings. Raw floats
// print as 47.32499999999999, which buries the number the reader needs.
function mm1(v) = round(v * 10) / 10;

// Uppercase ASCII a-z (703.2.2: characters shall be uppercase)
function to_upper(s) =
    len(s) == 0 ? "" :
    chr([for (i = [0:len(s)-1])
        let(o = ord(s[i]))
        (o >= 97 && o <= 122) ? o - 32 : o]);

function display_text(s) = uppercase_on ? to_upper(s) : s;

function is_braille_char(c) = (c >= 10240 && c <= 10495);
function has_invalid_chars(str) =
    len(str) == 0 ? false :
    len([for (i = [0:len(str)-1]) if (!is_braille_char(ord(str[i]))) i]) > 0;
function get_dot_pattern(char) =
    let(code = ord(char))
    (code >= 10240 && code <= 10495) ?
        let(pattern = code - 10240)
        [
            (pattern % 2) >= 1 ? 1 : 0,
            floor(pattern / 2)  % 2 >= 1 ? 1 : 0,
            floor(pattern / 4)  % 2 >= 1 ? 1 : 0,
            floor(pattern / 8)  % 2 >= 1 ? 1 : 0,
            floor(pattern / 16) % 2 >= 1 ? 1 : 0,
            floor(pattern / 32) % 2 >= 1 ? 1 : 0
        ]
    : [0, 0, 0, 0, 0, 0];

// Dot offsets in a flat face frame (+X = reading direction, +Y = up)
dot_col_x_offsets = [-braille_dot_spacing_mm / 2, +braille_dot_spacing_mm / 2];
dot_row_y_offsets = [+braille_dot_spacing_mm, 0, -braille_dot_spacing_mm];
dot_positions     = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1]];

// =============================================================================
// DOT MODULE (shared geometry with the wedge card)
// =============================================================================
module braille_dot_centered() {
    if (use_rounded_dots) {
        _total_height = rounded_dot_base_height + rounded_dot_dome_height;
        _dome_r = rounded_dot_dome_diameter / 2;
        _R_sphere = (_dome_r * _dome_r + rounded_dot_dome_height * rounded_dot_dome_height) / (2 * rounded_dot_dome_height);
        _center_z = rounded_dot_base_height + rounded_dot_dome_height - _R_sphere;
        _fuse = 0.02;
        translate([0, 0, -_total_height / 2]) {
            union() {
                translate([0, 0, (rounded_dot_base_height + _fuse) / 2])
                cylinder(
                    h  = rounded_dot_base_height + _fuse,
                    r1 = rounded_dot_base_diameter / 2,
                    r2 = rounded_dot_dome_diameter / 2,
                    center = true,
                    $fn = dot_segments
                );
                intersection() {
                    translate([0, 0, _center_z])
                    sphere(r = _R_sphere, $fn = quality_fn);
                    translate([0, 0, rounded_dot_base_height + _R_sphere])
                    cube([_R_sphere * 4, _R_sphere * 4, _R_sphere * 2], center = true);
                }
            }
        }
    } else {
        cylinder(
            h  = cone_dot_height,
            r1 = cone_dot_base_diameter / 2,
            r2 = cone_dot_top_diameter / 2,
            center = true,
            $fn = dot_segments
        );
    }
}

// =============================================================================
// SPLIT BORDER (2D, plate-local: plate centred at origin)
// =============================================================================
// Full ring minus one rail: the letter plate keeps top + sides, the braille
// plate keeps bottom + sides. Stacked (letters above braille) the segments
// join into one continuous frame.
module border_ring_2d(w, h) {
    difference() {
        square([w, h], center = true);
        square([w - 2 * border_width_mm, h - 2 * border_width_mm], center = true);
    }
}

// which = "top": keep top + side rails (letter plate)
// which = "bottom": keep bottom + side rails (braille plate)
module split_border_2d(w, h, which) {
    eps = 0.01;
    difference() {
        border_ring_2d(w, h);
        if (which == "top") {
            // remove the bottom rail between the side rails
            translate([0, -h / 2 + border_width_mm / 2])
                square([w - 2 * border_width_mm + eps, border_width_mm + eps], center = true);
        } else {
            // remove the top rail between the side rails
            translate([0, h / 2 - border_width_mm / 2])
                square([w - 2 * border_width_mm + eps, border_width_mm + eps], center = true);
        }
    }
}

// =============================================================================
// LETTER PLATE (always prints flat, letters up)
// =============================================================================
// Raised text block is centred on the plate (the border is thin enough to
// ignore in the centring). Lines are centred horizontally per 703-style
// signage conventions.
module letter_plate() {
    union() {
        // Plate body
        linear_extrude(height = plate_thickness_mm)
            square([sign_w, letter_plate_h], center = true);
        // Split border: top + sides
        if (border_on) {
            translate([0, 0, plate_thickness_mm])
                linear_extrude(height = border_height_mm)
                    split_border_2d(sign_w, letter_plate_h, "top");
        }
        // Raised characters
        if (text_rows > 0) {
            block_h = (text_rows - 1) * text_line_pitch;
            for (i = [0 : text_rows - 1]) {
                if (len(_text_lines[i]) > 0) {
                    y_line = block_h / 2 - i * text_line_pitch;
                    translate([0, y_line, plate_thickness_mm])
                        linear_extrude(height = letter_raise_mm)
                            text(display_text(_text_lines[i]),
                                 size = letter_height_mm,
                                 font = "Liberation Sans",
                                 spacing = letter_spacing_factor,
                                 halign = "center",
                                 valign = "center");
                }
            }
        }
    }
}

// =============================================================================
// BRAILLE PLATE — face content (plate-local, flat, dots up)
// =============================================================================
// Braille block centred on the plate; line 0 at the top.
module braille_face_dots() {
    if (braille_rows > 0) {
        for (row = [0 : braille_rows - 1]) {
            line = _braille_lines[row];
            if (len(line) > 0) {
                y_line = braille_block_h / 2 - row * braille_line_spacing_mm;
                for (col = [0 : len(line) - 1]) {
                    // Left-aligned within the block, block centred by longest line
                    x_cell = -braille_block_w / 2 + col * braille_cell_spacing_mm;
                    dots = get_dot_pattern(line[col]);
                    for (d = [0:5]) {
                        if (dots[d] == 1) {
                            dot_pos = dot_positions[d];
                            translate([x_cell + dot_col_x_offsets[dot_pos[1]],
                                       y_line + dot_row_y_offsets[dot_pos[0]],
                                       plate_thickness_mm + dot_total_height / 2 - DOT_FACE_EMBED])
                                braille_dot_centered();
                        }
                    }
                }
            }
        }
    }
}

// Complete flat braille plate: body + split border (bottom + sides) + dots
module braille_plate_flat() {
    union() {
        linear_extrude(height = plate_thickness_mm)
            square([sign_w, braille_plate_h], center = true);
        if (border_on) {
            translate([0, 0, plate_thickness_mm])
                linear_extrude(height = border_height_mm)
                    split_border_2d(sign_w, braille_plate_h, "bottom");
        }
        braille_face_dots();
    }
}

// =============================================================================
// BRAILLE PLATE — ANGLED (leaning slab + break-away fins, wedge technique)
// =============================================================================
// The flat plate above is the "face". For the leaning version the plate is
// rotated 180 deg about Z then leaned back, exactly like the braille charm,
// which keeps braille reading left-to-right and the split-border bottom
// rail at the bottom.
//
// A leaned flat plate would touch the bed along a knife-edge line, so it is
// sunk by BED_SINK and cut flat at z=0, giving the bottom edge a real
// first-layer contact strip.
BED_SINK = 0.6;
bp_lift = (braille_plate_h / 2) * sin(face_angle_deg) - BED_SINK;
// Actual top of the leaned plate above the bed (after the bed sink)
bp_top = bp_height - BED_SINK;

module braille_plate_leaning() {
    difference() {
        translate([0, 0, bp_lift])
            rotate([-face_angle_deg, 0, 0])
                rotate([0, 0, 180])
                    braille_plate_flat();
        // Trim the sunk sliver below the bed -> flat first-layer strip
        translate([0, 0, -braille_plate_h])
            cube([4 * sign_w, 4 * braille_plate_h,
                  2 * braille_plate_h], center = true);
    }
}

function bp_fin_top_z() = fin_height_frac * bp_top;

module bp_support_fin_2d() {
    polygon([
        [-bp_base_run / 2 - fin_offset_mm, 0],
        [+bp_base_run / 2 - fin_offset_mm, 0],
        [-bp_base_run / 2 - fin_offset_mm, bp_fin_top_z()]
    ]);
}

module bp_support_fin(x) {
    translate([x - fin_thickness_mm / 2, 0, 0])
        rotate([90, 0, 90])
            linear_extrude(height = fin_thickness_mm)
                bp_support_fin_2d();
}

module bp_fin_brim(x) {
    if (brim_width_mm > 0 && brim_thickness_mm > 0) {
        y_back  = -bp_base_run / 2 - fin_offset_mm;
        y_front = +bp_base_run / 2 - fin_offset_mm;
        y_lo = y_back - brim_width_mm;
        // Stop short of the plate's bottom contact line (no self-touching STL)
        y_hi = min(y_front + brim_width_mm, bp_base_run / 2 - 0.05);
        translate([x - fin_thickness_mm / 2 - brim_width_mm, y_lo, 0])
            cube([fin_thickness_mm + 2 * brim_width_mm, y_hi - y_lo, brim_thickness_mm]);
    }
}

// Y of the leaning plate's back face at height z (plate-local assembly frame)
function bp_lean_back_y(z) = (bp_lift - z) / tan(face_angle_deg);

module bp_bridges(x) {
    eps = 0.01;
    top_clear = 0.1;
    z_lo = min(max(bridge_height_mm, 2),
               max(bp_fin_top_z() - bridge_height_mm / 2 - top_clear, bridge_height_mm / 2));
    z_hi = max(z_lo, bp_fin_top_z() - bridge_height_mm / 2 - top_clear);
    for (k = [0 : bridge_count - 1]) {
        z_k = (bridge_count == 1)
            ? (z_lo + z_hi) / 2
            : z_lo + (z_hi - z_lo) * k / (bridge_count - 1);
        y_far  = -bp_base_run / 2 - fin_offset_mm - eps;
        y_near = bp_lean_back_y(z_k) + bridge_contact_mm;
        translate([x - bridge_width_mm / 2, y_far, z_k - bridge_height_mm / 2])
            cube([bridge_width_mm, y_near - y_far, bridge_height_mm]);
    }
}

function bp_fin_x_positions() =
    let(
        half  = sign_w / 2,
        n     = max(1, floor(sign_w / fin_interval_mm)),
        inner = [for (i = [0 : n]) -half + i * fin_interval_mm]
    )
    concat(
        [-half],
        [for (xi = inner) if (xi > -half + 1e-3 && xi < half - 1e-3) xi],
        [half]
    );

module bp_support_fins_all() {
    for (x = bp_fin_x_positions()) {
        bp_support_fin(x);
        bp_fin_brim(x);
        bp_bridges(x);
    }
}

module braille_plate_angled() {
    union() {
        braille_plate_leaning();
        if (fins_on) bp_support_fins_all();
    }
}

// =============================================================================
// CONSOLE DIAGNOSTICS
// =============================================================================
// Each overflow warning reports the measured size against the space available,
// matching the counted "TEXT TOO LONG: n/capacity" style the cylinder generator
// uses. "Too tall" on its own leaves you guessing how much to add; the numbers
// say it outright.
echo(str("Braille sign: ", text_rows, " text line(s), ", braille_rows,
         " braille line(s), ", sign_w, " mm wide, plates ",
         letter_plate_h, " + ", braille_plate_h, " mm tall"));
if (text_rows > 0 && _letter_block_h > _letter_inner_h)
    echo(str("WARNING: TEXT TOO TALL: ", mm1(_letter_block_h), "/", mm1(_letter_inner_h),
             " mm. The raised text block is taller than the letter plate's usable height. ",
             "Turn on auto_fit, raise letter_plate_height_mm to at least ",
             mm1(_letter_block_h + 2 * _border_inset), ", or remove a line."));
if (braille_rows > 0 && _braille_block_total_h > _braille_inner_h)
    echo(str("WARNING: BRAILLE TOO TALL: ", mm1(_braille_block_total_h), "/", mm1(_braille_inner_h),
             " mm. The braille block is taller than the braille plate's usable height. ",
             "Turn on auto_fit, raise braille_plate_height_mm to at least ",
             mm1(_braille_block_total_h + 2 * _border_inset), ", or remove a line."));
if (braille_max_len > 0 && _braille_block_total_w > _inner_w)
    echo(str("WARNING: BRAILLE TOO WIDE: ", mm1(_braille_block_total_w), "/", mm1(_inner_w),
             " mm (longest line is ", braille_max_len, " cells). ",
             "Turn on auto_fit, raise sign_width_mm to at least ",
             mm1(_braille_block_total_w + 2 * _border_inset), ", or shorten the line."));
if (_est_text_w > _inner_w)
    echo(str("WARNING: TEXT TOO WIDE: ", mm1(_est_text_w), "/", mm1(_inner_w),
             " mm (estimated from character advances, so treat it as approximate). ",
             "Turn on auto_fit, raise sign_width_mm to at least ",
             mm1(_est_text_w + 2 * _border_inset), ", or shorten the line."));
for (i = [0:_line_count-1])
    if (has_invalid_chars(_braille_lines[i]))
        echo(str("WARNING: braille_line_", i + 1, " contains non-braille characters. Use Unicode braille (U+2800-U+28FF)."));
if (_sample_on)
    echo(str("NOTE: sample_sign is ", sample_sign, "; text_line_N and braille_line_N are ignored."));
if (letter_height_mm < 15.9)
    echo("NOTE: ADA 703.2.5 requires raised characters at least 15.9 mm (5/8 in) tall.");
echo("NOTE: ADA defaults are recommendations only - this tool does not guarantee compliance. Mount the braille plate at least 9.5 mm (3/8 in) below the raised text.");

// =============================================================================
// MAIN RENDERING
// =============================================================================
// Both mode mirrors the final mounted arrangement on the bed: letter plate
// above (+Y), braille plate below (-Y), plate_gap_mm apart.
if (show_letter_plate && show_braille_plate) {
    translate([0, plate_gap_mm / 2 + letter_plate_h / 2, 0])
        letter_plate();
    if (angled_on) {
        // Front bed edge of the leaning assembly sits at -plate_gap_mm/2
        translate([0, -plate_gap_mm / 2 - bp_base_run / 2, 0])
            braille_plate_angled();
    } else {
        translate([0, -plate_gap_mm / 2 - braille_plate_h / 2, 0])
            braille_plate_flat();
    }
} else if (show_letter_plate) {
    letter_plate();
} else if (show_braille_plate) {
    if (angled_on) braille_plate_angled();
    else braille_plate_flat();
}

// End of file
