# And Then the Dragons Came: Purewater

A Classic Fantasy Imperative port of 'And then the Dragons Came', relocated to Purewater -- a Venice-like canal city where the sacred waters of the Lake Lady meet the sea. Baron Hanzo di Teufel arrives with his Dragon Knights for the Lake Lady's Tourney, his possessed champion concealed among them. Four strangers arrive the same week. Built as a living world: every NPC and faction runs its own agenda on a clock, and what the party does not witness happens anyway.

A **Mythras Imperative** campaign in the
[mythras-gm](https://github.com/fourth-wall-gaming/mythras-gm) publishable
campaign format (v1.2).

| Contents | Count |
|---|---|
| Lore entries | 53 |
| Characters | 202 (PCs: Halla, Nimras, Hrill Helmdance) |
| Creature templates | 4 |
| Locations | 94 |
| Factions | 24 |
| Encounters | 21 |
| Journal events | 1197 |
| Agendas | 48 |
| Beats | 115 |
| Facts | 767 |
| Knowledge edges | 1884 |

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

- [A di Teufel who is not his](agendas/a-di-teufel-who-is-not-his.md) -- *Hanzo di Teufel* (0/6)
- [Clean up after the young master](agendas/clean-up-after-the-young-master.md) -- *Blau* (2/6)
- [Culvert robbery: take carrier cart](agendas/culvert-robbery-take-carrier-cart.md) -- *Joric Vane* (0/3)
- [End the hunting conversion](agendas/end-the-hunting-conversion.md) -- *Sivren Kest* (2/3)
- [Field the champion and take the city](agendas/field-the-champion-and-take-the-city.md) -- *Hanzo di Teufel* (2/8)
- [Find who carved Emmeralda](agendas/find-who-carved-emmeralda.md) -- *Marisette* (2/6)
- [Finish the comparison before returning](agendas/finish-the-comparison-before-returning.md) -- *Rennic Vaur* (0/4)
- [Get paid, keep the company whole](agendas/get-paid-keep-the-company-whole.md) -- *Tat Atarer* (0/4)
- [Have her](agendas/have-her.md) -- *Santo di Teufel* (0/6)
- [Hold the streets as if we own them](agendas/hold-the-streets-as-if-we-own-them.md) -- *The Dragon Knights* (2/6)
- [Hrill road: a usable independent crossing](agendas/hrill-road-a-usable-independent-crossing.md) -- *Maelin Voss* (3/3)
- [Hrill road: impose exclusive pass command](agendas/hrill-road-impose-exclusive-pass-command.md) -- *Sir Aldren Vaust* (0/4)
- [Hrill road: sell one stolen funerary standard](agendas/hrill-road-sell-one-stolen-funerary-standard.md) -- *Sir Aldren Vaust* (0/3)
- [Identify and obstruct the interfering mage](agendas/identify-and-obstruct-the-interfering-mage.md) -- *Captain Mara Senn* (0/3)
- [Keep Greywatch people free and post independent](agendas/keep-greywatch-people-free-and-post-independent.md) -- *Corporal Dera Venn* (0/3)
- [Keep the Lady's water clean](agendas/keep-the-lady-s-water-clean.md) -- *High Priestess Nerissa* (0/6)
- [Keep the champion unseen](agendas/keep-the-champion-unseen.md) -- *Hanzo di Teufel* (1/4)
- [Keep the table level](agendas/keep-the-table-level.md) -- *Crowbill* (0/6)
- [Long Shore: dependable consenting supply passage](agendas/long-shore-dependable-consenting-supply-passage.md) -- *Edda Vale* (3/3)
- [Long Shore: preserve independent safe shallows](agendas/long-shore-preserve-independent-safe-shallows.md) -- *Ilyen* (0/3)
- [Long Shore: take reedback horn plates](agendas/long-shore-take-reedback-horn-plates.md) -- *Garr Hew* (2/3)
- [Make Randall say it](agendas/make-randall-say-it.md) -- *Sinnit* (2/6)
- [Make them pay for one of ours](agendas/make-them-pay-for-one-of-ours.md) -- *Marda Blackwater* (1/4)
- [Midnight Exchange: independent examination of advertised papers](agendas/midnight-exchange-independent-examination-of-advertised-papers.md) -- *Oren Vey* (3/3)
- [Midnight Exchange: recover claimant property by purchase or evidence](agendas/midnight-exchange-recover-claimant-property-by-purchase-or-evidence.md) -- *Olt Marek* (0/3)
- [Midnight Exchange: recover the authentic Ash Register](agendas/midnight-exchange-recover-the-authentic-ash-register.md) -- *Severin Rusk* (0/4)
- [Midnight Exchange: sell the genuine clearance consignment](agendas/midnight-exchange-sell-the-genuine-clearance-consignment.md) -- *Seressa Venn* (0/3)
- [Notice resistance from local guards](agendas/notice-resistance-from-local-guards.md) -- *Tat Atarer* (2/6)
- [One big score, and a name](agendas/one-big-score-and-a-name.md) -- *Nus* (0/4)
- [Preserve a library worth finding](agendas/preserve-a-library-worth-finding.md) -- *Oren Vey* (0/6)
- [Put the Glass Hounds report before a warranted Assayer](agendas/put-the-glass-hounds-report-before-a-warranted-assayer.md) -- *Beren Holt* (3/3)
- [Quiet War: an armed toll command](agendas/quiet-war-an-armed-toll-command.md) -- *Captain Oth Bren* (0/3)
- [Quiet War: bind the waterfront to protection](agendas/quiet-war-bind-the-waterfront-to-protection.md) -- *Crowbill* (0/3)
- [Quiet War: exclusive waterfront carriage](agendas/quiet-war-exclusive-waterfront-carriage.md) -- *Sella Marr* (0/4)
- [Reclaim household authority without losing the city](agendas/reclaim-household-authority-without-losing-the-city.md) -- *Hanzo di Teufel* (1/4)
- [Recover Nessa working tools](agendas/recover-nessa-working-tools.md) -- *Nessa Rill* (3/3)
- [Recover keeper and protect boat fee](agendas/recover-keeper-and-protect-boat-fee.md) -- *Captain Surn Pike* (0/3)
- [Recover quarry arsenal for restorationist buyers](agendas/recover-quarry-arsenal-for-restorationist-buyers.md) -- *Merrit Dane* (1/3)
- [Remove Drell before the promised interview](agendas/remove-drell-before-the-promised-interview.md) -- *Blau* (0/4)
- [Sell the hunting pack](agendas/sell-the-hunting-pack.md) -- *Captain Mara Senn* (0/4)
- [Settle the missing teacher’s commission](agendas/settle-the-missing-teacher-s-commission.md) -- *Rennic Vaur* (3/3)
- [Shield the boy, unmask the house](agendas/shield-the-boy-unmask-the-house.md) -- *Temerach Nebulo* (1/6)
- [Shift requisition liability to Vantt](agendas/shift-requisition-liability-to-vantt.md) -- *Blau* (1/4)
- [Take Greywatch as an imperial foothold](agendas/take-greywatch-as-an-imperial-foothold.md) -- *Dame Avel Veyr* (0/3)
- [Take the champion beyond Purewater](agendas/take-the-champion-beyond-purewater.md) -- *Hanzo di Teufel* (1/4)
- [The one who works it out](agendas/the-one-who-works-it-out.md) -- *Kag* (0/4)
- [Turn seized grain into respectable collateral](agendas/turn-seized-grain-into-respectable-collateral.md) -- *Alderic Vantt* (1/6)
- [Wake a Dragon King](agendas/wake-a-dragon-king.md) -- *The Awake the Dragon Movement* (3/10)

## The worldbook (lore index)

**character-creation**
- [Rolling Your Own](lore/character-creation/rolling-your-own.md)
- [The Four Companions](lore/character-creation/the-four-companions.md) *(GM only)*
- [Nimras — character creation in progress](lore/character-creation/nimras-character-creation-in-progress.md)
- [Hrill Helmdance — character creation in progress](lore/character-creation/hrill-helmdance-character-creation-in-progress.md)

**cosmology**
- [The Realm of Thornmere](lore/cosmology/the-realm-of-thornmere.md)

**daily-life**
- [The dragonshits in the streets](lore/daily-life/the-dragonshits-in-the-streets.md)
- [The Lake Lady's Tourney](lore/daily-life/the-lake-lady-s-tourney.md)
- [Tourney entry fees](lore/daily-life/tourney-entry-fees.md)

**entry-points**
- [Entry Point: Conall on the road](lore/entry-points/entry-point-conall-on-the-road.md)
- [Entry Point: Gardwen at the ford](lore/entry-points/entry-point-gardwen-at-the-ford.md)
- [Entry Point: Magda at the ford](lore/entry-points/entry-point-magda-at-the-ford.md)
- [Entry Point: Randall in Caravan Square](lore/entry-points/entry-point-randall-in-caravan-square.md)

**evidence**
- [Rennic’s lodging note to Oren Vey](lore/evidence/rennic-s-lodging-note-to-oren-vey.md)

**geography**
- [The City and Its Islands](lore/geography/the-city-and-its-islands.md)
- [The Lands of Thornmere](lore/geography/the-lands-of-thornmere.md)

**gm-guide**
- [GM Guide: Conflicting agendas, and resolving them offscreen](lore/gm-guide/gm-guide-conflicting-agendas-and-resolving-them-offscreen.md) *(GM only)*
- [GM Guide: Dramatis Personae](lore/gm-guide/gm-guide-dramatis-personae.md) *(GM only)*
- [GM Guide: Running the Living World](lore/gm-guide/gm-guide-running-the-living-world.md) *(GM only)*
- [GM Guide: Supporting and Offscreen Cast](lore/gm-guide/gm-guide-supporting-and-offscreen-cast.md) *(GM only)*
- [The Catacombs: where they run](lore/gm-guide/the-catacombs-where-they-run.md) *(GM only)*
- [The DragonBarge: deck plan](lore/gm-guide/the-dragonbarge-deck-plan.md) *(GM only)*
- [The Governor's council](lore/gm-guide/the-governor-s-council.md) *(GM only)*
- [GM Procedure: Offscreen information flow](lore/gm-guide/gm-procedure-offscreen-information-flow.md) *(GM only)*
- [Marr measuring crew at the southern intake](lore/gm-guide/marr-measuring-crew-at-the-southern-intake.md) *(GM only)*

**gm-method**
- [Reusable adventure construction after pitch selection](lore/gm-method/reusable-adventure-construction-after-pitch-selection.md) *(GM only)*
- [Reusable brainstorming: dramatic arcs and shared campaign connections](lore/gm-method/reusable-brainstorming-dramatic-arcs-and-shared-campaign-connections.md) *(GM only)*

**gm-secret**
- [GM Secrets: The Possession Scheme](lore/gm-secret/gm-secrets-the-possession-scheme.md) *(GM only)*
- [The Ember Society](lore/gm-secret/the-ember-society.md) *(GM only)*

**history**
- [The Dragon Kings and the Lake Lady](lore/history/the-dragon-kings-and-the-lake-lady.md)
- [The Widow of the Pearl](lore/history/the-widow-of-the-pearl.md)

**house-rules**
- [Luck Is PC-Only](lore/house-rules/luck-is-pc-only.md)

**law**
- [The King's justice, and how a lord is called to answer](lore/law/the-king-s-justice-and-how-a-lord-is-called-to-answer.md)

**magic-community**
- [Purewater's working mages and the Understairs](lore/magic-community/purewater-s-working-mages-and-the-understairs.md)

**magic-politics**
- [Magic and power in Purewater](lore/magic-politics/magic-and-power-in-purewater.md)

**magic-system**
- [Magic in Purewater: Water and Fire](lore/magic-system/magic-in-purewater-water-and-fire.md)

**player-briefing**
- [Choosing a Character](lore/player-briefing/choosing-a-character.md)
- [Welcome to Purewater](lore/player-briefing/welcome-to-purewater.md)

**religion**
- [The Gods of Thornmere](lore/religion/the-gods-of-thornmere.md)
- [The Order and the Swords: one goddess, two houses](lore/religion/the-order-and-the-swords-one-goddess-two-houses.md)

**scenario**
- [Glass Hounds: selected adventure and finite operations](lore/scenario/glass-hounds-selected-adventure-and-finite-operations.md) *(GM only)*
- [Hrill: The Road Beyond the Banners — live preparation](lore/scenario/hrill-the-road-beyond-the-banners-live-preparation.md) *(GM only)*
- [Hrill: Road Beyond the Banners — three-act development](lore/scenario/hrill-road-beyond-the-banners-three-act-development.md) *(GM only)*
- [Hrill: The Long Shore — selected preparation and operations](lore/scenario/hrill-the-long-shore-selected-preparation-and-operations.md) *(GM only)*
- [Hrill: The Long Shore — three-act development](lore/scenario/hrill-the-long-shore-three-act-development.md) *(GM only)*
- [Culvert Patrol complete GM preparation](lore/scenario/culvert-patrol-complete-gm-preparation.md) *(GM only)*

**scenario-preparation**
- [Midnight Exchange: selected campaign and kingdom backdrop](lore/scenario-preparation/midnight-exchange-selected-campaign-and-kingdom-backdrop.md) *(GM only)*
- [The Midnight Exchange — three-adventure arc (GM preparation)](lore/scenario-preparation/the-midnight-exchange-three-adventure-arc-gm-preparation.md) *(GM only)*
- [Midnight Exchange — first customer opening](lore/scenario-preparation/midnight-exchange-first-customer-opening.md) *(GM only)*
- [Hrill exploration proposals and Dragon Kings connections — unselected](lore/scenario-preparation/hrill-exploration-proposals-and-dragon-kings-connections-unselected.md) *(GM only)*
- [Midnight Exchange auction chapter — live preparation](lore/scenario-preparation/midnight-exchange-auction-chapter-live-preparation.md) *(GM only)*
- [The Crown Last Light — selected executable preparation](lore/scenario-preparation/the-crown-last-light-selected-executable-preparation.md) *(GM only)*
- [What She Sold — selected executable preparation](lore/scenario-preparation/what-she-sold-selected-executable-preparation.md) *(GM only)*

**scenario-proposals**
- [Hrill action adventure brainstorm — 27 October 2026](lore/scenario-proposals/hrill-action-adventure-brainstorm-27-october-2026.md) *(GM only)*

## Dramatis personae

**Player characters**
- [Halla](characters/pcs/halla.json) — Male dwarf Fighter; Forge Quarter bodyguard, fixer and hired muscle.
- [Nimras](characters/pcs/nimras.json) — Nimras: human Rank 2 Magic-User, freelance mage hunter trained by an independent fellowship. Left amicably to spread his wings. Review draft; not yet in play.
- [Hrill Helmdance](characters/pcs/hrill-helmdance.json) — Hrill Helmdance, he/him, human knight aged 42, Rank 2; honorable veteran of Crown service seeking purpose beyond fighting.

**NPCs**
- [Conall Bjornlasch](characters/npcs/conall-bjornlasch.json) — Warranted investigator of the King's Assay -- the Crown's arcane inspectorate; twin brother of Randall and secretly a son of Baron Hanzo. A razor-sharp investigator (Insight 88) who is also a capable fighter.
- [Gardwen](characters/npcs/gardwen.json) — Feral-raised elf druid and lone survivor of a Dragon Knight raid; a rank-1 divine caster of nature and pure-water magic who walks with a befriended she-wolf, searching for her long-lost brother.
- [Magda](characters/npcs/magda.json) — Aged barbarian berserker and sworn servant of the death-goddess Hel; Blessed by Hel (she does not age), she guards Gardwen and the lost twins and fights with berserk fury despite her years.
- [Randall](characters/npcs/randall.json) — Street thief of Purewater, raised in a brothel on the Pearl; identical twin of Conall and secretly a son of Baron Hanzo. A nimble, silver-tongued rogue (Deceit 75, Stealth 72, Sleight 71).
- [Abel Weir](characters/npcs/abel-weir.json) — Sergeant of the City Watch, forty-one, twenty-two years in blue-grey. Keeps the referral book at the Isle post -- four inches of complaints against the Baron's people that he has been ordered to record and not act on. He is very tired.
- [Alderic Vantt](characters/npcs/alderic-vantt.json) — Merchant prince and councillor, fifty-two: borderland transit, grain and timber. The Baron's host -- the Dragon Knights are camped on his water-meadow -- and the man who drafted the standing order and put it in front of the Prince.
- [Asphodel](characters/npcs/asphodel.json) — A courtesan at the Promise of Heaven, the house where Randall grew up. Warm, quick, and trusted by him 'as brother and sister' -- his closest confidante on the Pearl Quay and a ready source of information from the working girls.
- [Blau](characters/npcs/blau.json) — Baron Hanzo's albino lieutenant -- known to the ranks as Commander Vask. A thin, red-eyed, burn-scarred killer with unnatural strength who runs the Dragon Knights' day-to-day command and handles the Baron's 'dirty work': a cold, efficient assassin and intimidator.
- [Cailan](characters/npcs/cailan.json) — Gardwen's possessed brother (birth name Gabriel) -- the Baron's tournament champion, host to the ancient dragon-knight spirit Thuban Eta. Dragon-scale armor fused to his skin; eyes flicker reptilian when possessed; fights with uncanny ancient skill and minor fire.
- [Cassian Bree](characters/npcs/cassian-bree.json) — Secretary of the Ember Society, forty-four: courteous, damp-handed, immaculate minutes, boring on purpose. The only confirmed member of the Awake the Dragon Movement in Purewater -- and everything he does is legal.
- [Constantine](characters/npcs/constantine.json) — Proprietor of The Sylph's Embrace on the Pearl -- shrewd, protective of her workers, fiercely independent. Operates under Marisette's authority. After what a di Teufel did to Emmeralda under her roof, she is hiring protection and wants justice.
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
- [Kag](characters/npcs/kag.json) — Half-orc, female, thirties. Rank 2 Thief of Crowbill's guild -- muscle, not a burglar, and the only person in the outfit who can read a ledger. Raised among humans in a Purewater that had no use for her. Seven feet of her, a club she actually reaches for, and a quarter-bound octavo with five years of the Shoals in it that she paid for herself. she/her.
- [Kerrin (brown coat)](characters/npcs/kerrin-brown-coat.json) — One of Crowbill's watchers. Dockside, unremarkable, brown coat. Professional -- follows, does not close.
- [Lilura Deepcurrent](characters/npcs/lilura-deepcurrent.json) — Deputy to High Priestess Nerissa and her right hand in the Order of the Lake Lady -- about thirty, dark, usually wet to the knee because she is the one who actually goes into the channel to check it. Rumoured merfolk ancestry on her mother's side; she holds her breath unnaturally long and does not discuss it. A genuine divine caster in her own right, and the person who decides who reaches the High Priestess and who does not.
- [Marda Blackwater](characters/npcs/marda-blackwater.json) — Broad-shouldered leader of The Dredgers, risen from the dredge-boats during a labor dispute five years ago. A powerful working-class champion (Brawn 75, Oratory 78, Influence 75) who rallies dock labor against the merchant princes and -- above all -- against the Baron's Dragon Knights.
- [Mariarta](characters/npcs/mariarta.json) — An older, canny courtesan of the Promise of Heaven with 'the calm intelligence of someone who can survive almost any situation involving men.' Sent up to entertain the Baron's soldiers, she brings back the hard intelligence on his guarded quarters -- Randall's most valuable inside source on the Dragon Knights' manor.
- [Marisette](characters/npcs/marisette.json) — Madame of The Mother of Pearl and the near-absolute authority over Purewater's Pearl -- the proprietors, Constantine among them, answer to her. A consummate social power broker who keeps the pleasure district running, keeps her accounts in obligations, and resents the disorder the Baron and Santo have brought to it. Her oldest rule: the Pearl sells a night, never a person.
- [Maro Quist](characters/npcs/maro-quist.json) — Councillor, seventy-one, thirty years on the council: incorruptible, formidable, and completely wrong. He voted for both instructions on the merits and will defend them to your face.
- [Murgeroch](characters/npcs/murgeroch.json) — Temerach Nebulo's squire and go-between -- the steady, competent young fighter who carries the knight's messages, screens her meetings, and tends her gear. Usually the first of Temerach's people the party deals with.
- [Nus](characters/npcs/nus.json) — A quick-fingered Purewater street thief and loyal friend of Randall -- lookout, fence, and second pair of hands for a job; nimble, streetwise, and easy to underestimate.
- [Orrin Sculle](characters/npcs/orrin-sculle.json) — The champion's keeper. Ten years feeding, dressing, washing and walking a boy who is not there, and talking to him every night while he does it.
- [Prince Emeric](characters/npcs/prince-emeric.json) — The young Governor of Purewater -- the King's nephew, perhaps two-and-twenty: clever, idealistic, genuinely decent, and entirely unsuited to govern a city like this. He wants to reform Purewater; the factions humor him, manage him, and run rings around his good intentions.
- [Ravella](characters/npcs/ravella.json) — Half-merfolk proprietor of The Siren's Call -- pleasure house and information market in one. Subtle waterfolk tells (webbed fingers, water-reflecting eyes, Swim 90). A master broker (Insight 85, Streetwise 88, Commerce 80) with light innate water magic, secretly protecting the city's hidden waterfolk.
- [Sana](characters/npcs/sana.json) — Nineteen, dark red hair chopped ragged on the left side. High Priestess Nerissa's niece, six weeks at the temple and not yet resigned to it. Clever, not biddable, and a noticer -- she sees the thing nobody else in the room thought was worth looking at, and says so at the wrong moment.
- [Santo di Teufel](characters/npcs/santo-di-teufel.json) — Baron Hanzo's cruel son and heir -- a sadistic young fire-mage who has decided he wants Emmeralda of the Sylph's Embrace, and who carries a stolen ritual knife marked with the sigil of Asmodeus because he cannot imagine being told no.
- [Sinnit](characters/npcs/sinnit.json) — A brutish Lullwater canal-rat and rival thief who has hated Randall for seven years over a purse handed back with a bow -- and who, in the one week Randall's face is worth money, sells what he sees to the men who can hurt him worst.
- [Tat Atarer](characters/npcs/tat-atarer.json) — Captain of the Dragon Knights -- a hardened, pragmatic mercenary commander who serves Baron Hanzo for pay, not ideology. Master fighter (combat 97%); 'the Baron pays for our swords, not our opinions.'
- [Temerach Nebulo](characters/npcs/temerach-nebulo.json) — Elf knight of the Swords of the Lake, called 'the Lakelady's Javelin' -- and the order's spymaster in Purewater, who has spent four years building a quiet network around Baron Hanzo and has not yet made her move. Nobody recruits her. She recruits them.
- [Thorne](characters/npcs/thorne.json) — Elderly storyteller of The Moist Oyster -- frail-seeming but with penetrating blue eyes and a cane that hides a blade. Secretly a former Order of the Lake initiate and Dragon-Knight-raid survivor with peerless historical lore (Dragon Kings era 92) and knowledge of possession-ritual weaknesses.
- [Thuban Eta](characters/npcs/thuban-eta.json) — The ancient dragon-knight spirit bound inside Cailan. A betrayed tactical genius from the Dragon Kings era, held in thrall by Baron Hanzo's ritual through his bones and the binding locket. Indomitable will (Willpower 95), peerless tactics, honors the old codes -- a potential ally if freed.
- [Crowbill's runner](characters/npcs/crowbill-s-runner.json) — Adult male courier working for Crowbill; carries offers and payment terms.
- [Stand-builder at the Lists](characters/npcs/stand-builder-at-the-lists.json) — Adult male carpenter building Tourney stands; Halla freed his boot from shifted timber.
- [Herald house clerk](characters/npcs/herald-house-clerk.json) — Adult woman assisting Tourney herald; works at herald house beside Lists west gate.
- [Rusk](characters/npcs/rusk.json) — Adult human fighter available for controlled practice at Lists; quilted training coat, sword and round shield.
- [Dragon Knight at the inspection cover](characters/npcs/dragon-knight-at-the-inspection-cover.json) — Adult male advance Dragon Knight, eating bread with two comrades on Triumph Bridge, boot on Guild inspection cover.
- [Warehouse intruder](characters/npcs/warehouse-intruder.json) — Adult human man carrying an oilskin bundle in Fishmarket Bridge warehouse, turning toward rear doorway as Halla enters. No visible weapon, no armour.
- [Irena](characters/npcs/irena.json) — Adult human woman entering the Purewater Tourney. Lean, worn travelling coat and practical armour bundled nearby, well-used spear; checking its head binding beside Lists practice sand.
- [Nessa](characters/npcs/nessa.json) — Adult human woman selling and repairing arms at a temporary Tourney stall outside the Lists; rolled sleeves, iron filings caught in leather apron. Ordinary merchant, no hidden plot affiliation.
- [Dagna](characters/npcs/dagna.json) — Dagna, adult dwarf woman and Halla's sister; independent boatwright and repair-yard owner in the Forge Quarter.
- [Perrin Cale](characters/npcs/perrin-cale.json) — Adult human boatman forty, Shoals local, twenty years rowing. Plain short waterside speech, concrete boat concerns; wants retain working skiff and get guild fare delivered.
- [Dragon Knight boat-sergeant](characters/npcs/dragon-knight-boat-sergeant.json) — Sergeant Harl Brenn, the existing Dragon Knight boat-sergeant Halla knocked into the canal at the Watercrafters guild stair. Adult human; clipped orders, led three other soldiers trying to commandeer the hired skiff carrying Torval crew and tools. Name supplied by colleague Drell, no new prior encounter or current whereabouts asserted.
- [Dragon Knight beside the mooring ring](characters/npcs/dragon-knight-beside-the-mooring-ring.json) — Adult human Dragon Knight, square-faced, standing behind boat-sergeant on guild water-stair. He keeps hand on sword hilt while two fellow soldiers reach for fallen sergeant. A short-speaking soldier concerned with retrieving his leader, wary of nearby axes, no appetite for gratuitous public fight. Does not volunteer stories.
- [Merrit](characters/npcs/merrit.json) — Adult human woman running the Copper Oar public eating house on Pie Row. Flour-marked apron, practical short direct speech, concrete prices and work; wants meals served and food deliveries safely unloaded in kitchen courtyard. Hiring ordinary yard guard tonight,1GP for two hours from dusk. No hidden criminal or political affiliation, no known connection to Halla's debt or guild employment.
- [Dragon Knight at the Copper Oar](characters/npcs/dragon-knight-at-the-copper-oar.json) — Adult male human Dragon Knight, one of the pair Halla spotted at Copper Oar door earlier. Now at kitchenyard duskfooddelivery with patrolpartner. Easy entitled tone, short bland commands, calls supplies Baron's provisions and expects his name to obtain them. No personal knowledge of Halla or guildstair incident. Wants food supplies for comrades without payment; this is his unilateral demand, not a lawful proven title.
- [Dena Reed](characters/npcs/dena-reed.json) — Adult human woman in her twenties, local message runner with a worn coat, practical boots and small satchel. Occasionally carries messages for Thorne; no weapons or armour.
- [Dragon Knight provisioning corporal](characters/npcs/dragon-knight-provisioning-corporal.json) — Adult human man in dragon-blazoned mail, narrow beard, dusty gloves. Leads a fresh provisioning detail at the Shoals on d-1 afternoon. No knowledge of Halla or earlier incidents.
- [Dragon Knight provisioning escort woman](characters/npcs/dragon-knight-provisioning-escort-woman.json) — Adult human woman in dragon-blazoned mail, short dark hair and sword-and-shield kit. Fresh Shoals provisioning detail; no Halla knowledge.
- [Dragon Knight provisioning escort man](characters/npcs/dragon-knight-provisioning-escort-man.json) — Adult human man in dragon-blazoned mail, broad nose, sword-and-shield kit. Fresh Shoals provisioning detail; no Halla knowledge.
- [Bera Lowkeel](characters/npcs/bera-lowkeel.json) — Adult human woman in her forties, owner of two small working cargo boats carrying grain and provisions. Coarse grey coat, salt-stiff cuffs, practical boots. A Shoals boat owner whom Marda approaches about paid protective guards.
- [Bera's lead boatman](characters/npcs/bera-s-lead-boatman.json) — Adult human boatman on Bera Lowkeel's leading grain boat. Weathered face, rolled sleeves, working boots. Professional boat-hand responsible for steering and bringing the load alongside.
- [Bera's lead boatman](characters/npcs/bera-s-lead-boatman-2.json) — Adult human boatman on Bera Lowkeel's leading grain boat. Weathered face, rolled sleeves, working boots. Responsible for steering and bringing the load alongside.
- [Household archer at the Long Butts](characters/npcs/household-archer-at-the-long-butts.json) — Adult human professional archer entered in the open Tourney archery; household retainer in plain shooting harness.
- [Pell Nettles](characters/npcs/pell-nettles.json) — Adult Purewater crowd thief who works festivals, ferry queues and tournament grounds.
- [Joss Fen](characters/npcs/joss-fen.json) — Adult Purewater crowd thief who works tournament gatherings with Pell Nettles.
- [Garran Holt](characters/npcs/garran-holt.json) — Unused setup record: default avian species was incorrect. Never introduced in play; superseded by humanoid Garran Holt.
- [Garran Holt](characters/npcs/garran-holt-2.json) — Adult human touring swordsman entering Single Combat; sturdy mail and helm, longsword and round shield. Minor entrant, champion's first opponent, experienced with no main-plot ties.
- [Veya Dorn](characters/npcs/veya-dorn.json) — Human tournament entrant, cropped grey hair, square build, riveted armour, mace and round shield. Surviving entrant on the other side of the single-combat draw; next opponent after Halla defeats Cailan.
- [Tournament healer](characters/npcs/tournament-healer.json) — Duty healer at the Lists. First Aid70 and Healing75 match previously assigned tournament medical staff ratings. Treats Halla after his fourth bout; professional care, no fee established.
- [Captain Elian Ward](characters/npcs/captain-elian-ward.json) — Adult human man, forties; captain of Prince Emeric's household guard. Close-cropped greying hair, plain mail, lake-green service sash. Soldier responsible for the Prince's household, distinct from Hesper and the City Watch.
- [Sergeant Jory Vale](characters/npcs/sergeant-jory-vale.json) — Adult human woman, thirties; Dragon Knight rear-party sergeant supervising packing at Vantt's waterside landing after Hanzo's departure. Plain mail, rolled blanket over shoulder, cropped dark hair. Not the provisioning corporal or Vask.
- [Teren Hale](characters/npcs/teren-hale.json) — Adult human man in his twenties, Dredgers' guild runner working between the Vantt landing and Purewater during camp clearance. Plain working clothes, white-wave guild armband. Introduced when Marda calls for a messenger, not a soldier or a child.
- [Emmit Rill](characters/npcs/emmit-rill.json) — Adult human dockhand and small-skiff owner, previously reported by Thorne as off work after a Dragon Knight beating. Currently recovering at the Dredgers' Hall. Owner of the nearer skiff with an iron stern-brace; Marda recognises his boat from local work.
- [High Isle Watch duty officer](characters/npcs/high-isle-watch-duty-officer.json) — Adult human duty officer at High Isle Watch post. Ink on right cuff, worn uniform, direct ordinary questions. Has been indoors on receiving duty, not a spectator at final.
- [Jessa Fen](characters/npcs/jessa-fen.json) — Adult human woman, household guard, short dark braid and weathered service cloak. Practical and sociable, likes discussing canal-side work; off duty supper at Copper Oar. No knowledge of Halla private debts or past scandal.
- [Orren Pike](characters/npcs/orren-pike.json) — Adult human man, older household guard, close-trimmed beard and patched cloak. Dry ordinary humour, prefers practical company and food after watch. No knowledge of Halla private dealings.
- [Vantt mill landing watchman](characters/npcs/vantt-mill-landing-watchman.json) — Adult human man in a patched mail shirt holding a hooded lantern. Vantt's paid mill watchman; wants unauthorised boats kept outside the loading channel, will not knowingly attack identified Crown guards over a shipment.
- [Sergeant Drell](characters/npcs/sergeant-drell.json) — Adult human man, square beard with grey through it, mail shirt and an unfastened sword belt. Sergeant named by captured frame-planter as ordering silver planted against Halla's sister; higher command responsibility remains unproved. Currently assigned to mill escort under Vask.
- [Nella Venn](characters/npcs/nella-venn.json) — Adult human flour supplier with chalk-white cuffs, operating a small flour shed at the Shoals water-stair. One of the two other provision-boat owners whose loads Drell brought to Vantt mill, alongside Bera Lowkeel's grain.
- [Davin Kett](characters/npcs/davin-kett.json) — Adult human bean and dry-provision seller with a patched sackcloth apron, keeping a store beside Nella Venn's flour shed at the Shoals water-stair. One of the other provision-boat owners recorded in Drell's collection book.
- [DragonBarge gangplank sentry](characters/npcs/dragonbarge-gangplank-sentry.json) — Adult human household sentry at DragonBarge gangplank, helmet cheekguards open and spear held upright. Household defence under Vask, not a new member added beyond six Dragon Circle aboard.
- [Ward escort, bow guard](characters/npcs/ward-escort-bow-guard.json) — Adult household guard with a stitched repair across a green sash. One of the six household guards assigned to Ward's authorised Vask escort, not an additional reinforcement.
- [Ward escort, stern guard](characters/npcs/ward-escort-stern-guard.json) — Adult household guard with close-shorn hair and a hooded lantern. One of the six household guards assigned to Ward's authorised Vask escort, not an additional reinforcement.
- [Ward escort, port oarsman](characters/npcs/ward-escort-port-oarsman.json) — Adult household guard with a leather palm guard for rowing. One of the six household guards assigned to Ward's authorised Vask escort, not an additional reinforcement.
- [Ward escort, starboard oarsman](characters/npcs/ward-escort-starboard-oarsman.json) — Adult household guard with a square-cut cloak pinned clear of the oar. One of the six household guards assigned to Ward's authorised Vask escort, not an additional reinforcement.
- [Sella Marr](characters/npcs/sella-marr.json) — Adult human freight broker. Direct offers, impatient interruptions. Wants exclusive waterfront carriage; 120GP remaining reserve, two lighters, launch, six employees and Oth's company. Will bargain to preserve solvency. No royal authority or secret PC knowledge.
- [Captain Oth Bren](characters/npcs/captain-oth-bren.json) — Adult human mercenary captain. Terse orders. Seeks permanent toll command; eight soldiers besides himself, never simultaneously in two places. Four veterans65 and four recruits45. Prefers survival to dying for Sella's debts. No mastery, magic or Luck.
- [Neri Pell](characters/npcs/neri-pell.json) — Adult human boat organiser. Blunt practical questions and quick laughter. Protects six independent crews; two boats, twelve workers, local routes and market trust. Opposes either criminal monopoly; not automatically loyal to Halla.
- [Edra Venn](characters/npcs/edra-venn.json) — Adult human lighter master of Reedwife, blue headscarf and missing left little finger. Independent carrier carrying six bales of dyed wool for Crowbill with a disputed Marr delivery agreement. No kinship with other Venn names established. Wants crew safe and agreed freight paid.
- [Oren Vey](characters/npcs/oren-vey.json) — Established independent master of divination, illusion and old texts, resident at the House of Small Windows on High Isle. Private library and patronage support a pursuit of a vanished magician’s dispersed library. Has limited professional exchanges with Hesper; does not know Hesper’s private allegiance. No Crown office.
- [Rennic Vaur](characters/npcs/rennic-vaur.json) — Nimras’s former teacher and experienced mage hunter. Retained an entrusted binding manuscript beyond its loan to help disable a living-caster hunt. Affectionate, practical, independent. Selected Glass Hounds setup supersedes the rejected survey purpose.
- [Hedda Rook](characters/npcs/hedda-rook.json) — Adult fitter, one of Sella Marr’s existing six civilian employees. Measuring proposed gate fittings, not installing or guarding a gate. Broad-shouldered, wool work jacket, chalk on her cuffs. No knowledge of Nimras or Vaur’s commission.
- [Tovin Beck](characters/npcs/tovin-beck.json) — Adult assistant, one of Sella Marr’s existing six civilian employees. Carries tools and holds measuring ends. Work shirt and canvas apron. No knowledge of the mages or manuscript.
- [Sivren Kest](characters/npcs/sivren-kest.json) — Independent arcane artificer; apprentice of no newly invented city institution. Clipped technical speech, stained hands, battered spectacles. Full selected plan in Glass Hounds GM lore.
- [Captain Mara Senn](characters/npcs/captain-mara-senn.json) — Independent recovery captain. Cropped hair, well-cut patched coat, short offers and dockside humour. Commands exactly five other company members; no institutional immunity.
- [Doria Flint](characters/npcs/doria-flint.json) — Adult master glassblower of Furnace Court; no spellcasting. Burn mark at wrist; blunt and warm. Gives useful evidence freely when danger is clear.
- [Neral Brinehand](characters/npcs/neral-brinehand.json) — Independent merfolk pilot; no Council mandate, no spell repertoire granted. Dark green tail; direct questions. Prior working introduction to Thessa; cannot speak for her.
- [Iven Toll](characters/npcs/iven-toll.json) — Local hired blade and hound handler in Senn’s six-person company. Assigned room search with Bess; knows only orders and reports he receives.
- [Bess Arl](characters/npcs/bess-arl.json) — Local burglar and intimidation specialist in Senn’s six-person company. Assigned room search with Iven. Wages and survival, not fanatic allegiance.
- [Pell Dask](characters/npcs/pell-dask.json) — Paid recovery company member; short practical speech, wants wages and survival. Will retreat or surrender when defeated; no fanatic allegiance.
- [Jory Fen](characters/npcs/jory-fen.json) — Paid recovery company member; short practical speech, wants wages and survival. Will retreat or surrender when defeated; no fanatic allegiance.
- [Nel Aster](characters/npcs/nel-aster.json) — Paid recovery company member; short practical speech, wants wages and survival. Will retreat or surrender when defeated; no fanatic allegiance.
- [Elna Pike](characters/npcs/elna-pike.json) — Adult keeper of Three Steps Rooms; plain-spoken, commercially shrewd, wants safe guests and a solvent lodging. Does not hide useful leads behind riddles.
- [Leth Varro](characters/npcs/leth-varro.json) — Itinerant private recovery broker. Polished patient speech, treats coercive work as a purchase. No Crown warrant, personal guards or secret command over Purewater masters.
- [Beren Holt](characters/npcs/beren-holt.json) — Noncasting resident correspondent of the King’s Assay; former instrument-maker. Receives packets, arranges witnesses, preserves copies. No warrant, punch or licensing authority. Rolled sleeves and square working hands; speaks readily about people, reluctantly about interpretations.
- [Nessa Rill](characters/npcs/nessa-rill.json) — Recover her own tool-case and resume appraising
- [Tobin Marr](characters/npcs/tobin-marr.json) — Return misdelivered property and maintain his forwarding business
- [Avel Sorn](characters/npcs/avel-sorn.json) — She/her; custodian of the fellowship shared manuscripts, authorised to receive returned loans and settle recovery fees.
- [Maelin Voss](characters/npcs/maelin-voss.json) — Wants Hrill to help people coordinate; owes Len safe practical help; will take sheep-track rather than sacrifice him for the load.
- [Len Rook](characters/npcs/len-rook.json) — Wants his property safe; owes delivery but will abandon cart to save himself.
- [Mother Anwen](characters/npcs/mother-anwen.json) — Wants immediate stores; owes all guests welcome. Can close and disperse supplies rather than admit a garrison.
- [Serevan Ashleaf](characters/npcs/serevan-ashleaf.json) — Wants restitution but owes living pupils safety. Can leave, trade information or demand an actual protective plan.
- [Sir Aldren Vaust](characters/npcs/sir-aldren-vaust.json) — Wants personal permanence; owes lawful road protection. Aid is real, coercion is chosen. Bargains or surrenders when survival requires it.
- [Sergeant Cessa Dorn](characters/npcs/sergeant-cessa-dorn.json) — Wants a quiet contract; owes obedience. Accepts lawful restraint or paid withdrawal when credible, not by automatic defection.
- [Harl Teven](characters/npcs/harl-teven.json) — Knows own assignment; no automatic knowledge of relic identity or commander secrets.
- [Oda Vennick](characters/npcs/oda-vennick.json) — Knows own assignment; no automatic knowledge of relic identity or commander secrets.
- [Merrit Caul](characters/npcs/merrit-caul.json) — Knows own assignment; no automatic knowledge of relic identity or commander secrets.
- [Fenn Ash](characters/npcs/fenn-ash.json) — Knows own assignment; no automatic knowledge of relic identity or commander secrets.
- [Joss Veller](characters/npcs/joss-veller.json) — Knows own assignment; no automatic knowledge of relic identity or commander secrets.
- [Ina Kett](characters/npcs/ina-kett.json) — Knows own assignment; no automatic knowledge of relic identity or commander secrets.
- [Mistress Ysabet Rill](characters/npcs/mistress-ysabet-rill.json) — She/her. Independent established master specialising in alteration and protection; practical commissions fund research into preservation, form and decay. No kinship to Nessa Rill implied.
- [Lady Ilyra Voss](characters/npcs/lady-ilyra-voss.json) — She/her. Established independent master of binding and bargaining; wealthy High Isle household, estates and civic connections. No relationship to Maelin Voss inferred.
- [Caldris](characters/npcs/caldris.json) — He/him. Established independent master, scholar of passage and distance; shipping and salvage partnerships fund expeditions. Exact lost-place project remains private, not active travel capability.
- [Edda Vale](characters/npcs/edda-vale.json) — she/her. Knows Maelin professionally and reports of unsafe landings; has not seen reedback, secret inner channels, Garr plan, Hrill history or other PCs.
- [Perrin Moss](characters/npcs/perrin-moss.json) — he/him. Knows old chart and local depths, not uncharted northern channels or magical answers.
- [Ressa Dain](characters/npcs/ressa-dain.json) — she/her. Knows lake shelters and sailing, recent storm; no northern enclave secret or hunter plan.
- [Tovin Reed](characters/npcs/tovin-reed.json) — they/them. Knows cargo and own duties, dock gossip only; no hidden loyalties.
- [Nera Quill](characters/npcs/nera-quill.json) — she/her. Has seen animal grazing and hunter questions, knows broken landing; uncertain whether fish are displaced permanently. No imperial secrets.
- [Garr Hew](characters/npcs/garr-hew.json) — he/him. Hunter at White Shingle; knows his own crew, buyer estimate and25morningreedbackfeedinglocation. Recognises Hrill as visitor who refused hunt; does not know his name/backstory or Selith’s identity yet, or safe enclave channel.
- [Berrin Holt](characters/npcs/berrin-holt.json) — they/them. Knows announced hunt and wages, not inner channel or broader history.
- [Ula Marrick](characters/npcs/ula-marrick.json) — she/her. Knows lines/harpoons and Garr announced hunt. No enclave route.
- [Dorr Marrick](characters/npcs/dorr-marrick.json) — he/him. Knows own hunt duties and sister Ula, not all Garr intentions.
- [Ilyen](characters/npcs/ilyen.json) — they/them. Knows seasonal animal route, own scouts/enclave and Selith records existence; not all records, Hrill mind or current imperial plots.
- [Leth Aren](characters/npcs/leth-aren.json) — she/her. Knows local patrol paths and Ilyen orders only, not Selith records.
- [Siv Orr](characters/npcs/siv-orr.json) — he/him. Knows patrol route and orders, not hidden regional politics.
- [Selith An](characters/npcs/selith-an.json) — she/her. Knows historical imperial shore names, resistance/refuge channels and own community; no other PCs or current restorationist operations.
- [Adra Tern](characters/npcs/adra-tern.json) — She/her. Ordinary secondhand-clothes stallholder in Lullwater beside the bookbinder display; no prior acquaintance with Nimras or affiliation to a patron.
- [Pell Sedge](characters/npcs/pell-sedge.json) — He/him. Independent Lullwater skiffman; carries passengers and small cargo between the islands. Ordinary local acquaintance, not a retainer.
- [Orsa Bell](characters/npcs/orsa-bell.json) — She/her. Lullwater dealer in salvage, secondhand locks and reused household iron; an ordinary acquaintance from the Oyster.
- [Seressa Venn](characters/npcs/seressa-venn.json) — she/her. Auction proprietor, independently owns the consignment and controls her staff.
- [Olt Marek](characters/npcs/olt-marek.json) — he/him. Independent antiquities buyer acting for a dispossessed claimant.
- [Severin Rusk](characters/npcs/severin-rusk.json) — he/him. Former estate factor pursuing his own derivative binding venture; no current office over Purewater.
- [Mina Krail](characters/npcs/mina-krail.json) — she/her. Rusk purchasing agent and tracker; carries30GP shared purchase fund and signed order.
- [Davren Vetch](characters/npcs/davren-vetch.json) — he/him. Rusk second purchasing/recovery agent, knows the sketch and return route.
- [Istra Den](characters/npcs/istra-den.json) — she/her. Velvet Hold captain; protects vessel and ordinary crew.
- [Nedo Harrow](characters/npcs/nedo-harrow.json) — he/him. Ordinary Velvet Hold sailor.
- [Fenn Rook](characters/npcs/fenn-rook.json) — they/them. Ordinary Velvet Hold sailor.
- [Rovan Hest](characters/npcs/rovan-hest.json) — he/him. Paid Velvet Hold guard; one of four total.
- [Mila Quern](characters/npcs/mila-quern.json) — she/her. Paid Velvet Hold guard; one of four total.
- [Derrit Sahl](characters/npcs/derrit-sahl.json) — he/him. Paid Velvet Hold guard; one of four total.
- [Hobb Marrin](characters/npcs/hobb-marrin.json) — he/him. Paid Velvet Hold guard; one of four total.
- [Balin Tuck](characters/npcs/balin-tuck.json) — he/him. Marek escort; one of two total.
- [Kessa Rane](characters/npcs/kessa-rane.json) — she/her. Marek escort; one of two total.
- [Rusk depot retainer 1](characters/npcs/rusk-depot-retainer-1.json) — they/them. One of four retainers staying at Ashwick; no simultaneous deployment.
- [Rusk depot retainer 2](characters/npcs/rusk-depot-retainer-2.json) — they/them. One of four retainers staying at Ashwick; no simultaneous deployment.
- [Rusk depot retainer 3](characters/npcs/rusk-depot-retainer-3.json) — they/them. One of four retainers staying at Ashwick; no simultaneous deployment.
- [Rusk depot retainer 4](characters/npcs/rusk-depot-retainer-4.json) — they/them. One of four retainers staying at Ashwick; no simultaneous deployment.
- [Dame Avel Veyr](characters/npcs/dame-avel-veyr.json) — she. Blunt soldier, convivial off duty. Wants an imperial foothold and permanent command; owes followers survival and promised wages. Knows own plan, not Hrill or cistern. Attempts capture, accepts lawful custody if defeated.
- [Captain Surn Pike](characters/npcs/captain-surn-pike.json) — he. Familiar sailor idiom. Wants unpaid12GP and sound boat; owes crew pay. Knows own contract and visible pursuit, not garrison interior. Withdraws rather than lose boat or fight entire village.
- [Corporal Dera Venn](characters/npcs/corporal-dera-venn.json) — she. Short practical directions and ordinary humor. Wants keepers and Crown post safe; owes soldiers sensible orders. Knows cistern and visible besiegers, not contract. Welcomes help, can evacuate instead of last stand.
- [Halwen Tarr](characters/npcs/halwen-tarr.json) — she. Plain, ordinarily gossipy keeper. Wants shelter and adult sibling Bess safe. Knows pursued route, demand and cistern maintenance; no political secret or enemy roster. Seeks refuge, guides only by consent.
- [Bess Tarr](characters/npcs/bess-tarr.json) — they. Dry working speech. Wants household freedom and tower maintained. Knows cistern/fuel, not enemy contracts. Braces door, helps evacuate; no fighting specialist.
- [Arlo Fen](characters/npcs/arlo-fen.json) — he. Laconic sailor; wants wages and no drowning. Knows pursuit task only. Bow available in boat with Pike, no shot ordered. Yields if isolated.
- [Mar Lusk](characters/npcs/mar-lusk.json) — she. Brusque, mocks hesitation; wants Pike respect and pay. Knows custody task only, underestimates lone older knight. Drawn sword approaching house; bow slung. Backs down when outmatched.
- [Toll Reed](characters/npcs/toll-reed.json) — he. Repeats captain wording; wants berth and passage home. Knows custody task only. Cudgel ready beside Mar, no attack made. Surrenders at serious threat.
- [Enna Rusk](characters/npcs/enna-rusk.json) — she. Quiet precise crossbow hand; wants contracted pay and comrades alive. Knows employer imperial aspiration, not Hanzo or unrelated people sharing surname. Covers quay after actual deployment.
- [Corl Hen](characters/npcs/corl-hen.json) — he. Talkative cook and spearman; wants home money and regular meals. Knows own employer and task only; guards track, yields if cut off.
- [Venn Tal](characters/npcs/venn-tal.json) — they. Gruff spear carrier; wants unit intact, dislikes wasted lives. Knows own employer and task only; holds yard, retreats under half strength.
- [Essa Gant](characters/npcs/essa-gant.json) — she. Young, direct spear carrier; wants wages, owes comrades cover. Knows own employer and task only; carries ladder, yields at credible defeat.
- [Jerr Low](characters/npcs/jerr-low.json) — he. Genial spearman off duty; wants recognized military work, fears captivity. Knows own employer and task only; carries ladder, will accept clear safe surrender.
- [Noll Beck](characters/npcs/noll-beck.json) — he. Cautious guard; wants civilians safe and corporal supported. Knows tower and demands only. Holds door with spear and shield; evacuation acceptable.
- [Vela Sorn](characters/npcs/vela-sorn.json) — she. Outspoken guard; wants keepers free and Crown flag flying. Knows tower and demands only. Crossbow at shutter, obeys sensible withdrawal.
- [Reeve Elric Marden](characters/npcs/reeve-elric-marden.json) — Hythe harbour reeve; a broad, grey-haired man in a salt-marked blue coat with a Crown badge.
- [Sergeant Brann Tarrow](characters/npcs/sergeant-brann-tarrow.json) — Broad scarred chin, worn watch coat, short iron-grey hair.
- [Orrin Fell](characters/npcs/orrin-fell.json) — Long thin face, broad hands, repaired crossbow stock.
- [Benno Reed](characters/npcs/benno-reed.json) — Young freckled man, cropped black hair, carefully maintained spear.
- [Joric Vane](characters/npcs/joric-vane.json) — Red beard cut square, patched brigandine, no badge or livery.
- [Dain Sedge](characters/npcs/dain-sedge.json) — Dark cropped beard, leather cap, missing coat buttons.
- [Moss Pell](characters/npcs/moss-pell.json) — Narrow shoulders, yellow scarf, leather jerkin.
- [Kell Rook](characters/npcs/kell-rook.json) — Heavy eyebrows, broad neck, torn green sleeves.
- [Pella Wren](characters/npcs/pella-wren.json) — Weathered woman with wool apron, greying braid and thick leather gloves.
- [Elen Veyr](characters/npcs/elen-veyr.json) — she. Grey braid, flour on cuffs. Warm blunt questions; wants family informed and home left alone. Will not excuse Avel attacking keepers. Knows60GPsale and buyer, notarrest/cache. WIll answer willingly andshowcounterfoil oncepurposeexplained.
- [Tavin Veyr](characters/npcs/tavin-veyr.json) — he. Broad palms, patched coat. Plain agricultural comparisons; wants farmsolvent andfamilypropertyrespected. Knowscounterfoil andsurfacequarrypath, notcache/politics. Will guideifhomesafe; fleesoverwhelmingforce,yieldhonestly.
- [Merrit Dane](characters/npcs/merrit-dane.json) — he. Neat beard and inkstained fingertips. Affable preciseprices,curtwhenthwarted. Wantscacheforrestorationbuyersandprofit;paidhisown60GPforAvelgoods,nocommandofher. Knowssurveyandsale,nothingofHrillorGreywatchcapture. Warning/bargainthenfiniteforce; abandonsifguardlostandnoexit,surrendersseriouswound.
- [Kett Orr](characters/npcs/kett-orr.json) — he. Weathered red scarf. Terse practicalguard; wantswagesandbreathing,notideology. Knowscart/protectioncontract. Coversretreat,declinesmurderofnonresistingwitness,yieldsisolated.
- [Willa Ash](characters/npcs/willa-ash.json) — she. Cropped hair, stitched quiver. Dry terse talk; wantslivingwages. KnowsDaneexpectsweapons,nobuyeridentity. Warnsnonhostileapproach,takescover,usesactualreload,withdrawswhen cutoff,yieldscredibledefeat.
- [Sergeant Lysa Bell](characters/npcs/sergeant-lysa-bell.json) — she. Dark cropped hair, creased watchcoat. Direct ordinaryspeech. Wants safe roadsandCrownstoressecure;owesdistrictguardcoverage. Knowslocalroads,notAvel/privateevents. Takesactualevidence,allowshelp; can bringJoandIvowithpreparationandactualjourney,neverinstant.
- [Jo Ren](characters/npcs/jo-ren.json) — they. Stocky watchman with worn spearshaft. Brief friendlyspeech; wants fellowwatchsafe. Knowsdistrictroadsnotprivateconspiracy. ObeysLysaslegitimateorders,usesterrain,acceptssurrender.
- [Ivo Gell](characters/npcs/ivo-gell.json) — he. Freckled youngadult with neatlypatchedcoat. Straightforwardwatchspeech; wants reliablework. Knowspatrolroadsnotprivateevents. ObeysLysa,useactualcover,yieldsifoverwhelmed.
- [Brenna Tull](characters/npcs/brenna-tull.json) — Broad woman with rolled sleeves and a linen apron. Brisk ordinary speech; wants guests fed, beds paid for and peace in commonroom. Knows local craftspeople and personally recommends Vara’s sound work, no privateknowledgeofAvel/quarry. Answersdirectionsplainly;doesnotdemandanorderfirst.
- [Vara Flint](characters/npcs/vara-flint.json) — Grey hair cropped close, broad forearms and leather apron. Patient direct craftspeech; wants soundsteel and fairpayment, owes customers honestassessment. Knownlocallyforordinarywellmadeswords. Asks intendedusebeforecommission,won’tpromiseinstantcraftorautomaticmagic. No privateAvel/quarryknowledge.
- [Rellan Voss](characters/npcs/rellan-voss.json) — Spare middle-aged man, curledwoodshavingsonapronandthreadwaxonfingers. Quietmatteroffactspeech,patientcraftquestions. Wants honestordersandsoundgear,owescustomersaccurateadvice. Knowslocalbowpracticeandhisownstock,notAvel/Daneprivateplans. No pressuretopurchase;doesnotleavebusinesstoactasfreeguard.
- [Bera Holt](characters/npcs/bera-holt.json) — Bera Holt, she,51. Ashwick carpenter, square hands and a grey work braid. Plain practical speech. Wants fair pay and sound work; refuses unsupported stonework and needless risk. Knows only Dane has a cracked landing support in an old quarry store. Does not know Avel, Dragon politics, Hrill identity or military ownership claims. Will inspect with lantern and actual tools, devise shoring using real materials via Craft(Carpentry)75, uncertain damaged masonry Engineering55; never automatic repair. Fee2GP for day41 plus meals,1GP deposit received40day255,1GP balance after work. Departs Ashwick41dawn0 with own hand tools, reaches quarry41dawn180 after actual3hwalk. No guards, combat mission, magical repair or teleport.

**Creatures**
- [Ruhi](characters/creatures/ruhi.json) — Gardwen's befriended companion -- a loyal she-wolf; swift, keen-nosed and savage in the bite.
- [Glass Hound 1](characters/creatures/glass-hound-1.json) — Physical animated glass hunting construct. Exact scenario rules in Glass Hounds GM lore. No spell immunity or electricity resistance. Removable tracking throat. No free attacks or pounce.
- [Glass Hound 2](characters/creatures/glass-hound-2.json) — Physical animated glass hunting construct. Exact scenario rules in Glass Hounds GM lore. No spell immunity or electricity resistance. Removable tracking throat. No free attacks or pounce.
- [Glass Hound 3](characters/creatures/glass-hound-3.json) — Physical animated glass hunting construct. Exact scenario rules in Glass Hounds GM lore. No spell immunity or electricity resistance. Removable tracking throat. No free attacks or pounce.
- [Glass Hound 4](characters/creatures/glass-hound-4.json) — Physical animated glass hunting construct. Exact scenario rules in Glass Hounds GM lore. No spell immunity or electricity resistance. Removable tracking throat. No free attacks or pounce.
- [Reedback of the northern shallows](characters/creatures/reedback-of-the-northern-shallows.json) — Single migratory herbivore; custom aquatic anatomy. No Luck, spells, intelligence in Common, prophecy or imperative to fight. Grazes and retreats.

## Factions

- [Crowbill's Underworld](factions/crowbill-s-underworld.md) — Purewater's criminal underground -- canal smuggling, gambling, protection -- run to a code by the unremarkable crime lord Crowbill. Signaled by crow marks. The occupation is wrecking the equilibrium his business depends on.
- [The Awake the Dragon Movement](factions/the-awake-the-dragon-movement.md) — A shadowy movement to revive the ancient draconic order and transform men into Dragon Kings. Baron Hanzo's true cause; an existential threat to water magic.
- [The City Watch](factions/the-city-watch.md) — Purewater's ordinary police: about ninety men and women in blue-grey, competent at drunks, thieves and canal disputes -- and under standing orders not to provoke the Baron's people until the Tourney is over.
- [The Currents](factions/the-currents.md) — A leaderless network of spies and informants trading in secrets, not contraband. Marked by chalk water-signs; the hidden 'Source' directs it.
- [The Dragon Knights](factions/the-dragon-knights.md) — Baron Hanzo's 20-30 sworn warriors -- brutal mercenaries in dragon heraldry, enhanced with fire demonology. In Purewater for the Tourney and behaving like an army of occupation, because they have been told the watch will not touch them.
- [The Dredgers](factions/the-dredgers.md) — Labor guild and mutual-aid society of Purewater's working poor -- canal-clearers, dockers, fishers. Black armbands, white wave. Led by Marda Blackwater, and three hundred strong in a week when the Baron's men are taking their boats.
- [The Harbor Masters](factions/the-harbor-masters.md) — The regulatory guild of Purewater's docks and shipping -- tariffs, berths, maritime law. Dark blue uniforms, a harbor tower HQ, a publicly incorruptible Harbormaster, and increasingly corrupt upper ranks. They berthed the DragonBarge.
- [The King's Assay](factions/the-king-s-assay.md) — The Crown's chartered body for licensing, inspecting and recording arcane practice in Thornmere -- founded after the uprising to put magic on a register. Warrants, hallmarks, and a personal steel punch. Conall is one of theirs.
- [The Mermaid's Court](factions/the-mermaid-s-court.md) — A secretive society of pure-water practitioners bound to merfolk, preserving water magic older than the city. Hidden under Lost Isle; led by the enigmatic 'Pearl'.
- [The Order of the Lake Lady](factions/the-order-of-the-lake-lady.md) — The water-faith of Purewater: priesthood of the lake goddess, guardians of pure water magic, and owners of the Tourney. Robed in blue-green with silver wave patterns. Their fouling alarm has been silenced by written instruction.
- [The Pleasure Houses of the Pearl](factions/the-pleasure-houses-of-the-pearl.md) — The courtesan network of the Pearl, under the madame Marisette's near-absolute authority. Constantine's Sylph's Embrace and Ravella's Siren's Call among them. The richest information market in Purewater, and the campaign's front door.
- [The Quiet Hand](factions/the-quiet-hand.md) — A secret, centuries-old fellowship that steers the world toward the good from the shadows -- by knowing first and acting unseen. Espionage as mercy. Hesper is their agent in Purewater. (GM: a benevolent hidden patron.)
- [The Swords of the Lake](factions/the-swords-of-the-lake.md) — An austere knightly order sworn to the Lake Lady and the protection of the realm's water magic. Temerach Nebulo is their most famous blade -- and the only armed authority in Purewater that does not answer to the Governor's council.
- [The Watercrafters Guild](factions/the-watercrafters-guild.md) — Boat-builders, canal engineers, water-diviners and makers of water-enhanced goods -- the artisans whose enchantments keep the canal-city working. Indigo sashes. One of their Tide Masters signed the Baron's corruption off as a false reading.
- [Nimras’s independent fellowship](factions/nimras-s-independent-fellowship.md) — The independent fellowship that trained Nimras; his former home and current client. Formal name remains unchosen.
- [Nimras former independent fellowship](factions/nimras-former-independent-fellowship.md) — The unnamed independent magical fellowship that trained Nimras, from which he left amicably. Current client for live recovery of Rennic Vaur and return of its entrusted manuscript; agreed fee8GP. Proper name remains unchosen.
- [Vaust road company](factions/vaust-road-company.md)
- [Three Hearths road households](factions/three-hearths-road-households.md)
- [Grey Heron supply crew](factions/grey-heron-supply-crew.md)
- [Garr Hew hunting crew](factions/garr-hew-hunting-crew.md)
- [Listening Reeds shore households](factions/listening-reeds-shore-households.md)
- [Velvet Hold auction business](factions/velvet-hold-auction-business.md) — Independent Venn auction staff; fourguards,captain,two ordinarycrew. No allegiance to Rusk.
- [Rusk recovery venture](factions/rusk-recovery-venture.md) — Finite derivative estate venture: Rusk,sixretainers total,80GP originally; two agents carry30GP,remaining50GP and fourretainers at Ashwick. No replacement army.
- [Marek claimant purchase party](factions/marek-claimant-purchase-party.md) — Marek and twoescorts,20GP real purchase funds; independent of Venn and Rusk.

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
