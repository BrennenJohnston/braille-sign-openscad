// =============================================================================
// generate_sample_braille.mjs: one-time liblouis translation of the sample
// signs offered by the sample_sign dial of Braille_Sign_STL_Generator.scad.
// =============================================================================
//
// Run by hand (never in CI) whenever a sample's wording changes:
//
//     node scripts/generate_sample_braille.mjs
//
// It translates the SAMPLES wording to UEB Grade 2 Unicode braille with the
// same engine and table chain the OpenSCAD Assistive Forge uses (liblouis,
// unicode.dis + en-ueb-g2.ctb), then:
//
//   1. writes scripts/sample_signs.json (committed; tests/test_sample_signs.py
//      locks its shape, and the .scad's sample tables are copied from it), and
//   2. prints the four braille strings to stdout.
//
// Rules mirrored from the Forge (src/js/braille-translator.js):
//   * input is lowercased (signage style, no capital indicator),
//   * table chain unicode.dis,en-ueb-g2.ctb (unicode.dis first forces
//     Unicode braille output),
//   * ASCII spaces in the output become U+2800 (the braille blank), so every
//     codepoint of a stored line is in U+2800..U+28FF.
//
// Requires a local clone of openscad-assistive-forge (the FORGE path below)
// with its node_modules installed and public/liblouis/tables populated.
// Adapted from the plug puller's scripts/generate_braille_labels.mjs.
//
// License: PolyForm Noncommercial 1.0.0

import { createRequire } from "node:module";
import { writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const FORGE = "C:/Users/WATAP/Documents/github/openscad-assistive-forge";

// Reuse the Forge's installed liblouis build. In the Node build the table
// folder is mounted at /tables inside the emscripten FS, so chain entries
// need the tables/ prefix (the browser worker uses bare names instead).
const require = createRequire(join(FORGE, "package.json"));
const liblouis = require("liblouis");
liblouis.enableOnDemandTableLoading(resolve(join(FORGE, "public/liblouis/tables")));

const NODE_CHAIN = "tables/unicode.dis,tables/en-ueb-g2.ctb";

// The sample_sign dropdown's options after "Type my own", in dropdown order.
// Each value is the sign's text lines as the letter plate shows them before
// force_uppercase; the braille is translated from the lowercased wording.
const SAMPLES = {
  "Restroom": ["Restroom"],
  "Exit": ["Exit"],
  "Stairs": ["Stairs"],
  "Room 101": ["Room 101"],
};

const BRAILLE_ONLY = /^[\u2800-\u28FF]+$/;
const MAX_CELLS = 30;

const out = {};
let failed = false;
for (const [name, lines] of Object.entries(SAMPLES)) {
  const braille = lines.map((text) => {
    const cells = liblouis
      .translateString(NODE_CHAIN, text.toLowerCase())
      .replace(/ /g, "\u2800");
    if (!BRAILLE_ONLY.test(cells)) {
      console.error(`ERROR: ${name} "${text}" produced non-braille output: ${cells}`);
      failed = true;
    }
    if (cells.length > MAX_CELLS) {
      console.error(`ERROR: ${name} "${text}" is ${cells.length} cells; the limit is ${MAX_CELLS}`);
      failed = true;
    }
    return cells;
  });
  out[name] = { text: lines, braille };
}

const here = dirname(fileURLToPath(import.meta.url));
const jsonPath = join(here, "sample_signs.json");
writeFileSync(jsonPath, JSON.stringify(out, null, 2) + "\n", "utf-8");
console.error(`Wrote ${jsonPath}`);

for (const [name, sample] of Object.entries(out)) {
  sample.braille.forEach((cells, i) => {
    console.log(`${name}: "${sample.text[i]}" -> ${cells} (${cells.length} cells)`);
  });
}

if (failed) {
  console.error("\nFAILED: fix the wording above and re-run.");
  process.exit(1);
}
