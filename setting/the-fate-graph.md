# The Fate Graph — Purewater

Replaces the linear doomline. Same job, better shape: **nodes, not a line.**

Each node says what the situation is, who has to be *present* for which outcomes
to exist at all, what gets rolled, and which node each result leads to. The
graph is not a script — it is the set of places the story can be, and the edges
between them are dice.

## How a node works

```
NODE  T1.1 — a short name
WHEN  d-3/night                     the clock position, if fixed
ENTRY from T1.0 (automatic)         what leads here
PRESENCE                            WHO IS THERE CHANGES WHAT CAN HAPPEN
  nobody      → the default outcome, which is usually the worst one
  Gardwen     → unlocks an outcome that does not otherwise exist
  Magda       → unlocks a different one
ROLL  the check, the grade, and what each level means
EXITS → T1.2a / T1.2b, with the flag each one sets
TAKES what this node costs whoever walks through it
```

**The default outcome is what happens with no PC present**, and it is generally
the worst available. That is the whole engine: the party changes outcomes by
*being somewhere*, and cannot be everywhere.

## State flags

Flags are the graph's memory. They are set by outcomes and read by later nodes.
Keep them few and blunt.

| flag | values |
|---|---|
| `EM` | `alive` · `dead` |
| `SANTO` | `free` · `held` · `dead` · `disgraced` |
| `BLAMED` | `randall` · `conall` · `santo` · `nobody` |
| `EVIDENCE` | who physically holds the knife, the scroll, neither, both |
| `HOUSE` | `clean` · `complicit` — has the Baron's household covered for Santo *yet* |
| `WATCH` | `ordered` · `cracking` · `turned` |
| `KNIGHTS` | rung 1–5 on the escalation ladder |
| `LOCKET` | `worn` · `taken` · `lost` |
| `BONES` | `unknown` · `located` |

## Two rules that sit above the graph

> **Every act takes something** — a person, a place, a standing, a route, and it
> does not come back. A stretch of play in which the party only gains has not
> happened.

> **Most people say no the first time.** An ally is a scene, not a conversation.

---

# ACT I — ARRIVAL

Three openings, played in parallel, cutting between them. **Every player reads
their own sheet and backstory before the first line is narrated** — the PCs know
who they are even when they know nothing about Purewater.

## NODE A0 — The ford *(Gardwen, Magda)*
**WHEN** `d-3/dawn`

Gardwen has followed a di Teufel column for three weeks and is stuck in the
tourney queue behind it, watching the last of the dragon-scale go up the road —
with a covered litter in the middle that the outriders will not let anyone near.
Three places back, an old woman leaning on a staff is looking at her.

Magda has dreamed the same dream eleven nights. She knows this face.

**ROLL** none. This is a meeting.
**EXITS** → **A3** (the gate)
**TAKES** nothing. This is the one node that gives.

## NODE A1 — "Lord Santo" *(Randall)*
**WHEN** `d-3/day`

Randall is working the Tourney crowd at the gate bridge when a Dragon Knight
takes his arm, calls him **my lord**, and puts a hand out to help him down off a
cart he was in the middle of robbing.

**PRESENCE**
- Randall alone → he plays along or bolts; either way somebody in scale now has
  a face in their memory.

**ROLL** Deceit (Standard) to play it, or Stealth (Hard) to be gone.
- *critical* → he gets a name out of the knight before he goes. `KNIGHT_NAMED`
- *success* → clean away, but he has been **looked at**
- *failure* → he is walked twenty yards toward the column before he gets loose
- *fumble* → he is put in front of somebody who knows what Santo looks like
  close up, and has to talk his way out of it

**EXITS** → **A3**
**TAKES** Randall's ability to move through this city unnoticed. From here his
face is a liability and he knows it.

## NODE A2 — The road, and the joke *(Conall, Temerach)*
**WHEN** `d-3/day`

Four knights on the Anminster road, bored, a day out. They stop a King's officer
in plain armour with no house on her shield **because she is an elf and because
they can** — not violence, just the long, slow, public humiliation of a woman who
outranks them and cannot use it.

**PRESENCE**
- Temerach alone → she takes it. Absolutely still, and does not answer.
- **Conall present** → he watches her take it, which is the point of the node.

**ROLL** Conall's **Willpower (Hard)** not to intervene. She has told him not to.
- *success* → he stands there. It costs him and it teaches him what she is.
- *failure* → he speaks, and it gets worse, and she has to get him out of it —
  `KNIGHTS` → rung 2 immediately, and they remember his face too.

**EXITS** → **A3**
**TAKES** Conall's belief that a warrant means anything out here.

## NODE A3 — The gate toll *(any)*
**WHEN** `d-3/day`

