# Purewater — run 5 (Halla, Nimras, Hrill), played in Codex

**Three concurrent playthroughs kept as a record. This is not a starting
point** — for that, install the plugin and run `/purewater:start`, which imports
the clean seed at the repository root.

The fifth run, and the first with **three protagonists on independent clocks in
one world**. Where runs 1–4 were a single party through one arc, this is three
unconnected lives in the same city, each with its own local date, advanced
separately and never rewound onto each other.

- **Halla** — male dwarf Fighter; Forge Quarter bodyguard, fixer and hired muscle.
- **Nimras** — human Rank 2 Magic-User; freelance mage hunter trained by an
  independent fellowship.
- **Hrill Helmdance** — human knight, 42, Rank 2; an honourable veteran looking
  for a use for himself that is not fighting.

Snapshot taken at **session 8, `time_index` 229**, with Nimras at local d8/day
and the shared world clock at d23. Played **5 September – 28 October 2026**.

| Contents | Count |
|---|---|
| Lore entries | 53 |
| Characters | 202 (PCs: Halla, Nimras, Hrill Helmdance) |
| Locations | 94 |
| Factions | 24 |
| Agendas | 48 |
| Beats | 115 |
| Facts | 767 |
| Encounters | 21 |
| Journal events | 1,197 across 9 sessions |
| Knowledge edges | 1,913 |
| Storylines | 3 |

Journal by kind: 761 scenes, 142 combats, 133 GM notes, 101 skill rolls,
49 decisions, 8 session starts, 3 session ends.

## Where this came from

It was played in **Codex**, not Claude Code, in a separate working directory
(`~/Documents/ChatGPT/mythras`) that was never under version control — the whole
body of work sat untracked. This branch is that material brought into the
repository for the first time.

The campaign id is the same seed as the root of this repo
(`myth-campaign-purewater-s1`), played forward. Checked directory by directory
against `main`, the run is **purely additive**: it adds 32 agendas, 82 beats,
164 characters, 752 facts, 11 factions, 72 locations, 31 lore entries and 21
encounters, and changes **no** existing file. Only the journal differs, from the
seed's single note to 1,197 events.

## It needs an engine this repository does not ship

The run depends on **parallel storyline clocks** — `--pc` / `--storyline` /
`list-storylines`, and the `storylines.json` beside this file. That is a
1,810-line patch across 12 files which lives in the Codex workspace and is in
neither `mythras-gm` nor the installed plugin; both return zero matches for
"storyline". Loading this snapshot into the shipped engine will not reproduce
the three independent clocks, and the per-PC local dates in `campaign.yaml` and
in character `extras` will read as one shared timeline.

That patch is **not** included here. It is engine work and belongs in
`mythras-gm` if it is wanted.

## preparation/

The GM-side material that produced the run, copied as found:

- `scenarios/` — 146 files. Eight prepared adventures (Glass Hounds, Midnight
  Exchange, The Quiet War, The Price of Bread, Greywatch, Edda, The Road Beyond
  the Banners, Unbroken Crown), their arcs, situation lists, id manifests and
  setup scripts.
- `characters/` — build and verification scripts for the three PCs.
- `purewater-magic-and-power.md`, `purewater-working-mages.md` and their
  manifest — setting canon with no counterpart on `main`.
- `purewater-halla-live-story.md` — Halla's run written out as prose.
- `codex-AGENTS.md` — the instructions Codex was operating under, kept because
  the method it mandates is visible throughout the prep.

`package-README.md` and `package-CLAUDE.md` are the export's own package files,
renamed so this README is the one a reader meets first.
