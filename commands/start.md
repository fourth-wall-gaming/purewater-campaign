---
description: Begin Purewater from the beginning — introduce Mythras, import the scenario, make or choose a character, and open the first scene.
---

# Start Purewater

The zero-state path. Use this when the campaign has never been played on this
machine. **If a game is already in progress, stop and use `/mythras-gm:play`
instead** — step 2 checks, and it matters, because a start command that resets
somebody's campaign is worse than no start command at all.

Resolve the engine first; everything below needs it:

```bash
. "${CLAUDE_PLUGIN_ROOT}/scripts/engine.sh"   # sets GM_ROOT, GM_SKILL, GM_CLI, gm()
[ -z "$GM_ROOT" ] && echo "mythras-gm is not installed: /plugin install mythras-gm@fourth-wall-gaming"
```

## 1. Is the player new to Mythras? Brief them first

Ask — do not assume. If they have played it, say so in a line and move on.

If they have not, read `${GM_SKILL}/NEW-TO-MYTHRAS.md` and give them the
one-minute version **in your own words**: skills are percentages you roll under,
combat picks hit locations and lets the winner choose a Special Effect, and
Passions are the good bit. Offer the links — the free Classic Fantasy Imperative
rules, and **inwils' YouTube channel** if they would rather be shown than read.

Do this **before** character creation. Knowing that Passions matter changes what a
player writes down, and a player who has been told "you don't need to learn any
rules" relaxes.

## 2. Check the state of the save

```bash
gm init-db                                        # idempotent; stop and report if it fails
gm get-campaign --campaign myth-campaign-purewater-s1
```

- **Not found** → carry on to step 3.
- **Found with `myth-session-number` of 0** → already imported, never started.
  Skip step 3.
- **Found with a session number above 0** → a game is in progress. **Stop.** Tell
  the player what clock it is at and hand them `/mythras-gm:play`. Do not import,
  do not re-seed, and do not offer to start over unless they ask in so many words.

## 3. Import the scenario

```bash
gm import-campaign --path "${CLAUDE_PLUGIN_ROOT}"
```

A few hundred rows — 43 beats, 15 agendas, 42 characters, 22 locations, the lore
graph. Say it will take a moment. The seed id is fixed on purpose: importing the
same package twice fails loudly rather than quietly forking the save.

## 4. Read the table rules and the plan

Not optional, and not summarised here — they belong to the engine:

- `${GM_SKILL}/TABLE.md` — how to run the table
- `${GM_SKILL}/styles/gamesmaster.md` — the voice
- `${CLAUDE_PLUGIN_ROOT}/setting/the-story.md` — what this scenario is *for*, act
  by act, and what each act takes from the party

That last path is why this command exists at all: the engine's `SKILL.md` names
`setting/the-story.md` with no path, and only a campaign plugin knows where its
own files live.

## 5. Describe the setting

Read `${CLAUDE_PLUGIN_ROOT}/lore/player-briefing/welcome-to-purewater.md` and give
it to them properly — about five minutes, in your own words, and **stop as soon as
they start asking questions**, because their questions are better than your
briefing.

The four things they must walk away with: there is no ground and no horses, so
everything moves by boat and outsiders cannot crew one; the water is the goddess
and the Order owns it; the Tourney is in three days; and a Baron has been sitting
on this city for nine weeks with a champion nobody has seen, and nobody has called
it an occupation out loud.

Everything in that file is public knowledge in the city. Offer the deeper lore by
name if they want it; do not recite it.

## 6. Offer the four, in full

Read `${CLAUDE_PLUGIN_ROOT}/lore/player-briefing/choosing-a-character.md` and give
them **a real paragraph each** — Gardwen, Magda, Randall, Conall — including the
italic line that says what each one is *for*. All four before you ask, because
nobody can choose from a list they have not heard.

Do not rank them. Do not have a favourite out loud. Do not answer "what happens to
them", even asked directly — it depends on what they do.

Say that the other three stay in the world as GM-run companions they will meet.
It makes the choice feel less like a door closing, and it is true.

**Or they roll their own.** If they would rather build somebody, go to
`${CLAUDE_PLUGIN_ROOT}/lore/character-creation/rolling-your-own.md` and work
through it *with* them: roll first and decide who they are second, ask why they are
in Purewater this week and who would notice if they left, put them in somebody's
debt, then build the Passions with a collision in them on purpose. Ask the four
backstory questions, **read the result back as prose in the voice of the game**,
and save it with `update-character --actor-notes`.

Do not write a backstory for them. Ask, and write down what they say.

## 7. Set it up

For a pregen:

```bash
gm update-campaign --campaign myth-campaign-purewater-s1 --played <chosen-pc-id>
```

`--played` tells the world-clock which PCs are the player's, so the other three
stay in the world as companions rather than being staged as absent.

For a rolled character: `create-character --type pc`, then **`move-character` to a
real location**. Without that they are nowhere and every beat reads as offscreen.

Then, either way:

```bash
gm set-scene --campaign myth-campaign-purewater-s1 --scene "<their opening>"
gm update-campaign --campaign myth-campaign-purewater-s1 --session-number 1
gm log-event --campaign myth-campaign-purewater-s1 --type session-start --summary "..."
```

## 8. Give them their backstory, then open the scene

**This is the payoff of the choice and it should not be rushed.**

For a pregen, read their entry point from
`${CLAUDE_PLUGIN_ROOT}/lore/entry-points/` — it is written in second person and it
is theirs: who they were before this week, what they can do, what they are walking
into, and what they do not know. Deliver it as prose, not as a briefing document.
It ends with an opening move; use it.

For a rolled character, read back the backstory the two of you just wrote, in the
same register.

Then narrate the opening — two to four sentences, smell and noise before sight —
and **stop**, and hand the floor over. Do not play the first scene for them.

From here on it is `/mythras-gm:play`.
