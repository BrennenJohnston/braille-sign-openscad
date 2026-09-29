# Scripts

Helper scripts for this repository. Run each one from the repository root.

| Script | What it does | How to run it |
|---|---|---|
| `scad-check.ps1` | Renders the generator with strict warnings and OpenSCAD's own parameter checks into `build/check.stl`, then prints `CHECK PASSED` or `CHECK FAILED`. | `powershell -ExecutionPolicy Bypass -File scripts\scad-check.ps1` |
| `generate_sample_braille.mjs` | Translates the sample signs to UEB Grade 2 braille with liblouis and writes `scripts/sample_signs.json`. | `node scripts/generate_sample_braille.mjs` |
| `measure_glyph_advances.py` | Measures each character's width in Liberation Sans with OpenSCAD and writes `scripts/glyph_advances.json` and the `GLYPH_METRICS` table. | `python scripts/measure_glyph_advances.py` |
| `build_release_stls.py` | Renders both plates of every sample sign into `stl/`, checks each is watertight, and writes `stl/README.md`. | `python scripts/build_release_stls.py` |
| `render_doc_images.py` | Renders the preview pictures the guides show into `docs/images/` and prints each file's size. | `python scripts/render_doc_images.py` |
| `check_docs.py` | Checks `README.md` and every page under `docs/` against the documentation rules and prints each finding; exits 1 if any fails. | `python scripts/check_docs.py` |

`measure_glyph_advances.py` is run by hand when the font or the width estimate changes; paste the table it prints into the `.scad`.

`build_release_stls.py` is run by hand after any change to the `.scad` that moves the geometry, and the regenerated files are committed; `--out <folder>` renders somewhere else to compare without touching `stl/`.

`render_doc_images.py` is run by hand after a change to the `.scad` that changes what the pictures show; `--only <name>` renders one picture. Look at each picture, and check its alt text in the guide still matches, before committing it.

`check_docs.py` runs in CI through `tests/test_docs_gate.py`; run it yourself after editing the README or any page under `docs/`. Findings in a file a later phase will rewrite print with that phase's tag and do not fail it.

`generate_sample_braille.mjs` is run by hand, never in CI. It needs a local clone of the OpenSCAD Assistive Forge with its liblouis package and braille tables installed; the path is set at the top of the script. Braille in this repository always comes from this script, never typed by hand, and `tests/test_sample_signs.py` checks the file it writes.
