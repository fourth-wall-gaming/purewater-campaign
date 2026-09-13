# Purewater — the fate graph

One file. Every pathway the story can take, and the dice that choose between
them. **Written and owned by the Gamesmaster**; the tools only ever read it.

## How to write a node

Write whatever prose you like. The parser recognises seven labels and ignores
everything else, so an unfinished node is just prose and still parses.

```
## NODE T9.1 · A short name
WHEN   d-1/night                  optional clock position
ENTRY  T9.0, T8.4                 what leads here ("start" for an opening)
TAKES  what this node costs       every node needs one

Any amount of prose. Describe the room. Argue with yourself. Leave a note
for later. None of it is parsed and none of it has to be tidy.

IF nobody
  -> T9.2   SETS DOOR=shut
IF Gardwen
  ROLL Piety (Hard) — and say why the grade is what it is
  -> T9.2   SETS DOOR=open
  -> END    she does not come back out
```

**`IF nobody` is the default branch** — what happens when the party is somewhere
else. Write it first and write it honestly; it is usually the worst outcome, and
it is the reason being present matters.

**Every node takes something.** The checker complains if one doesn't.

---

# ACT I — ARRIVAL

## NODE A0 · The ford
WHEN d-3/dawn
ENTRY start
TAKES nothing — the only node in the graph that purely gives

Gardwen has followed a di Teufel column for three weeks and is stuck in the
tourney queue behind it, watching the last of the dragon-scale go up the road.
There is a covered litter in the middle of them the outriders let nobody near.
Three places back, an old woman leaning on a staff is looking at her.

Magda has dreamed the same dream eleven nights and knows this face.

IF nobody
  -> A3
IF Gardwen
  -> A3   SETS MAGDA=met

## NODE A1 · "Lord Santo"
WHEN d-3/day
ENTRY start
TAKES Randall's ability to move through this city unnoticed

A Dragon Knight takes his arm at the gate bridge, calls him **my lord**, and
puts a hand out to help him down off a cart he is in the middle of robbing.

IF nobody
  -> A3   SETS FACE=noted
IF Randall
  ROLL Deceit (Standard) to play it, or Stealth (Hard) to be gone. A critical
  gets a name out of the knight first; a fumble puts him in front of somebody
  who knows what Santo looks like close up.
  -> A3   SETS FACE=noted
  -> A3   SETS FACE=noted KNIGHT=named

## NODE A2 · The road, and the joke
WHEN d-3/day
ENTRY start
TAKES Conall's belief that a warrant means anything out here

Four knights on the Anminster road, bored, a day out from the city. They stop a
King's officer in plain armour with no house on her shield **because she is an
elf and because they can**. Not violence. The long, slow, public humiliation of
somebody who outranks them and cannot use it.

She takes it. Absolutely still, and does not answer, and does not look at him.

IF nobody
  -> A3
IF Conall
  ROLL Willpower (Hard) not to intervene. She has told him not to.
  -> A3   SETS TEMERACH=seen
  -> A3   SETS TEMERACH=seen KNIGHTS=2 FACE=noted

## NODE A3 · The gate toll
WHEN d-3/day
ENTRY A0, A1, A2
TAKES a coin, or a piece of somebody's dignity in front of a crowd

Three Dragon Knights hold the gate bridge and take a toll they have no right to.
The watch stands twenty feet away and looks at the water. A heavy, tired sergeant
in blue-grey writes something in a four-inch book and closes it.

IF nobody
  -> A4
IF anyone
  ROLL whatever they try. Failure is *turned back*, not taken.
  -> A4
  -> A4   SETS KNIGHTS=2

## NODE A4 · Sergeant Weir's book
ENTRY A3
TAKES Weir's deniability, the moment anybody asks him what he is writing

Open for the whole adventure. Anybody who talks to the man with the book has
opened the watch thread.

IF nobody
  -> T1.1
IF anyone
  -> T1.1   SETS WATCH=cracking

---

# THREAD 1 — SANTO

> Santo's escapade is **entirely his own**. Blau is not there and would never
> have permitted it. A young man, a knife, and a scroll he is not good enough to
> use. The household's guilt begins afterwards, as a decision.

## NODE T1.1 · The room at the Sylph's Embrace
WHEN d-3/night
ENTRY A4
TAKES Emmeralda on most branches; on the rest, the party's anonymity

He has been refused. He has taken a room anyway, with a girl, a scroll in his
father's hand that he has read four times, and a barbed knife he has been told
is necessary. He is nineteen and about to discover he cannot do this.

The working fails. There is a channel half-opened in her and no way to finish
and no way to stop, and he uses the knife.

**This is the hinge of the act. Who is in the building decides what is possible.**

IF nobody
  -> T1.2   SETS EM=dead SANTO=free BLAMED=randall
IF Gardwen
  ROLL Spirit Sight (Standard) first shows *why* the wound will not close, which
  drops the heal from Formidable to Hard. Piety to hold it — the channel reopens
  from the inside as fast as it is healed until the working itself is broken.
  -> T1.2   SETS EM=alive SANTO=free
  -> T1.2   SETS EM=dead SANTO=free
IF Magda
  ROLL Combat Style against a panicking fire-caster in an enclosed wooden house.
  He will use fire. There are people asleep upstairs.
  -> T1.2   SETS SANTO=held BLAMED=santo
  -> T1.2   SETS SANTO=dead
