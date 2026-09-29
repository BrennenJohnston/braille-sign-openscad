# Makers Making Change submission packet

No submission form was found on the Makers Making Change site on 2026-09-28.
The contact routes are the email address info@makersmakingchange.com and the
site's contact page, <https://www.makersmakingchange.com/contact>, which the
OpenAT template's "Contact Us" section links. The owner sends the email at the
end of this page; nothing here has been sent.

## The device

The Braille Sign STL Generator makes a two-part tactile room sign: a letter
plate with the words in raised capital letters, and a braille plate with the
same words in braille, mounted touching so their raised borders join into one
frame. It is one parametric OpenSCAD file with a Customizer in four beginner
Steps, four ready-to-print sample signs, and checks that hold the braille to the
figures of ADA Table 703.3.1. The letter plate prints flat and the braille plate
leans back at 75 degrees on break-away fins, so both print on an ordinary FDM
printer without slicer supports.

> **ADA note.** The defaults follow the published §703 figures, but this tool
> does **not** guarantee compliance. Real signage has requirements this
> generator does not model — mounting height and location, contrast, glare,
> character width ratios, and the 9.5 mm (3/8 in) minimum braille offset below
> the raised text. Verify against the standard before installing.

## Who it helps

The sign is for everyone who reads a door: a braille reader, a reader who finds
the raised letters with their fingers, and a sighted reader all get the same
words from one sign. It helps the makers, teachers and facilities staff who put
up room signs, and the [User Guide](../guides/user-guide.md) says in plain
words where ADA 703.4 puts a sign. The generator also runs in the OpenSCAD
Assistive Forge, a browser customizer built for screen readers and keyboards
that translates the braille with liblouis, so a blind maker can make a sign
without a sighted person driving the software.

**An automatic translator is not a certified transcriber.** The guides say to
have the braille of a sign in a public building checked by a transcriber
certified in Unified English Braille (UEB).

## The OpenAT documents

| Document | Path in this repository |
|---|---|
| Design Rationale | [`docs/guides/design-rationale.md`](../guides/design-rationale.md) |
| Maker Guide | [`docs/guides/maker-guide.md`](../guides/maker-guide.md) |
| User Guide | [`docs/guides/user-guide.md`](../guides/user-guide.md) |
| Bill of Materials | [`docs/guides/bom.md`](../guides/bom.md) |
| Changelog | [`CHANGELOG.md`](../../CHANGELOG.md) |
| OKH manifest | [`okh.yml`](../../okh.yml) |
| README in the OpenAT order | [`README.md`](../../README.md) |

Beyond the template: a one-page [quick start](../guides/quick-start.md) and a
[full guide](../guides/full-guide.md) to every dial and message.

## Files

- [`Braille_Sign_STL_Generator.scad`](../../Braille_Sign_STL_Generator.scad):
  the generator, one self-contained OpenSCAD file.
- [`Braille_Sign_STL_Generator.json`](../../Braille_Sign_STL_Generator.json):
  presets that OpenSCAD's Customizer loads beside it.
- The eight STLs in [the `stl/` folder](../../stl/README.md), both plates of
  each sample sign:
  - `restroom-letter-plate.stl` and `restroom-braille-plate.stl`
  - `exit-letter-plate.stl` and `exit-braille-plate.stl`
  - `stairs-letter-plate.stl` and `stairs-braille-plate.stl`
  - `room-101-letter-plate.stl` and `room-101-braille-plate.stl`

## License

The design, the code and the documents are under PolyForm Noncommercial 1.0.0
([`LICENSE`](../../LICENSE)). It lets anyone use, change and share them for any
noncommercial purpose, including personal projects and use by charities,
schools and public health, safety and research organizations, as long as the
copyright notice travels with them. It gives no right to use them for a
commercial purpose, such as selling the files or signs made from them.

The OpenAT template suggests open-source licenses and allows a maker's own
choice; this license limits commercial use, so it is not an open-source license.

## Photos

The seven photos of the shot list are to come: both plates mounted with a hand
on the braille (the cover), the two plates apart, the braille plate on the bed
with its fins, the letter plate lying flat, a close-up of the dots, calipers on
a letter, and a sign of several lines. They enter `docs/images/` once the owner
has chosen them.

## Readiness

From [`okh.yml`](../../okh.yml), where both are marked as the owner's claim to
confirm before submitting: documentation readiness ODRL-3 and technology
readiness OTRL-4. Its attestation reads: "Rendered and checked by the
repository's tests; a test print of this version by the designer is pending; no
third-party certification has been performed."

## Checklist against the OpenAT template

| Template item | Here |
|---|---|
| Design Rationale | `docs/guides/design-rationale.md` |
| Maker Guide | `docs/guides/maker-guide.md` |
| Bill of Materials | `docs/guides/bom.md` |
| User Guide | `docs/guides/user-guide.md` |
| Changelog | `CHANGELOG.md` |
| Open Know-How manifest | `okh.yml` |
| README sections in the template's order | `README.md`, with one more section, How to use it |
| Documentation folder | `docs/` and `docs/guides/` |
| Design files: CAD | `Braille_Sign_STL_Generator.scad` and `Braille_Sign_STL_Generator.json` |
| Design files: PCB | not applicable: no electronics |
| Build files: 3D printing | `stl/` |
| Build files: PCB | not applicable: no electronics |
| Firmware | not applicable: no firmware; the generator is a design file |
| LICENSES folder | `LICENSE` at the root, one license for everything |
| Photos folder | to come: the shot list, then `docs/images/` |
| Attribution to the OpenAT template | `README.md`, section Attribution |
| Assistive Device Library link | to come: once Makers Making Change lists the device |

## The email

Subject: Braille Sign STL Generator, a two-part tactile room sign for the
Assistive Device Library

> Hello Makers Making Change team,
>
> I would like to offer the Braille Sign STL Generator for your Assistive Device
> Library. It makes a two-part tactile room sign: raised capital letters on one
> plate and the same words in braille on a second plate below, which join into
> one framed sign on the wall. One OpenSCAD file with a four-step Customizer and
> four ready-to-print samples (Restroom, Exit, Stairs and Room 101) covers most
> doors, and the OpenSCAD Assistive Forge runs it in a browser for screen-reader
> users and translates the braille. An automatic translator is not a certified transcriber, so the guides ask for a
> transcriber's check on public signs.
>
> The repository follows your OpenAT template: Design Rationale, Maker Guide,
> User Guide, Bill of Materials, Changelog, okh.yml and the README's order.
>
> https://github.com/BrennenJohnston/braille-sign-openscad
>
> Two things to know. The license is PolyForm Noncommercial 1.0.0, which allows
> noncommercial use and sharing but not commercial use. A test print of the
> current version is still pending. The dimensions follow the 2010 ADA
> Standards' sign figures, with no claim of compliance.
>
> What would you need from me to list it?
>
> Brennen Johnston