Three Dragon Knights hold the gate bridge and take a toll they have no right to.
The watch stands twenty feet away and looks at the water. **Sergeant Abel Weir
writes it in a book.**

**PRESENCE**
- anybody with money → they pay, and watch somebody who has none be turned back
- anybody *without* → the scene is theirs

**ROLL** whatever they try. Failure is *turned back*, not captured.
**EXITS** → free play in the city; **A4** is always available
**TAKES** a coin, or a piece of somebody's dignity in front of them.

## NODE A4 — Sergeant Weir's book *(any, any time from here)*
Available for the whole adventure. Anybody who talks to the watchman with the
four-inch book has opened the **WATCH** thread. `WATCH` → `cracking` the first
time a PC asks him what he is writing.

---

# THREAD 1 — SANTO

> **Santo's escapade is entirely his own.** Blau is not there and would never
> have permitted it. There is a young man, a knife, and a scroll he is not good
> enough to use. The household's guilt begins *afterwards*, as a decision.

## NODE T1.1 — The room at the Sylph's Embrace ★ **the hinge of the whole act**
**WHEN** `d-3/night`
**ENTRY** automatic

Santo has been refused. He has taken a room anyway, with a girl, a scroll in his
father's hand he has read four times, and a barbed knife he has been told is
necessary. He is nineteen and he is about to find out he cannot do this.

**PRESENCE — this is the entire node**

| who is there | what becomes possible |
|---|---|
| **nobody** | `EM=dead`, `SANTO=free`. The default, and the worst. |
| **Gardwen** | The wound is a ritual cut that will not close on its own. Piety, **Formidable** — the channel reopens from the inside as fast as it is healed unless the *working* is broken first. **`EM=alive` is only reachable here.** |
| **Magda** | Santo is nineteen, panicking, and holding a knife. Combat. `SANTO=held` or `SANTO=dead` become reachable. |
| **Randall** | He is in this house and knows every back stair. He can get people *out* — or be found standing over it. |
| **Conall** | Arrives after, with a warrant and an eye. `EVIDENCE` is cleanest on this branch. |

**ROLLS**
- Gardwen: **Piety (Formidable)** to hold the wound closed, or Spirit Sight
  (Standard) first to see *why* it will not close — which drops the heal to Hard.
- Magda: Combat Style vs a panicking fire-caster. He will use fire in an
  enclosed wooden house.
- Anybody: Perception (Standard) in the room afterwards finds the chalk.

**EXITS**
- `EM=dead`, `SANTO=free` → **T1.2** (the catacombs), `BLAMED=randall`
- `EM=alive`, `SANTO=free` → **T1.2**, but Marisette does not close the Pearl —
  she waits for him to come back for what is his
- `SANTO=held` → **T1.2**, `BLAMED=santo`, and the house must respond → `HOUSE`
  decision happens *early*
- `SANTO=dead` → the whole graph tilts: no Santo thread, and a baron with a dead
  son and a reason

**TAKES** Emmeralda, in most branches. In the rest, it takes the party's
anonymity — somebody was *there*.

## NODE T1.2 — The catacombs ★ **both twins, and the question**
**WHEN** `d-2/dawn`
**ENTRY** from T1.1 on any branch

Marisette's people take whoever wears that face. On the branch where Santo was
caught they take him too, and it is worse. Two men with the same face, tied to
chairs, in the dark, under a city.

**This is the node where everybody finds out what the di Teufel family is.** The
twins see each other. Somebody says the word *brother*. Somebody works out that
the face they have all been describing belongs to a third man.

**ROLL** Marisette's **Insight (Standard)** to believe them — or the party's own
account, if any PC was present at T1.1 and can say what they saw.
- Any PC witness → automatic. She believes a witness over a face.
- No witness → Insight, and a failure means hours in the dark first.

**EXITS** → **T1.3**. Sets `BLAMED` definitively. Opens **Marisette** and
**Crowbill** as approachable for the first time.
**TAKES** the twins' idea of who they are. Neither of them gets that back.

## NODE T1.3 — The room, afterwards
**WHEN** `d-2/day`
**ENTRY** from T1.2

The upstairs room, before or after somebody else gets to it. What is in it:
**the barbed Asmodeus knife** behind the armoire, **a spent scroll in Baron Hanzo
di Teufel's own hand**, an unfinished **chalk seat** under the rug, and a coat
with the di Teufel crest under the collar.

Damning, and — this is the important part — **embarrassing**. It does not say
*the Baron is a monster*. It says *the Baron's son is an incompetent who could
not finish his father's working and panicked.* That is a thing a great house will
pay, threaten and kill to keep quiet, and it is not the same thing as a
conspiracy.

