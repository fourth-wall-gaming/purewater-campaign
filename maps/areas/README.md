# Area maps

Nineteen sheets that zoom into `../purewater-map.png`, rendered through the
ElevenLabs Image API by `mapgen` in the mythras-gm engine.

Each `*.md` here is one sheet: YAML front-matter (slug, title, tier, style,
aspect ratio, seed, the labels to letter, and anything that must **not** be
labelled) over a drawing brief written from the matching file in `../../locations/`.

Two shared style blocks are prepended at render time and do the heavy lifting:

- `_style-cadastral.md` — plan-view district and region sheets
- `_style-floorplan.md` — building and site plans

## Consistency with the master map

This is the whole point, and it is why every render passes
`../purewater-map.png` as a reference image rather than relying on the prompt
alone. The style block tells the model that the reference **is** the master map
of this city and that the new sheet is *an enlargement of one part of it* — so
the reference supplies not only the pen-and-ink-on-parchment look but the actual
coastlines, canal courses and island shapes. Area sheets are meant to be
cuttable from the same atlas.

Upload the reference once; the `asset_id` is cached in `.assets.json` and
reused, which is also what makes a re-render reproducible rather than merely
similar.

## Rendering

```bash
GM=~/mythras-gm/skills/mythras-gm
export ELEVENLABS_API_KEY=...          # needs a Pro plan or above

run() { uv run -q --project "$GM" python "$GM/mapgen.py" \
          --campaign "$(git rev-parse --show-toplevel)" "$@"; }

run list                                      # what exists, and what is rendered
run style-ref --upload ../purewater-map.png   # once
run render the-lullwater --dry-run            # read the prompt, spend nothing
run render the-lullwater --res 1K --quality high
run render --all --res 4K --quality max --yes
```

**Prove the style on one or two sheets at `1K`/`high` before committing the set
at `4K`/`max`.** Iterating on `_style-cadastral.md` is cheap; nineteen 4K
renders are not.

Every render drops a `<slug>.json` beside the image recording the model,
resolution, quality, seed, the exact prompt and the generation id — so any sheet
can be traced to what made it, and reproduced.

## Things that will go wrong

- **The API has no negative prompt.** Every exclusion lives inside the style
  block as prose. If a sheet comes back isometric or with little 3D houses, that
  is the text to strengthen, not a parameter to set.
- **Labels get mangled.** Expect to re-typeset some by hand; the `labels:` list
  in each spec exists so you never have to re-derive what a sheet should say.
- **Three things must never be labelled** anywhere: the Quiet Hand, the
  Mermaid's Court, the Catacombs. Specs that touch the Lullwater, the temples or
  the Northern Isles carry a `do_not_label:` list and the generator appends it
  to the prompt. Check the output.

## Before committing renders

`purewater-campaign` is an installable plugin: `/plugin install purewater`
clones this repo, so everything committed here is downloaded by every player.
Nineteen 4K PNGs is on the order of a hundred megabytes. Decide deliberately —
downscale for the repo and keep the 4K masters elsewhere, or keep the renders
out of `main` — rather than committing them by reflex.