IF Randall
  ROLL Locale (Easy) — he knows every back stair in this building and can get
  people out of it. Or be found standing over it.
  -> T1.2   SETS BLAMED=randall
  -> T1.2   SETS BLAMED=nobody
IF Conall
  ROLL Perception (Standard) arriving after, with a warrant and an eye.
  -> T1.2   SETS EVIDENCE=both

## NODE T1.2 · The catacombs
WHEN d-2/dawn
ENTRY T1.1
TAKES the twins' idea of who they are; neither gets that back

Marisette's people take whoever wears that face. Two men with the same face,
tied to chairs, in the dark, under a city — and on the branch where Santo was
caught, three.

**This is where everybody finds out what the di Teufel family is.** The twins
see each other. Somebody says the word *brother*. Somebody works out that the
face everyone has been describing belongs to a third man.

IF nobody
  ROLL Marisette's Insight (Standard) to believe them. Failure is hours in the
  dark first, and she is still right in the end.
  -> T1.3
IF anyone
  A PC who was in the building at T1.1 makes it automatic. She believes a
  witness over a face.
  -> T1.3   SETS MARISETTE=open

## NODE T1.3 · The room, afterwards
WHEN d-2/day
ENTRY T1.2
TAKES nothing yet — and that is why it is the most dangerous node to walk past

The barbed knife behind the armoire. A spent scroll in Baron Hanzo di Teufel's
own hand. An unfinished chalk seat under the rug. A coat with the crest under
the collar.

Damning, and — the part that matters — **embarrassing**. It does not say *the
Baron is a monster*. It says *the Baron's son is an incompetent who could not
finish his father's working and panicked*, which is a thing a great house will
pay, threaten and kill to keep quiet, and is not the same as a conspiracy.

**The scroll is under the rug.** Somebody has to think to look at the floor.

IF nobody
  -> T1.4   SETS EVIDENCE=none
IF anyone
  ROLL Perception (Standard) finds the knife and the coat. The scroll is
  Perception (Hard), or free to anyone who lifts the rug. A reader gets the hand.
  -> T1.4   SETS EVIDENCE=knife
  -> T1.4   SETS EVIDENCE=both

## NODE T1.4 · Santo comes back
WHEN d-2/dusk
ENTRY T1.3
TAKES part of Constantine's house, and a named person in it

He cannot report the loss to his father. So he pays **three Dragon Knights** out
of his own pocket, walks them to the green door in daylight, and demands what is
his. Constantine refuses him at her own step.

He is nineteen, humiliated in front of hired men, and he uses fire on an
inhabited wooden building in a crowded street.

**Then Blau.** Whatever is happening stops, because a thin white man walks into
the middle of it with empty hands and takes Santo away — publicly, one hand flat
between his shoulder blades, in front of thirty witnesses.

That is the moment the household stops having a disgraceful son and starts having
covered for one, and the whole street saw it.

IF nobody
  -> T1.5   SETS HOUSE=complicit KNIGHTS=3 PEARL=burned
IF anyone
  ROLL Combat, properly. Three armoured professionals fighting in a trio, plus a
  panicking caster, in a street full of people who cannot get away. A d6 clock on
  the fire. A PC who takes one knight alone should lose.
  -> T1.5   SETS HOUSE=complicit KNIGHTS=3
  -> T1.5   SETS HOUSE=complicit KNIGHTS=3 SANTO=held
IF Gardwen
  The fire and the wounded are hers, and she cannot do that and fight.
  -> T1.5   SETS HOUSE=complicit KNIGHTS=3 SAVED=some

## NODE T1.5 · What the party does with it
ENTRY T1.4
TAKES whatever the door they choose charges them — every one of them charges

They hold some combination of a knife, a scroll, a witness, a burned street and
a dead girl. The graph opens.

**The gate on all of it:** with `EVIDENCE=knife` they accuse a *son*, and every
door below is harder. With `EVIDENCE=both` they accuse a *house*.

IF nobody
  The default advances without them.
  -> END   the doomline runs: the sand, the shut room, the Prince
IF anyone
  -> W1    SETS DOOR=watch
  -> J1    SETS DOOR=jurisdiction
  -> P1    SETS DOOR=pearl
  -> C1    SETS DOOR=canals
  -> S1    SETS DOOR=santo

---

# THREAD HEADS — to be written

## NODE W1 · Abel Weir's book finds a hand
ENTRY T1.5
TAKES Weir's career, unless somebody else can be the one who disobeyed
IF nobody
  -> END   ninety watchmen do nothing for another week
IF anyone
  -> END   *(unwritten)*

## NODE J1 · The court his protection cannot reach
ENTRY T1.5
TAKES the protection of being nobody — a warrant used is a warrant noticed
IF nobody
  -> END   the standing order holds
IF anyone
  -> END   *(unwritten — Assay, maritime law, or the Lady's own ground)*

## NODE P1 · Marisette spends the boycott
ENTRY T1.5
TAKES four hundred people's wages, and she can only spend it once
IF nobody
  -> END   the Pearl stays dark and it buys nothing
IF anyone
  -> END   *(unwritten)*

## NODE C1 · Crowbill fetches you at dawn
ENTRY T1.5
TAKES something you will not like being asked for
IF nobody
  -> END   he goes on watching and decides you do not exist
IF anyone
  -> END   *(unwritten)*

## NODE S1 · Santo cornered
ENTRY T1.5
TAKES whoever is nearest him when he panics
IF nobody
  -> END   he is moved to the barge and out of reach
IF anyone
  -> END   *(unwritten — cornered, then the bargain)*
