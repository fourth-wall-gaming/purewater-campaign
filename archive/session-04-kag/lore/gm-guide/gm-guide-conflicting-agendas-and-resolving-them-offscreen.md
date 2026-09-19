---
id: "myth-lore-f10bee04984e"
title: "GM Guide: Conflicting agendas, and resolving them offscreen"
category: "gm-guide"
visibility: "gm"
summary: "When two agendas collide out of sight, the dice decide it, not the GM. The procedure: opposed roll, real outcome, clock feedback, and add-consequence so the result sticks."
created_at: "2026-09-09T00:00:00"
---

Everyone on this board wants something and several of them want incompatible
things. The rule is the same offscreen as on: **a beat is an attempt, not a
script, and the dice say what happened.** What follows is how to do that when
nobody is watching.

## 1. Before firing a beat, ask who it damages

`tick` hands you a due beat. Before resolving it, look at `list-agendas
--compact` and ask: **whose agenda does this beat hurt, and are they in a
position to do anything about it?**

If nobody is, it is a simple roll -- the acting NPC's relevant skill at a stated
difficulty. If somebody is, it is **opposed**, and that is the whole difference.

## 2. Roll it opposed

```
roll-opposed --id-a <actor> --skill-a <skill> \
             --id-b <resister> --skill-b <skill> \
             [--difficulty-a <grade>] [--difficulty-b <grade>]
```

Pick the skills honestly and out loud, the same way you would in front of a
player. Santo trying to have Emmeralda carried out of a house is *Deceit* or
*Influence* against Constantine's *Insight* or *Willpower*; men taking a boat off
a stair is *Intimidate* against a boatman's *Willpower*; a courier moving unseen
is *Stealth* against *Perception*.

The resister does not have to be present in the fiction to resist. A house with
standing orders, a network of watchers, a guild that checks its own paperwork --
all of these are somebody's skill, rolled.

## 3. Read all four results, not two

| | What it means |
|---|---|
| **Actor wins** | the beat's facts as written |
| **Resister wins** | the attempt happened and *failed* -- write different facts |
| **Both fail** | it stalls; nothing is established, and the actor tries again worse-tempered |
| **Critical either way** | the winner gets something extra: a witness, an object, a name, a debt |

**A botched offscreen attempt is not a non-event.** Santo failing to get her
aboard leaves a hired boatman who now knows something, a house that is awake all
night, and an heir who is frantic instead of methodical. Write those facts.

## 4. Feed the result back into both clocks

```
fire-beat --id <beat> --outcome played|narrated|preempted --witnesses <ids> --log
advance-agenda --id <winner's agenda> --by 1 --note "..."
advance-agenda --id <loser's agenda>  --by 0            # or stall it
```

The loser's clock should usually **not** simply freeze. A thwarted agenda either
stalls, changes method, or escalates -- and escalation is what makes a living
world feel dangerous rather than fair.

## 5. Make the conflict structural, so it is not your memory

This is the part that matters. **`add-consequence` is the agenda-conflict
primitive:**

```
add-consequence --fact <fact> --agenda <other agenda> \
                --effect thwart|abandon|stall|advance|activate|complete [--amount N]
```

Declare it **in advance**, when you can see that two agendas cannot both succeed.
Then whichever way the dice fall, the moment the winning fact is established the
losing agenda is thwarted or stalled *automatically*, and the cascade retires the
beats it was going to produce. Run `cascade --campaign <id>` after anything messy.

`require-fact --agenda A --fact F` is the same idea pointing the other way: a
dormant agenda that wakes the instant its holder learns something.

Between them, an agenda conflict stops depending on the GM remembering it.

## 6. Priority breaks ties

When two agendas come due in the same watch and cannot both act, the higher
`priority` (1-5) goes first, and the loser reacts to a world that has already
changed. That is what priority is for; it is not importance, it is **initiative**.

## Live conflicts on this board

| | vs | |
|---|---|---|
| Santo — *Have her* | Constantine — *Protect my house* | one girl, one house |
| The Dragon Knights — *Hold the streets* | Marda — *Make them pay for one of ours* | every unanswered incident feeds both |
| Hanzo — *Keep the champion unseen* | Temerach — *Shield the boy, unmask the house* | the presentation of entrants is where these two touch |
| Hanzo — *Field the champion* | Nerissa — *Keep the Lady's water clean* | the fouling alarm, and who is allowed to say so |
| Crowbill — *Keep the table level* | The Dragon Knights — *Hold the streets* | he cannot enforce a code against armoured men |

**None of these should be settled by GM preference.** Set the consequence links
now, roll them opposed when they touch, and let the board be what the dice made
it.
