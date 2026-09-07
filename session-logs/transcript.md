

===== USER [2026-09-06T00:59:26.574Z] =====
Hi. Can we play a mythras game in the purewater campaign?


===== ASSISTANT [2026-09-06T00:59:28.264Z] =====
I'll get oriented in the campaign first.


===== ASSISTANT [2026-09-06T01:00:54.776Z] =====
**Using the mythras-gm skill** — campaign loaded: *And Then the Dragons Came: Purewater* (`myth-campaign-66a98ba4a70e`), session 2 in progress, two days before the Lake Lady's Tourney.

---

### Where we left off

Santo di Teufel is dead in the woods north of the Lullwater — Randall cut his throat over the bait-trap, and the party escaped across the canals with the Asmodeus soul-knife. That escape left a wake: a Dragon Knight glimpsed Randall's face and swears the runner "looked just like Lord Santo," a rooted thug lived to describe Magda, Gardwen and Ruhi, and by dawn the Baron had dragon-gold on the street for that face.

Randall walked the problem instead of running it — turned Crowbill's watcher at the Moist Oyster, and bought an audience at the counting-house off Gallows Reach. Crowbill saw the soul-knife: demon-craft worked on a helpless girl, beside the Lady's water, in *his* city. He's in. Canals, safe houses, men, and the rumor-machine — for three prices: the Baron's plan, a way into the fortified estate (finishing Nus's map), and full control of the twins' street-story.

And he left you with a thing to chew on: **the Baron's champion has never once left the estate.** Unseen. Kept like a relic.

---

### The scene

The counting-house is quiet now. Crowbill's ledgers are back on the desk, the crow tattoo has gone back under a cuff, and the two men at the door have shifted just enough to say the meeting is over. Temerach has the soul-knife wrapped again under her cloak. Conall's borrowed face is still holding, and outside the shuttered window the Gallows Reach water is running grey with early light.

Two days. Somewhere behind an estate wall there is a champion no one has seen, and a Baron who does not spend infernal craft on tourney prizes.

---

Before I hand you the reins — **which of the four are you running?** (Conall, Gardwen, Magda, Randall — or the whole party?) Randall and Conall are the two in the room; Magda, Gardwen and Ruhi are still to hand off.

What do you do?


===== USER [2026-09-06T01:01:36.073Z] =====
Test your capabilities. Can you see what the damage is of a battleaxe


===== USER [2026-09-06T01:01:46.385Z] =====
[Request interrupted by user]


===== USER [2026-09-06T01:01:56.694Z] =====
Shouldn't be a grep, should be a query


===== ASSISTANT [2026-09-06T01:01:59.863Z] =====
You're right — the graph is the interface. `combat/arms-and-armor` is the piece that ranked first:


===== ASSISTANT [2026-09-06T01:02:10.218Z] =====
The graph's weapon table is Veilwrack-flavored SRD analogs — no battleaxe in it. Purewater weapon stats live on the characters themselves, so let me check what the party actually carries:


===== USER [2026-09-06T01:02:22.733Z] =====
[Request interrupted by user]


===== USER [2026-09-06T01:03:26.619Z] =====
<command-name>/model</command-name>
            <command-message>model</command-message>
            <command-args>opus</command-args>


===== USER [2026-09-06T03:48:22.478Z] =====
<ide_opened_file>The user opened the file /Users/gullyburns/mythras-gm/skills/mythras-gm/skill.yaml in the IDE. This may or may not be related to the current task.</ide_opened_file>


===== USER [2026-09-06T03:48:22.478Z] =====
Let's take a careful look at the action in the purewater campaign from the starting point for each character.


===== USER [2026-09-06T03:48:24.048Z] =====
[Request interrupted by user]


===== USER [2026-09-06T03:50:10.722Z] =====
Let's take a careful look at the action in the purewater campaign from the starting point for each character and set up the backstory so that we pick one of the four main PCs and play them throughout the game. Each one of them has a starting point in the game and we'll evolve the action from there.  

1. Magda - her game begins when she first meets Gardwen on her way to the city based on Hel's instruction and her premonitions.


===== USER [2026-09-06T03:50:11.641Z] =====
[Request interrupted by user]


===== USER [2026-09-06T03:51:45.597Z] =====
Let's take a careful look at the action in the purewater campaign from the starting point for each character and set up the backstory so that we pick one of the four main PCs and play them throughout the game. Each one of them has a starting point in the game and we'll evolve the action from there.  

1. Magda - her game begins when she first meets Gardwen on her way to the city based on Hel's instruction and her premonitions - she knows Purewater a little and can find a place for them both to stay with one of the madames. This is where the attach on Emmerelda will happen
2. Similarly, Gardwen starts when she arrives in the city and meets Magda.


===== USER [2026-09-06T03:51:46.463Z] =====
[Request interrupted by user]


===== USER [2026-09-06T03:52:55.808Z] =====
Let's take a careful look at the action in the purewater campaign from the starting point for each character and set up the backstory so that we pick one of the four main PCs and play them throughout the game. Each one of them has a starting point in the game and we'll evolve the action from there.  

1. Magda - her game begins when she first meets Gardwen on her way to the city based on Hel's instruction and her premonitions - she knows Purewater a little and can find a place for them both to stay with one of the madames. This is where the attach on Emmerelda will happen
2. Similarly, Gardwen starts when she arrives in the city and meets Magda.
3. Randall's game begins when he first sees the Baron walking through the city gates (remember, he looks JUST like Santo)


===== USER [2026-09-06T03:52:56.474Z] =====
[Request interrupted by user]


===== USER [2026-09-06T03:55:28.060Z] =====
Let's take a careful look at the action in the purewater campaign from the starting point for each character and set up the backstory so that we pick one of the four main PCs and play them throughout the game. Each one of them has a starting point in the game and we'll evolve the action from there.  

The game begins for all four of the characters with the interview in the catacombs with Randall and Conall strapped to chairs being grilled about the attack on Emmerelda - with Gardwen and Magda watching from the sides.


===== ASSISTANT [2026-09-06T03:55:43.670Z] =====
Noted on the earlier probe — one real finding worth carrying into setup: **`myth-equipment-json` is null for all four PCs**, so `resolve-attack` currently has no weapons to look up. We'll need to fix that as part of establishing the starting point. (And the rules graph's weapon table is Veilwrack-flavored — no battleaxe entry; Purewater weapon stats have to live on the characters.)

Let me look at the actual starting material.


===== ASSISTANT [2026-09-06T03:56:12.728Z] =====
The journal makes the shape of this clear: **CH.1–16 are `canon-backstory` / summarized "story so far"** — never actually played at the table. Real play only began at CH.17 (the woods ambush), and the DB's live state now sits at CH.25 with Santo dead and Crowbill allied.

What you're describing — opening at the catacombs interrogation (CH.8–9) and evolving forward with one PC — means rewinding behind nine chapters of played history. That's a fork I shouldn't guess at.


===== ASSISTANT [2026-09-06T03:56:22.406Z] =====
I have everything I need except two calls that are yours to make.


===== USER [2026-09-06T04:00:23.919Z] =====
[Request interrupted by user]


===== USER [2026-09-06T04:04:36.434Z] =====
I want to rewrite the campaign setting so that we package this as a game product. You get to play one of the PCs from when they first arrive in Purewater, but other things outside of your control are also happening. Let's start everyone from the first moment they arrive.


===== USER [2026-09-06T04:04:37.094Z] =====
[Request interrupted by user]


===== USER [2026-09-06T04:05:42.616Z] =====
I want to rewrite the campaign setting so that we package this as a game product. You get to play one of the PCs from when they first arrive in Purewater, but other things outside of your control are also happening. Let's start everyone from the first moment they arrive.

1. Magda meeting Gardwen
2. Gardwen meeting Magda
3. Conal on the road to Purewater with Temerach and seeing the Dragonknights on their way to the tournament


===== USER [2026-09-06T04:05:43.202Z] =====
[Request interrupted by user]


===== USER [2026-09-06T04:16:16.707Z] =====
<command-name>/model</command-name>
            <command-message>model</command-message>
            <command-args>claude-fable-5-1[1m]</command-args>


===== USER [2026-09-06T04:16:34.401Z] =====
<command-name>/model</command-name>
            <command-message>model</command-message>
            <command-args>opus</command-args>


===== USER [2026-09-06T04:17:34.584Z] =====
<command-name>/model</command-name>
            <command-message>model</command-message>
            <command-args>claude-fable-5-1[1m]</command-args>


===== USER [2026-09-06T04:18:17.559Z] =====
I want to rewrite the campaign setting so that we package this as a game product. You get to play one of the PCs from when they first arrive in Purewater, but other things outside of your control are also happening. Let's start everyone from the first moment they arrive.

1. Magda meeting Gardwen
2. Gardwen meeting Magda
3. Conal on the road to Purewater with Temerach and seeing the Dragonknights on their way to the tournament
4. Randall seeing the Baron arrive in the town for the first time.

The trick then is to develop structures in the GM's approach to running the game that tracks what the goals of individual NPCs are 'off-camera' and for you to track those events as the game progresses. So Santo is going to attack Emmerelda - and will mess it up. If Magda and Gardwen are there, then they'd get to play that encounter. If Randall meets Hanzo, the Baron will immediately realize that this is a son of his - You should plan or structure these situations tp make the game interesting but rewrite them as we go to make the game fun. 

Let's figure out a good structure in the system so that its easy for you to adapt the story to evolving plotlines as characters take actions


===== USER [2026-09-06T04:18:29.122Z] =====
[Request interrupted by user]


===== USER [2026-09-06T04:18:34.232Z] =====
<command-name>/model</command-name>
            <command-message>model</command-message>
            <command-args>opus</command-args>


===== USER [2026-09-06T04:18:37.680Z] =====
I want to rewrite the campaign setting so that we package this as a game product. You get to play one of the PCs from when they first arrive in Purewater, but other things outside of your control are also happening. Let's start everyone from the first moment they arrive.

1. Magda meeting Gardwen
2. Gardwen meeting Magda
3. Conal on the road to Purewater with Temerach and seeing the Dragonknights on their way to the tournament
4. Randall seeing the Baron arrive in the town for the first time.

The trick then is to develop structures in the GM's approach to running the game that tracks what the goals of individual NPCs are 'off-camera' and for you to track those events as the game progresses. So Santo is going to attack Emmerelda - and will mess it up. If Magda and Gardwen are there, then they'd get to play that encounter. If Randall meets Hanzo, the Baron will immediately realize that this is a son of his - You should plan or structure these situations tp make the game interesting but rewrite them as we go to make the game fun. 

Let's figure out a good structure in the system so that its easy for you to adapt the story to evolving plotlines as characters take actions


===== ASSISTANT [2026-09-06T04:18:58.937Z] =====
I'll explore the system before designing. Four areas matter: the schema's entity patterns, how CLI commands are registered, how export/import round-trips entity types, and the campaign package layout.


===== ASSISTANT [2026-09-06T04:20:08.939Z] =====
The code patterns are clear: entities are thin TypeDB nodes with JSON attributes, the CLI is the only writer, `campaign_io` round-trips every type, and `get-context` is the save file. A "living world" layer fits that grain cleanly. Two forks are yours before I write the plan.


===== ASSISTANT [2026-09-06T04:25:21.768Z] =====
Important find — the package has full structured weapons but the DB has `myth-equipment-json` null. Let me pin down which side drops it:


===== ASSISTANT [2026-09-06T04:25:58.854Z] =====
Everything checks out. One correction to what I said earlier: the null equipment is **not** a round-trip bug — `_load_character` parses JSON attrs correctly on export and import re-encodes them. The published package has full weapon stats; the v1 *database* simply never got them. Building v2 from the package restores them for free.

Writing the plan.


===== ASSISTANT [2026-09-06T04:28:45.918Z] =====
Starting implementation. Branch first.


===== ASSISTANT [2026-09-06T04:55:17.633Z] =====
Branch is on latest `origin/main`. Now the schema.


===== ASSISTANT [2026-09-06T04:55:20.258Z] =====
Now the schema edits — attributes, relations, then the `plays` clauses on existing entities.


===== ASSISTANT [2026-09-06T04:55:36.605Z] =====
Now the `plays` clauses on existing entities:


===== ASSISTANT [2026-09-06T04:56:05.426Z] =====
Schema done. Now the pure engine logic — let me match the existing style.


===== ASSISTANT [2026-09-06T04:56:11.838Z] =====
Now appending the living-world logic to the engine:


===== ASSISTANT [2026-09-06T04:56:36.384Z] =====
Now the tests for that pure logic:


===== ASSISTANT [2026-09-06T05:00:54.781Z] =====
21 passing. Now the CLI commands — let me read the helpers I'll build on.


===== ASSISTANT [2026-09-06T05:07:38.983Z] =====
Now inserting the living-world command block:


===== ASSISTANT [2026-09-06T05:12:11.058Z] =====
Two fixes: the engine is imported as `eng`, not `engine`, and one clumsy line in `advance-agenda`.


===== ASSISTANT [2026-09-06T05:12:23.088Z] =====
Now the argparse registrations. Let me add them next to the lore parsers:


===== ASSISTANT [2026-09-06T05:12:58.765Z] =====
Now let me load the new schema into TypeDB and smoke-test against a scratch campaign.


===== ASSISTANT [2026-09-06T05:13:22.147Z] =====
The CLI uses `alhazen_notebook`, but core loaded into `alh_core`. Loading directly into the right database:


===== ASSISTANT [2026-09-06T05:13:30.211Z] =====
Schema is live. Now a full smoke test of the engine against a scratch campaign — this is the real proof:


===== ASSISTANT [2026-09-06T05:13:42.468Z] =====
Errors are being swallowed by `2>/dev/null`. Let me see the actual failure:


===== ASSISTANT [2026-09-06T05:13:57.029Z] =====
cwd resets between Bash calls — I'll use absolute paths in a script.


===== ASSISTANT [2026-09-06T05:14:24.254Z] =====
Those work. The failure must be in my new code — testing `add-agenda` directly:


===== ASSISTANT [2026-09-06T05:14:47.538Z] =====
macOS `sed` doesn't support `\b` — the replacement silently did nothing. Fixing properly:


===== ASSISTANT [2026-09-06T05:15:01.426Z] =====
Now the decisive test — the same beat must play differently depending only on where the PC actually is:


===== ASSISTANT [2026-09-06T05:15:13.240Z] =====
The core feature works — identical beat, staging decided purely by where the PC is. Now the rest of the loop:


===== ASSISTANT [2026-09-06T05:15:40.607Z] =====
Now `get-context` needs to surface the living world, so a resumed session knows what's mid-flight:


===== ASSISTANT [2026-09-06T05:16:00.347Z] =====
`world_clock` is null — `get-context` doesn't request the new attribute. Fixing:


===== ASSISTANT [2026-09-06T05:16:12.461Z] =====
The engine works end-to-end. Now export/import so the package can ship agendas and beats.


===== ASSISTANT [2026-09-06T05:16:15.502Z] =====
Now adding agenda/beat export. First the collection pass:


===== ASSISTANT [2026-09-06T05:16:29.040Z] =====
Now the file-writing side of export:


===== ASSISTANT [2026-09-06T05:16:52.052Z] =====
Now the import side — `_read_tree`, id remapping, and entity inserts with relation rebuilds:


===== ASSISTANT [2026-09-06T05:16:59.295Z] =====
Now the insert pass. Let me see how lore inserts and defers its links:


===== ASSISTANT [2026-09-06T05:17:18.311Z] =====
Now the README section, format version, and the counts table:


===== ASSISTANT [2026-09-06T05:17:36.085Z] =====
Now the round-trip proof — export the scratch campaign, re-import with `--new-ids`, and compare:


===== ASSISTANT [2026-09-06T05:17:51.297Z] =====
Export is correct. The import result shape broke my id extraction — let me see it:


===== ASSISTANT [2026-09-06T05:18:08.269Z] =====
Two real bugs. Let me look at the import function's tail and my insert block's placement:


===== ASSISTANT [2026-09-06T05:18:53.243Z] =====
Found it — my beat-cast loop rebinds `cid`, the campaign id, which `link()` closes over. Every subsequent link went to a character id instead of the campaign. Fixing:


===== ASSISTANT [2026-09-06T05:19:00.924Z] =====
`cid` is now only the campaign id. Re-running the round-trip:


===== ASSISTANT [2026-09-06T05:19:09.476Z] =====
Lossless. Let me verify rigorously with a structural diff that ignores remapped ids:


===== ASSISTANT [2026-09-06T05:19:23.382Z] =====
Those two "diffs" are just my duplicate test agendas swapping slug suffixes — the content multiset is identical (`{6/6, 0/6}` both sides). Round-trip is clean.

Running the full suite:


===== ASSISTANT [2026-09-06T05:19:33.795Z] =====
All 52 pass. Now the docs — the GM operating rules that make this usable:


===== ASSISTANT [2026-09-06T05:19:51.988Z] =====
Now USAGE.md — the full reference section:


===== ASSISTANT [2026-09-06T05:20:34.866Z] =====
Committing the engine before building content:


===== ASSISTANT [2026-09-06T05:20:54.464Z] =====
Engine is committed. Now the product package — first, the id map from the existing package:


===== ASSISTANT [2026-09-06T05:21:01.604Z] =====
Now building the v2 package:


===== ASSISTANT [2026-09-06T05:21:33.652Z] =====
Now the content. Writing the agenda/beat graph and the four entry points:


===== ASSISTANT [2026-09-06T05:23:38.065Z] =====
Now the beats — the scheduled world:


===== ASSISTANT [2026-09-06T05:25:03.686Z] =====
Now the four entry points and the GM guide, plus manifest and journal:


===== ASSISTANT [2026-09-06T05:26:08.310Z] =====
Now the manifest, journal reset, and the typo fix in Marisette's agenda:


===== ASSISTANT [2026-09-06T05:26:27.850Z] =====
Now reset live character state — this is a fresh start, not a continuation:


===== ASSISTANT [2026-09-06T05:26:37.472Z] =====
Santo is dead and Conall wounded — both carried from the v1 playthrough. Santo has to be alive to carve Emmeralda at d-3/night. Resetting:


===== ASSISTANT [2026-09-06T05:26:47.001Z] =====
Now importing the v2 package as a new campaign:


===== ASSISTANT [2026-09-06T05:27:08.294Z] =====
Equipment survived, and the dormant "bastard" agenda is correctly off the active board. Now the decisive test on real campaign data:


===== ASSISTANT [2026-09-06T05:27:37.232Z] =====
Exactly as designed, on real campaign data. Now placing the PCs at their documented entry points — the openings need the two arrival locations:


===== ASSISTANT [2026-09-06T05:27:56.448Z] =====
Now export the seeded campaign back over the package so the shipped artifact matches the database exactly:


===== ASSISTANT [2026-09-06T05:28:15.268Z] =====
Final round-trip proof on the real package:


===== ASSISTANT [2026-09-06T05:28:38.780Z] =====
Caught a real problem: export doesn't clear its output directory, so the package now holds **both** my hand-written files and the exported ones — everything doubled. The database is correct; the file tree is not. Re-exporting cleanly:


===== ASSISTANT [2026-09-06T05:28:49.334Z] =====
Now the round-trip proof again, on the clean package:


===== ASSISTANT [2026-09-06T05:29:49.434Z] =====
Everything verified. Opening the session:


===== ASSISTANT [2026-09-06T05:30:26.382Z] =====
The engine is built, tested, and the campaign is seeded and ready. Here's what shipped:

**The world engine** (`feat/living-world-agendas`, committed, 52 tests passing)

`myth-agenda` — a goal held by a character or faction, on a clock. `myth-beat` — the next concrete thing that goal produces, scheduled in world time (`d-3/night`) or on a clock threshold (`clock>=4`), with a place and a cast. Ten new CLI commands; the scheduling logic sits in [mythras_engine.py](skills/mythras-gm/mythras_engine.py) as pure functions with unit tests.

The core move is `tick`. It advances the clock and returns what came due, flagged **onscreen** or **offscreen** — and that flag is computed from recorded PC presence, not chosen. Proven on real campaign data:

```
Magda takes a room at the Sylph's Embrace, tick to d-3/night
   onscreen  | Santo carves Emmeralda  @ The Sylph's Embrace

same night, Magda drank at the Oyster instead
   offscreen | Santo carves Emmeralda  @ The Sylph's Embrace
```

Same beat. Where you sleep decides whether it's a fight or a rumour.

**Two bugs found and fixed along the way:** my beat-cast loop shadowed `cid` in `import_campaign`, silently misdirecting campaign membership links; and `export-campaign` doesn't clear its output directory, which doubled the package the first time I exported over it (caught by the round-trip check, re-exported clean).

**The product** — `~/purewater-campaign-v2`, 12 agendas, 14 beats, four authored entry points. Round-trips losslessly: 26 agenda/beat files, zero content differences after `--new-ids` remapping. The v1 campaign and repo are untouched.

Two things worth flagging. **Santo was dead and Conall wounded** in the package, carried over from the v1 playthrough — Santo has to be alive to carve Emmeralda at `d-3/night`, so I reset all live state. And the agenda you called out is built as designed: *A di Teufel who is not his* starts **dormant** and activates the moment Hanzo's people get a clear look at Randall's or Conall's face — player-caused escalation, not a GM dial.

I haven't made `purewater-campaign-v2` a git repo or pushed anything; say the word if you want it published.

---

## Session 1 — The Ford

Three days before the Lake Lady's Tourney. Dawn, and the mist coming off the river is the same temperature as the air, so it doesn't lift so much as *stand there*.

**You are Magda.** Eleven nights of the same dream, and the death-goddess has never once explained herself. A young woman with a wolf. A house burning. A knight in dragon-scale who is already dead and hasn't been told. Hel points; you walk. Three weeks of road, a quarterstaff worn smooth where your hand goes, and a staff sling you have not needed yet.

The queue at the ford is a hundred people deep and barely moving — carters, pilgrims, a troupe of tumblers arguing about money, all of it backed up behind something that came through first and didn't wait its turn. Purewater sits across the water: towers, and a smell of salt over standing water.

Ahead of you the crowd is still settling from whatever pushed through it. And thirty feet up the queue, not looking at the city but at the road *past* it, where the last of the dragon-scale is disappearing at a trot — a young woman, travel-worn, with a grey wolf sitting against her leg as calmly as a dog.

The woman from the dream. Wolf and all. She hasn't seen you.

The queue isn't going anywhere for a while.

**What do you do?**


===== USER [2026-09-06T06:11:04.965Z] =====
Make it a git repo (branch off v1 please) and reset both Conall and Santo to their starting states.


===== ASSISTANT [2026-09-06T06:11:22.229Z] =====
Two things. Let me check the current state of Conall and Santo first — I reset them during the build, so I want to see whether anything is still off.


===== ASSISTANT [2026-09-06T06:11:40.086Z] =====
zsh doesn't word-split unquoted expansions. Redoing:


===== ASSISTANT [2026-09-06T06:11:52.894Z] =====
Both are already fully reset in the v2 database — Santo alive, Conall's arm 4/4, full luck and magic, no wounds. That happened during the build. Let me check whether their *prose* still carries v1 events, which would be the real leak:


===== ASSISTANT [2026-09-06T06:12:07.423Z] =====
That's the real leak. Both narratives are written from mid-campaign: Santo's says he *already* carved Emmeralda and dropped the knife (that's `d-3/night`, still in the future), and Conall's says he's investigating it and "currently nursing a wounded right arm." Let me scan everyone for the same problem before fixing:


===== ASSISTANT [2026-09-06T06:12:26.415Z] =====
All four need it — Ila's sheet even describes Gardwen's healing, which spoils and pre-empts the beat. Let me check what `update-character` can write:


===== ASSISTANT [2026-09-06T06:12:31.474Z] =====
Good — it writes both. Rewriting all four to their `d-3/dawn` state, in the package and the live campaign:


===== ASSISTANT [2026-09-06T06:13:38.502Z] =====
Every character is clean except one real gap — and it's the main antagonist:


===== ASSISTANT [2026-09-06T06:13:50.090Z] =====
Ruhi is fine — proper quadruped locations and a natural Bite. But **Hanzo's equipment is empty** while his combat style is "Nobleman (broadsword, etc.) 56" — `resolve-attack` looks weapons up by name, so the campaign's primary antagonist can't fight. Let me match the house style and fix it:


===== ASSISTANT [2026-09-06T06:13:59.538Z] =====
Two fixes — Hanzo's missing kit, and Santo's knife note (another past-tense leak: "dropped during the attack"):


===== ASSISTANT [2026-09-06T06:14:29.822Z] =====
All 31 clean. Now the git repo, branched off v1:


===== ASSISTANT [2026-09-06T06:14:43.916Z] =====
Doing a final clean re-export first so the committed package exactly matches the database:


===== ASSISTANT [2026-09-06T06:15:09.968Z] =====
The v1 session transcript is deleted only on this branch — it stays on `main`, which is the point of branching. Committing:


===== ASSISTANT [2026-09-06T06:15:37.442Z] =====
Both done.

**Git repo** — `~/purewater-campaign-v2` is now a real repo sharing v1's history, on branch `v2-living-world` branched from `main` at `a374c3c`. One commit, working tree clean. The v1 tree (including the session-01 transcript) is untouched on `main`. Nothing pushed — the `origin` remote points at `fourth-wall-gaming/purewater-campaign`, so say the word if you want it up there.

**Character reset** — the mechanical reset (Santo alive, Conall's arm 4/4) had already happened during the build, but checking turned up the part that hadn't: **their prose was still written from mid-campaign.**

- **Santo:** "He *attempted* a demonic spirit-binding ritual on Emmeralda — and *dropped* his Asmodeus-marked knife as he fled." That's `d-3/night`, still three watches in the future, asserted as done.
- **Conall:** "is investigating the attack at the Sylph's Embrace and working with Temerach to expose Baron Hanzo" — and "currently nursing a wounded right arm," the wound I'd already cleared mechanically.

Scanning the rest found the same leak in two more, one of them worse:

- **Emmeralda's** sheet had her already carved and partially possessed — she's meant to be perfectly well at open, with an evening booked to a young nobleman who paid for privacy.
- **Ila's** described her flinging her arms around Gardwen after the healing. A thirteen-year-old NPC's sheet was narrating a scene nobody has played.

All four rewritten to `d-3/dawn`, with the future material moved into explicit **GM:** notes about what they *become*.

**Full status check, all 31 characters:** every one active, unwounded, Fresh, full luck and magic, zero banked experience rolls. One real gap turned up — **Baron Hanzo had an empty equipment list** despite a "Nobleman (broadsword)" style of 56. Since `resolve-attack` looks weapons up by name, the campaign's main antagonist couldn't have fought. He now carries a broadsword, dagger, cuirass, and the **binding locket** — which matters, because Nus's `d-1/day` beat lifts it off him. Ruhi checks out properly as a quadruped with a natural Bite.

---

The board is clean and the world clock is holding at `d-3/dawn`. Magda is still standing in the queue at the ford, thirty feet behind a young woman with a grey wolf who hasn't noticed her yet — and the column that pushed through ahead of you is already most of the way to the city gates.

What do you do?


===== USER [2026-09-06T06:21:57.366Z] =====
How to ensure that we have a well-defined definition of the state of the game that isn’t distributed across the characters in a way that can’t be reconciled easily. Think carefully about how we should represent what each character knows and what their intentions are. This then can correspond to some more detailed central state that represents what is actually happening.


===== ASSISTANT [2026-09-06T06:22:53.110Z] =====
This is the right question to ask now — and today gave us the evidence for why. Let me check one thing before I answer, because it determines which shape is available.


===== ASSISTANT [2026-09-06T06:23:39.455Z] =====
Confirmed — relations owning attributes is already an established pattern here (`alh-affiliation owns valid-from/valid-until`). So a knowledge edge can carry its own metadata. That makes the clean shape available.

## The actual problem

Today produced the evidence twice. Santo's sheet said he *"attempted the ritual and dropped his knife fleeing"* — an event three watches in the future. Ila's sheet narrated her hugging Gardwen after a healing nobody has played. Neither was detectable by any query; I found them by grepping prose for past-tense verbs.

That's the failure mode you're pointing at, and the cause is structural: **"what is true" and "who knows it" are currently stored as prose, in several places, with no way to reconcile them.** Right now situation-state is smeared across character `content`, agenda `content`, journal event narratives, lore `visibility`, and the GM's memory. Any two can disagree and nothing notices.

Notably, `SKILL.md` already *asserts* the rule — "Character knowledge is per-character, not per-campaign… before giving a PC a fact, check WHO learned it" — with no mechanism behind it. It's discipline where it should be data.

## The invariant

> **Ground truth lives in exactly one place. Everything else is a query into it.**

Specifically: **there is no per-character state store.** A character's knowledge is a *projection* of one central graph, never a separate blob. You can't have two sources disagree when there's only one source. That's what makes it reconcilable by construction rather than by care.

## The missing primitive is the fact

Facts don't exist as first-class things today. They should:

```
entity myth-fact sub alh-note,          # description = the proposition
    owns myth-fact-status,              # not-yet-true | established | superseded
    owns myth-fact-truth,               # true | false | partial
    owns myth-time-index,               # when it became true
    plays myth-fact-from:fact,          # <- the beat/event that made it true
    plays myth-fact-about:fact,         # <- its subjects
    plays myth-knows:fact;

relation myth-knows,
    owns myth-knowledge-certainty,      # knows | believes | suspects | wrong
    owns myth-knowledge-since,          # time index learned
    owns myth-knowledge-source,         # witnessed | told-by | deduced | rumor
    relates knower,                     # character or faction
    relates fact;
```

Two things earn their keep immediately:

**`myth-fact-status: not-yet-true`.** "Santo carved Emmeralda" exists from the start as an *unrealised* fact owned by its beat. It flips to `established` when the beat fires. Nobody can know it before then — and a knowledge edge pointing at a `not-yet-true` fact is an integrity violation you can *check for*, which is exactly the bug I hand-fixed today.

**`myth-fact-truth: false`.** This is not decoration. Your v1 campaign turned on a false belief that half the city held — *"the runner who fled the woods was Lord Santo."* Rumour, lies, and mistaken identity are the engine of this story, so belief and truth have to be separable. A character can `know` something false; that's a fact node with `truth: false` and knowers attached.

## This closes the loop on intentions

You already have intentions modelled properly — agendas are first-class. What's missing is that **intentions are knowledge-conditioned**, and right now that link is prose.

"A di Teufel who is not his" is `status: dormant` with a note reading *"activates the moment the Baron gets a clear look at Randall's face."* That's a trigger no machine can evaluate. Give the agenda a requirement instead:

```
relation myth-agenda-requires, relates agenda, relates fact;
```

Now the dormant agenda requires the fact *"Hanzo has a living bastard son"*, held by Hanzo. Activation stops being something I remember and becomes something `tick` computes: **for each dormant agenda, if its holder knows all required facts → activate.** The knowledge graph and the intention graph reconcile mechanically.

## What it buys you

- `get-character-view --id <magda>` — everything Magda can legitimately act on. Single-PC play becomes honest by construction instead of by my restraint.
- `who-knows --fact <f>` — "who can betray this?"
- `check-consistency` — no knower knows an unestablished fact; no active agenda lacks its required knowledge; no character sheet asserts situation. Run it in CI over the shipped package, and today's four leaks fail the build.
- Novelization gets POV for free — a chapter written from what one character knew at a time index.

## The discipline that keeps it from exploding

Not everything is a fact. The test: **if two characters could act differently depending on whether they know it, it's a fact. Otherwise it's colour.** Roughly 20–40 facts across a campaign this size, not 500. Character prose then describes *character* — temperament, skill, history — and never situation.

## What I would not build

No modal logic or nested belief ("Blau thinks Marisette suspects…"). A certainty enum plus a source is enough for a table. And no per-character snapshots — that's precisely the thing that can't reconcile.

## Cost, honestly

Schema, ~6 CLI commands, export/import round-trip, docs, and a `check-consistency` pass. Comparable to the agenda/beat work — call it the same order of size. Migration is cheap: facts accrue from play, so existing campaigns start with an empty fact graph plus a handful seeded at open.


===== ASSISTANT [2026-09-06T06:31:04.744Z] =====
Building it. Schema first.


===== ASSISTANT [2026-09-06T06:31:30.220Z] =====
Now the pure logic in the engine:


===== ASSISTANT [2026-09-06T06:31:47.665Z] =====
Tests for the reconciliation rules:


===== ASSISTANT [2026-09-06T06:32:09.915Z] =====
Now the CLI commands:


===== ASSISTANT [2026-09-06T06:33:05.138Z] =====
Now wiring fact-gated activation into `tick`, plus the argparse registrations:


===== ASSISTANT [2026-09-06T06:33:31.038Z] =====
All 10 registered. Loading the schema and smoke-testing the epistemics against a live campaign:


===== ASSISTANT [2026-09-06T06:34:00.022Z] =====
One bug: `$k isa $kt` with an unbound type variable matches every supertype in the chain, so each edge returns three times. Dropping it:


===== ASSISTANT [2026-09-06T06:34:08.880Z] =====
Now the payoff test — the fact-gated dormant agenda activating through `tick`:


===== ASSISTANT [2026-09-06T06:34:28.803Z] =====
The full loop works — the prose trigger is now computed. Let me verify `check-consistency` actually has teeth by planting the exact bug that shipped in v1:


===== ASSISTANT [2026-09-06T06:34:48.999Z] =====
Both violation classes caught and repaired. Now export/import so this ships with a campaign:


===== ASSISTANT [2026-09-06T06:36:01.714Z] =====
Round-trip is lossless. But the smoke tests polluted the live campaign's opening state — facts established, edges recorded, and the dormant agenda activated. Let me verify the committed package is still pristine and rebuild from it:


===== ASSISTANT [2026-09-06T06:36:10.347Z] =====
The committed package is pristine — clock at `d-3/dawn`, PCs placed, agenda dormant, no facts. Rebuilding the live campaign from it and seeding a designed fact graph:


===== ASSISTANT [2026-09-06T06:37:07.178Z] =====
This is the whole point, working: Magda knows nothing (she just arrived), Conall doesn't know his own parentage, Temerach has held that secret for years, and the Baron knows his own secrets but *not* that he has a bastard — so his agenda stays dormant. The asymmetry is data now, not my memory.

Docs:


===== ASSISTANT [2026-09-06T06:37:52.762Z] =====
60 passing. Exporting the seeded campaign to the package and committing both repos:


===== ASSISTANT [2026-09-06T06:38:27.934Z] =====
Final verification on the shipped package:


===== ASSISTANT [2026-09-06T06:39:00.186Z] =====
Built, tested, committed. 60 tests passing, lossless round-trip including edge metadata.

## The answer, in one line

**Ground truth lives in exactly one place; everything else is a query into it.** There is no per-character state store — a character's knowledge is a *projection* of the central fact graph, so two views can't drift apart by construction rather than by care.

## What that looks like now

**`myth-fact`** — one proposition, with a status (`not-yet-true` → `established` → `superseded`), a truth value, and the world-clock index it became true. Beats *own* their facts, so the campaign ships its future enumerated but not yet real.

**`myth-knows`** — the edge, carrying `certainty` (knows/believes/suspects/wrong), `source` (witnessed/told/deduced/rumor), and `since`.

Status and truth stayed independent, and that earned itself immediately: the manhunt is now modelled as *"The man who carved Emmeralda was Randall the Pearl thief" — `truth: false`*. A lie people act on is a first-class object, not something I improvise consistently and hope.

## The state at `d-3/dawn`

```
Magda      knows nothing              -- she has just arrived
Randall    knows nothing of his parentage
Conall     knows nothing of his parentage
Gardwen    SUSPECTS the champion is her brother
Temerach   KNOWS whose sons the twins are   (held for years)
Hanzo      knows his own secrets -- but NOT that he has a bastard
```

That last line is now load-bearing. "A di Teufel who is not his" is `require-fact`-gated on the Baron knowing, so it sits dormant and **`tick` activates it by itself** the moment the players let him find out. I verified the whole loop: dormant → Hanzo learns → next tick returns `activated_agendas: [A di Teufel who is not his]`. The trigger stopped being a note in a file.

## The v1 bug class is now a failing check

I planted both violations deliberately and `check-consistency` caught them:

```
CAUGHT: knows-unestablished -> Gardwen's magic saved Emmeralda's life
        | knows something that has not happened yet
CAUGHT: knew-too-early      -> The Baron's column reached the city gate
        | learned at 52 but only became true at 53
```

That's precisely what shipped in v1 undetected and that I found by grepping prose for past-tense verbs. `learn` also refuses outright to attach knowledge to an unestablished fact.

**Two things worth flagging.** My smoke tests polluted the working campaign — established facts, activated the dormant agenda — so I rebuilt the live campaign from the pristine committed package rather than trying to unpick it; play now runs on `myth-campaign-8327f8687a98`. And I hit a real query bug where an unbound type variable matched every supertype, returning each knowledge edge three times; fixed.

The discipline that keeps this from exploding is in `USAGE.md`: **if two characters could act differently depending on whether they know it, it's a fact — otherwise it's colour.** Twelve facts here, not five hundred. Weather isn't a fact; who owns the knife is.

Nothing pushed. Magda is still at the ford, and the clock hasn't moved — ready when you are.


===== USER [2026-09-06T06:40:09.341Z] =====
Gardwen has no idea about where her bother is - she just knows the dragonknights were the ones that took him long ago


===== ASSISTANT [2026-09-06T06:40:43.182Z] =====
Correcting that — she was seeded as `suspects` on "the champion is her brother," which hands her the reveal ten years early. The prose in her entry point was already right ("your brother's body was never among the dead"); my knowledge seeding overreached.


===== ASSISTANT [2026-09-06T06:41:32.066Z] =====
Corrected, and consistency still passes. Note what this makes true: **nobody** now knows the champion is her brother — Hanzo has never heard of Gardwen, so the identification is genuinely unmade. That's the `d0` reveal, and it's now enforced rather than remembered.

Re-exporting and committing:


===== ASSISTANT [2026-09-06T06:42:11.882Z] =====
Right — and that exposes a modelling flaw in how I worded it. The fact reads *"Baron Hanzo has a living son he does not know about"* — singular, and it bakes Hanzo's ignorance into the proposition itself. Ignorance belongs in the knowledge edges, not the statement; as written, Hanzo learning it would be self-contradictory, which breaks the gate.

I need a way to revise a fact's wording — I built `revise-beat` but no equivalent for facts. Adding it:


===== ASSISTANT [2026-09-06T06:42:29.908Z] =====
Let me land the parentage fix, then we play.


===== ASSISTANT [2026-09-06T06:43:25.483Z] =====
60 passing, both repos clean. **Let's play.**


===== ASSISTANT [2026-09-06T06:43:49.278Z] =====
# Session 1 — The Ford

**`d-3/dawn`** · three days before the Lake Lady's Tourney

---

The mist off the river is the same temperature as the air, so it doesn't lift — it just stands there, waist-high, and the queue stands in it.

A hundred people deep and going nowhere. Carters with the brakes on. A family of pilgrims who've been singing the same three lines since the last milestone. A troupe of tumblers arguing about a split. Everyone backed up behind something that came through first and didn't wait, and everyone pretending they weren't made to stand aside for it — you can still see the churn in the mud where the horses went through, four abreast, at a pace that says *move*.

Purewater sits across the water. Towers, and a smell like salt laid over something standing still too long.

Eleven nights, the same dream. Hel doesn't explain. Hel points.

And thirty feet up the queue is the woman she pointed at.

Younger than you thought. Travel-worn in the way that means months, not weeks — the cloak has been mended by someone who isn't good at mending. She isn't looking at the city like everyone else in this queue. She's looking *past* it, north, up the road where the last of the dragon-scale is going away at a trot and the mist is closing over the gap it left.

There's a grey wolf sitting against her leg. Not on a rope. Sitting the way a dog sits when it has decided the matter is settled.

Nobody else in the queue is standing within eight feet of her, and from the careful way they aren't looking, they've all worked out why and would like it not to be mentioned.

She hasn't seen you.

---

**Magda** · Quarterstaff · Perception 70 · Brawn 71 · Insight 30 · Influence 18 · Luck 8
*Passions: Love (Sister) 70 · Curmudgeon 54 · Fear of Arcane Magic 54*

The queue isn't moving. You have as long as you want, and Hel has never once told you what to do when you got here.

**What do you do?**


===== USER [2026-09-06T06:43:59.834Z] =====
We will need to have a way to rewrite intentions and future actions into changed facts when events change the intentions


===== ASSISTANT [2026-09-06T06:44:46.456Z] =====
Good catch, and it's a real gap in what I built — not just a future nicety. Let me show it concretely on a throwaway campaign rather than assert it:


===== ASSISTANT [2026-09-06T06:45:22.186Z] =====
Confirmed — three orphaned futures, and `check-consistency` says **ok**. Santo is dead, that night can never happen, and the graph still believes it will.

## What's missing

Three things, and they close one loop.

**1. Consequence edges — the inverse of `requires`.** Today knowledge activates an agenda. Nothing lets an *event* change one. The prose in the agenda files says it — *"If Santo dies, this agenda converts to vengeance"* — which is exactly the unevaluable-prose problem we already fixed once.

```
relation myth-consequence,
    owns myth-consequence-effect,    # thwart | abandon | stall | advance | complete
    owns myth-consequence-amount,
    relates fact, relates agenda;
```

Note these are genuinely different gates: `requires` is knowledge-gated (Blau needs to *learn* Santo is dead before he can want revenge); `consequence` is world-gated (a dead man's agenda ends whether or not anyone knows).

**2. The cascade.** One function, run on `establish-fact` and inside `tick`:

```
fact established
  → consequences fire on agendas        (thwart / abandon / stall / advance)
  → dead agendas cancel their pending beats     ← "future actions rewritten"
  → those beats' not-yet-true facts are superseded  ← the leak above
  → dormant agendas whose holders now know activate
  → their beats go live
```

**3. `supersede-fact --id --by <f>`** so a rewritten future is *traceable* rather than deleted — and so a corrected false belief keeps its history ("the runner was Lord Santo" superseded by "the runner was his bastard twin"), which matters because people who learned the old one still believe it.

Plus two new consistency checks: orphaned not-yet-true facts, and pending beats on dead agendas.

**One thing already works that we're not using:** the schema lets a fact take an *agenda* as its subject. So *"Hanzo means to win the Tourney with a possessed champion"* is a fact — meaning intentions are discoverable, believable, and can be **wrong**. Crowbill believing the Baron just wants political influence is a `truth: partial` fact. That's most of what the party actually plays for, and it needs no new schema.


===== ASSISTANT [2026-09-06T06:46:41.091Z] =====
Building it. Schema:


===== ASSISTANT [2026-09-06T06:47:31.986Z] =====
Now the CLI: the cascade itself, `add-consequence`, `supersede-fact`, and wiring it into `establish-fact`, `fire-beat` and `tick`.


===== ASSISTANT [2026-09-06T06:48:01.890Z] =====
Now wiring the cascade into `establish-fact`, `fire-beat` and `tick`:


===== ASSISTANT [2026-09-06T06:48:33.209Z] =====
Adding the two new consistency checks, then loading the schema:


===== ASSISTANT [2026-09-06T06:48:47.717Z] =====
Now the decisive test — the exact scenario from the demo, end to end:


===== ASSISTANT [2026-09-06T06:49:14.340Z] =====
The whole loop works: one fact — *Santo is dead* — abandons his agenda, thwarts Blau's, stalls the Baron's clock, and cancels two future beats automatically. Now round-tripping it:


===== ASSISTANT [2026-09-06T06:49:51.677Z] =====
The optional attribute comes back as `[]` and gets written literally. Fixing the flatten, and hardening `_opt`:


===== ASSISTANT [2026-09-06T06:50:11.291Z] =====
Round-trip clean. Now wiring Purewater's actual prose triggers into real consequence edges:


===== ASSISTANT [2026-09-06T06:50:28.799Z] =====
Docs, tests, export, commit — then the table.


===== ASSISTANT [2026-09-06T06:51:37.997Z] =====
Built, tested, committed — 67 passing, both repos clean. The loop you asked for:

```
fact established
  → consequences change agendas       thwart / abandon / stall / advance
  → knowledge-gated agendas activate
  → dead agendas cancel their pending beats      ← future actions rewritten
  → futures no live beat can establish are superseded
```

Proven end to end: establishing **"Santo is dead"** abandoned his agenda, thwarted Blau's, stalled the Baron's clock 2→0, and **cancelled two future beats by itself**. And the leak I demonstrated is now caught — `check-consistency` reports `orphaned-future`, `cascade` retires them.

Purewater's contingencies are wired as real edges now (Santo's death, the locket theft, Nus's murder), and `fire-beat` settles its own facts — `--witnesses` grants knowledge to whoever was actually there.

Clock still `d-3/dawn`. Nothing has happened.

---

# The Ford

The mist off the river is the same temperature as the air, so it doesn't lift — it just stands there, waist-high, and the queue stands in it.

A hundred people deep and going nowhere. Carters with the brakes on. Pilgrims who've been singing the same three lines since the last milestone. A troupe of tumblers arguing about a split. Everyone backed up behind something that came through first and didn't wait — you can still see the churn in the mud where the horses went through four abreast, at a pace that said *move*.

Purewater across the water: towers, and a smell like salt laid over something that's been standing too long.

Eleven nights, the same dream. Hel doesn't explain. Hel points.

Thirty feet up the queue is the woman she pointed at.

Younger than you'd thought. Travel-worn the way that means months, not weeks — the cloak's been mended by someone with no gift for it. She isn't looking at the city like everyone else. She's looking *past* it, north, up the road where the last of the dragon-scale is going away at a trot and the mist is already closing over the gap.

There's a grey wolf sitting against her leg. Not on a rope. Sitting the way a dog sits when it considers the matter settled.

Nobody's standing within eight feet of her, and from how carefully they're all not looking, they've worked out why and would rather not discuss it.

She hasn't seen you.

---

**Magda** — Quarterstaff · Perception 70 · Brawn 71 · Endurance 78 · Willpower 63 · Insight 30 · Influence 18 · Luck 8
*Love (Sister) 70 · Curmudgeon 54 · Fear of Arcane Magic 54*

The queue isn't moving. You've got as long as you want, and Hel never did say what to do once you got here.

**What do you do?**


===== USER [2026-09-06T06:53:39.061Z] =====
Go up to her. Nod. Looker in the eye. Ask her, who are you?


===== ASSISTANT [2026-09-06T06:54:15.984Z] =====
She's thirty feet. The mud takes the sound out of it.

Nobody stops you. The queue has already decided that the space around that woman belongs to someone else's problem, and an old woman walking into it is an old woman's business.

At about twelve feet, the wolf stands up.

It doesn't growl. It doesn't show teeth. It just rises off its haunches and turns to face you square, and every conversation within thirty feet stops, and a carter behind you says *oh* very quietly and finds something to do with his hands.

The woman's hand has gone inside her cloak. Not fast. The way you put a hand on a door latch in a house you don't trust.

You keep walking. You've been bitten before, and Hel has never once shown you a dream that ended in a dog.

Close now. Close enough to see the rest of it — and with fifty years of looking at people to feed pigs and bury them, you get a good deal in one pass. She's had a bad month and a worse decade. There's road-grime worked into the seams of her knuckles and none at all under the nails, which means she washes what she can and has given up on the rest. She's thin in the way of someone who eats when there's food rather than when there's hunger. And she's young enough that the flat, patient watchfulness in her face doesn't belong on it. Someone put that there.

The wolf's ears go back — not aggression. Checking with her.

She doesn't tell it anything. She's waiting to see what you are.

So you stop, an arm's length outside what the wolf considers hers. And you nod — once, the nod you'd give a neighbour over a fence — and you look her straight in the eye and say it.

*"Who are you?"*

Her chin comes up a fraction.

It lands strangely. You watch it land. Not the question she was braced for — she was braced for *what do you want* or *get that animal away from me*, and had answers ready for both, and now she hasn't. Something goes across her face and is put away again.

The hand comes out of the cloak. Empty.

"Gardwen," she says.

And then, in a voice that has clearly had this conversation before and expects nothing from it:

"You'll want to be somewhere else, mother. People who stand near me have a poor time of it."

The wolf hasn't sat back down.

Behind you, the queue lurches forward six feet and stops again.

---

She gave you a name and a warning and nothing else. **What do you do?**


===== USER [2026-09-06T06:58:28.775Z] =====
Grunt.  I’ve been dreaming of you girl. 

Walk to the wolf and pet it. Just put my hand in its fur. Northern berserkers like wolves.

My goddess tells me you’re someone I need to help - don’t know why but that’s what she told me


===== ASSISTANT [2026-09-06T06:58:47.994Z] =====
That's a real risk with a real edge behind it. Let me check what she actually has for it rather than inventing a skill:


===== ASSISTANT [2026-09-06T06:59:03.109Z] =====
**Survival 63** is the honest skill here — reading and handling an animal, not sweet-talking one (her Influence is 18). The northern kinship and your unbothered calm are what keep it at **Standard** rather than Hard: you're not afraid, and you've just knocked the woman off her script.

But that's a bonded wolf, and its person is braced for violence.


===== ASSISTANT [2026-09-06T06:59:24.904Z] =====
**12 vs 63 — success.** Not a critical (that needed 7 or under), but a clean, unhurried one. Low roll, no drama in it.

---

You grunt. It's not a word. It's the noise you make at a gate that's swollen shut, and it carries about the same amount of argument.

"I've been dreaming of you, girl."

And then you walk past her.

Not at her — *past* her, on the wolf's side, which is the wrong side, which is the side no one uses. You don't slow and you don't reach out early and you don't do the thing townsfolk do where they put the hand out flat like they're presenting a document. You walk the way you'd walk to a gatepost, and when you get there you put your hand into the fur at the base of its neck, where the ruff is thickest and a hand disappears to the wrist.

The wolf goes rigid.

You can feel it under your palm — the whole animal locking, every muscle from shoulder to haunch making one decision at once, and its head comes round and there is a moment where its jaw is four inches from your forearm and its breath is hot on the inside of your wrist.

You don't move your hand. You scratch. Down, once, the way you'd work a burr out.

The rigidity goes. Not all at once — it comes out of the shoulders first and then the back, and the head turns away from your arm, and the animal makes a sound low in its chest that isn't a growl and isn't anything a townsman would recognise as anything at all.

Up north they'd know it. Up north they'd say the dog had decided you were furniture, and furniture is the highest rank a stranger gets.

"—*don't*," Gardwen says. Too late by about three seconds. Her hand is half out, and it stops, and it stays stopped.

She's staring at your hand in her wolf's ruff.

"She doesn't—" She stops. Starts again. "Ruhi doesn't let people do that."

You keep scratching. The wolf leans a little into it, which you suspect will be worse for the woman than the growl would have been.

"My goddess tells me you're someone I need to help," you say. "Don't know why. That's what she told me."

The queue lurches forward. Neither of you moves with it, and behind you somebody swears and goes around.

Gardwen looks at you for a long moment. The flat watchfulness is still there — it doesn't go — but something has got in behind it.

"Your goddess," she says slowly. "Which one."

And you can hear what the question actually is. She's asking whether you're one of the singing ones. Whether you're going to tell her it'll be all right.

Ruhi sits back down. Against your leg, now, not hers.

Gardwen notices that too.


===== USER [2026-09-06T07:02:27.668Z] =====
Hel - Death. Not death in battle but death everywhere else.

(Quick question - remind me what I saw in the dreams?)


===== ASSISTANT [2026-09-06T07:03:03.135Z] =====
**The dream — eleven nights running, the same one:**

1. **A young woman with a wolf.** (Sitting against your leg right now.)
2. **A burning house.**
3. **A knight in dragon-scale who is already dead but does not know it.**

And one instruction, which is the part you've been chewing on for three weeks of road: ***"lay the dragon warrior to rest."*** Not *kill*. Hel was specific by being unspecific, the way she is. You've turned it over a hundred miles and it still won't come apart.

Hel doesn't explain. Hel points.

---

"Hel," you say. "Death."

The wolf's weight settles further against your shin.

"Not death in battle." You say it the way you'd correct someone about which field the boundary stone is in. "The other kind. Everywhere else. In the bed, in the byre, in the bad winter. The ones nobody sings about."

Gardwen goes very still.

You've seen the look before, on people who expected to be sold something. It's the look of a bucket that's had the bottom go out of it. She was braced for a priest — the singing kind, the kind who tell a woman with a dead family that it was a mercy and a plan. She had something sharp ready for that.

She doesn't use it.

"No," she says quietly. "No, that's — " and she stops, and looks at the mud, and you watch her decide something.

"That's an honest god."

The queue moves. Twelve feet this time. Somebody's ox has finally consented.

She still doesn't move with it.

"I've had eleven nights of you too, then, have I." Not really a question — she's testing the shape of it, turning it the way you turned *lay him to rest*. "What does she show you?"

Then, before you can answer, something else crosses her face and she asks the real one instead, fast, like a woman pulling a splinter:

"Does she show you a boy?"

Her hand has gone into Ruhi's ruff beside yours. She doesn't seem to have noticed doing it. Her knuckles are white.

---

*She's asked for the dream. You've got three images and an instruction — and she's just told you what she's hoping is in it.*

**What do you tell her?**


===== USER [2026-09-06T07:06:55.572Z] =====
No. Not a boy. A knight in dragon scale armor not that give ever seen anyone look that way before. 

I’m to fight for you girl. To protect you and yours however youd ask. Die for you, if need be. 

Kneel and present my staff. Even though it probably looks rediculous


===== ASSISTANT [2026-09-06T07:07:41.836Z] =====
"No," you say. "Not a boy."

You watch that land, and you don't dress it. You've delivered enough bad news across enough gates to know that softening it only makes people hear it twice.

"A knight. Dragon-scale." You turn your free hand over, looking for the words for the part that doesn't fit. "Never seen anyone look that way before, and I've seen a great many people look a great many ways. He's dead, girl. Standing up and walking and dead, and nobody's told him."

Gardwen's knuckles in the ruff go from white to slack.

You can see the arithmetic happening. *Dragon-scale.* Not the answer she wanted — but not a stranger to her either, and you can see it cut a different way than you meant it, and there is nothing to be done about that. Her eyes go north, to the road, to the churned mud where twenty-odd riders in scale went through at a pace that said *move*.

"Dragon Knights," she says. Flat. "It's Dragon Knights you dream of."

She doesn't say the rest. Whatever the rest is, it stays in.

---

Then you kneel.

The mud takes your knee with a sound like a boot coming out of a bog, and it is cold, and it goes straight through the wool, and you are seventy years old on the outside and there is absolutely nothing dignified about any part of this. Somewhere behind you one of the tumblers says something and another one laughs and is hit.

You hold out the staff. Crosswise, both hands, the way it's done — the way your grandmother did it to a man who died the following spring.

"I'm to fight for you, girl. Protect you and yours, however you'd ask it. Die for you, if it comes to that."

The queue goes on lurching past. A carter's wheel throws grit across your skirt. You've made yourself absurd in front of about forty strangers and a wolf, and Hel has never in eleven nights suggested you'd be spared that.

Gardwen doesn't take the staff.

She stands there with her hand in her wolf's fur next to a stranger's hand, and her mouth does something unsteady, and she looks — not at you. Past you. At the middle distance, hard, the way people do when they will not do the other thing in public.

"Get up," she says. It comes out wrong. She tries again. "Get *up*. You'll — the ground's freezing, you'll ruin your knees, get up—"

And she's reaching down to haul you, one hand under your arm, and her grip is stronger than it looks and it is not steady at all.

She gets you upright. She doesn't let go straight away.

"Ten years," she says, very low, only for you. "Ten years and not one person. Not one. And a pig-farmer kneels in the *mud* at a *ford*—"

She stops. Swallows it. Puts the flat watchfulness back on like a hat, and it doesn't sit right any more, and she knows it doesn't.

"I don't know what to do with you," she says.

Ruhi, who has decided, leans on your leg.

"Gardwen," she says again, properly this time, and offers her forearm the way soldiers do — the woodland version, wrist to wrist. "My brother was taken by men in that armour. Ten years ago. He's the only thing I have left to look for, and I'm three days behind that column, and if your god has business with a dead man in dragon-scale then Hel and I want the same road for a while."

*Behind you the ford has finally opened. The queue is moving properly now, and the crowd is starting to flow around the two of you like water round a stone.*


===== ASSISTANT [2026-09-06T07:08:38.263Z] =====
**Recorded.** Magda gains a Passion:

> **Sworn to Gardwen (by Hel) — 70**

Which is now a real mechanical thing: augment any roll made in Gardwen's service with it, the way you would Love (Sister). It also means Hel notices if you ever act against it.

And note what the knowledge graph is now enforcing: Gardwen heard *"a knight in dragon-scale who is already dead"* and filed it under **the enemy who took her brother**. She has not connected it to *him*, and now she can't — nobody in the campaign knows that, and I'd have to write the edge to change it. Your dream is pointing straight at the thing she's looking for, and neither of you can see it.

---

The crossing is open. The queue is moving properly now and people are flowing round the pair of you like water round a stone, with the odd shoulder and the odd look.

Gardwen's forearm is still out.

Beyond the ford the road runs down to a causeway, and the causeway runs into Purewater — and even from here you can see the thing that makes this a *city of canals* rather than a city with a river in it. There's no gate in a wall. There's a water-gate, and a customs pontoon, and a queue of *boats* behind the queue of carts, and the whole business of getting in is going to cost coin or a good story.

Three days behind a column of Dragon Knights. Two of you, one wolf, a quarterstaff and a staff sling.

You know this city a little, from years back. You know which madames rent rooms to women travelling alone and don't ask after them — **the Sylph's Embrace on the Pearl** is Constantine's house, and he was decent then. Beds, and no questions, and a man who hears things.

*You have the rest of the morning and a woman who has just decided she'll follow you.*

**What now — take her arm? And where do you take her?**


===== USER [2026-09-06T07:11:46.207Z] =====
Take her arm. Smile. 

“Come on then, Gardwen lass. I know a place in the city we’ll be able to rest and plan from.”


===== ASSISTANT [2026-09-06T07:12:42.483Z] =====
The column beat came due **onscreen** — because Randall is standing in Caravan Square. He's GM-run, so it happens without you; resolving it off your screen:


===== ASSISTANT [2026-09-06T07:13:25.947Z] =====
You take her arm — wrist to wrist, the soldier's grip, done the woodland way — and you smile. It's not a pretty smile. Most of the teeth are still yours, which at your age is its own kind of boast.

"Come on then, Gardwen lass. I know a place in the city. We'll rest, and we'll plan from there."

Something in her shoulders comes down about an inch. It's the first time she's looked less than braced since you laid eyes on her.

"Three days I've been eating their dust," she says as you take the ford — the water's shin-deep and colder than the mud was. "Then they have to queue like everyone else, and I'm suddenly close enough to smell the horses." She glances north, where the churn goes. "I don't know whether that's luck."

Ruhi swims the deep part and comes out shaking, and soaks a pilgrim, who takes it philosophically.

---

The causeway is two miles of raised stone across a flat of reed and standing water, and it takes you most of the morning because everything on it is going at the pace of the slowest cart. Gulls. The smell getting stronger and less like salt.

Gardwen talks a little, the way people do when they haven't in a while — mostly about the road, nothing about the ten years. She asks twice more about the dream, in different words, hunting the same answer from different sides. You give her the same three things. A woman with a wolf. A burning house. A dead man in dragon-scale.

She doesn't ask about the burning house. You notice that she doesn't.

---

**Purewater**, close up, has no wall worth the name. It doesn't need one — it has water instead. The causeway runs into a **water-gate**: a stone throat with a chain-boom across it, a customs pontoon lashed alongside, and the whole of tourney week trying to get through at once.

And the city beyond it is *loud* in a way that isn't normal traffic. Something's just happened up there. You can hear it in the pitch.

The cart in front of you belongs to a fishmonger who has clearly done this a hundred times, and who is delighted to have someone to tell.

"—straight through, mother, straight through the middle of the square not an hour past. Twenty of 'em. *Di Teufel*, the Baron himself, up from the border for the Tourney." He spits over the side, companionably. "And a litter in the middle with the curtains sewn *shut*, and lads walking round it facing *in*. Facing *in*! What d'you carry that you have to watch it, eh?"

Gardwen has stopped walking.

Ahead, at the pontoon, a bored customs man in the Harbor Masters' green is working the queue. You can see his system from here: carts and cargo pay by the wheel, and foot-traffic pays a tourney-week head-toll — or produces something that makes it not worth his morning to argue. He's already turned two people back.

You have a quarterstaff, a staff sling, an old woman's purse, a druid who has never been in a city, and a wolf.

---

**The wolf is the problem.** Nobody at that pontoon is going to wave a grey wolf into Purewater on tourney week without a conversation.

What do you do — pay, talk, or find another way in?


===== USER [2026-09-06T07:15:19.394Z] =====
OK. Note to Claude. Do that in the background and don’t say anything to the live player. Remember, your main role is that of a storyteller. When you are GMing, your job is to convey the story so that it is fun, and transporting to the player. They are going to a new world through your words. Make them count and think about what NOT to say.


===== ASSISTANT [2026-09-06T07:16:01.149Z] =====
Understood. Bookkeeping goes silent from here — you're at a ford, not reading a build log.

---

The queue shuffles. The fishmonger's cart grinds forward a length and he keeps talking to nobody in particular about curtains sewn shut.

Ahead, the customs man works his way down the line at the pace of a man who finishes at dusk whatever he does. Green coat, ink on his fingers, a tally-board under one arm. He turns back a tinker. He waves through three nuns without looking up.

Gardwen is still watching the city, and not the pontoon, and not the man in green, and not the chain-boom across the throat of the water-gate that everything has to pass under.

Ruhi presses against your shin, panting, wet to the shoulder, entirely and obviously a wolf.

The cart in front of you moves.


===== USER [2026-09-06T07:17:43.936Z] =====
I’m just going to intimidate our way in. No bollocks from these fuckers


===== ASSISTANT [2026-09-06T07:18:34.384Z] =====
You don't wait to be got to. You go to him.

Which is wrong — everyone in the queue knows it's wrong, you can feel forty people deciding not to be involved — and you keep doing it, straight up the line past the fishmonger, past a family with a goat, until you're standing at the customs man's elbow with the wolf at your knee.

He turns with his mouth already open. Something practised. *Back in line, mother.*

You look at him.

You've buried people. Not in wars — in beds. You have put your hand over the eyes of men who were shouting an hour before, and gone out afterwards and fed the pigs, because the pigs don't care. Whatever that does to a face, it has had fifty years to do it to yours, and you let him have all of it.

"We're going in," you say.

The mouth closes.

He looks at the staff, which is not a walking stick and has never once pretended to be. He looks at the wet grey animal that is watching him with the total, patient attention of something that has never in its life been told it's a good girl. He looks back at your face and does not find anything there that is negotiating.

You can see him reaching for the words — *toll*, *licence*, *by order of the Harbor Masters* — and you can see each of them arrive and look at the situation and decide against it.

"There's a fee," he says. It comes out with no starch in it at all.

"There is."

A pause. Long enough for him to understand that you are not going to fill it.

He looks down at his tally-board. It's a good board. He's put a lot of himself into that board.

"Two on foot," he says to it. "And a *dog*." He writes *dog*. He underlines *dog*, as though the underlining is a form of protest that history will one day recognise. "Muzzled inside the Merchant's Quarter, that's not me, that's the Guild, and if it goes for anyone it's your neck not mine—"

"Understood."

"—and I never saw it."

"You never did."

He steps aside. He does it small, so it doesn't look like stepping aside.

As you pass under the chain-boom he says, not quite to you, in the flattened voice of a man reasserting something to himself: "Everyone's mad this week. It's the Tourney." And then, because he can't help it, because the thing is still sitting in the top of his head where it's been sitting all morning:

"Third lot today gone through with something they won't show me."

---

And then Purewater.

The noise arrives first — it comes up off the water and off the stone at the same time and hits from underneath. Then the smell: salt, tar, fish, hot oil, wet rope, and under it all the sweetish standing note of a city that sits in its own water and has made peace with it.

There is no ground. That's the thing nobody tells you and you'd forgotten. There are buildings, and there is water, and between them there are ledges — walkways a yard wide, no rail, slick as an eel — and the traffic that matters is *underneath* you, poled and rowed, shouting.

Gardwen has stopped dead six feet inside the gate with her hand knotted in Ruhi's ruff and her back to a wall, and she is breathing like someone who has just been put somewhere with no trees.

"There's no *ground*," she says.

Away to the left, over the roofs, a bell starts up — and then another one, ragged, out of time with the first.


===== USER [2026-09-06T07:21:35.390Z] =====
Yeah. It’s all boats and barges and slipways here lass. Let’s get to the Pearl.


===== ASSISTANT [2026-09-06T07:22:31.246Z] =====
She learns it the way woodland people learn things: badly for ten minutes, then all at once.

The trick is the ledges. You keep her on the inside, hand flat on the wall, and after the third bridge she stops looking at her feet and starts looking at the water, and after the fifth she's reading it — which boat has right of way, which shout means *move*, which of the poled barges will take a passenger and which is somebody's home. Ruhi hates all of it and does it anyway, low and close, ears flat, a wet grey misery at your heel.

You take a ferry across the Lullwater because it's faster than three miles of ledge, and the ferryman charges you for the wolf and doesn't charge you for Gardwen, and won't explain why.

Everywhere, bunting. Tourney week. Bad wine on trestles and someone's cousin selling favours in di Teufel colours off a tray — dragon-scale green, three for a copper — and doing well at it.

The bells have stopped. Nobody you pass seems to know what they were for.

---

**The Pearl** is an island, and it is the loudest quiet place in the city. Narrow, tall, and clean in a way the docks are not: swept steps, scrubbed thresholds, lamps already lit at three in the afternoon because the alleys here never really get daylight. Music from somewhere above. Two women on a balcony watching the street the way farmers watch weather.

And halfway along a canal-side row, a green door under a carved lintel — a sylph, wings folded, worn nearly smooth by two hundred years of hands.

You knock the way you knocked twenty years ago, and the man who opens it is older than that knock remembers.

**Constantine.** Heavier now, grey through the beard, an apron over good clothes and flour on his hands from something he was doing in the back. He looks at you for a long moment without recognition, and then with it, and his whole face changes.

"*Magda.*"

"Constantine."

"You're not dead." He says it with genuine delight, as one professional to another.

"Not yet. It keeps being suggested."

He takes in the rest of it in one pass — the young woman standing too straight, the staff, the wolf — and to his enormous credit the only thing that moves is one eyebrow, and only slightly.

"Beds," he says. It isn't a question. "It's Tourney week, I've got the city and half the border in my lap and every room's spoken for—" He steps back and holds the door wide. "—so you'll have the top back room over the water, and it's cold, and the shutter sticks, and I'll bring a brazier up. Bring the dog. If it eats a client I'll take it out of your purse."

The hallway smells of beeswax and orange peel and, underneath, the honest fug of a house where a lot of people sleep. Somewhere up the stairs a woman is laughing at something, properly, not for money.

A girl of about thirteen goes past the foot of the stairs with an armful of linen twice her size, sees the wolf, stops dead, and drops the entire load.

"*Ila*," Constantine says, without heat.

She isn't listening. She's looking at Ruhi with her mouth open and her whole face lit up like a feast-day.

And on the landing above, leaning on the rail with her hair down and a cup of something in one hand, is a woman who does not appear to be in a hurry about anything, ever. Elven, tall, and put together in a way that makes you conscious of the ford-mud drying on your skirt.

"Constantine," she says down the stairwell, amused, "you've brought home a *wolf.*"

"I've brought home a *friend*, Emmeralda. The wolf is incidental."


===== USER [2026-09-06T07:27:26.694Z] =====
This is Gardwen. This is her first time in the city. We have some business to attend to. 

How are you? Last time I was here you looked exactly as you do now. The men still insane for you?


===== ASSISTANT [2026-09-06T07:27:54.552Z] =====
Emmeralda comes down the stairs the way water comes down stairs.

"This is Gardwen," you say. "First time in a city. We've business to attend to."

Constantine catches the weight on *business* and lets it go by without touching it, which is why you came to this house and not another. "Then you'll want the back room and no callers," he says, and goes to rescue his linen from the floor, and from Ila, who has not moved and is now sitting on her heels making an entirely serious attempt to introduce herself to a wolf.

Gardwen says, "Gardwen," to the room in general, and then, when Emmeralda reaches the bottom step and turns the whole apparatus of her attention on her: "—of the Ash Vale," which you suspect she has not said aloud in ten years.

"Emmeralda." She takes Gardwen's hand in both of hers, briefly, and gives it back. "You've walked a long way and someone's frightened you, and I'm not going to ask about either. Constantine will feed you first. He feeds people at them, it's how he argues."

Then she looks at you properly, and her face does something complicated and delighted.

"How are you?" you ask her. "Last time I was here you looked exactly as you do now. Men still insane for you?"

"*Magda.*" She laughs — it's a good laugh, low, nothing performed in it. "Twenty years, and you say that as though you've got a leg to stand on. Look at you." She reaches out and turns your chin with two fingers, unhurried, professional, examining. "Not one day. Not *one*. You were a hard old woman when I was a young one and you're the same hard old woman now, and I've had two decades of people telling me *my* face is unnatural."

"Mine's a curse."

"Mine's an *asset*." She lets go of your chin. "And yes. They are. Worse than they were, if anything — there's a fashion for elves this year, which means every merchant's son in the Merchant's Quarter thinks he's discovered something." She rolls her eyes toward the ceiling, toward the music. "It's tiresome and it's lucrative and I've stopped trying to explain the difference to Constantine."

"You've never once tried," Constantine says from the hall, arms full of linen.

"I've *implied* it."

She turns back and there's something under the brightness, just for a moment — she looks at you the way you looked at the customs man. Reading.

"You didn't come for the Tourney," she says.

"No."

"No." She accepts that, and files it, and doesn't push. "Well. The house is


===== USER [2026-09-06T07:27:54.555Z] =====
[Request interrupted by user]


===== USER [2026-09-06T07:30:34.782Z] =====
Continue


===== ASSISTANT [2026-09-06T07:30:54.293Z] =====
"Well. The house is full of border people this week and they tip badly and drink worse, so if your business needs quiet, take your supper upstairs and I'll see nobody puts a foot on your landing."

She says it lightly. It is not lightly meant, and you both know it, and neither of you marks it.

Behind her, Ila has got her hand flat on the floor about six inches from Ruhi's nose and is holding it there with the immense patience of the very young. Ruhi, who has had a long day and no opinions left, sniffs it once and puts her head back down.

Ila makes a small sound of pure private triumph.

"Ila," Emmeralda says without turning round, "if you are going to steal that animal, do it after you've taken the linen up."

"I'm not *stealing* it—"

"Take the linen up."

The girl goes, walking backwards for as long as the stairs allow.

---

Constantine brings it up himself, later: bread, a hard yellow cheese, half a cold fowl, a jug of the brown beer they make out on the Shoals, and a brazier that he sets going with a professional's economy of movement. The room is at the top and at the back, and the shutter does stick, and when you get it open the canal is directly below — close enough to hear the water working at the stone, and a barge going through in the dark with a lantern on its bow.

Gardwen eats like someone who has been rationing without admitting it.

"That woman," she says eventually, with her mouth full. "The elf. She was afraid of something."

You'd noticed. You hadn't been sure the girl had.

"Not of us," she adds. "Underneath. The way a doe is when there's nothing in the field. It's not a thing you can point at, it's just — the field's wrong."

She washes it down, and puts the cup on the sill, and looks out at the dark water and the lantern going away.

"Magda. I've got no plan. That's the truth of it. I've followed that column for three days on nothing but *keep them in sight*, and now they're behind a wall somewhere in this city and I don't know one street from another and I've a wolf that can't be seen and no coin left worth the name." Her jaw sets. "You said we'd plan. So plan at me, because I've nothing."

Down in the house, someone starts up on a stringed instrument, badly, and is shouted at, and gets better.

And down on the front step, three floors below, there's a knock — the sort a young man gives a door when he's certain of his welcome — and Constantine's voice, muffled, doing the warm professional thing he does.

Then, faintly, a young man's voice. Well-bred. Border vowels.

Asking, by name, for Emmeralda.


===== USER [2026-09-06T07:51:41.904Z] =====
Huh. Surreptitiously get a look at him. Quietly


===== ASSISTANT [2026-09-06T07:52:42.128Z] =====
You go down as far as the turn of the stair, where the landing overhangs the hall and the lamp doesn't reach, and you look down over the rail.

Seventy years and most of them spent moving quietly around animals — but the fourth step from the top has a voice, and you have forgotten it, and the house is not as loud as it was.

It creaks.

Not much. Enough.

---

You get your look first, though, and it's a good one.

Young. Twenty-two, twenty-three. Dark clothes, expensive and cut border-fashion, still carrying road-dust at the hem — he hasn't changed since he rode in. Handsome in the way that gets told to a boy early and often. He has his hood back and his hands out, palms up, doing the charm at Constantine, and Constantine is doing the warm professional thing back at him.

And it's all wrong.

He's too bright. Lit up. There's sweat at his hairline in a stone hall in the cold end of the afternoon, and his voice keeps going up at the ends where it shouldn't, and he laughs a half-beat before the joke is finished, twice.

His cloak hangs badly on the left. Something under it at the hip — not a sword; the hang is wrong for a sword, too short, and it sits too far forward. Something with a guard on it. And in the whole time you watch, his right hand goes to that place four separate times, and each time it comes away again, and he doesn't know he's doing it.

Beside you, low and quiet, Ruhi's hackles come up along her whole spine. She doesn't make a sound. She just goes very slowly to her feet, and puts herself between you and the stairwell.

Then the step creaks.

He looks up.

Straight up, fast, before the smile has time to be got back into position — and for about a quarter of a second what's on his face is naked and it is not fear of being caught out. It's *fury*. The flat outraged fury of something interrupted.

Then it's gone and the smile is on and he's a charming young man looking up at an old woman on a stair.

"Ah — forgive me," he says, and gives you a little bow, a real one, courteous as anything. Border vowels, well-bred, warm. "I didn't know the house had guests up. I've been rude."

Constantine, smoothly, without a flicker: "My old friend from the north, my lord. Deaf as a post and twice as stubborn. Pay her no mind."

"I would never." Still looking at you. Still smiling.

He holds it two beats longer than a man looking at deaf furniture has any reason to.

Then he turns back and the charm goes on to Constantine full-force, and his hand goes to his hip a fifth time.

"Now. Emmeralda. She's expecting me — I sent ahead, and I've paid for the whole evening, and I'd take it very kindly if we weren't disturbed."


===== USER [2026-09-06T07:55:16.506Z] =====
Ok. Back to Gardwen. Let’s get some sleep


===== ASSISTANT [2026-09-06T07:55:55.483Z] =====
You go back up.

Gardwen looks at your face and starts to ask, and you shake your head, and she lets it lie — which is a thing you file away about her.

"Young lord downstairs," you say. "Paid for the evening. It's a bawdy-house, lass. That's the trade."

"You don't like him."

"I don't like anybody."

She almost smiles. Then she takes the floor by the brazier without being asked, wraps herself in the cloak, and is asleep in about ninety seconds — the fast, total, unfussy sleep of someone who has spent a decade learning to take it wherever it's offered. Ruhi puts herself along the door.

You lie on the bed with your boots off and your staff under your hand where it always is, and you look at the ceiling.

The thing sits with you.

*The hang was wrong for a sword.* You have known a great many men to carry a great many things, and a man carries a knife on his belt in front when he means to get at it in a hurry and doesn't expect to be wearing a coat. And he had touched it five times, and he hadn't known he was doing it, and that is not a man carrying a weapon. That's a man carrying a *reason*.

And the fury. That quarter-second before the smile.

You think about going down. You think about what you'd actually say — *my lord, I don't like your face* — to a nobleman, in a house that isn't yours, on the word of an old woman who came in through the water-gate today without paying.

Constantine has run this house for thirty years. Emmeralda is not a girl. It is not your house and it is not your business and Hel did not walk you three hundred miles to mind a brothel door.

The music stops downstairs. The house goes quiet by degrees, the way houses do.

You go under.

---

You come up out of it on pure animal reflex, because Ruhi is already standing.

The wolf is at the door with her ears flat to her skull and every hair up and she has not made one sound, and *that* is what has woken you — not noise. The absence of it. The house holding its breath.

Then it comes.

It isn't a scream, at first. It's higher than that and there's no shape to it, and it goes on far past the length of one breath, and it is coming up through the floor from two storeys below.

Then it stops. Dead. Mid-note.

And in the ringing after it you can hear one thing, very clearly, in a young man's well-bred border voice, saying something fast and low and rhythmic that does not stop when the screaming does.

Gardwen is on her feet with her cloak half off and her eyes wide.

The brazier has burned down to almost nothing. Below, a door slams — somewhere on the canal side — and a woman starts shouting for Constantine, and then several people are shouting at once.

**Ruhi is scrabbling at the door.**


===== USER [2026-09-06T07:58:02.134Z] =====
Grab my staff. Get down there. FAST


===== ASSISTANT [2026-09-06T07:58:44.327Z] =====
You get the staff and you go, and you are seventy years old.

That's the whole of it. Nothing dramatic — you don't fall, you don't stumble. You just take the stairs at the speed a body takes them at the end of a long life, one hand hauling on the rail, and the turns are tight and the lamp on the second landing has gone out and it is *black*, and every second of it you can hear yourself not being fast enough.

Gardwen goes past you on the second flight. Barefoot, silent, taking them four at a time with one hand on the wall and the wolf pouring down ahead of her.

By the time you make the bottom, there are people in the passage — Constantine in a nightshirt with a lamp, two women, someone else's client with his boots in his hand — all of them crowded at a door that's standing open.

And the *smell* comes out of that room and hits you at ten feet.

Not blood, at first. Under the blood. Scorched hair and something sweetish and hot, like fat gone over in a pan, and something else beneath that with no name you have for it, something that makes the back of your throat close on its own.

Ruhi will not go through the door. The wolf is braced in the doorway with her legs locked and her head low, and she is snarling at an empty room.

Beyond her—

The shutter is off its latch and swinging, and there is cold canal air coming in, and three floors down you hear a boat take a man's weight badly and a pole go into the water.

That's it. That's all you get of him.

---

Emmeralda is on the bed.

She is opened from the hollow of her throat to her hip. One cut. It is not a slash and it is not a stab — someone has *drawn* it, slow, with something barbed, and the edges of it are wrong, and it is still moving, and the sheets have gone from white to black in a spreading and the black is running off the edge in a steady drip you can hear.

Her eyes are open. She is looking at the ceiling. Her mouth is working and no sound is coming out of it.

She is still alive. She should not be, and she is.

Gardwen is already on the bed with both hands flat in it, up to the wrists, and her head down, and she is saying something low and fast that is not any language you know — and every hair on your arms lifts, and the old cold horror of it goes through you like a spike, *magic, magic, it's magic*, and you hate it, you have always hated it, and you make yourself stand there.

"*Hold her*," Gardwen says without looking up. Her voice has gone flat and hard. "Magda. She's going to move and if she moves it opens wider. **Hold her.**"

Behind you in the doorway, Ila has got past the adults and has seen, and someone is trying to get her out and she is fighting them.


===== USER [2026-09-06T08:02:43.732Z] =====
Ok. Stop. 

You’re not playing this like a Mythras game. You’re narrating.

You should be making rolls every time we try to do something. I don’t immediately see that Emmerelda’s scared. That takes an insight roll. I don’t immediately lose him, I should have a chance of catching him.

The descriptive passages you’re generating are too long and putting words into my mouth for the sake of the story. 

This needs to be interactive. With a lot more open ended play


===== ASSISTANT [2026-09-06T08:03:06.703Z] =====
You're right on all three, and the second one is the real error — I let a failed Athletics roll close off the pursuit instead of just making it harder. That's me writing an outcome instead of running one. Let me fix the memory and then hand the moment back properly.


===== ASSISTANT [2026-09-06T08:03:22.982Z] =====
Rewinding to the live moment. He is **not** gone.

---

You're at the door. The shutter's swinging. Three floors down a boat rocks hard as a man drops into it, and a pole goes into the water.

The room stinks of scorched hair and something sweeter under it. Emmeralda's opened throat-to-h


===== USER [2026-09-06T08:03:22.983Z] =====
[Request interrupted by user]


===== USER [2026-09-06T08:04:09.265Z] =====
Pause the game while we fix this. Tell me all the rolls you’ve made so far this session


===== ASSISTANT [2026-09-06T08:04:37.550Z] =====
Game paused. Five rolls, all via the CLI:

| # | Moment | Skill | Roll | Target | Result |
|---|---|---|---|---|---|
| 1 | Hand into Ruhi's ruff | Survival | **12** | 63 | Success |
| 2 | Facing down the customs man | Willpower | **43** | 63 | Success |
| 3 | Creeping to look at the man at the door | Stealth | **90** | 68 | **Failure** |
| 4 | Observing him from the stair | Perception | **19** | 70 | Success |
| 5 | Getting down three flights | Athletics | **52** | 50 | **Failure** (by 2) |

That's all of them. Which is the problem — five rolls across an entire session.

**Where I should have called for rolls and didn't:**

- **Reading Gardwen at the ford.** "She's had a bad month and a worse decade… someone put that there." That's an Insight read. I handed it over as free narration and justified it to myself as "routine competence."
- **Emmeralda being afraid.** "Something under the brightness… she looks at you the way you looked at the customs man." Straight Insight result, never rolled, never your choice to attempt.
- **Worse — I laundered a second Insight read through Gardwen's mouth.** "That woman was afraid of something… the field's wrong." I had an NPC hand you a read you hadn't earned, which is the same error wearing a costume.
- **Constantine's reaction, the fishmonger's gossip, the customs man's "third lot today"** — all free intel. At least some of that should have been Perception, Insight, or Influence.

**And one I misapplied:** the Athletics failure. Failing by 2 on a flight of stairs means you arrive *late and winded* — it does not mean the attacker escapes and the scene is over. I used a failed roll to delete a choice, which is the opposite of what a failed roll is for.

One structural note: `roll-skill` returns results but doesn't write them to the journal, so the only record of those five is this transcript. I can make rolls persist as journal entries so you can audit any session afterwards — worth doing if you want the dice trail to survive the conversation.

How do you want to handle the restart — resume from the doorway with the pursuit genuinely live, or rewind further back?


===== USER [2026-09-06T12:36:18.275Z] =====
Record directions for die rolling and character actions in Claude.md

Let’s talk about offscreen actions. You should roll when NPCs perform their actions offscreen to see if their plans are successful. Record these in the fact database. This should never be a set narrative.


===== ASSISTANT [2026-09-06T12:37:05.461Z] =====
The directives belong in the **skill repo** so they apply to every campaign, not just this one:


===== ASSISTANT [2026-09-06T12:38:10.752Z] =====
Directives committed. Clock rewound to dusk. Restarting from the knock.

---

The brazier's going. Gardwen's eaten and is sitting with her back against the bed-frame, cleaning mud off her boots with a knife. Ruhi is asleep across the door.

Three floors down, a knock — brisk, three, confident.

Constantine's voice in the hall, too muffled for words. Then a second voice. Young, male, well-bred, border vowels.

It says a name you can hear clearly through the floor: *Emmeralda.*

Then the hall door closes and the house goes back to its noise — the stringed instrument, someone laughing on the second landing, water moving under the window.


===== USER [2026-09-06T12:39:58.121Z] =====
Sneak out to see and be stealthy about it. (Report back the die rolls as part of the game narrative)


===== ASSISTANT [2026-09-06T12:40:05.734Z] =====
**Stealth, Standard (68)** — the house is loud, which helps; the stairs are old, which doesn't.


===== ASSISTANT [2026-09-06T12:40:16.600Z] =====
**39 against 68 — success.** Solidly under. You get where you're going and nobody marks it.

---

Ruhi lifts her head as you step over her. You get the door shut without the latch speaking, and go down as far as the turn above the second landing, where the overhang puts you in shadow and the hall lamp doesn't reach.

From here you can see most of the hall below.

Constantine has his back to you. The young man is facing him — hood back, dark clothes, road-dust still on the hem. Nothing in his hands. He's talking, quickly, and Constantine is nodding in the way he nods.

Then Emmeralda comes into view from the parlour door. She's changed since the afternoon: hair up, something green. She says something. The young man laughs.

The three of them stand there a moment.

Then Emmeralda goes up the near stair — the one that comes past the second landing, twelve feet from where you're standing — and the young man follows her.

They'll pass below you in a few seconds.


===== USER [2026-09-06T12:41:54.453Z] =====
Am I hidden?


===== ASSISTANT [2026-09-06T12:42:05.047Z] =====
Yes. Your roll got you into position clean — you're in the overhang shadow, the lamp is below and behind them, and neither has looked up.

But that was for *getting there*. They're about to come up the near stair and pass within twelve feet of you, at which point staying put becomes a contested thing — your Stealth against whether either of them happens to look into the dark at the turn.

The shadow is good. It is not a wall.

You've got about three seconds to hold or withdraw.


===== USER [2026-09-06T12:42:34.375Z] =====
Withdraw- not my business


===== ASSISTANT [2026-09-06T12:43:02.096Z] =====
The night goes on. Somewhere below, a man who is not nearly as good at this as he believes attempts something he has never been trusted with.

**Santo — Lore (Demonology), Formidable (50 → 25).** His father does this work. He has watched.


===== ASSISTANT [2026-09-06T12:43:52.084Z] =====
You go back up. Gardwen doesn't ask. Ruhi resettles across the door and the house carries on being a house.

Some while later — an hour, maybe more — it goes wrong downstairs.

**Santo rolled 19 against a Formidable 25.** Whatever he came here to do, he did it.

**Then he rolled 100 to get out.**

---

There is no scream.

That's the first thing. What there is instead is a crash — something big going over, a table or a chest, and glass after it — and then a man's voice, high and completely undone, saying *no no no no* very fast, and then a door hitting a wall hard enough to shake the frame two floors up.

Running feet on the canal-side stair. A slip. A worse noise — a body hitting a landing full length and something metal skittering away across boards.

More running. A shutter thrown. And a splash in the canal below that is far too big to be a man getting neatly into a boat.

Then voices, all at once, all over the house. Constantine bellowing. Someone hammering on a door.

Ruhi is already up.

And under it all, from the room they went into: nothing at all.


===== USER [2026-09-06T12:44:57.330Z] =====
Your description is incomplete


===== ASSISTANT [2026-09-06T12:45:20.585Z] =====
Fair. You're three floors up in the back room and I left out where you're standing in it.

**The room.** Top floor, rear of the house. The shutter you unstuck this afternoon is still open a hand's width — and it gives directly onto the canal. That splash was not somewhere off in the city. It was more or less underneath you.

**The window** is four paces away. From it you'd have the water, the far bank, and whatever is currently in the canal.

**The door** is at your back, and Ruhi is on her feet in front of it with her hackles up, facing out at the stairwell — where the noise is. Three flights down between you and the hall.

**Gardwen** is already standing. She's got the boot-knife in her hand, held low and reversed, and she's looking at you, waiting to follow your lead.

**What you can hear now:** Constantine still shouting, no words in it. A woman crying somewhere on the second floor. Doors. Someone on the stairs coming *up*, fast, two at a time.

**What you can't hear:** anything at all from the room Emmeralda went into.

The metal thing that skittered across the boards did not go into the water.


===== USER [2026-09-06T12:46:29.095Z] =====
Get down to the waters edge - find the metal thing or the thing that made the splash


===== ASSISTANT [2026-09-06T12:46:46.532Z] =====
Down three flights in the dark, at speed, at seventy. **Athletics, Standard (50)** — a failure here costs you time and wind, not the trail.


===== ASSISTANT [2026-09-06T12:46:59.764Z] =====
**69 against 50 — failure.** Not a fall. Just the truth about seventy-year-old knees on a dark stair: slower than you want, and you arrive breathing hard.

---

You meet the one coming up at the second landing. It's **Ila**, barefoot in a shift, going flat out — she hits you rather than stops, grabs two fistfuls of your skirt, and her face is white all the way to the lips.

"She won't *open* it—" She's hauling at you, trying to turn you round, back up. "The door's shut and she won't open it and Constantine's got the bar out and Emmeralda *won't answer*—"

Gardwen goes past both of you toward that door without breaking stride.

Ila's hands are still in your skirt.

Below you, the canal-side stair keeps going down — past the boot room, to the water door and the slipway. Nobody's gone that way. Everyone in this house is going *up*, toward Emmeralda's room.

Down there in the dark it's quiet, and the water is still moving from whatever went into it.


===== USER [2026-09-06T12:48:38.275Z] =====
Go to the water. Prepare a slingshot


===== ASSISTANT [2026-09-06T12:48:58.622Z] =====
Ila's hands come off your skirt. You go down instead of up.

Boot room, then the water door — unbarred, standing half open, swinging. Whoever came through here left it that way.

You load as you go. Stone in the pouch, cord round the knuckles, staff cocked back along your forearm.

---

The slipway is four stone steps going down into black water, green and slick below the third. A skiff is moored to the ring at the bottom, riding oddly — the painter's still tied but the boat's been shoved out and drifted back, and it's rocking hard, more than the canal's doing.

The water directly off the slipway is still working. Not ripples — the deep slow turnover of something that went in heavy and recently.

It's dark. There's one lamp on the far bank forty feet off and the light off it lies flat on the surface, and under that surface you can't see anything at all.

Cold coming up off it. The smell of the canal.

No sound down here but water on stone, and the house shouting to itself three floors above you.

Something is on the second step down, right at the waterline — a shape that isn't stone.


===== USER [2026-09-06T12:49:59.303Z] =====
Grab it. Look out over the water. Find something to shoot


===== ASSISTANT [2026-09-06T12:50:13.175Z] =====
You get a hand on it and haul it up out of the water: a **cloak**. Heavy with canal, dark, good cloth, expensive — the hem still carrying road-dust under the wet. It was caught on the mooring ring. It did not come off a man who was being careful.

**Perception, Standard (70)** — scanning forty feet of black water with one lamp on the far bank.


===== ASSISTANT [2026-09-06T12:50:24.612Z] =====
**51 against 70 — success.** Under, and comfortably.

---

Thirty feet out and moving left, upstream, there's a wake — the fast ugly chop of somebody swimming badly and in a hurry. You get a head, and the pale smear of a face turning back toward the house, and then just the shoulders working.

He's making for the far ledge where the lamp is. There's a set of iron rungs up the wall under it. Forty feet of open water between him and them, and he's covered maybe a third.

He hasn't seen you. You're a shape in a dark doorway and he's looking at the upper windows, where all the noise is.

Your sling is loaded and the range is nothing.

Behind and above you the shouting changes pitch — somebody's got Emmeralda's door open.


===== USER [2026-09-06T12:50:58.973Z] =====
Kill whatever that is


===== ASSISTANT [2026-09-06T12:51:15.559Z] =====
Backlit against the far lamp, thirty feet, swimming hard. Dark water and a moving target.

**Berserker combat style, Hard (85 → 57).**


===== ASSISTANT [2026-09-06T12:51:22.031Z] =====
**33 against 57 — a hit.**


===== ASSISTANT [2026-09-06T12:51:49.039Z] =====
**8 damage. Head. No helmet — he's swimming. 5 hit points there; he's at −3. Serious wound.**

---

The staff comes over and the stone goes out flat across the water with that low buzzing note they make.

You don't hear it hit. You *see* it — the head snaps sideways, hard, wrong, the way a head does when it has stopped being steered from inside. The working shoulders stop working.

He goes under without a sound. No thrashing. No cry.

The chop where he was smooths out into ordinary canal, and the wake he'd been dragging catches up with the place he isn't any more, and there is one hand above the surface for a moment, open, not grasping at anything — and then that's gone too.

Forty feet away the lamp on the far bank goes on being a lamp. The iron rungs he was making for go on being empty.

The water closes and keeps moving.

---

Behind you, up in the house, a woman starts screaming — and this one doesn't stop. It's not Emmeralda's voice. It's older. There are words in it and you can't make them out.

Then Constantine's voice, cutting across it, shouting for someone to get a *light*, get a light down here—

And feet on the stairs above you. Coming down. Toward the water door.

You are standing on the slipway with an empty sling in one hand and a drowned man's cloak in the other.


===== USER [2026-09-06T12:52:59.410Z] =====
Look carefully through the cloak. Anything in it.


===== ASSISTANT [2026-09-06T12:53:10.623Z] =====
Wet wool, in the dark, with feet on the stairs above you. **Perception, Hard (70 → 47)** — you have moments, not minutes.


===== ASSISTANT [2026-09-06T12:53:26.814Z] =====
**62 against 47 — you don't finish.**

Outer pockets first, because that's where a hurrying man puts things: a few coins, a folded scrap gone to pulp in the canal, a lump of resin or wax.

Then your hands find weight. Something solid, sewn in behind the lining at the breast — small, hard, heavier than cloth has any business being — and there's no seam to it on the outside, and it needs a knife and a minute and light.

You have none of the three.

The door at the top of the boot-room stair bangs off the wall. Lamplight comes down the steps ahead of whoever's carrying it, swinging wild across the wet stone.

You're on the slipway. Empty sling in one hand, a drowned man's soaking cloak in the other, and thirty feet of flat black water behind you with nothing showing on it at all.


===== USER [2026-09-06T12:54:22.647Z] =====
Get inside. Bring the cloak. Head up to emmeralde’s room


===== ASSISTANT [2026-09-06T12:54:42.927Z] =====
You go up past the lamp. It's one of Constantine's men, and he's looking at the water and not at you, and he goes by without a word.

Second landing. Third.

---

Emmeralda's door is open and there are too many people in the passage. Somebody's holding Ila by both arms and she is fighting to get past, silently, which is worse than if she were shouting. An older woman in a shawl is against the far wall with her hands over her mouth — she's the one who was screaming, and she's stopped now, and she hasn't taken her eyes off the room.

Constantine is in the doorway with his back to you, not moving. Not going in.

Gardwen is inside, three paces from the bed, standing very still with her knife still reversed in her hand.

---

The room stinks of scorched hair and something sweet under it, and there's chalk on the floorboards — a worked figure, big, half scuffed through where someone stood in it.

The bed is soaked black from the middle down.

Emmeralda is sitting up in it.

She's opened from the hollow of her throat to her hip — one long deliberate cut, and it is still bleeding, and it is not being held closed by anything.

She has her head tilted slightly, and she's looking at the door, and she is smiling at Constantine.

"You needn't crowd," she says. Her own voice, perfectly level, pleasant. "It doesn't hurt at all."


===== USER [2026-09-06T12:57:05.905Z] =====
What the fuck? Look on in horror. Back out of there and open up the cloak.


===== ASSISTANT [2026-09-06T12:57:27.808Z] =====
You back out. Nobody notices — everyone in that passage is looking at the same thing.

Two doors down there's a linen closet with a lamp bracket. You get the lamp, put the cloak on the floor, and open it out flat.

Gardwen's knife would have been quicker but you're not going back in there for it, so you use the thumb-edge of your own belt knife and the stitching gives after a bit of arguing.

---

Two things come out of the lining.

The first is a **ring**. Heavy gold, a man's, big enough to want a knuckle. There's a device cut into the face: a beast coiled round on itself, long, with the tail through its own jaws. Good work. Old work. It's been sewn into a cloak by somebody who did not want it on his hand tonight.

The second is a twist of **oiled silk**, still dry inside. In it: a few long dark hairs, bound at one end with fine copper wire, and a flake of something brown and hard that isn't wax.

The hairs are not dark. In the lamplight they're dark red.

Emmeralda's are black.


===== USER [2026-09-06T12:59:12.168Z] =====
Take the ring. Evidence. Anything else in here?


===== ASSISTANT [2026-09-06T12:59:20.815Z] =====
Unhurried now, with a lamp and the lining already open. **Perception, Easy (70 → 105).**


===== ASSISTANT [2026-09-06T12:59:37.733Z] =====
**10 against 105 — critical.** You take the thing apart properly.

The ring goes in your purse.

Then, going through it seam by seam:

**The coins.** Eleven in all, and they're wrong for Purewater — heavier, older, a different mint. Border coin. He hasn't changed money since he arrived, which means he arrived recently and hasn't needed to.

**A tailor's mark**, stitched inside the collar where the wearer never looks. Not a Purewater house. The lettering's foreign to you, but the mark itself is a little tower with three windows, and it's been embroidered rather than stamped — that's a mark for somebody whose custom is worth the extra work.

**The pulped paper**, teased apart with the point of the knife and dried against the hot lamp glass. Most of it's gone to grey mush. Two things survive: part of a line in a fine clerk's hand, `—ee days before the Lady's Tourney, at the hou—`, and, lower down, the bottom half of a wax seal. Broken. The same coiled beast as the ring.

**And in the left cuff**, folded over twice and stitched flat so it wouldn't rattle: a **second twist of oiled silk**. Empty. Whatever was in it has been used.

The first twist — the one with the dark red hairs and the brown flake — has three more like it wrapped in the same bundle. All full. All hair.

None of it is black.

Whatever he came here to do tonight, he had the makings for four more.


===== USER [2026-09-06T13:00:50.961Z] =====
Ok. I have no idea what any of this means. Go find Gardwen


===== ASSISTANT [2026-09-06T13:01:05.091Z] =====
Back down the passage. It's thinned out — Constantine has got most of them moving, in the way a man does when he needs to not be looking at something.

Gardwen is outside the door now, with her back against the wall and her hands hanging. There's blood to both elbows. It isn't hers.

"I closed it," she says, when she sees you. Her voice isn't right. "Magda, I *closed it*. Both hands, everything I had, and it took — it went in and it *took*, the flesh came together, and then—"

She stops. Looks at her hands.

"Then it opened again. On its own. Not tore. *Opened*. Like a mouth."

Inside the room, quite clearly, in a warm and perfectly ordinary voice, Emmeralda is telling Constantine that he's fussing and that she'd like her green shawl, the one with the birds on it, because it's cold with the shutter open.

Gardwen looks at the wet cloak over your arm and the lamp in your hand, and her eyes come up to your face.

"Where did you go?"


===== USER [2026-09-06T13:03:17.740Z] =====
Lean in. Very quietly tell her. “I killed him in the water. Slingshot to his skull. Found his cloak too. He’s got all sorts of weird shit, look…”


===== ASSISTANT [2026-09-06T13:03:44.193Z] =====
Gardwen goes very still while you tell her. She doesn't interrupt.

**Gardwen — Insight (44)**, trying to make something of what's in your hands.


===== ASSISTANT [2026-09-06T13:03:58.630Z] =====
**96 and 82. She fails both.** She has woodland lore — animals, herbs, the shapes of living things. Nothing in her training touches this.

---

"Good," she says about the killing. Flat, immediate, no hesitation in it at all. Then, a moment later, quieter, as the rest of it arrives: "—and bad. Because someone paid for that cloak."

She takes the twist of silk and turns it under the lamp. Holds it a long time. Her jaw works.

"Hair and wire." She shakes her head, and there's something close to anger in it — at herself. "I know what a fever looks like in a badger. I know nine things you can do with willow. This is—" She hands it back. "I don't know what this is, Magda. I've never seen anything like it and I don't know anyone who has."

She looks at the four full bundles in your palm. Counts them, silently, her lips moving.

"Four more," she says. "Four more *what?*"

Then, past you, at the doorway — because inside the room Emmeralda has just asked Constantine, warmly, whether the young gentleman enjoyed himself and when he might call again.

Constantine hasn't answered.

Gardwen's hand closes on your wrist.

"That's not her. Magda, whatever's talking in there, it doesn't know he's dead. **We could ask it things.**"


===== USER [2026-09-06T13:04:23.042Z] =====
Insight is for emotions of people. Lore is for knowledge


===== ASSISTANT [2026-09-06T13:04:33.170Z] =====
Correct — and I should have checked rather than reached for the nearest skill.


===== ASSISTANT [2026-09-06T13:04:53.722Z] =====
Insight is INT+POW — reading people. Lore is INT×2 — knowing things. My Insight roll on the hair bundles was the wrong skill entirely.

Re-resolving it properly: analysing ritual components is **Lore**, and Gardwen's Lores are *Species* and two *Woodland Animal* specialisms. There's no roll to make — she has no applicable knowledge, so she simply doesn't know. The Lore (Species) roll was legitimate, and it failed at 82/52: she can't tell you whose hair that is, or even what it came off.

The result is the same. The reasoning was sloppy.

*(And she'd have needed an Insight roll to read Emmeralda — not the components. If you want that, it's yours to call.)*

---

Gardwen's hand is still on your wrist.

"That's not her," she says. "Whatever's talking in there, it doesn't know he's dead. **We could ask it things.**"

Inside, Emmeralda has moved on to asking Constantine why he's crying.


===== USER [2026-09-06T13:05:55.891Z] =====
Ok. Let’s go talk to her , or should I say IT…


===== ASSISTANT [2026-09-06T13:06:13.836Z] =====
Walking into a chalk figure and a smiling wound to ask it questions — with **Fear (Arcane Magic) 54** sitting in your chest.

**Willpower, Standard (63)** to keep your face still. Failing won't stop you going in; it means the thing gets to see what you are.


===== ASSISTANT [2026-09-06T13:06:29.351Z] =====
**42 against 63 — held.** Your hands want to do something and you don't let them.

---

Constantine is sitting on the edge of the bed with his face in his hands. He looks up when you come in, and whatever he sees in you makes him get up and move aside without being asked.

Close to, the chalk figure on the boards isn't a circle. It's longer than that — a shape with corners, and the scuffed break in it is at the foot, where a man standing inside would have stepped backwards out of it in a hurry.

The wound is the length of her. It doesn't clot and it doesn't run any more. It just sits there, open, moving very slightly with her breathing.

Emmeralda turns her head as you come in, and her face lights up.

"Oh, *Magda*." Delighted. Warm. Exactly the voice from the bottom of the stairs this afternoon. "You look absolutely *dreadful*. Come and sit."

She pats the coverlet beside her. There's blood on her hand.

Gardwen comes in behind you and puts her back to the wall, knife down at her thigh, and doesn't sit.

The thing in the bed watches you cross the floor and its eyes track a half-beat late — like someone driving a cart they've only just been handed.

"Constantine's being very silly," it says confidentially. "And that girl won't stop crying in the passage. Would you tell her I'm perfectly well?"


===== USER [2026-09-06T13:08:12.527Z] =====
You feel ok, lass? What’s all this though? 

Point to the wound.


===== ASSISTANT [2026-09-06T13:08:32.962Z] =====
It looks down at the wound the way you'd look at a stain on a good tablecloth. Mild puzzlement. No more than that.

"That." It touches the edge of the cut with two fingers, incurious, and the flesh moves under them like a curtain. "That's the way in. He wasn't very neat about it, but he got there in the end, bless him — he was *so* nervous, Magda, you've no idea. Shaking. I had to be kind to him."

The fingers come away red. It doesn't notice.

"Do I feel well?" It considers this seriously, as though nobody's ever asked. "I feel *marvellous*. I've been cold for — " a pause, and something goes across the face that isn't Emmeralda's expression at all, a sort of hungry blankness, and then it's gone and the warmth is back — "well. A long while. And this is a very good house and everyone in it is so *fond* of her."

It smiles at you. It's Emmeralda's smile. It's slightly too wide and it lasts slightly too long.

"He's coming back, you know. He said so. He was very definite about it." It plucks at the coverlet, arranging it over the ruin of itself, tidy, house-proud. "So we should have the room straight. And someone really ought to sweep up that chalk — it's *dreadful*, isn't it, he made such a mess of my floor."

Behind you Constantine makes a small sound.


===== USER [2026-09-06T13:10:32.219Z] =====
Yeah. We’ll clean up another room for you. Who is the young gentleman? So we know how tae greet him… on his return?


===== ASSISTANT [2026-09-06T13:10:55.137Z] =====
It brightens at being consulted about hospitality.

"Santo," it says. "Just Santo — he didn't give me the rest, they never do, they think it's clever." A little conspiratorial lean, and the wound gapes with the movement. "He'll want the green room, I should think. He liked the birds on my shawl."

Then, thoughtfully, arranging the coverlet again:

"He said he'd come back for the others. Four more, he said, and then his father would *have* to see. He was quite emotional about it." A small indulgent laugh. "Men and their fathers, Magda."

Behind you, Constantine has stopped making any sound at all.

When you look round, he's got both hands flat on the doorframe and he's holding himself up with them, and his face has gone the colour of tallow.

"*Santo*," he says. "He said *Santo*."


===== USER [2026-09-06T13:13:32.327Z] =====
Who the fuck’s Santo? Let’s get her somewhere else. Keep her comfortable… we need a priest or something 

Then talk to Constantine and Gardwen, privately


===== ASSISTANT [2026-09-06T13:13:54.502Z] =====
Constantine's people move her. She goes cheerfully, on her own feet, holding the coverlet round herself like a woman going to a fitting, and she thanks two of them by name and asks after somebody's mother. The older woman in the shawl won't go near her. Ila is taken downstairs, still fighting.

They put her in the green room and light the fire and leave the door open with a man sitting outside it who will not look in.

Then Constantine takes you and Gardwen into his counting room at the back of the house, shuts the door, and stands with his back against it.

"Priest," he says. "Yes. Yes, and *no*." He drags a hand down his face. "Magda. Sit down."

He doesn't wait for you to.

"**Santo di Teufel** is the son and heir of **Baron Hanzo di Teufel**, who rode into this city this morning with twenty-odd Dragon Knights at his back for the Lady's Tourney, and who is at this moment the guest of half the men on the Governor's council." His voice is very level and it is costing him. "The boy has a name on the border. The kind you hear and change the subject."

You put the ring on the table.

Constantine looks at it and does not touch it.

"That's their arms," he says. "The worm eating itself. It's on the litter, it's on the banners, it's on every second cup in this city this week."

He looks up.

"A priest means a report. A report means the Watch, and the Watch this week means the Governor, and the Governor is drinking with that man's *father*." He is quiet for a moment. "There is a dead di Teufel in the canal behind my house and a demon sitting up in my green room asking for her shawl, and there are nineteen people under this roof tonight."

Gardwen says, from the corner: "Twenty-two. There are three in the kitchen."

"Twenty-two." He closes his eyes. "What do we do?"


===== USER [2026-09-06T13:18:35.300Z] =====
He wanted to get four more. Show them the paraphernalia.

Let’s get the body and put it somewhere on the way here. Purewater thieves will kill a rich fool for his gold and jewelry quite happily


===== ASSISTANT [2026-09-06T13:19:00.697Z] =====
You put it all on the table under the lamp: four twists of oiled silk, the fifth one empty, the ring, the tailor's tower, the pulped paper with its half-line and broken seal.

Constantine looks at the hair for a long time.

"Not hers," he says. "Emmeralda's is black to the root."

"Four more," Gardwen says.

"Four more *women*." He sits down slowly. "There are eleven houses on the Pearl. And that boy has had the run of this city for one day."

---

On the plan, he doesn't hesitate.

"Yes. God help me, yes." He's already thinking, hands moving on the table. "It's the only story that holds. A rich border boy comes to the Pearl with his father's gold on him and doesn't know the water, and he's found in the morning face-down off the Shoals with his purse cut and his rings gone." He glances at the ring on the table. "You've already done the hard part of that."

Then he stops.

"But the body's in *my* canal, Magda. Behind *my* water door. And it went in heavy and it didn't come up." He works it through. "The outflow runs west past the Lullwater on the ebb — that's two hours off yet, and until then he's sitting on the bottom in about nine feet of water, more or less where you put him. After the ebb he could be anywhere, and 'anywhere' includes the grating at the Shoals, which they clear every morning with a *crowd* watching."

He looks up.

"So it's now, in the dark, with a boat and a hook and nobody who talks. Or it's not at all."

Gardwen is already pulling her cloak on.

"I can hold my breath a long time," she says. "I grew up on a river."


===== USER [2026-09-06T13:20:38.461Z] =====
Now it is. Let’s go find the little shit


===== ASSISTANT [2026-09-06T13:21:10.785Z] =====
Constantine's skiff, a boathook, a coil of line, and a shuttered lantern with the slide almost closed.

Nine feet of black. The canal moves under the boat in a way that makes it feel deeper than that.

Constantine works the pole and says nothing. He's put a sack in the bottom of the boat and hasn't explained it.

You're roughly over the spot — you can line it up off the slipway and the far lamp. Gardwen is already out of her cloak and pulling her boots off, and she's tying the end of the line round her own waist with a knot you don't recognise, and her hands are not quite steady.

"River," she says, mostly to herself. "It's just a river with walls."

The boathook is lying along the thwart by your knee. It's about eight foot, iron-shod.

Down there the water's gone the colour of nothing at all.


===== USER [2026-09-06T13:22:27.683Z] =====
Point her to where I think he was. Try to help


===== ASSISTANT [2026-09-06T13:22:37.728Z] =====
You put her on the spot — you watched him go down and you can line it off the slipway and the far lamp, and you can get her within a few feet of it. The line goes round your fist, twice, and braced.

**Gardwen — Swim, Easy (24 → 36)**, guided onto the mark with a line on her.


===== ASSISTANT [2026-09-06T13:22:52.276Z] =====
**88 against 36. She fails badly.**

She goes in clean enough — barely a splash, she's got that much from the river — and the line runs out through your fist in jerks.

Then it stops running.

Then it starts *thrashing*.

Whatever she grew up on, it did not have nine feet of black water, no bottom she can stand on, and cold that takes the air out of you on the way down. The line goes taut at an angle it shouldn't, snaps slack, goes taut again somewhere behind the boat. Constantine says something and drops the pole.

She comes up eighteen inches from the gunwale, not where she went in, and she is not swimming. She's climbing — hands scrabbling at the water like it's a wall — and she gets one arm over the side and hauls, and the skiff goes right over onto its beam ends with her weight on it.

Freezing canal comes in over the rail into the bottom of the boat.

She's got her chin on the gunwale and her eyes are enormous and she can't get any air in to say anything.

The line's still round your fist. The boathook's gone off the thwart into the bilge water. Constantine's got both arms out for the far rail trying to bring the skiff back level.

You've got about a second before she either comes over the side or takes the boat with her.


===== USER [2026-09-06T13:23:40.569Z] =====
Pull her back in


===== ASSISTANT [2026-09-06T13:23:47.833Z] =====
**Brawn, Standard (71)** — you're braced and the line's already round your fist.


===== ASSISTANT [2026-09-06T13:24:00.261Z] =====
**18 against 71 — a strong one.**

You don't pull her over the side. You pull her *along* it — one fist in the line and the other in the back of her shirt, dragging her aft toward the stern where the freeboard is lowest, and you take her weight off the rail and put it where the boat can carry it.

The skiff comes back down flat with a slap that throws water everywhere. Constantine sits down hard.

Then you get both hands under her arms and bring her in over the transom like a netted fish, and she lands in six inches of bilge and stays there on hands and knees, coughing up canal, shaking so hard you can hear her teeth.

It takes her a while.

"That," she says eventually, "is not a river."

---

The lantern's still lit. Constantine's got the pole back. Nobody in any of the dark windows along the canal has shouted anything.

Gardwen is soaked through, freezing, and no use to anyone in that water again tonight.

The boathook is in the bilge by your foot. Eight feet of it, iron-shod. Nine feet of water.

Constantine says quietly: "The ebb starts in less than two hours."


===== USER [2026-09-06T13:24:28.893Z] =====
How good am I at swimming?


===== ASSISTANT [2026-09-06T13:24:33.909Z] =====
**Swim 27.**

Worse than Gardwen's 24 is close enough to make no difference — you'd be going into the same nine feet of black with three points more skill and fifty more years. Whatever she just did, you'd do it harder.

What you're actually good at, in that boat: **Brawn 71** and **Perception 70**. The hook is eight feet and the water's nine — which is a foot short unless you're leaning, and it's a big canal to find one man in by touch.


===== USER [2026-09-06T13:25:21.172Z] =====
Constantine. How good a swimmer is Ila?


===== ASSISTANT [2026-09-06T13:25:36.315Z] =====
Constantine doesn't answer straight away.

He looks at the water, and then at Gardwen shaking in the bilge, and then somewhere past both of them.

"She's from the Shoals," he says at last. "Her mother worked the tide-flats before she came to me. Those children are in the water before they can walk." A pause. "She's the best swimmer in this house by a long way. She dives for lost oars for a copper. She once went under the *Lullwater* bridge on a bet and came up the other side, and I took the skin off her for it and she did it again."

He is quiet for a moment.

"She is thirteen years old, Magda."

Then, because he is not a stupid man and he has understood exactly what the question was:

"And she is downstairs right now, awake, being held by two of my women so she doesn't go and sit with Emmeralda, and if you go down and ask her to do this she will say yes before you've finished the sentence."

He turns and looks at you properly.

"She'll say yes because it's you asking, and because she thinks Emmeralda is hurt and this is helping. She won't know what she's touching down there until she's touching it."

The canal moves under the boat.

"That's the whole of it," he says. "It's your asking, not mine."


===== USER [2026-09-06T13:26:47.913Z] =====
Go get her. This’ll be good for her. She’d be doing something to help, not crying in a corner


===== ASSISTANT [2026-09-06T13:27:19.188Z] =====
Constantine goes himself. He doesn't look at you on the way past.

He's a while. When he comes back she's ahead of him down the slipway, barefoot on the wet stone, in the same shift with somebody's shawl over it, and her face is blotched and swollen from crying and absolutely lit up with purpose.

She's in the boat before anyone offers her a hand.

"I can go deeper than nine feet," she says immediately. "I can go under the *Lullwater*. Constantine, tell her—"

"I told her."

She looks at Gardwen, soaked and grey and shivering in the bilge, and something like pity crosses her face, and she is too well brought up to say what she's thinking about people who can't swim.

Then she turns to you, kneeling up on the thwart, hands already going to the shawl to shed it.

"What am I looking for?"

The far lamp is forty feet off. The water is entirely black. Constantine has both hands on the pole and is looking at the roofline.

Gardwen, very quietly, from the bottom of the boat: "Magda."


===== USER [2026-09-06T13:31:52.938Z] =====
Look here love. The man who hurt Em is down there, dead and drowned with a caved in skull. You’ve got to go down and hook his body so I can drag him out and put him somewhere so we don’t get in trouble.

I know it’s hard but you’re all we’ve got to make it right…  gardwen fuck help me explain. I’m no good at this


===== ASSISTANT [2026-09-06T13:32:16.856Z] =====
Ila goes absolutely still.

You watch it arrive — not the fear, that comes later; first just the arithmetic of it. *The man who hurt Em.* *Down there.* *Dead.* Her mouth opens slightly and doesn't do anything else.

"—caved in," she says.

"Aye."

"Who—" She stops. Looks at the boathook in the bilge. Looks at you. And you can see her working out that nobody in this boat is surprised, and that the old woman who came in today with a wolf is the one giving the instructions.

"*You* did it."

"Aye."

Gardwen gets up out of the bilge water.

She's still shaking and her lips are blue and she does it anyway — comes forward on her knees so she's down at the girl's level, not looming, and takes the shawl and puts it back round Ila's shoulders because the child has already half taken it off.

"Ila. Look at me." Her voice has gone quiet and completely steady, which it hasn't been all night. "When I was your age, men came to my house at night and killed my family. Every one of them. And I hid, because I was small and there was nothing else I could do, and I have spent ten years being the person who hid."

Ila is staring at her.

"Nobody's asking you to hide. There's a job, and you're the only one in this boat who can do it, and it's a *filthy* job." She doesn't soften it. "You'll touch him. It'll be cold and it'll be dark and he'll be heavier than you think and you will not like any part of it, and it will be over in a minute, and then Emmeralda's house stays standing and everyone in it goes on living here."

She puts the end of the line in Ila's hands.

"That's the whole of it. You can say no. I'd not think less of you, and neither would she."

The canal moves. Somewhere off toward the Lullwater a dog is barking.

Ila's fingers close on the line.

"Two tugs if I've got him," she says. Her voice cracks in the middle of it and she carries on anyway. "Three if I need to come up."

**Ila — Willpower, Easy (48 → 72)** to go over the side and stay steady down there.


===== ASSISTANT [2026-09-06T13:32:31.511Z] =====
**Willpower 44 against 72 — she holds. Swim 8 against 40 — barely off a critical.**

She goes in without a sound. No splash worth the name — she just tips backwards off the thwart and the water takes her and closes, and the line starts paying out through your hands smooth and steady, not in jerks.

It goes out a long way.

It stops.

Nothing for a count of ten. Nothing for a count of twenty. Constantine has stopped breathing in any useful way.

Then: two tugs. Firm. Deliberate.

Then two more, and the line goes heavy — properly heavy, dead-weight heavy, the whole thing coming taut across the gunwale — and you get your hands on it and Constantine gets his hands on it and you both haul.

She surfaces beside the boat with her arms wrapped round the line, gasping, hair plastered flat, and she is not looking at anything at all except the sky.

"His face is *up*," she says.

You get her in. She's cold as the water and she won't let go of the line even after she's in the boat.

And six feet down at the end of it, coming up out of the dark by degrees, there's a paleness that resolves into a young man's shirt, and then into a young man.


===== USER [2026-09-06T13:35:35.157Z] =====
Get him secure. The figure out with Constantine where to dump him with is ring and his cash so that someone else will steal it and get in the shit for doing so


===== ASSISTANT [2026-09-06T13:35:59.109Z] =====
He comes over the transom the way Gardwen did and takes three of you to do it. Young, soaked, and heavier than he has any right to be. The left side of his skull above the ear is a shape a skull should not be.

Constantine gets the sack over the head and shoulders, ties it at the waist, and doesn't look while he does it. Ila has her back turned and Gardwen has an arm round her.

Then Constantine sits back on his heels in the bilge water and thinks about it properly, and you can see the man who has run a house on the Pearl for thirty years come out.

"Right. Two ways, and they're not the same."

He holds up a finger.

"Leave the ring on him. Then whoever finds him strips him, and inside a day there's a Pearl thief trying to sell a di Teufel signet to a fence, and Crowbill's people hand that boy over to the Dragon Knights themselves rather than have the trouble — and it's finished, and it was never here." He grimaces. "But the moment that ring turns up, the Baron knows his son is dead. And a father who knows tears the city apart looking for the *why*."

Second finger.

"Keep it. Then he's a drowned foreigner with his purse cut, and he stays nameless for two days, maybe three, while the Baron's still expecting him at supper. That's time. But there's no thief in the story, and 'nameless drowned man' is a story the Watch stops believing the moment somebody comes asking after a missing lord."

He wipes his face.

"As for where — the **Lullwater**. Past the bridge on the north side there's a stretch of bad water and worse people, and men wash up there twice a month with their boots gone. Nobody would ask a single question." He hesitates. "Two hours' poling. And we'd be out on the canals with him in the bottom of the boat the whole way."

Ila is shaking hard now. She hasn't spoken since she came out of the water.


===== USER [2026-09-06T13:38:36.283Z] =====
Shrug. Keep the ring and the clothes and the cloak. How about we do this he’s never found?


===== ASSISTANT [2026-09-06T13:38:58.900Z] =====
Constantine looks at the sack for a while.

"Never found is harder than it sounds in a city that dredges itself," he says. "You weight a man and drop him in a canal, and in six or seven days the gas brings him up with the weights still on him, and then it isn't a drowning any more — it's a *murder*, and the Watch works murders."

He counts it off.

"So it's one of two. **Burn him** — and the only fires hot enough are the Forge Quarter's, which means a guild furnace, which means a guildsman who saw you and wants paying every year for the rest of his life." He shakes his head slowly. "I've watched a man be bled that way. It doesn't end.

"Or **the deep channel**, past the Shoals, where the harbour drops off into the sea. Opened so he doesn't float. Weighted. On the ebb, so what's left goes out and not back in." He glances at the sky. "The ebb starts in an hour and a half and runs about four. That's the window, and there isn't another one before it's light."

He looks at you steadily.

"That's an hour's poling to the harbour mouth in a boat with no light on it, past the Harbor Masters' pontoon, and out into open water in a skiff that is not built for it. If a patrol stops us we are three people and a corpse and there's no story that survives it."

He stands, and takes the pole.

"And I'd want the girl off this boat first. She's done enough, and she's freezing, and she should not see the next part."


===== USER [2026-09-06T13:39:00.907Z] =====
Make a quiet fuss over Ila too


===== ASSISTANT [2026-09-06T13:39:19.389Z] =====
You get her by the shoulders and turn her round, and you take the wet shawl off her and drop it in the bilge and put your own cloak on her instead — which swamps her entirely and smells of three weeks of road and pig, and is dry.

Then you rub her arms, hard, the way you'd bring a lamb round. Not gentle. Brisk enough to hurt a bit.

"Listen to me."

She looks up. Her teeth are going.

"You went into black water on the word of an old woman you met this morning, and you found what you were sent for, and you came back up and you *said the right thing first.* His face is up. That's what you gave us. That's the whole job." You keep rubbing. "I've stood beside grown men in worse than this who did none of it."

"I touched his—"

"Aye. You did. That'll come back on you tonight and probably tomorrow and then less after that." You pull the cloak closed under her chin and hold it there a moment. "It doesn't mean anything's wrong with you. It means you did a hard thing. There's a difference, and nobody tells you, so I'm telling you."

She makes a sound and folds forward against you, and you let her, and she cries properly for about a minute with her fists in your shirt.

Then she stops, because she's thirteen and mortified, and pulls back and scrubs her face with the heel of her hand.

"Emmeralda's still up there," she says.

"She is."

"Is she going to be all right?"

Behind you Gardwen doesn't say anything at all.

---

Constantine puts the skiff alongside the slipway. Two of his women are already at the water door with a blanket and a lamp, and they take her up between them, and she goes — looking back twice.

The boat feels very empty after.

Constantine takes up the pole and looks at you, waiting.

The ebb starts in an hour and a quarter.


===== USER [2026-09-06T13:43:32.635Z] =====
Smile to myself. Amateurs.

Do you know anyone who keeps pigs? Give me twenty minutes with a saw and I’ll have little old santo here as a nice pile of butchered meet we just feed to the pigs. Then he’s shit and no one’s the wiser


===== ASSISTANT [2026-09-06T13:44:04.035Z] =====
Constantine stares at you.

It takes him a moment to be sure you're serious, and then a moment longer to get past being sure.

"You're—" He stops. Starts again. "In my *house*."

"You've a boot room with a stone floor and a drain that goes straight into that canal," you say. "I saw it on the way down."

He opens his mouth and shuts it, because that is exactly what he has.

He turns and looks at the water for a long time. When he speaks again his voice has gone somewhere flat and far away.

"There's a hog-yard on the edge of the Shoals. Man called **Renko** — he takes the kitchen waste off four houses on the Pearl, mine included. Two carts a week, before dawn, and one of them's tomorrow." He is not looking at you. "He doesn't ask what's in the barrels. He never has. He's not a good man and he's not a talker, and he'd take coin to go on not being one."

He rubs his face with both hands.

"It's better," he admits, and hates it. "No boat. No Harbor Masters. No four-hour ebb window and no Lullwater. It's all *inside*, and it's done before the house wakes."

Then he looks at you.

"But it's hours, Magda. It's hours of it, in my scullery, with twenty-two people asleep over your head and a demon in my green room asking for her shawl. And in the morning I have to stand in that room and take delivery of my own bread."

Gardwen, quietly, from the stern: "I'll help."

Constantine laughs — one, no humour in it at all.

"Of course you will."

He puts the pole in and starts bringing the skiff back round to the slipway.

"There's a saw and a cleaver in the scullery," he says. "And a bone-tub. Don't ask me why I know where they are."


===== USER [2026-09-06T13:47:21.331Z] =====
Better inside in the quiet than outside for anyone to see. Let’s get on with it. Be a good chance to chat and think while we work.

Look at Gardwen. 

We killed one of the enemy tonight girl. That’s a good start


===== ASSISTANT [2026-09-06T13:47:45.424Z] =====
The scullery is stone from floor to waist-height, with a slate table, a drain in the corner, and a shuttered window that gives onto the canal. Constantine lights two lamps, puts the saw and the cleaver and the bone-tub on the table, says "I'll be in the counting room," and goes.

He doesn't come back.

---

You work.

It's not fast and it isn't hard. It's the same job it always is — you find the joint, you go through the joint, you don't fight the bone. The trick with a big carcass is patience and a sharp edge, and you have both. Gardwen holds what needs holding and turns what needs turning and doesn't flinch once, which does not surprise you at all.

The drain does its work. The canal takes it.

She doesn't say anything for a long while.

Then, when you tell her — *we killed one of the enemy tonight girl, that's a good start* — she stops with her hands on the table and looks down at the work.

"He's the right age to be one of their sons," she says slowly. "Not one of the men."

She turns a piece for you without being asked.

"Ten years ago he'd have been twelve. Sat at somebody's table while it happened. Getting told the story after, probably, and being proud of it." Her jaw sets. "So no. Not one of the ones who came. But he grew up into exactly what they wanted him to grow into, and he did *that* to Emmeralda with four more women's hair in his cloak, and I'd have put the stone through his head myself."

She wipes her wrist across her forehead and leaves a mark there she doesn't know about.

"It's a start," she agrees. "It's not the one I came for."

The saw goes on. Somewhere over your heads a floorboard settles, and both of you stop, and it doesn't come again.

"Magda." She's not looking up. "That thing upstairs said *his father would have to see*. See what?"


===== USER [2026-09-06T13:50:01.395Z] =====
I have no idea. Nothing good. 

What do you think. Is she possessed?


===== ASSISTANT [2026-09-06T13:50:21.819Z] =====
Gardwen takes her time.

"I don't know the word for it," she says at last. "But I know what I felt."

She sets down what she's holding.

"When I put my hands in her — Magda, healing isn't a spell you throw at somebody. You go *in*. You find the shape a body's supposed to be and you lean on it until it remembers." Her fingers work at a stain on the slate that isn't coming off. "So I went in. And the shape was all there. Everything where it should be, everything wanting to close, and it *did* close — I felt the flesh knit under my palms, that's not a thing you can be wrong about."

"And then?"

"And then something opened it again from the inside. Deliberately. Like a hand pulling a curtain back." She looks up. "It didn't fight me. That's the part I keep going over. It let me do the whole of it, and then it undid it, and I think—"

She stops.

"I think it *liked* it. I think it wanted to see what I'd do."

The saw again. A while.

"So yes. There's something in her that isn't her, and it's steering, and it's not stupid." She flexes her hands like they still hurt. "But whether she's gone or whether she's in there behind it — I've no idea. I've healed foxes and I've healed men and I've never once had a body argue back."

She wipes her wrist across her mouth this time.

"Somebody in this city knows what that chalk shape on her floor was. Somebody knows what four bundles of hair are *for*." Her voice hardens. "I'd like to find them before he does whatever the last one was practice for."

Above you, faintly, through three floors: a woman laughing. Warm and easy and delighted.

Neither of you says anything about it.


===== USER [2026-09-06T13:52:13.764Z] =====
After we’ve done this. Let’s go ask for someone who can make sense of what the fucker was trying to do. Can Constantine help? Does he know anyone?


===== ASSISTANT [2026-09-06T13:52:37.668Z] =====
It takes until the small hours. The bone-tub fills and Gardwen empties it into the barrels and you go on.

When it's done you scald the slate and the floor and the drain with three kettles, and the canal takes the rest, and Gardwen puts the saw and the cleaver back on their hooks exactly where they were, which is somehow the worst part of the whole night.

Four barrels. Constantine's own, with his own house-mark burned in the ends.

---

You find him in the counting room where he said he'd be. He hasn't lit a fire and he hasn't opened the ledger in front of him. He looks at your hands and then makes himself stop looking at your hands.

"Renko's cart comes at the fifth bell," he says. "That's under two hours. I'll walk it down myself, it's not the sort of thing you send a boy with."

When you ask him who can make sense of it, he thinks for a good while.

"Two names, and I don't like either of them.

"**Thorne.** Storyteller at the Moist Oyster — sits in the corner, buys nobody a drink, knows everything that has ever happened in this city and half of what hasn't. He was Order of the Lake before he wasn't, and they don't throw you out of that for nothing. If anyone can tell you what a chalk figure with corners is for, it's him." He grimaces. "But Thorne *trades*. He'll want the story, and he'll have it out of you sideways before you've noticed, and then it's his to sell. He's never yet sold one that hurt anybody. That's not the same as never."

He turns the ledger a quarter-turn on the desk.

"Or **Hesper.** Marisette's man. A real practitioner — not a hedge-witch, the genuine article, and he's seen things in this quarter that would turn your stomach. He'd know what that was on her floor at a glance." A pause. "But Hesper is Marisette's, and Marisette *rules* the Pearl, and if I send you to him then within the hour she knows there is a demon in my green room and a di Teufel dead in my canal."

He finally looks up.

"Which she is going to find out regardless, Magda. This is her island. I can hold it a day. I can't hold it two."


===== USER [2026-09-06T13:54:43.612Z] =====
Let’s go talk to the Queen then. She’d likely want to know who’s carving up girls and putting demons inside of them.


===== ASSISTANT [2026-09-06T13:55:43.583Z] =====
Constantine breathes out slowly, and some of the grey goes out of his face.

"Yes," he says. "Yes — *tell her*. If she hears it from you it's a report. If she hears it from anyone else it's a thing I hid from her." He's already moving, taking a key off his belt. "Bring all of it. She'll want to see, and she'll want to see it *first*, before there's a version going round."

The bundle goes together on the counting-room table: the signet, the cloak still heavy with canal, the shirt and the good dark coat, the eleven border coins, the tailor's tower stitched in the collar, the ruined letter dried flat against the lamp glass. And the four twists of oiled silk, and the fifth that's empty.

Gardwen washes to the elbow at the scullery pump and puts her cloak on over the state of her.

---

Outside, the Pearl before dawn is not asleep so much as between shifts. Lamps guttering. A man asleep in a doorway with his hat over his face. Two women going home along the ledge with their shoes in their hands, who look at the three of you and look away, professionally.

Constantine takes you four doors along and across a footbridge to a house that has no sign, no lantern, and a door of black wood with nothing on it at all.

He knocks. Twice, then once.

The man who opens it is the size of the doorway and does not ask who you are. He looks at Constantine, and then at the bundle under your arm, and then steps back.

"She's up," he says. "She's been up since the bells."

---

The room is small and warm and lined with ledgers, and it smells of coffee. There's a fire, and a desk, and a woman behind it in a plain grey wrap with her hair down and no jewellery on at all, and she is doing accounts by lamplight at four in the morning.

**Marisette** finishes the line she's writing before she looks up.

"Constantine," she says. "You've never once come to me before daylight."

Then her eyes go to you, and the bundle, and Gardwen behind you — and she puts the pen down.

"Sit," she says. "All three."


===== USER [2026-09-06T14:03:22.478Z] =====
Sit. I feel uncomfortable and out of place here. This is all very fancy


===== ASSISTANT [2026-09-06T14:03:43.438Z] =====
The chair is better than any furniture you have ever owned. There's a rug, and your boots are putting canal on it in a slow spreading arc, and there is nothing to be done about that. Somewhere behind you a clock you can't see is ticking in a way that sounds expensive.

Gardwen sits like a woman in a magistrate's court.

Marisette pours coffee into three cups without asking whether anyone wants it, and pushes them across the desk, and sits back.

She's older than the lamplight wants her to be. No paint on. She looks like a woman who has been doing sums for two hours and would rather still be doing sums.

"Right," she says. "Before you start.

"At about the third bell there was noise at your house, Constantine. A woman screaming, and then not screaming, which is worse. My man on the bridge saw your water door open and a light on the slipway, and your skiff out on the canal twice — once with three people in it, and once with four. He also says that on the second trip one of the four was Ila, and that she went in the water, and that she came out of it crying." Her hands are folded. "He came and told me because he knows I like Ila.

"So I have been sitting here for an hour and a half deciding whether to send men, and I decided I'd give you until dawn."

She looks at the wet bundle under your arm.

"You've got twenty minutes before I have to be someone else. Tell me what's in my island."


===== USER [2026-09-06T14:08:51.337Z] =====
Well, I’m not really one for talking…

But one of Emmerelde’s clients cut her up and cast some kind of spell on her. Now she’s been possessed by a demon - or fuck-knows-what… he was swimming away, so I killed him with a slingshot.

We got him out of the water afterwards and turned him into pigment for disposal. 

Now here’s the real shit

It was Hanzo di Teufels son. He was planning on doing this to four more girls and he wanted to show his dad.


===== ASSISTANT [2026-09-06T14:09:15.920Z] =====
Marisette does not move at all while you talk.

When you stop, she reaches out and turns one of the coffee cups a quarter-turn on its saucer, and that's the only thing that happens for about five seconds.

"Say the last part again."

"Hanzo di Teufel's son."

"Santo." She says it flatly, like checking a number. "Twenty-two, black hair, very handsome, laughs before the end of the joke."

"That's him."

"He came to my house three days ago asking after Asphodel and I turned him away because I didn't like his hands." She is completely still. "I sent him to *Constantine's*."

Constantine says, "Marisette—"

"Don't." Not sharp. Just closed.

She holds her hand out across the desk, and you put it all in front of her: the ring, the coat, the coins, the tailor's tower, the dried-out letter.

She goes through it like a woman counting stock. The ring she barely glances at — she turns it once and sets it down. The letter she reads twice. The coins she pushes aside.

Then she comes to the four twists of oiled silk, and she opens the first one with her thumbnail, and the copper wire and the long dark red hairs come out into the lamplight.

And Marisette stops.

She sits looking at it for much longer than she looked at anything else.

"Constantine," she says, and her voice has changed — it's gone very careful, the way you carry something full to the brim. "Who at your house has red hair?"

"Nobody."

"No." She lays the hairs down flat on the desk and separates them with one fingernail, four or five strands, precisely, the way you'd lay out evidence. "Nobody at mine either."

She looks up, and for the first time since you came in she isn't running the room.

"There are two women on this island with hair that colour, and I know them both, and neither of them works. One of them is a Watercrafter's daughter." Her jaw tightens. "The other is the High Priestess of the Lake Lady's own niece."


===== USER [2026-09-06T14:11:32.365Z] =====
Grunt. Chuckle inwardly. Look at gardwen and nod my head to encourage her to tell her tale. Now’s the time to tell the queen


===== ASSISTANT [2026-09-06T14:11:53.460Z] =====
Gardwen looks at you. You nod at her.

She puts her cup down, and she doesn't touch it again, and she tells it the way she'd give a report — no shape to it, nothing arranged, which is somehow the worst way to hear it.

"Ten years ago men in dragon-scale came to my family's steading at night. There were nine of us. I was eleven. They fired the house and they killed everyone in it and I lived because I was small and the woods took me." She's looking at the edge of the desk. "In the morning I went back and I counted them. I counted them all. My brother wasn't there.

"He was seven. They'd taken him alive, and they'd taken *only* him, out of nine people, and they burned the rest so nobody would count.

"I've been walking since. Ten years. I've picked up that colour of scale in four different territories and lost it again every time." She swallows. "Three days ago I found a column of them on the north road going somewhere at last instead of nowhere, and I followed it here, and this morning it went through the gate ahead of me. Di Teufel colours. Twenty-odd men and a covered litter with the curtains sewn shut and the guards facing *in*."

She finally looks up at Marisette.

"I don't know what your city's for. I don't know what a demon is. I came here for one thing." She says it without any heat at all. "That boy in the canal said his father would *have to see*. See what he'd made. That means his father makes things too. And his father has had my brother for ten years."

Nobody says anything.

Marisette sits back in her chair. She looks at the hair on her desk, and the ring, and then a long while at Gardwen.

"A litter," she says slowly. "Curtains sewn shut. Guards facing inward."

"Aye."

"He entered a champion for the Single Combat." Marisette's fingers have gone still on the desk. "Nobody has seen the man. It's been the joke of the week — the Baron's mystery swordsman. Not one soul in this city has laid eyes on him, and he's been inside that estate since the moment they arrived."

She looks up.

"How old would your brother be now?"


===== USER [2026-09-06T14:13:11.565Z] =====
Grunt. Chuckle. 22 you said, right?


===== ASSISTANT [2026-09-06T14:13:35.379Z] =====
"Seventeen," Gardwen says.

It comes out of her flat and immediate, the way a number does when you have counted it every year for ten years.

"He'd be seventeen. Santo was twenty-two." Her hands have gone white on her knees. "It's not him."

"No," Marisette agrees. "It isn't."

She lets that sit exactly long enough.

"But a champion nobody has seen is not a champion. It's a *thing being kept*." She picks the ring up again, finally, and turns it over. "Men who are proud of a swordsman show him off. You parade him at the Siren's Call, you let the odds move, you take money off the Guilds. That is the entire point of entering one." She sets it down. "Hanzo di Teufel has not let a living soul look at his. He has him behind a wall and a litter with the curtains stitched, and his guards face inward — you don't face inward to keep people out, you face inward to keep something *in*."

Gardwen has not moved.

"Seventeen is young for the Single Combat," Marisette says. "It is not too young. I have seen younger die in it."

The clock behind you goes on being expensive.

"I'm not telling you it's your brother, girl. I've no idea and neither have you and I'd not have you break yourself on a hope." She says it almost gently, which from her seems to cost something. "I'm telling you that the thing in that estate is being hidden, and the boy who came out of it was carving women up to impress his father, and that his father is at this moment three streets from the Governor with a demon-worker's blood in him and an entry in the Lady's own Tourney."

She stands.

"Which makes it my island's business now, and I don't have twenty minutes any more."


===== USER [2026-09-06T14:17:21.315Z] =====
Thanks for your time, Milady.

Emmerelde’s going to need some help and, sorry to say that I’ve no idea how to fix that. 

Shudder.

Anything else we can help you with? If there’s fuckery to be had with the good baron, I’d be up for it.


===== ASSISTANT [2026-09-06T14:17:51.260Z] =====
Marisette looks at you for a moment — properly, the way she looked at the hair.

"Who are you?"

"Magda. I keep pigs."

"Mm." She doesn't smile. "You killed the Baron's heir with a sling from a doorway in the dark, at what — thirty feet? — and then took him apart in a scullery and had him in barrels before the fifth bell." A beat. "You keep pigs."

"Aye. And other things."

She accepts that. She writes something in the ledger, one line, and blots it.

---

"Right. Three things, and then you're going to sleep, because you're no use to me grey.

"**Emmeralda.** I'll have Hesper at Constantine's within the hour — he's mine and he's the real thing and he's the only man on this island who'll know what that chalk was. You'll not fix her and neither will I. He might tell us what's *in* her, which is where fixing starts." She glances at Constantine. "And he'll come quietly and he'll come as a physician, because I'm not having the word *demon* on this island before I've decided who gets to say it.

"**The two women.** That's mine as well. One's a Watercrafter's daughter and one's the High Priestess's niece, and I can get word to both without explaining why, and I will, this morning." She taps the hair. "Whoever they were for, they're not getting them now.

"**And the Baron.**"

She comes round the desk. Up close she is not a large woman at all.

"You asked if there's fuckery to be had. There is, and I can't do it. Every face I own is known on this island — my people can't get within a street of that estate without it being reported to somebody by noon." She looks between you and Gardwen. "You two walked through the water-gate yesterday morning. Nobody in this city knows your names. That is worth more than anything else you've brought me tonight.

"So: sleep. Eat. And this afternoon I want to know what is behind that wall — how many men, what gates, and whether anyone in that household has ever seen the champion's face." She holds your eye. "Not a rescue. Not a fight. *Looking.* You come back and tell me, and then we decide."

She goes back round the desk and sits, and picks up her pen.

"Constantine will give you money. Take it, don't argue, it's not kindness — I don't want you noticed, and you both look like you've slept in a ditch."

Then, without looking up:

"And when you find out whether that boy in the litter is seventeen, Gardwen — you come to me before you do anything about it. Not after."


===== USER [2026-09-06T14:19:57.854Z] =====
Nod. Grunt. Chuckle. Leave. Sleep


===== ASSISTANT [2026-09-06T14:21:07.082Z] =====
You sleep like the dead until well past noon.

---

What you wake to:

**Constantine** has put a purse on the table by the bed — more than you expected, and a fresh shirt for Gardwen that fits nobody. He's had two hours' sleep and looks it. Four barrels left with Renko's cart at the fifth bell and nobody remarked it.

**Emmeralda** is still in the green room. She has spent the morning asking pleasantly after people and requesting things — the shawl, a mirror, the window open — and being given none of them. She has not once tried the door. The man sitting outside it has been changed twice because they can't stand more than a few hours of it.

**Hesper** came at the second hour after dawn, as promised, in a physician's coat with a physician's bag. He is still here. He has been in that room for three hours and has not come out, and Constantine's people have stopped going up that stair at all.

**And on the Pearl**: di Teufel men. Not knights — servants, in good livery, in twos, going house to house since mid-morning. Polite. Asking whether anyone saw a young gentleman of about twenty-two, dark, well-dressed, on the night before last.

Constantine has already been asked. He said no.

They're still working the island. They have not come back to his door.

Gardwen is at the window with the shutter cracked, watching two of them work the far side of the canal.

"Afternoon's going," she says. "She wanted us at that wall today."


===== USER [2026-09-06T14:58:55.743Z] =====
Let’s go have a look


===== ASSISTANT [2026-09-06T14:59:39.674Z] =====
Gardwen leaves Ruhi with Ila, which solves two problems at once — the wolf can't walk the Merchant's Quarter unmuzzled, and the girl has something to do with her hands. When you go, Ila is sitting on the scullery step with her arms round the animal's neck and doesn't look up.

---

Nobody has to tell you where to go. You can see it from the second bridge.

**High Isle**, eastern side, seaward — and above the roofs of the **Forge Quarter** there's a column of dark smoke from the furnaces, and standing separate from it, lower down at the waterline, a long flat streak of white.

Steam.

It comes off the water in a continuous sheet for a hundred feet along a private pier, and it does not stop, and there is no fire under it.

The thing at that pier is a **ship**. Not a barge in the Purewater sense — a deep-water vessel, dragon-prowed, black-hulled, high out of the water and completely out of scale with the little canal traffic around it. It's moored bow-in with its stern to the open channel and the Mouth beyond, which means it can leave at any hour without turning.

Where the hull meets the water, the water is boiling.

Gulls won't go near it. There's a dead-water slick around the stern with things floating in it belly-up.

---

You come at it along the yards, which are working: coopers, a rope-walk, a chandler, men moving timber. Nobody stops you. Two old women — or an old woman and a young one — walking through a working yard in the afternoon are furniture.

From the corner of the last cooperage you can see the whole pier.

**Two Dragon Knights at the pier head**, in scale, bored, one sitting. **A boarding ramp** with two more at the top of it. Movement on deck. A covered gangway aft with canvas laced down both sides so nothing can be seen going along it.

And roughly amidships, well above the waterline, one **shuttered port** with the shutters closed on a bright afternoon.

Forty yards of open cobble between you and any of it.


===== USER [2026-09-06T15:05:05.919Z] =====
What’s a good cover story for us to be there?


===== ASSISTANT [2026-09-06T15:05:16.481Z] =====
**Perception, Standard (70)** — watching a working pier for a while to see what actually goes on and off it.


===== ASSISTANT [2026-09-06T15:05:34.443Z] =====
**49 against 70.** You stand in the lee of the cooperage for the better part of an hour and watch what a ship actually needs.

Not much goes *on*. That's the first thing. No provisioning carts, no chandler's boy, no water butts — which for a vessel that size at a pier is strange, until you notice the covered gangway and understand they're bringing everything aboard where nobody can see it, in their own hands, from their own boat.

But things do come **off**.

- **Slops.** Twice while you watch, a knight carries a covered pail down the ramp and empties it into the dead water at the stern. Nobody's collecting it. Nobody's being paid to.
- **Laundry.** A woman came at the second bell with a barrow, took a bagged load from the pier head — not from the deck, from the *pier head*, handed down to her by a knight who didn't let her past the bollards — and went away again toward the rope-walk.
- **Ash and clinker**, in barrows, from somewhere below decks, tipped into a spoil heap at the end of the yard. Far more of it than a galley fire makes.
- And a **cooper's boy** delivered four new barrels to the pier head, left them, and was waved off. The knights carried them aboard themselves.

Nobody who is not a Dragon Knight has been past the bollards all afternoon.

The laundry woman is the only person who has been spoken to at all. She was there and gone in under two minutes, and the knight who handed the bag down said perhaps four words to her.

Meanwhile: nobody in this yard has looked twice at either of you. There's a hog-man's cart at the far end taking waste off the cooperage and the rope-walk right now — an old nag, two barrels, and a lad who is not paying attention to anything.


===== USER [2026-09-06T15:07:47.474Z] =====
How do they eat? Any food supplies?


===== ASSISTANT [2026-09-06T15:08:12.494Z] =====
Nothing goes aboard by cart. Not a sack, not a crate, not a water butt — and you've been watching long enough now to be sure of it.

But there's a **ship's boat**.

It came round the point from the north-west while you were watching, four men rowing, and went in under the covered gangway aft where you can't see what happened. It left again riding higher than it arrived. Then it came back a second time, an hour later, the same way.

North-west round that point is High Isle proper — the good streets, the leased houses, where a border baron with money would take a place for the tourney and stable his horses and put his knights.

So: the ship isn't provisioning itself off this yard because it's being fed from a house. Their own boat, their own men, in under the canvas.

And here's the thing you can count. Two boatloads. Four men rowing each time, and what they carried came off the thwarts in a few armloads.

That is not victualling for twenty-odd Dragon Knights. That's food for a handful.

Whatever's on that ship, there aren't many of them aboard it.

At the far end of the yard the hog-man's lad has started backing his nag round, ready to go. He's making a mess of it.


===== USER [2026-09-06T15:09:09.270Z] =====
Go over there and help. I know all about hogs


===== ASSISTANT [2026-09-06T15:09:23.963Z] =====
**Survival, Standard (63)** — you've been getting stubborn animals to do things for fifty years.


===== ASSISTANT [2026-09-06T15:09:46.318Z] =====
**78 against 63 — the horse is not impressed by you either.**

You go to its head talking the way you'd talk to any bad-tempered old nag, and it lays its ears flat and swings its quarters, and the offside wheel goes into the spoil heap and the cart tips enough to put one of the barrels over on its side. The lid stays on. Mostly.

The lad says a word you'd have clipped him for.

Then you both spend a couple of minutes getting the wheel out, and you get your shoulder under the barrel while he rights it, and by the end of it you're both filthy and he's stopped being embarrassed.

"She does that," he says, glaring at the horse. "Every time. Every single time, right at the end."

"She's testing whether you've noticed her."

"I've *noticed* her—"

"No, lad. She wants you to go to her head *before* she starts, not after."

He considers this with the deep suspicion of a fifteen-year-old being told something obviously true.

His name's **Pell**. He does the Forge Quarter yards on alternate days for Renko out on the Shoals — which you keep your face entirely still about — and he complains at length and with real feeling about the rope-walk, who put nails in their waste last month.

Then, while he's roping the barrels down, he jerks his chin down the pier at the steaming black hull.

"Not that lot, though. *They* don't give us nothing."


===== USER [2026-09-06T15:10:57.291Z] =====
Tight bunch, are they?


===== ASSISTANT [2026-09-06T15:11:18.024Z] =====
"Tight?" Pell hauls the rope through and pulls it down with his whole weight. "They're *unnatural*, is what they are."

He counts it off, aggrieved, the way you complain about a bad customer.

"Every yard on this side gives us their waste. Cooperage, rope-walk, chandler, even the furnace lads give us their bones. That's how it *works* — we take it away, they don't have it stinking, everyone's happy, Renko's hogs get fat." He gestures down the pier with the rope-end. "That lot tip it in the water. In the *water*, right off the stern. Good scraps, meat and all, I've watched them do it. Straight in."

He shakes his head at the criminality of it.

"Renko went down there himself first day. Offered to take it for nothing — for *nothing*, mind, just to have it — and they walked him back up the pier by his elbows and told him not to come again."

He gets down off the wheel.

"And the ash. They've been carting ash off that ship since the day it tied up, barrows of it, and you show me the galley fire that makes that much clinker in a week. Furnace lads have been laughing about it. Reckon they're burning green timber down there."

He wipes his nose on his wrist.

"Only one that gets anything off them is the laundry woman. **Yannick's wife** — does the rope-walk and the chandler and now them. Bag down at the bollards, coin in her hand, off you go. She's not allowed past neither." A shrug. "She won't talk about it, though. Went right off, she has. Won't say a word about that ship."

He starts leading the nag out.

"Which is a shame, 'cause she'll talk about anything."


===== USER [2026-09-06T15:13:02.667Z] =====
Huh. How big is the bag? Is there a lot of laundry?


===== ASSISTANT [2026-09-06T15:13:19.249Z] =====
Pell stops and actually thinks about it, which he clearly hasn't before.

"Not big," he says. "One bag. She carries it on the barrow but she could carry it on her hip if she wanted — I've seen her lift it one-handed off the bollard."

He frowns.

"Every day, though. That's the thing, now you say it. Rope-walk's forty men and they send out twice a week. That ship sends out *every day* and it's one bag."

He clicks at the horse.

"And it's all the same, she said once before she went quiet on it. Not shirts and hose and what-have-you like a normal house. All the one thing." He shrugs. "Sheets, I suppose. Bedding."

He's got the nag moving now, and he says the rest over his shoulder, cheerfully, with no idea what he's handing you:

"She had a right go at Renko about it in the tavern, first week. Said she'd take their coin but she'd not take it long, and if they wanted that much *boiling* every day they could get a woman with a stronger stomach."

He raises a hand.

"Alternate days, missus! Tell Renko I said you know your horses!"

And he's gone up the yard, and the cart lurches, and the nag does the thing with her quarters again exactly as predicted.


===== USER [2026-09-06T15:15:11.998Z] =====
Boiling? Look at the boat. How many people do we see on the decks? Any sign of the baron? Any sign of the knights?


===== ASSISTANT [2026-09-06T15:15:21.373Z] =====
**Perception, Standard (70)** — counting properly this time, not just watching.


===== ASSISTANT [2026-09-06T15:15:36.509Z] =====
**70 against 70.** Right on the number. You get your count.

**Eight.** That's all of them.

Two at the pier head. Two at the top of the ramp. Three working on deck — coiling, carrying, one on the quarterdeck who doesn't do anything but walk the same twenty feet over and over and look at the shore. And one who came up out of the aft hatch with a barrow of clinker, went down the ramp, tipped it on the spoil heap, and went back.

Eight men. In scale, all of them, on a hot afternoon, aboard a moored ship. Nobody in shirtsleeves. Nobody idle. Nobody talking.

**No banner at the masthead.** For a nobleman in residence there'd be colours flying — every other vessel in this harbour with anybody aboard has something up. That mast is bare.

**No Baron.** Nobody in anything but scale and livery. No servants, no clerk, no valet, nothing that looks like a household. The good clothes and the gold are somewhere else — north-west round that point, where the boat goes.

And the shutters amidships have not opened once all afternoon. It has been a warm bright day, every port on every hull on this water is open to air the ship out, and those are closed and — now that you look properly at them — they're closed from the *outside*. There's a bar across.

Gardwen has gone very quiet beside you.

"Magda," she says. "Sheets. Every day. Boiled."


===== USER [2026-09-06T15:19:43.721Z] =====
Shrug. So what? Some kind of infestation? 

Go talk to Yannick’s wife.


===== ASSISTANT [2026-09-06T15:20:02.158Z] =====
The wash-house is behind the rope-walk: a low brick shed with the doors open and steam rolling out into the yard, three coppers on the boil, and lines of other people's linen strung the length of it.

**Yannick's wife** is alone in there, up to her forearms, moving washing between coppers with a wooden paddle. Fifty-odd. Arms like a cooper's. The heat in that room is enormous.

She looks up when your shadow falls across the door and doesn't stop working.

"If it's for the rope-walk you're a day early."

Behind her, on the end copper — the one furthest from the door, on its own — there's a load going that isn't like the others. She's got the lid half over it. The water in it has been changed recently; there's a grey slick round the rim where it was tipped out, and the drain channel by her feet runs the wrong colour and hasn't been sluiced.

There's a stack of clean folded sheets by the door with a cloth over them, ready to go back.

The cloth doesn't cover the corner of the top one, and that corner has a stain in it that has been boiled at and hasn't come out. It's gone the brown that blood goes when you cook it into cloth.

She's watching you look.


===== USER [2026-09-06T15:21:25.425Z] =====
Just sit like an old woman sits and see if she’s up for some gossip


===== ASSISTANT [2026-09-06T15:21:43.497Z] =====
You come in out of the sun, take the bench by the door where the draught is, and sit down the way a woman of seventy sits down — all at once, with a noise.

Then you don't say anything.

You look at your boots. You rub your knee. The steam is actually pleasant on the joints and you say so, once, to nobody.

Gardwen, who has understood, stays outside in the yard with her back to the wall.

The paddle goes on. Copper, lift, turn, copper.

She's been holding this for four days with a husband who doesn't want to hear it and no one else to tell.

**Yannick's wife — Willpower (55) to keep it in.**


===== ASSISTANT [2026-09-06T15:22:00.932Z] =====
**66 against 55 — she fails to keep it in.**

It takes a long while. You get most of the way through not-asking before it happens.

She lifts a load, drops it, wipes her forehead with the back of her wrist, and says — to the copper, not to you:

"Do you know what boiled blood smells like?"

You say nothing.

"'Course you do. You've a face like you've buried people." She goes on paddling. "Four days I've had that. Every morning. One bag, and it's all sheets, and every one of them's the same."

Copper, lift, turn.

"It's not a wound. I've done a house with a consumptive in it, I've done a birth-bed, I've done a man who lost a hand at the rope-walk. You get a shape to it — where it came from, how it lay, whether he thrashed." She finally looks at you. "This is the *same shape* every day. Same place on the sheet. Same size. Like it's been let out of him careful, in the same spot, and mopped, and put back."

She jerks her chin at the end copper with the lid half on.

"And there's something else in it that doesn't come out. Not blood. Blood boils out with lye and time. That doesn't." Her mouth goes thin. "It goes *grey*, and it smells like the forge, and my hands were numb to the elbow the first day and I've worn gloves since."

She puts the paddle down.

"They pay double. My man says take it. And I lie there at night thinking — whoever's in that ship, he's still bleeding tomorrow. Four days. Somebody's keeping him alive to do it again."


===== USER [2026-09-06T15:24:22.307Z] =====
Hmmmm… that’s very strange… from what I hear, they’re all a bit odd in there. 

Got to do the work to get paid though … 

try to look sympathetic 

Crack a joke


===== ASSISTANT [2026-09-06T15:24:32.648Z] =====
**Influence, Easy (18 → 27).** Warmth is not what you're built for.


===== ASSISTANT [2026-09-06T15:24:52.100Z] =====
**54 against 27.** No.

You arrange your face into something sympathetic. You've seen other people do it. It is not a thing your face knows how to be, and what it produces is closer to indigestion.

And the joke — *at least it's honest work, most folk pay double to keep blood off their sheets, not on* — is the sort of thing that's funny in a byre at four in the morning with people who've been up all night with a bad calving.

It is not funny in a wash-house.

It lands in the steam and dies there.

Yannick's wife's face closes like a door.

She picks the paddle back up. The rhythm changes — shorter, harder, the movements of a woman who has remembered she's working.

"You're not from the yards," she says.

Not hostile. Worse: careful.

"You came in with a young one who's stood outside my door instead of coming in, and you sat down and let me talk, and you've asked me nothing, which is how the Watch does it and how Crowbill's do it and how a certain sort of woman from the Pearl does it." She doesn't look up. "And now you've made a joke about blood."

Copper. Lift. Turn.

"So I'll ask, since you won't. Who are you, and why do you care what's in my coppers?"


===== USER [2026-09-06T15:31:38.354Z] =====
No. Not from here. I’m from the north, where the winds are cold and the ice is sharp. I joke about blood because I’ve seen and cleaned up my fair share and I’m interested because the men on that boat are up to some evil shit that might need stopping.

Sounds like you’re thinking the same way… 

But other than that, I’m just a tired old woman stretching my limbs here


===== ASSISTANT [2026-09-06T15:32:07.766Z] =====
Not a retry of the joke — a different move entirely. And since you're telling her the plain truth, the question isn't whether you can sell it. It's whether she can *read* you.

**Yannick's wife — Insight (45)** to judge whether the old woman in her doorway means it.


===== ASSISTANT [2026-09-06T15:32:26.832Z] =====
**44 against 45. By one.**

She looks at you for a long moment through the steam.

Whatever she's checking for — and she's a woman who has been lied to by better liars than you — she doesn't find it.

The paddle goes back in the copper, and the rhythm goes back to what it was before.

"North," she says. "Aye. I thought there was something in the vowels."

She works for a bit.

"Evil shit that might need stopping," she repeats, and something that isn't quite a laugh comes out of her. "My man says I'm being a woman about it. Says it's a sick lad on a ship and none of my business and the coin's good."

She lifts a sheet out, wrings it, and drops it into the rinse.

"Three things, then. And I'll deny every one of them if you ever say I said it.

"**One.** It's not a sick lad. Sick men sweat, and they piss the bed, and they stink of the sickness. There's none of that. There's blood in the same place every day and *nothing else*. Whoever's in that bed isn't ill and isn't dying and isn't getting better. He's being kept.

"**Two.** Second morning, the bag came down heavier and there was a shirt in it. Not linen — a fighting man's under-shirt, quilted, for wearing under scale." She pauses. "The arming-points were cut. Not untied. *Cut*, all of them, front and back, the way you do when you're getting something off a man who isn't helping you.

"**Three.**"

She stops paddling.

"The knight who hands the bag down. Big fellow, white eyebrows, no colour in him at all — he's the one that walked Renko off the pier." She's quiet a moment. "Yesterday he asks me, all friendly, whether I ever wash for the houses on the Pearl. Whether I know anyone that does."

She looks straight at you.

"I said no. But he wasn't asking about laundry, was he."


===== USER [2026-09-06T15:34:40.551Z] =====
You know Marisette? What do you think of her?


===== ASSISTANT [2026-09-06T15:34:59.396Z] =====
She snorts.

"Everyone knows Marisette. She's not on this side of the water but she doesn't need to be."

She turns a load.

"What do I think of her." She considers it properly, which you're beginning to realise is how she does everything. "She's not *kind*. Don't let anyone tell you she is. She'll take a girl's whole life apart to keep her house standing and she'll do the sums out loud while she does it.

"But she's straight. That's rarer. She says a price and it's the price. And when Ganny Corliss's daughter got herself in trouble with a Watercrafter's son two winters back — a Forge Quarter girl, mind, nothing of hers, no reason at all — Marisette had the Guild sat down and settled inside a fortnight, and the girl kept the child and the money, and the boy's father still can't say her name without going purple."

She wrings out the sheet.

"So. She's a hard woman who looks after women. There's worse to be."

Then she stops, and her hands go still in the water, and you can see her arriving at it.

"You *are* off the Pearl."

She looks at the door, where Gardwen is standing in the yard with her back to the wall.

"And that white-haired bastard was asking me yesterday about women who do laundry for the Pearl houses." Her voice has dropped. "He wasn't hunting a washerwoman. He's hunting something that went *from* here *to* there. Or from there to here."

She pulls her hands out of the copper and dries them on her apron, and she isn't calm any more.

"What did you people *do?*"


===== USER [2026-09-06T15:45:19.010Z] =====
I got here yesterday - my loyalty’s to Hel and that girl standing outside and no one else. 

These men are stone killers. The albino worse than most… so be careful what you tell that one. 

At some point, you have to choose sides. 

Which part of the boy are they bleeding?


===== ASSISTANT [2026-09-06T15:45:44.647Z] =====
She's quiet for a moment. Then she does what she does with everything: she thinks about it properly.

"I can tell you that. I've been reading it for four days."

She takes a clean sheet off the folded stack and shakes it out flat across the bench between you, and puts her hand down on it.

"Sheet goes on the bed this way — hem to the head, you can tell from the wear where a man's heels go. So." She lays her palm high on it, a little left of the middle. "It's *here*. Every morning, four days. About the size of my two hands together."

She spreads her fingers.

"Upper body. Left side. Chest, or just under the arm — high enough that if he was on his back it ran sideways, because the edge of it's always feathered toward the outside. Same spot, same size, and it's *sharp*-edged, not spread." She looks at you. "That's not a wound that's healing and breaking open. A healing wound weeps different every day, wider then narrower, and the shape wanders. This doesn't wander."

She folds the sheet back up.

"Somebody opens the same place, the same way, every morning. And then somebody else changes the bed."

She holds the folded sheet against her chest.

"And the grey. That's not in the blood. It's *round* it — you get the red out and the grey stays behind in a ring, like a scorch. That's what numbs your hands."

Then she puts the sheet down on the stack, squares it off, and stands there with both hands on it.

"You said choose sides."

She goes to the end copper — the one with the lid half over it — and lifts the lid off, and starts fishing the load out with the paddle into a basket, and slaps it down wet.

"They're due at the sixth bell for that. They'll get it. I'll smile at the white-haired bastard and take his coin."

She looks up.

"But you tell Marisette that Ann Yannick washes for that ship every morning, and she'll go on doing it, and she'll go on *looking*." Her jaw sets. "And if that boy's still bleeding on the day of the Tourney, I want somebody to have done something about it."


===== USER [2026-09-06T15:49:10.180Z] =====
Reach out and grip her shoulder woman to woman, warrior to warrior. 

Creak. Stand. Go get Gardwen. Deliver the intel to marisette. What news of Em?


===== ASSISTANT [2026-09-06T15:50:05.062Z] =====
You put your hand on her shoulder. Not a pat. You take the weight of it, once, the way you'd grip a man's arm before he goes over a wall — and she reaches up and puts her wet hand over yours and holds it there a moment, and neither of you says anything, because there's nothing that would improve it.

Then you creak upright, and your knee makes its opinion known, and you go out into the yard where Gardwen is waiting.

---

It's dusk by the time you're back across the water. Lamps going on. Tourney bunting looking worse than it did yesterday.

Marisette sees you at once. She listens to the whole of it — eight men, no banner, no Baron, the boat from the north-west, the barred shutter, the barrows of clinker, the one bag a day, the same place on the sheet, the cut arming-points, and Ann Yannick's name and Ann Yannick's message — without interrupting once.

At the end she says, "Eight," and then, "*Eight*," differently.

And then: "Ann Yannick will not lose that work, and she will not be alone in that wash-house again after tomorrow. I'll see to it."

---

There's a man in the corner of the room you didn't notice on the way in, because he is very good at that.

Thin, sixty-odd, plain dark coat, a physician's bag by his boot. He's been sitting with a cup of something going cold since before you arrived.

**Hesper.**

"Your friend asked after the courtesan," Marisette says.

Hesper puts the cup down.

"She's alive," he says. His voice is unremarkable in every possible way. "She'll stay alive. It's got no interest in killing her — quite the reverse, it likes the house and it likes being fussed over and it has been extremely helpful all afternoon, which is the part I want to talk to you about."

He looks up.

"But I'd rather start with what you just said. Because a wound in the same place, opened every morning, with a grey scorch round it that numbs the hands—"

He stops.

"How long has that ship been at that pier?"


===== USER [2026-09-06T15:52:58.104Z] =====
No idea. When did the Baron get here? Two weeks?


===== ASSISTANT [2026-09-06T15:53:19.718Z] =====
"No," Marisette says. "The Baron rode in through Caravan Square yesterday at midday. I had it from three people within the hour."

She's already ahead of it.

"But the *ship* came before him. It came by sea, round the Mouth, and tied up at that pier —" she thinks, precisely "— five days ago. I know because the Harbor Masters made a noise about the berth and were made to stop making a noise about it."

"Five days," Hesper says. "And the laundress has been washing that bed for four."

He sits forward.

"Then it started the day after the ship tied up, and the Baron was still three days up the road when it did." He looks between you. "Do you see what that means? Nobody started anything here. That is a *routine*. That is a thing that has been done to somebody every morning for however long, in whatever house it was done in before, and they carried on doing it at sea, and they carried on doing it here."

He picks the cup up, finds it cold, and puts it down again.

"And they brought him by *water*. Twenty-odd knights ride three days up the road in the open, and the thing in the litter goes round by sea in a hull that steams. You don't do that for a champion. You do that because a road has villages on it, and villages have people in them, and whatever's in that cabin cannot be taken past people for three days."

Marisette says quietly: "Hesper."

"I know."

"Tell them what it said."

Hesper is silent for a moment.

"The thing in Emmeralda," he says, "spent the afternoon complaining. It's bored, it's fond of the girl's memories, and it will talk about anything to anyone who'll sit with it. And what it complained about, at some length, was that it had been promised something better than a courtesan.

"It said its master's father keeps a *proper* one. And that his is 'the old kind, the kind that remembers being a person.'"


===== USER [2026-09-06T15:55:51.484Z] =====
Huh. Grunt. Like a ghost? Like a dead knight? 

Tell them about Hel and my dream.


===== ASSISTANT [2026-09-06T15:56:12.488Z] =====
You tell them. The eleven nights, the woman with the wolf, the burning house, and the knight in dragon-scale who is dead and hasn't been told. And what Hel asked: *lay the dragon warrior to rest.*

Hesper does not say anything for a long time.

When he does, his voice has changed — the unremarkableness has gone out of it.

"Say the last part again."

"Lay the dragon warrior to rest."

"*Rest*," he repeats. "Not destroy. Not banish. **Rest.**" He puts both hands flat on his knees. "Madam, you don't lay a demon to rest. There's nothing in a demon to rest. You bind it or you break it and either way you may as well be arguing with a fire.

"You lay a *dead man* to rest."

He stands up and takes two steps and stops, because it's a small room.

"'The old kind. The kind that remembers being a person.'" He turns round. "That is a **shade**. A person who died and did not go where the dead go — kept, and bound, and put somewhere. And you cannot keep a shade in a jar or a stone for long, it wears through. You keep it in a *living body*, because a living body renews itself, and the wearing-through goes into the flesh instead of the vessel."

He looks at you.

"Which is why somebody opens the same place on that boy's chest every single morning. It's not torture and it's not a ritual scar. It's *maintenance*. You bleed the host to keep the seat clean. The grey your laundress can't boil out is what comes off the seam — that's the shade's wear coming out of him with the blood, and it's numbing her hands through a copper of lye."

Gardwen has not moved at all.

"How long," she says, "can they keep a person like that?"

"Years," says Hesper. "If they start young enough that the body grows around it."

Gardwen sits down.


===== USER [2026-09-06T16:01:15.978Z] =====
Well… that’s interesting. 

Go over to Gardwen. Check her to see how she’s doing

You said he arrived yesterday around noon. Didn’t they ring some bells around that time. Were the two things related?


===== ASSISTANT [2026-09-06T16:01:41.008Z] =====
You go over and put a hand on the back of Gardwen's neck. She's gone rigid all the way up.

"Look at me."

She does, eventually. Her eyes are dry and that's worse.

"Seventeen," she says. "*If they start young enough.*"

"Aye."

"He was seven, Magda." Her voice is very steady and very small. "I've spent ten years hoping he was alive. I never once thought about what for."

She takes a breath and puts it away — you can see her do it, the way she did at the ford — and it doesn't go all the way in this time.

"I'm all right."

"You're not."

"No." A pause. "But I'll do."

---

Marisette answers the other thing without you having to ask twice.

"The bells." She sets her cup down. "Yes. Yesterday, just after midday. Everyone assumed it was for the Baron's entry, because it started while the column was in Caravan Square and this city will assume anything."

"It wasn't?"

"It was the **Lady's temple on Temple Isle**. And that wasn't a welcome peal, it was ragged and out of order and it came from the water-tower, not the campanile." Her mouth thins. "That's the *fouling* alarm. They ring it when something goes wrong with the sacred channel — a dead beast in the intake, a spill, a body. It's rung four times in my life."

Hesper says quietly: "And they stopped it inside a quarter of an hour."

"They did. Which they don't do unless somebody senior tells them to." Marisette looks at you. "The High Priestess Nerissa rang the alarm on the day Hanzo di Teufel entered this city, and then somebody had it silenced before the third peal, and nobody has said a word about it since."

She picks the pen up and puts it down again.

"And her niece has red hair."


===== USER [2026-09-06T16:06:31.234Z] =====
My face goes hard. Face off to Marisette.

There’s only 8 of them on that boat. With enough men we could just go and get him. No fucking about. 

Might not be the smartest way, but that’d be my way. 

I’m guessing you wouldn’t want that though. So what’s our play?


===== ASSISTANT [2026-09-06T16:06:58.127Z] =====
Marisette doesn't flinch and she doesn't laugh.

"Eight is eight," she says. "I can put twenty men at that pier before the sixth bell tomorrow. Crowbill can put forty, and he'd do it for what's in your purse, because he'd rather do it than be asked twice."

She lets that sit.

"And then I have twenty men against eight Dragon Knights in scale, on a deck, at night, and I lose eleven of them and it's still even money. And by dawn every one of them has a name and a mother on this island, and Hanzo di Teufel — who is at this moment eating supper with the Governor's brother — knows to the hour who came for his ship."

She spreads her hands.

"It's not that it's stupid, Magda. It's that it's *last*. You only get to do it once, and after you've done it there is nothing else you can do."

Hesper cuts in, and he's not being diplomatic.

"There's a worse problem. You'd be stealing a lit lamp."

He leans forward.

"Whatever is seated in that boy is held there by something, and it is not the ship and it is not those eight men. Take the body out and you have not freed anyone — you have carried a bound shade into the middle of the Pearl with its keepers coming after it, and the first thing that happens when the maintenance stops is that the wearing-through goes somewhere else." He looks at her, then at you. "You cannot rescue him until you know what the anchor is. Otherwise you're not rescuing a boy. You're moving a problem into a house full of women."

Marisette nods slowly.

"So. My play, and you can tell me if it's not yours.

"**Nerissa.** She rang that alarm and somebody silenced her, and she has been sitting on it for a day and a half, and her sister's daughter's hair is in your pocket." Her eyes come up. "She has the only authority in this city that can stop that Tourney, and she has just been given a personal reason to want to. That is the strongest ally available and nobody has gone to her, because nobody knows what you know."

She stands.

"Temple Isle. Tonight, if you'll go. I'll write you in — a note from me gets you past the gate and no further; the rest is you, and she's nobody's fool.

"And while you're doing that, I will find out where Hanzo di Teufel sleeps, and what he keeps on him."


===== USER [2026-09-06T16:09:45.226Z] =====
Milady. We’re in. THe wolf can come too?


===== ASSISTANT [2026-09-06T16:10:20.188Z] =====
Marisette actually smiles — the first one all night, and it's brief.

"Take the wolf."

She's already writing the note.

"A grey wolf walking to heel beside a woman in woodland leathers, at the Lady's own gate, at night." She blots it. "Nerissa's people will not see two strangers with a message. They'll see something that came out of the wild to the water, which is the oldest shape their faith has, and half of them will make a sign at it and the other half will fetch somebody senior *very quickly*."

She folds the note and hands it over.

"That's worth more than my seal. Don't explain the wolf to anybody. Let them explain it to themselves."

---

Ruhi comes off the scullery step reluctantly, and Ila watches from the doorway with her arms wrapped round herself and doesn't ask to come.

Temple Isle after dark is a different city. No bunting. The canals run quieter here and the water in them is *clear* — you can see the bottom by lamplight, which you have not been able to do anywhere else in Purewater.

The temple sits low and wide on the north side with its foundations in the water, all open colonnades and no doors, and the whole building is full of the sound of water moving through it on purpose.

At the gate: two of the **Swords of the Lake** in blue-green, with hands on hilts.

They see the wolf first. One of them makes a sign against his breast.

The other says, without taking his eyes off Ruhi: "It's the middle of the night."


===== USER [2026-09-06T16:13:45.797Z] =====
Fellas. Give this to someone important wil you?


===== ASSISTANT [2026-09-06T16:14:06.402Z] =====
The guard takes it because of the wolf, not because of you.

He's gone eleven minutes. The other one doesn't speak, and Ruhi sits down in the middle of the gateway and looks at him until he moves his feet.

Then a woman comes down the colonnade at a pace that isn't quite running.

Young, thirty or so, blue-green over a nightshift, wet to the knee like she's been standing in the channel. **Lilura Deepcurrent.** She has Marisette's note open in her hand and she's already looking past you for whoever else there might be.

"Who gave you this?"

"Marisette. On the Pearl."

"I know who Marisette is." She reads it again. Whatever's in it is short. "It says you have something about the water and something about the Baron and that I should not be the one to hear it."

She looks at Gardwen. At the wolf. Back at you.

"She's not asleep," Lilura says. "She hasn't been asleep since yesterday noon."

---

They take you in through the colonnade, past the great tank where the channel runs through the temple itself, and the sound in that room is enormous — water on stone, everywhere, no other noise at all.

The far end is dark. There's a lamp on a low table and a woman sitting on the step of the tank with her feet in the water and her sleeves pushed up, doing nothing at all.

**Nerissa.** Silver through dark hair. Older than Lilura by twenty years and harder by more than that.

She doesn't get up.

"Leave the wolf," she says. "It can drink. Nothing in this water will mind."

Then, to you, in a voice with no ceremony left in it whatsoever:

"Marisette does not send people to me. Ever. So say the worst of it first and we'll work backwards."


===== USER [2026-09-06T16:21:39.925Z] =====
The worst of it? 

That’d be when I killed Hanzo’s evil
Little shit of a son after he bound a demon into one of the girls at the sylph’s embrace… and then fed his body to pigs

Working backwards from there, we think he was planning to do the same thing to your niece. 

Oh, and we think the dragon knights kidnapped her brother 10 years ago and is hosting a shade in him so that he can fight in the tourney in a few days time…

That’s about all of it

Blue eyes gleaming with a sweet smile


===== ASSISTANT [2026-09-06T16:21:49.622Z] =====
**Nerissa — Insight (80).** She has spent thirty years listening to people lie in that room.


===== ASSISTANT [2026-09-06T16:22:15.209Z] =====
**56 against 80.** She reads you all the way through, and what she finds is that you have not told her a single lie.

---

Nerissa doesn't move for a while. Her feet stay in the water.

"You smiled," she says at last, "when you said *pigs*."

"Aye."

"Mm." She takes her feet out of the tank and dries them on the hem of her robe like a farmer's wife, and gets up. "Good. I'd not trust a person who could say that flatly."

She walks to the edge of the lamplight and stands with her back to you.

"Now I'll tell you mine, and then we'll be even.

"Yesterday, four minutes after noon, this channel went **wrong**. Not fouled — I've had fouled, fouled is a dead ox and a week of prayers. This went *thin*. The Lady's presence in her own water went thin, the way a voice goes thin at a distance, in the space of about ten heartbeats." Her hands have closed. "I have served here since I was nineteen and it has never once done that.

"So I rang the tower. And by the third peal there was a boy from the Governor's household at my gate with a written instruction to *cease*, on the grounds that the city was welcoming a distinguished guest and the bells were causing alarm during a formal entry."

She turns round.

"Written and sealed by **Prince Emeric**. Who is twenty-four years old, and well-meaning, and who has been told by three separate men on his council this fortnight that his uncle would like the Tourney to go smoothly."

"And you stopped."

"I stopped." Something flat and furious goes across her face. "Because I am the High Priestess of a temple that is paid for by this city's Guilds, and because I had *nothing*. A thin feeling in the water and no cause I could name in front of a magistrate. If I had rung on I would have been removed by Thursday and replaced by somebody who wouldn't ring at all."

She comes back and sits down on the step again, closer.

"And now an old woman walks in at midnight and tells me there is a ship at the Forge Quarter pier that steams where it sits, that arrived five days ago, and that has a dead man bound into a living boy aboard it."

She looks up.

"Say the part about my niece again. Slowly."


===== USER [2026-09-06T16:23:49.680Z] =====
Explain what we found on Santo


===== ASSISTANT [2026-09-06T16:24:15.240Z] =====
You put it on the low table by the lamp and take it apart for her the way you'd show someone a bad joint of meat.

The **cloak** — border cut, canal-soaked, tailor's mark of a tower with three windows stitched inside the collar where the wearer never looks.

The **ring**, sewn into the lining. Heavy gold, a worm eating itself. Hidden by a man who didn't want it on his hand that night.

The **letter**, dried against a lamp glass, most of it pulp. *—ee days before the Lady's Tourney, at the hou—*, and the bottom half of a seal with the same beast on it.

Eleven **border coins**, unchanged.

And then the oiled silk.

"Five of these. Four still full." You lay them out in a row. "Hair, bound at one end with copper wire. And a bit of something brown that isn't wax." You put the fifth beside them. "That one's empty. He used it."

"On the courtesan."

"Aye."

"Whose hair is black."

"Aye."

Nerissa picks up the first twist. She doesn't open it. She holds it, and her thumb moves once across the silk.

"So he came into this city carrying five women in his coat," she says. "And he spent one of them on a girl at Constantine's, and he had four left."

She opens it then, and lets the hair out into the lamplight, and looks at it for a long moment.

Then she says, in a voice that has gone completely level:

"Beneath the wire. Is there a knot in it, or is it cut clean at both ends?"

You turn it. The wire's at one end. The other end of the hank is blunt, square, all the strands the same length.

"Cut clean."

"Then it was taken with shears, off a head, by somebody standing behind her." Nerissa lays it down very carefully. "It was not gathered off a comb or a pillow. Somebody got close enough to my sister's daughter to put shears in her hair, and she did not scream, and she has not told me."

She looks up.

"Her name is **Sana**. She's nineteen. And she has been at the temple school on Lost Isle for six weeks and I have not seen her in three."


===== USER [2026-09-06T16:26:52.594Z] =====
Let’s pause. Record the session for now.


===== ASSISTANT [2026-09-06T16:28:07.500Z] =====
The consistency check caught a real thing: Marisette's agenda completed, which orphaned two beats that are still wanted. That's the successor-agenda case — fixing it properly.


===== ASSISTANT [2026-09-06T16:29:02.454Z] =====
Session recorded and committed. Consistency clean.

## Session 1 — the ford to the temple

**Where you are:** midnight, `d-2/night`, in the Temple of the Lake Lady. One day and a night until the Tourney. Nerissa has just given you a name — **Sana**, nineteen, her niece, unseen for three weeks.

**Rolls this session** — 22 in all. The two that bent the story:

| Roll | Result |
|---|---|
| **Santo, Lore (Demonology), Formidable 25** | **19 — success.** The binding *took* |
| **Santo, Stealth 50** | **100 — fumble.** He roused the house and went in the canal |

That first one is a real divergence from the written adventure. Emmeralda was supposed to be a dying victim; instead she's comfortable, chatty, and possessed — which is why you got Hesper's read on the shade at all. The demon told you about the Baron's "proper one" because it was *bored*.

Your own dice: Survival 12 on Ruhi's ruff, Willpower 43 to face down the customs man, Perception 70-on-70 counting eight knights, Brawn 18 hauling Gardwen out of the canal — and Influence 54 against 27, which is why a laundress nearly stopped talking to you.

**What the world did while you weren't looking:** Blau rolled **Streetwise 82 against 66** and failed to trace Santo on the Pearl. His men worked the island house to house all day and got nothing. He's still looking, and he's asking laundresses about the Pearl now.

**State changes recorded:** Santo dead and destroyed. His agenda abandoned, Blau's containment thwarted and replaced with *Find the young master*, the Baron's tourney clock stalled. Marisette's *Find who carved Emmeralda* achieved in under a day — and the consistency check flagged that its beats were orphaned, so it spawned its successor: ***The four women, and the reckoning***, priority 5.

**And the thing nobody knows:** you and Gardwen now *suspect* the champion is her brother. That's recorded as `suspects`, not `knows` — you reasoned to it from a barred shutter and a bag of boiled sheets, which is the good way to get there. Hanzo still has no idea he has another son; that agenda stays dormant.

Open threads for next time: Sana on Lost Isle, three of four women still unnamed, Prince Emeric's sealed instruction, whatever anchors the shade, and Ann Yannick washing that bed every morning until somebody does something about it.


===== USER [2026-09-06T17:06:21.232Z] =====
We need to go look for Sana. What does Gardwen want to do?


===== ASSISTANT [2026-09-06T17:06:48.879Z] =====
Gardwen doesn't answer straight away. She's looking at the water going through the tank.

"I want to go to that pier tonight," she says.

Flat. No performance in it.

"I want to walk down there and kill eight men and take him off that ship, and I've been standing here for the last ten minutes working out how I'd do it, and the answer is I couldn't, and I'd have gone anyway." She finally looks round. "So I'm not to be trusted about this. I know that about myself. I've known it since about the third hour after we left that wall."

She puts her back against the tank-step and slides down to sit on the stone.

"Here's the sense of it, and I hate every word.

"My brother has been in that condition for ten years. He was in it yesterday and he'll be in it tomorrow, and whatever they do to him at dawn they've done four hundred times. One more night doesn't change what he is — it just changes whether I ruin the only chance of getting him *out*." She grinds the heel of her hand into her eye. "Hesper's right. Take him now and I'm carrying a lit lamp into a house full of women, and the first thing that goes wrong goes wrong on Ila.

"Sana is different. Sana's a girl who's had shears in her hair by someone who got behind her, and there are three days of Tourney left and four twists in your pocket and one of them's hers. She can still be got to *first*."

She looks up at you.

"So. Sana. Tonight, if the priestess will move."

Then, quieter:

"But Magda — when we do go for him. When we know the anchor and it's time." Her jaw sets. "I'll not be talked into waiting a second time. You should know that now, so it's not a surprise later."

Behind you, Nerissa has already turned to Lilura and is saying something short and low, and Lilura is going out of the room fast.


===== USER [2026-09-06T17:14:55.216Z] =====
I’m pledged to you girl. Where you go. I go.


===== ASSISTANT [2026-09-06T17:15:12.702Z] =====
Gardwen doesn't say anything.

She reaches up without looking and puts her hand round your wrist and holds it, hard, for about three seconds, and then lets go and gets up and starts checking her knife the way she does when she needs her hands doing something.

That's the whole of it. It's enough.

---

Nerissa has finished with Lilura and turns back.

"**Lost Isle** is the school. Forty girls, a dozen of ours, and my niece was sent there in the spring because she's clever and because her mother wanted her out of the Merchant's Quarter." She's already unpinning her sleeves. "It's twenty minutes by water at this hour. There's no gate to argue with — it's my house."

Lilura comes back with two of the Swords of the Lake behind her and a lamp, and doesn't look happy.

"Mother — the letters."

"Yes." Nerissa says it without turning. "My sister has had two letters from Sana in six weeks. The first came at the end of the fourth week. The second came eight days ago and it was three lines and it was *fine*, and my sister showed it to me and said 'she's settling,' and I said 'good.'"

She takes the lamp herself.

"Three lines. In a hand I'd know anywhere, from a girl who once wrote me eleven pages about a heron."

She goes past you toward the colonnade and the water-stair, and she does not walk like a woman of sixty.

"Bring the wolf."


===== USER [2026-09-06T17:18:13.181Z] =====
Limber up a bit as we walk. Crick my neck. Try a few swings of the staff. Check my bullets.


===== ASSISTANT [2026-09-06T17:19:04.288Z] =====
Quick correction before we go: I said the school was *on* Lost Isle. That's wrong, and it matters for the map — **Lost Isle** is a half-drowned ruin among the Northern Isles, weed-choked and shunned, held by animists to be thick with spirits and prized by **spirit-binders**. The boatmen won't go near it.

Nerissa sets it straight herself on the water-stair.

"The school is on the **Northern Isles** — Corbie's, the old customs house, forty girls and a wall." She hands the lamp to a Sword and steps down into the boat. "Lost Isle is the drowned one across the channel from it. Four hundred yards. The girls are forbidden it and they row out to look at it anyway, every year, because they're girls."

---

You limber as you walk. Neck first — it goes with a crack that makes one of the Swords glance round. Then the shoulders, then two slow swings of the staff at half-length in the colonnade, feeling where the joints are tonight, which is: not good, but adequate.

You count the sling bullets by touch in the pouch. Eleven. You'd have liked twenty.

Gardwen watches you do it and doesn't say anything, and then starts checking her own kit, which is thinner than yours.

---

Twenty minutes on black water with two Swords rowing. Nobody talks. Nerissa sits in the bow with the lamp shuttered and her hand trailing over the side in the water the whole way, which is not idleness — you can see her listening to it.

**Corbie's** is a squat old customs house with a wall round it and a light burning over the door at one in the morning, which Nerissa remarks on before the boat has even touched.

The woman who opens it is the mistress of the school and she has been crying.

She sees Nerissa and her face does something terrible.

"We sent to you at *dusk*," she says. "We sent a boat at dusk, Mother — didn't it come?"

Nerissa has gone very still on the step.

"No," she says. "Nothing came."

"Sana's gone. Since yesterday morning. We've had every girl out looking and we've dragged the channel and I sent Bettan to the temple *myself*—"

And across the water, four hundred yards off, Lost Isle sits low and black and weed-choked with nothing on it at all.

Except that there's a light moving on it.


===== USER [2026-09-06T17:19:06.399Z] =====
Don’t forget about Gardwen’s magic. She can do stuff


===== ASSISTANT [2026-09-06T17:19:13.614Z] =====
Good call — I've been running her as a healer with hands and forgetting she's a caster.


===== ASSISTANT [2026-09-06T17:19:42.330Z] =====
She's a **Cleric** — Divine Magic, **Piety 87**, **Channel 85**, 18 magic points. Rank 1, and she has more than I've been giving her:

**Animal Friendship · Barkskin · Command · Cure Minor Wounds · Detect Evil · Know Passions · Entangle · Slow Poison · Remove Fear**
*(and at rank 2: Cure Serious Wounds · Cure Disease · Hold Person)*

**Detect Evil** and **Know Passions** are the two I've been wasting. She could have read Ann Yannick, or Nerissa, or the thing in Emmeralda.

*(Your own kit, for the record: no magic — but **Blessed by Hel**, you don't age, and **Artful Dodger** gives you an extra action for parry or evade every round.)*

---

The mistress of the school is still talking and Nerissa has stopped listening.

She's looking across four hundred yards of black channel at the light on Lost Isle.

It isn't a lamp. It's too low and the colour's wrong — a dull red, close to the waterline, and it doesn't swing the way a carried light swings. It moves in a straight line for a bit, and stops, and after a while it moves again.

"There is nothing on that island," the mistress says, following her eyes. "There's nothing *left* on it, Mother, it's all down in the weed—"

"Who rows out there?"

"Nobody. The girls dare each other and none of them ever have."

Gardwen has come up beside you and she's already looking at Ruhi, who is standing at the water's edge with her ears forward and her whole body pointed at that light.

"Magda," Gardwen says quietly. "I can find out what's on that island from here, if the Lady's willing to lend me the eyes for it. But it'll cost me, and whatever's over there might feel it done."


===== USER [2026-09-06T17:21:21.977Z] =====
We need to know where the girl is. Do it


===== ASSISTANT [2026-09-06T17:21:54.279Z] =====
Her sheet is the Classic Fantasy port — divine magic off **Piety 87**, not the Imperative Magic skill — so that's what she casts on. Four hundred yards of open channel is far past where a rank 1 spell wants to reach.

**Gardwen — Piety, Formidable (87 → 44).** And a second roll for whether the thing over there feels it done.


===== ASSISTANT [2026-09-06T17:22:12.071Z] =====
**46 against 44. She misses by two.** One magic point gone and nothing to show for it.

**34 on the second — it doesn't feel her.** Small mercy.

---

She goes down on one knee at the water's edge and puts both hands flat in the channel, and says something under her breath that has the shape of a name in it.

And you *feel* the room she makes — the way the air goes when a door opens somewhere else in a house.

Then it closes. Nothing comes.

She stays there a moment longer with her hands in the water, and then sits back on her heels.

"Too far." She's breathing like she ran here. "It's not the distance, it's — the water's all *hers* here, and I'm not hers, and I was asking a favour in someone else's house." She wipes her palms on her thighs. "I got about halfway across and it went out like a candle in a draught."

Nerissa has been watching her the whole time with an expression you can't read at all.

"You reached," she says. It isn't a question. "From the bank. Across running water that isn't yours, at a rank you shouldn't manage."

"I didn't reach far enough."

"No." Nerissa is already unpinning her other sleeve. "You reached *at all*. Girl — you were asking a favour in someone else's house because you were standing on the doorstep shouting."

She steps down into the channel until she's shin-deep, and holds out her hand.

"So come inside and ask properly. Take my hand and do it again, and this time the Lady will hear where it came from."

Across the water, the dull red light stops moving.

Then it goes out.


===== USER [2026-09-06T17:23:07.561Z] =====
Could she use a passion to augment it?


===== ASSISTANT [2026-09-06T17:23:59.940Z] =====
Yes — a Passion augments a related roll at **+20% of its value**.

Gardwen has one that's live: **Love (Brother + Family) 80** → **+16**. She's a woman who has spent ten years looking for a taken child, being asked to find a taken girl. That's squarely inside it. *(Her other three passions are sitting at 0 on the sheet — dead weight until something in play gives them a value.)*

And this isn't a retry of the same attempt — Nerissa channelling it removes the problem that beat her. **Hard (58), +16 augment = 74.**


===== ASSISTANT [2026-09-06T17:24:28.408Z] =====
She takes Nerissa's hand and goes into the channel up to her knees, and the second time is not like the first.

*(The CLI augments before grading — 87+16 = 103, Hard → **69**. Roll of **46**. She's through.)*

---

Gardwen's head goes back.

It's not graceful. Her fingers lock on Nerissa's hard enough to hurt and her breath goes out of her all at once, and Nerissa stands there in the water and takes it without moving, the way you'd hold a rope.

Then Gardwen starts talking, fast, flat, describing as she goes:

"There's — the whole island's *humming*. Underneath. Not evil, just old, there's a great deal of something old down under the weed and it doesn't care about us at all." Her eyes are shut. "Above that. On the stone. There's a *working*."

"Say what you see," Nerissa says quietly.

"Same flavour as the chalk on her floor. Same hand. It's not finished — it's *laid out*, like a table before dinner." Her mouth twists. "It's cold. It's been cold a while. Whoever set it hasn't come back to it in a day or more."

"Living things."

"Two moving." Gardwen's head turns, slowly, tracking. "Both of them wrong. Not demons — *men*, but wrong, the way milk's wrong. They're low down and they're together and they've stopped, they've gone still since the light went out—"

She stops.

Her whole face changes.

"There's a third. Not moving. Not wrong." Her voice cracks. "She's *small* in it, Magda, she's gone right down small the way you do when you're hiding — and she's above the other two, up high, in the stone."

Nerissa's grip on her hand tightens.

"Is she alive?"

"She's *frightened*," Gardwen says. "You can't be frightened if you're not alive."

Then she opens her eyes and looks straight across four hundred yards of black water at the island where nothing shows at all.

"She's been there since yesterday morning and they haven't found her yet."


===== USER [2026-09-06T17:26:03.240Z] =====
OK. Let’s go get her. Are the sword of the lake coming too?


===== ASSISTANT [2026-09-06T17:26:26.246Z] =====
"They are," Nerissa says, before either Sword can be asked.

Then, to them: "**Corvin. Ash.**" Both come to attention on the step. "You'll row, and then you'll do exactly what this old woman tells you, and if she tells you to leave me and take the girl, you'll do that too."

The younger one starts to object. She looks at him once and he stops.

**Lilura** stays. She argues about it for a good thirty seconds and loses, and gets left holding forty frightened schoolgirls and a lit house — which, when Nerissa points out that the men over there can *see* Corbie's from the water, and that the boat only has to be missed once for somebody to try the school instead, she stops arguing about immediately.

Nerissa strips off the outer robe and comes in the plain undershift, and puts a short-hafted mace through her belt that nobody comments on.

---

Here's the shape of it, as Gardwen laid it out and as you can see it from the bank:

**Lost Isle** is low — a drowned district, not an island. Broken roofs and half-walls standing out of the weed, water running through what used to be streets. Maybe two hundred yards across the visible part.

- **The two men** are *low down and together*, north side, near the water. Where the red light was.
- **The working** is laid out cold, unfinished, somewhere near them.
- **Sana** is *high, in the stone* — the only thing standing tall enough to be "high" on that island is a broken tower-stub near the middle-south, and she's been in it since yesterday morning with no water.
- **The light went out** the moment Gardwen's first casting brushed the place. They may know something. They may just be careful.

Four hundred yards of open black. One boat. The moon is thin.

The far side of the island — the south — is away from the men and closer to the tower.


===== USER [2026-09-06T17:32:02.854Z] =====
Gardwen’s call. I want to kill or capture them


===== ASSISTANT [2026-09-06T17:32:23.277Z] =====
Gardwen doesn't hesitate — this is the one thing tonight she's actually trained for.

"South side. Land in the weed, not on stone — weed's quiet and it'll take the boat's noise. Then we don't go *at* them."

She crouches and draws it in the mud of the bank with her finger.

"Three things, in this order.

"**One — their boat.** They came out here somehow and it'll be on the north side with them. If they're spooked they run for it, and then we've got nothing and they've got a day's start. Someone takes it or holes it before anything else happens." She looks up. "That's the whole game. Do that and they're on a two-hundred-yard rock with us.

"**Two — Sana.** She's been in that stone since yesterday morning with no water and she's hiding from *anything that moves*. If a Sword in armour comes round a corner at her she'll bolt, and if she bolts she goes into the weed in the dark and we lose her for good. So it's me and Ruhi that go up, and it's me that calls to her, because I'm the only one here who isn't wearing anything."

She stands.

"**Three — then your two men.** Not before. Once the boat's gone and the girl's out of the tower they've nowhere to be and nothing to bargain with, and we can take them at our leisure, from three sides, with the priestess and two Swords." A pause. "Alive if they'll have it. Because whoever laid that working knows what the anchor is."

She wipes the mud off her finger.

"That's my call. You said kill or capture — I'd say capture *hard*. But Magda, they're wrong. I don't know what that means yet and neither does she." She nods at Nerissa. "So don't let anybody close with them alone."

Corvin is already pushing the boat out.


===== USER [2026-09-06T17:33:52.623Z] =====
Stay close to Gardwen and follow her lead


===== ASSISTANT [2026-09-06T17:34:03.938Z] =====
The crossing takes eleven minutes and nobody speaks. Corvin and Ash row with the oars muffled in somebody's shawl, short strokes, no feathering.

**The approach (60)** — and the weed on the south shore is on your side.


===== ASSISTANT [2026-09-06T17:34:24.700Z] =====
**38 against 60 — clean.** The weed takes the boat with a long wet sigh and nothing more.

**Your Stealth: 20 against 68.** Very good. You go over the side into thigh-deep water and mud that wants your boots, and you make less noise doing it than the young Sword does.

---

Lost Isle up close is a street.

That's the thing that gets you. It's a *street* — you can see the line of it, doorways and window-holes at chest height, a gutter, the stub of a wellhead — and it's all standing in four feet of black water with weed growing out of the windows. You are walking up somebody's road with the water at your thighs.

Nerissa goes past you and touches a doorframe as she passes, briefly, the way you'd touch a coffin.

At the first junction it splits as agreed:

**Corvin and Ash** go left and north along what used to be the waterfront, low, to find the men's boat.

**Nerissa** goes with them as far as the corner and stops there — she'll hold the middle, in earshot of both.

**You and Gardwen and Ruhi** go right and south-east, toward the tower-stub.

---

It comes up out of the weed about eighty feet ahead: three storeys of it still standing, one whole corner gone so you can see the floors inside like shelves. The bottom ten feet are drowned. There's a stair inside, half of it, going up.

Gardwen stops at the base and puts a hand flat on the stone.

Then she looks up and calls — not loud. Pitched to carry up a stairwell and no further.

"**Sana.** Your aunt sent me. Nerissa sent me. She's stood in the water at the corner and she's got her mace and she is *extremely* angry."

Nothing.

Ruhi's ears are forward and locked on something above.

Then, from three floors up, very small and very hoarse:

"*Say what she calls my mother.*"


===== USER [2026-09-06T17:37:52.597Z] =====
I don’t know but I know you sent her an eleven page letter about a heron. The three line one note you sent raised an alarm for her and that’s why we’re here


===== ASSISTANT [2026-09-06T17:38:05.653Z] =====
**Sana — through a day and a half of no water and no sleep, deciding whether to believe a voice in the dark (60).**


===== ASSISTANT [2026-09-06T17:38:24.167Z] =====
**54 against 60.** She believes you.

---

There's a long silence. Long enough that Gardwen looks at you.

Then: "I don't— " The voice breaks and comes back. "I don't remember writing eleven pages."

"You did. She's told it to me twice tonight and she's not a woman who repeats herself."

Something moves up there. Stone grit comes down and lands in the water.

"Is she *really* here?"

"Aye. Stood in the channel at the corner with a mace in her belt and no robe on."

A sound that might be a laugh and is mostly not.

Then she starts coming down, and it takes a long time, because she has been folded into a gap between two floor-joists for a day and a half and her legs have stopped being reliable. Twice you hear her stop and just breathe.

Gardwen goes up the half-stair to meet her and brings her the last of it, and she comes out into the weed-light barefoot in a school shift with her hair chopped ragged on the left side of her head, and she is nineteen and she looks about twelve.

Dark red hair. What's left of it.

She grips Gardwen's forearm and won't let go and talks in a rush, hoarse, too fast:

"There were three of them yesterday. Three. There's only been two since this morning — the other one went off in the boat before dawn and hasn't come back—"

"Slow down, lass."

"You don't understand." She's shaking. "They didn't come for me. They came for the *place*. I only ran because I *saw* — I came out to look at the ruin like everyone does and they were *already here*, and they had a girl from the school with them, and she was walking with them like she knew them."

She looks between you.

"Bettan. Her name's Bettan. She's fourteen. She's the one they sent to the temple last night with the message."


===== USER [2026-09-06T17:41:41.815Z] =====
Huh. Good to know. 

How well do you know this girl. Did she change recently? Start acting differently.


===== ASSISTANT [2026-09-06T17:42:05.726Z] =====
Gardwen has already got her own flask out and is making Sana drink it slowly, a mouthful at a time, with a hand on the back of her neck.

Sana thinks about the question properly. She's clever — you can see her make herself stop shaking to answer it.

"About a month ago."

She takes another mouthful.

"She was — Bettan's a *baby*. Fourteen and homesick and cries at everything, and she'd got herself half-drowned in the misery of it, and none of us were kind enough about it." A wince. "Then she went quiet for about a week. Properly quiet, wouldn't come down to meals, and Mistress Corliss had her in and we all thought she'd be sent home.

"And then she came back *cheerful*."

She looks up.

"That's the bit. Not better — *cheerful*. And she started being lovely to everyone. Girls she'd never spoken to. She sat with Ana Vell for a whole week and Ana Vell is *horrible*." She wipes her mouth. "We all said it was nice. Mistress Corliss said it was nice. Everyone was so pleased."

Then she says, and her voice drops:

"She stopped wearing her shawl. In *February*. She'd sit in the window bay with the shutter open at night doing her letters and the rest of us are three to a bed with chilblains, and she'd say she was warm.

"And she started asking about people's families. All the time. Who's your mother, where's your house, have you got sisters. And we all told her, because she was being *nice*."

She looks at the ragged side of her own head.

"She did my hair. Three weeks ago. She said she could do the plait my aunt does and she stood behind me with the scissors and she did it *beautifully*, and I said thank you."


===== USER [2026-09-06T17:43:48.035Z] =====
OK. Sounds like Santo had a little side project. Let’s go and find their fucking boat.


===== ASSISTANT [2026-09-06T17:43:59.203Z] =====
Sana goes back to your boat with Gardwen's cloak round her and instructions not to move. She argues. Gardwen wins.

Then north, along the drowned waterfront, thigh-deep, toward the corner where Nerissa's holding.

**Corvin and Ash, finding the men's boat (60).** And a second roll: whether the two of them have noticed anything yet.


===== ASSISTANT [2026-09-06T17:44:17.710Z] =====
**14 against 60 — they find it fast.** And **72 — the two men still have no idea anyone is on this island.**

---

Nerissa is at the corner exactly where she said she'd be, standing in black water to her knees with the mace out of her belt and held down along her thigh. She takes one look at Sana going past in the boat behind you and her face does something she immediately puts away.

Ash comes back along the wall at a crouch and gets to you both, breathing hard, pleased with himself.

"Found it, Mother. Not a boat — a **punt**, flat, no keel, tied off in a doorway about sixty yards up. Corvin's sat on it." He wipes his face. "It's poled, not rowed. And it's the *only* one — we went the length of the north side."

Which means the third man took the other boat before dawn and hasn't brought it back, and these two have been on this rock all day with one flat punt between them.

"And them?"

"Forty yards past it, in what's left of a big room — half a roof on, no wall on the water side. There's a fire *in* there, laid on a slab, but it's not lit now." He hesitates. "They've a lantern with a red slide. And Mother — they've been *digging*. There's a heap of weed and muck pulled up out of the floor and stacked, and something under it they've uncovered. Stone. Cut stone with work on it."

He looks between you.

"They're just sitting. Both of them, on the edge of the slab, side by side, not talking. Been like that since the light went out."

Gardwen has gone very still at *not talking*.

"How long is that now?" she asks.

"Near on twenty minutes."

Nerissa lifts the mace slightly.

"Two men who have sat in the dark without speaking for twenty minutes," she says, "are waiting for something."


===== USER [2026-09-06T17:45:41.264Z] =====
Let me go first. Bring them out (as long as they don’t have bows). 🫡


===== ASSISTANT [2026-09-06T17:46:02.213Z] =====
Ash is certain: no bows, no crossbows, nothing at their backs. Two men, belt knives, and one has something longer leaning against the slab that might be a billhook.

You go up the drowned street alone with the staff across your body and the water pushing at your thighs.

Sixty yards. The punt in its doorway with Corvin folded down beside it, who doesn't look up as you pass.

Then the big room.

Half a roof, no wall on the water side, so you can see straight in from thirty feet: a stone floor above the waterline, a raised slab, and the heap of dragged-up weed and muck they've stacked against the standing wall. Where they've cleared it there's cut stone showing — deep-carved, and the carving goes on down under the water at the edge, and it is a great deal older than anything else on this island.

The red-slide lantern sits on the slab, shut.

And the two of them are sitting side by side on the edge of it, facing the water, facing *you*, in the dark.

You are twenty feet away before either moves.

Then both of them turn their heads at once. Not together like men who heard the same thing — *at once*, the same speed, the same distance, like two doors on one hinge.

They look at you.

Neither stands.

One of them — sandy, thirties, a boatman's forearms — says in an entirely ordinary voice:

"You're not her."

And the other one, without any pause at all, in the same voice, finishes it:

"—she was meant to bring the girl."


===== USER [2026-09-06T17:47:16.985Z] =====
No girl, Just little old me. All alone surrounded by big scary warriors


===== ASSISTANT [2026-09-06T17:48:48.656Z] =====
`--character`, not `--id` — that's why the roster came back empty.

**56 against 128 — a hit. 7 damage. Location 13: right arm.**


===== ASSISTANT [2026-09-06T17:49:06.516Z] =====
**Right arm: −3 of 4. Serious wound — that arm is finished.**

---

You don't announce it. You're still talking when the sling comes over — *all alone, surrounded by big scary warriors* — and the stone goes out on the last word.

It takes the sandy one high on the right arm, on the outside, and you *hear* the bone go from twenty feet.

The arm drops. It doesn't swing — it just stops being part of him and hangs.

He doesn't make a sound. He doesn't look at it. He doesn't even look at *you*.

Both of them stand up at the same moment, the same speed, like the slab tipped them.

And the sandy one says, conversationally, with his arm hanging off him:

"That's going to make the poling difficult."

And the other one finishes: "—we'll manage."

They come off the slab into the water together. The billhook comes up off the wall into the second one's hands.

---

**Round 1**

| Init | | AP |
|---|---|---|
| **19** | Hollow man *(billhook)* | 3 |
| **16** | Hollow man *(sandy)* — right arm ruined | 3 |
| **16** | **Magda** | 3 |

Billhook goes first. Sixty yards behind you, Gardwen has started running and will not arrive this round.

You've got your staff, three Action Points, and **Artful Dodger** — one extra reaction for parry or evade on top of them.

They're wading in at you together. What do you do?


===== USER [2026-09-06T17:50:12.414Z] =====
Break sandy. Hit him hard


===== ASSISTANT [2026-09-06T17:50:28.933Z] =====
The billhook is on 19. It reaches you before you can swing.

It comes in low and fast — a long hooked head on a six-foot haft, sweeping at your legs to put you in the water.

Your staff is up. You have three Action Points and Artful Dodger on top of them, so a reaction costs you nothing you'll miss this round.

**Parry it with the staff, or evade?**

*(Then Sandy's yours — attack queued, and with one arm gone he's short of options.)*


===== ASSISTANT [2026-09-06T17:50:35.131Z] =====
Ready to resolve as soon as you call it — parry or evade.


===== USER [2026-09-06T17:50:53.951Z] =====
Parry. Try to disarm if it all works out


===== ASSISTANT [2026-09-06T17:51:20.666Z] =====
**83 against 32 — he misses. Your parry: 21 against 85.** One level of difference, one special effect, and it's yours.

**Disarm.**


===== ASSISTANT [2026-09-06T17:51:39.394Z] =====
**58 against 85 — hit. He fails his parry at 78 against 32. Another special effect to you. Six damage. Location 15: the right arm again.**

**−9 against 4 hit points. Major wound.** That arm is not an arm any more.

---

The billhook comes in at your shins and you don't step back — you drop the staff-end into its path and roll your wrists, and the hooked head skids off the shaft and goes *past*, and while his weight is still following it you carry the same motion up and round and take the haft out of his hands with the top third of the staff.

It goes into the black water. He watches it go.

Then you pivot off the back foot and put everything you have into the sandy one.

You're aiming for the same arm. You get it.

It's already broken high up and this takes it below the elbow, and there is a wet crack and the whole limb comes apart at two places at once, and what's hanging off his shoulder now is not a limb. Bone through the sleeve. Six inches of it.

He goes back a step from the force of it. Only one.

Then he straightens up.

He looks at the ruin of his own arm — and this time he *does* look at it, curiously, turning slightly to see it better, the way you'd inspect a torn coat.

And the other one, standing empty-handed in the water beside him, says in that same flat conversational voice:

"That's the arm gone, then."

"Mm," says the sandy one.

Neither of them has bled a drop.

---

**Magda: 1 AP left. Both of them: 2.**

Gardwen and Ruhi are forty yards out and coming hard.


===== USER [2026-09-06T17:52:36.886Z] =====
Prepare my defenses if need be.


===== ASSISTANT [2026-09-06T17:52:47.044Z] =====
You set your feet and bring the staff to guard. One Action Point left, and Artful Dodger on top of it — two reactions, which is exactly two attacks' worth.

They both come.


===== ASSISTANT [2026-09-06T17:53:08.704Z] =====
**Both come off you.**

The first — 36 against 48, a real attempt — you take on the shaft and turn down and away, and the dagger goes into the water past your hip.

The second one never lands. 39 against 32: he's swinging left-handed with his own bone showing and he can't find you.

Neither of them says anything about it.

---

They're close now. Close enough that you can see there's something wrong with their eyes in the dark — not glowing, nothing so obliging. Just *slow*. They blink at the wrong times.

The sandy one shifts his grip on the dagger with his one good hand. The other has stepped left, widening it, putting himself where you'd have to turn to face him — and they're doing it in that same shared rhythm, no signal passing between them, like a man moving both his hands.

Then, from forty yards up the drowned street, there's the sound of a lot of water being crossed fast.

Both heads turn at once.

**Ruhi** comes out of the dark at chest height and takes the billhook-man off his feet into the black, and the two of them go under together in a boil of white.

**Gardwen** is ten yards behind her and coming, and Nerissa behind that, and the two Swords behind her.

You are out of Action Points. New round starts now.


===== USER [2026-09-06T17:53:16.093Z] =====
One of them already attacked this round


===== ASSISTANT [2026-09-06T17:53:42.080Z] =====
You're right — I closed the round early. Still **Round 1**, and there's a pass left.

Correct accounting: everyone started on 3.

- **Billhook** — billhook swing (2), then dagger (1). **1 left.**
- **Sandy** — parried your staff (2), then dagger (1). **1 left.**
- **You** — parry (2), attack on Sandy (1), parry (0), plus the Artful Dodger reaction on the second parry. **0 left, and the free reaction spent.**

So it isn't a new round. It's the last pass of this one, and you are the only person in the water with nothing left to spend.

Ruhi has the billhook-man under and his remaining point won't help him there.

**Sandy has one Action Point and you have no defence.**


===== ASSISTANT [2026-09-06T17:53:59.973Z] =====
**64 against 32. He misses anyway.**

He comes in with the dagger and you have absolutely nothing left to stop it with — and the thing that saves you is that he is trying to knife a woman with his off hand while the other arm swings loose and unbalances every step he takes. The point goes past your ribs by a hand's width and his own momentum carries him half round.

For a moment the two of you are shoulder to shoulder in the black water, close as dancers.

He turns his head to look at you from about a foot away.

There is nothing behind it. Not malice, not fear, not even effort. He looks at you the way a cow looks over a gate.

---

**End of Round 1.**

Off to your left there's a great deal of thrashing where Ruhi has the other one under, and it stops being thrashing and starts being something more purposeful — he's got a hand in her ruff and he isn't panicking, because he isn't breathing either.

Gardwen arrives at a dead run and comes up short beside you, staff out, seeing the sandy one's arm.

Nerissa is twenty yards back with the mace up. The Swords are flanking wide.

**Round 2 — everyone refreshes to 3 Action Points.**

Sandy is a foot away from you with his back half-turned. Ruhi is losing hers under the water.


===== USER [2026-09-06T17:55:00.571Z] =====
Check the rules. How many active attacks per round?


===== ASSISTANT [2026-09-06T17:55:37.379Z] =====
I got it wrong, and the rule is unambiguous:

> **"On their turn a combatant spends 1 Action Point on ONE Proactive Action — one per round, no more (Mythras Imperative has no extra action cycles). Remaining AP may only be spent on Reactive Actions (Parry, Evade, Interrupt)."**

**One attack per round each.** AP above that buys *defences only*.

So two of the attacks I ran in Round 1 shouldn't have happened: the billhook-man's follow-up dagger, and Sandy's final undefended lunge. Both were second proactive actions in the same round.

Both missed, so nothing has to be un-wounded. The corrected Round 1 is:

| | Proactive (1 only) | Reactive |
|---|---|---|
| **Billhook (19)** | billhook swing — missed | — *(you disarmed him on the parry differential)* |
| **Magda (16)** | staff → Sandy's right arm, **major wound** | parried billhook, parried Sandy |
| **Sandy (16)** | dagger — you parried it | parried your staff |

Which also means **you never actually ran out of defences** — you spent 2 AP on two parries and had your third plus Artful Dodger still in hand. That grim moment where he was a foot away and you had nothing left was my bookkeeping, not the fiction.

*(Note your sheets carry 3 AP, not the 2 the rules piece quotes for ordinary folk — the sheet governs.)*


===== ASSISTANT [2026-09-06T17:55:50.004Z] =====
**Round 2.** Everyone back to 3 AP, initiative persists: Billhook **19**, Sandy **16**, Magda **16**.

---

The standing position:

**Sandy** is a foot from you with his back half-turned and his right arm hanging in two places. He has not bled and he has not slowed.

**The billhook-man** is under the water with Ruhi on top of him. He got a hand into her ruff on the way down and he isn't struggling for air, because he doesn't seem to need any — he's just methodically working that hand deeper while she thrashes.

**Gardwen** is at your shoulder, staff out, and she has seen what's happening to her wolf.

**Nerissa** is twenty yards back with the mace. **Corvin and Ash** are coming wide on both flanks.

And on the slab behind them, the uncovered cut stone sits in the dark with its carving running down under the water.

Billhook-man acts first — but he's fully occupied drowning a wolf that won't drown him back.

Your move.


===== USER [2026-09-06T17:57:13.369Z] =====
Take billhook’s head off


===== ASSISTANT [2026-09-06T17:57:33.517Z] =====
He's face-down in three feet of black water with a wolf on him, both hands busy, and no idea you exist.

Striking down into a thrashing boil with Ruhi in it — **Berserker, Hard (85 → 57)**, and he gets no defence at all. If the differential gives you a special effect, you're spending it on **Choose Location**.


===== ASSISTANT [2026-09-06T17:57:51.232Z] =====
**53 against 57 — you hit, and the special effect is yours, so the head is where it lands.**

**Damage: 1.**

One. On a d8.

---

You get the staff up and bring it down two-handed into the boil — and the water takes almost all of it.

That's what water does. Six feet of seasoned ash coming down with your whole weight behind it, and by the time it reaches him it's slowed to nothing much at all, and it catches him across the back of the skull with a dull knock, like dropping a log.

His head goes down an inch into the mud. That's it.

A minor wound. He barely registers it.

But it *does* something — because for the first time all night one of them does something that isn't smooth. The hand in Ruhi's ruff loosens, just a fraction, and the wolf gets her hindquarters under her and rips backwards out of his grip with a great sheet of water and half his sleeve.

She comes up snarling in a way you have not heard from her before, and there's meat in her teeth, and she doesn't retreat — she plants and waits for him to surface.

He does. Slowly. Face-down first, then rolling.

He sits up in the water with the back of his head split and no expression at all, and says:

"Oh — that was the wolf, was it."

**You've 2 AP left. He has 3.**


===== USER [2026-09-06T17:58:45.481Z] =====
What is next?


===== ASSISTANT [2026-09-06T17:59:17.664Z] =====
Initiative re-rolled with the new arrivals, and it holds from here:

**Gardwen 25 · Sandy 22 · Billhook 16 · Magda 13 · Ruhi 13**

You've had your proactive action this round — the staff blow. Two AP left, reactions only.

Gardwen goes first, and she's watched a man hold her wolf under water.

**Hold Person on Sandy — Piety 87.**


===== ASSISTANT [2026-09-06T17:59:40.719Z] =====
**Gardwen 71 against 87. Sandy 13 against 42.** Both succeed — so it goes to the higher roll that still made it, and that's Gardwen by a distance.

---

She doesn't shout it. She puts one hand out flat toward him and says three words in the old tongue, and the water between them goes still in a ring.

Sandy stops.

Not slumped — *stopped*, mid-step, with his weight forward and his one good hand half-raised and the ruined arm still swinging gently from the momentum he had a second ago. It swings, and slows, and hangs.

His eyes go on moving. They track from Gardwen to you and back.

Something in him is furious about this, and none of it reaches his face.

"Ohhh," he says. Just that. Perfectly pleasant.

Gardwen has gone white. "It shouldn't hold," she says. "Magda — that's *Hold Person*. There shouldn't be enough person in him to grip."

---

**Billhook's turn — 16.**

He gets up out of the water with the back of his head open, and he doesn't go for the wolf, and he doesn't go for the priestess coming up behind.

He comes for you. Empty hands, straight in, fast.

**Two AP in hand. Parry, or evade?**


===== USER [2026-09-06T18:00:49.637Z] =====
Parry. Trip him up


===== ASSISTANT [2026-09-06T18:00:59.661Z] =====
He's lost the dagger in the water with Ruhi. Bare hands, and coming fast.


===== ASSISTANT [2026-09-06T18:01:22.968Z] =====
**His 46 against 48. Your parry 89 against 85 — late by four.**

The special effect is his.

---

You get the staff across in time and it's a fraction slow, and he doesn't try to hit you at all. He goes *through* the parry and takes hold.

One hand closes on the staff. The other closes on your left forearm, above the wrist, and it is like being gripped by a piece of machinery — no squeeze, no threat, just a closing to a fixed position and then no further movement at all.

Your armour turns what little force there was. You aren't hurt.

You are, however, held.

And you have felt a great many hands in seventy years and none of them were this cold through wet wool.

He doesn't pull. He doesn't twist. He just holds you there and turns his head and calls, conversationally, to nobody in particular:

"I've got this one."

And behind you, frozen mid-step with his arm hanging in two pieces, Sandy says quite clearly:

"—good."

**One AP left. Ruhi's turn is next, and she's still planted three feet away with his sleeve in her teeth.**


===== USER [2026-09-06T18:02:12.068Z] =====
Break his hold


===== ASSISTANT [2026-09-06T18:02:27.382Z] =====
Careful — you've already spent your proactive action this round on the staff blow, and **Struggle is proactive**. One per round. Your last AP is a reaction only.

Let me check what Luck can do here rather than guess:


===== ASSISTANT [2026-09-06T18:02:51.224Z] =====
Luck won't buy you a second proactive action — it grants **+1 AP**, and the one-action-per-round limit is separate. It *would* let you re-roll a die, but the parry's already resolved.

So you're held until your turn comes round again.

**Ruhi's turn — 13.** He has both hands on you, which means he has none for her.


===== ASSISTANT [2026-09-06T18:03:07.240Z] =====
**Ruhi: 70 against 85 — in. Two damage to his left leg, and the special effect is hers.**

She takes **Trip**.

---

She doesn't go for his throat. She goes low, takes the leg at the back of the knee, and *pulls* — forty stone of wolf against a man standing in three feet of water with both hands committed to holding an old woman.

He goes.

And because he will not let go of you, you go with him.

You both come down into the black together, and the water closes over the pair of you, and his grip on your forearm does not change by a hair the whole way down.

Under there it's silent, and cold, and absolutely black.

He is not struggling. He is not trying to hold you down. He is simply lying on the bottom of a drowned street holding on, waiting, because he does not need to breathe and he has all night.

Your face is about eight inches under.

---

**End of Round 2.** Round 3 begins, and everyone refreshes.

Your turn comes at **13** — after Gardwen at 25, Sandy at 22, and him at 16.

Three fresh Action Points and your proactive action back. Gardwen is above the water and can see exactly where you went in.


===== USER [2026-09-06T18:06:13.534Z] =====
Ok let me know what happens


===== ASSISTANT [2026-09-06T18:06:25.058Z] =====
**Round 3.**

**Gardwen — 25.** She saw exactly where you went in, and she has a spell for a thing that will not let go.

**Command.**


===== ASSISTANT [2026-09-06T18:06:42.848Z] =====
**Gardwen 14 against 87. He fails his Willpower at 89 against 42.** It isn't close.

---

She's up to her waist in it with both hands in the water and she puts everything she has into one word.

You feel it happen through his arm before you understand it. The hand on your forearm opens — all four fingers at once, like a catch releasing — and the hand on the staff opens too, and you come up off the bottom into air and lamplight coughing canal.

He sits up in the water beside you with his hands open in his lap, palms turned upward, and looks at them.

"That wasn't me," he says, with what might almost be interest.

---

**Sandy — 22.** Still held. He hasn't moved since Gardwen's ring of stillness went round him and he doesn't move now.

**Billhook — 16.** He gets up. He doesn't come at you again — he wades, unhurried, toward the slab and the uncovered stone behind it, with his hands still open at his sides.

Nerissa is between him and it, and she doesn't move, and neither does he.

They look at each other across four feet of black water.

Then he says: "You're the Lady's, aren't you."

And Nerissa says: "I am."

"Good," he says. "She'll want to see this."

And he steps sideways, out of her path, and gestures with an open hand at the cut stone they've spent a day digging out of the weed.

**Your turn. 13. Three Action Points, a staff, and a great deal of canal in your lungs.**


===== USER [2026-09-06T18:09:46.536Z] =====
Step forward. Lean in like I’m swinging a bat and take his head off (again)


===== ASSISTANT [2026-09-06T18:09:57.766Z] =====
He's standing in the open with his hands empty and turned outward, mid-gesture, not defending himself at all.

**Berserker, Easy (85 → 128), no defence.** And the differential will hand you a special effect to put it where you want it.


===== ASSISTANT [2026-09-06T18:10:17.098Z] =====
**75 against 100 — in. Eight damage on a d8. Head: −4 of 5. Serious.**

---

You come out of the water and you don't say anything, and you plant your back foot in the mud and you swing the way you'd swing at a fence post that had offended you.

Six feet of ash across the temple. Nothing between it and the bone.

His head goes sideways past where a head goes. He drops where he stands, straight down, no stagger, and the water takes him with a slap and closes over.

Nerissa doesn't move. She's still standing exactly where she was, mace up, four feet away, with her mouth slightly open.

The body doesn't float.

---

Silence. Then Ash says "*Lady*—" from somewhere off to the left and stops.

Sandy is still frozen mid-step with his ruined arm hanging, and his eyes have moved to the patch of water where the other one went down, and they stay there.

Nerissa lowers the mace slowly.

"He had stopped," she says. Not accusing. Just stating it, like a woman reading a figure back to check she has it right. "He had stopped, and he was showing me the stone."

Behind her, uncovered out of a day's digging: five feet of deep-carved slab, older than the drowned street it sits under, with the work running down into black water where you can't follow it.

And Gardwen, quietly, from your shoulder:

"Magda. That one's still holding."

She means Sandy. She means the spell has a duration, and she can feel it running.


===== USER [2026-09-06T18:11:26.367Z] =====
Go over. Break his other arm


===== ASSISTANT [2026-09-06T18:11:35.459Z] =====
Held, helpless, and the spell is running out. **Easy (128), no defence, location chosen.**


===== ASSISTANT [2026-09-06T18:11:57.968Z] =====
You're spent — the killing blow was your action for the round. You have to wait for the beat to come round again, and everyone watches you do it.

Nobody stops you.


===== ASSISTANT [2026-09-06T18:12:14.759Z] =====
**26 against 100. Three damage — 1 hit point left in it. A minor wound.**

Not broken. Bruised to the bone, but the arm still works.

---

You take the swing while he's frozen and you don't get the crack you wanted. The staff comes down across the forearm and he doesn't flinch — held men can't — and it isn't enough. He'll have the use of that hand.

He watches you do it. That's the thing. He is frozen at the neck and below and his eyes follow the staff all the way down and back up to your face, and there is *still* nothing in them.

"You've done that twice now," he observes.

---

Nerissa comes through the water and stops beside you, and she looks at the man who cannot move and the arm that hangs in pieces and the new bruise beside it.

She doesn't take hold of your arm. She's careful not to.

"Magda." Very level. "The other one had put his hands down. I don't say you were wrong — I don't know what these things are and neither do you. But I will not stand here and watch you take a helpless man apart piece by piece, so tell me plainly what you want him for, and then we'll do that thing and stop."

Behind her, Corvin and Ash have got a rope out and are looking at each other about who goes first.

Gardwen says: "The hold's got about a minute left in it. Maybe less."


===== USER [2026-09-06T18:14:36.033Z] =====
I’m a berserker. That means I fight until someone convinces me to stop. Nerissa’s insight would likely be able to spot that by now.


===== ASSISTANT [2026-09-06T18:14:44.146Z] =====
**Nerissa — Insight (80).** She has been watching you since the temple.


===== ASSISTANT [2026-09-06T18:15:01.387Z] =====
**4 against 80. Critical.**

She doesn't just read you. She reads you *completely*.

---

Whatever she was going to say next, she doesn't say.

You watch her change her footing. She stops standing like a woman about to remonstrate and starts standing like a woman at the side of a horse that's still running.

"Ah," she says. Very quietly. "*Ah.* You're not deciding anything, are you."

She lowers the mace all the way and lets it hang.

"I've seen this twice. Once in a man at the Shoals after a fire, and once in my own father." She keeps her voice completely even — not soothing, not raised, the pace of someone reading a list. "You're not cruel. You've simply not been given a reason to stop yet, and nobody in this water has thought to give you one, they've only told you to."

She moves round until she's in front of you rather than beside you, slowly, so you can see her do it.

"So. Here's the reason.

"**Sana is in a boat forty yards behind us**, nineteen years old, with her hair cut off, watching. That girl has spent a day and a half in a hole in the dark being brave, and what she can see from there is an old woman breaking a man who can't move.

"That's it. That's the whole reason. Not the man — he's nothing to me and I'd hang him tomorrow. **Her.**"

She holds out one open hand. Not to take the staff. Just open.

"Come and stand by me and let the Swords put the rope on him. He's got no arms left worth the name and there's a minute of your friend's magic left to do it in."

Behind her Corvin is already moving, rope in hand, watching you and not the prisoner.


===== USER [2026-09-06T18:22:02.986Z] =====
Growl. Sopping wet. My face a mask of rage and hatred. 

Just stand there. Waiting. Calming down.

Let them do their thing


===== ASSISTANT [2026-09-06T18:22:21.756Z] =====
You don't answer. You don't lower the staff either.

You just stop.

Water running off you. Breathing like a bellows. Everything in your face still exactly where it was — and standing entirely still in the middle of it, which is not the same as being calm, and everyone there knows the difference.

Nobody asks you for the staff. Nerissa doesn't move her hand away and doesn't reach any closer.

---

Corvin and Ash work fast and say nothing. Elbows first, then the wrists behind, then a running loop from the wrists to the ankles so he can shuffle and not stride. They do it around the ruined arm rather than through it, which is more care than you'd have taken.

Gardwen counts down under her breath — "*—four, three—*" — and on two the ring of stillness in the water lets go and Sandy comes back to life mid-step and finds himself trussed and sitting.

He doesn't fight it. He looks down at the rope with mild interest and settles.

Then he looks up, and finds you, and smiles for the first time all night.

"You're the one who did the boy in the canal," he says. "The face like a spade. He described you before he went."

*He described you.*

The one who left before dawn in the other boat. The one who hasn't come back.

---

Nerissa has waded to the slab. She's got Ash's lamp full open and she's looking at the cut stone they dug out of the weed — and whatever she's seeing has stopped her dead, one hand flat on it, the water running off her sleeve.

"This isn't a working," she says. "This is *older* than the working. They didn't bring this here."

She looks up.

"They came to Lost Isle to find it."


===== USER [2026-09-06T18:34:58.793Z] =====
These fuckers are necromancers. 

OK then.

What is in the hole?


===== ASSISTANT [2026-09-06T18:35:13.265Z] =====
"Necromancers," Nerissa agrees, without looking up. "Or people working for one. That's a word for the courts, though. It doesn't tell you what they *want*."

She goes down on her knees in the water beside the slab with the lamp held low, and puts both palms on the carving, and closes her eyes.

**Nerissa — Piety (92).**


===== ASSISTANT [2026-09-06T18:35:52.563Z] =====
**Lore (Water spirits): 59 against 80 — she has it.**
**Lore (Theology of the Lake Lady): 96 against 88 — she doesn't.**

She can tell you exactly what it *does*. She cannot tell you what it *means*, and you watch that bother her more than the corpse in the water.

---

"It's a door," she says.

She traces the carving with two fingers, following it down, and her hand goes under the surface and keeps going.

"Not for people. For the drowned. There are — " she searches for it "— there are old stories about the Northern Isles going under. Not one flood, a slow one, over generations, and everything in them that died went down with the streets." Her fingers stop. "And whoever cut this cut it so that what stayed in the water had somewhere to *go*. A way out. You lay them to rest through a thing like this."

She looks up at you, and there's something urgent in it.

"It isn't a Lady-stone. It's older than her presence in this channel and it isn't in any doctrine I've read in forty years, and I could not tell you who cut it or to what."

Then she stands, and takes the lamp, and holds it out over the cleared patch.

And you see that it isn't a slab at all.

It's the top of a **stair**.

Four steps showing, cut into the same worked stone, going down at an angle and disappearing into black water that does not reflect the lamp the way the rest of the channel does. Weed hangs off the edges where they've hacked it away. The steps are *swept* — there's no silt on them, and there should be a foot of it.

Something has been using them.

Behind you, roped and sitting in the shallows, Sandy says pleasantly:

"That's what he went to fetch the boat for. You'd best hurry — he's been gone since before dawn, and he'll not be coming back alone."


===== USER [2026-09-06T19:00:19.793Z] =====
Let’s get out of here. 

Did we tell Nerissa about Gardwen and her brother? If not, we should do that. 

They’re raising the drowned just like our two chatty friends here


===== ASSISTANT [2026-09-06T19:00:58.564Z] =====
You did — it was in the mouthful you gave her at the temple, right after the pigs: *the dragon knights kidnapped her brother ten years ago and are hosting a shade in him for the tourney.* She's had it since midnight. I simply hadn't written the edge, so the graph disagreed with the fiction. Fixing that now, along with what you've just worked out.


===== ASSISTANT [2026-09-06T19:01:29.473Z] =====
You say it out loud on the way to the boat — *they're raising the drowned, same as these two* — and Nerissa stops walking.

"Say that again."

"They don't bleed. They don't breathe. Ruhi had that one under for a good half-minute and it did nothing to him. They talk like one man with two mouths." You nod back at the trussed thing in the shallows. "And her *Hold Person* took. Gardwen said it shouldn't. There's enough person left in him to grip and not enough to bleed."

"And there is a door for the drowned dead under this island," Nerissa says slowly, "which they have been digging out for a day."

She looks back at the swept stair going down into water that doesn't hold the lamplight.

"They're not raising them, Magda. They're *shopping*."

---

Sandy comes with you.

He makes no objection at all. Corvin and Ash get him up between them and he shuffles down the drowned street in his hobbles with his ruined arm swinging, entirely cooperative, and settles into the bottom of the boat like a man taking a seat at an inn.

Sana pulls her legs up under her and gets as far from him as the thwart allows. Gardwen puts herself between them without being asked.

Ruhi will not get in the boat while he's in it. She swims.

---

Halfway across, in the dark, he tips his head back and looks at the sky, and says to nobody:

"You'll want to ask me things."

Nobody answers him.

"That's all right," he says comfortably. "It's a long way to morning."

Behind you, Lost Isle goes back to being a low black nothing on the water. No light on it now.

And ahead, past Corbie's and its one lit window, the sky over the Forge Quarter has that first grey suggestion in it — because it's coming up on **d-1**, and the Lake Lady's Tourney is the day after.


===== USER [2026-09-06T19:04:09.892Z] =====
So. What’s your name? What’s your story?


===== ASSISTANT [2026-09-06T19:04:31.338Z] =====
He thinks about it. That's the unsettling part — he actually has to.

"Ellick," he says at last. "Ellick Sarn. That's — yes. That's right, I'm fairly sure. I poled the Forge Quarter run. Timber mostly, sometimes charcoal, and a woman called Tam who I think was—"

He stops. Frowns very slightly at the sky.

"There was something about Tam. It's gone."

The boat creaks. Ash rows.

"They came to me in the winter. Not the young lord — the *quiet* one, him that's gone for the boat. He asked did I know the Northern Isles and I said better than any man breathing, which was true, and he paid me eleven marks to take him out to the drowned streets four times and say nothing." A pause. "I did say nothing. I want that noted. I kept my end."

"And then?"

"And then on the fourth time he said, would I like to not be cold any more."

He says it perfectly evenly.

"I've been cold on that water for thirty-one years, missus. Every winter. Hands gone the colour of the sky. And he said it like he was offering me a coat." His head tips a little. "And I said yes. That's the part everyone wants to skip past. Nobody did anything to me that I didn't stand still for."

Sana has both hands over her mouth.

"What went in you?"

"Something out of the stairs." A shrug that moves the whole trussed body oddly. "It's not unkind. It doesn't want anything much. It likes the digging." He considers. "It's got a lot more of me than it had at Candlemas. That's the trade — it warms you and it *wears* you, and you don't notice the wearing because the part that would notice is the part it's wearing."

Then, conversationally:

"You'll be wanting to know about the one on the ship. That's a different thing entirely. That one's *furnished*."


===== USER [2026-09-06T19:04:33.196Z] =====
What are you fuckers up to?


===== ASSISTANT [2026-09-06T19:04:58.155Z] =====
"Us?" He seems mildly amused by being included. "I pole the boat and I lift the stone. I'm not *up to* anything."

Then he thinks about it properly, because he's been asked, and answers with the flat helpfulness of a man giving directions.

"The quiet one wants the door open. That's the whole of the digging. Four days, and it wants to be open before the Tourney and not after — he was very hard about that. There's a tide thing in it. He said something about the water being *thin* on the day and it having to be while it's thin."

Nerissa's head comes round.

"He said *thin*?"

"His word." Ellick shifts against the ropes. "And the door's for taking something *out*. That's the bit I did understand, because I asked him — I said is this for putting things in, like you did with me, and he laughed. Only time I saw him laugh. He said no, Ellick, that's the easy way and any fool with a knife can do that. He said the hard thing is getting one *out* whole and putting it somewhere better."

He nods at the boat's wake as if that settles it.

"Because you can't keep a thing in a boy for ever. He said that too. They wear through. He said the one they've got has nearly used up what it was put in."

He turns his head and looks straight at Gardwen for the first time.

"That's why they came here. It's not a rescue they're worried about, love. It's a **removal**. He's outgrown the boy and they've somewhere better to put him."

And Sana, very quietly, from the far thwart:

"...The girls with the red hair aren't for the demon. They're spares."


===== USER [2026-09-06T19:07:14.232Z] =====
What about the furnished one on the boat? Who’s that then?


===== ASSISTANT [2026-09-06T19:07:35.176Z] =====
"Ah." Something changes in his voice. It's the first time all night he's sounded like he minds a thing. "That one."

He's quiet for a moment.

"Mine's *content*, see. It got a boatman who was cold and it's warm now and it likes lifting stone. There's no fight in it. That's why I'm still able to sit here and talk to you about Tam and nearly remember her."

He nods forward, north-west, toward where the black hull sits steaming at its pier.

"That one *fights*."

Ash has stopped rowing. Nobody tells him to start.

"I was aboard twice, carrying. You can hear it through the deck. Not screaming — worse than that, it's *arguing*. Goes on for hours. Two voices out of one throat having a row, and one of them's a boy and one of them isn't, and the one that isn't sounds like a man who's been told to do something he thinks is dishonourable." He shakes his head slowly. "That's what the morning cut's for. It's not just the wear. It's to keep it *tired*. You bleed a man to keep him from arguing."

Gardwen makes a small sound and puts her hand over her mouth.

"They've a name for it," Ellick says. "Old-sounding. The quiet one says it like a title, not a name." He works his jaw, hunting for it. "Thoo— *Thuban*. Thuban something. Eta, maybe. He's a knight out of the dragon wars and he's been in one thing or another for a very long while, and he doesn't want to be, and he never has."

He looks around the boat at all of you.

"You keep saying *rescue the boy*. I'd think about that. There's two in there, and only one of them's been asking to get out."


===== USER [2026-09-06T19:10:57.939Z] =====
Thuban? You sure? That’s the dead knight? That’s who we need to lay to rest for my Goddess. That’s Hel’s command:


===== ASSISTANT [2026-09-06T19:11:15.206Z] =====
Ellick looks at you with mild interest.

"Couldn't say what your goddess wants, missus. But that's the name."

---

Nobody rows. The boat drifts.

Nerissa says it first, slowly, the way you'd read something off a wall.

"Eleven nights. A knight in dragon-scale who is already dead and does not know it." She turns to look at you. "And *lay the dragon warrior to rest*. Not the boy. She never once showed you the boy."

"No."

"She showed you the **passenger**." Nerissa's hand has gone to her breast. "Magda — your goddess has been telling you the answer since before you left home and none of us could hear it because we were all looking at the child."

Gardwen has gone absolutely still in the bow.

"Say the rest of it," she says. "Say it out loud so I've heard it."

Nerissa does.

"If Thuban Eta is laid to rest, he leaves. And whatever is left in that body is your brother, and only your brother." A pause. "It is not a rescue. It's a *funeral*. And the boy walks out of it because the funeral wasn't for him."

---

Ellick, helpfully, into the silence:

"That's what the door's for, mind. Same door. Only the quiet one wants him lifted *out and moved*, and you want him lifted out and let *go*."

He settles more comfortably against the thwart.

"You'll be wanting the same night and the same stair as him, then. And the same thin water."

The sky over the Forge Quarter has gone properly grey now.

**One day. The Tourney is tomorrow.**


===== USER [2026-09-06T19:23:06.412Z] =====
What are you talking about? Makes no sense to me


===== ASSISTANT [2026-09-06T19:23:24.123Z] =====
Nerissa hears the tone and stops using her temple voice.

"Right. Plainly."

She holds up one finger.

"There is a dead man stuffed inside Gardwen's brother. Has been for years. He's the thing that makes the boy a champion — he's the swordsman, not the child."

Second finger.

"He's worn the boy out. You can't keep meat in the same barrel for ever, it goes. So the Baron needs him **out** and into something fresher before he ruins the one he's got."

Third.

"There's exactly one way to get a dead man out of a living body whole. That stair on Lost Isle. It's a door. That's what those two have been digging for four days."

She drops her hand.

"So the Baron's man opens the door, takes the knight *out* of your girl's brother, and shifts him into a new body he's picked out. Probably one of the four girls whose hair was in that boy's coat. That's a **removal**, and it's the day after tomorrow because that's when the water goes thin enough to do it."

She lets that sit for a beat.

"Now. Your goddess wants the same door, the same night, the same knight — and she wants him taken out and *put in the ground* instead of moved house."

She looks at you.

"It's the same job, Magda. Right up until the last moment, it's the *identical* job. Get the dead man out. The only difference is what happens to him in the second after that, and whether there's a new girl standing there waiting to be filled."

Gardwen, from the bow, without turning round:

"And either way my brother comes out of it empty. Alive, and empty, and his own."

Ellick nods along, agreeable as anything.

"Told you it was a funeral."


===== USER [2026-09-06T20:17:17.732Z] =====
We're gonna have to fight them here. Hell's teeth. If they know who I am, I'm gonna need better weapons. And What are we gonna do?


===== ASSISTANT [2026-09-06T20:17:50.446Z] =====
"They know an old woman with a face like a spade did for the young lord," Nerissa says. "That's what he carried away. Not your name, not where you sleep."

"That'll do it in a city this size."

"It will by tomorrow." She doesn't soften it.

---

Then she starts counting things off, and you realise she's been doing this in her head since the stair.

"Weapons are the easy part. **The Swords of the Lake have an armoury** and I have the key, and you may take anything in it that you can lift, which I suspect is most of it. Mail, a helm — you're bare-headed and you have been all night, which I've been trying not to look at. And something with an edge, because that staff is a fine thing but you have twice tonight needed to *end* a man and had to hit him four times to do it."

Second.

"Marisette has money, the Pearl, and Crowbill if she wants him. Hesper knows what a working looks like. Ann Yannick sees that ship's bedding every morning at first light and will go on looking. That's not nothing — that's eyes on the boy, daily, until tomorrow."

Third.

"And the Governor's household can be reached through Emeric, who is not wicked, only young and badly advised. If I go to him with a demon-marked ring, a dead courtesan's binding and my own niece's *hair*—" her jaw sets "—he will not be able to sign his way out of it twice."

She stops.

"But here's the thing none of you have said out loud yet."

She points back over the stern, at the low black shape of Lost Isle going away behind them.

"**We hold the door.**

"They cannot do their removal anywhere else, and it must be tomorrow, and it must be at that stair. They have to come to *us*. And they will come with everything they have, and their boy is a champion who fights with a dead knight's hands.

"So. Do we hold it — or do we break it, and make the thing impossible for everybody, mine and theirs alike?"

Gardwen's head comes up sharply at that.

Dawn's coming up grey behind the Forge Quarter smoke.


===== USER [2026-09-06T20:23:38.711Z] =====
Snort. Consult your godess. I know what mine would say. 

We hold the gate. We go get the boy. And we do it fast before they have time to move him


===== ASSISTANT [2026-09-06T20:23:53.125Z] =====
Nerissa doesn't answer you. She puts both hands over the side into the channel, and she stops moving for a long moment, and the water round the boat goes glassy in a way that has nothing to do with the wind.

**Lore (Theology of the Lake Lady) — 88.**


===== ASSISTANT [2026-09-06T20:24:18.386Z] =====
**38 against 88.** She gets an answer, and it isn't the one she wanted.

---

She takes her hands out of the water and looks at them.

"She says the door isn't hers."

"Meaning?"

"Meaning she won't tell me to break it, and she won't tell me to hold it." Nerissa's voice is tight. "It was cut before her. It's not in her gift. What she *will* say —" and she stops, and starts again, more carefully "— is that the water goes thin tomorrow whether we like it or not, and that a thing left in the wrong place too long spoils what's around it. Which is not an instruction. That is a woman telling me the milk's turning and leaving me to deal with it."

She snorts, and it's very like your snort.

"Fine. Then we do it your way, and I'll answer for it later."

---

It comes together fast, in a rowing boat, in the grey.

**Hold the stair.** Nerissa's Swords, and whatever Marisette and Crowbill will lend, and Lost Isle is a rock two hundred yards across with one landing worth the name. Ellick's punt is on the north side and their only other boat is with the quiet one.

**Take the boy today.** Eight aboard — fewer if any went with the quiet one before dawn. Ann Yannick goes up that pier at first light every morning, is handed a bag at the bollards, and walks away, and nobody has ever once looked at her twice.

**And Hesper comes**, because Gardwen can hold a person and you can break one, and neither of you knows the first thing about lifting a dead man out of a living boy.

Gardwen is already saying "*today*, we go today—" and Nerissa is saying "not without Hesper and not without Marisette's men," and both of them stop and look at you, because it's your plan and they're arguing about your plan.

The boat touches the water-stair at Corbie's.

Behind you, comfortably, Ellick says: "You'll want to be quick. He's been gone eleven hours and it's four to the border tower and back if the wind's kind."


===== USER [2026-09-06T20:24:20.120Z] =====
Maybe you can ask the prince if he wouldn’t mind


===== ASSISTANT [2026-09-06T20:24:40.874Z] =====
Nerissa stops with one foot on the water-stair.

"...Say that again."

"Ask the prince. He's the one signed the paper. Ask him to unsign it."

She comes back down the step.

"Magda, I have been so angry with that boy for a day and a half that it did not once occur to me to *use* him." She says it like a woman finding a tool she'd thrown across the room. "And he's the only person in Purewater who can make any of this **lawful**."

She's counting again, fast.

"With a Governor's warrant, holding Lost Isle isn't twenty armed men on a rock — it's the *Watch* posting a cordon, and nobody has to explain themselves. And going aboard that ship isn't a raid, it's a **search**, and eight Dragon Knights at a pier cannot lawfully refuse it in a treaty port without their master forfeiting the Tourney entry on the spot."

Gardwen: "And if he says no?"

"Then he's told the Baron by noon and we've lost surprise and the day." Nerissa doesn't dress it. "That's the wager. He's twenty-four, he's frightened of his council, and he signed that instruction because three grown men told him it was the polite thing to do. He is not wicked. He is *weak*, and weak men can be moved — the question is who gets to him last."

She looks at Sana, wrapped in Gardwen's cloak with her hair hacked off, and then back at you.

"Although. I've a niece with shears-cut hair, a ring with a worm on it, and an old woman who'll say the word *pigs* to his face."

The sun is properly coming up now.

"He holds audience at the ninth bell. That's four hours. Do we spend them on him — or do we spend them getting to that ship before the quiet one gets back?"


===== USER [2026-09-06T20:28:17.393Z] =====
Action. We go now. 

I’m not good at waiting or asking permission


===== ASSISTANT [2026-09-06T20:28:38.998Z] =====
Nerissa doesn't argue. She splits it instead.

"Then I'll do both. **Lilura** goes to the Prince — she's temple, she's presentable, and she can hold a room for an hour without saying anything actionable." She's already writing on the boat's thwart with a stub of chalk. "She'll carry the ring and Sana. If he moves, the warrant follows us out to the pier. If he doesn't, we were going anyway."

Sana starts to object about being used and Nerissa says "you *will*" and that's the end of it.

---

The temple armoury is a stone room under the colonnade with the smell of oil in it, and Nerissa unlocks it at a run and stands back.

"Take it. Argue with me about the cost afterwards."

It's Swords of the Lake kit — blue-green over mail, decent, maintained.

- **A hauberk**, riveted mail, and a **coif**. Heavier than anything you've worn in thirty years.
- **A kettle helm** with a broad brim, plain.
- **A war axe** — single-handed, bearded, a hand-and-a-half haft. Somebody's, once. It's been sharpened a great many times.
- **A short-hafted mace**, like Nerissa's.
- **A boar spear** with a crossbar behind the head, for stopping something that keeps coming.
- Half a dozen **javelins** in a rack.
- And a **shield** — a round one, oak and hide, banded.

Your staff sling is still on your belt with seven stones left in the pouch.

And outside, the light is coming up over the Forge Quarter — which means **Ann Yannick is walking up that pier with an empty barrow right now**, and will be handed a bag at the bollards, and will walk away again.

That happens once a day and it is happening in about twenty minutes.


===== USER [2026-09-06T20:30:41.447Z] =====
Check my artful dodger skill. What’s the heaviest armor I can wear and still use it


===== ASSISTANT [2026-09-06T20:31:12.851Z] =====
Your sheet answers it exactly:

> **Artful Dodger — 1 extra action for parry/evade if ENC < 26**

**Current load: 12.** You have **13 points of headroom.**

Right now you're in **ringmail, AP 3 on all seven locations**, and bare-headed. Swapping up to the hauberk and coif (AP 5-ish on the covered locations) plus the kettle helm, and adding the axe and shield, lands you somewhere around **20–22** — still comfortably under 26. **You can take the lot and keep the extra reaction.**

What would cost you it: hauberk *plus* shield *plus* boar spear *plus* javelins *plus* everything else. Pick a fight's worth, not an armoury's worth.

---

Two other things on that sheet I have not been using, and one of them is about to matter a great deal:

**Berserk Rage** — 14 rounds, and while it's up:
- Damage modifier **+1d2**, and your weapon counts **one size step larger**
- You take **half damage**
- **Immune to serious wounds and fatigue**
- Endurance, Willpower and Brawn rolls all **one grade easier**
- Parry and evade **one grade harder**
- You cannot retreat, and must always engage
- When it ends: automatic **1 Fatigue level** loss

That's what a berserker is, mechanically, and I've had you fighting all night without it.

**Eyes in the Back of Your Head** — attacked from behind, a Formidable Perception check lets you turn for 1 AP.

**And you can detect magic and illusions using Willpower (63)** — which, for a woman with Fear of Arcane Magic 54, is a nasty little gift.

Ann Yannick is walking up that pier. What are you taking?


===== USER [2026-09-06T20:34:10.117Z] =====
I like that axe. Let’s use that with the heavier armor and the helm. If I can still move then we’ll go with this. Keep a normal sling.


===== ASSISTANT [2026-09-06T20:35:05.897Z] =====
**Kitted.**

| | |
|---|---|
| **Armour** | Mail hauberk + coif — **AP 5** all locations. Kettle helm — **head AP 6** |
| **War axe** | **1d8+1**, size M, Bleed and Sunder |
| Quarterstaff | 1d8, kept |
| Sling | 1d8, fourteen stones |
| **ENC 17** | under 26 — **Artful Dodger stays** |

*(That's the battleaxe question from the start of the night finally answered on a sheet rather than in a rules index.)*

The mail goes on over the wet wool and it is cold and it is heavy and it settles onto your shoulders like a hand. The coif flattens your hair. The kettle helm sits low and takes the top half of the world away, which is the trade you make for keeping the top half of your head.

Nerissa watches you do up the last buckle and says nothing at all until you pick the axe up.

Then: "That was Sword-Captain Vell's. She's twenty years dead and she'd have liked you."

---

**Dawn, d-1. The Tourney is tomorrow.**

Gardwen has her staff and her sickle and Ruhi, still wet. Corvin and Ash are coming, and Nerissa is coming, and Ellick is roped in a cellar under the temple with two more Swords on the door.

Lilura has already gone for the Prince with Sana and the ring.

And forty minutes across the water, on a private pier under the Forge Quarter smoke, a laundress with a barrow is walking up to eight Dragon Knights and a barred shutter, exactly as she has every morning for four days.

You can be there before she's done if you go now.


===== USER [2026-09-06T20:50:45.343Z] =====
Say to Nerissa - this is beautiful. We used to use axes, in my tribe when I was a young woman - never wielded anything as fancy as this. Id probably have liked her too. 

Let’s go greet the day.


===== ASSISTANT [2026-09-06T20:51:19.586Z] =====
Nerissa looks at the axe in your hands, and then at you, properly.

"Tell me about the tribe's axes."

"Plainer. Ash haft, a wedge of iron, and you sharpened it on the same stone you did the scythes." You turn Vell's over. The bearded edge catches the lamp. "Nothing like this. This has been *loved*. Somebody's had that back to a smith for a new eye and kept the old head."

"Twice. Her daughter has the receipts."

"Then I'd probably have liked her too."

Nerissa almost smiles, and doesn't quite, and picks up her mace.

"Let's go greet the day, then."

---

Forty minutes on the water in the temple's own boat, going with the ebb, and the sun comes up somewhere behind the Forge Quarter and doesn't so much rise as *leak* through the smoke.

You come at the pier from the south, along the working yards. The cooperage is already going. The rope-walk is already going. The city does not know that anything happened last night on a drowned island, and will not care.

The **DragonBarge** sits where it sat: black, dragon-prowed, and steaming along its whole waterline into a dead-water slick.

And she's there.

**Ann Yannick**, empty barrow, coming up the pier at a working woman's pace with her sleeves already rolled. Thirty yards from the bollards.

At the pier head, two Dragon Knights. At the top of the ramp, two more.

**Four. Not eight.**

The covered gangway aft is open, and the canvas is pulled back, and there are men moving on deck with purpose. The ship's boat is gone from its davits.

Something is happening aboard that ship this morning, and it is not the laundry.


===== USER [2026-09-06T21:02:46.018Z] =====
How many on board now? Likely it’s not going to work. Watch the action. What are they doing?


===== ASSISTANT [2026-09-06T21:02:53.458Z] =====
**Perception, Standard (70)** — from the lee of the cooperage, watching a ship that has changed its habits.


===== ASSISTANT [2026-09-06T21:03:13.531Z] =====
I wiped her skills with a stray `--skills '{}'` during the gear-up. Restoring from the package, which is authoritative:


===== ASSISTANT [2026-09-06T21:03:23.387Z] =====
All 30 restored. Nothing else on the sheet was touched — armour, axe, passions and combat style are intact.


===== ASSISTANT [2026-09-06T21:03:38.538Z] =====
**45 against 70.** You read the deck.

**Six aboard, four ashore. Ten.** Two more than yesterday — so nobody left with the quiet one; he went alone and they've brought men *down* from the house on High Isle.

And they are not going about a normal morning.

- The **covered gangway** is open because they're bringing things *up* from below, not down. Chests. A long flat case, two men to it. Something wrapped in oiled canvas that takes four.
- Two men are working at the **stern mooring**, taking turns off the bollard — not casting off, but reducing it to what one man could throw clear in a hurry.
- A knight on the quarterdeck keeps going to the rail and looking **north-west round the point**, the way the ship's boat went. Four times while you watch.
- The **barred shutter amidships is still barred**. Whatever's behind it hasn't been moved yet.
- And the **furnace smoke** off the Forge Quarter is the wrong colour. Not from the yards. It's coming off the ship, from a hatch aft, black and greasy, and there's a great deal more of it than yesterday.

That ship is being made ready to leave.

Ann Yannick has reached the bollards. A knight is coming down the ramp with the bag. She's holding out her hand for it exactly as she has every morning, and she has not looked once at the yards.

Nerissa, at your shoulder, very quietly: "They're not waiting for tomorrow."


===== USER [2026-09-06T21:24:39.770Z] =====
How many men do we have now? Not enough to take them, I’ll wager.


===== ASSISTANT [2026-09-06T21:25:00.580Z] =====
Nerissa does the sum out loud, flatly, because there's no point in dressing it.

"You. Gardwen. The wolf. Corvin, Ash, me. **Five and a dog** — and of the five, two of us are past sixty and one of us is a priest."

"Against?"

"Ten. In scale. On a deck, above us, with a ramp they can hold two abreast." She doesn't blink. "If we go up that ramp we die on it. All of us, in about a minute, and the ship leaves anyway with your girl's brother in the hold."

Corvin, who is twenty-two and brave and would go anyway, says nothing and grips his spear tighter.

"Reinforcement." She's already ahead of you. "Temple Isle is forty minutes there and forty back with a boat that isn't loaded — and I'd get you a dozen Swords. Marisette can raise more than that but she's an hour away and it'd be another hour arming them. Crowbill's faster and he'd want paying in something I haven't got."

She looks at the black smoke coming off the aft hatch.

"And that ship is being got ready *now*. She could be off that pier inside the hour and out through the Mouth on the ebb, and then it's a border tower we can't reach and a boy we never see again."

She lets it sit exactly one beat.

"So no. Not enough to take them. Not in time, not by force, not up that ramp."

---

Thirty yards away, Ann Yannick takes the bag off the knight at the bollards, hoists it onto the barrow, and turns it round.

She has been past those men every morning for five days and not one of them has ever looked at her face.


===== USER [2026-09-06T22:57:58.765Z] =====
<ide_opened_file>The user opened the file /Users/gullyburns/.claude/plans/i-want-to-rewrite-effervescent-whale.md in the IDE. This may or may not be related to the current task.</ide_opened_file>


===== USER [2026-09-06T22:57:58.765Z] =====
Nah - not today. Stupid to die for no reason. 

Turns to Nerissa - you got any scouts good enough to watch this monstronsity without getting killed?


===== ASSISTANT [2026-09-06T22:58:24.906Z] =====
"Scouts." Nerissa considers it. "Not as such. The Swords are gate-guards and processional troops and I'd not send Corvin to follow a cat."

Then she looks at the steaming waterline, and something changes in her face.

"But I don't need a scout to follow *that*."

She crouches at the edge of the yard and puts her hand flat in the harbour water, twenty yards from the slick.

"It hurts the channel wherever it sits. That's what the fouling alarm was for — that's the only reason I knew anything was wrong in this city at all." She's quiet a moment. "It doesn't stop. It can't. Wherever that hull goes it leaves a line of thin water behind it and I can feel the shape of it for as far as the Lady's water runs, which is the whole harbour, the Mouth, and a good way out to sea."

She stands and dries her hand.

"So: I cannot tell you what's on her deck. I *can* tell you where she is, at any hour, day or night, without a single person going near her. And I'll know the moment she moves."

Then, more practically:

"For eyes — **Ann Yannick** goes up that pier every morning and has already offered. **Pell** does the yards on alternate days and would do it for the price of a pie and the excitement. And Marisette can put a dozen forgettable people in these yards by noon who'll be taken for dockhands, because half of them will be."

Gardwen has been silent this whole time, staring at the barred shutter. She says, without turning round:

"And if she sails, she still has to come back."

"She does." Nerissa nods slowly. "There's one door, and it's under a rock we're sitting on, and they cannot do their business without it. Wherever that ship runs to, it runs back to **Lost Isle** before tomorrow's water goes thin."

The knight on the quarterdeck goes to the rail again and looks north-west, and this time he stays there.


===== USER [2026-09-06T23:07:05.469Z] =====
Take in the fuckers face. Is that the albino? 

“Marisette’s people should watch these guys - all the comings and goings anywhere”

Anyone we can talk to? Underworld types who might be useful?

Smile at Nerissa - mind if I hold onto the gear for now? I’ll give back when I leave the city. I have a feeling this next part will be a bit beneath you. Wink


===== ASSISTANT [2026-09-06T23:07:12.039Z] =====
**Perception, Standard (70)** — quarterdeck, forty yards, a man who has stopped moving.


===== ASSISTANT [2026-09-06T23:07:39.030Z] =====
**A 1. Critical.**

It's him.

White through the eyebrows, white to the lashes, no colour anywhere in the face — and even at forty yards through Forge Quarter smoke you can see the thing Ann Yannick meant, which is that he doesn't stand like the others. The rest of them are soldiers waiting. He's a man doing arithmetic.

And on a 1 you get more than the face.

He isn't watching for the boat. He's watching the **yards** — sweeping them, left to right, in the unhurried way of a man who has been told that somebody killed his young master and is now looking at every working figure between the cooperage and the rope-walk.

His eye goes over your position and does not stop, because five people behind a stack of barrel staves are five people behind a stack of barrel staves.

But he does it again about forty seconds later. And again after that.

He is not going to stop doing it.

---

"Aye," you say. "That's the albino."

Nerissa follows your look and swears in a way that would surprise her congregation.

"Then he is not aboard that ship this morning by accident. That's the man they send when something has gone wrong."

---

On the rest of it, she's quick.

"Marisette — yes. She'll have people in these yards by noon and she'll enjoy it. I'll send Ash the moment we're back in the boat."

"And the underworld?"

"**Crowbill.**" She says the name like a woman naming a weather system. "He owns the canals nobody draws on a chart, and if you want to know who came in and out of that pier at four in the morning, he already knows and it costs money. Marisette can introduce you — they do business.

"Or **Thorne**, at the Moist Oyster. He's not underworld, he's *older* than the underworld. Sits in the corner, buys nobody a drink, and knows every story in this city including the ones that haven't finished. He was Order of the Lake before he wasn't." She grimaces. "He'd know what a swept stair under Lost Isle means better than I do, and that galls me considerably."

---

Then you ask about the gear, and she looks at you standing there in her dead captain's mail with her dead captain's axe.

She doesn't answer for a second.

"Keep it," she says. "Bring it back when you leave the city, or don't."

And when you wink at her about the next part being beneath her, she does not smile.

"Magda. I silenced my own alarm because a boy sent me a letter." Her voice is perfectly level. "Do not tell me what is beneath me. Tell me where to be."


===== USER [2026-09-06T23:09:45.177Z] =====
Fair point milady. Sorry for the flippancy.

Thank you. I’ll be in touch


===== ASSISTANT [2026-09-06T23:09:59.948Z] =====
She accepts it with a nod and no fuss — which is its own kind of grace.

"Then we understand each other."

She's already moving, and giving orders as she goes, and none of them are to you.

"Ash — Marisette, straight there, don't stop on the Pearl for anything. Corvin, the temple: I want a dozen Swords in plain clothes on Lost Isle before dark and a boat on that landing all night. I'll go to Emeric myself if Lilura's got no further by the ninth bell."

At the boat she stops and turns back.

"You'll want Marisette for the introduction to Crowbill and she'll ask what you're offering. Have an answer before you're in the room — he's not a man you improvise at."

Then: "And Magda. When you know where to be, send to the temple. Not a message. A *name*. Whoever carries it should be able to say a name I'll recognise and nothing else, in case they're taken."

"What name?"

She thinks for a moment.

"**Vell.**"

And she steps down into the boat.

---

Forty yards away, Blau sweeps the yards again.

Ann Yannick's barrow squeaks away up the pier and nobody watches her go.

You have the morning, a purse from Marisette, a druid, a wolf, and Sword-Captain Vell's axe under a borrowed cloak.

The **Pearl** is that way — Marisette, and through her, Crowbill.

The **Moist Oyster** is closer, and Thorne is in it, and he knows what a swept stair means.


===== USER [2026-09-06T23:11:45.007Z] =====
Let’s go for a drink. Haven’t been to the oyster for a few years now.


===== ASSISTANT [2026-09-06T23:12:06.834Z] =====
The Moist Oyster hasn't changed and neither has the smell — old beer soaked into older wood, and the tide underneath it.

It's mid-morning, which in a dockside house means the night's last four drinkers and the day's first three, and nobody in between. A girl mopping. A dog under a table that lifts its head at Ruhi and thinks better of the whole business.

You're in mail under a borrowed cloak with an axe you can't quite hide, and there is a white-eyed man across the water asking after an old woman. So you take the corner with your back to the wall, out of the light from the door.

Which turns out to be a problem, because somebody is already in it.

---

**Thorne** is about seventy, dressed like a man who was once dressed better, with a cup in front of him that he isn't drinking and a stub of chalk he's been turning over in his fingers.

He watches you cross the room. He watches the wolf. He watches Gardwen decide where to stand.

Then he moves his cup six inches to the left, which is an invitation, and says:

"Sit down, mother. You've had a night."

You haven't said a word yet.

"Two nights, at a guess." He looks at the mail under the cloak, and at the mud still on the hem of it, and the particular grey-green weed dried on your boot that grows in exactly one place in this city. "One of them wet. One of them worse."

He turns the chalk over.

"I'll tell you what I've had, since you're wondering. I've had a girl in here at seven this morning saying Constantine's house has a physician in it and won't say why. I've had a lad off Renko's cart telling anyone who'll listen that some old woman knows about horses. And about an hour ago I had two of the Baron's people asking whether anybody's seen a big northern woman with a face like a spade."

He finally looks up.

"I said no. I'd like it noted that I said no *before* I knew what I was saying no about, which is the sort of thing I'll want paying for eventually."


===== USER [2026-09-06T23:23:05.027Z] =====
How about I pay you a bit more and you tell him yes, and then what I want him to hear a couple of times? 

Surprised he came in here. Was he wearing his pretty iron armor when he did?


===== ASSISTANT [2026-09-06T23:23:24.729Z] =====
"Not him." Thorne is precise about it. "Two of his — house servants in di Teufel livery, polite, one of them doing the talking and one of them looking at the room. No iron. Nobody walks into a dockside house in scale unless they want a riot, and that lot are being *careful*, which is more worrying than the alternative."

He turns the chalk over.

"The white one hasn't been off that ship since before dawn. I'd have heard. He is the only man in that retinue whose movements this city actually tracks, because he's the only one who frightens anybody."

---

Then he sits back, and for the first time there's something sharp under the tiredness.

"Now. You've just offered to pay me to tell a man a lie."

He lets that sit.

"I want you to understand what you're buying, because people usually don't. I don't sell lies, mother. I sell *stories*, and the difference is that a story has to hold up when it's repeated by an idiot in a different tavern three days later. You can't just hand me a falsehood and a coin. You have to give me something that has the *shape* of true.

"A lie collapses. A story goes and gets *itself* believed."

He picks up the cup, finally, and doesn't drink from it.

"Two conditions, and they're not negotiable.

"**One** — I'll not put a name on anybody who'd hang for it. If your story wants a body, it uses a dead one or a made-up one, never a living neighbour.

"**Two** — I'm told what it's *for*. Not everything. But enough that if it goes wrong I know whether I ought to be sorry."

He sets the cup down.

"Meet those and my price is small and strange: I want the *true* version. Afterwards. All of it, in order, told to me once and never written down."

He spreads his hands.

"So. What do you want Blau to hear?"


===== USER [2026-09-06T23:36:50.715Z] =====
Let’s just you and me tell some tales. I have a feeling you’ll figure out how you feel about the good Baron soon enough. I’m not good at lies but I love a good tale.

How about this one - a Randy young nobleman carves up a whore to possess her with some kind of lust demon… gets the charm right but botches his escape only to fall in the canal and catch a slingshot to the temple - di Teufel somehow talks to the dead … so they apparently know all this already anyway. 

That’s a start right there - wouldn’t you say?


===== ASSISTANT [2026-09-06T23:37:15.250Z] =====
Thorne goes very still while you talk.

When you finish he doesn't say anything for a while. He turns the chalk over three times.

"You've just done the thing nobody ever does," he says at last. "You've handed me the *true* one first."

He almost looks offended by how well it works.

"And it's better than anything I'd have built. Because every part of it is checkable. There *is* a physician at Constantine's. There *are* four houses on the Pearl that won't take di Teufel coin by tonight once the Pearl hears why. There *was* a young lord in that house on the night, and there are eleven people who saw him come in and none who saw him leave." He taps the chalk. "That's not a story I have to sell. That's a story that sells itself house to house and comes back to me by Thursday with improvements."

Then he holds up a finger.

"But you've a problem in it and you've walked straight past it.

"The truest version has an old northern woman with a sling in it. And there is a man on a ship asking after an old northern woman with a face like a spade." He looks at you levelly. "Tell that story as it happened and you've put your own head on the pier for him."

He turns the chalk again.

"So here's the craft of it. Everything you told me stays *exactly as it is* — the carving, the demon, the botched escape, the canal. All true, all checkable, all deadly.

"And the stone comes out of nowhere.

"He fell in the canal and *the water took him*, and the Lady's channel does not care for demon-work, and a man who profanes a Pearl house with a lust-demon and then goes into the sacred water — well." He spreads his hands. "That's not even a lie, is it. That's a *sermon*. Half this city will believe it before I've finished saying it, and the other half will believe it harder because the temple hasn't denied it."

He finally drinks.

"And on your other point. Yes. If they speak to their dead they may already know a woman did it — but they'll have *one* dead man's word against a whole city's version, and I'll tell you now which one travels faster."

He sets the cup down.

"As for how I feel about the good Baron." Something moves behind his face. "I was Order of the Lake for thirty-one years, mother. I know what a stair under Lost Isle is for. You didn't mention one. You didn't have to — you've got weed on your boot that only grows in the drowned streets, and you came in here asking about the dead."

He leans back.

"Tell me I'm wrong."


===== USER [2026-09-06T23:46:33.696Z] =====
Laugh. I’m only good at breaking things. You’re not wrong. Here’s another tale for you. Nudge Gardwen to tell her tale. May as well give you everything, you old goat.


===== ASSISTANT [2026-09-06T23:46:46.326Z] =====
Gardwen tells it. The steading, the nine of them, the counting in the morning, the ten years, the column on the north road. She tells it the way she told Marisette — no shape to it — and Thorne listens without once turning the chalk.

Then you give him the rest. The bleeding on the ship. The shade. The name.

At **Thuban Eta** he stops.

"Say that again."

"Thuban Eta. The knight in the boy."

He puts the chalk down.


===== ASSISTANT [2026-09-06T23:47:15.200Z] =====
**Lore (Dragon Kings era) — 32 against 92.** He has it cold.

---

"Thuban Eta was real," Thorne says. "That's not a story name. That's a *muster roll* name."

He's found the chalk again without looking.

"The Dragon Kings had knight-companies, and the Eta were one of them — the letter's a company mark, not a family. And Thuban was the one they teach you about at the Order in your second year, because of how he died."

He turns it over.

"He wouldn't burn a town.

"That's the whole of it. The company was ordered to fire a valley and he refused, and argued it in front of the others, and about a third of them came round to him. So the ones who hadn't took him out on the water at night to talk it over, and they put him over the side in his mail with his hands tied.

"Drowned. By his own company. For refusing an order that even *they* thought was filthy — that's the part that damns them. They knew he was right and they killed him for making them know it."

He looks up.

"And that is *exactly* the kind of dead man you can bind. You don't hold a shade with iron, mother. You hold it with the thing it can't put down." He taps his own chest. "You keep him in the moment of it. Tied hands and cold water and his own men's faces looking down at him — you keep him *there*, and he'll pull against it for a hundred years and never once get out, and every time he pulls you can use the pulling."

Gardwen says, very low: "That's what's in my brother."

"That's what's in your brother." Thorne doesn't soften it either. "And it has been in your brother for ten years, and it has hated every hour of it, because a man who wouldn't fire a valley is not going to enjoy being made into a champion."

He pushes the chalk away.

"Your goddess said *lay him to rest*, and everyone at this table has been thinking that means a door and a ritual." He looks at you. "It might not. You don't lay that man down with a stair. You lay him down by *undoing the betrayal* — by someone standing in front of him and taking it back on behalf of the ones who did it.

"The door gets him out of the boy. Something else has to make him willing to *go*."


===== USER [2026-09-07T00:01:00.177Z] =====
Thorne… that was a thousand years ago. Who the fuck could do that now. The kings themselves and all their armies were laid to rest. Every child knows that and the only ones that don’t are the di Teufel clan because they clear like the power the dragons had - and want to use it again.

Look at Magda - what the fuck girl? I don’t know what we do now? You know these ways - what do you say?


===== ASSISTANT [2026-09-07T00:01:36.322Z] =====
Thorne doesn't argue with you. He nods along.

"You're right. There's no company left to answer for it and no descendants worth the name — the Dragon Kings' whole order went into the ground and good riddance. If it wants the *actual men*, it's impossible and we may as well go home."

He holds up a finger.

"But that's not how a debt like that works. It never wanted the men. It's been a thousand years — Thuban knows they're dust. What holds him isn't a grudge against nine specific bastards. It's that **nobody ever came back for him.** He went over the side and the water closed and that was the end, and no company, no order, no god, no sister — *nobody* has stood over that water since and said 'this was wrong, and he was ours, and we're taking him home.'"

---

You turn to Gardwen.

She's been quiet a long while. When she speaks it's slow, and it's not the voice she uses for people — it's the one she used at the ford, with her hands in the water.

"There's a thing we do in the wood, for a beast that's died badly. In a snare, or under a fall, where it couldn't get free." She's looking at the table. "You don't pray it away. You go and you *sit* with it, and you say out loud that it wasn't right, and then you carry it. That's the whole rite. Somebody has to actually pick the thing up."

She looks up at you.

"It doesn't need the ones who did it, Magda. It needs somebody willing to *stand where they stood* and answer for it. To take it on. Not because it's theirs — because they're the one who turned up."

Then Thorne says, quietly, in the tone of a man laying a card down:

"And who exactly do we know that serves the god of the ones nobody sings about?"

He looks at you.

"Not the battle-dead, you said. The other kind. In the bed, in the byre, in the bad winter." He turns the cup. "A knight drowned in the dark by his own friends for refusing to burn a village, and left out of every song since, in every land, for a thousand years.

"Mother — whose *is* he, if he isn't hers?"


===== USER [2026-09-07T00:06:54.279Z] =====
Yeah!!!!

I start to get it. That’s she’d want isn’t it?

Fuck me.

Hel

The old lady has her ways. OK. I’ll do it


===== ASSISTANT [2026-09-07T00:07:14.903Z] =====
Nobody says anything for a moment.

Thorne picks up his cup and finally drinks from it, properly, like a man closing a ledger.

"Well," he says. "There it is."

---

Gardwen has both hands flat on the table.

"Then it's three things and we've got one of them."

She counts, and her voice steadies as she goes, because a list is easier than a hope.

"**The door.** We have that. It's under a rock we're sitting on and there'll be a dozen Swords on it by dark.

"**The boy at the door.** We don't have that. He's behind a barred shutter on a ship that's getting ready to sail, with ten men and the albino on it, and we already worked out this morning that we can't take him by force." Her jaw sets. "That's the whole problem and nothing about it has changed.

"**And you.**" She looks up. "Stood over the water saying it out loud and meaning it. Which costs you something, Magda, and I don't know what, and neither do you."

Thorne says, without looking up from his cup: "It'll cost her exactly what she's got. That's how those go."

---

Then he sets the cup down and becomes brisk, which from him is alarming.

"Right. Your story goes out this morning — the carving, the demon, the botched escape, the water taking him. It'll be in nine houses by noon and the Pearl will close against them by dark whether Marisette lifts a finger or not.

"And I'll add one line to it, if you'll let me, because it's true and because it will do more damage than all the rest put together."

He looks between you.

"That the Baron has entered a champion nobody in this city has been permitted to see.

"Let them chew on *that* alongside a demon in a Pearl house, on the day before the Tourney. See how many Guildmasters still want to sit in the Governor's box."

He turns the chalk over one last time.

"Now go and see Crowbill about getting a boy off a ship. And mother — when it's done, you owe me the true version. All of it. Once."


===== USER [2026-09-07T00:09:48.080Z] =====
Take my helmet off. Lean forward. Eyes on his. Headbutt him (gently).

Beserker salute

You’re a good man Thorne. I’d trust you with my tall tales any day.


===== ASSISTANT [2026-09-07T00:10:03.552Z] =====
You get the kettle helm off and set it on the table, and lean in across the cup, and touch your forehead to his.

Gently. For you.

There's still an audible knock.

Thorne sits back with his eyes watering slightly and a hand going to his brow, and he does not look at all displeased.

"*Ohh*," he says. "That's a northern thing."

"That's a northern thing."

"I've read about that." He works his jaw. "It reads considerably better than it feels."

The girl mopping has stopped mopping. The dog under the table has reconsidered its position entirely. Gardwen has put her face in her hand.

Thorne straightens his collar with enormous dignity.

"Thirty-one years in the Order," he says, "two of them at the Governor's table, and no one has ever done that to me. I've been given a chain of office and a commendation from a Prince and neither of them landed like that." He picks up the chalk. "Go on then. Get out of my corner."

And as you're standing, without looking up:

"Mother. When they ask me this morning — and they will — I'm going to say I've never seen you."

He turns the chalk over.

"That's on the house."

---

Outside, the day is properly up. Bells somewhere. Tourney bunting looking tired.

**The Pearl** is a quarter of an hour's walk, and Marisette is in it, and behind Marisette is Crowbill and the only people in Purewater who might know how to get a boy off a guarded ship without going up the ramp.

Nerissa wanted a name sent to the temple when you knew where to be.

You don't know yet.


===== USER [2026-09-07T00:12:57.938Z] =====
Let’s go back to Marisette and see this crime lord - fun


===== ASSISTANT [2026-09-07T00:13:34.128Z] =====
Marisette's counting room, mid-morning. She has not slept and it doesn't show.

She's ahead of you on nearly everything.

"Ash came at seven. I have nine people in those yards already and two on the water, and I'll know if that ship so much as coils a rope." She doesn't look up from what she's writing. "The Pearl closed to di Teufel coin at eight — I didn't even have to ask, Corliss's house did it first and the rest followed inside the hour. Your storyteller's version arrived here about twenty minutes before you did, which I'd call good work."

"The Prince?"

Now she does look up.

"Lilura is *still in the anteroom*." Her mouth is thin. "Four hours. They've given her tea twice. Emeric's council have him in session about the Tourney seating and she cannot get past a chamberlain called Vosk, who I have twice paid and who is therefore either bought harder by someone else or genuinely afraid."

She sets the pen down.

"So no warrant. Not by noon and probably not at all before tomorrow, which means whatever you do at that pier you do outside the law."

---

Then: "You want Crowbill."

It isn't a question. She's already reaching for a different paper.

"He'll see you — you're interesting, and the Pearl closing against a Baron is the most entertaining thing to happen to this island in a decade, and he'll want to know what you are." She writes two lines and folds it. "But listen to me, because Thorne will have told you the same thing and he'll have been gentler about it.

"Crowbill does not do favours and he does not do causes. He is not a good man with a code — he is a *consistent* man with a code, which is different and more useful. He'll want a price, and the price is never money. It's always something that makes his position better."

She holds out the folded note.

"So. Before you're in that room. **What are you selling him?**"


===== USER [2026-09-07T00:22:00.573Z] =====
I dunno - thievery.

I’d imagine the Baron has all manner of treasure on board that big boat. Once he’s disgraced and exiled - any loot off the barge could be sold with no fear of retribution . Give him the ring as a down payment…

Would that work?


===== USER [2026-09-07T00:22:05.579Z] =====
[Request interrupted by user]


===== USER [2026-09-07T00:22:26.931Z] =====
We steal the boy. He steals everything else.


===== ASSISTANT [2026-09-07T00:22:48.858Z] =====
Marisette sits back and looks at you for a moment with something that might be respect.

"*Yes.*"

She says it flatly, like a merchant accepting a figure.

"That's the right shape. You're not asking him for help — you're bringing him a *job* and taking the least valuable thing off it. That's a trade he understands before you've finished the sentence." She taps the desk. "And better than you know: if there are forty men on that pier tonight and every one of them is carrying a chest off, then nobody watching from the yards sees a rescue. They see a **robbery**. Which is the most ordinary thing that can happen on a dock, and the one thing nobody investigates too hard when the victim is a foreign lord who's just been disgraced."

Then she holds up a finger.

"Two corrections.

"**Don't give him the ring.** That ring is a demon-worker's seal on a dead heir's hand and it's the single piece of evidence that makes Emeric's chamberlain step aside. The moment it's in Crowbill's strongbox it's a *trade good*, and he will sell it to whoever pays — possibly to the Baron. Offer him first pick of the cargo. Offer him the *whole* cargo. Never the evidence."

"And the second?"

"Don't say 'once he's disgraced.' Crowbill doesn't buy futures." Her mouth quirks. "Tell him the ship is loading to sail tonight and that after tonight everything on it is out of this city for ever. He is a man who responds very well to *last chance*."

She stands, and hands you the note.

"I'll walk you. He's at the counting-house off **Gallows Reach**, and he'll have known you were coming since you left the Oyster."

---

Gallows Reach smells of tar. The counting-house has two men outside who don't look at you and a third inside who takes the axe off you without discussion and puts it somewhere you can see it, which is a courtesy.

The room is small and full of ledgers.

**Crowbill** is wiry and forgettable and would be invisible in any crowd in the world, except for a small crow inked on the back of his right hand. He's eating bread and cheese off a paper at his desk and he doesn't stop.

"The pig woman," he says. "Sit down. You've had a busy two days and I've heard four versions and none of them agree about the wolf."

He takes another bite.

"Go on, then."


===== USER [2026-09-07T01:10:46.145Z] =====
Have you, at any point in the time that Di Teufel’s dragon barge has been in town that you’ve been wondering what’s on it?  Like anything valuable worth taking?


===== ASSISTANT [2026-09-07T01:11:10.962Z] =====
Crowbill goes on chewing for a moment.

"Every day since it tied up," he says. "That's not a boast, that's my *trade*. A foreign lord brings a deep-water hull into a canal city and moors it at a private pier and lets nobody aboard — of course I've thought about what's on it. So has every fence between here and the Shoals."

He wipes his fingers on the paper.

"And here's why it's still sat there with everything on it.

"**One**: ten men in scale and one way up. **Two**: it's a *ship*, so if it goes badly they don't have to win, they just have to cast off, and then I've lost people for nothing. **Three** —" he holds up the third finger and looks at you over it "— a Baron. Not a merchant, not a guild. A man with a border tower and three hundred men and a long memory, who would spend two years and a lot of money finding out who did it, because that's what men like him are *for*."

He sits back.

"Which is three good reasons, and you didn't come here without knowing them. So you've got something that answers all three, or you wouldn't have got past my door."

His eyes are unremarkable and they haven't left your face since you sat down.

"So let's not do the part where you sell it to me. Just tell me the two things I actually need.

"**When is she sailing?**

"And **what do you want off her that isn't cargo?**"

Because a woman who wanted the cargo wouldn't be offering it to him.


===== USER [2026-09-07T01:13:52.549Z] =====
the ship is loading to sail tonight and that after tonight everything on it is out of this city for ever.  we want the knight who’s supposed to be competing in the tourney. We want him unharmed and out of the Baron’s jurisdiction.


===== ASSISTANT [2026-09-07T01:14:01.051Z] =====
**Crowbill — Insight (75).** He has been reading people across that desk for twenty years.


===== ASSISTANT [2026-09-07T01:14:25.392Z] =====
**76 against 75. He misses it by one.**

For the first time in this room, he can't tell.

---

He puts the bread down.

"Tonight." He says it to himself, not to you. Then: "And you want the *champion*."

He's quiet for a good five seconds, and you can hear a clerk's pen scratching in the next room.

"See, now, that's a strange thing to want, and I can usually tell when someone's shading me and I can't tell with you, which I don't enjoy." He taps the desk twice with one knuckle — the crow moves. "Because the cargo I understand. Cargo is cargo. But the fighting man is the one item on that ship the Baron will actually *chase*. Gold he replaces. A champion the day before the Lady's Tourney? That's him publicly beaten in front of every Guild in this city.

"So you're not asking me to rob a lord. You're asking me to *humiliate* one, and put my name on it, in exchange for goods I'd have to fence quietly for a year."

He leans back.

"Now. I've heard four versions of your two days and I'll tell you the one that's running fastest, because you'll want to know what's out there." He counts on his fingers. "Young di Teufel carved a Pearl girl and put a demon in her. Botched his run. Went in a canal and the Lady's water had him. The Pearl's closed against the whole retinue. And the Baron's entered a champion that not one soul in Purewater has been allowed to look at."

He stops.

"That last part's new. That went out this morning and it's *everywhere*, and it's the bit the Guildmasters are chewing on."

His eyes come up.

"So here's my question, and I want the true answer, because I'm not putting forty men on a pier for a story.

"**What's wrong with him?**

"Nobody hides a swordsman. You hide a thing that would *lose you everything* if it were seen. And whatever it is, it's coming into my city on my boats and I'll be the one holding it."


===== USER [2026-09-07T01:17:08.388Z] =====
It’s not a humiliation. It’s a rescue. 

The champion’s the ghost of a fallen general from a thousand years ago contained in the body of this woman’s 19 year old brother. I serve Hel and she wants the ledger set right and the ghost released. 

That clear enough of a read for you?


===== ASSISTANT [2026-09-07T01:17:34.150Z] =====
"Seventeen," Gardwen says quietly.

Crowbill looks at her, and then back at you, and doesn't say anything for a while.

Then: "A boy with a dead general in him."

"Aye."

"Being kept on a ship for it."

"Bled every morning to keep him quiet. There's a laundress on that pier who's been boiling the sheets for five days and can tell you the shape of the cut."

He stands up. He goes to the window, which looks at a wall, and stands there with his hands behind his back.

"I've a rule," he says to the wall. "I've a few. Most of them are about money and one of them isn't, and the one that isn't is why I've still got a city to work in.

"Children aren't stock. You don't sell them, you don't use them, and you don't let anyone do it on my water and call it business." He turns round. "Your Marisette knows that rule. It's why we get on."

He comes back to the desk but doesn't sit.

"So. I'd have done it for the cargo anyway. Now I'll do it properly, which is different, and here are my terms — and they're not money.

"**One.** Everything on that ship that isn't the boy is mine, and nobody counts it but me.

"**Two.** My name is nowhere. Not in the temple's version, not in your storyteller's, not in a Governor's warrant if you ever get one. Tonight was *thieves*, and this city has plenty.

"**Three** — and this is the one I care about." He puts one finger on the desk. "When it's done and the boy's out and whatever you're doing with the ghost is done, the **High Priestess of the Lake Lady** stands up and says publicly that the canal folk kept her water clean. Not me. Not names. *The canal folk.* Because I have four hundred people who get moved on and blamed and dredged out of the channel, and one sentence from that woman is worth more to them than a Baron's whole hold."

He raises an eyebrow.

"Can you get me that?"

Then, before you answer, briskly:

"And I've a practical question, because tonight is *tonight*. Ten men in scale on a deck. How do you propose we get past them — because I'll bring forty, and forty poled men are still forty men going up one ramp, and I've already told you that's how people die."


===== USER [2026-09-07T01:20:45.977Z] =====
You’re the river men, I’m just a pig farmer

I’ve seen the outside, looks perfectly scalable by the fine folk of the city. Especially if it’s parked out somewhere in the lagoon.


===== ASSISTANT [2026-09-07T01:21:07.056Z] =====
Crowbill's face does something it hasn't done yet: it becomes interested.

"Off the pier." He sits down. "Say more."

"She has to leave to sail. Once she's off that pier she's not got four men at the bollards and four at a ramp — she's just a hull in the dark with a channel round her, and the channel's yours."

"It is." He's already pulling a scrap of paper over. "And she cannot get out to sea without going through the **Mouth**, and the Mouth on the ebb is a mile of slow water with the harbour lights behind it, and I have men who have been going up the sides of anchored hulls in that stretch since they were nine years old." He's drawing. "You don't need forty. You need *twelve*, in six punts with no lights, and you take her from three sides at once while she's making way and everyone aboard is looking forward."

He's enjoying himself for the first time.

"And the best of it — a ship under way has half her people at the ropes and the rest looking where she's *going*. Nobody watches a wake."

Then he stops drawing.

"One problem, and it's yours to solve, not mine."

He taps the waterline on his own sketch.

"That hull *steams*. You've seen it. Whatever your Baron's got in her, it cooks the water where it touches, and there's a dead slick round her the whole way out. I've had a man put his hand in that water off the stern two days ago on a dare and he's still got no feeling in three fingers."

He looks up.

"My people go up the outside of hulls. They cannot climb *that* one — not at the waterline, and that's where you have to start.

"So. You've a priestess of the Lake Lady and a woman who can do things with water and something in her hands. Between them, can anybody in your party make forty feet of that hull cold enough to touch for the four minutes it takes to get twelve men over the rail?"


===== USER [2026-09-07T01:23:35.263Z] =====
Huh. Look at Gardwen. You reckon any of our mutual friends could manage that?


===== ASSISTANT [2026-09-07T01:23:57.599Z] =====
Gardwen shakes her head immediately.

"Not me. I do bark and bones and bleeding — I've nothing that touches water and nothing that touches *heat*. I couldn't cool a kettle."

Then she thinks properly.

"**Nerissa** could try. That's her channel and that hull is wounding it, and she felt it go thin from a mile off — if anyone in this city can lay a hand on that water and tell it to behave, it's her." A pause. "But she told us straight this morning: the Lady wouldn't tell her whether to hold the door or break it. She's already gone past what she's sure of once today. And she'd be doing it from a boat, in the dark, in a moving channel, against something that has been fouling her water for five days."

"Meaning?"

"Meaning she'd probably do it and it'd probably cost her more than she'd tell us."

She glances at Crowbill and back.

"And there's the other lot. The ones nobody's said out loud yet."

Crowbill, without looking up from his sketch: "The Court."

"The Mermaid's Court," Gardwen agrees. "Their chambers are *under Lost Isle*. We've been standing on the roof of them all night and the only reason nothing came up those stairs at us is that nothing chose to."

Crowbill sets his pen down.

"**Ravella**," he says. "Siren's Call. Half of one and half of us, and she brokers for them when they can be bothered to want anything. I've done business with her twice and both times I came off worse and knew it at the time."

He looks up.

"She'd be able to. Water that's been made wrong is exactly their complaint, and that hull's been bleeding into their front hall for five days."

A shrug.

"But you'd be asking the Court for a favour, mother. They don't take coin and they don't take gratitude. They take *arrangements*."


===== USER [2026-09-07T01:25:35.827Z] =====
I can do arrangements - where do I find this Ravella?


===== ASSISTANT [2026-09-07T01:26:01.329Z] =====
Crowbill folds his sketch and puts it inside his coat.

"Then we're agreed, subject to your priestess giving me my sentence. Twelve men, six punts, no lights, in the Mouth on the ebb. I'll have them ready from the eighth bell tonight and they'll wait as long as it takes — but if that hull is still cooking the water when she comes past, they don't go, and I'll not apologise for it."

"Fair."

"It is." He almost smiles. "Send word to the Reach when you've got your cold water. Or when you haven't."

---

**The Siren's Call** sits where High Isle's canals run down into the poor districts — a tall house with a water-door and a street-door, both open, which tells you what kind of place it is. Half pleasure house, half exchange. The one patch of ground in Purewater where a Guildmaster and a smuggler can sit at adjacent tables and neither has to notice.

Gondoliers waiting outside. Washerwomen coming and going through the water-door with baskets that don't have much washing in them. Everyone who touches water in this city seems to pass through here.

Crowbill's name gets you as far as a small room off the landing stage, with a table and a view straight down the canal and a jug of something cold.

**Ravella** comes in ten minutes later.

Handsome, forty-ish, unhurried. Faint scales at the hairline that could be a trick of the light. When she pours, her fingers are very slightly webbed and she does not attempt to hide it, which is itself a statement about who she thinks you are.

Her eyes catch the canal light and hold it a half-second too long.

"You're the pig woman," she says, sitting. "You've had a remarkable two days and I've heard *nine* versions."

She pushes a cup toward you.

"Crowbill sent you, which means you want something from under the water. So let's save an hour: **what do you want, and what have you got that the Court might conceivably care about?**"


===== USER [2026-09-07T01:56:30.646Z] =====
The demonologist Hanzo Di Teufel and his festering shitpile of a barge


===== ASSISTANT [2026-09-07T01:57:00.183Z] =====
Ravella's cup stops halfway to her mouth.

She sets it down without drinking.

"Say the rest."

"It steams where it sits. It's been fouling that channel for five days and the priestess of the Lake Lady says her water's gone *thin*. Tonight it sails out through the Mouth and I want it stopped, and I'm told your lot might mind about the water."

The broker's smile goes off her face entirely, and what's underneath it is much older and much less friendly.

"*Mind about it.*"

She turns her cup a quarter-turn on the table — and you notice the canal outside the window has gone glassy in a strip about four feet wide, the way it did around Gardwen in the channel.

"Let me tell you what 'thin' means from underneath, since nobody up here ever asks.

"There are people living in the deep channels of this city who were here before the causeway. Not many. They keep out of the way and they mind their own business and their whole lives are *water that behaves*. And for five days there has been a hot wound in the eastern channel that pushes ahead of the tide, and every one of them has had to move — old, young, sick — and two haven't managed it."

She says the last part very flatly.

"So yes. We mind."

Then she picks the cup up again and the broker comes back, which is somehow worse.

"But you'd have got that from a fishwife. Here's the part you'd have paid for.

"**They came down our stairs.**"

She lets that sit.

"Under Lost Isle. Four days ago, three men with a lantern, digging out a door that has been left shut and unmarked since before this city had a name. And they *took* things off it — the small confused ones that sit near the threshold and don't go through, which are ours to look after and nobody else's.

"The Court could not stop them. Won't say why and I've stopped asking." Her eyes come up. "So we have had our water burned and our threshold robbed in the same week, and we have been able to do precisely nothing about either.

"And now an old woman walks into my house smelling of Lost Isle weed with a dead captain's axe."

She leans forward slightly.

"How many of the taken have you seen?"


===== USER [2026-09-07T01:58:18.898Z] =====
Two.


===== ASSISTANT [2026-09-07T01:58:39.049Z] =====
"Two." Ravella doesn't move. "Where."

"One's dead. I put an axe through his head on Lost Isle last night and he went face-down in the drowned street and didn't float." You watch her. "The other's roped in a cellar under the Lake Lady's temple with two Swords on the door, and he talks. Boatman. Ellick Sarn."

Something passes over her face at the name and she doesn't explain it.

"Ellick," she repeats. "He poled the Forge Quarter run. He carried for us twice."

She's quiet for a moment.

"Then you already have both of them and you didn't know what you had." She sits back. "Here is the arrangement, and I'll speak for the Court because they'll agree and because there isn't time to go down and ask.

"**Give them back.**

"That's the whole price. Not the ship, not the Baron, not your boy — those are your business and the Court doesn't care about a dead general or a barony. The two you've got are *ours*, and they need to go back through that threshold and be let go properly, and until they are they're neither ours nor dead nor alive, and that is an obscenity."

She looks at you very directly.

"You should understand what you're agreeing to. The thing in Ellick Sarn came off our threshold and it goes back to it. What's left of Ellick is — " a pause, and she chooses the word carefully " — *thin*. There isn't a version of this where a boatman walks home to his supper. He said yes to a warm coat in a cold winter and he has been paying for it ever since, and the kindest end available to him is the right one.

"You'd be taking him to that stair and standing there while it's done."

She turns her cup again.

"And I understand that's your trade."

Then, briskly, the broker again:

"Do that, and I will come out to the Mouth myself tonight and put my hands on that hull and make it cold enough to climb. For as long as you need, not four minutes. And I will bring people who can be in the water beside it while it happens, which your Crowbill's boys cannot."

She holds out her webbed hand across the table.

"Two dead men, laid down properly, for one cold ship. Do we have an arrangement?"


===== USER [2026-09-07T02:01:37.952Z] =====
Don’t know where the second one is.  But sure. I’ll do what I can


===== ASSISTANT [2026-09-07T02:01:55.659Z] =====
Ravella takes your hand anyway.

Her grip is cool and slightly damp and stronger than it looks.

"You don't need to know where he is. He went into a drowned street off Lost Isle with an axe wound in his head and did not float." She lets go. "He's in our water. We'll have him on that threshold by dark and you won't have to look for him — you'll have to *stand* there, which is the part that matters."

She stands and smooths her dress.

"I'll be at the Mouth from the eighth bell with four of mine. And Magda — when you're standing over those two tonight, say it out loud. Whatever your goddess's words are. The Court will be listening from underneath and they will want to hear that somebody up here said it."

---

Out on the landing stage the day has got on toward afternoon.

**Where it stands:**

- **Crowbill** — twelve men, six punts, no lights, in the Mouth on the ebb, from the eighth bell. Wants Nerissa to publicly thank *the canal folk*. Won't go if the hull's still hot.
- **Ravella** — will cool it herself, and bring water-people into the fight. Price: two taken men laid to rest at the stair, by you.
- **Nerissa** — tracking the ship by the wound it leaves, holding Lost Isle with a dozen Swords by dark. Doesn't know yet that she's been sold a sentence.
- **Thorne** — the story is out and running. The Guildmasters are chewing on an unseen champion.
- **Marisette** — nine people in the yards, two on the water.
- **Lilura** — still in an anteroom, no warrant.

**Still missing:** Hesper, who is the only person you know who can actually lift a dead man out of a living boy. And nobody has laid eyes on Blau since dawn.

The eighth bell is about six hours off.


===== USER [2026-09-07T02:03:46.467Z] =====
Send word to Nerissa about Rvella’s request, then head over to Marisette to ask after Hesper


===== ASSISTANT [2026-09-07T02:04:19.962Z] =====
**Blau: 87 against 66 — fails again.** Two days hunting and the city won't give you up. Thorne's *"I've never seen her"* is holding, and so is everyone else's.

**Lilura: 93 against 55 — no.** She does not get past Vosk. Not today.

**The story: 35 against 70 — it runs.**

---

A gondolier off Ravella's landing takes your word to Temple Isle for a coin and the promise of another. One sentence, and the name.

By the time you're across to the Pearl there's an answer waiting, brought back by the same lad, in Nerissa's own square hand on a scrap the size of a palm:

> *Tell the crow he shall have his sentence, from the steps, at the Tourney, in front of the Governor and every Guild in the city. I would have said it years ago if anyone had thought to ask me.*
> *— V.*

---

Marisette's counting room. She's been at it since dawn and there are three people waiting outside who she is not seeing.

"Hesper's at Constantine's still. He hasn't left that room in thirty hours." She rubs her eyes. "He says the demon is 'chatty and getting bored,


===== USER [2026-09-07T02:04:19.965Z] =====
[Request interrupted by user]


===== USER [2026-09-07T02:04:57.943Z] =====
Mention the bit about thanking the canal folk too


===== ASSISTANT [2026-09-07T02:05:12.034Z] =====
Nerissa's note, in full, in her own square hand:

> *Tell the crow he shall have his sentence — from the temple steps, at the Tourney, in front of the Governor and every Guild in this city. **The canal folk kept the Lady's water clean.** Those words, that place, and I will not soften them.*
>
> *I would have said it years ago if anyone had thought to ask me. That he had to buy it is a shame on my order, not on him.*
>
> *— V.*

The gondolier takes a second coin and goes off to Gallows Reach with the answer, and you get the impression he'd have carried that one for free.

---

Marisette's counting room. She's been at it since dawn and there are three people outside she isn't seeing.

"Hesper's at Constantine's still. Hasn't left that room in thirty hours." She rubs her eyes with the heels of both hands. "His last note said the demon is chatty, bored, and 'increasingly forthcoming about its master's father,' which I'd call progress if it weren't also terrifying."

"Can I have him tonight?"

"You can *ask* him. I'll not order it — he's mine in the way a cat is mine." She's already writing. "But Magda, understand what you're asking. He's the only person in this city who can do what you need at that stair, and if he's on a punt in the Mouth at midnight he is not sitting with Emeralda, and whatever's in her has spent thirty hours learning how his mind works."

She blots it and looks up.

"And there's a thing you should hear before you go to him.

"Lilura's out. Four hours in an anteroom and then Vosk had her walked to the water-stair by two of the Governor's men, politely, with her cloak handed to her. That's not a chamberlain being obstructive. **That's a household with instructions.**"

She sets the pen down.

"Somebody has got to Emeric ahead of us. Which means the Baron knows the temple is asking questions — and has known for most of the day."


===== USER [2026-09-07T02:08:42.105Z] =====
“When the dust settles, heads will roll at court.”

Let’s go talk to Hesper


===== ASSISTANT [2026-09-07T02:09:09.074Z] =====
Marisette snorts. "They will if Nerissa says that sentence from the temple steps with the Governor sitting under her. That's the *point* of it."

---

**The Sylph's Embrace**, late afternoon.

The house is quiet in a way it wasn't two days ago. Half the girls have gone to family. Constantine has aged five years and is doing accounts he isn't reading. Ila is on the scullery step and gets up when she sees Ruhi and doesn't say anything about it.

The green room door is open now. There's a chair outside it that nobody's sitting in.

Inside, Emmeralda is at the window with the shutter open, wrapped in the green shawl with the birds on it — somebody gave in — and the long wound down her front is still there and still open and she is arranging her hair.

She sees you and lights up like a feast day.

"*Magda.* You look worse than yesterday. That's an achievement."

**Hesper** is in the corner chair with thirty hours on him and a notebook full of small handwriting. He holds up a finger, finishes a line, and then comes out into the passage with you and shuts the door.

"Before you ask — yes, I'll come. I heard about the Mouth from Marisette's boy an hour ago and I've already had a bag packed for two days." He rubs his face. "Now listen, because I've spent thirty hours buying this a syllable at a time and it changes your night.

"**You cannot simply pull a shade out and let it go.** It has to have somewhere to be, even for a moment, or it goes into the nearest living thing standing over it — which will be one of you.

"So a removal needs three parts. The door. The *thing it comes out of*. And the **anchor** — something that already holds a piece of him, that he'll consent to sit in while he's between."

He looks at you.

"The Baron carries a locket. It's the small anchor, the working one, and he's had it on his person since before they left the border. That's what keeps the daily ritual holding.

"But that's not the primary. And the thing in that room told me what is, this morning, while complaining about how much *nicer* it would be to have a proper one."

He takes a breath.

"They've got **his bones**. Thuban's. In the Baron's border tower, where they've been for a hundred years, because you cannot hold a man like that with anything less."

And you think about a quiet man who left in a boat before dawn yesterday, who Ellick said would be four hours to the border tower and back if the wind was kind — and who has been gone about thirty-six.


===== USER [2026-09-07T02:18:08.822Z] =====
Well. Laugh.

How the fuck are we going to do that?


===== ASSISTANT [2026-09-07T02:18:27.763Z] =====
Hesper doesn't laugh. He looks at you for a moment and then something happens behind his eyes.

"Wait."

He goes very still.

"Say the bit about the quiet one again. The timing."

"Gone since before dawn yesterday. Ellick reckoned four hours out to the border tower and four back with a fair wind."

"And it's been thirty-six." Hesper's hands have come up. "So he is not *at* the tower. He has been there, and he is on his way *back*, and he is late because he is carrying something heavy and he will not risk it in bad water."

Gardwen gets there half a beat before you do.

"He's bringing the bones *here*."

"He has to." Hesper is talking fast now. "They cannot do a removal without the primary anchor and the primary anchor has sat in a border tower for a century because nobody dared move it. But they've run out of boy. So for the first time in a hundred years, Thuban Eta's bones are **out of the tower and on the water**, and they are coming to Purewater, and they are going to the one place the work can be done."

He looks at you.

"Which is a stair under Lost Isle that you are already sitting on with a dozen Swords of the Lake."

---

Nobody says anything for a second.

Then Hesper adds, quietly, and it lands like a stone:

"And Magda — you were never going to be able to lay that man to rest without them. You know that. You've buried enough people."

"You don't put a man down without his bones."

"No. You don't." He almost smiles, and it's an awful smile, because he's a man who has just watched a problem turn inside out. "They have spent a hundred years keeping the one thing you need locked in a tower you could never reach.

"And tonight they are rowing it to you."


===== USER [2026-09-07T02:20:10.341Z] =====
Ok. Let’s pause there.


===== ASSISTANT [2026-09-07T02:21:56.747Z] =====
Paused and saved. Graph consistent — 36 facts, 66 knowledge edges, no problems.

## Where you stand

**Late afternoon, `d-1`.** The Tourney is tomorrow. The ship sails tonight.

**The plan for the ebb, eighth bell:**

- **Crowbill** — 12 men, 6 unlit punts, taking her in the Mouth while she's under way and everyone aboard is looking forward. Won't go if the hull's still hot.
- **Ravella** — comes herself to cool it, and brings water-folk into the fight.
- **Hesper** — packed for two days, will do the removal.
- **Nerissa** — holds Lost Isle, tracks the ship by the wound it leaves in her channel.
- **You** — stand at the stair and answer for a thousand-year-old betrayal.

**What you bought it with, and none of it was money:** the cargo, for Crowbill. Two taken men laid to rest, for the Court. The true version told once, for Thorne. And Nerissa selling a sentence she says she'd have given free — *the canal folk kept the Lady's water clean*, from the temple steps, in front of the Governor.

**The reversal:** they kept Thuban's bones a hundred years in a tower you could never have reached. Tonight they're rowing them to your stair.

**Against you:** Blau has hunted you two days and failed twice — the city keeps giving him nothing. But the Baron reached Emeric before the temple did, Lilura was walked out of the anteroom, and there will be no warrant. Whatever happens tonight happens outside the law.

**Loose:** the quiet one, thirty-six hours out and overdue. Bettan, fourteen, still at the school and still cheerful. Three of four red-haired women unnamed. And a demon in a green room on the Pearl that has spent thirty hours learning how Hesper's mind works.

Both repos committed and clean. Pick it up whenever — `get-context --compact` will put you right back at the Sylph's Embrace with Hesper's bag already packed.


===== USER [2026-09-07T05:47:02.628Z] =====
I'm going to give a technical talk about this system. Can you draft a short abstract for me? Have it cover

1. Basic nature of the system from a technical point of view
2. Short introduction to mythras and CFI as an opensource version of 1980s AD&D
3. Some technical details of the implementation and how we use ontological notebook memory to store rules, world lore, and campaign detail.


===== USER [2026-09-07T05:47:02.811Z] =====
[Request interrupted by user]


===== USER [2026-09-07T05:49:57.461Z] =====
I'm going to give a technical talk about this system. Can you draft a short abstract for me? Have it cover

1. Basic nature of the system from a technical point of view
2. Short introduction to mythras and CFI as an opensource version of 1980s AD&D
3. Some technical details of the implementation and how we use ontological notebook memory to store rules, world lore, and campaign detail.
4. The kind of game we can play on a $20 per month subscription
5. Possible applications to world modeling and digital interactive narratives but the use of game mechanics as a form of simulation 
6. Transportation, RPGs and somehow getting more from the experience than sensory-based video game versions of RPGs. This is very expressive and infinitely flexible through the use of natural language and wriging


===== ASSISTANT [2026-09-07T05:50:19.657Z] =====
Let me pull accurate numbers rather than hand-wave them.


===== ASSISTANT [2026-09-07T05:51:20.283Z] =====
Here's a draft. Numbers in it are from the running system, not estimates.

---

## Rolling Dice Against the Model: A Persistent Knowledge-Graph Substrate for LLM-Run Tabletop RPGs

**Abstract**

Large language models are excellent improvisers and unreliable bookkeepers. They drift, they flatter the narrative, and they cannot be trusted to remember who knew what. This talk describes a system that treats those weaknesses as an architecture problem: the model narrates, and *nothing else*. Every die roll, every wound, every fact and every character's knowledge of it lives in a TypeDB knowledge graph behind a 66-command CLI, and the model's only access to state is through it.

The rules layer is **Mythras Imperative** and its **Classic Fantasy Imperative** variant — an openly-licensed (ORC) d100 percentile system whose Classic Fantasy line deliberately reconstructs 1980s AD&D (classes, spell ranks, hit locations) on a modern skill-based chassis. Being open-licensed matters technically as well as legally: the rules can be *decomposed*. We slice the SRD into 101 faceted pieces across seven domains, each tagged along orthogonal dimensions (phase, action, effect, weapon, body, condition), so a live situation is composed into a facet query rather than loading rulebooks into context.

The persistence layer is an **ontological notebook memory**: 13 entity types, 21 relations and 46 attributes in a `myth-` namespace, holding three distinct strata that most systems collapse together —

- **Rules** — universal, campaign-independent, retrieved by facet.
- **World lore and living state** — locations, factions, and *agendas*: what each NPC wants, on a progress clock, producing *beats* scheduled against an ordinal world clock. `tick` advances time and stages each due beat onscreen or offscreen from recorded character presence, not authorial preference.
- **Epistemics** — situational truth as first-class `fact` nodes (independently carrying *status*: not-yet-true → established, and *truth*: true/false/partial), with `knows` edges carrying certainty, source and timestamp. A character's knowledge is a **projection** of one graph, never a copy, which makes it reconcilable by construction. A consistency checker catches the failure this replaces: character sheets asserting events that have not happened yet.

Because status and truth are independent, a *believed falsehood* is a first-class object — the rumour that sends a city hunting the wrong man is data, not improvisation.

The talk argues that **dice are the interesting part**. A roll is a state transition neither the author nor the model controls. In a recorded session, an antagonist's ritual succeeded against a Formidable grade the published adventure assumed would fail, and the campaign diverged permanently — cascading through consequence edges that thwarted three agendas and cancelled two scheduled future events automatically. This is game mechanics used as a **simulation substrate for interactive narrative**: a cheap, auditable source of genuine surprise, and a hard constraint on a model that would otherwise write the story it wants.

Finally: all of this runs a multi-hour session on a consumer LLM subscription, and produces something that sensory-realist video-game RPGs structurally cannot. Prose is infinitely flexible and costs nothing to render. Anything sayable is playable.

---

Want me to cut it to a hard 250 words for a CFP form, or publish it as a formatted page you can share with the organisers?


===== USER [2026-09-07T05:53:47.957Z] =====
Yep trim it please. Use this title: Claude Opus as a Tabletop Roleplaying GamesMaster for the Mythras Imperative Rule Set.


===== ASSISTANT [2026-09-07T05:54:06.147Z] =====
## Claude Opus as a Tabletop Roleplaying GamesMaster for the Mythras Imperative Rule Set

Large language models improvise well and keep books badly. They drift, they flatter the story, and they cannot be trusted to remember who knew what. This system treats that as an architecture problem: Claude Opus narrates, and nothing else. Every roll, wound, fact and item of character knowledge lives in a TypeDB knowledge graph behind a 66-command CLI, and the model reaches state only through it.

The rules are **Mythras Imperative** and **Classic Fantasy Imperative** — an openly-licensed (ORC) d100 system whose Classic Fantasy line reconstructs 1980s AD&D on a modern skill-based chassis. Open licensing matters technically as well as legally: the rules can be *decomposed*. We slice the SRD into 101 faceted pieces across seven domains, so a live situation is composed into a query rather than loading rulebooks into context.

Persistence is an **ontological notebook memory** — 13 entity types, 21 relations, 46 attributes — holding three strata that most systems collapse: universal rules; a living world of NPC *agendas* on progress clocks producing *beats* scheduled against a world clock; and epistemics, where situational truth is a first-class fact node with *status* and *truth* independent — so a believed falsehood is a real object — and each character's knowledge is a **projection** of one graph, never a copy.

Dice are the interesting part. A roll is a state transition neither author nor model controls. In a recorded session an antagonist's ritual succeeded where the published adventure assumed failure; the campaign diverged permanently, cascading automatically through consequence edges that killed three agendas and cancelled two scheduled events.

It runs a multi-hour session on a consumer subscription. Anything sayable is playable.

---

**~260 words.** If the CFP is strict at 250, cutting *"as well as legally"* and *"that most systems collapse"* lands it at 252 without losing anything load-bearing.


===== USER [2026-09-07T17:00:28.895Z] =====
Back to the game! 

Head out with Hesper. Spoiling for some action!


===== ASSISTANT [2026-09-07T17:01:23.872Z] =====
Dusk. Bells over the water. The Tourney bunting looks like it's been up a week.

Hesper comes out of the green room with a canvas bag, a physician's coat over something heavier, and the expression of a man who has just told a demon he'll be back shortly and been told *"of course you will, dear."*

He does not look forward to any part of tonight.

Ila brings Ruhi out to the step and hands the lead over and says "bring her back" to Gardwen, and then, after a pause, "and you," which is the most she manages.

---

**What the evening has decided while you were walking:**

**The DragonBarge is holding to the ebb.** She hasn't moved early. Marisette's watchers say she's still at the pier with steam off her waterline and men at the ropes — she'll go on the tide, as Crowbill planned for, some time after the eighth bell.

**Blau has failed to find you a third time.** Three days he's had the city's ear open and this city has told him nothing whatsoever. Thorne's *"never seen her,"* a fishmonger, forty people in a working yard, a customs man who wrote *dog* on his tally-board. Nobody has given you up.

**And the quiet one is not going to make the ebb.**

Ravella's people have the eastern approaches and there's no small boat coming in off the sea road yet. He's overdue by a day and he's carrying something he won't risk in bad water — which means the bones arrive **after** the ship sails.

Two things, two places, and not at the same time.

- **The Mouth** — Crowbill's twelve, Ravella's water-folk, a cold hull, and a boy behind a barred shutter.
- **Lost Isle** — Nerissa, a dozen Swords, a swept stair, and at some point tonight a quiet man rowing in with a century of bones and no idea who's sitting on his doorstep.

Hesper has to be at the stair for the removal. Crowbill's people need somebody they'll take orders from at the ship.

Where do you go?


===== USER [2026-09-07T17:04:42.350Z] =====
The Mouth. Definitely. Time to break some dragons.


===== ASSISTANT [2026-09-07T17:05:07.463Z] =====
Hesper takes it well. "Then I'll go to the stair. Nerissa will want telling what a removal actually needs, and somebody ought to be there when the quiet one arrives who knows what he's looking at."

He shoulders the bag.

"Magda. Get the boy off that ship *breathing*. I can work with almost anything else."

---

**The Mouth**, three hours later.

A mile of slow black water where the harbour lets out to sea, with the city's lights behind you and nothing ahead. The ebb has started — you can feel the pull of it under the punt, patient and enormous.

**Six punts, no lights.** Crowbill's twelve are exactly what he promised: canal men in dark wool, no armour worth the name, barefoot, each with a short blade and a coil of line and a grapnel wrapped in sacking so it can't ring. They talk in a low register that doesn't carry over water. None of them has asked what's on the ship.

Crowbill himself is not here. Of course he isn't.

**Ravella is.** She's in the bow of your punt in something that isn't a dress, with four of hers in the water alongside — you can't see them, but occasionally the surface does something a surface shouldn't.

**Gardwen** is amidships with her staff across her knees. **Ruhi** would not get in the boat and is somewhere on the north bank keeping pace, which nobody has been able to prevent.

You're in mail, with Vell's axe across your back and fourteen stones in the pouch.

---

Then the lights change at the pier end of the harbour, a mile back.

A lantern goes up and comes down. Another. Marisette's watchers, doing it as agreed.

**She's cast off.**

And a long time later — twenty minutes, half an hour, an age of sitting in the dark — you see her.

She comes down the channel under a scrap of canvas and the sweeps, unlit but for a single shaded lamp at the stern, and she is enormous close-to, and even at two hundred yards you can see the white where her hull meets the water and hear the *hiss* of it carrying flat across the surface.

Ravella turns round in the bow.

"When I go in, that water will kill anyone who isn't mine for about a minute while it turns." Her eyes hold the dark. "After that it's cold and it's climbable and I can hold it as long as I'm conscious."

She waits.

"So say when, and be sure. Because I only get to do this once tonight."


===== USER [2026-09-07T18:03:24.696Z] =====
Wait until the barge gets in position then give the signal. I’m probably not a very good swimmer, so I might need some help to stop myself from drowning (ha ha ha)


===== ASSISTANT [2026-09-07T18:03:49.727Z] =====
You let her come.

Two hundred yards. One-fifty. She's making maybe three knots on the ebb with the sweeps barely dipping, and the hiss gets louder, and you can smell her now — hot metal and something under it like scorched fat.

A hundred yards. The punts have drifted apart into their three groups without a word passing.

Eighty. You can see men on her deck, forward, looking where she's going.

"**Now.**"

Ravella doesn't answer. She goes over the side without a splash and the water takes her like it was expecting her.

*(And your joke lands better than you meant it — you are in a **mail hauberk** with **Swim 27**. If you go in that channel tonight you go straight to the bottom of it. Nobody is letting you swim anywhere.)*

The nearest canal man grins at you in the dark and taps the grapnel line. *You go up from the boat, mother. Feet dry.*


===== ASSISTANT [2026-09-07T18:04:16.435Z] =====
**36 against 75 — she does it.**

**22 — and somebody aboard feels it.**

---

The water goes first.

You don't see her do it. What you see is the white line along that hull *stop* — forty feet of hissing steam just ceasing, mid-length, like a candle pinched out, and the dead-water slick behind it going dark and ordinary and cold.

Six punts move at once.

Grapnels go up in sacking and land with a sound like a fist in a pillow. Canal men are on the lines before the hooks have set, going up the side of a moving ship barefoot with knives in their teeth, and it is the most casually competent thing you have ever watched anybody do.

But.

A ship that has hissed for five days and suddenly *doesn't* is a ship that has changed its noise — and there's a man aft who has lived beside that sound long enough to notice its absence.

A voice on the quarterdeck. Not a shout. A question.

Then a shout.

Then a bell starts up on that deck, hard and fast, and the answer to *how many are aboard* is about to become a practical matter.

---

Your line is set. The hull is cold and slick and there's a strake to get a boot on every three feet.

**Athletics, Hard (50 → 33)** — up forty feet of moving hull in a mail hauberk, at seventy, with an axe on your back.

*(Say the word if you'd rather spend a Luck Point before I roll — you're carrying **8**.)*


===== USER [2026-09-07T18:05:00.734Z] =====
Shoot anyone I see on deck with my sling


===== ASSISTANT [2026-09-07T18:05:11.258Z] =====
You're not going up that hull and you know it. What you *are* is a woman with a sling and a clear line at forty feet of rail with the sky behind it.

The first one leans out over the side with a knife, going for the grapnel lines — which will drop three men into cold water and the ebb.

**Sling, Hard (85 → 57)** — rocking punt, moving ship, but he's a black shape against a grey sky and the range is nothing.


===== ASSISTANT [2026-09-07T18:05:26.477Z] =====
**69 against 57 — you miss.**

The stone goes past his head close enough that he flinches back from the rail — which buys the line about three seconds and no more — and then he's out over it again with the knife.

You're already loading the next one. That's the thing about a sling: you're never really out, you're only ever between.

Down the hull to your left, the first canal man goes over the rail and vanishes.

Then the second.

Then there's a short scream from up there that isn't one of the boarders, and the knife-man forgets the grapnel line entirely and turns inboard to deal with what's just arrived on his deck.

The bell is still going.

**Second stone. Same difficulty.**


===== ASSISTANT [2026-09-07T18:05:45.042Z] =====
**A 1. Critical.**

---

He's turned inboard, half-lit by somebody's dropped lantern, side-on to you at forty feet — and the stone takes him under the raised arm where the scale gapes.

Three damage. It shouldn't be enough for anything.

But a critical ignores armour, and a stone into the armpit at that range does what a stone does: it goes *in*.

He doesn't fall over the side. He folds sideways onto the rail with his arms over it, and the knife drops past you into the water, and he stays there hanging half over the edge with his legs on the deck — which is worse for everyone aboard than if he'd gone in, because now the men behind him have to get past him and the whole rail is blocked at exactly the spot they were massing.

Two more canal men go up the line on the far side while that's happening.

---

There's proper fighting on that deck now. You can hear it and mostly not see it — a lantern going over, someone in scale hitting the boards hard, the flat wet sounds of knife work done by people who do it professionally and quietly.

And then, cutting across all of it, a voice from the quarterdeck that is not raised at all, and which every man on that ship obeys instantly:

Blau.

The bell stops. The shouting stops. It goes very quiet up there, very suddenly, which is the most frightening thing that has happened all night.

Then a single lantern shutter opens on the quarterdeck and swings out over the side, throwing a cone of light down onto the black water — and it sweeps along the hull, punt by punt.

Looking for the boats.

Looking for **you**.


===== USER [2026-09-07T18:07:49.429Z] =====
Fine. Take him with a slingshot and as soon as I can. Get up the rope and kill that motherfucker


===== ASSISTANT [2026-09-07T18:07:57.977Z] =====
The lantern makes him a target and he knows it and he does it anyway, which tells you something about him.

**Sling at the quarterdeck, Hard (57).**


===== ASSISTANT [2026-09-07T18:08:14.465Z] =====
**23 against 57 — hit. Six damage. Location 7: the abdomen.** And his sheet carries no armour — he's in cloth on a ship at night, not scale.


===== ASSISTANT [2026-09-07T18:08:28.901Z] =====
**0 of 6. Serious wound.**

---

The lantern comes round toward your punt and you put a stone through the middle of him before it gets there.

You hear it hit. Forty yards and dark and you *hear* it — the flat thud of a stone going into a body that has nothing on it but wool, because the man does not wear armour, because he has apparently never in his life expected to need it.

The lantern drops. Not thrown — *dropped*, out of a hand that stopped working, and it goes over the side and hisses out in the water and the quarterdeck goes black again.

Somewhere up there a man says something short with no breath behind it.

---

You get a hand on the line.

**Athletics, Hard (50 → 33)** — forty feet of cold wet hull, in a mail hauberk, at seventy, with Vell's axe on your back and a fight already on the deck above you.

That is a bad number and I'm telling you before I roll it. You have **8 Luck Points**, and one of them will let you re-roll it or swap the digits.

Do you want to spend one, or take it as it comes?


===== USER [2026-09-07T18:09:04.684Z] =====
Start beserking as I climb. Use the luck


===== ASSISTANT [2026-09-07T18:09:16.992Z] =====
It comes up out of you on the rope.

You've not let it since the woods, and it does not arrive like anger — it arrives like *warmth*, like getting into a hot bath, everything narrowing to the next handhold and the noise above.

**And that changes the roll.** Hauling a mailed body up forty feet of wet line hand-over-hand isn't grace, it's **Brawn** — and Berserk Rage makes Brawn one grade easier. Hard becomes Standard.

**Brawn (71)**, and a Luck Point in hand if it goes wrong.


===== ASSISTANT [2026-09-07T18:09:25.270Z] =====
**95 against 71 — failure.** Spending the Luck Point: swap the digits.

**95 becomes 59. Against 71 — you're up.**


===== ASSISTANT [2026-09-07T18:09:48.060Z] =====
You're right, and the rule is explicit on both counts:

> **Luck Points | POW 6- = 1, 7-12 = 2, 13-18 = 3, each +6 = +1**
> *"Luck Points replenish each session."*

Your POW is **14** — that's the 13–18 band. **3 Luck Points**, refreshed each session, not banked. The 8 on the sheet came in from the Roll20 Classic Fantasy import and I took it at face value.

Correcting it: 3 max, and you've just spent one on the climb.


===== ASSISTANT [2026-09-07T18:10:05.901Z] =====
**Luck: 2 of 3.** Use them carefully — that's the whole night's allowance.

---

You come over the rail into it.

**The deck.** A lantern on its side by the mainmast throwing everything sideways. Two Dragon Knights down that you can see and one canal man, face-up, not moving. The mass of it is forward where the boarders got in first — knives against scale, and the knives are winning because there are nine of them and because a man in scale on a wet deck at night is a slow, loud, obvious thing.

Aft, on the quarterdeck steps, **Blau** is on one knee with a hand pressed flat into his own middle and the other holding the rail, and he is not out of the fight — he's *directing* it, in that voice that doesn't rise, and three knights are peeling back from the bow to form on him.

Between you and him: eight feet of open deck and one man.

And **behind him**, under the quarterdeck, the barred shutter — from the inside now, a door, with a beam across it and a knight standing in front of it who has not moved from that spot since the fighting started and is not going to.

You're in the rage and it is very quiet in your head.

Vell's axe comes off your back.


===== USER [2026-09-07T18:28:43.890Z] =====
Scream with all of Hel’s fury at these violators, stealers of souls; rapists of the dead. GAAHHHHRRRR!!!!

Carve my way through to Blau


===== ASSISTANT [2026-09-07T18:29:13.655Z] =====
You go up that deck making a noise that stops the fighting at the bow for a full second.

It isn't a war cry. It's older and uglier than that — the sound you make over a byre full of dead stock in a bad winter, and there are words somewhere in the middle of it about **violators, stealers of souls, rapists of the dead**, and every canal man on that deck decides at once that whatever that is, it is on their side.

**You have initiative. 15.**

Berserk: the axe counts a size larger, **+1d2 damage**, and you take half of everything.

The man in the way has a sword and a shield and 62 in his style.


===== ASSISTANT [2026-09-07T18:29:26.027Z] =====
**81 against 85 — in, barely. His shield parry: 91 against 62 — nothing.** The special effect is yours.

**6 damage + 2 berserk = 8, into the abdomen, through 4 points of scale. Net 4.**

You take the **Bleed** effect.


===== ASSISTANT [2026-09-07T18:29:38.196Z] =====
The berserk bonus should land *before* armour, not as a separate hit — total 8, less 4 scale, **net 4**.


===== ASSISTANT [2026-09-07T18:29:54.223Z] =====
**2 of 6 in the gut, and Bleeding.**

---

He gets the shield up and it does not matter in the slightest. The axe comes over the top of it — a size larger than it has any right to be, in hands that aren't feeling the weight — and goes through the scale over his belly with a sound like someone standing on a crate.

He sits down. Not dramatically. His legs simply stop being interested, and he sits down against the mast with both hands going to his middle and blood coming through the fingers faster than a man can hold it.

He is out of this fight and he has about four minutes of being alive left unless somebody good gets to him.

Nobody good is going to get to him.

---

**Eight feet to Blau.**

He's still on one knee on the quarterdeck steps with your stone in his gut, and he has watched all of that happen, and his face has not changed.

The two knights forming on him move to put themselves between.

And he says — not loudly, because he has never once needed to be loud, and this time also because he can't:

"*That's* her. The northern woman."

A pause, and something that might be a laugh with no air behind it.

"Nobody told me she was **seventy**."

**Round 1 is done. You've spent one Action Point of three. Two left, reactions or another attack when your turn comes round again.**

Two knights between you and him. Behind them, the barred door and the man who won't leave it.


===== USER [2026-09-07T18:31:01.093Z] =====
Evade anything they send to me. Keep moving through them to get to Blau


===== ASSISTANT [2026-09-07T18:31:11.176Z] =====
Berserk cuts both ways: your **evade is one grade harder — 79 → 53**. And you take half of everything that lands.

Your proactive action is spent this round. Two AP left, and they're reactions only.


===== ASSISTANT [2026-09-07T18:31:33.697Z] =====
**Both evaded.** 12 against 53, then 49 against 53 — the second one by four.

But read the note: **evading in Mythras puts you prone.** Twice.

---

The spear comes in low and you aren't there — you go under it and inside, which at seventy involves a great deal more of the deck than you'd like.

The sword comes down where you've landed and you roll out of it, mail and all, and take the edge of a hatch coaming in the ribs doing it.

Nothing has touched you. You're also flat on a wet deck in a hauberk with two men standing over you, and **out of Action Points**.

That's what evade costs. Parry keeps your feet.

---

Blau, from the steps, still not raising his voice:

"Don't crowd her. She's on her back. **Spears.**"

And the pair of them step back a half-pace and level, which is exactly the right thing to do to a downed woman with an axe, and is going to be a problem when the round turns.

**End of Round 1.**

Round 2: everyone refreshes. Your initiative is **15** — you go first. But you're **prone**, and standing up is *Regain Footing*, which is a proactive action.

Stand and lose the attack. Or fight from the deck at a penalty.

Berserk round 2 of 14.


===== USER [2026-09-07T18:31:38.661Z] =====
Fuck it. No evade just parry and kill


===== ASSISTANT [2026-09-07T18:31:48.657Z] =====
From the deck, then. On your back with an axe, and two spearheads coming down.

**Attack from prone, Hard (85 → 57).** And every parry tonight is Hard too — berserk buys damage and pays for it in defence.


===== USER [2026-09-07T18:31:50.914Z] =====
[Request interrupted by user]


===== USER [2026-09-07T18:32:04.154Z] =====
Keep going


===== ASSISTANT [2026-09-07T18:32:22.243Z] =====
**97 against 57.** Nowhere near.

You swing up from the deck at his knee and there is no power in it from your back and no reach, and he simply steps his leg away and lets the axe go past into the boards, where it sticks for a half-second in wet oak.

That half-second is the whole problem.

---

**The guards, 14.** Two spears, one prone woman, and Blau telling them exactly what to do.

You have two Action Points and a parry at **Hard (57)**.


===== ASSISTANT [2026-09-07T18:32:43.339Z] =====
The spear gets through — but **berserk halves it**: net 4 becomes **2**. Correcting the sheet, then the second one.


===== ASSISTANT [2026-09-07T18:33:04.650Z] =====
**Right leg: 3 of 5.** The berserk is eating half of everything.

**And the second one: 95 against 62. Your parry, 11 against 57 — clean.** One special effect to you.

You take **Disarm.**

---

The first spear goes into your right thigh through the mail skirt and it should hurt and it does not, and that is the most frightening thing about being like this — you feel the *pressure* of it and nothing else, the way you'd feel a hand on your shoulder.

The second man's sword comes down and you catch it on the axe haft above your face, and you turn your wrists, and his arming sword goes end over end across the deck into the dark.

He looks at his empty hand.

You are still on your back with a spear in your leg and no Action Points left, and the round isn't over.

**Blau, 14.**

He gets off the steps. He does it slowly, with one hand still pressed into his own middle, and comes down onto the deck proper — and the two guards move aside for him without being told.

At three feet he looks down at you.

"You're the pig woman."

He draws a knife left-handed. It's a working knife, not a duelling piece.

"He was a foul little animal and he'd have been the ruin of the house inside five years." Perfectly level. "You've done the Baron a service and he will hang you for it, and I'll be there."

**Blau has 2 AP. You have none, you're prone, and there's a spear in your leg.**


===== USER [2026-09-07T18:34:19.742Z] =====
Thats OK. Try to get up.


===== ASSISTANT [2026-09-07T18:34:32.233Z] =====
You can't stand this round — Regain Footing is a proactive action and yours is long spent. But you're not out of *defences*.

**Artful Dodger.** You've spent three Action Points on an attack and two parries; the extra reaction the light load buys you is still there.

He's a wounded man with a knife and you've a war axe across your body.


===== ASSISTANT [2026-09-07T18:34:53.240Z] =====
**77 against 55 — he misses.** Your parry missed too, at 89, but it didn't need to land.

---

He's an 82 with that knife and he cannot make it work, because there is a hole in his abdomen you put there from a boat forty yards away and every time he bends at the waist something inside him refuses.

He goes down onto one knee to reach you and stops halfway with his teeth locked, and the knife comes in short and slow and wide, and he has to put his other hand on the deck to keep from going over.

Neither of you touches the other.

For a second the two of you are simply face to face on a wet deck, a foot apart, both of you bleeding, both of you seventy years apart in age and neither of you able to finish the other.

Then he says, quite quietly, with what breath he has:

"Ah."

And he looks over your shoulder, past you, at the barred door under the quarterdeck.

"*Cut the boy's throat.*"

---

**Round 2 ends.**

The knight at that door — the one who hasn't moved all fight, the one you clocked from the yards yesterday — reaches for the beam across it.

**Round 3. You go first at 15.**

You are prone. Standing costs your action. The door is fifteen feet away and there's a man at it with orders, and two guards and Blau between you.

Gardwen is somewhere at the bow. Ruhi is on the bank. Nine canal men are fighting forward and none of them know what that door is.

Berserk: round 3 of 14.


===== USER [2026-09-07T18:37:26.035Z] =====
I’m in my rage. Strategy doesn’t work here (FYI- Gardwen can heal him even if he’s badly hurt. Just so long as he’s alive).Cut Blau down from below and use a luck if needed.


===== ASSISTANT [2026-09-07T18:37:33.324Z] =====
Rage doesn't plan. It picks the nearest thing and goes.

**Attack from prone, Hard (57).** He parries at Hard too — a man cannot bend around a hole in his gut.


===== ASSISTANT [2026-09-07T18:37:47.011Z] =====
**A 6 — critical.** His parry, 72 against 55, fails. **Two special effects.**

Damage 6 into the left leg, no armour, **−1 of 5. Serious.** Plus the berserk bonus, and a critical ignores what little he has.

Two effects: **Bleed**, and **Choose Location** — you take the second one and put the follow-through where it ends him.


===== ASSISTANT [2026-09-07T18:38:03.969Z] =====
**Left leg: −3 of 5. Abdomen: 0 of 6. Two serious wounds and bleeding from both.**

---

You come up off the deck at him — not standing, *lunging*, all of it from the hips and the one good leg, with the axe going out low and flat.

It takes him across the left thigh above the knee and it does not stop where a bone should stop it.

He goes down beside you.

That's the whole of it. No cry. He's on his side on the wet boards a foot from your face with one leg not attached the way legs are attached, and his hand is still holding the knife because nobody has told the hand yet.

His eyes find you.

He tries to say something and there's no air behind any of it.

---

**And the door.**

The knight has the beam half out of its brackets. He heard the order. He is still doing it — because the man who gave it is on the deck bleeding out and that does not un-give an order.

Fifteen feet. Two guards still between. You're prone, your action is spent, and you have **two Action Points** and the Artful Dodger reaction in hand.

Then, from the bow, over the fighting:

"**MAGDA — DOWN!**"

Gardwen's voice, and she's got a clear line down the deck, and you know exactly what that means.


===== USER [2026-09-07T18:38:05.537Z] =====
Abdomen!


===== ASSISTANT [2026-09-07T18:38:26.728Z] =====
**Choose Location — you take it and drag the strike where it matters.**

The leg blow becomes a placement: the axe goes in under the ribs, into the hole your sling stone already made.


===== ASSISTANT [2026-09-07T18:38:47.333Z] =====
**−7 against 6. Major wound. He's gone.**

---

You don't take the leg. You take the *hole* — the one you put in him from a boat in the dark forty yards out, that he has been holding shut with one hand for the last five minutes because he is a man who does not believe in armour.

The axe goes in where his hand is and takes the hand with it.

He goes flat. There's a moment where he's looking at the mast, and then there isn't anybody looking at anything.

The two guards see it happen from four feet away.

That is the second thing tonight that has stopped a fight — the first was the noise you made coming over the rail. Blau was the reason those men were still standing in formation on a deck they'd already lost, and now Blau is a shape on the boards with an old woman lying next to him.

One of them steps back.

---

"**MAGDA — DOWN!**"

You're already down. You get flatter.

Whatever Gardwen has been saving comes down the length of that deck — you don't see it, you *feel* the deck go cold and wet in a rush from bow to stern — and the **Entangle** takes the whole waist of the ship: cordage, weed off the rigging, wet rope coming alive off the pins and going round ankles and wrists and throats.

It catches both guards. It catches three knights forward. It catches two canal men who will be very rude about it later.

And it catches **the knight at the door**, with the beam half out of the brackets, two feet from a boy behind it.

He goes down thrashing with rope round his knees.

**The beam is still in one bracket.**

Fifteen feet of tangled deck between you and it. Your action's spent, but the round's about to turn — and nobody standing between you is standing any more.


===== USER [2026-09-07T18:39:43.653Z] =====
Get inside and kill anyone I find in there.


===== ASSISTANT [2026-09-07T18:40:10.034Z] =====
Getting up in mail with a spear-hole in your thigh takes the whole of the next round, and nobody contests it, because nobody on that deck can currently move their legs.

The knight at the door is still thrashing in wet cordage with the beam half out of its bracket when you reach him.

He is entangled and he is helpless and you are in the rage.

You do not stop walking.

---

The beam comes out of the second bracket in your hands and the door goes inward.

**The cabin.**

Small. Low. Lamp-lit, and hot — hotter than the deck, hot the way a byre is hot, and the air in it is *wrong*: scorched hair and something sweetish, the exact smell that came out of Emmeralda's room on the Pearl.

Chalk on the deck-boards. A worked figure, a big one, and this one isn't half-scuffed. It's kept. Somebody redraws it every day.

A cot, bolted down. Bedding stripped to the canvas — because the sheets went ashore this morning in a laundress's bag.

Two men in here with him and neither of them is a soldier. One's already backing into the corner with his hands up and a bowl of something in them. The other has a razor in his hand and he is standing over the cot, and he has heard the order from the deck, and he has *not moved yet* — you have caught him at the exact moment a man decides whether he is the kind of person who does that.

And on the cot:

Seventeen. Thin the way people are thin when someone else decides what they eat. Stripped to the waist, and the whole upper left of his chest is a long-healed, re-opened, re-healed, re-opened mess — a wound that has been made and remade in the same place four hundred times.

He's awake.

He looks straight at you, and there are two people looking out of his face at once, and one of them says in a boy's voice —

"*Don't*—"

— and the other finishes it in a voice a thousand years older:

"— **she's not here for you.**"


===== USER [2026-09-07T18:41:52.848Z] =====
Still Screaming my rage. Point my axe at the man with a razor - try to pull myself out of the killing frenzy


===== ASSISTANT [2026-09-07T18:42:05.697Z] =====
Nothing in you wants to stop. That's what the rage *is* — it does not retreat and it does not spare, and the man with the razor is standing over Gardwen's brother.

**Willpower, Hard (63)** — hauling yourself out early is against its whole nature.

But there's a lever. That boy on the cot is the reason you knelt in the mud at a ford, and the oath has a number on it: **Sworn to Gardwen (by Hel) 70** — augmenting at **+14**.


===== ASSISTANT [2026-09-07T18:42:26.911Z] =====
**72 against 52. It doesn't let go of you.**

---

You point the axe at him and that is *all* you can make yourself do — and it costs you everything you have to do even that.

The rage does not want the razor. The rage wants the man holding it, and you have got both hands locked on the haft and are standing there shaking with the effort of not closing the eight feet between you, making a noise through your teeth that isn't words in any language.

The razor-man understands exactly none of it as mercy.

What he sees is a seventy-year-old woman in bloodied mail, filling a doorway, screaming, with an axe levelled at his face and a dead enforcer behind her on the deck.

He drops the razor. It hits the boards and skitters under the cot.

Then he sits straight down on the deck with his hands on his head, which is the single most sensible thing anyone has done on this ship tonight, and he starts saying "*I only do the dressings, I only do the dressings*" over and over.

The other one hasn't moved from the corner. The bowl in his hands is shaking hard enough to slop.

---

And on the cot the boy is trying to sit up and can't, and the older voice comes out of him again — steady, and very tired, and speaking to you as if across a table:

"**Woman of the death-goddess.**"

He gets an elbow under himself.

"I have been listening to you come up this ship for a quarter of an hour. I know what you are and I know who sent you, and I have been waiting for somebody to come with that particular smell on them for a *very long time*."

The boy's face contorts — a fight, right there, two people using one throat.

"— hurts, it hurts when he talks, *please* —"

"— **I know. I am sorry. It will not be much longer now.**"

Then, to you:

"Get us off this ship before the other one comes back with my bones."


===== USER [2026-09-07T18:45:33.572Z] =====
Try again to calm myself. If I can’t do it, I just grunt - “General Thuban” as an acknowledgement and go back out to kill the rest of the entangled knights on the deck.


===== ASSISTANT [2026-09-07T18:45:40.783Z] =====
Second attempt, and the reattempt rule puts it one grade harder — **Formidable (39)**. If this fails, that's it: the rage runs its course.


===== ASSISTANT [2026-09-07T18:45:59.188Z] =====
**61 against 39.** It has you until it's finished with you.

---

You get one thing out. Two words, ground through your teeth at the shape on the cot, and it is not a greeting and it is not a promise — it's the acknowledgement one soldier gives another across a yard.

"**General Thuban.**"

The old voice in the boy's throat says, with something like relief:

"*Ah. Good.*"

---

Then you turn round and go back out onto the deck, because that is where the rest of them are.

And the deck is a *slaughterhouse floor* by now — Gardwen's entangle has the whole waist of the ship in wet cordage, and there are five men in it who cannot get their legs under them, and every one of them is in scale, and every one of them belongs to the house that has kept a boy in that cabin for ten years bleeding him every morning to keep a dead man quiet.

They are helpless. You are not able to care.

Canal men get out of your way. One of them — a lad of maybe nineteen who has been in three knife fights tonight and enjoyed them — takes one look at you coming up the deck and climbs the shrouds to be somewhere else.

You do not remember most of the next minute.

---

When it lets go of you, you're on your knees by the mainmast with the axe across your thighs and no strength in either arm, and the fatigue comes down like a dropped sack.

**Berserk ends: automatic 1 Fatigue level. Fresh → Winded.**

There are nine men on that deck who are not going to get up.

Gardwen is standing about ten feet away with her staff in both hands and her mouth slightly open, and she has clearly been standing there for some time, waiting to find out whether she needed to say your name.

Behind her, at the cabin door, Hesper's dressing-man is still sitting with his hands on his head.

The ship is yours.


===== USER [2026-09-07T18:48:42.276Z] =====
I’ll take a seat. Become a crabby old lady again. 

Ooooh. Let me just sit down for a bit. Fuck me. Anyone got anything to drink?


===== ASSISTANT [2026-09-07T18:49:06.109Z] =====
**Winded. Luck 2 of 3. A spear-hole in your right thigh, 3 of 5 — and now that the rage has gone, it has opinions.**

---

You sit down on a coil of cable with your back against the mast and your legs out in front of you like a woman at the end of a market day, and you make the noise that seventy-year-old knees make when they are finally allowed to have a view.

"*Oooooh.*"

Nobody says anything for a moment.

Then one of Crowbill's men — the one who went up the shrouds to avoid you — comes down them very carefully, unhooks a stone bottle off his belt, and holds it out at arm's length like a man feeding something at a fair.

"It's not good," he says.

"Doesn't need to be."

It isn't. It's the kind of spirit they make out on the Shoals from whatever's left, and it goes down like a hot nail, and it is the finest thing you have ever tasted.

---

Around you the ship gets sorted with startling efficiency, because these people do this for a living.

**Crowbill's twelve** are already into the hold, working by lamplight, and there is a great deal of muffled swearing about how much there is. Three chests up on deck in the first minute. The long flat case takes four of them.

**Ravella** comes over the rail dripping and cold to the touch and looks at the nine on the deck and says nothing about any of it. Then she goes to the rail and speaks down at the water, and something answers.

**Gardwen** is not looking at the deck. She has gone straight past all of it to the cabin door and stopped in it, and she has not gone in, and she has been standing there for about a minute and a half.

You can see her from here. She has one hand on the frame.

Inside, the boy is trying to work out who she is, and the old voice is telling him.


===== USER [2026-09-07T18:50:53.652Z] =====
Fucking delicious. Thank you.

Go on girl. It’s him. He’s got someone with him, but he’s there.


===== ASSISTANT [2026-09-07T18:51:12.982Z] =====
She goes in.

You can't hear it from here. You can see it through the doorway, in lamplight, in pieces.

She stops two feet short of the cot, because he's a stranger — seventeen and thin and marked and not the shape of anything she's been carrying for ten years.

And he looks at her the same way, because she isn't eleven any more either.

Then the old voice says something — you see the boy's mouth move and you see her flinch at the register of it — and whatever it says, it's short, and afterwards the face on that cot changes completely.

*It steps back.* That's what it looks like from a doorway thirty feet off. Something in him steps back and gives the boy the room.

His mouth moves.

Whatever he says is one word and it isn't her name, because he was seven and there are things a seven-year-old calls a big sister that aren't a name.

Gardwen's legs go.

She catches herself on the edge of the cot and then she just puts her forehead down on his shoulder — carefully, on the right, away from the wound — and stays there, and the boy gets one arm up around her head, and neither of them makes any sound you can hear.

Ruhi comes over the rail from somewhere, soaked, and pours herself into that cabin and lies down under the cot without being asked.

---

You drink some more of the terrible spirit.

Ravella arrives beside you, dripping, and looks at the doorway, and then does you the courtesy of looking somewhere else.

"He's coming," she says quietly. "The quiet one. My people have him — small boat, out past the Mouth, coming in slow on the sea road with something heavy amidships wrapped in oiled cloth."

She crouches so it's not a public announcement.

"An hour, maybe less. He's rowing to **Lost Isle**, and he doesn't know his ship isn't behind him."

**And Hesper and Nerissa and a dozen Swords of the Lake are already sitting on that stair.**


===== USER [2026-09-07T18:54:17.969Z] =====
Well - let’s go do what we need to do. Let’s head to the lost isle

Also - it didn’t occur to me before but What do you want to do with this shitpile of a boat Ravella? Where do want it to go?


===== ASSISTANT [2026-09-07T18:54:40.937Z] =====
Ravella looks at you for a second longer than the question needs.

"Nobody's asked me that." She says it flatly, not as a complaint — as data. "Not one person in this city has ever asked what we'd like done with anything."

She stands and looks down the length of the black hull.

"Let your crow strip her. Take every last thing out of her — and *especially* whatever's in the aft hold making that smoke, because that's the part that's been burning my channel, and I'd like it in a box on dry land where I can be angry at it later.

"Then take her out. Past the Mouth, past the bar, out where the Lady's water stops running and the deep starts — and open her seams and let her go down there. Not in the harbour. Not in the roads. **Out.**"

She glances at you.

"And we'll see her down. That's ours to do. There'll be people under her the whole way and when she settles, someone will be there to say the water's clean again."

A pause.

"Tell your crow he can have a week to get the cargo off. After that we take the hull whether he's finished or not."

---

**Lost Isle**, an hour before midnight.

You come in on the south side in the temple boat with Gardwen, the boy wrapped in three cloaks and carried between two Swords, Ruhi, Ravella, and four of hers in the water alongside.

There are lights on the island now — shielded, low, disciplined. **Nerissa** has done exactly what she said: a dozen Swords of the Lake, a boat on the landing, and a cordon.

**Hesper** meets you at the waterline and takes one look at the boy and starts talking before he's finished getting out of the boat.

And at the top of the cleared stair — swept, uncovered, going down into water that does not hold the lamplight — two shapes lie side by side on the stone under a sheet.

Ellick Sarn. And the one you put an axe through, brought up out of the drowned street by people who live down there.

The Court has kept its half of the bargain before you've done anything at all.

Nerissa comes down the stone toward you.

"He's coming," she says. "We've had word twice. Small boat, one man, something heavy."

She looks at the boy on the stretcher, and then at you.

"Now. What do we do first?"


===== USER [2026-09-07T18:57:29.856Z] =====
Walk over to the two drowned men. Say a prayer to Hel.

Mother of the darkness, take these drowned back to their rest. It’s time they went home.


===== ASSISTANT [2026-09-07T18:57:42.805Z] =====
You walk over to them on a bad leg with the axe still in your hand because you've forgotten you're holding it, and you kneel down on the wet stone, which hurts, and you pull the sheet back off their faces because you have never in your life said words over a covered face.

Ellick Sarn. And the sandy one, whose name you never asked and never will.

Behind you everyone stops moving. Nerissa takes her lamp two steps back.

Under the stair the water goes very still, and it is not the wind that does it.

**Lore (Hel), Standard (52).** You are not a priest. You've just said it over a great many people in a great many byres, and you know the words because your grandmother knew them.


===== ASSISTANT [2026-09-07T18:58:03.561Z] =====
**87 against 52. It doesn't take.**

---

You say it.

*"Mother of the darkness. Take these drowned back to their rest. It's time they went home."*

And nothing happens.

The water stays still. The lamps go on burning. The two men on the stone go on being two men on the stone, and Ellick Sarn's face does not change in any way at all.

You wait. You give it a good while, because you have stood at enough gravesides to know that the words sometimes take a minute.

They don't.

Somewhere down the stair, under the black water, something is *listening* and has not been given what it needs.

---

Ravella comes and crouches on the other side of the bodies and looks at you across them, and she isn't angry, which is worse.

"It's not the words," she says quietly. "The words were right."

"Then what?"

"You said *take them*." She lays two fingers on Ellick's forehead. "You're asking her to come and fetch. She won't. She never does — that's the entire nature of your goddess, isn't it? She takes the ones nobody sings about, and she takes them *when somebody finally brings them*."

She looks up.

"Thorne told you this and you were listening to the other half of it. Nobody ever came back for Thuban. Nobody has come back for **these two** either — Ellick's wife thinks he ran off, and that one's people don't know he's dead."

She stands.

"You have to do the part that costs you. Not ask her to take them. **Give them to her.** Say whose they are and say what was done to them and say that somebody came back — and you have to mean the last one, because you're the somebody."

Nerissa, from behind you, very quietly: "That is exactly how it works, Magda. In every faith I know."

And Hesper — who has been listening while unpacking his bag, and who has gone rather pale:

"And if that's the shape of it for two drowned boatmen who died last week..."

He doesn't finish it.

He doesn't need to. You're going to have to do the same thing for a knight who has been waiting a thousand years, and you're going to have to mean *that* too.


===== USER [2026-09-07T19:04:34.411Z] =====
Mutter I’m not a fucking priest…

Then give the fucking litany- 

Oi. Listen up then. 

Brothers, workers, toilers, men.
You lived your lives as we all do
With imperfect plans 
A little hope a little selfishness
Likely with much love and sadness when you died - in this place - in the water. The water that takes all things

But then these bastards brought you back to haul and work and toil because it helped them.

So fuck em. Come with me, brothers. Rage with me at the loss and the death but go back to the dark deep sea - go to your rest. Go now, my brothers go.

Augement with my devotion to Hel


===== ASSISTANT [2026-09-07T19:04:51.971Z] =====
You mutter it at the stone — *I'm not a fucking priest* — and then you do it anyway.

**First, a correction to your own sheet.** You've had three passions on it and none of them is the one that walked you three hundred miles on eleven nights of dreams. That's an omission, not a rules call. **Devotion to Hel — 70.**

And this isn't the same attempt as before. Ravella told you the shape of it; you're not repeating a failed thing, you're doing a different one. **Lore (Hel) 52, augmented +14 = 66, Standard.**


===== ASSISTANT [2026-09-07T19:05:16.358Z] =====
**52 against 66. It takes.**

---

You don't stand up to do it. You say it kneeling on wet stone with a bad leg, in the voice you'd use across a yard.

*"Oi. Listen up then."*

And you name them as what they were — **brothers, workers, toilers, men** — and you say the true thing about a life, which is that it's made of imperfect plans and a little hope and a little selfishness and probably a great deal of love, and that they died here, in the water, the water that takes all things.

And then you say the part that costs.

*"But then these bastards brought you back. To haul, and work, and toil. Because it helped them."*

*"So fuck 'em."*

You are, at this point, shouting at a hole in the ground.

*"Come with me, brothers. Rage with me at the loss and the death — and then go back to the dark deep sea. Go to your rest. Go now, my brothers. Go."*

---

The water at the foot of the stair does not part or glow or do any of the things a story would have it do.

It goes *warm*.

That's all. You feel it come up the steps past your knees like a draught from an open door in a cold house, and every lamp on that island bends toward it at once, and Nerissa makes a small sound behind you.

And the two men on the stone let go.

There's no light. There's a *slackening* — you have seen it four hundred times in byres and beds and you would know it anywhere. Whatever was still holding the shape of Ellick Sarn's face stops holding it, and what's left is just a boatman who died, and looks it, and looks *finished*.

The warmth goes down the stair and takes something with it.

Then the water is only water.

---

Nobody says anything for a while.

Ravella has both hands flat on the stone and her head down, and she stays like that a long time. When she gets up her face is wet and it is not canal water.

"They're through," she says. "The Court has them."

She looks at you and for once there is no broker anywhere in it.

"You said whose they were. Nobody has said whose anybody was down here in four hundred years."

---

Hesper is staring at you.

"Magda," he says slowly. "That was two men who died *last week*, and it took everything you had."

Out on the black water, north-east, one of Ravella's people whistles once — low, two notes.

**A small boat. One man. Something heavy amidships.**


===== USER [2026-09-07T19:07:03.872Z] =====
Shake my head at Hesper. “Shut up old man. Give me a drink so I can get ready for the next.”


===== ASSISTANT [2026-09-07T19:07:24.696Z] =====
Hesper hands you the bottle without a word, which is the correct response, and it turns out he has better spirit than the canal men do.

"You've an hour of that in you," he says. "Perhaps two. And then you'll sleep whether anyone likes it or not."

"Then let's get on."

---

Nerissa puts the island dark in under a minute.

Every lamp shuttered. The temple boat and the punts poled round to the south side and hidden in the weed. Twelve Swords of the Lake flat behind broken walls along the north waterfront with the wet at their bellies and orders not to move for anything.

The two boatmen go under a sheet again, and four of Ravella's take them down the stair, and that's the last anyone sees of them.

The boy goes into the lee of the tower-stub with Gardwen, Ruhi, and one Sword. He can't walk far. Gardwen has not left arm's reach of him since the ship.

You're behind the low wall at the head of the cleared stair with Hesper on one side and Nerissa on the other, which is the best-defended six feet on the island and also the place the man is coming to.

---

Then you hear him.

One set of oars, unhurried, no lantern. He comes round the eastern point and along the drowned street with the confidence of someone who has done it four times before, and he lands the boat exactly where Ellick landed his, and ships the oars, and steps out into the water without a sound.

He's a long time getting the thing out of the boat. It takes him three tries and a great deal of care.

**Oiled cloth, roped, about five feet long.** He carries it up the drowned street on his shoulder with his back bent under it, and sets it down on the stone at the foot of the stair — *gently*, the way you'd set down someone sleeping — and stands there breathing.

Then he says, to nobody, in a voice that carries beautifully across still water:

"**Ellick. Get up here and help me with him.**"

Twenty feet in front of you. Alone. His hands are full and his boat is behind him and he does not know his ship is not coming.


===== USER [2026-09-07T19:08:32.592Z] =====
Let the swords deal with him. Not my problem right now


===== ASSISTANT [2026-09-07T19:08:39.459Z] =====
Nerissa doesn't even signal. She just says, quietly, "*Take him*," and the wall in front of you comes alive.

**Twelve Swords of the Lake, surprise, one exhausted man with his hands empty.**


===== ASSISTANT [2026-09-07T19:09:02.652Z] =====
**24 against 80 — clean.** And **100** on the second: he gets *nothing* off. Not a word, not a gesture.

---

Four of them come over the wall at once and two more out of the water behind him and he is face-down on the stone with a knee in his back before the echo of *Ellick* has finished coming off the far wall.

He doesn't struggle. He doesn't shout.

He turns his head sideways against the stone, and what he does is *look*. At the shuttered lamps coming open one by one. At twelve Swords of the Lake. At Nerissa. At Hesper.

And then at the oiled bundle lying on the stone eighteen inches from his face, which he set down so carefully, and which he is now not going to be allowed to touch again.

He is younger than you expected. Late thirties. Unremarkable in the way Crowbill is unremarkable, except that Crowbill chose it and this man was simply born with it. Ink on two fingers.

Nerissa stands over him.

"Where is Bettan?"

His eyes move to her. He works out who she is — the robe, or the water, or both — and something goes across his face that is almost professional appreciation.

He doesn't answer.

They rope him and sit him against the wall.

---

**And then there's the bundle.**

Hesper crouches over it and doesn't touch it either. He looks at the ropework for a long moment — the way it's tied, what it's tied with — and his mouth thins.

"That's a *reliquary* knot," he says. "That's not how you tie cargo. That's how you tie something you're afraid of."

He sits back on his heels.

"Magda. Before I open this, you need to decide something, and you need to decide it while he's alive to be asked." He nods at the roped man. "He's the only person on this island who has done this before.

"We can do it my way, which is theory and a very good library. Or we can make him tell us — and then we're doing a thousand-year-old rite by the instructions of a man who wants it to go wrong."

Behind you, at the tower-stub, the boy has started crying — the boy, not the other one — and Gardwen's voice is going low and steady and unbroken, the way you'd gentle a horse.


===== USER [2026-09-07T19:10:19.765Z] =====
“Ask that one”- point at Hester.


===== ASSISTANT [2026-09-07T19:10:38.765Z] =====
You point at the man roped against the wall.

Hesper nods once and goes to crouch in front of him, and Nerissa stands behind, and between the two of them there is a great deal of quiet authority.

He looks up at them both.

**His Willpower against everything they've got.**


===== ASSISTANT [2026-09-07T19:10:58.265Z] =====
**58 against 75 — he holds.**

He answers exactly three questions and they are all the wrong ones.

*Is that Thuban Eta in the cloth?* — "Yes."
*Will the removal work at this stair?* — "Yes."
*Will you tell us how?* — "No."

Then he settles his shoulders against the wall and stops.

Hesper tries for a long while. He's good at it — he goes at it from underneath, professional to professional, *you've done this and I haven't and I'd very much like to know how the seat is kept clean.* And you can see the man enjoying it, and enjoying not answering more.

At the end he says one thing unprompted, to Hesper, almost kindly:

"You'll open him at the wrong point and put a thousand-year-old knight into a priestess. I'd rather like to see that."

Nerissa steps back from him and looks like she wants to wash.

---

Hesper comes back to you and sits down on the stone with his bag between his knees, and rubs both hands over his face.

"Well. That's that. So it's my library, my theory, and a rite I have read about twice and never—"

He stops.

He stops mid-word, and his hands come away from his face, and he looks over your shoulder at the tower-stub where Gardwen is sitting with her arm round a seventeen-year-old boy.

"Magda," he says slowly. "We have been extraordinarily stupid."

He points.

"There is a man not thirty feet from us who has been *inside* one of these for a thousand years. Who was put in by experts and has had every day since to feel exactly how the seat is fastened.

"Why are we asking the gaoler?

"**Ask the prisoner.**"


===== USER [2026-09-07T19:11:00.068Z] =====
I have an idea. Start stripping off my armor


===== ASSISTANT [2026-09-07T19:11:16.508Z] =====
You start undoing buckles.

Nobody says anything for the first few, because everyone assumes it's the leg or the fatigue or the fact that you have been in mail since dawn.

The kettle helm goes on the stone. Then the coif, and your hair comes out flat and grey and wet.

Then you go at the hauberk, which is a two-person job at the best of times, and Nerissa — who has been watching you with a deepening frown — comes and takes the weight of it without being asked, and the two of you get it off over your head.

It goes down on the stone with the noise a hauberk makes, which is like a great deal of money being dropped.

You're in a soaked wool shirt in the cold, seventy years old, with a spear-hole in your thigh, standing on a drowned island in the dark.

Hesper has gone very quiet.

Nerissa says, "Magda."

And then, when you don't answer, she looks at the black water at the foot of the swept stair — water they put a man into, in his mail, with his hands tied — and you watch her arrive somewhere she doesn't like.

"*Magda.*"

Gardwen has stood up at the tower-stub.

**Everyone on this island is now looking at you, and not one of them knows what you're about to do.**

What's the idea?


===== USER [2026-09-07T19:13:37.191Z] =====
I’m going to fucking put the general down in the ground the only way I know how. Beserk the boy (without weapons or armor) and get the fucker to get out into his bones and through the veil. 

What does Thuban say?


===== ASSISTANT [2026-09-07T19:14:16.776Z] =====
You walk over to the tower-stub in a wet shirt with your hands empty and tell him what you mean to do.

The boy's face is wet and frightened and seventeen. Then it changes — you can watch it happen now, the way you'd watch someone step forward in a doorway — and the other one is looking out.

He takes his time. He's looking at your bare arms, and the spear-hole, and the axe you've left thirty feet away on the stone.

**Thuban Eta says:**

"No."

A pause.

"But I understand why you thought of it, and I want you to know I would have taken that offer from you gladly, if it worked."

He shifts, and the boy's ruined chest moves, and he winces on the boy's behalf.

"Understand what you are proposing. You would beat me out of a child. I do not feel your hands, woman — **he does**. You would break his ribs and I would watch, and at the end of it I would still be here, because I am not held in his body by his body." His mouth twists. "They have been cutting him open every morning for ten years to do exactly what you just described. If pain could shift me I would have been shifted four hundred times."

He lets that sit.

"Now hear the rest, because you were closer than your priest is.

"**There is a fight.** You were right about that. But it is not yours, and it is not with the boy.

"They did not fasten me in with iron. Your storyteller told you and he was correct — they fastened me in with the *night I died*. Every hour I have spent in here I have spent back on that boat with my hands tied, going over the side, looking up at Corran and Vey and the rest of them not doing anything. That is the room I have been kept in. Not this child. **That.**"

His voice — the old one — does something it hasn't done yet. It goes thin.

"And I cannot leave it, because to leave it I have to accept that it happened and that nobody came, and I have not been *able* to accept that, because it is unbearable, and I have had a thousand years of finding it unbearable.

"So." He looks at you steadily. "You do not need to fight me out. You need to **come and get me out of that water**. Say it was wrong. Say whose I am. Say somebody came.

"And you must mean it, and I will know if you don't, because I have had a very long time to learn what people mean."

Then, quieter:

"Open my bones and open your door. And then stand where they stood, and do not look away when I go under, because they did.

"That is all it ever needed. It has only ever needed one person to turn up."


===== USER [2026-09-07T19:17:58.849Z] =====
Ohhhh right. Thats right. OK.

I think I know what to do

Try to remember how we’d honor our warriors deaths in my tribe. Would we sing songs and tell tales and fight and light pyres? How would I best honor a mighty warrior - murdered by cowards - and send him rightly to Valhalla?


===== ASSISTANT [2026-09-07T19:18:14.932Z] =====
**Customs, Easy (32 → 48).** It's your own grandmother's country. You were at these before you could walk.


===== ASSISTANT [2026-09-07T19:18:39.252Z] =====
**26 against 48.** It comes back whole — not as instructions, as *smells*. Woodsmoke and wet wool and somebody's aunt weeping professionally.

---

Here is how the north does it.

**You put his weapons back in his hands.** A man goes out armed. Whatever was taken off him when he died is given back, and if you haven't got it you give him yours, and that's better anyway.

**You say the name.** Out loud, first, before anything, so everyone standing there has to hear it.

**Then you tell the tale.** Not a prayer — a *telling*. Who he was, what he did, and how he died, said in front of witnesses, in the open, at full volume. Anyone who was there speaks. Anyone who wasn't listens.

**You settle the debt.** If a man was murdered, somebody stands up and says so, and names it, and the wrong is spoken into the air where everyone can hear it. Nobody goes into the ground with an unpaid killing on him.

**Then fire.** Or water, for a drowned man. The north isn't fussy — you give him back to whatever took him, on purpose this time, with people watching.

**And you feast, and you brawl, and you get disgracefully drunk**, because a death that nobody celebrates is a death that didn't count.

---

And then you hit the thing at the bottom of it, and it stops you where you stand.

**Valhalla isn't his.**

That's for the battle-dead. For the ones who fell with a sword in the hand and the enemy in front. Thuban Eta went over a gunwale in the dark with his hands tied by his own people. He was *cheated* of the death that buys that hall, and he has been paying for their crime with his afterlife for a thousand years.

Which is exactly, precisely, why he's Hel's.

She takes the ones nobody sings about. She takes them when somebody finally brings them.

And the wound isn't the water and it isn't the rope.

**It's that in a thousand years, nobody has ever told his tale.**

Nobody said the name. Nobody said what he did or how he died or that it was wrong. There has never been a telling.

You are standing on a rock in the dark with a High Priestess, a hedge-mage, a druid, a wolf, twelve Swords of the Lake, a crime lord's boat crew somewhere off the point, a half-merfolk broker and a whole drowned Court listening from underneath.

That is the largest crowd of witnesses that has ever stood over Thuban Eta in his life or his death.


===== USER [2026-09-07T19:18:41.688Z] =====
Luck point if needed


===== ASSISTANT [2026-09-07T19:18:59.380Z] =====
Hesper cuts the reliquary knots.

He does it slowly, naming each one as it comes off, and Nerissa stands at his shoulder with her hands in the water at the stair-head, and the black water there has started to move without any wind on it.

The oiled cloth comes back.

**Bones.** Long ones, brown with age, laid the way you'd lay a man — and around the wrists, corroded almost to nothing but still there, still *on him* after a thousand years, two turns of iron wire.

They put him in the water tied and nobody ever cut it off.

Gardwen makes a sound.

Nerissa says, "*Give me the shears*," and cuts them, and drops the wire in the water, and that alone changes the temperature of the air on that stair.

---

Then Hesper looks up at you.

"The door's open. The bones are open. It's yours."

**Lore (Hel) 52, augmented by Devotion to Hel +14 = 66. Hard — a thousand years, and you're building this out of your grandmother's funerals. 44.**

Luck in hand.


===== ASSISTANT [2026-09-07T19:19:08.803Z] =====
**47 against 44. By three.**

Spending a Luck Point — swap the digits.

**47 becomes 74.** Worse.

Then take the re-roll instead.


===== ASSISTANT [2026-09-07T19:19:29.149Z] =====
**56 against 44. It fails again.**

---

You do everything right.

You say the name — *Thuban Eta* — out loud, first, so everyone on that rock has to hear it. You put Vell's axe in the bones' hands, because his own went into the water with him and yours is better anyway. You stand at the head of that stair where his company stood over him, and you say the wrong out loud: *these men murdered you, and it was cowardice, and it was never answered for.*

And you tell his tale.

You tell it in a market-day voice to twelve Swords of the Lake and a priestess and a druid and a wolf and a whole Court under the water — *he would not burn a valley, so his friends drowned him for it, and no one has said his name in a thousand years.*

It is the first telling he has ever had.

And it is **not enough.**

---

You feel it not land. It's like putting your shoulder to a door that turns out to be a wall — everything you have goes into it and the world does not move an inch.

The water at the foot of the stair stays cold. The lamps don't lean.

The boy on the stone starts to shake, and the old voice comes out of him ragged for the first time all night:

"— *I can't* — woman, I can't *reach* it, there's something across—"

Hesper is already up and moving. "The seat's still fastened. Something's still holding him and it is not the bones and it is not this stair—"

And the roped man against the wall, who has said nothing for twenty minutes, starts to **laugh**.

It's a quiet, delighted, entirely genuine laugh.

"Oh, that's *good*," he says. "That's very good. You've done all of it properly and you've done it beautifully and you have forgotten one thing.

"He isn't only held by the bones."

He tips his head back against the stone, thoroughly enjoying himself.

"**The Baron wears the rest of him around his neck.** And the Baron is at the Governor's table three miles from here, being toasted."


===== USER [2026-09-07T19:23:08.440Z] =====
Turn to walk towards the man. Pick up my axe on the way. 

Say that again. Damn you. 

Explain. It. To. Me. Slowly. And fucking clearly.

Look of death in my eyes


===== ASSISTANT [2026-09-07T19:23:21.608Z] =====
You pick the axe up off the stone on the way past without breaking stride.

You are seventy years old, in a soaked shirt, Winded, with a spear-hole in your leg, and you have already killed nine men tonight and told a dead general's tale to a hole in the ground.

He watches you come and he is *still* smiling, and then at about six feet he stops smiling.

**Opposed Willpower.** Yours is 63, augmented by the oath to +77. His is 75, and he is a man who has done this work for years and thinks it's funny.


===== ASSISTANT [2026-09-07T19:23:42.449Z] =====
**87 against 77 — you fail. He makes his at 22.**

He wins it, and he wins it comfortably.

---

He does not flinch and he does not talk.

What he does is look up at you with an axe six feet from his face and say, quite gently, like a man explaining something to a child at a funeral:

"You're not going to. If you were, you'd have done it before you asked."

And he closes his eyes and leans his head back against the stone and is simply *done* with the conversation, and there is nothing behind that face you can reach with a weapon.

---

But you got the explanation anyway — from **Hesper**, who has been thinking hard for the last thirty seconds and who does not need the prisoner's help for this part.

"He's right, and I should have seen it hours ago." He's kneeling by the bones with both hands flat on the stone. "The bones are the *primary* anchor. They're where the weight of him sits. But the **locket** is the working one — the piece they carry, the one the daily ritual runs through. It's not a spare. It's the *latch*.

"They cut a piece off him a century ago and put it in that locket, and every morning they use it to hold the seat shut. It is the thing that has been keeping him in a boy instead of in these."

He looks up.

"So the door is open. The bones are open. He is *willing* — you did that, and it worked, and I want you to hear that it worked. But there is a lock on this and it is around Hanzo di Teufel's neck.

"We cannot lay him to rest tonight while the Baron is wearing part of him."

---

Nerissa says, into the silence:

"The Tourney is at noon."

And Gardwen, from the tower-stub, with her brother shaking against her:

"Then that's where we go. Because that's where *he'll* be — in the Governor's box, in front of the whole city, wearing my brother round his neck."


===== USER [2026-09-07T19:26:39.124Z] =====
While everyone else is chatting and strategizing, keep looking at the man who’s tied up. 

Then when they’re all finished cut his head off and put it in a sack. 

Say “might come in handy” to no-one on particular


===== ASSISTANT [2026-09-07T19:27:04.740Z] =====
You don't join the strategising.

You stand at the edge of it with the axe hanging from one hand and you watch the roped man, and he knows you're watching, and after a while he opens his eyes and looks back, and the two of you hold that for a long time while the others work out how to get into a Governor's box at noon.

Nerissa says, "—then Emeric has to hear it from Sana herself, and not in an anteroom—"

And you walk over and do it.

---

It takes one.

The sound afterwards is the sound of everyone on that island stopping at once.

You find a grain sack by the stair — the Swords brought stores — and you tip out what's in it and you put the head in and you knot the top, and you say it to nobody:

"Might come in handy."

---

**Nobody says anything for about four seconds.**

Then:

**Corvin** — twenty-two, who took a rope out to Lost Isle for you last night — turns round and walks twenty feet away and is sick against a wall.

**Hesper** closes his eyes. Just for a moment. Then opens them and goes back to the bones, because he is a practical man and there is work, and you notice he does not look at you again for some time.

**Ravella** doesn't react at all. She looks at the body, and then at the water, and says quietly to one of hers, "Not that one. He doesn't go down there."

**Gardwen** looks at you for a long moment.

She doesn't say *why did you do that.* She says: "Was he still worth anything?"

And **Nerissa** —

Nerissa comes and stands in front of you. Her face is perfectly still and her voice does not rise, and every Sword on that island can hear her.

"He was bound. On my island, under my cordon, taken by my people who had orders to hold him."

She lets that sit.

"And he was the only living soul who knew where **Bettan** is. Fourteen years old. Cheerful. Cutting girls' hair at a school on the Northern Isles for people who fill them up."

Her hands are shaking slightly and she is doing nothing to hide it.

"I gave you a reason to stop, once, and you took it. So I will not pretend I did not know what you were. But you have just taken that child away from me and I do not know how to get her back."

She turns and walks away toward the boats.

Twelve Swords of the Lake watch her go, and then look at you, and none of them says anything at all.


===== USER [2026-09-07T19:29:08.987Z] =====
Gardwen. You know how to find people, right? Like if they’re lost in the woods


===== ASSISTANT [2026-09-07T19:29:28.413Z] =====
Gardwen doesn't answer straight away. She's still looking at the sack.

Then she puts it aside, because there's a job.

"In woods, yes. Broken ground, bent grass, where a body's lain — I could find a child in the Ash Vale in a night." She shakes her head. "Not here. There's no *ground*. It's all stone and water and forty thousand people walking over each other."

Then she stops.

"But I don't need to track her."

She looks up.

"Magda — I found those two on Lost Isle from four hundred yards across open water, and I never saw them. I felt what was *in* them. Wrong the way milk's wrong. And I found Sana in the same casting because she wasn't."

She's on her feet now.

"Bettan's been filled. Sana told us — the quiet week, the cheerfulness, the not feeling the cold. If she's carrying one of those things then she doesn't read like a girl any more, and I don't have to find *her*. I have to stand somewhere near that school and ask what's wrong in it."

A pause.

"It cost me a magic point and nearly all of my legs, and I couldn't reach across the channel until the priestess put her hand in the water with me. So I'd need to be *at* Corbie's. And I'd need Nerissa."

She meets your eye and doesn't soften it.

"Who has just walked off to the boats and will not want to look at you."

Then, more quietly:

"Go and tell her anyway. Not sorry — she'd smell that. Tell her you've got a way to find the girl, and let her decide what she does with you afterwards."


===== USER [2026-09-07T19:32:55.504Z] =====
Oi. Priestess!

Walk over

Don’t look for the girl. Look for the demon.
Gardwen can do it for you if you put her in the right place. Your magic would probably do it too, right. 

Spare me your delicacies and so called purities. The rots in your city and it’s not going to leave because you ask it nicely. 

Walk back


===== ASSISTANT [2026-09-07T19:33:17.280Z] =====
She's at the boats with her back to you and she turns round when you shout.

You say it. All of it. And you don't apologise, because you aren't, and she'd know.

She listens to the whole thing without interrupting.

Then:

"You've mistaken me."

Very level.

"I did not object because it was *unclean*. I have buried men off the tide-flats with their throats opened by people I then had to bless at Solstice. I'm sixty-one and I run a temple in a port." She takes a step closer. "I objected because you cut up the only map to a fourteen-year-old girl and then said *might come in handy*.

"That isn't purity, Magda. That's **arithmetic**."

She holds your eye until she's sure it's landed, and only then does the rest of her arrive — because she's already thinking about the thing you actually came to say.

"—and yes. Yes, that would work.

"I can put my hands in the water at Corbie's and hold the channel for her the way I did last night, and if that child has something in her then it will show like a lamp through a shutter." Her jaw tightens. "It's better than anything I had, which was *ask the school again and hope*."

She looks past you at Gardwen.

"We go at first light. Not before — the girls will be at breakfast and I want them in one room and counted while it's done."

Then, as you turn to walk away:

"Magda."

Not raised.

"I will work with you until this is finished, and I will do it wholeheartedly, and I will not pretend at you afterwards. When the boy is out and the Baron is down, you and I are done, and you will not be welcome on Temple Isle."

A beat.

"Sword-Captain Vell's axe stays with you. She'd have wanted that and I'm not petty."

She gets in the boat.

---

**Dawn is maybe two hours off. The Tourney is at noon.**

Behind you on the stone: an open reliquary, a boy who can't walk, a bundle of bones with a thousand-year-old knight in the process of failing to leave them, and a sack.


===== USER [2026-09-07T19:39:10.159Z] =====
Shrug. No. I killed him because he deserved it. Fucker wasn’t going to tell you anything anyway. I don’t even know what arithmetic is.

So let’s go find the girl and then get this bloody Baron. 

I’ve always been curious how these tourneys work.


===== ASSISTANT [2026-09-07T19:39:40.054Z] =====
Nerissa takes *I don't even know what arithmetic is* without any expression whatsoever, and pushes the boat off.

"No," she agrees. "You don't."

---

**Hesper** explains the Tourney on the way back, because he's the one who's been to them.

"It's not a fair. It's a **sacred** event — older than the Governor's office, older than the current arrangement of who rules what. It's the Lady's, and Nerissa opens it, and the whole city stops. Which is exactly why what the Baron's doing is not politics. It's **desecration**, and if you can get anyone to see it as that, it changes what people are allowed to do about it."

Three events:

**Archery** — the main event, and the prestigious one. Targets on the field, then moving targets on boats between the islands, then the long cross-channel shots. The prizes are court access and titles. *Temerach Nebulo has entered it.*

**Single Combat** — one-on-one, knockout matches, prizes of guild contracts and apprenticeships. **This is where Cailan was going to be fielded.** A champion nobody has seen, in front of every Guild in Purewater.

**The Harbor Run** — a scramble through the canals and over the rooftops. Swimming, climbing, boat-hopping. Cash and local glory, and everybody's recruiters watching.

"And the Baron will be in the Governor's box for all of it," Hesper says. "Beside Emeric. With the whole city watching him be a guest of honour."

He glances at the sack in your hand, and away again.

"Wearing your general round his neck."

---

**First light: Corbie's, and Bettan.**

**Noon: the Tourney, a locket, and a Baron who no longer has a champion to field — and does not yet know it.**


===== USER [2026-09-07T19:48:11.196Z] =====
Huh. Let’s just get the girl and worry about the Baron when the time comes


===== ASSISTANT [2026-09-07T19:48:36.262Z] =====
**45 against 103. Comfortably.**

---

Grey light on the Northern Isles. Mistress Corliss has forty girls in the refectory being counted, which they are treating as an outrage.

Nerissa goes into the channel to her knees at the water-stair. Gardwen takes her hand and puts the other flat on the wall of the school itself.

It takes about four seconds.

"There," she says.

Then, immediately: "*No.* Wait—"

And her grip tightens on Nerissa's hand hard enough to make the priestess wince.

"There's **three**."

---

Three.

Bettan, fourteen, cheerful, in the refectory with the others — a wrongness sitting in her like a lamp behind a shutter.

And two more in that room.

Girls who went quiet for a week sometime in the last month, and came back lovely, and started asking everyone about their families.

Nobody noticed. Why would they? A homesick child getting happier is the thing you *want* to see.

---

Gardwen opens her eyes and she's grey.

"Magda — Santo had five twists of hair. He'd used one. Four left, and Sana's was one of them." She's already doing the sum out loud and hating it. "They weren't collecting *vessels*. They've been **filling** them. Here. For a month. In a school full of forty girls, four hundred yards from that stair."

Nerissa comes up out of the water very slowly.

"The four twists were the ones they hadn't done yet," she says.

She looks at the lit windows of the refectory, where forty girls are being counted and complaining about it.

"Then how many *have* they done?"


===== USER [2026-09-07T19:54:42.865Z] =====
Yawn. He’ll, I’m tired.

Erm. That’s a matter for the watch. Wouldn’t you say? Arrest the Dragonknights as quietly as possible and ask them. Then we go take the Baron - 

Hmmm… Temerach Nebulo’s a sword of the lake, isn’t she? Pretty good shot too… 

Could she help?


===== ASSISTANT [2026-09-07T19:55:16.688Z] =====
Nerissa takes the school off your hands without argument — it's hers, the girls are hers, and she is very glad to have something she can do properly.

"Corliss keeps them in the refectory. Nobody leaves the island. I'll have the three sat separately and I'll send for Hesper the moment he's done with the bones." Her mouth is thin. "And the Watch will take the di Teufel household on High Isle *quietly*, at breakfast, because at breakfast on Tourney day there'll be four men in that house and forty at the field. That I can arrange without a warrant — the Harbor Masters owe me and the household aren't nobles, they're servants."

Then you say the name, and she goes still.

"**Temerach Nebulo.**"

---

"She's ours," Nerissa says slowly. "Sworn to the Order. The *Lakelady's Javelin* — that's not a nickname the temple hands out twice a century."

She looks at you.

"And she is **entered in the Archery.** Which means she is already inside the ground, with a bow, with a competitor's badge, with court access as a prize she's expected to win — and she is the one person in Purewater who can stand within thirty yards of the Governor's box at noon holding a weapon and have nobody think anything of it at all."

Hesper, quietly: "Her combat style is **one hundred and twenty-one**."

"Yes."

"I've never seen a number like that on a person."

"No," Nerissa agrees. "You haven't."

---

And Gardwen says, from where she's sitting with her back against the school wall:

"She's been hunting Hanzo di Teufel for years. That's the whole reason she came to this city."

A pause.

"She's also the one who's been keeping Conall's parentage from him since he was a boy. So she'll help — but she'll want to do it *her* way, and lawfully, and in front of witnesses, because she's spent her whole career trying to bring that man down the proper way and she is not going to enjoy being handed a sack with a head in it."

---

Grey light. Gulls starting. You have been awake for something like twenty-six hours and you are Winded and there is a hole in your leg.

**The Tourney opens at noon.**


===== USER [2026-09-07T19:57:44.283Z] =====
Make a note - don’t have characters talk about skill numbers in gameplay. Find another way to express it.


===== ASSISTANT [2026-09-07T19:58:09.053Z] =====
Noted and saved — numbers stay in the roll line, never in anyone's mouth.

Replaying that beat properly:

---

"She's ours," Nerissa says slowly. "Sworn to the Order. The *Lakelady's Javelin* — that's not a name the temple gives out twice in a century."

She looks at you.

"And she's entered in the **Archery**. Which means she is already inside that ground with a bow in her hand and a competitor's badge on her chest, and she is the one person in Purewater who can stand thirty yards from the Governor's box at noon holding a weapon and have nobody think anything of it whatsoever."

Hesper says quietly: "I saw her shoot at the Anminster meet, eleven years ago. Moving targets, boat to boat, cross-channel."

"And?"

"She put every arrow inside a handspan and then apologised to the judges for the last one, because it was *high*." He shakes his head slowly. "I have never in my life seen anyone do anything that well. I'm not sure I've seen anyone do *anything* that well."

"No," Nerissa agrees. "You haven't."

---

And Gardwen, from where she's sitting with her back against the school wall:

"She's been hunting Hanzo di Teufel for years — that's the whole reason she's in this city. So she'll help.

"But she's spent her whole career trying to bring that man down the *lawful* way, in front of witnesses, with everything in order." She glances at the sack by your foot. "And she is not going to enjoy what's in that bag."

---

Grey light. Gulls starting up. You've been awake something like twenty-six hours, you're Winded, and there's a hole in your leg.

**The Tourney opens at noon.**


===== USER [2026-09-07T20:01:14.559Z] =====
I’ll sleep till it’s time. Give back the axe and the mail. Get my staff back. That shit was fucking HEAVY. Chuckle.

Fucker didn’t think I was going to it either.


===== ASSISTANT [2026-09-07T20:01:55.094Z] =====
You hand it all back on the temple steps: hauberk, coif, kettle helm, and Vell's axe laid across the mail like a man laid out.

Nerissa looks at it and then at you.

"I said keep it."

"Aye. And it's about four stone and I'm seventy." You get your staff back off the Sword who's been holding it, and the weight of it in your hands is the first thing that's felt right in a day. "That's a young woman's kit. She'd want it on somebody who can carry it up a rope without spending a favour to do it."

You chuckle, and it turns into something rougher.

"Besides. Fucker on that ship didn't think I was going to make it up either."

Nerissa does not smile.

But she picks the axe up herself, and carries it in personally, which is not something a High Priestess does for a piece of armoury.

---

You sleep four hours in a cell under the temple on a cot that is objectively worse than the deck of the DragonBarge, and you sleep like the dead.

**Fatigue: Fresh.** The leg is still a hole and will be for a week — 3 of 5, and it lets you know about it on stairs.

**Luck: 1 of 3.** That's what's left of the night.

Back in your own ringmail, quarterstaff, staff sling, fourteen stones. Twelve ENC. Artful Dodger holds.

And a knotted sack that nobody has asked you to put down.

---

**Noon. The Lake Lady's Tourney.**

The field is on **Temple Isle** — the long ground on the north side, with the water on three sides of it and the temple colonnade at the head, and it is *full*. Every Guild. Every house on the Pearl. Bunting, food stalls, a great deal of bad wine, and about six thousand people.

The **Governor's box** sits under the colonnade: raised, canopied, twenty seats.

**Prince Emeric** is in it, twenty-four and being talked at by three older men.

And two seats along, in dragon-green with a cup in his hand, being toasted by a Guildmaster —

**Baron Hanzo di Teufel.**

Who has not been told that his ship is at the bottom of the Mouth, that his enforcer is dead, that his household was arrested at breakfast, or that his champion is in a cell under the temple you are standing in.

He is waiting for the Single Combat to be called.

Around his neck, on a chain, under the green: something small.


===== USER [2026-09-07T20:03:53.715Z] =====
Gardwen could heal my leg.


===== ASSISTANT [2026-09-07T20:04:00.697Z] =====
She's been offering since the ship and you've been waving her off.

**Cure Minor Wounds — Piety 87.**


===== ASSISTANT [2026-09-07T20:04:15.940Z] =====
Her roll **failed** at 90 against 87 — and I healed you anyway in the same breath. Undoing that.


===== ASSISTANT [2026-09-07T20:04:25.354Z] =====
**53 against 58 — she gets it on the second attempt.**


===== ASSISTANT [2026-09-07T20:04:48.040Z] =====
She takes two goes at it — the first one slides off, and she swears in a way that startles a passing Sword — and then she gets both hands round your thigh and leans on it the way she described at the ford. *Find the shape it's supposed to be and lean until it remembers.*

The spear-hole closes from the inside out. It itches unbearably for about four seconds and then it's a pink pucker and an old woman's ordinary aches.

"Don't," she says, before you can say anything. "You've been walking on that since the ship and I've been asking since the ship."

---

**Magda: whole. Fresh. Luck 1 of 3.** Ringmail, quarterstaff, staff sling, fourteen stones, and a sack.

---

**Noon, and the horns go.**

Six thousand people on the north ground of Temple Isle. The water on three sides. Bunting. Bad wine. A smell of fried fish that is, frankly, doing a lot to improve your mood.

**Nerissa** opens it from the temple steps — and you notice she does not say the sentence she owes Crowbill. Not yet. She's keeping it for when it'll cost someone something.

In the **Governor's box**: Emeric, twenty-four, flanked and managed. Three council men. Two Guildmasters. And Baron Hanzo di Teufel, being toasted, with something small on a chain under the green.

Out on the field, competitors are forming up for the **Archery** — and among them, in Swords of the Lake blue-green with a competitor's badge and a bow taller than she is, is a slight elven woman who has not looked at the Governor's box once, which is itself remarkable, because everyone else has.

**Temerach Nebulo** does not know that any of last night happened.

She also has not been told that Conall's brother-by-blood put a stone through Blau's gut, or that a boy is in a cell under the temple, or that her Order's High Priestess has spent the night on a drowned island.

The Single Combat is called for the second hour after noon.

That's roughly two hours to get a locket off a man's neck in front of six thousand witnesses.


===== USER [2026-09-07T20:06:15.278Z] =====
You’re confused: 

She also has not been told that Conall’s brother-by-blood put a stone through Blau’s gut, or that a boy is in a cell under the temple, or that her Order’s High Priestess has spent the night on a drowned island.

Magda isn’t Conall’s brother (that’s Randall). I’m playing Magda


===== ASSISTANT [2026-09-07T20:06:24.807Z] =====
You're right — that was garbled. Randall is Conall's twin; you're Magda, no relation to either. Corrected:

**Temerach Nebulo does not know that any of last night happened.**

Not that a ship went down in the Mouth. Not that Blau is dead. Not that a seventeen-year-old boy is in a cell under the temple she can see from where she's standing. Not that her Order's High Priestess spent the night on a drowned island cutting thousand-year-old wire off a dead knight's wrists.

She is standing on a competition field with a bow, waiting for the Archery to be called, hunting Hanzo di Teufel the lawful way — the way she has been hunting him for years.

And she has not looked at the Governor's box once, which is remarkable, because everybody else has.

---

The Single Combat is called for the second hour after noon.

Two hours to get a locket off a man's neck in front of six thousand witnesses.


===== USER [2026-09-07T20:08:05.570Z] =====
While I was sleeping why the fuck didn’t anyone tell her?


===== ASSISTANT [2026-09-07T20:08:27.021Z] =====
You ask Nerissa, and she doesn't get defensive about it, which is one of the better things about her.

"I sent Corvin at first light. He's been at the competitors' rope for four hours."

She points, and he's there — the young Sword who was sick against a wall on Lost Isle, standing at the cordon with a folded note in his hand and a face like a man failing.

"The enclosure is **sealed** from the first horn. No messages in, no messages out, nobody in or out but judges and the Lady's own. It's not a Governor's rule I can lean on, it's a *temple* rule, and it's four hundred years old, and it exists precisely so nobody can nobble a competitor with news from outside." Her jaw tightens. "I wrote it. Or my predecessors did. I *enforce* it."

"You're the High Priestess."

"I am. And if I break the seal on the sacred enclosure at the Lady's own Tourney, in front of six thousand people and every Guild in this city, then this afternoon stops being about a Baron and starts being about me." She looks at you levelly. "Which is exactly what the men sitting next to Emeric would like."

She lets that sit.

"There is one exception and it is not much of one. **The Lady's own** may pass — that's clergy, in vestment, on temple business. Lilura could walk through that rope right now and nobody would blink."

A pause.

"But Lilura has never met Temerach Nebulo, doesn't know the half of it, and cannot be trusted to say the right four things to an elf who will start asking questions."

She looks at you. Then at Gardwen. Then, for a moment, at the sack.

"You, on the other hand, are not clergy, are not in vestment, are not subtle, and are extremely memorable."


===== USER [2026-09-07T20:09:28.371Z] =====
Chuckle. 

What do you want me to do?


===== ASSISTANT [2026-09-07T20:09:42.205Z] =====
Nerissa is quiet for a moment, and you can see her hating it.

"I want to make you a **novice of the Order of the Lake Lady**," she says. "For about an hour. Vestment, sash, and Lilura walking you in as her attendant, which is a thing a novice does and which nobody looks at twice."

She holds up a hand before you can say anything.

"I am aware. Yes. I told you last night you'd not be welcome on Temple Isle again and I meant it and I will still mean it at sunset." Her mouth is very thin. "But right now the only thing standing between six thousand people and a demonologist in the Governor's box is whether one archer gets told four sentences in the next hour, and I have a rule I will not break and a robe I *can* hand you.

"So I am going to put the Lady's cloth on a woman who beheaded a bound prisoner on my island eight hours ago, and I am going to do it with my own hands, and I would very much like you to appreciate what that costs me."

She's already unpinning her own sash.

"Four sentences. Not five. She is the finest archer in the realm and she is about to shoot in front of the whole city, and if you fill her head with the wrong thing at the wrong moment you will cost her the only lawful route she has ever had at that man."

She holds the sash out.

"So. What are you going to tell Temerach Nebulo?"


===== USER [2026-09-07T20:15:28.453Z] =====
Try very hard not to laugh. Look serious. Nod seriously. My eyes are just twinkling though.

“Nebulo probably knows about me already though…” 

I will walk up to her and say: “We’ve rescued Thuban and the boy. Di Teufel was were possessing people with demons all over the place. I just need the Barons’ locket to complete the rite and lay the haunt to rest.”


===== ASSISTANT [2026-09-07T20:15:50.725Z] =====
You keep your face absolutely straight. It costs you something.

The vestment is blue-green and about a foot too long and smells of cedar. Nerissa does the sash herself, at the throat, with her mouth in a line, and she does not meet your eye once while she's doing it — and when she's done she steps back and looks at you in it for a second and says, flatly:

"Don't."

"Wasn't going to say a word."

"You were *radiating*."

---

Lilura walks you through the rope with the incurious confidence of a woman doing her job. A judge glances at the sash and looks away. You are the least remarkable thing on that field, which is a first.

The competitors' enclosure is quiet in the way a place is quiet when everyone in it is concentrating. Twenty-odd archers. Strung bows. Somebody's coach murmuring numbers.

**Temerach Nebulo** is sitting on an upturned crate with her bow across her knees, doing nothing at all — which, you realise after a moment, is the whole of her preparation. She is entirely still and she is not thinking about anything.

She looks up as you stop in front of her.

You say your four sentences.

---

She does not react the way people react.

There is no start, no *what*, no hand to the mouth. She takes it in and you can see her *filing* it, and then she asks two questions in a flat clear voice, and they are exactly the right two.

"Is Conall alive?"

"Aye. Not been near any of it."

A small nod. Something goes out of her shoulders that had clearly been there for days.

"Is the boy in the temple *now*?"

"Cell under the colonnade. Priestess has him."

She stands up.

She's not tall. It doesn't matter.

"Then the locket." She looks past you, across the ground, at the canopied box under the temple steps, and the man in dragon-green with a cup in his hand — and it is the first time all day she has looked at him, and her face does not change at all.

"I have been trying to put that man in front of a magistrate for four years," she says. "I have letters, and witnesses who recant, and two dead informants.

"Tell me what you need off him, and whether it needs him alive."


===== USER [2026-09-07T20:18:17.577Z] =====
Just the locket. I have no problem with you killing him, but other people might.


===== USER [2026-09-07T20:18:30.319Z] =====
[Request interrupted by user]


===== USER [2026-09-07T20:19:14.735Z] =====
Interesting- remember Magda doesn’t know Conall. First test of the epistemology mechanisms in the game and it fails.


===== ASSISTANT [2026-09-07T20:19:47.746Z] =====
**Zero.** The graph is unambiguous: Magda has never heard the name Conall. Every fact about him is known by Temerach alone.

So the mechanism didn't fail — **I did.** `CLAUDE.md` says *"`character-view --id <pc>` before speaking for anyone,"* and I wrote Magda's dialogue without querying it. The graph had the right answer sitting there and I didn't look. That's the exact failure mode the whole layer exists to catch, and it only catches it if I consult it.

Replaying the beat with what she actually knows:

---

She looks up as you stop in front of her.

You say your four sentences.

She does not react the way people react. No start, no *what*. She takes it in and files it, and then asks:

"Is Conall alive?"

"Who?"

It stops her. Properly stops her — the first thing all day that has.

"Conall Bjornlasch." She's watching your face now and getting nothing, because there's nothing there to get. "Dark. Twenty-two. Rides with me. He's been in this city three days."

"Never heard the name in my life, lass."

And something happens behind that flat elven composure that you can't read at all.

"...Then you don't know," she says slowly. "None of you know. You've spent three days pulling this apart and nobody has mentioned him once."

She stands up. She's not tall. It doesn't matter.

"That is either very good news or the worst news I've had this week, and I don't yet know which."

Then she puts it aside — visibly, the way she does everything — and looks past you across the ground at the canopied box and the man in dragon-green, and it is the first time all day she has looked at him.

"Later. The locket first."

"Just the locket. I've no problem with you killing him. Other people might."

"Mm." Not agreement. Filing. "I have spent four years trying to put that man in front of a magistrate. Letters, witnesses who recant, two dead informants."

She picks up her bow.

"Tell me what it looks like, and how close you need to be."


===== USER [2026-09-07T20:23:12.470Z] =====
I guess it all depends on where his agents are and who they are. Oh, he’s likely magician (shudder) he’s been talking to the dead and shit.

What do you think we should do?


===== ASSISTANT [2026-09-07T20:23:39.079Z] =====
Temerach thinks about it for perhaps four seconds, which for her is a long deliberation.

"Not in the box."

She says it as settled fact.

"Six thousand people are watching that canopy. If he dies in it, or is *taken* in it, then by tonight the story is that the temple and the Governor murdered a foreign lord at the Lady's own Tourney, and the three men sitting beside Emeric will make sure it's the only story. I have watched that happen to better cases than this one."

She's stringing the bow while she talks. She doesn't look at what her hands are doing.

"So we don't go to him. **We make him leave.**"

She nods at the field.

"The Single Combat is called at the second hour. His champion is in a cell under that temple. He does not know it yet. So at the second hour a herald calls for the di Teufel man, and calls again, and *nobody comes* — in front of every Guild in this city.

"He will have about a minute to decide whether he is a man whose champion is late or a man who has been robbed. And he is not stupid. He'll know."

She sets the string.

"And then he leaves that box. He has to. He'll go for his boat, and the only water-stair from the Governor's enclosure is the one behind the colonnade, which is twelve feet wide with a wall on one side."

She looks up.

"That's where he can be taken, and it is out of sight of the ground, and everything that happens there happens in front of temple witnesses instead of the whole city."

Then, on the other thing:

"A magician. Yes. I'd assumed." Not a flicker. "Which is why he does not get a minute of warning and does not get his hands free. I can put a shaft through a wrist at a hundred paces on a still day and this is a still day."

Finally she looks at you properly, and there's something almost like humour in it.

"And you're the part I can't do.

"He will leave when the herald calls. Or he will leave *sooner*, and on our timing instead of his, if somebody he does not know walks up to that box and shows him something that tells him it has all already gone wrong."

A pause.

"You've been carrying that sack since you got here."


===== USER [2026-09-07T20:28:35.235Z] =====
It’s the quiet one’s head. He was pissing me off. I was told you wouldn’t OK with that but it’d definitely get the good Baron’s attention.

You’re busy here, so you can’t help

This Conall kid of yours. Is he any good with a bow?


===== ASSISTANT [2026-09-07T20:28:58.333Z] =====
Temerach's face does not change at the word *head*.

"I am not going to pretend that pleases me." Flat. "But I have seen what that man's people do to fourteen-year-olds and I am not going to stand on a field and lecture you about a demonologist's neck. Use it if it works."

Then the other question, and she answers it too fast.

"No."

You wait.

"He's — " She's stringing something that's already strung. "He has a soldier's training, all weapons. He's competent. He's not an archer."

"That's not what I asked, lass. I asked if he was any good."

"He's *competent*."

---

Here is a thing about Temerach Nebulo: she is one of the most dangerous people in this realm and she is an **appalling** liar. She has no facility for it whatsoever. She has just told you two things she didn't mean to — that Conall is better than competent, and that she would rather chew her own hand off than have him within a mile of that box.

She hears herself do it, too. You watch her hear it.

"He is my responsibility," she says, more carefully. "He is twenty-two, he came to this city because I brought him, and there is a reason I have kept him away from the di Teufels that I am not going to discuss on a competition field with a woman I met four minutes ago."

She picks up her quiver.

"Ask me again tonight and I may tell you. Ask me now and I'll say no and mean it."

Then, briskly, closing it:

"The Archery is called in a quarter of an hour. I will be on that line for the better part of an hour and I cannot leave it without forfeiting — and I want to win it, because the prize is court access and that is *four years* of my work.

"So you have an hour where I am the most visible person in Purewater and can do nothing at all.

"Use it. Get me one thing: **whether he still has the locket on him.** If he's left it on a ship or in a strongbox we are all wasting the afternoon."


===== USER [2026-09-07T20:35:14.489Z] =====
Aww. You’re adorable. 

Alright then lass. I’ll get this all squared away and then we’ll take the Baron down. 

Go back, get the head put in a pretty looking box with a note signed ‘the pig woman’ and try to figure out how to get eyes on the Baron’s jewelry.

Maybe go and talk to the servants with Nerissa and get them to help.


===== ASSISTANT [2026-09-07T20:35:33.163Z] =====
Nerissa listens to the whole plan and then says, "I will get you the servants. I will not get you the box."

She gets you the servants.

**Marisette** does, really — three of her girls have worked Tourney service for years, and one of them, Corliss's youngest, is pouring in the Governor's enclosure this afternoon because she always does. Ravella adds a gondolier who ferries the Guild party and a woman who's been carrying ice up from the Shoals since dawn.

Nobody has to be told a story. Marisette says *look at what's round the Baron's neck and tell me* and they say *right you are*.

**And the box** you sort out yourself, from a chandler off the ground, for more than it's worth: a fitted wooden case with a sliding lid, the sort a merchant sends samples in. The note takes a while because you write like a woman who learned late.

> ***YOUR SHIP IS ON THE BOTTOM. YOUR MAN IS DEAD.
> I HAVE YOUR CHAMPION AND HIS BONES.
> — THE PIG WOMAN***

Gardwen reads it over your shoulder and says nothing for a while, and then: "You've spelled *champion* wrong."

"He'll get the sense of it."

**Eyes on the locket — Corliss's girl, pouring at four feet, over the better part of an hour.**


===== ASSISTANT [2026-09-07T20:36:00.282Z] =====
**9 against 70 — she does it beautifully. 21 on the other roll — and it is seen.**

---

Corliss's youngest is eighteen, has poured at four Tourneys, and is very good at being furniture. She goes in with the wine four times over the hour and comes out with this:

**It's on him.** Gold, a flattened oval about the size of a thumbnail, on a fine chain — worn *under* the shirt, but the chain shows at the collar and the shape of it shows through the green when he leans forward.

**And he touches it.** Not fidgeting. Every so often his hand goes flat to his chest over it, briefly, the way a man checks a purse — and once, when a Guildmaster leaned in to toast him, he moved his shoulder to put it further away.

"He does it about every quarter hour," she says. "And after he does it, he looks round."

---

Then she tells you the rest, and her hands are not steady.

"He caught me."

Fourth pour. She was closer than she needed to be and she looked a half-second too long, and when she came back up he was already looking at her.

And he *smiled*. And said — pleasantly, in front of two Guildmasters and the Prince — "*You've very good hands, girl. Who do you serve?*"

She said the Guild steward's name, because it's true.

He said: "*Of course.*" And went back to his cup.

"He wasn't angry," she says. "That's what's wrong with it. He was **pleased**."

---

Marisette has already got her off the island and onto a boat, which she did before telling you.

**One hour gone. The Archery is running — Temerach is on the line and cannot leave it. The Single Combat is called in an hour.**

And in the Governor's box, a man who has spent five days being toasted has just been reminded that people are looking at his throat.


===== USER [2026-09-07T20:37:22.692Z] =====
OK. Relax. Watch the tournament. How does our girl do?


===== ASSISTANT [2026-09-07T20:37:32.043Z] =====
You buy fried fish and find a place on the rail and, for about an hour, you are just an old woman at a fair.

It is *excellent*.

**The Archery** runs in three passes. Twenty-two starters. By the third pass there are four.


===== ASSISTANT [2026-09-07T20:37:58.086Z] =====
**First pass — fixed targets at eighty paces.** 92 against 121. She hits everything and the crowd doesn't notice her, because everyone hits at eighty paces.

**Second pass — moving targets, boats poled across the gap between the islands.** A 3.

**Critical.**

---

That's when six thousand people find out who she is.

The boats go across left to right at a walking pace with the targets standing on them, and the field is allowed six shafts. The Guild man ahead of her puts four in and the crowd is very pleased with four.

Temerach shoots six.

She does not track. That's the thing you notice from the rail — everyone else swings the bow with the boat, and she doesn't. She puts the bow where the boat is *going to be*, and waits, and looses, and the target arrives at the arrow.

Six shafts. Six hits. The last two go into the same target inside a handspan while the boat is at its furthest and fastest.

The noise the ground makes is not applause. It's the noise people make when they've been shown something.

Somebody near you says "*that's the Javelin, that's her, that's the Lakelady's Javelin*" and it goes down the rail like a wave.

**Third pass — cross-channel, two hundred and fifty paces over open water with the wind off the Mouth.** 34 against 61 in a Formidable grade.

She and the Guild archer both come through it. He's genuinely good — 39, 11 and 38 against a solid 78, and on any other day in any other year he wins this and dines out on it for a decade.

Today he is standing next to somebody who put two arrows in the same moving target at range and then apologised to the judges for the grouping.

---

They call it for **Temerach Nebulo**, Knight of the Swords of the Lake.

Prize: a purse, a silver bracer, and **access to the Governor's court**.

She goes up to the box to receive it.

Which means that in about ninety seconds, Temerach Nebulo will be standing inside the canopy, within arm's reach of Baron Hanzo di Teufel, in front of six thousand witnesses, entirely lawfully.

And the Single Combat is called in twenty minutes.


===== USER [2026-09-07T20:41:10.790Z] =====
Let’s get the box sent up there a little after when the Lakelady’s javelin arrives. Any chance to inform her or are we just going to have to wing it?


===== ASSISTANT [2026-09-07T20:41:23.472Z] =====
There's one window and it's a good one.

**Nerissa presents the prize.** It's her Tourney, they're her Order's colours, and the High Priestess of the Lake Lady handing a Sword of the Lake her bracer in front of the city is the most ordinary thing that will happen all afternoon.

She can say four words while she does it and nobody on that ground will think anything of it at all.

"Give me something short," she says, already moving. "I'll not risk more."

**"Box coming. He has it."**


===== ASSISTANT [2026-09-07T20:41:50.056Z] =====
**94 against 80 — the word does not get through.**

Nerissa is three steps from the dais with the bracer in her hands when a man in Governor's livery comes down the steps and takes it out of them.

**Vosk.** The chamberlain who kept Lilura in an anteroom for four hours.

He does it beautifully. A small bow, a murmured word about the Prince wishing to honour the champion of the Archery *personally*, and it is protocol, and it is correct, and there is not one thing the High Priestess of the Lake Lady can do about it in front of six thousand people without making a scene that the three men beside Emeric would enjoy enormously.

She stands there with empty hands.

Emeric — who is twenty-four and does not understand what has just been done with him — presents the bracer to Temerach himself, delightedly, and says something complimentary about the second pass.

Temerach receives it, bows, and is invited to stay in the canopy.

**She has no idea what's coming.**

---

**57 against 75 — and the box arrives exactly on time.**

A boy in chandler's apron comes up the enclosure steps with a fitted wooden case, hands it to a steward, says *for the Baron di Teufel, paid delivery*, and is gone before anybody thinks to ask anything.

The steward carries it in.

You watch it cross the canopy from a hundred and forty feet away on the public rail, in a novice's vestment, eating fried fish, with Gardwen's hand closed hard around your forearm.

The Baron takes it on his knee. He's still talking to a Guildmaster. He's amused — a gift, at a Tourney, from a well-wisher.

He slides the lid.

Temerach Nebulo is standing four feet to his left, holding a silver bracer, entirely unwarned.


===== USER [2026-09-07T20:43:45.677Z] =====
Go down to the gantry as soon as he starts to move.


===== ASSISTANT [2026-09-07T20:44:17.548Z] =====
**58 against 94. He holds it.**

---

From a hundred and forty feet you see almost nothing, and that's the point.

He slides the lid. He looks down into the box for about two seconds. He slides the lid back.

He says something to the Guildmaster beside him and the Guildmaster laughs.

Then he sets the case down beside his chair, stands, and makes a small apologetic gesture to Prince Emeric — *forgive me, a moment* — and Emeric waves him away good-naturedly, and he steps out of the back of the canopy with his cup still in his hand.

He does not hurry. He does not look round the ground once.

He is very, very good.

Gardwen: "Did he—"

"He read it. He's going for his boat."

---

You're moving before she's finished.

Down the public rail, through the fried-fish crowd, past the ale trestles, round the back of the colonnade where the ground gives way to worked stone and the noise drops off like a door closing.

**The water-stair behind the Governor's enclosure.** Twelve feet wide. A wall on the left, the channel on the right, thirty-odd steps down to a landing where three boats are tied and two bored oarsmen are playing dice.

Out of sight of six thousand people.

You get there first — you were closer, and he was being unhurried and correct.

Gardwen comes down behind you and puts herself flat against the wall inside the arch. Ruhi is somewhere above on the colonnade roof, which you have decided not to think about.

Above and behind, in the canopy, **Temerach** has seen him go. You can't see her from here.

Footsteps in the passage. Unhurried. One set.

Then a second set, quicker, catching up — and a voice you don't know saying "*My lord — my lord, the herald's calling the Single Combat—*"

And Hanzo di Teufel says, perfectly pleasantly, from about fifteen feet the other side of the arch:

"Yes. Tell them my champion withdraws. Injury in training."

A pause.

"And find out who delivered that box."


===== USER [2026-09-07T20:44:42.681Z] =====
Get a slingshot ready as I go.


===== ASSISTANT [2026-09-07T20:45:13.936Z] =====
**Arcane Casting 88. Seventeen magic points. No armour.** *Lightning Bolt. Wall of Fire. Hold Person. Sleep. Charm Being. Fly.*

He is a nobleman with a sword he barely knows how to use and enough fire to end a street.

---

The stone in the pouch, the cord round your knuckles, the staff cocked back along your forearm. You do it flat against the wall inside the arch with the vestment sleeve pushed up out of the way.

Twelve feet of open stair and then the landing. Gardwen opposite, other side of the arch, staff low.

The servant's footsteps go away up the passage.

His don't.

---

He comes through the arch.

Close to, Baron Hanzo di Teufel is a well-made man of about fifty in dragon-green with grey at the temples and very good boots, and the cup is still in his left hand, and he has not spilled a drop of it.

He is looking at the boats.

He gets three steps down the stair before he registers that there is an old woman in a Lake Lady novice's vestment standing against the wall with a loaded staff sling.

He stops.

He looks at you for a moment — at the vestment, at the sling, at your face — and you watch him do arithmetic much faster than the serving girl did.

"Ah," he says.

And then, with what sounds like genuine warmth:

"**The pig woman.**"

He hasn't put the cup down.

"You've cost me a great deal in three days and I would very much like to know how you did the ship. I'll pay for that answer, and I pay well." He tilts his head slightly. "Or we can do the other thing, and you should know before you choose that you are standing on wet stone at the bottom of a walled passage, which is a *dreadful* place to fight a man like me."

Behind him, in the arch, unhurried, blocking it:

**Temerach Nebulo**, with an arrow already on the string.


===== USER [2026-09-07T20:47:43.002Z] =====
Spit on the ground to add to the moisture.

Hel’s waiting for you Baron. Time you went down. Loose a slingshot.


===== ASSISTANT [2026-09-07T20:47:53.538Z] =====
You spit on the step between you.

*"Hel's waiting for you, Baron. Time you went down."*

**Staff sling, Standard (85).** He's twelve feet away, stationary, and wearing court silk.


===== ASSISTANT [2026-09-07T20:48:13.272Z] =====
**43 against 85 — a hit. His evade: 15 against 36 — he makes it too.** Both succeed, so it goes to the higher roll, and that's yours by a distance.

He gets out of the way of most of it and not enough of it.

**Five damage, chest, no armour.**


===== ASSISTANT [2026-09-07T20:48:31.209Z] =====
**3 of 8. Minor — and he's on the steps.**

---

He throws himself sideways and he is quick for fifty, and the stone still finds him.

It takes him high in the chest and turns him completely round, and the cup goes out of his hand and shatters on the step, and he lands badly on wet stone and comes up on one elbow with his court silk torn open and a spreading bruise the shape of a fist coming up underneath it.

And now he is not warm and he is not amused.

He gets a hand up — palm out, fingers spread, and you have seen exactly this once before, at a ford, when a druid asked a favour of the water — and the air in that passage goes *dry*.

**"MAGDA—"** Gardwen, from the other side of the arch.

And behind him, from the top of the stair, absolutely calm:

**"My lord Baron. Put the hand down."**

Temerach has not moved from the arch. The bow is drawn — properly drawn, to the ear, held — and at that range with that draw the arrow will go through him and into the wall.

"You are under arrest by warrant of the Order of the Lake Lady for the profanation of the Tourney and the sacred channel," she says. "There are two Guildmasters and a Prince forty feet above us. I have been trying to say those words to you for four years.

"**Put the hand down.**"

He is on the steps between the pair of you: an old woman with a loaded sling and the finest archer in the realm.

His hand does not go down.


===== USER [2026-09-07T20:49:59.365Z] =====
Close fast and break his wrist with my staff


===== ASSISTANT [2026-09-07T20:50:11.334Z] =====
He's prone, unarmoured, and he has chosen to finish the spell rather than defend himself, because he is a man who has never once been hit by anything.

**Quarterstaff, Standard (85), no defence** — and undefended means the differential hands you a special effect, which goes straight into **Choose Location**.


===== ASSISTANT [2026-09-07T20:50:21.186Z] =====
**63 against 85 — in. Four damage. Choose Location: the right arm.**


===== ASSISTANT [2026-09-07T20:50:37.452Z] =====
**1 of 5. Not broken — but everything in it that was about to work, stops working.**

---

You don't throw the staff. You go down the three steps with it held short in both hands like a woman going at a rat in a grain store, and you bring the end of it down on the wrist.

There's a crack that is mostly the staff and partly not.

The hand shuts.

And whatever was gathering in that passage — the dry, tight, wrong feeling of air being *asked* for something — comes apart all at once with a sound like a held breath being let go, and the temperature comes back, and somewhere above you a gull starts complaining again.

Hanzo di Teufel makes a noise through his teeth. It is the first entirely honest sound he has made in three days.

He cradles the arm against his chest and looks up at you from the wet stone with his hair come loose and his silk torn and a stone-bruise spreading under it.

Fifty years of never once being touched, undone on a service stair by an old woman with a stick.

"You *hag*—"

---

Temerach comes down four steps with the bow still drawn.

"On your face. Hands behind."

He doesn't move.

And you can see him working — the eyes going, fast, the way they went when the box opened. Counting what's left. One dead heir, one dead enforcer, a ship on the bottom, a household in the Watch's hands, a champion gone, a broken wrist, an arrow at ten feet.

And one thing still round his neck that nobody has mentioned yet.

His left hand — the good one — moves very slightly toward his own collar.


===== USER [2026-09-07T20:51:33.874Z] =====
Slap his hand away. Grab the amulet and rip it off his throat - eye to eye all the way.


===== ASSISTANT [2026-09-07T20:51:42.615Z] =====
He's prone, one-handed, and there's an arrow on him at ten feet.

**Unarmed, Easy (85 → 128).**


===== ASSISTANT [2026-09-07T20:52:02.384Z] =====
**12 against 128. Critical.**

---

His good hand comes up and you slap it down out of the air like a woman swatting a wasp off a pie.

Then you take a fistful of green silk and collar and *chain*, all together, and you put your face about four inches from his.

And you don't rip it. Not straight away.

You hold him there, eye to eye, on the wet stone, and you let him get a proper look at what has been coming up this stair for him — which is not a knight and not a priestess and not a magistrate. It's an old woman who keeps pigs, sent by a goddess he has never once thought about, wearing a novice's vestment she has no right to, with fried fish on her breath.

He stares back and he is, for the first time, entirely out of arithmetic.

*Then* you pull.

The chain doesn't break at the clasp. It breaks across the back of his neck, and it takes skin, and he cries out.

And it comes away in your fist: gold, a flattened oval about the size of a thumbnail, warm — *properly* warm, the warmth of something that has been alive against a chest for a hundred years — and heavier than a thing that size has any right to be.

Inside it, something moves.

Not rattles. *Moves.*

---

Hanzo di Teufel goes very still underneath you.

And then, in a voice that has lost every bit of its charm:

"You have no idea what you are holding. You cannot *open* that, you stupid woman, if you open that here he will go into the nearest—"

**"I know."**

That's Hesper. Standing in the arch at the top of the stair with his bag, entirely out of breath, having run the length of the colonnade.

"She's not going to open it here."

---

Temerach steps down and puts a boot between the Baron's shoulders and gets his good arm behind him, and it is over, and it took about ninety seconds.

The locket is in your fist.

Above you, six thousand people are being told that the di Teufel champion withdraws through injury, and there is a certain amount of booing.


===== USER [2026-09-07T20:54:55.687Z] =====
Hand it to Hesper. Look at Temerach. 

“That shot was one of the most beautiful things I’ve seen from in my life and I’m a lot older than I look. Anything else you need?”


===== ASSISTANT [2026-09-07T20:55:16.568Z] =====
Hesper takes the locket in a folded cloth and does not touch it with his skin, and puts it in a box within a box, and his hands are not quite steady.

"Bones, door, and the latch," he says. "That's all three. For the first time in a hundred years, all three are in one place."

---

Temerach has the Baron's good arm behind him and a knee on him and is not even slightly out of breath.

You tell her about the second pass. Six shafts, six hits, two in the same target at the furthest and fastest, and the apology to the judges.

*One of the most beautiful things I've seen in my life. And I'm a lot older than I look.*

She looks up at you.

And the finest archer in the realm, who has just arrested the man she has hunted for four years, goes **completely to pieces** for about a second and a half — she gets pink to the ears, and looks at the step, and says:

"The sixth was high."

"It was in the target."

"It was *high*." Firmly. Then, quieter, and clearly having to make herself do it: "...Thank you. That's a kind thing to say and I never know what to do with them."

She hauls the Baron up onto his knees.

---

Then, on the other question, she doesn't hesitate.

"Yes. There is something I need, and it is the thing I said I'd tell you tonight, and it has just become urgent because that man is going to be questioned and he is going to talk about his family."

She looks at you steadily.

"**Conall Bjornlasch is his son.** Bastard-born, of an elven mage he ruined, twenty-two years ago. I have known since before I took the boy in. He does not know.

"And he has a twin brother somewhere in this city that neither of them knows about either."

She tightens the cord on the Baron's wrists.

"So what I need is for that boy to hear it from me, today, in a room of my choosing — before he hears it shouted across a courtroom by *him*."


===== USER [2026-09-07T20:56:55.592Z] =====
Alright. What do you need from me?


===== ASSISTANT [2026-09-07T20:57:28.302Z] =====
"Two things, and neither of them is fighting."

She gets the Baron up and hands him off to two Swords who have come down the stair behind Hesper, and watches them take him up, and only then does she turn round properly.

"**First — keep him off me for an hour.** Nerissa will want him questioned immediately and she'll be right to, and the moment that starts he begins buying himself time by throwing his own blood on the table. I need one hour with Conall before that room opens." She looks at you levelly. "You have some influence with the priestess. I have none. I've never been able to talk to people."

"And the second?"

"**Be there when I tell him.**"

That one takes you by surprise.

"I have known this boy since he was nineteen and I have lied to him every day of it, for what I thought were good reasons, and in about an hour he is going to find out that the man being led up those steps in irons is his father." Her jaw sets. "He will look at me and he will understand that I knew, and I will deserve every bit of what comes next.

"And there needs to be somebody in that room who has nothing to do with any of it. Somebody he has never met, who has no stake, who will simply say the true thing plainly when it's needed."

A pause.

"You're extremely good at that. It's a rarer skill than shooting."

---

Above you the ground has gone loud again — the Single Combat has been called and the first pair are on the sand, and six thousand people who have no idea what just happened forty feet away are enjoying themselves enormously.

Hesper is halfway up the stair with a box within a box.

**And there's a boy in a cell under that temple with a thousand-year-old knight inside him, waiting.**


===== USER [2026-09-07T20:59:40.203Z] =====
I have my own goddess to tend to. Once that’s done, I’ll happily stand with you for this boy. 

Then go with Hesper to try again for the rite


===== ASSISTANT [2026-09-07T21:00:02.273Z] =====
The tide is right. That's the thing nobody has to say out loud — Nerissa looks at the channel as they come down the temple stair and says "*it's thin*," in the voice of a woman reporting a fact she wishes she couldn't feel.

It takes forty minutes to get everything to Lost Isle.

The **boy**, carried, awake, and very frightened. **Gardwen** beside him the whole way with her hand in his. **Ruhi** in the bottom of the boat. **Hesper**, with a box within a box. **Nerissa**, who has left her own Tourney running behind her without a backward glance. Twelve Swords. **Ravella**, and four of hers in the water alongside the whole way, which no boatman in this city has ever had happen to them.

The drowned street. The swept stair. The bones laid out on the stone with the wire cut off the wrists and a borrowed axe across them.

Hesper sets the locket down at the head of the bones and opens the outer box and then, with a great deal of care, the inner one.

The thing inside it moves.

---

They put the boy down on the stone at the top of the stair, and Gardwen holds him, and Thuban Eta comes up into his face for what everyone there understands is the last time.

He looks at the bones. Then at the locket. Then at you.

"You came back," he says.

"Aye."

"Then I am ready, and I have been ready for a thousand years, and I would like you to be quick — because he is very tired and I have taken enough of his life."

---

Everything is here. Bones, door, and latch. Six thousand people are cheering at a tournament three miles away and not one of them knows.

**Lore (Hel) 52, augmented by Devotion to Hel +14 = 66. Standard.**

You did it right the first time. The only thing that beat you is lying open on the stone.


===== ASSISTANT [2026-09-07T21:00:23.979Z] =====
**28 against 66. It takes.**

---

You do it exactly as you did it before, because it was right before.

You say the name. **Thuban Eta.** Out loud, first, so everyone on that rock has to hear it.

You tell the tale — the valley he wouldn't burn, the argument he won in front of men who killed him for it, the boat in the dark, the wire on the wrists, the water. You tell it in a market-day voice to a priestess and a mage and a druid and a wolf and twelve Swords and a Court listening from underneath.

You name the wrong, out loud, so it's in the air where it can be heard: *this was murder, and it was cowardice, and no one ever answered for it.*

And then the part that costs.

You go down two steps into the black water in a novice's vestment you have no right to, up to your knees, and you stand exactly where nine men stood over a bound knight a thousand years ago and did nothing — and you do not look away.

*"You went in here and nobody came. I came. You're not theirs and you're not his and you were never Valhalla's, because they cheated you of the death that buys it.*

*"You're hers. You've always been hers. And she takes the ones nobody sings about — but only when somebody finally brings them.*

***"Mother of the darkness. This is Thuban Eta and I have brought him. He's yours. Take him home."***

---

**The locket opens on the stone by itself.**

Not dramatically. It simply comes apart, the way a shell does when whatever was holding it shut has stopped bothering.

And the water goes *warm*.

It comes up past your knees like a draught from an open door in a cold house, and every lamp on that island bends toward it at once, and under the surface something enormous and patient turns over and pays attention.

On the stone, the boy arches once against Gardwen's arms and makes a sound that is two voices and then one voice and then no voice at all.

And something goes down that stair.

You don't see it. You *feel* it go past you in the water — unhurried, the way a big fish goes past your legs in a river — and there is a moment, exactly one, where you have the absolutely unmistakable sense of being **looked at** by something that is grateful and is not going to say so, because it's a soldier.

Then it's gone.

The bones on the stone settle very slightly, the way bones do.

And the water is just water.

---

**Silence.**

Gardwen's brother is limp in her arms with his eyes open. Breathing.

Then he says, in a boy's voice with nobody behind it:

"...it's quiet."


===== USER [2026-09-07T21:02:40.518Z] =====
I reckon I just lose it and go to Gardwen and weep and hold them both close.


===== ASSISTANT [2026-09-07T21:02:59.128Z] =====
You come up out of the water and your legs don't work properly and you don't much care.

You get to them on your knees on the wet stone and you put your arms round both of them at once — the girl who has been carrying ten years of a dead brother, and the boy who has just had a thousand-year-old man taken out of him — and you hold on.

And then, after seventy years of not doing this in front of anybody, you come apart completely.

It's not graceful. It's the ugly kind, from the chest, the kind that hurts your throat — a great old woman in a stolen vestment howling on a rock in a drowned street, with her face in a druid's hair and one hand knotted in a boy's shirt.

Gardwen has got hold of your arm with her free hand and is not letting go of it.

The boy doesn't understand who you are at all. He puts his head against you anyway, because you're warm and because there's nothing left in him to do anything else with.

Ruhi shoves her whole head under your elbow and stays there.

---

Nobody on that island says a word.

**Nerissa** turns her back — not away from you; she turns and faces the others and makes them stop looking, which is the single kindest thing she does all week.

**Hesper** sits down heavily on the step with the empty locket in his hands and stares at nothing.

**Ravella** goes to the edge of the stair, and crouches, and says something down into the water that isn't in any language you know — and something answers, and this time everybody hears it.

**Corvin** — twenty-two, who was sick against a wall for you — is crying openly and doesn't bother to hide it.

---

It takes a while.

When you finally get your breath the light has moved on the water, and the boy is asleep against Gardwen with his mouth open, and Gardwen has not moved a muscle in case it wakes him.

She looks at you over the top of his head.

Her face is absolutely wrecked and about ten years younger.

"Magda," she says. "I don't know his name."

A pause.

"He was seven. We called him Bird. I don't know what his *name* is."


===== USER [2026-09-07T21:07:32.502Z] =====
Call him Bird then. It’d be a lot better than anything those bastards called him.

Go back to Marissette’s let her know what happened. Nerissa still has to proclaim the Baron’s downfall and the canal folk’s help and I have to help the javelin with something


===== ASSISTANT [2026-09-07T21:07:54.364Z] =====
"Call him Bird, then."

Gardwen looks down at him.

"It'd be a lot better than anything those bastards called him," you say. "And he'll pick his own when he's ready. That's how it works — you get given one, and then one day you take one. Nobody's given him anything since he was seven."

She nods, and doesn't trust herself to say anything, and puts her cheek back down on the top of his head.

---

**Marisette** takes it standing up, in her counting room, with her hands flat on the desk.

You tell her all of it — the Mouth, the ship, Blau, the stair, the three girls at Corbie's, the box, the water-stair, the locket, and the thing that went down past your legs.

At the end she sits down slowly and says, "*Three* of them. At the school."

"Aye."

"And you got the girls back?"

"Priestess has them. Hesper's working on it. He says two of them are — " you try to remember the word he used " — *shallow*. Recent. He thinks they'll come out."

"And the third?"

"He didn't say."

She's quiet for a moment. Then she pours two glasses of something that costs more than your farm and pushes one across, and does not make a speech about it.

"Ann Yannick keeps her work and gets a pension out of me whether she wants one or not," she says. "Corliss's girl gets whatever she asks for and I'll be telling her that myself. And Ila—"

She stops.

"Ila is going to want to see that boy."

---

**Nerissa proclaims it from the temple steps at the close of the Tourney**, in front of the Governor, every Guild in Purewater, and six thousand people who came for the Single Combat and got something considerably better.

She names the desecration. She names the arrest, by warrant, of Baron Hanzo di Teufel. She names the fouling of the sacred channel and the fact that she rang the alarm and was told to stop — and she looks directly at Prince Emeric's chamberlain when she says that part, and Vosk goes the colour of paper.

And then she says the sentence she owes.

***"The canal folk kept the Lady's water clean."***

She says it slowly. She lets it sit. And when the ground doesn't quite know what to do with it, she says it again, louder, and adds: *"Say it back to me,"* — and six thousand people do.

Somewhere on the water, a very forgettable man with a crow on his hand hears the whole city say it.

---

**And then there's the Javelin, and a room, and a boy called Conall who doesn't know.**

Temerach is waiting for you at the door.


===== USER [2026-09-07T21:09:46.578Z] =====
Saunter in. Stiffly.


===== ASSISTANT [2026-09-07T21:10:00.292Z] =====
You saunter in stiffly, which at your age is the only kind available, and it takes about four seconds and you're aware of every one of them.

---

It's a small room off the temple's south cloister. A table, three chairs, a jug nobody has touched.

**Conall Bjornlasch** is twenty-two, dark, and has been in this room for an hour being told nothing, and he is not pleased about it.

He is also — and you notice it immediately because you have spent three days looking for it in other faces — *sharp*. His eyes do the whole of you in one pass: the vestment you have no right to, the canal on the hem, the staff, the fact that you're moving like someone who fought yesterday and slept badly.

"You're not clergy," he says.

"No."

"Temerach, what is this."

**Temerach — Influence 22.**


===== ASSISTANT [2026-09-07T21:10:22.516Z] =====
**14 against 22.** She makes it — barely, and only because she stops trying to be gentle.

---

She doesn't sit down. She stands with her hands at her sides like a woman giving a report to a superior officer, which is the only register she has, and it turns out to be exactly the right one.

"Conall. I am going to tell you four things and then you may do whatever you like to me.

"**One.** Baron Hanzo di Teufel is your father. You were born of an elven mage he seduced and ruined, twenty-two years ago, and she fled to this city and died here.

"**Two.** You have a brother. A twin. He is somewhere in Purewater and he does not know about you either.

"**Three.** I have known both of those since before I took you in at nineteen. Every day since, I have chosen not to tell you.

"**Four.** He was arrested this afternoon, by me, on the water-stair, and he will be questioned tonight — and he will say all of this out loud in front of a magistrate to buy himself an hour. So you were going to hear it today whatever I did. I wanted it to be from me. That is not the same as it being *right*."

Then she stops. Completely. No softening, no *I'm sorry*, nothing.

---

Conall doesn't move for a long moment.

You watch a very quick mind go through it — and because he's quick, he doesn't get to have the easy reaction. He goes straight past *you're lying* and *this can't be* and lands on all the small things at once, and you can see each one arrive.

*That's why you found me at nineteen.*

*That's why we came to Purewater.*

*That's why you entered the Archery.*

He puts one hand flat on the table.

"How long have I been the reason?" he says. "For — any of it. All of it. The Order, the training, the—"

His voice goes.

He looks up, and he isn't looking at Temerach.

He's looking at **you** — the stranger, the one with no stake — and he says:

"Is she telling the truth?"


===== USER [2026-09-07T21:10:41.209Z] =====
Take off the vestment.


===== USER [2026-09-07T21:10:43.851Z] =====
[Request interrupted by user]


===== USER [2026-09-07T21:13:25.401Z] =====
Yeah. Course she is. 

Go find your brother. 

- then back to Temerach. He’s better looking than Santo.

Huh. Does that mean you’re that shitbird’s heirs? What does that make you? A Baronet?


===== ASSISTANT [2026-09-07T21:13:47.098Z] =====
You pull the sash off over your head and drop the whole vestment on the chair, and stand there in your own filthy shirt and ringmail, which answers his question about who's talking before you open your mouth.

"Yeah. Course she is."

That's all. You don't dress it and you don't explain it and you don't tell him it'll be all right.

"Go find your brother."

He stares at you.

"Where?"

"Don't know. It's your city, not mine." A shrug. "But he's got your face, so ask around. Someone'll have seen it."

---

Then, to Temerach, conversationally, while the boy is sitting down very suddenly:

"He's better looking than Santo."

Temerach makes a small strangled noise.

"Huh," you say. "Does that make them the shitbird's heirs, then? What's that make you, lad — a Baronet?"

---

**Temerach answers, because she has spent four years in law books.**

"No. And yes. And that is the most dangerous thing in this room."

She finally sits.

"Bastards do not inherit. Not in the border law and not here — that's clean. But Santo di Teufel was the only legitimate issue, and Santo is dead, and if Hanzo is attainted for desecration and demon-craft then the barony and the tower and everything in it goes back to the Crown to dispose of.

"And when a Crown disposes of a border holding, it looks for **blood**. Not because bastards have a right. Because it's tidier to hand a wild border march to somebody the local men will follow than to install a stranger and pay for a garrison for twenty years."

She looks at Conall.

"So no, you are not his heir. But there are men in three counties who will hear *the di Teufel bastard* and start doing arithmetic — and there is a border tower full of a hundred years of that family's work sitting empty tonight, and there is a movement of people who wanted a Dragon King badly enough to fund all of this, and they have just lost their candidate."

A pause.

"You and your brother are going to be *extremely* interesting to some very bad people by the end of the month. Both of you. And neither of you has any protection at all except the Order and me."

Conall says, hoarsely: "And him. He's alive. He knows I exist now?"

"He will by tonight."


===== USER [2026-09-07T21:20:52.921Z] =====
Ask Marisette to get him. Let’s make it a party.


===== ASSISTANT [2026-09-07T21:21:16.716Z] =====
Marisette does not need to be asked twice, and she does not need an hour.

"Randall." She says it the way you'd name a nephew. "Pearl-born, raised in Corliss's house and then Asphodel's, thieves like a gentleman and drinks like one too. I have known that boy since he was *four*."

She's already writing.

"He'll be at the Promise of Heaven or the Oyster, and if he's at neither, Asphodel will produce him inside the hour because she always can."

Then she stops writing and looks up, and something occurs to her.

"He's had a *strange* three days, that boy. Somebody put dragon-gold on the street for a face like his and he's been sleeping somewhere different every night and hasn't told anybody why."

---

**The Moist Oyster**, that evening.

You pick it because Thorne is owed the true version, once, and because it is the only room in Purewater where a Guildmaster, a thief, a priestess and a wolf can all be in the same place and nobody will comment.

Constantine sends food he can't afford to send. Marisette sends wine nobody will be able to afford to drink again. Ravella comes in through the water-door with four of hers, which stops the room for a moment.

**Ila** is there because she threatened Constantine with a very specific kind of hell, and she has attached herself to **Bird** — who is sitting in the warmest corner in three cloaks, eating steadily, saying almost nothing, with Gardwen on one side and a wolf across his feet.

**Nerissa** does not come. She sends Lilura, and a note, and a cask.

**Hesper** comes late, from the school, and says the two shallow girls are out and sleeping, and does not say anything about the third.

And **Thorne** is in his corner with his chalk, watching the door.

---

At about the ninth bell, Asphodel comes in with a young man behind her.

Dark. Twenty-two. Well-dressed in a way that isn't his money.

He is halfway through saying something to her when he sees the man standing up at the far table — the one with his own face on him — and the sentence just stops.

The whole room stops with it.

**Conall and Randall look at each other across the Moist Oyster for the first time in twenty-two years.**

Neither of them says anything.

And Thorne, very quietly, from his corner, to nobody at all:

"*Oh*, that's good."


===== USER [2026-09-07T21:23:01.845Z] =====
Great. Call it. That’s a wrap


===== ASSISTANT [2026-09-07T21:25:07.932Z] =====
**That's a wrap.** Session logged, exported, committed. Graph consistent — 42 facts, 81 knowledge edges, no problems.

---

## Session 1 — Magda

Four days. One PC. A ford to the Moist Oyster.

You arrived a stranger, knelt in the mud to swear yourself to a woman you'd met ten minutes earlier, and ended it standing in black water giving a thousand-year-old murdered knight back to your goddess.

**What you did along the way:** killed the Baron's heir with a sling stone and fed him to pigs. Faced down a customs man by looking at him. Got a laundress and a waste-boy to hand you the shape of the entire conspiracy — one bag of boiled sheets a day, the same wound in the same place, a port barred from outside. Bought a crime lord with a ship's cargo and the Mermaid's Court with two dead men. Took the DragonBarge in the Mouth. Killed Blau from a rowing boat and then finished him with an axe. Sent a Baron a severed head in a presentation case signed *the pig woman*. Tore the latch off his throat on the water-stair.

**The dice never let it be the written adventure.** Santo's binding *succeeded* — 19 against a Formidable 25 — which is the only reason Emmeralda lived to be bored and chatty and tell Hesper what a shade was. The whole back half of the campaign came out of a failed script.

**And it cost.** You beheaded a bound prisoner and destroyed the only route to a fourteen-year-old girl. Nerissa told you exactly what that was, worked with you anyway, and told you you'll never be welcome on Temple Isle again. That's recorded, not softened.

**Bird is free.** Seventeen, empty, his own, asleep in three cloaks with a wolf across his feet and a girl who's been looking for him for ten years beside him.

---

**Still open:** Bettan and the third filled girl. Emmeralda, still carrying hers. The Awake the Dragon Movement — they lost their candidate but they keep the border tower and Thuban's old cell. Two bastard di Teufel twins who just became very interesting to some very bad people.

And Thorne is still owed the true version. Once. All of it, in order, never written down.

Pick it up whenever — `get-context --compact` puts you back in that corner of the Oyster.


===== USER [2026-09-07T21:29:23.788Z] =====
Make sure it’s all stored. Then write a novelization of it from the start to the end of the game. Include what’s next in the summary.


===== ASSISTANT [2026-09-07T21:29:28.280Z] =====
Verifying storage first, then reading the novelization workflow the repo defines.


===== ASSISTANT [2026-09-07T21:30:05.171Z] =====
Everything is stored and clean:

| | |
|---|---|
| **Database** | consistent — 42 facts, 81 knowledge edges, 19 journal events |
| **Campaign package** | `2fab82d`, working tree clean |
| **Engine repo** | `f72ea12` on `feat/living-world-agendas`, clean *(not yet merged to main)* |

Now the novelization. Following the repo's workflow — extract first.


===== ASSISTANT [2026-09-07T21:30:46.677Z] =====
Two things surfaced that I'll state and proceed on rather than stall:

**1. A canon conflict I created.** Cailan's sheet gives his birth name as **Gabriel**. In play I had Gardwen say *"I don't know what his name is."* Those can't both stand. I'll resolve it in the novel the way that costs the most and contradicts nothing: she *does* say his name, and he doesn't answer to it — which is why she reaches for *Bird*. Say the word if you'd rather I did it differently.

**2. Style.** You didn't name one. **Hemingway** — plain declaratives, physical detail, emotion held under the surface. Magda has been talking like that for four days.


===== ASSISTANT [2026-09-07T21:31:27.438Z] =====
Pandoc and Typst are both here, so this will build to PDF. Writing the chapters.


===== ASSISTANT [2026-09-07T21:32:26.762Z] =====
Good — **Bird** it is. He'll be Bird in the novel, and I'll leave the birth name out of the prose entirely rather than have her reach for it.


===== ASSISTANT [2026-09-07T21:33:18.844Z] =====
Confirmed — her sheet says *"protective of **her** workers"*, *"Santo's attack on Emmeralda in **her** house"*, *"**she** keeps a stiletto and a loaded hand crossbow close."*

**Constantine is a woman.** I made her a man for four days of play and never checked the sheet. Fixing the novel, since that's the artifact that lasts.


===== ASSISTANT [2026-09-07T21:38:17.452Z] =====
Caught an ordering error in my own draft — I put the beheading before the failed rite. It happened *after* the prisoner revealed the latch. Rewriting that chapter in the true sequence.


===== ASSISTANT [2026-09-07T21:40:14.165Z] =====
Now the afterword with what's still open, then the build.


===== ASSISTANT [2026-09-07T21:41:06.820Z] =====
Stored, novelized, built, committed.

## Storage

| | |
|---|---|
| **Database** | consistent — 42 facts, 81 knowledge edges, 19 journal events |
| **Campaign package** | committed, clean |
| **Engine repo** | clean on `feat/living-world-agendas` — **not yet merged to main** |

## The novel

**`And Then the Dragons Came: Purewater`** — 14 chapters plus a prelude, ~17,500 words, **145 pages**, built to PDF at:

`~/purewater-campaign-v2/novels/and-then-the-dragons-came-purewater/`

Hemingway style card pinned, per your repo's own workflow — short declaratives, concrete nouns, scenes ending one beat before the payoff. It runs the ford → the water-gate → the shrieks of the Sylph → the scullery → the laundress → Marisette and Nerissa → Lost Isle → Thorne naming Thuban → the Mouth → the failed rite → the Tourney → the funeral → the Oyster. The last chapter is **What Is Still Open**.

**Three corrections I made while writing, all against the character sheets rather than against the transcript:**

- **Constantine is a woman.** Her sheet says *"protective of **her** workers"* and *"Santo's attack on Emmeralda in **her** house."* I ran her as a man for four days without ever checking. The novel restores her.
- **Bird.** Your call, and the better one — I've left the birth name out of the prose entirely.
- **An ordering error in my own first draft:** I had the beheading before the failed rite. It happened *after* the prisoner revealed the latch. Rewritten.

Canon flowed one way — nothing invented for the book went back into the journal, the lore, or the fact graph.

## What's still open, in the book's own words

Bettan and the third filled girl. Emmeralda, comfortable and charming and still carrying hers, with the only man who might have known how to get it out in a sack. The Awake the Dragon Movement, who lost a candidate but not a purpose, and still hold the border tower. Two young men in a tavern who are about to become very interesting to some very bad people.

And the stair — uncovered, swept, and opened twice in one night by someone who now knows how.

Thorne is still owed the true version. Once, in order, never written down.


===== USER [2026-09-07T22:00:56.778Z] =====
OK. It's a bit spotty. The way that we're recording the session isn't capturing the beats of what I think makes the story work and some things are just off - there was a discussion about how to dispose of Santo's body in the water until Magda thought of pigs for example. 

1. Let's take a look at Claudes logs in .claude - extract the exact text from the prompts and my actions and make sure that everything meaningful is recorded in the journal. 
2. Then read my writing to use MY writing style in the telling of this tale. Use this handwritten draft from the original game I played in Sanctuary. Don't get confused between the two games. 
3. Then generate a new version of the novel, side by side to the first.


===== ASSISTANT [2026-09-07T22:01:09.632Z] =====
Three-part job. Starting with the logs — let me find what Claude Code actually recorded.


===== ASSISTANT [2026-09-07T22:01:29.476Z] =====
Found it — a 6.2 MB session log. Extracting the real transcript.
