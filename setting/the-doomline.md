---
arc: Purewater -- the doomline
campaign: myth-campaign-44abede1efbf
note: 'This front matter IS the schedule. Rewrite it, then run `sync-arc --file setting/the-doomline.md`
  to reconcile the graph: entries are created or updated, entries you delete are cancelled, and anything
  already played or narrated is left alone. The prose below is the same arc written for a human -- edit
  both in the one pass.'
thread:
- id: myth-beat-25961a354ace
  when: d0/night
  title: Santo's third errand
  agenda: myth-agenda-584bbb809405
  at: myth-loc-02141eddf75b
  cast:
  - myth-char-981b1b011ac7
  onscreen_if: A PC is on the Pearl after dark
  summary: One night left before the combat and he still has not got the sheet back. He pays somebody
    worse than Fennow, and he pays too much, which is how people get remembered.
- id: myth-beat-7e2f7007b3fa
  when: d1/dawn
  title: A price on the face
  agenda: myth-agenda-43fb5d3c4f30
  at: myth-loc-d39950294ef9
  cast:
  - myth-char-bfd8e78eb24f
  onscreen_if: The whole city has the description by the next dawn
  summary: Dragon-gold offered on the street for a man with the dead heir's face
- id: myth-beat-042d8fcdb075
  when: d1/dawn
  title: The stairs stop
  agenda: myth-agenda-38522f402dc9
  at: myth-loc-e2ae6d850b05
  cast:
  - myth-char-a505c427515b
  onscreen_if: Any PC on the Shoals, the Pearl, or anywhere goods move -- which by mid-morning is everywhere
  summary: The water-stairs stop -- IF 'Make them pay for one of ours' has reached 4. It stands at 2.
- id: myth-beat-12921d0f696c
  when: d1/day
  title: Conall follows the money to its house
  agenda: myth-agenda-548bb979a9ab
  at: myth-loc-effa8ec8c83d
  cast:
  - myth-char-6d2291950d63
  onscreen_if: A PC is in the Merchant's Quarter
  summary: He has the banking house. Next he wants the name on the other end of the credit -- which is
    the Movement, though he has no word for it yet.
- id: myth-beat-4ff01ad055cf
  when: d1/dusk
  title: 'PIVOT (F): the Archery -- and what Temerach does with winning it'
  agenda: myth-agenda-60d66b181533
  at: myth-loc-409cf49a6a95
  cast:
  - myth-char-4bcd7153d73c
  - myth-char-d142079adee8
  - myth-char-d5d19b6fcd63
  onscreen_if: A PC is at the Archery
  summary: 'Four thousand witnesses, the Governor in the stand, and the one person in Purewater with standing
    enough to make a baron answer. Canonically she does NOT spend it: all she holds is a boy''s knife,
    which accuses a son. She will not burn thirty years to have a father say ''my son is wild'' and be
    believed.'
  branches:
    wins-and-spends-it:
      thwarts:
      - myth-agenda-957017a6f62e
    wins-and-holds-it: {}
    loses: {}
- id: myth-beat-7059471ea1ef
  when: d1/dusk
  title: The Order's alarm is stood down again
  agenda: myth-agenda-605af58e242b
  at: myth-loc-620ee1d17332
  cast:
  - myth-char-5eb88c4a324b
  - myth-char-bc0e03fbbd4b
  onscreen_if: A PC is on Temple Isle
  summary: Nerissa asks for the water to be named publicly before the Combat. Lilura refuses -- a faith
    whose goddess has gone quiet cannot afford to be wrong in front of the city. The third refusal in
    two years.
- id: myth-beat-47d4b5a07169
  when: d1/night
  title: 'PIVOT (C): Santo comes for the knife himself'
  agenda: myth-agenda-584bbb809405
  at: myth-loc-02141eddf75b
  cast:
  - myth-char-8d55d2eb9316
  - myth-char-981b1b011ac7
  onscreen_if: The party has baited him with the knife and he has run out of hirelings
  summary: Three failed errands and one night left. If the bait is set well he stops paying strangers
    and comes himself -- off the barge, past his father's man, onto ground he does not own.
  branches:
    captured:
      activates:
      - myth-beat-8370bf7c2188
      thwarts:
      - myth-agenda-584bbb809405
    escapes:
      advances:
      - myth-agenda-584bbb809405:2
    never-comes: {}
