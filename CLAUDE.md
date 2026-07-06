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

## This campaign is already loaded

It lives in the `alh_mythras` TypeDB database as:

- **And Then the Dragons Came: Purewater** — `myth-campaign-66a98ba4a70e`

So you normally skip the import step and go straight to `get-context`.

## How to run

1. **Invoke the `mythras-gm` skill** (triggers: "play", "continue campaign",
   "run mythras", "gamesmaster"). Read its `SKILL.md`, then `USAGE.md`.
2. Confirm it's loaded: `list-campaigns` — you should see the id above. If it
   somehow isn't there, `import-campaign --path <this-directory>` (no `--new-ids`
   — this tree carries stable ids).
3. `get-context --campaign myth-campaign-66a98ba4a70e --compact` — **this is the
   save file**: current scene, PC combat cards, factions, recent events.
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

Campaign id: `myth-campaign-66a98ba4a70e`
