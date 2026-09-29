# Scripts

Helper scripts for this repository. Run each one from the repository root.

| Script | What it does | How to run it |
|---|---|---|
| `scad-check.ps1` | Renders the generator with strict warnings and slider range checks into `build/check.stl`, then prints `CHECK PASSED` or `CHECK FAILED`. | `powershell -ExecutionPolicy Bypass -File scripts\scad-check.ps1` |
| `generate_sample_braille.mjs` | Translates the sample signs to UEB Grade 2 braille with liblouis and writes `scripts/sample_signs.json`. | `node scripts/generate_sample_braille.mjs` |

`generate_sample_braille.mjs` is run by hand, never in CI. It needs a local clone of the OpenSCAD Assistive Forge with its liblouis package and braille tables installed; the path is set at the top of the script. Braille in this repository always comes from this script, never typed by hand, and `tests/test_sample_signs.py` checks the file it writes.
