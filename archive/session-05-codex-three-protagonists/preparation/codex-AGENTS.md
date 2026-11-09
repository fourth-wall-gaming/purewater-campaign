# RPG adventure preparation in this workspace

For any new or substantially rebuilt adventure, including another campaign or
game system, read `docs/scenarios/adventure-construction-method.md` before
preparing the selected premise. Use `docs/scenarios/brainstorming-method.md`
for proposals and `docs/scenarios/consequence-driven-design.md` for operation
resolution and consequences. Player instructions take precedence.

After selection, briefly interview the player about their desired activities
and tone before deep preparation; reuse answers already given. Then build the
cast, adversarial plans, per-character knowledge,
three-act development and concrete playable situations before opening play.
Follow the method's readiness check; a pitch or a list of clocks is insufficient.
The method is system-independent; use the current game's actual mechanics and
persistence model. For Mythras, use its GM skill and TypeDB through the CLI.

## Mandatory antagonist actions and counteractions

Always prepare what each principal antagonist actually does to advance their
objective, and what they do in response to interference. Before opening an
adventure, save both an executable unopposed plan and a reaction matrix in the
story arc framework and live model. Each operation needs actors, target,
prerequisites, finite assets/costs, place, duration/earliest time, warning and
discovery routes, resolution, and success/failure/withdrawal consequences.
Reactions must specify what the antagonist learns, how and when the report
reaches them, what surviving assets permit the response, and which future
operations change or cease. Cover exposed secrecy, protected victims, lost
resources or followers, official intervention, and early defeat. Never replace
this with motives, a generic escalation clock, or a villain waiting for the PC.
Attempt deadlines are not guaranteed outcomes. Revise the plan after actual
play; losses, surrender and effective early victories must remain effective.

During an OOC design review, hold play and the world clock. Incorporate feedback
into both documents and the live model before resuming. Do not turn GM review
or future possibilities into character knowledge or events that already happened.
Offer a spoiler walkthrough when requested; otherwise preserve discoveries.

# Independent PC clocks

For NPC personalities use `docs/scenarios/npc-behaviour-model.md` alongside
the engine character scores. Model behavioural traits, not psychiatric diagnoses
as moral categories. For Purewater read `docs/scenarios/purewater-tone.md`.


The installed Mythras engine supports native storyline clocks. All gameplay
CLI calls must select `--pc CHARACTER_ID` or `--storyline NAME/ID`; use
`list-storylines` to read the saved scene and local time. Use `--storyline world`
only for explicit shared world administration. Never rewind the campaign to
switch PCs, and do not use legacy `extras.thread_clock` as the authoritative
clock. Spell expiry, rest and prepaid lodging use the selected party's clock.
See `docs/engine/storyline-clocks/README.md` and its command guide for mappings,
migration evidence and grouping/splitting commands. Hold play during clock or
scenario design reviews; switching storylines does not grant rest or knowledge.
