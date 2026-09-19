# Working in this repository

**This file is for contributors editing this repo in a git clone. It is not read
when the plugin is installed** — everything a player or a GM needs is in
`skills/purewater/SKILL.md` and `commands/`, which do ship. Do not put anything
load-bearing here.

## What this repository is

A **campaign package** for the [mythras-gm](https://github.com/fourth-wall-gaming/mythras-gm)
engine, shipped as a Claude Code plugin. The file tree is the *source*: beats,
characters, agendas, locations, lore and the worldbook, in the publishable
campaign format (v1.1).

**It is not a save game.** A save lives in TypeDB. `/purewater:start` imports this
package once, and from then on the database is the game and these files are the
thing it was built from. Editing them does not change a running campaign.

## The seed

```
myth-campaign-purewater-s1        d-3/dawn, time_index 52, session_number 0
```

That id is fixed, shipped in `campaign.yaml`, and identical on every install. It
is deliberate: `id` is a key in the schema, so importing the same package twice
**fails loudly** instead of quietly forking somebody's save. Nothing in this
package's documentation should ever name a different id as the campaign to play.

The root is a clean starting point — 43 beats all pending, an empty journal, four
pregens offered and none chosen. If you change that, you have broken a new
player's first session; there is a test.

## Previous playthroughs

These are **this developer's database**, not anybody's install. They are renamed
in the DB so they cannot be mistaken for a startable game.

| id | run |
|---|---|
| `myth-campaign-f7af4bb667ac` | run 4 — Kag, `d1/night`, session 2 · `archive/session-04-kag/` on `playthroughs` |
| `myth-campaign-44abede1efbf` | S2 — Gardwen, CH.1–13 · `archive/session-03-gardwen/` on `playthroughs` |
| `myth-campaign-7883760b82ef` | run 3 — Gardwen, `d-3` to `d-2` |
| `myth-campaign-66a98ba4a70e` | v1, finished at CH.25 |

Kag from run 4 is canon and ships in the seed as an NPC — `characters/npcs/kag.json`,
`agendas/the-one-who-works-it-out.md`, `setting/kag-as-an-npc.md`, and seven
`beats/kag-*.md`. Leave them alone; they are already written for a fresh run.

## Running it locally

```bash
claude --plugin-dir ~/mythras-gm --plugin-dir ~/purewater-campaign-v2
```

Local copies satisfy the `dependencies` entry, so this exercises the real
resolution path without publishing anything. The engine is found by
`scripts/engine.sh`, which checks `$MYTHRAS_GM_ROOT`, then the pointer file the
engine's `init-db` writes, then the plugin cache.

**Never test against port 1730 with database `mythras`.** That is the live
database and it holds four real campaigns. Use a scratch one:

```bash
export TYPEDB_PORT=1730 TYPEDB_DATABASE=purewater_test
gm init-db && gm import-campaign --path .
```

## Operating rules

- **Every mechanical resolution goes through the engine CLI.** It is the shared,
  deterministic dice tower and it looks skills up from the database.
- **The database is the save.** Persist with `log-event`, `set-scene`,
  `update-character`. Never hand-edit these files to change game state.
- **`export-campaign`** when you want a fresh file snapshot for git — but not over
  the root, which is the seed. Finished runs are exported to `archive/` **on the
  `playthroughs` branch**, never onto `main`; `.gitignore` here enforces that.
- **Load rules lazily** from the rules graph (`query-rules`, `get-rule`). Never
  read `rules/*.md` wholesale into context.

## Spoilers

`lore/gm-secret/`, `lore/gm-guide/the-plot-timeline.md` and
`lore/character-creation/the-four-companions.md` hold the reveals — the possession
scheme, the champion's identity, the twins. Keep them out of player-facing
narration until they land in play.

`session-logs/`, `novels/` and `archive/` are records of four finished
playthroughs and the worst spoilers in the project. **They are not on this
branch.** They live on `playthroughs`, which is never released, because a
25MB directory of the answer held back by a prose instruction in a skill file
is not held back at all.

To work with them:

```bash
git checkout playthroughs            # the full record
git checkout main                    # the release tree
git checkout playthroughs -- novels/ # or pull one directory across
```

Do not merge `playthroughs` into `main`. It is a parallel record, not work in
progress, and `main` is what a player installs.

## A note on `claude plugin validate --strict`

It warns that `CLAUDE.md` at the plugin root is not loaded as project context and
that shipped context belongs in a skill. **That warning is correct and expected**
— it is the reason the top of this file says what it says, and the reason
everything load-bearing lives in `skills/purewater/SKILL.md`. Validate without
`--strict`, or expect that one warning.