- id: myth-beat-db3072f04ee2
  when: d1/night
  title: The last reinforcement
  agenda: myth-agenda-957017a6f62e
  onscreen_if: A PC is aboard the DragonBarge
  summary: The night before the sand, the Baron tops the working up himself. Deeper than the daily rite,
    because tomorrow it has to hold through a fight and then let go on command.
- id: myth-beat-5a74248a934d
  when: d2/dawn
  title: Cailan is walked to the lists
  agenda: myth-agenda-957017a6f62e
  at: myth-loc-409cf49a6a95
  cast:
  - myth-char-bfd8e78eb24f
  - myth-char-bed406244ae9
  - myth-char-4bcd7153d73c
  onscreen_if: A PC is at the lists on the morning of the Single Combat
  summary: The only time the champion leaves that ship. In harness, deck cleared, and in the open for
    the length of a walk.
- id: myth-beat-7698d0669426
  when: d2/dawn
  title: Nus lifts the binding locket
  agenda: myth-agenda-0d0688a76b9a
  at: myth-loc-409cf49a6a95
  cast:
  - myth-char-4bcd7153d73c
  - myth-char-ffe75ff9dced
  onscreen_if: Any PC at the lists, or whoever put Nus up to it. NOBODY HAS. Unless a PC points him at
    the Baron before the lists fill, he robs someone safer and this is cancelled.
  summary: In the crush at the lists on the morning of the Single Combat, the pickpocket takes the locket
    off the Baron himself
- id: myth-beat-8de5c9af7c97
  when: d2/day
  title: 'PIVOT (G): the Single Combat -- Thuban fights in a boy''s body'
  agenda: myth-agenda-bde16a325a45
  at: myth-loc-620ee1d17332
  cast:
  - myth-char-bed406244ae9
  - myth-char-4bcd7153d73c
  - myth-char-e3e7b15fd5a4
  onscreen_if: The Tourney is public; the party will be there unless something extraordinary prevents
    it
  summary: Cailan fights the Single Combat masked and armoured, and wins it, because there is a dragon-knight
    in him
  branches:
    champion-wins:
      activates:
      - myth-beat-c5e2d6d42e63
    champion-loses:
      cancels:
      - myth-beat-c5e2d6d42e63
      - myth-beat-10b0508be90b
      thwarts:
      - myth-agenda-bde16a325a45
    combat-does-not-happen:
      cancels:
      - myth-beat-c5e2d6d42e63
      - myth-beat-10b0508be90b
- id: myth-beat-c5e2d6d42e63
  when: d2/dusk
  title: The private audience
  agenda: myth-agenda-bde16a325a45
  at: myth-loc-620ee1d17332
  cast:
  - myth-char-bed406244ae9
  - myth-char-4bcd7153d73c
  - myth-char-d142079adee8
  - myth-char-e3e7b15fd5a4
  onscreen_if: Any PC who has got themselves inside the Governor's enclosure, or who stops the combat
    before it is won
  summary: The Single Combat champion is presented alone to Prince Emeric in the old rite -- and Hanzo
    moves Thuban out of a worn-out boy and into the Crown's own nephew
- id: myth-beat-10b0508be90b
  when: d2/night
  title: 'THE DOOM: the Prince is seated, and the boy is tidied'
  agenda: myth-agenda-bde16a325a45
  at: myth-loc-409cf49a6a95
  cast:
  - myth-char-bfd8e78eb24f
  - myth-char-bed406244ae9
  - myth-char-4bcd7153d73c
  - myth-char-d142079adee8
  onscreen_if: Anyone who got through that door first
  summary: 'TERMINAL. Behind the closed door the working is done: Thuban is drawn out of a spent boy and
    seated in Prince Emeric. The Crown''s man in Purewater becomes the Baron''s. And the emptied seventeen-year-old,
    who is now only evidence, is a loose end in a house that has begun tidying.'
