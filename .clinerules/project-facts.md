# Project Facts — braille-sign-openscad (always active)

Two-part tactile signs: raised uppercase letter plate + braille plate.
Working branch: main.

1. Main model: Braille_Sign_STL_Generator.scad.
2. Named checks: powershell -ExecutionPolicy Bypass -File scripts\scad-check.ps1
   (after every .scad edit) and python -m pytest tests/ -v (before commits).
   CI renders with OpenSCAD 2026.01.03 — same as the local canonical binary.
3. Canonical braille constants (do not change without my approval): dot
   spacing 2.5 / cell 6.5 / line 10.0 mm; dot map [[0,0],[1,0],[2,0],[0,1],
   [1,1],[2,1]] = dots 1–6. Full geometry specs live in
   braille-cylinder-stl-generator\docs\specifications\.
4. Signage follows ADA tactile-sign conventions: raised characters AND braille
   are both accessibility features — never trade one off to fit the other;
   flag conflicts to me instead.
