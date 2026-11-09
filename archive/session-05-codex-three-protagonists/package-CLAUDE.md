# Running this campaign (mythras-gm)

This directory is a **published snapshot** of a `mythras-gm` campaign — a Mythras
Imperative RPG whose **live, authoritative state lives in TypeDB**, not in these
files. The file tree is an export for reading, diffing, and version control. It
is **not the save game**, and editing it does not change the game.

> **AI assistants: if the user asks to play, continue, or GM this campaign,
> invoke the `mythras-gm` skill and run through its CLI. Do NOT game-master
> directly off these files.** GMing from the file tree bypasses the dice engine
> and the persistent database: your rolls aren't auditable, and any state you
> change here is silently discarded the next time the campaign is exported.

## How to run

1. **Invoke the `mythras-gm` skill** (triggers: "play", "continue campaign",
   "run mythras", "gamesmaster"). Read its `SKILL.md`, then `USAGE.md`.
2. **Make sure this campaign is loaded into TypeDB:**
   - `list-campaigns` — look for **And Then the Dragons Came: Purewater** (`myth-campaign-purewater-s1`).
   - If it isn't there, `import-campaign --path <this-directory>` (add
     `--new-ids` only to load a second copy alongside an existing one).
3. `get-context --campaign myth-campaign-purewater-s1 --compact` — **this is the save file**:
   current scene, PC combat cards, factions, recent events.
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
- **Load rules lazily** from the rules graph (`query-rules`, `get-rule`) — never
  read `rules/*.md` wholesale into context.
- **Re-export** (`export-campaign`) when you want a fresh file snapshot for git.

Campaign id: `myth-campaign-purewater-s1`
