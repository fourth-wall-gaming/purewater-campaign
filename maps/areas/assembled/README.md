# Ready-to-paste prompts

Generated from the specs in the parent directory — do NOT edit these by hand.
Each file is the complete prompt for one sheet, already assembled.

Regenerate after editing any spec or style block (see the parent README).

## Which reference images to attach

**Two sheets are finished** and their prompts are plain, for reference only --
`temple-isle` and `the-siren-s-call`. Both scored 4+ across the board, and the
one fault each had (a wrong cartouche title, and unlabelled rooms) is now fixed
in the shared style blocks rather than in their own briefs.

**The other seventeen are revisions.** Fourteen scored below the bar. The other
three -- `caravan-square`, `the-forge-quarter` and `the-moist-oyster` -- were
kept, but each had one specific fault their spec had to answer for: a Land Gate
labelled on the wrong side of the water, forges indistinguishable from houses,
and a cellar that was never drawn. Their images are usable as they stand; the
re-roll is optional. Their prompts open with "TWO REFERENCE
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
