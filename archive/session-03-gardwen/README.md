# Purewater — Gardwen

A Classic Fantasy Imperative port of 'And then the Dragons Came', relocated to Purewater -- a Venice-like canal city where the sacred waters of the Lake Lady meet the sea. Baron Hanzo di Teufel arrives with his Dragon Knights for the Lake Lady's Tourney, his possessed champion concealed among them. Four strangers arrive the same week. Built as a living world: every NPC and faction runs its own agenda on a clock, and what the party does not witness happens anyway.

A **Mythras Imperative** campaign in the
[mythras-gm](https://github.com/fourth-wall-gaming/mythras-gm) publishable
campaign format (v1.1).

| Contents | Count |
|---|---|
| Lore entries | 22 |
| Characters | 43 (PCs: Conall Bjornlasch, Gardwen, Magda, Randall) |
| Creature templates | 4 |
| Locations | 20 |
| Factions | 14 |
| Encounters | 0 |
| Journal events | 48 |
| Agendas | 44 |
| Beats | 47 |
| Facts | 55 |
| Knowledge edges | 127 |

## Repository layout

| Directory | Contents |
|---|---|
| `lore/` | The worldbook, one markdown file per entry, grouped by category |
| `characters/` | PCs, NPCs, and creatures (full sheets + GM narratives, JSON) |
| `templates/` | Reusable creature/NPC stat blocks (JSON) |
| `locations/` | Places (markdown + frontmatter) |
| `factions/` | Factions and organizations (markdown + frontmatter) |
| `encounters/` | Combat encounter state (JSON) |
| `journal/` | The campaign event log (JSON) |
| `agendas/` | What each NPC and faction wants, on a progress clock |
| `beats/` | What happens next if nobody interferes, scheduled in world time |
| `facts/` | Situational truth: one proposition per file, with when it became true |
| `knowledge.json` | Who knows which fact, how, and since when |

## The living world (agendas)

What the world is doing while the PCs are elsewhere. Each agenda is a goal held
by a character or faction, tracked on a clock; the `beats/` directory holds the
concrete things those goals produce, scheduled against the world clock. Run
`tick` between scenes to find out what has come due.

- [A di Teufel who is not his](agendas/a-di-teufel-who-is-not-his.md) -- *Hanzo di Teufel* (1/6)
- [Be heard by someone who can end it](agendas/be-heard-by-someone-who-can-end-it.md) -- *Thuban Eta* (5/8)
- [Be taken seriously by somebody](agendas/be-taken-seriously-by-somebody.md) -- *Sana* (0/4)
- [Bring back what the soldiers say](agendas/bring-back-what-the-soldiers-say.md) -- *Mariarta* (1/4)
- [Clean up after the young master](agendas/clean-up-after-the-young-master.md) -- *Blau* (2/6)
- [Do right by the city on the facts I am given](agendas/do-right-by-the-city-on-the-facts-i-am-given.md) -- *Maro Quist* (0/6)
- [Do something about it myself](agendas/do-something-about-it-myself-2.md) -- *Ila* (0/4)
- [Do something about it myself](agendas/do-something-about-it-myself.md) -- *Ila* (2/4)
- [Do what the dream keeps showing me](agendas/do-what-the-dream-keeps-showing-me.md) -- *Magda* (3/6)
- [Earn the white belt](agendas/earn-the-white-belt.md) -- *Corvin* (0/4)
- [Field the champion and take the city](agendas/field-the-champion-and-take-the-city.md) -- *Hanzo di Teufel* (2/8)
- [Find out what I was brought here for](agendas/find-out-what-i-was-brought-here-for.md) -- *Conall Bjornlasch* (4/6)
- [Find out what the strangers are](agendas/find-out-what-the-strangers-are.md) -- *Kerrin (brown coat)* (1/4)
- [Find out why the goddess has stopped answering](agendas/find-out-why-the-goddess-has-stopped-answering.md) -- *Lilura Deepcurrent* (2/8)
- [Find who carved Emmeralda](agendas/find-who-carved-emmeralda.md) -- *Marisette* (3/6)
- [Get aboard that hull and understand it](agendas/get-aboard-that-hull-and-understand-it.md) -- *Guildmaster Torval Bluehand* (1/6)
- [Get it back before my father finds out](agendas/get-it-back-before-my-father-finds-out.md) -- *Santo di Teufel* (2/4)
- [Get one word out that is mine](agendas/get-one-word-out-that-is-mine.md) -- *Cailan* (1/6)
- [Get paid, keep the company whole](agendas/get-paid-keep-the-company-whole.md) -- *Tat Atarer* (0/4)
- [Get the book into hands that can use it](agendas/get-the-book-into-hands-that-can-use-it.md) -- *Abel Weir* (2/6)
- [Get through this week with my name clean](agendas/get-through-this-week-with-my-name-clean.md) -- *Alderic Vantt* (1/4)
- [Govern this city properly, just once](agendas/govern-this-city-properly-just-once.md) -- *Prince Emeric* (1/6)
- [Have her](agendas/have-her.md) -- *Santo di Teufel* (0/6)
- [Hold the streets as if we own them](agendas/hold-the-streets-as-if-we-own-them.md) -- *The Dragon Knights* (3/6)
- [Keep Randall out of the water he is wading into](agendas/keep-randall-out-of-the-water-he-is-wading-into.md) -- *Asphodel* (1/4)
- [Keep my son's neck out of it](agendas/keep-my-son-s-neck-out-of-it.md) -- *Hesketh Pyle* (1/4)
- [Keep the Lady's water clean](agendas/keep-the-lady-s-water-clean.md) -- *High Priestess Nerissa* (3/6)
- [Keep the champion unseen](agendas/keep-the-champion-unseen.md) -- *Hanzo di Teufel* (1/4)
- [Keep the port lawful in a week when law has been suspended](agendas/keep-the-port-lawful-in-a-week-when-law-has-been-suspended.md) -- *Harbormaster Velen Deepkeel* (1/4)
- [Keep the table level](agendas/keep-the-table-level.md) -- *Crowbill* (2/6)
- [Know it first, and keep my people invisible](agendas/know-it-first-and-keep-my-people-invisible.md) -- *Ravella* (1/6)
- [Live -- and be believed](agendas/live-and-be-believed.md) -- *Emmeralda* (0/4)
- [Live with what I signed](agendas/live-with-what-i-signed.md) -- *Ivo Calder* (2/4)
- [Make them pay for one of ours](agendas/make-them-pay-for-one-of-ours.md) -- *Marda Blackwater* (3/4)
- [One big score, and a name](agendas/one-big-score-and-a-name.md) -- *Nus* (0/4)
- [One good week off the Tourney crowd](agendas/one-good-week-off-the-tourney-crowd.md) -- *Randall* (1/4)
- [Protect my house, and get justice for my girl](agendas/protect-my-house-and-get-justice-for-my-girl.md) -- *Constantine* (1/4)
- [See the dragon-thing come round again, and be believed th...](agendas/see-the-dragon-thing-come-round-again-and-be-believed-th.md) -- *Thorne* (1/4)
- [Serve the Javelin well enough to be trusted with more](agendas/serve-the-javelin-well-enough-to-be-trusted-with-more.md) -- *Murgeroch* (0/4)
- [Serve the Quiet Hand without ever being seen to](agendas/serve-the-quiet-hand-without-ever-being-seen-to.md) -- *Hesper* (1/6)
- [Settle with Randall](agendas/settle-with-randall.md) -- *Sinnit* (0/4)
- [Shield the boy, unmask the house](agendas/shield-the-boy-unmask-the-house.md) -- *Temerach Nebulo* (3/6)
- [Sort the sixty, and keep reporting on the Baron](agendas/sort-the-sixty-and-keep-reporting-on-the-baron.md) -- *Cassian Bree* (2/6)
- [Wake a Dragon King](agendas/wake-a-dragon-king.md) -- *The Awake the Dragon Movement* (3/10)

## The worldbook (lore index)

**character-creation**
- [The Four Companions](lore/character-creation/the-four-companions.md)

**cosmology**
- [The Realm of Mystamyr](lore/cosmology/the-realm-of-mystamyr.md)

**daily-life**
- [The dragonshits in the streets](lore/daily-life/the-dragonshits-in-the-streets.md)
- [The Lake Lady's Tourney](lore/daily-life/the-lake-lady-s-tourney.md)

**entry-points**
- [Entry Point: Conall on the road](lore/entry-points/entry-point-conall-on-the-road.md)
- [Entry Point: Gardwen at the ford](lore/entry-points/entry-point-gardwen-at-the-ford.md)
- [Entry Point: Magda at the ford](lore/entry-points/entry-point-magda-at-the-ford.md)
- [Entry Point: Randall in Caravan Square](lore/entry-points/entry-point-randall-in-caravan-square.md)

**geography**
- [The City and Its Islands](lore/geography/the-city-and-its-islands.md)

**gm-guide**
- [GM Guide: Dramatis Personae](lore/gm-guide/gm-guide-dramatis-personae.md) *(GM only)*
- [GM Guide: Running the Living World](lore/gm-guide/gm-guide-running-the-living-world.md) *(GM only)*
- [GM Guide: Supporting and Offscreen Cast](lore/gm-guide/gm-guide-supporting-and-offscreen-cast.md) *(GM only)*
- [The DragonBarge: deck plan](lore/gm-guide/the-dragonbarge-deck-plan.md) *(GM only)*
- [The Governor's council](lore/gm-guide/the-governor-s-council.md) *(GM only)*
- [The Doomline -- what happens if nobody interferes](lore/gm-guide/the-doomline-what-happens-if-nobody-interferes.md) *(GM only)*

**gm-secret**
- [GM Secrets: The Possession Scheme](lore/gm-secret/gm-secrets-the-possession-scheme.md) *(GM only)*
- [The Ember Society](lore/gm-secret/the-ember-society.md) *(GM only)*

**history**
- [The Dragon Kings and the Lake Lady](lore/history/the-dragon-kings-and-the-lake-lady.md)

**law**
- [The King's justice, and how a lord is called to answer](lore/law/the-king-s-justice-and-how-a-lord-is-called-to-answer.md)

**magic-system**
- [Magic in Purewater: Water and Fire](lore/magic-system/magic-in-purewater-water-and-fire.md)

**religion**
- [The Gods of Mystamyr](lore/religion/the-gods-of-mystamyr.md)
- [The Order and the Swords: one goddess, two houses](lore/religion/the-order-and-the-swords-one-goddess-two-houses.md)

## Dramatis personae

**Player characters**
- [Conall Bjornlasch](characters/pcs/conall-bjornlasch.json) — Warranted investigator of the King's Assay -- the Crown's arcane inspectorate; twin brother of Randall and secretly a son of Baron Hanzo. A razor-sharp investigator (Insight 88) who is also a capable fighter.
- [Gardwen](characters/pcs/gardwen.json) — Feral-raised elf druid and lone survivor of a Dragon Knight raid; a rank-1 divine caster of nature and pure-water magic who walks with a befriended she-wolf, searching for her long-lost brother.
- [Magda](characters/pcs/magda.json) — Aged barbarian berserker and sworn servant of the death-goddess Hel; Blessed by Hel (she does not age), she guards Gardwen and the lost twins and fights with berserk fury despite her years.
- [Randall](characters/pcs/randall.json) — Street thief of Purewater, raised in a brothel on the Pearl; identical twin of Conall and secretly a son of Baron Hanzo. A nimble, silver-tongued rogue (Deceit 75, Stealth 72, Sleight 71).

**NPCs**
- [Abel Weir](characters/npcs/abel-weir.json) — Sergeant of the City Watch, forty-one, twenty-two years in blue-grey. Keeps the referral book at the Isle post -- four inches of complaints against the Baron's people that he has been ordered to record and not act on. He is very tired.
- [Alderic Vantt](characters/npcs/alderic-vantt.json) — Merchant prince and councillor, fifty-two: borderland transit, grain and timber. The Baron's host -- the Dragon Knights are camped on his water-meadow -- and the man who drafted the standing order and put it in front of the Prince.
- [Asphodel](characters/npcs/asphodel.json) — A courtesan at the Promise of Heaven, the house where Randall grew up. Warm, quick, and trusted by him 'as brother and sister' -- his closest confidante on the Pearl Quay and a ready source of information from the working girls.
- [Beck](characters/npcs/beck.json) — Constantine's houseman at the Sylph's Embrace -- eighteen years on the same door. He was on it the night Emmeralda died.
- [Blau](characters/npcs/blau.json) — Baron Hanzo's albino lieutenant -- known to the ranks as Commander Vask. A thin, red-eyed, burn-scarred killer with unnatural strength who runs the Dragon Knights' day-to-day command and handles the Baron's 'dirty work': a cold, efficient assassin and intimidator.
- [Cailan](characters/npcs/cailan.json) — Gardwen's possessed brother (birth name Gabriel) -- the Baron's tournament champion, host to the ancient dragon-knight spirit Thuban Eta. Dragon-scale armor fused to his skin; eyes flicker reptilian when possessed; fights with uncanny ancient skill and minor fire.
- [Cassian Bree](characters/npcs/cassian-bree.json) — Secretary of the Ember Society, forty-four: courteous, damp-handed, immaculate minutes, boring on purpose. The only confirmed member of the Awake the Dragon Movement in Purewater -- and everything he does is legal.
- [Constantine](characters/npcs/constantine.json) — Proprietor of The Sylph's Embrace on the Pearl -- shrewd, protective of her workers, fiercely independent. Operates under Marisette's authority. After Santo's attack on Emmeralda in her house, she is hiring protection and wants justice.
- [Corvin](characters/npcs/corvin.json) — Sword of the Lake, twenty-two, earnest and brave and not remotely subtle. Rows well. Currently in a brown coat that is too short in the arm and sulking about it.
- [Crowbill](characters/npcs/crowbill.json) — Leader of Purewater's criminal underworld -- canal smuggling, gambling, protection. Wiry and forgettable but for a small crow tattoo on his right hand. A master of streets and shadows (Streetwise 88, Stealth 82, Conceal 78) who keeps to a code: no killing locals, no harming children, no touching the Lake Lady's sites.
- [Emmeralda](characters/npcs/emmeralda.json) — Elven courtesan of The Sylph's Embrace -- poised, magnetic, and the finest performer on the Pearl (CHA 18, Seduction 88, Dance 85).
- [Guildmaster Torval Bluehand](characters/npcs/guildmaster-torval-bluehand.json) — Guildmaster of the Watercrafters -- middle-aged, practical innovator whose hands are permanently blue-tinged from decades of watercraft enchantment. A Magic-User specialized in water artifice (Craft 85, Arcane Casting 60, Mechanisms 80) rather than battle magic; his guild's enchantments keep the canal-city running.
- [Hanzo di Teufel](characters/npcs/hanzo-di-teufel.json) — Baron Hanzo di Teufel -- the campaign's master villain: a charismatic borderland noble and fire-wielding arcane sorcerer/demonologist who commands the Dragon Knights, runs possession rituals, and secretly seeks to become a Dragon King.
- [Harbormaster Velen Deepkeel](characters/npcs/harbormaster-velen-deepkeel.json) — Stern, weathered Harbormaster with forty years at the docks -- meticulous, traditional, publicly incorruptible. A consummate seaman and administrator (Seamanship 85, Navigation 82, Maritime Law 80) who controls the harbor's lawful face while quietly tolerating Crowbill's smuggling.
- [Hesketh Pyle](characters/npcs/hesketh-pyle.json) — Councillor, fifty-eight: salt, glass and a good name going soft. Votes as he is told and drinks more than he did last year. The crack in the council.
- [Hesper](characters/npcs/hesper.json) — To Purewater, Hesper is the madame Marisette's cold, dangerous mage-enforcer -- quiet, watchful, able to drop a strong man with a single spoken word. The truth is the opposite of what the mask suggests: Hesper is a deep-cover agent of the Quiet Hand, a hidden fellowship that works unseen for the good of the world, and the menace is a costume worn over a conscience. Master arcane caster (Arcane Casting 100, Willpower 95).
- [High Priestess Nerissa](characters/npcs/high-priestess-nerissa.json) — High Priestess of the Temple of the Lake Lady -- middle-aged, silver-streaked hair, blue-green robes that ripple like water. A powerful divine caster (Piety 92, Willpower 85) who senses water corruption, blesses sacred waters, and speaks with water spirits. Temple law forbids her from intervening directly, so she works through the PCs.
- [Ila](characters/npcs/ila.json) — A young elven girl (about thirteen) at the Sylph's Embrace, devoted to Emmeralda. An innocent of the Pearl, and a thread on the party's conscience.
- [Ivo Calder](characters/npcs/ivo-calder.json) — Tide Master of the Watercrafters Guild, fifty, assessor by appointment to the city -- and the man who signed the Lake Lady's fouling alarm off as a false reading six weeks ago. He has not slept properly since.
- [Kerrin (brown coat)](characters/npcs/kerrin-brown-coat.json) — One of Crowbill's watchers. Dockside, unremarkable, brown coat. Professional -- follows, does not close.
- [Lilura Deepcurrent](characters/npcs/lilura-deepcurrent.json) — Deputy to High Priestess Nerissa and her right hand in the Order of the Lake Lady -- about thirty, dark, usually wet to the knee because she is the one who actually goes into the channel to check it. Rumoured merfolk ancestry on her mother's side; she holds her breath unnaturally long and does not discuss it. A genuine divine caster in her own right, and the person who decides who reaches the High Priestess and who does not.
- [Marda Blackwater](characters/npcs/marda-blackwater.json) — Broad-shouldered leader of The Dredgers, risen from the dredge-boats during a labor dispute five years ago. A powerful working-class champion (Brawn 75, Oratory 78, Influence 75) who rallies dock labor against the merchant princes and -- above all -- against the Baron's Dragon Knights.
- [Mariarta](characters/npcs/mariarta.json) — An older, canny courtesan of the Promise of Heaven with 'the calm intelligence of someone who can survive almost any situation involving men.' Sent up to entertain the Baron's soldiers, she brings back the hard intelligence on his guarded quarters -- Randall's most valuable inside source on the Dragon Knights' manor.
- [Marisette](characters/npcs/marisette.json) — Madame of The Mother of Pearl and the near-absolute authority over Purewater's Pearl -- the proprietors, Constantine among them, answer to her. A consummate social power broker who keeps the pleasure district running, keeps her accounts in obligations, and resents the disorder the Baron and Santo have brought to it. Her oldest rule: the Pearl sells a night, never a person.
- [Maro Quist](characters/npcs/maro-quist.json) — Councillor, seventy-one, thirty years on the council: incorruptible, formidable, and completely wrong. He voted for both instructions on the merits and will defend them to your face.
- [Murgeroch](characters/npcs/murgeroch.json) — Temerach Nebulo's squire and go-between -- the steady, competent young fighter who carries the knight's messages, screens her meetings, and tends her gear. Usually the first of Temerach's people the party deals with.
- [Nus](characters/npcs/nus.json) — A quick-fingered Purewater street thief and loyal friend of Randall -- lookout, fence, and second pair of hands for a job; nimble, streetwise, and easy to underestimate.
- [Prince Emeric](characters/npcs/prince-emeric.json) — The young Governor of Purewater -- the King's nephew, perhaps two-and-twenty: clever, idealistic, genuinely decent, and entirely unsuited to govern a city like this. He wants to reform Purewater; the factions humor him, manage him, and run rings around his good intentions.
- [Ravella](characters/npcs/ravella.json) — Half-merfolk proprietor of The Siren's Call -- pleasure house and information market in one. Subtle waterfolk tells (webbed fingers, water-reflecting eyes, Swim 90). A master broker (Insight 85, Streetwise 88, Commerce 80) with light innate water magic, secretly protecting the city's hidden waterfolk.
- [Sana](characters/npcs/sana.json) — Nineteen, dark red hair chopped ragged on the left side. High Priestess Nerissa's niece, six weeks at the temple and not yet resigned to it. Clever, not biddable, and a noticer -- she sees the thing nobody else in the room thought was worth looking at, and says so at the wrong moment.
- [Santo di Teufel](characters/npcs/santo-di-teufel.json) — Baron Hanzo's cruel son and heir -- a sadistic young fire-mage who has decided he wants Emmeralda of the Sylph's Embrace, and who carries a stolen ritual knife marked with the sigil of Asmodeus because he cannot imagine being told no.
- [Sinnit](characters/npcs/sinnit.json) — A brutish Purewater canal-rat and rival thief who nurses a hard grudge against Randall -- a brawling enforcer-type with a long memory and a short temper.
- [Tat Atarer](characters/npcs/tat-atarer.json) — Captain of the Dragon Knights -- a hardened, pragmatic mercenary commander who serves Baron Hanzo for pay, not ideology. Master fighter (combat 97%); 'the Baron pays for our swords, not our opinions.'
- [Temerach Nebulo](characters/npcs/temerach-nebulo.json) — Elf knight of the Swords of the Lake, called 'the Lakelady's Javelin'; a deadly archer and peerless martial fighter who has spent four years trying to get Baron Hanzo called to answer -- and has not yet dared make the accusation.
- [Thorne](characters/npcs/thorne.json) — Elderly storyteller of The Moist Oyster -- frail-seeming but with penetrating blue eyes and a cane that hides a blade. Secretly a former Order of the Lake initiate and Dragon-Knight-raid survivor with peerless historical lore (Dragon Kings era 92) and knowledge of possession-ritual weaknesses.
- [Thuban Eta](characters/npcs/thuban-eta.json) — The ancient dragon-knight spirit bound inside Cailan. A betrayed tactical genius from the Dragon Kings era, held in thrall by Baron Hanzo's ritual through his bones and the binding locket. Indomitable will (Willpower 95), peerless tactics, honors the old codes -- a potential ally if freed.
- [Orrin Sculle](characters/npcs/orrin-sculle.json) — The champion's keeper. Ten years feeding, dressing, washing and walking a boy who is not there, and talking to him every night while he does it.
- [Grissel Nye](characters/npcs/grissel-nye.json) — Carries out the ashes and the grates for all six counting-houses on Chandler'\''s Row, in before light and out before the clerks. Forty years. Deaf as a post. Cannot read.

**Creatures**
- [Ruhi](characters/creatures/ruhi.json) — Gardwen's befriended companion -- a loyal she-wolf; swift, keen-nosed and savage in the bite.

## Factions

- [Crowbill's Underworld](factions/crowbill-s-underworld.md) — Purewater's criminal underground -- canal smuggling, gambling, protection -- run to a code by the unremarkable crime lord Crowbill. Signaled by crow marks. The occupation is wrecking the equilibrium his business depends on.
- [The Awake the Dragon Movement](factions/the-awake-the-dragon-movement.md) — A shadowy movement to revive the ancient draconic order and transform men into Dragon Kings. Baron Hanzo's true cause; an existential threat to water magic.
- [The City Watch](factions/the-city-watch.md) — Purewater's ordinary police: about ninety men and women in blue-grey, competent at drunks, thieves and canal disputes -- and under standing orders not to provoke the Baron's people until the Tourney is over.
- [The Currents](factions/the-currents.md) — A leaderless network of spies and informants trading in secrets, not contraband. Marked by chalk water-signs; the hidden 'Source' directs it.
- [The Dragon Knights](factions/the-dragon-knights.md) — Baron Hanzo's 20-30 sworn warriors -- brutal mercenaries in dragon heraldry, enhanced with fire demonology. In Purewater for the Tourney and behaving like an army of occupation, because they have been told the watch will not touch them.
- [The Dredgers](factions/the-dredgers.md) — Labor guild and mutual-aid society of Purewater's working poor -- canal-clearers, dockers, fishers. Black armbands, white wave. Led by Marda Blackwater, and three hundred strong in a week when the Baron's men are taking their boats.
- [The Harbor Masters](factions/the-harbor-masters.md) — The regulatory guild of Purewater's docks and shipping -- tariffs, berths, maritime law. Dark blue uniforms, a harbor tower HQ, a publicly incorruptible Harbormaster, and increasingly corrupt upper ranks. They berthed the DragonBarge.
- [The King's Assay](factions/the-king-s-assay.md) — The Crown's chartered body for licensing, inspecting and recording arcane practice in Mystamyr -- founded after the uprising to put magic on a register. Warrants, hallmarks, and a personal steel punch. Conall is one of theirs.
- [The Mermaid's Court](factions/the-mermaid-s-court.md) — A secretive society of pure-water practitioners bound to merfolk, preserving water magic older than the city. Hidden under Lost Isle; led by the enigmatic 'Pearl'.
- [The Order of the Lake Lady](factions/the-order-of-the-lake-lady.md) — The water-faith of Purewater: priesthood of the lake goddess, guardians of pure water magic, and owners of the Tourney. Robed in blue-green with silver wave patterns. Their fouling alarm has been silenced by written instruction.
- [The Pleasure Houses of the Pearl](factions/the-pleasure-houses-of-the-pearl.md) — The courtesan network of the Pearl, under the madame Marisette's near-absolute authority. Constantine's Sylph's Embrace and Ravella's Siren's Call among them. The richest information market in Purewater, and the campaign's front door.
- [The Quiet Hand](factions/the-quiet-hand.md) — A secret, centuries-old fellowship that steers the world toward the good from the shadows -- by knowing first and acting unseen. Espionage as mercy. Hesper is their agent in Purewater. (GM: a benevolent hidden patron.)
- [The Swords of the Lake](factions/the-swords-of-the-lake.md) — An austere knightly order sworn to the Lake Lady and the protection of the realm's water magic. Temerach Nebulo is their most famous blade -- and the only armed authority in Purewater that does not answer to the Governor's council.
- [The Watercrafters Guild](factions/the-watercrafters-guild.md) — Boat-builders, canal engineers, water-diviners and makers of water-enhanced goods -- the artisans whose enchantments keep the canal-city working. Indigo sashes. One of their Tide Masters signed the Baron's corruption off as a false reading.

## Loading this campaign

```bash
python skills/mythras-gm/mythras_gm.py import-campaign --path <this-directory> --new-ids
```

Then resume play with `get-context --campaign <new-id>`.

> Lore files marked `visibility: "gm"` contain spoilers. Players: browse
> `lore/` but skip anything GM-marked, and stay out of `encounters/` and
> `journal/` if you want to avoid table history.

Based on Mythras Imperative, Written by Pete Nash and Lawrence Whitaker,
published by The Design Mechanism, Copyright 2023, used under the ORC License.
