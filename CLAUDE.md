# Running this campaign (mythras-gm)

This directory is a **published snapshot** of a `mythras-gm` campaign — a Mythras
Imperative (Classic Fantasy port) RPG whose **live, authoritative state lives in
TypeDB**, not in these files. The file tree is an export for reading, diffing,
and version control. It is **not the save game**, and editing it does not change
the game.

> **AI assistants: if the user asks to play, continue, or GM this campaign,
> invoke the `mythras-gm` skill and run through its CLI. Do NOT game-master
> directly off these files.** GMing from the file tree bypasses the dice engine
> and the persistent database: your rolls aren't auditable, and any state you
> change here is silently discarded the next time the campaign is exported.

## Where the save actually is

**Database `mythras`, on `localhost:1730`, in the Docker container
`mythras-typedb` (image `typedb/typedb:3.8.0`).** These are the CLI defaults, so
you do not need to export anything. If the container is not running, bring it up
with `docker compose up -d` from the `mythras-gm` repo.

> This is the game's own TypeDB, not the Alhazen stack on 1729. It was created
> by hand with `restart: no` and no compose file, so it did not survive a
> reboot — and while it was down the save was moved onto the Alhazen server and
> this note was deleted as describing something that did not exist. It does
> exist. There is now a compose file with `restart: unless-stopped`.
>
> Migrated back on 11 Sep 2026. The legacy database predated the alh-collection
> rebase and had to be mapped across with GLAV rules rather than dumped and
> reloaded — see `migrations/legacy-mythras/` in the engine repo. Older copies
> remain on 1729 in `alhazen_notebook` and `alh_mythras`, and there are file
> exports plus a native database export under `~/mythras-backups/`.
>
> **If a command returns nothing, check which database and port you are pointed
> at before importing anything.**

The live game is:

- **Purewater — Gardwen** — `myth-campaign-44abede1efbf`

Other Purewater rows in the same database, none of which you should write to:

| id | what it is |
|---|---|
| `myth-campaign-66a98ba4a70e` | v1, **finished** — session 2, ends at CH.25 |
| `myth-campaign-8327f8687a98` | archive of the Magda playthrough |
| `myth-campaign-476ed76d90b8` | the Magda v2 run, superseded |
| `myth-campaign-cdd876ebe965` | the Conall run, archived under `archive/session-02-conall/` |

> **If `list-campaigns` does not show `myth-campaign-44abede1efbf`, STOP.**
> Do not run `import-campaign` to "fix" it — you will fork the save and play on
> a copy while the real one rots. Check the container is up
> (`docker start alhazen-typedb`) and ask.

Because the campaign is already loaded, skip the import and go straight to
`get-context`.

## How to run

1. **Invoke the `mythras-gm` skill** (triggers: "play", "continue campaign",
   "run mythras", "gamesmaster"). Read its `SKILL.md`, then `USAGE.md`.
2. Confirm it's loaded: `list-campaigns` — you should see
   `myth-campaign-44abede1efbf`. If you do not, read the warning above and stop.
3. `get-context --campaign myth-campaign-44abede1efbf --compact` — **this is the
   save file**: current scene, PC combat cards and where each one is standing,
   factions, recent events.
4. Recap the scene in a few sentences, then play.

## Operating rules (non-negotiable)

- **Every mechanical resolution goes through the CLI** — `roll-skill`,
  `roll-opposed`, `resolve-attack`, `apply-damage`, `heal`. Never free-hand,
  estimate, or narrate dice you didn't roll through the engine; it is the shared,
  deterministic dice tower, and it looks skills up from the DB for you.
- **The database is the save.** Persist anything worth remembering with
  `log-event`, `set-scene`, `update-character`, `add-lore`, etc. Never hand-edit
  the JSON/markdown here to change game state — those edits don't reach TypeDB and
  are lost on the next export.
- **Show the dice.** This table's house rule: surface every roll as
  `action (target N) → rolled R = result`, including luck-point spends. The CLI's
  JSON output gives you the numbers to quote.
- **Load rules lazily** from the rules graph (`query-rules`, `get-rule`) — never
  read `rules/*.md` wholesale into context.
- **Re-export** (`export-campaign`) when you want a fresh file snapshot for git.

## GM secrets

`lore/gm-secret/` and `lore/gm-guide/the-plot-timeline.md` hold the reveals
(the possession scheme, the champion's identity). Keep them out of player-facing
narration until they land in play.

Campaign id: `myth-campaign-44abede1efbf` (**Purewater — Gardwen**)