- id: myth-beat-63841780f428
  when: d2/night
  title: Tat counts the cost
  agenda: myth-agenda-05c91c16b97f
  at: myth-loc-610195a74035
  cast:
  - myth-char-6764a1c4166f
  onscreen_if: Only visible to a PC who has been cultivating him
  summary: The mercenary captain starts pricing what the Baron's private business will cost his company
- id: myth-beat-bf3a563f97fd
  when: d2/night
  title: 'The purge: a body on display'
  agenda: myth-agenda-0d0688a76b9a
  at: myth-loc-d39950294ef9
  cast:
  - myth-char-bfd8e78eb24f
  - myth-char-ffe75ff9dced
  onscreen_if: A PC is in the city that night
  summary: With the Prince in hand the household stops being careful. Anyone who has handled the Baron's
    property is collected. Nus, who has been telling people he could get in there, is taken and displayed.
- id: myth-beat-1b290ef4d050
  when: d3/day
  title: The Governor's first act
  agenda: myth-agenda-4d7f2706dbfd
  at: myth-loc-409cf49a6a95
  cast:
  - myth-char-4bcd7153d73c
  - myth-char-5eb88c4a324b
  - myth-char-d142079adee8
  onscreen_if: A PC is at the Governor's court
  summary: 'AFTERMATH. The Crown''s man in Purewater signs what he is given: the Order''s alarm about
    the water is formally set aside as superstition, and the Pearl is ordered open. Nerissa is right,
    on the record, and has no standing left to be right with.'
- when: d1/night
  title: Orrin leaves the hatch unlatched again
  agenda: myth-agenda-961860091bbf
  at: myth-loc-610195a74035
  cast:
  - myth-char-9a2814a45c5e
  - myth-char-e3e7b15fd5a4
  onscreen_if: Anyone who has been down there once and was not reported
  summary: He has kept a boy alive for ten years by never once doing anything that could be noticed. Having
    done one thing, he does it again.
  id: myth-beat-4842ac0f8405
---
# The Doomline

**This is not the plot. It is the default.** Every beat in it is an *attempt*,
and attempts are rolled. It exists so the living world is cheap to run:
simulating twenty agendas every watch turns a session into administration,
whereas writing down what happens if nobody interferes — once — means play only
has to record what *changes*.

It is rendered live from the graph by `forecast --campaign <id>`, and it goes
stale on purpose. `revise-beat` and `cascade` are how it keeps up.

> A doomline that survives contact with the players unchanged was never a
> doomline. It was a rail.

---

## Movement I — the murder (d-3 to d-2)

The Baron's column enters Purewater with a covered litter in the middle of it
that the outriders let nobody near. Three Dragon Knights hold the gate bridge
and take a toll they are not entitled to. **Randall is greeted at the gate as
"Lord Santo"** by a knight who has never met either of them, and starts keeping
his head down. Conall arrives with Temerach and begins doing the only thing he
knows how to do: asking, in order, of everyone, and writing it down.

That evening **Santo offers to buy Emmeralda's contract** and Constantine
refuses him. He takes a room anyway. In the night he attempts the working from
his father's scroll — **and fails it.** With a girl on the floor, a channel half
opened in her and no way to finish or stop, he uses the knife.

**Blau collects him.** He waits at the bottom of the back stair with a folded
cloth, puts it over the boy, walks him out the back and holds the door. *He
never goes up.* That is why a knife, a crested coat and a spent scroll sit in
that room for two days.

Emmeralda dies an hour before dawn. Hesper takes Randall off the street
believing him the killer; Marisette's people take Conall for the same reason.
**The Pearl goes dark** — four hundred people out of work on one woman's word.

## Movement II — the meeting (d-2)

In the Catacombs, Marisette works out that neither boy did it and lets them go.
**Conall and Randall discover they are twins.** Gardwen's brother is spoken of
aloud for the first time. Conall goes back to the room and finds **the knife and
the coat — but not the scroll under the rug**, because nobody tells him to lift
the rug.

Gardwen and Magda go and look at the barge. Spirit Sight shows the light of the
thing in the hold and gives her a *feeling* about her brother and nothing more.
Dragon Knights move them on; Magda puts one of them down; and word gets round
about an old woman with a face like a spade.

