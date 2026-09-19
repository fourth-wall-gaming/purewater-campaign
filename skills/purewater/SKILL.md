---
name: purewater
description: The Purewater campaign for mythras-gm — And Then the Dragons Came, a canal city three days before the Lake Lady's Tourney. Use when the user wants to play, start or continue Purewater, or asks about the Lake Lady, the Tourney, the di Teufels, or the dragons coming.
---

# Purewater

A campaign package for the **mythras-gm** engine. This skill is not a second GM
manual — the engine owns how to run a table (`TABLE.md`) and this owns four things
the engine structurally cannot know.

## 1. Where this campaign's files are

The engine's `SKILL.md` tells you to read `setting/the-story.md` and gives no
path, because a plugin cannot know where another plugin's data lives. Here it is:

```bash
PW="${CLAUDE_PLUGIN_ROOT}"
. "${PW}/scripts/engine.sh"    # sets GM_ROOT, GM_SKILL, GM_CLI and a gm() shell function
```

| what | where |
|---|---|
| the arc, act by act | `${PW}/setting/the-story.md` |
| player-facing briefing | `${PW}/lore/player-briefing/` |
| the four entry points | `${PW}/lore/entry-points/` |
| rolling a new character | `${PW}/lore/character-creation/rolling-your-own.md` |
| beat texts | `${PW}/beats/` |
| Kag, as an NPC | `${PW}/setting/kag-as-an-npc.md` |

## 2. The campaign id

**`myth-campaign-purewater-s1`** — fixed, shipped in `campaign.yaml`, the same on
every install. It is the only id that should ever appear in this package's docs.
Set `MYTH_CAMPAIGN` to it and stop passing `--campaign` everywhere.

A first run needs `/purewater:start`, which imports it. If `get-campaign` on that
id fails, the campaign is not imported yet — say so rather than improvising, and
**never GM from the files in this package**: they are a source export, not the
save, and edits to them never reach the game.

## 3. Never read these during play

This repository contains, for archival reasons, complete records of four previous
playthroughs. They are the highest-grade spoilers in the project.

| do not read | what is in it |
|---|---|
| `session-logs/` | full transcripts of prior runs |
| `novels/` | finished novelisations, including every ending |
| `archive/` | the end-state of four campaigns |
| `setting/adventure.md`, `setting/the-story-so-far.md` | the original adventure's full plot |
| `lore/gm-secret/`, `lore/gm-guide/the-plot-timeline.md` | the reveals |
| `lore/character-creation/the-four-companions.md` | GM-only; gives away the twins and the parentage |

The GM-side files are yours to use, but the reveals in them land **in play** and
never in narration before then. The first three are not even that — they are
records of somebody else's game and reading them will make you tell this one
wrong.

## 4. This campaign's own conventions

- **The clock is day-keyed.** `d-3` through `d0` (the Tourney) to `d2`. Time is an
  index; `d-3/dawn` is 52. `tick` between scenes — the living world runs whether
  anybody watches or not.
- **Fifteen agendas on clocks and 43 beats.** `forecast` between scenes, and
  `brief --id <beat>` **before narrating toward any beat**. Never narrate toward a
  beat you have not opened; the file is nearly always better than the mechanism you
  are about to invent.
- **Brief a place every time the party moves.** `brief --id <location>` carries
  the world constraints, and they are load-bearing: no roads, no horses,
  everything by boat, and outsiders cannot crew one.
- **Kag is an NPC and there is one rule for her.** How you talk to her decides
  what she is. Address the muscle and she is exactly as much use as she was paid to
  be; ask her what a thing *costs* and you have the best analyst in Purewater for
  nothing. It is not an Influence roll.

## Commands

| | |
|---|---|
| `/purewater:start` | first run: brief, import, choose or roll a character, open the scene |
| `/mythras-gm:play` | every session after that |
| `/mythras-gm:setup` | once per machine, if the database is not up |
