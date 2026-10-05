# And Then the Dragons Came: Purewater

A *Classic Fantasy Imperative* scenario packaged as a campaign for the
[mythras-gm](https://github.com/fourth-wall-gaming/mythras-gm) engine, and
shipped as a Claude Code plugin. This README is the technical account: what the
package is, how the engine loads and runs it, and how to work on it.

**If you want to run Purewater yourself, at a table, without the engine**, you
want the Games Master's Guide instead — and your players want the Players' Guide —
both published from this repository at
**https://fourth-wall-gaming.github.io/purewater-campaign/**.

```
/plugin marketplace add fourth-wall-gaming/mythras-gm
/plugin install purewater@fourth-wall-gaming
/mythras-gm:setup      # once per machine: TypeDB, schema, rules graph
/purewater:start       # import the seed, choose a character, open the scene
```

---

## 1. What this repository is

| | |
|---|---|
| **Format** | `mythras-gm-campaign`, format version **1.1** (`campaign.yaml`) |
| **System** | *Classic Fantasy Imperative*, on *Mythras Imperative* |
| **Campaign id** | **`myth-campaign-purewater-s1`** — fixed, the same on every install |
| **Seed state** | world clock `d-3/dawn` (`time_index` 52), session 0, every beat `pending`, one seed note in the journal, four pregens offered and none chosen |
| **Plugin** | `purewater` — depends on `mythras-gm` (`.claude-plugin/plugin.json`) |

**It is a seed, not a save.** The file tree is the *source* of a campaign. A save
lives in TypeDB: `/purewater:start` imports this package once, and from then on
the database is the game. Editing these files does not change a running campaign,
and the engine never writes back to them.

The marketplace is the **engine's** repository, not this one. This repository is a
plugin; mythras-gm carries the marketplace manifest that lists it, so a campaign's
dependency on the engine resolves by itself. Adding *this* repository as a
marketplace fails with `no manifest found at .claude-plugin/marketplace.json`,
which is correct.

### Contents

| Contents | Count |
|---|---|
| Lore entries | 28 |
| Characters | 42 (playable: Conall Bjornlasch, Gardwen, Magda, Randall) |
| Creature templates | 4 |
| Locations | 22 |
| Factions | 14 |
| Journal events | 1 |
| Agendas | 16 |
| Beats | 40 |
| Facts | 17 |

### Layout

| Directory | Contents |
|---|---|
| `agendas/` | What each character or faction wants, on a progress clock (markdown + frontmatter) |
| `beats/` | What happens next if nobody interferes, scheduled in world time (markdown + frontmatter) |
| `characters/` | `pcs/`, `npcs/`, `creatures/` — full Mythras sheets as JSON, with prose and actor notes |
| `templates/` | Reusable stat blocks the engine can `spawn` (Dragon Knights, the Watch, cutpurses) |
| `locations/` | Places, with staging notes and a **Map:** line naming the sheet they appear on |
| `factions/` | Factions and organisations |
| `facts/` | Situational truth: one proposition per file, `not-yet-true` until play establishes it |
| `journal/` | The event log; in the seed, one `gm-note` |
| `lore/` | The worldbook as database-ready entries, each marked `visibility: player` or `gm` |
| `setting/` | Long-form source: `the-story.md` (the plan), the original adventure, the worldbook books |
| `maps/` | The city map (canon), district sheets, building plans, the realm, encounters, GM-only secrets |
| `commands/` | The `/purewater:start` slash command |
| `skills/` | `skills/purewater/SKILL.md` — what the engine needs to know about this campaign |
| `hooks/` | The SessionStart hook that reports the state of the save |
| `scripts/` | `engine.sh` (finds the engine) and `session-start.sh` |
| `guide/` | The two books: `gm/` and `players/` chapters, the build script, templates and stylesheet |
| `tests/` | `test_seed.py` — the seed stays a seed, and the docs stay true; `test_guide.py` — the guide stays complete |

`knowledge.json` at the root holds who knows which fact, how, and since when.

---

## 2. How the plugin finds the engine

A plugin's `${CLAUDE_PLUGIN_ROOT}` resolves to its own directory and there is no
variable for a sibling's, so a campaign cannot name the engine it depends on.
`scripts/engine.sh` looks for it, in order of how much it trusts the answer:

1. **`$MYTHRAS_GM_ROOT`** — the documented escape hatch, and what CI uses.
2. **`~/.claude/mythras-gm/engine-root`** — the pointer the engine's `init-db`
   writes; checked, because a plugin upgrade can leave it stale.
3. **`~/.claude/plugins/installed_plugins.json`** — where Claude Code says it put
   the engine.
4. **A search of the plugin trees**, which come in more than one layout.

Sourcing it sets `GM_ROOT`, `GM_SKILL`, `GM_CLI` and a `gm` shell function:

```bash
. "${CLAUDE_PLUGIN_ROOT}/scripts/engine.sh"
gm doctor
```

Every variable in it expands with `:-`, because the hook that sources it runs
under `set -u`. The hook (`hooks/hooks.json` → `scripts/session-start.sh`) only
**reports** the state of the save at session start. It never imports and never
blocks.

---

## 3. Starting and resuming

`/purewater:start` (`commands/start.md`) is the zero-state path:

1. Brief the player on *Mythras* if they are new to it — before character
   creation, because knowing that Passions matter changes what a player writes down.
2. `gm init-db`, then `gm get-campaign --campaign myth-campaign-purewater-s1`.
   - **Not found** → import.
   - **Session 0** → imported, never played; skip the import.
   - **Session above 0** → a game is in progress. **Stop** and hand over to
     `/mythras-gm:play`. The command never re-seeds a live game.
3. `gm import-campaign --path "${CLAUDE_PLUGIN_ROOT}"`.
4. Read the engine's `TABLE.md` and `styles/gamesmaster.md`, and this campaign's
   `setting/the-story.md`.
5. Brief the setting (`lore/player-briefing/welcome-to-purewater.md`), offer the
   four pregens in full (`choosing-a-character.md`) or roll one
   (`lore/character-creation/rolling-your-own.md`).
6. `update-campaign --played <pc-id>` so the other three stay in the world as
   companions; for a rolled character, `create-character --type pc` and
   **`move-character` to a real location**, or every beat reads as offscreen.
7. `set-scene`, `update-campaign --session-number 1`, `log-event --type session-start`.
8. Deliver the entry point from `lore/entry-points/` and open the scene.

Every session after that is **`/mythras-gm:play`**.

### The campaign id

`myth-campaign-purewater-s1` is a key in the schema, so **importing the package
twice fails loudly** instead of quietly forking somebody's save. To run a second,
parallel playthrough deliberately, pass `--new-ids`. Set `MYTHRAS_CAMPAIGN` to the
id and stop passing `--campaign` everywhere.

---

## 4. The world clock

The clock is **day-keyed**, four watches a day — `dawn`, `day`, `dusk`, `night` —
and stored as an integer `time_index`. `d-3/dawn` is **52**.

| Day | What it is |
|---|---|
| `d-3` | Arrival: the Baron's column enters the city |
| `d-2` | The city closes |
| `d-1` | The presentation of the entrants |
| `d0` | The Tourney, day one: the Archery |
| `d1` | The Tourney, day two: the Single Combat |
| `d2` | The Tourney, day three: the Run, then the closing |

Negative days read as what they are — *two days before* — so the numbering has to
keep meaning that. Move time with `tick`, never by hand:

```bash
gm forecast                       # the canonical thread: what happens if nobody interferes
gm tick --to "d-3/night"          # advance; report what came due, onscreen or off
gm brief --id <beat|npc|place>    # read it before you narrate it
```

---

## 5. Agendas and beats: the living world

An **agenda** is a goal held by a character or faction, tracked on a clock.
A **beat** is the next concrete thing an agenda produces if nobody interferes,
placed in world time with a location and a cast. Run `gm list-agendas` for the
sixteen agendas and their clocks, and `gm forecast` for the schedule.

`tick` returns each due beat flagged **onscreen** or **offscreen**, computed from
where the player characters actually are — not chosen by the Games Master.
Onscreen beats are played as scenes; offscreen beats happened anyway, and are
recorded with `fire-beat --outcome narrated --log` so the party can discover them.

### Beat frontmatter

| Field | Meaning |
|---|---|
| `when` | The **latest** the beat happens — a backstop, not an appointment |
| `trigger` | `time`, `clock>=N` (the beat's agenda has reached N), `condition`, or `contact` |
| `needs` | Preconditions: `played: <beat-slug>`, `fact: <fact-slug>`, `contact: <char-or-loc-id>`, or `any:` a list of those |
| `onscreen_if` | Prose: who has to be where for it to be a scene |
| `agenda`, `place`, `cast` | Ids; `place` decides onscreen staging |
| `by: null` | No backstop: an opportunity that never fires on its own (`orrin-sculle-decides`) |

**Conditions accelerate; time backstops.** A beat can be brought forward when the
party earns it and can never be stalled forever. Bend a beat to what play has made
true with `revise-beat`; never edit the file.

### The three endings, and the one thing the engine cannot decide

The last day turns on the binding locket (`nus-lifts-the-binding-locket`,
`d1/night`):

| Ending | Condition | Beats that fire |
|---|---|---|
| **A** | Never stolen, or the theft failed | `the-run-across-the-town`, `the-private-audience` |
| **B** | Stolen; Blau recovers it | `the-lullwater-burns`, `sinnit-sells-nus`, `the-private-audience`, `the-impossible-shot` |
| **C** | Stolen; Nus lives and the party keeps it from Blau | `the-lullwater-burns`, `sinnit-sells-nus`, `thuban-breaks-out` |

`needs` can express "the theft happened" but not "the locket is *still* in the
party's hands". So at `d2/dawn` the Games Master reads the board and cancels the
beats that no longer apply. `setting/the-story.md` carries the same table.

### The arc is not loaded into the save, and that is expected

`forecast` reports `NO ARC LOADED`. `setting/the-story.md` is a plan for the Games
Master to **read** (step 4 above), one beat per row. It is not in the engine's arc
format: `sync-arc --file` expects YAML front matter and would rewrite the beats
from the document. **Do not run `sync-arc` on `the-story.md`.**

---

## 6. Facts and knowledge

`facts/` holds propositions about the world, each `not-yet-true` or `established`,
each with a `truth` that may be `false` — a belief the city holds that is not so
(*The man who carved Emmeralda was Randall the Pearl thief*). `knowledge.json`
records who knows what, how (`witnessed`, `deduced`, `told`) and how sure they are.
In play: `establish-fact`, `learn`, `who-knows`, `character-view`, and
`check-consistency` to reconcile the graph against the clock.

---

## 7. Working on this repository

### Run it locally

```bash
claude --plugin-dir ~/mythras-gm --plugin-dir ~/purewater-campaign-v2
```

Local copies satisfy the `dependencies` entry, so this exercises the real
resolution path without publishing anything.

### Test an import — never against the live database

```bash
export TYPEDB_PORT=1730 TYPEDB_DATABASE=purewater_test
. scripts/engine.sh
gm init-db
gm delete-campaign --campaign myth-campaign-purewater-s1 --yes   # only in the scratch database
gm import-campaign --path .
gm forecast
gm check-consistency
```

### Tests

```bash
uv run --with pytest --with pyyaml --with pillow pytest -q tests/
```

`test_seed.py` holds the seed to being a seed — clock 52, session 0, one journal
note, every beat pending, no character named in the opening scene — and the docs
to telling the truth: the counts in the table above match the disk, every
documented directory exists, only one campaign id is ever offered, and the player
briefing keeps its secrets.

`test_guide.py` holds both books to the data: every chapter in the Design
Mechanism's house style (Games Master, Non-Player Character, characters — never
GM, NPC, PC or "etc"), headings no deeper than four, every directive resolving,
every beat told exactly once, a stat block for every sheet and template, every
district and building map in the Games Master's Guide — and the Players' Guide
free of spoilers and of the Games Master's maps.

### The two books

The human-readable site at
https://fourth-wall-gaming.github.io/purewater-campaign/ holds two books, built
from this repository by `guide/build.py` into `_site/` (ignored by git):

- **The Games Master's Guide** (`guide/gm/`) in three parts, *Background*,
  *People and Places in Purewater* and *Events and Story Structure*, with
  appendices for the week at a glance and full statistics. It is written as prose
  for a person to read and run from, in the Design Mechanism's house style.
- **The Players' Guide** (`guide/players/`): the city as its people know it, the
  four characters with their sheets, making your own, and a *Mythras* primer.
  It is held spoiler-free by test.

```bash
uv run --with pyyaml --with pillow python guide/build.py            # site + both PDFs
uv run --with pyyaml --with pillow python guide/build.py --no-pdf   # site only, faster
```

It needs **pandoc** (3.10) and **Typst** (0.14). Each chapter opens with its
part, `<!-- part: Background -->`, and its title. **Anything with a number in it
comes from the campaign files**, through a directive on a line of its own, so a
fix to a sheet or a beat reaches the book without being retyped:

| Directive | Renders |
|---|---|
| `<!-- statblock: blau -->` | One sheet as a TDM stat block, with heading and description: major, minor, or monster for creatures and templates |
| `<!-- sheet: randall -->` | The stat tables alone, for the Players' Guide |
| `<!-- statblocks: major\|minor\|pcs\|creatures\|templates -->` | Every sheet of that kind |
| `<!-- map: districts/pearl -->` | The finished sheet, downsized for the web, with its numbered key from `labels.yaml` |
| `<!-- timeline -->`, `<!-- agendas -->`, `<!-- roster -->`, `<!-- areas -->` | Tables and lists from the beats, agendas, sheets and locations |
| `<!-- lore: lore/...md -->` | A lore entry, boxed |
| `<!-- box -->` … `<!-- endbox -->` | Boxed text |
| `<!-- covers: beat-a, beat-b -->` | Nothing visible: records which beats the prose beside it tells |

The Games Master's Guide does not use beats as sections; it tells them as
prose. The `covers` markers let `test_guide.py` prove that every beat in the
catalogue is told somewhere, exactly once. Text from the data was written for the
engine and says GM, PC and NPC; `guide/house.py` normalises it on the way in.
`.github/workflows/guide.yml` runs the tests and builds the site on every pull
request, and publishes it to Pages on every push to `main`.

### Editing the plot

The beats are the catalogue and `setting/the-story.md` is the plan. **Every beat
appears in `the-story.md` exactly once.** A new beat needs a frontmatter `id` of
the form `myth-beat-<12 hex>`, a `when` (opportunity beats still need a backstop
time, because `add-beat` will not take one without), a row in the plan, and its telling in the Games Master's Guide: prose in the
right chapter of `guide/gm/` with a `<!-- covers: slug -->` marker beside it.
Agendas take `myth-agenda-<12 hex>`. Update the counts above and in
`commands/start.md`, `skills/purewater/SKILL.md`, `.claude-plugin/plugin.json`
and the seed note in `journal/events.json`.

### Exporting and playthroughs

`export-campaign` writes a fresh file snapshot of a save — **never over the root**,
which is the seed. Finished runs are exported to `archive/` **on the `playthroughs`
branch**, never onto `main`, and `.gitignore` enforces it. Session logs, novels and
archives of four previous playthroughs live only on `playthroughs`; they are the
worst spoilers in the project and are not part of a release.

### Spoilers in the release tree

Lore marked `visibility: "gm"`, `lore/gm-secret/`, `setting/the-story.md`,
`setting/adventure.md` and `lore/character-creation/the-four-companions.md`
contain the reveals. The engine keeps GM lore out of player-facing narration until
it lands in play; a person browsing this repository has no such protection.

---

Based on *Mythras Imperative*, written by Pete Nash and Lawrence Whitaker,
published by The Design Mechanism, Copyright 2023, used under the ORC License.
