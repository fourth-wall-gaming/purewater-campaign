---
id: "myth-lore-rolling-your-own"
title: "Rolling Your Own"
category: "character-creation"
visibility: "player"
summary: "How to build a new character for Purewater and write a backstory with the player, rather than for them"
created_at: "2026-09-18T00:00:00"
---

A player who would rather invent somebody than take a pregen is doing the better
thing, and the most recent playthrough proves it — a rolled half-orc named Kag
turned out to be the most interesting character this scenario has had, and she is
now an NPC in it.

This is how to do that without it taking an hour or producing somebody who has no
reason to be in Purewater.

---

## The order that works

**1. Roll first, decide who they are second.** Mythras characteristics are
interesting precisely because you did not choose them. Offer the methods the
system gives — `create-character --roll` — and read the numbers out *before*
asking what kind of person this is. A CHA of 5 or a SIZ of 20 is a character
concept arriving unbidden, and it is nearly always better than the concept the
player walked in with.

**2. Ask the one question that matters.** Not "what is your backstory". Ask:

> **Why are you in Purewater this week, and who would notice if you left?**

A character with an answer to that is in the story. A character without one is a
tourist, and every session will be you inventing reasons for them to care.

**3. Put them in somebody's debt, or somebody in theirs.** One named relationship
with an existing NPC, decided now. The city is full of people who already want
things — a guild boss who is short of answers, a madame who is short of law, a
harbourmaster, a temple, a company of unpaid soldiers. Pick one and write the tie
down. This is the single highest-value thing on this page.

**4. Passions before skills.** Three of them, and **build a collision into them on
purpose** — a loyalty that will one day disagree with an ambition. Five points of
gap is plenty; it does not need to be a tragedy. Kag carried *Loyalty (Crowbill)
60* against *Ambition (to run these streets as he does) 55* for a whole campaign
and it never once stopped being live.

Passions are also where the character's voice comes from, so spend real time here
and let the player hear themselves say them out loud.

**5. Then the sheet.** Skills, kit, and the rest through the engine. Keep it
quick — nobody has ever enjoyed the shopping.

## Writing the backstory *with* them

Do not hand a player a finished history. Ask four questions and write down their
answers:

1. **Where did they learn the thing they are good at, and from whom?** Name that
   person. They may still be alive.
2. **What did they lose?** Not a tragedy competition — something specific and
   ordinary. A trade, a hand, a name, a city they cannot go back to.
3. **What do they carry?** One object with a history. It will come up.
4. **What would make them walk away from all of this?** This is the one players
   have not thought about, and it is the one that makes them a person.

Then **read it back to them as prose, in the voice of the game**, two short
paragraphs, and ask if it is right. Fix what they correct. That read-back is the
moment a stat block becomes somebody they will defend.

Write the result into the character with `update-character --actor-notes`, so it
survives the session and so future sessions play them consistently.

## Braiding them into the scenario

A new character must not become a side-quest. `TABLE.md §0b` has the eight-step
method — the short version:

- **Find where they already are.** Do not invent a new corner of the setting;
  the answer is nearly always already in `beats/` or `agendas/`.
- **The intersection is where their ordinary work breaks.** Not a summons and not
  a prophecy. Something only they would notice, running on their best skills
  rather than their class.
- **One beat per act, braided** — at least one of which is their angle on a beat
  that already exists.
- **Aim it at a decision only they can make.**

Twenty minutes of this is worth more than any amount of session-one improvisation.

## Then put them somewhere

**`move-character` to a real location before you narrate a line.** A PC with no
location is nowhere, every beat reads as offscreen, and the living world will
quietly fail to include them. The four entry-point locations are the obvious
choices — the Ford, the Anminster road, Caravan Square — but anywhere in the city
works if they have a reason to be there.

Then `set-scene`, and open on the smallest concrete thing in front of them.