**ROLL** Perception (Standard) for the knife and the coat. **The scroll is under
the rug and needs somebody to lift the rug** — Perception (Hard), or anybody who
thinks to look at the floor. Conall, or any reader, gets the hand.

**EXITS** → **T1.4**, and sets `EVIDENCE`.
- If the party lifts the rug: `EVIDENCE=both` — they have the *father*.
- If not: `EVIDENCE=knife` — they have the *son*, and a knife accuses a boy.

**TAKES** nothing yet. This is the node that arms everything downstream, and it
is the single highest-leverage search in the adventure.

## NODE T1.4 — Santo comes back ★ **the first real violence**
**WHEN** `d-2/dusk`
**ENTRY** from T1.3, or automatically if 24 hours pass

He cannot report the loss to his father. So he pays **three Dragon Knights** out
of his own pocket to walk him to the green door, and he stands in a public street
in daylight and demands what is his.

Constantine refuses him at her own door.

He is nineteen, humiliated in front of hired men, and he **uses fire on an
inhabited wooden building in a crowded street.**

**PRESENCE**
- nobody → the house burns in part, somebody inside dies, `KNIGHTS` → 3
- any PC → a genuine fight: three armoured professionals and a panicking caster,
  in a street full of people who cannot get away
- Gardwen → the fire and the wounded are hers to deal with, and she cannot do
  both that and fight
- Magda → she can reach him. She is the only one who can.

**ROLL** combat, properly. **The knights fight in threes and a PC who takes one
alone should lose.** Fire spreads: a d6 clock on the building.

**AND THEN BLAU.** Whatever is happening, it stops, because a thin white man
walks into the middle of it with empty hands and takes Santo away — publicly,
with one hand flat between his shoulder blades, in front of thirty witnesses.

**That is the moment `HOUSE` becomes `complicit`.** Up to here the family had a
disgraceful son. From here they have *covered for him*, and everyone on that
street saw it.

**EXITS** → **T1.5**
**TAKES** part of Constantine's house, and somebody in it. Non-negotiable: this
node costs a named person.

## NODE T1.5 — What the party does with it ★ **the fan-out**

They now hold some combination of a knife, a scroll, a witness, a burned street
and a dead girl. The graph opens.

| they go to | thread | what it needs | what it costs |
|---|---|---|---|
| **the watch** | `WATCH` | Abel Weir, and the standing order | he must not be the man who disobeyed |
| **the Assay** | `JURISDICTION` | Conall's warrant, which the order does not touch | it makes him the Baron's target |
| **the Harbour Masters** | `JURISDICTION` | maritime law — the Knights take boats | Deepkeel must be made to act, not refer |
| **the Order** | `WATER` | the fouling, and Nerissa | Lilura will not let the Order be wrong in public |
| **Marisette** | `PEARL` | evidence she can *use*, not just a name | she spends her boycott once |
| **Crowbill** | `CANALS` | straight dealing, and he fetches you at dawn | he asks for something you will not like |
| **Temerach** | `STANDING` | the scroll, not the knife | thirty years, spent in ninety seconds |
| **Santo himself** | `SANTO CORNERED` | finding him off the barge | he takes hold of whoever is nearest |
| **nobody** | the default | — | the graph advances without them |

**The gate on all of it:** with `EVIDENCE=knife` they are accusing a son and
every one of these doors is harder. With `EVIDENCE=both` they are accusing a
house, and Temerach in particular becomes reachable.

---

# THE BARON'S COUNTERS — triggered, not timed

Within one watch of the trigger, while the party is still in the room.

| trigger | counter |
|---|---|
| public questions about his money | a price on the face; men out by dawn to *name*, not take |
| they reach Santo | Blau moves him, and the messenger stops being findable |
| evidence reaches an official | **he accuses back** — unlicensed foreign sorcerer, a thief with a murderer's face, an Assay officer outside his warrant. The watch helps him *lawfully* |
| a hand on the champion | deeper reinforcement that night; the boy is moved |
| something taken off him | `KNIGHTS` +1 rung. Reprisals on people who cannot answer |
| the timetable threatened | a **deal**, warm and sincere, offered to whoever is most tired of losing |
| cornered | the warmth goes **up** |

---

# LATER THREADS — heads only

- **`WATER`** — the fouling, the Order, the three councillors, and the fact that
  the men who silenced the temple alarm are the men who wrote the watch's
  standing order.
- **`CHAMPION`** — the barge, the keeper, Thuban's terms, the Washing.
- **`MONEY`** — Hallow & Beck, the fire lit before four, and the discovery that
  cutting the credit line sends twenty-five knights home.
- **`SAND`** — the Single Combat, the shut room, **the standoff**, the shot, the
  flight.
- **`BONES`** — not this adventure.
