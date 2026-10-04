# Ready-to-paste prompts

Generated from the specs in the parent directory — do NOT edit these by hand;
edit the spec or the style block and regenerate (see `../README.md`).

Every correction from `../REVIEW.md` is already in these files.

## Two forms. Pick one.

**`single-reference/*.txt` — the simpler one, and the place to start.**
Attach ONE image: `../../purewater-map.png`, the master city map. Every fix from
the review is written into these as a positive instruction, so they describe the
sheet you want without referring to anything else. Seventeen files, one per
sheet that is being redone.

**`*.txt` (this directory) — the revision form.**
Attach TWO images, **in this order**:

1. `../../purewater-map.png` — the master city map
2. `../<slug>.png` — the previous render of that same sheet

These open with "TWO REFERENCE IMAGES ARE SUPPLIED" and name the faults to
correct, so the model keeps the framing and linework that already worked and
changes only what was wrong. Better results when the tool supports two
references and you attach them the right way round; **reversed, every
instruction points at the wrong picture.**

`temple-isle.txt` and `the-siren-s-call.txt` exist only here and are already
single-reference: those two sheets are finished and are included for reference,
not for re-rolling.

## Settings

Render at **4K**. The first pass came back at 1024×768 — the same as the master
— which is the single biggest reason the fine detail did not survive. Aspect
ratio per sheet is in `RE-ROLL.md`; it is 4:3 for districts, 16:9 for the two
regional sheets, 3:2 for set-pieces.

There is no negative prompt to fill in. Every exclusion is inside the text,
because the API these were written against has no such field.

## Expect to iterate

Lettering is the weak point — the first pass produced "PRŎHĬSE OF E HEAVEN" and
"The Carravan Road". Each spec keeps a `labels:` list so a mangled sheet can be
re-typeset or re-rolled without working out what it should have said.