Conall goes disguised to Temerach and gives her the knife.

> **This is where our play diverged, and it is the whole difference.**
> In our telling Gardwen found the **scroll** — the father's hand, not the
> son's knife — and had it read by a sorcerer. The doomline runs on a knife,
> which accuses a *son*. Everything downstream follows from which object
> somebody is holding.

## Movement III — the week (d-1 to d1)

**The presentation of the entrants.** Every competitor bare-headed for the space
of a bow. The helm comes off the Baron's champion and it is a thin boy with
dragon-scale growing out of his throat. Canonically Gardwen sees it from the
crowd, at distance, with nobody beside her — and has no standing to do anything
about it.

Santo, who cannot go ashore, starts paying strangers off the Hatter's stair to
get his father's sheet back. He is refused, robbed, and refused again. **The
household hears there is a second Santo-face asking questions in the Merchant's
Quarter** and puts a price on finding out whose it is.

Marda Blackwater's dredgers stop the water-stairs — no cartage, no
provisioning, no competitors' gear moved — which turns a labour dispute into a
sacred crisis four days before the Lady's own tournament.

**The Archery, and the shot Temerach does not take.** Four thousand witnesses,
the Governor in the stand, and the one person in this city with standing enough
to make a baron stand still and answer. She does not spend it. All she holds is
a boy's knife, and she will not burn thirty years to have a father say *my son
is wild* and be believed.

**The Order's alarm is stood down again.** Nerissa asks for the water to be
named publicly before the Combat; Lilura refuses, because a faith whose goddess
has gone silent cannot afford to be publicly wrong. The third refusal in two
years.

That night the Baron tops up the working himself, deeper than the daily rite,
because tomorrow it must hold through a fight and then let go on command.

## Movement IV — the sand (d2)

Cailan is walked to the lists. It is the only time he leaves that ship.

He wins, because what is in him has been winning fights since before this city
had walls.

**The private audience.** By a form older than the Governor's office, the
champion is presented **alone and unarmed** to the Crown's representative,
immediately after the bout, behind a closed door. It is ceremony rather than
politics, which is exactly why nobody has ever thought to guard it. Four
generations of that family have been buying their way toward a private room
with that boy in it.

Behind the door: **Draw Forth** on Cailan, **Seat the Bound** on Prince Emeric.

## THE DOOM (d2/night)

The Crown's man in Purewater becomes the Baron's.

And the emptied seventeen-year-old, who is now nothing but evidence, is a loose
end in a house that has already started tidying. **Gardwen's brother is a body
nobody will ever be shown.** With the Prince in hand the household stops being
careful at all: anyone who has handled the Baron's property is collected, and
Nus — who has spent a fortnight telling people he could get in there — is taken
and displayed.

## Aftermath (d3)

**The Governor's first act.** The Order's alarm about the water is formally set
aside as superstition and the Pearl is ordered open. Nerissa is right, on the
record, with no standing left to be right with.

**The Movement moves on.** The method works on a Crown officer. The credit line
is renewed and the next city is chosen. Hanzo was never the top of this.

---

## How to use it

- `forecast --campaign <id>` renders it live, in time order, with staging.
- `tick` reports **silent agendas** — live wants with nothing scheduled. Those
  are holes in the thread; a character with no next move stops existing.
- When the party interferes, **roll it, then `revise-beat` what no longer
  follows and `cascade`.** Do not re-author the whole line.
- Every beat says who holds it, so a deviation can be traced to whose plan just
  broke.

## The three hinges

Each of these is a single point where the doomline stops being inevitable:

1. **Which object reaches somebody with standing.** The knife accuses a son.
   The scroll accuses the house. Temerach spends thirty years of standing for
   one of those and not the other.
2. **The locket.** Nerissa's ruling: water puts the working out, and it does not
   matter at all while the anchor is on the Baron's body.
3. **The closed door.** A room with no guards on it has no guards on it for
   anybody. The Baron spent four generations engineering a private room; he is
   not the only person who can walk into it.
