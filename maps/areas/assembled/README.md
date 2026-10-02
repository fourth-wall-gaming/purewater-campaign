# Ready-to-paste prompts

Generated from the specs in the parent directory — do NOT edit these by hand.
Each file is the complete prompt for one sheet, already assembled.

Regenerate after editing any spec or style block (see the parent README).

## Which reference images to attach

**Five sheets are finished** and their prompts are plain, for reference only.
They scored 4+ on playability, fidelity and creativity in the first pass and
should not be re-rolled:

    caravan-square · temple-isle · the-forge-quarter
    the-moist-oyster · the-siren-s-call

**The other fourteen are revisions.** Their prompts open with "TWO REFERENCE
IMAGES ARE SUPPLIED" and then list the faults to correct, so they need **both**
images attached, in this order:

1. `../../purewater-map.png` — the master city map, the authority for style and
   geography.
2. `../<slug>.png` — the previous render of that same sheet, which the prompt
   refers to as "the previous attempt".

Attach them the other way round and the prompt's instructions point at the wrong
picture.

Set the aspect ratio per the spec's front matter (4:3 for districts, 16:9 for
the two regional sheets, 3:2 for set-pieces), and **render at 4K** — the first
pass came back at 1024×768, the same as the master, which is why so much of the
fine detail did not survive.

There is no negative-prompt field to fill in: every exclusion is inside the text.
