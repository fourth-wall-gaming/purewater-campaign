# Dramatic Structure and Evaluation: Design Notes

Player-led OOC review, 2026-11-06. Proposal, not implemented schema or engine
behaviour. Halla's game and world clock remain paused at d8/day minute350.
No proposed event is canon or character knowledge. Preserve actual victories.

## Problem and brief

The shared Purewater database contains 216 character records at audit time,
including other protagonists, creatures and older chapters. This offers scale,
not evidence of dramatic quality. The challenge is making play interesting,
dramatic and fun, rather than merely internally recorded.

The player found the rope investigation mildly interesting but low-stakes and
mostly routine. It did not advance the larger story. Do not declare all small
stories worthless: distinguish an enjoyable local episode from an incidental
errand. Everyday work should usually be compressed unless the player wants it.

Use the television analogy: a scene is a moment of play; an episode has a local
dramatic question; a season carries a larger conflict. Evaluate each level and
the coupling between them. Do not require every encounter to reveal a conspiracy.

## Proposed structural model

- Campaign: world, tone, player preferences and shared continuity.
- Arc: sustained conflict, contested stakes, principal actors and several
  possible resolutions, not an obligatory ending.
- Episode: a playable local problem with its own stakes, opposing objectives,
  entry opportunities, possible resolutions and consequences for its parent arc.
- Situation/scene: place, available actions, participants, knowledge boundaries,
  immediate pressure, discoverable evidence and a meaningful exit condition.
- Operation: an NPC's attempted change to the world. Actors, target, explicit
  prerequisites, committed resources, timing, warning routes and conditional
  outcomes. Can affect several scenes or episodes and happen off camera.
- Event: what actually occurred, including rolls, player choices and state deltas.
- Evaluation: a separately stored assessment referencing plans or actual events;
  never itself an in-world fact.

Use explicit membership and causal links, not name matching. Associate characters
with adventures by role and involvement interval. Distinguish entity existence,
current presence, planned participation and actual participation. Operations
must not teleport everyone in their cast to their target location.

Episode-to-arc links name the mechanism: changes resources, shifts allegiance,
reveals usable information, enables/prevents an operation, changes public
standing, or resolves a contested objective. Store expected links separately
from observed consequences. A plan is not proof that the player experienced it.

## Evaluation dimensions

Start with a small diagnostic profile, not a universal fun score. For each
dimension use 0 absent, 1 weak, 2 concrete, 3 strong, or unknown. Every rating
needs evidence and a short rationale. Separate pre-play prediction, post-play
GM assessment and direct player feedback; identify assessor and version.

| Dimension | Question |
| --- | --- |
| Local stake | What specific valued thing can change here? |
| Agency | Can the PC pursue materially different approaches with real effects? |
| Opposition | Does someone act towards an incompatible goal with credible means? |
| Uncertainty | Is an important outcome genuinely unresolved? |
| Discovery | Does new information change available action or understanding? |
| Consequence | Can this encounter leave a persistent change? |
| Character relevance | Does it engage this PC's abilities, commitments or relationships without contrivance? |
| Novelty | Does it offer a different activity or situation from recent play? |
| Local coherence | Does this episode have a comprehensible problem and resolution? |
| Arc coupling | Is there a specific causal connection to the wider conflict? |
| Payoff | Does it fulfil, complicate or resolve something actually established? |

These are not additive by default. Quiet family scenes can have low opposition
and high value. A strong local adventure can have weak arc coupling. Weighting
depends on player intent and scene purpose; any aggregate must expose weights.
Do not score personality disorders, gore, suffering or forced losses as quality.

## Pacing observations and alerts

Record player-visible meaningful choices, actionable discoveries and persistent
state changes, with event references. Track consecutive routine-only scenes,
repeated activities, outstanding dramatic questions and time since an antagonist
operation changed anything. Distinguish player-requested downtime from unwanted
inactivity. Raw dialogue length, dice count, NPC count and danger are not fun.

Initially use alerts rather than automatic escalation:

- Several scenes pass with no consequential choice, discovery or change.
- A scheduled operation is blocked but has no recorded reassessment.
- An episode has no local resolution or no stated relationship to its arc.
- A journal outcome is not reconciled with the operation it resolved.
- A reaction depends on information that has not reached its actor.

Response: compress, conclude a genuinely solved conflict, offer another prepared
situation, or revise future plans. Never invalidate success, invent retrospective
crimes, force an ambush, or make enemies omniscient to improve a score.

## Quiet War audit example

There are three antagonist agendas and nine saved beats. Four have resolved
statuses; five still read pending. The witnessed protection demand still reads
pending despite its messenger's detention. Its actual outcome lives in journal
entries. The beat cast links cover only Crowbill, Marr, Bren and Neri, omitting
important operational participants. Prerequisites, assets and reactions are
largely prose, including whole continuation documents repeated in beat content.

The rope case provided a solvable local task but little arc coupling. The safe
escort produced a real protective success. Repeated empty inspections and
stakeouts did not create a succession of new dramatic questions. Crowbill's
interception depended on a report from the detained messenger; that blockage
was valid, but the GM repeatedly presented inactive sites as consequential play.

No new numerical scores are claimed as player ratings. Use these examples to
calibrate a future rubric with the player, not to retroactively rewrite events.

## Proposed GM/engine contract

Author structured plans alongside prose. Validate participant IDs, causal links,
prerequisites, finite assets, knowledge routes and conditional outcomes before
opening an episode. Let the GM choose portrayal and fair adjudication.

At resolution, record attempted operation, actual outcome, rolls, resource and
knowledge deltas, affected beat statuses and changed future operations together.
Validate against the current version to avoid stale writes across sessions.
Keep an audit trail and support explicit corrections. This is a design target,
not a claim that the present CLI supplies transactional operation resolution.

Evaluate after a meaningful unit of play, then ask for occasional lightweight
player feedback. Inferred engagement is uncertain; direct feedback outranks it.
Evaluation should suggest reviews, never secretly determine dice or outcomes.

## Next engineering work

1. Trace source repo, installed plugin and executed local runtime versions.
2. Inventory current schema and commands against the proposed responsibilities.
3. Design a minimal episode/operation/evaluation representation with explicit
   adventure membership and links to existing facts and events.
4. Build validation and outcome reconciliation before automated scoring.
5. Test paused snapshots: successful early intervention, detained messenger,
   conflicting clocks, no-action downtime and a strong self-contained episode.
6. Calibrate the diagnostic dimensions on actual player feedback before deciding
   thresholds, weights or automated prompts.

No implementation, source-repo update, database migration or new chat is implied
by these notes. The game remains paused for the design discussion.
