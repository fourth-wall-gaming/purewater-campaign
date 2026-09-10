# And Then the Dragons Came: Purewater

> **Current playthrough:** session 1 as **Conall Bjornlasch**, database campaign
> `myth-campaign-cdd876ebe965`. The package at the repository root is the
> pristine seed state — world clock `d-3/dawn`, 12 agendas on their starting
> clocks, 17 facts none of them yet true.
>
> The previous playthrough (as **Magda**, complete) is archived in
> `archive/session-01-magda/`, at the git tag `session-01-magda`, and left live
> in the database as `myth-campaign-8327f8687a98` — *"ARCHIVE — Purewater S1
> (Magda, complete)"*. Its transcripts are in `session-logs/` and its two
> novelizations in `novels/`.

A Classic Fantasy Imperative port of 'And then the Dragons Came', relocated to Purewater -- a Venice-like canal city where the sacred waters of the Lake Lady meet the sea. Baron Hanzo di Teufel arrives with his Dragon Knights for the Lake Lady's Tourney, his possessed champion concealed among them. Four strangers arrive the same week. Built as a living world: every NPC and faction runs its own agenda on a clock, and what the party does not witness happens anyway.

A **Mythras Imperative** campaign in the
[mythras-gm](https://github.com/fourth-wall-gaming/mythras-gm) publishable
campaign format (v1.1).

| Contents | Count |
|---|---|
| Lore entries | 16 |
| Characters | 35 (PCs: Conall Bjornlasch, Gardwen, Magda, Randall) |
| Creature templates | 4 |
| Locations | 18 |
| Factions | 14 |
| Encounters | 0 |
| Journal events | 2 |
| Agendas | 14 |
| Beats | 21 |
| Facts | 17 |
| Knowledge edges | 13 |

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

The canonical full-prose worldbook sources live in [`setting/`](setting/) — see its README for the book list and audience guide. The `lore/` files below are the same material sliced into database-ready entries.

## The living world (agendas)

What the world is doing while the PCs are elsewhere. Each agenda is a goal held
by a character or faction, tracked on a clock; the `beats/` directory holds the
concrete things those goals produce, scheduled against the world clock. Run
`tick` between scenes to find out what has come due.

- [A di Teufel who is not his](agendas/a-di-teufel-who-is-not-his.md) -- *Hanzo di Teufel* (0/6)
- [Clean up after the young master](agendas/clean-up-after-the-young-master.md) -- *Blau* (0/6)
- [Field the champion and take the city](agendas/field-the-champion-and-take-the-city.md) -- *Hanzo di Teufel* (2/8)
- [Find who carved Emmeralda](agendas/find-who-carved-emmeralda.md) -- *Marisette* (0/6)
- [Get paid, keep the company whole](agendas/get-paid-keep-the-company-whole.md) -- *Tat Atarer* (0/4)
- [Have her](agendas/have-her.md) -- *Santo di Teufel* (0/6)
- [Hold the streets as if we own them](agendas/hold-the-streets-as-if-we-own-them.md) -- *The Dragon Knights* (2/6)
- [Keep the Lady's water clean](agendas/keep-the-lady-s-water-clean.md) -- *High Priestess Nerissa* (0/6)
- [Keep the champion unseen](agendas/keep-the-champion-unseen.md) -- *Hanzo di Teufel* (1/4)
- [Keep the table level](agendas/keep-the-table-level.md) -- *Crowbill* (0/6)
- [Make them pay for one of ours](agendas/make-them-pay-for-one-of-ours.md) -- *Marda Blackwater* (1/4)
- [One big score, and a name](agendas/one-big-score-and-a-name.md) -- *Nus* (0/4)
- [Shield the boy, unmask the house](agendas/shield-the-boy-unmask-the-house.md) -- *Temerach Nebulo* (1/6)
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

**gm-secret**
- [GM Secrets: The Possession Scheme](lore/gm-secret/gm-secrets-the-possession-scheme.md) *(GM only)*

**history**
- [The Dragon Kings and the Lake Lady](lore/history/the-dragon-kings-and-the-lake-lady.md)

**magic-system**
- [Magic in Purewater: Water and Fire](lore/magic-system/magic-in-purewater-water-and-fire.md)

**religion**
- [The Gods of Mystamyr](lore/religion/the-gods-of-mystamyr.md)

## Dramatis personae

**Player characters**
- [Conall Bjornlasch](characters/pcs/conall-bjornlasch.json) — Arcane-casting magical investigator of the Order of the Blue Star; twin brother of Randall and secretly a son of Baron Hanzo. A razor-sharp investigator (Insight 88) who is also a capable fighter.
- [Gardwen](characters/pcs/gardwen.json) — Feral-raised elf druid and lone survivor of a Dragon Knight raid; a rank-1 divine caster of nature and pure-water magic who walks with a befriended she-wolf, searching for her long-lost brother.
- [Magda](characters/pcs/magda.json) — Aged barbarian berserker and sworn servant of the death-goddess Hel; Blessed by Hel (she does not age), she guards Gardwen and the lost twins and fights with berserk fury despite her years.
- [Randall](characters/pcs/randall.json) — Street thief of Purewater, raised in a brothel on the Pearl; identical twin of Conall and secretly a son of Baron Hanzo. A nimble, silver-tongued rogue (Deceit 75, Stealth 72, Sleight 71).

**NPCs**
- [Abel Weir](characters/npcs/abel-weir.json) — Sergeant of the City Watch, forty-one, twenty-two years in blue-grey. Keeps the referral book: four inches of complaints against the Baron's men that he has been ordered in writing to record and not act on. Not brave, thoroughly professional, and looking for someone to refer it all *to*. The party's lawful door.
- [Asphodel](characters/npcs/asphodel.json) — A courtesan at the Promise of Heaven, the house where Randall grew up. Warm, quick, and trusted by him 'as brother and sister' -- his closest confidante on the Pearl Quay and a ready source of information from the working girls.
- [Blau](characters/npcs/blau.json) — Baron Hanzo's albino lieutenant -- known to the ranks as Commander Vask. A thin, red-eyed, burn-scarred killer with unnatural strength who runs the Dragon Knights' day-to-day command and handles the Baron's 'dirty work': a cold, efficient assassin and intimidator.
- [Cailan](characters/npcs/cailan.json) — Gardwen's possessed brother (birth name Gabriel) -- the Baron's tournament champion, host to the ancient dragon-knight spirit Thuban Eta. Dragon-scale armor fused to his skin; eyes flicker reptilian when possessed; fights with uncanny ancient skill and minor fire.
- [Constantine](characters/npcs/constantine.json) — Proprietor of The Sylph's Embrace on the Pearl -- shrewd, protective of her workers, fiercely independent. Operates under Marisette's authority. After Santo's attack on Emmeralda in her house, she is hiring protection and wants justice.
- [Corvin](characters/npcs/corvin.json) — Sword of the Lake, twenty-two: earnest, brave, and not remotely subtle. Rows well, watches badly, and wants the white belt more than he wants to be careful.
- [Crowbill](characters/npcs/crowbill.json) — Leader of Purewater's criminal underworld -- canal smuggling, gambling, protection. Wiry and forgettable but for a small crow tattoo on his right hand. A master of streets and shadows (Streetwise 88, Stealth 82, Conceal 78) who keeps to a code: no killing locals, no harming children, no touching the Lake Lady's sites.
- [Emmeralda](characters/npcs/emmeralda.json) — Elven courtesan of The Sylph's Embrace -- poised, magnetic, and the finest performer on the Pearl (CHA 18, Seduction 88, Dance 85).
- [Guildmaster Torval Bluehand](characters/npcs/guildmaster-torval-bluehand.json) — Guildmaster of the Watercrafters -- middle-aged, practical innovator whose hands are permanently blue-tinged from decades of watercraft enchantment. A Magic-User specialized in water artifice (Craft 85, Arcane Casting 60, Mechanisms 80) rather than battle magic; his guild's enchantments keep the canal-city running.
- [Hanzo di Teufel](characters/npcs/hanzo-di-teufel.json) — Baron Hanzo di Teufel -- the campaign's master villain: a charismatic borderland noble and the only complete practitioner of the binding school, who has held a dragon-knight's spirit inside a living child for ten years. Not a battle-mage; he has never personally fought anybody, and works through charm, suggestion, the Dragon Knights, and a hundred years of patience. He means to become a Dragon King.
- [Harbormaster Velen Deepkeel](characters/npcs/harbormaster-velen-deepkeel.json) — Stern, weathered Harbormaster with forty years at the docks -- meticulous, traditional, publicly incorruptible. A consummate seaman and administrator (Seamanship 85, Navigation 82, Maritime Law 80) who controls the harbor's lawful face while quietly tolerating Crowbill's smuggling.
- [Hesper](characters/npcs/hesper.json) — To Purewater, Hesper is the madame Marisette's cold, dangerous mage-enforcer -- quiet, watchful, able to drop a strong man with a single spoken word. The truth is the opposite of what the mask suggests: Hesper is a deep-cover agent of the Quiet Hand, a hidden fellowship that works unseen for the good of the world, and the menace is a costume worn over a conscience. Master arcane caster (Arcane Casting 100, Willpower 95).
- [High Priestess Nerissa](characters/npcs/high-priestess-nerissa.json) — High Priestess of the Temple of the Lake Lady -- middle-aged, silver-streaked hair, blue-green robes that ripple like water. A powerful divine caster (Piety 92, Willpower 85) who senses water corruption, blesses sacred waters, and speaks with water spirits. Temple law forbids her from intervening directly, so she works through the PCs.
- [Ila](characters/npcs/ila.json) — A young elven girl (about thirteen) at the Sylph's Embrace, devoted to Emmeralda. An innocent of the Pearl, and a thread on the party's conscience.
- [Kerrin (brown coat)](characters/npcs/kerrin-brown-coat.json) — One of Crowbill's watchers: dockside, unremarkable, professional. Eleven years of reading faces across a room, and he follows rather than closes.
- [Lilura Deepcurrent](characters/npcs/lilura-deepcurrent.json) — Elderly head of the Order of the Lake Lady for three decades -- piercing blue eyes, rumored merfolk ancestry (she holds her breath unnaturally long). The city's most powerful divine caster (Piety 95, Willpower 92), guiding the Order's water-faith against the Baron's fire demonologists.
- [Marda Blackwater](characters/npcs/marda-blackwater.json) — Broad-shouldered leader of The Dredgers, risen from the dredge-boats during a labor dispute five years ago. A powerful working-class champion (Brawn 75, Oratory 78, Influence 75) who rallies dock labor against the merchant princes and -- above all -- against the Baron's Dragon Knights.
- [Mariarta](characters/npcs/mariarta.json) — An older, canny courtesan of the Promise of Heaven with 'the calm intelligence of someone who can survive almost any situation involving men.' Sent up to entertain the Baron's soldiers, she brings back the hard intelligence on his guarded quarters -- Randall's most valuable inside source on the Dragon Knights' manor.
- [Marisette](characters/npcs/marisette.json) — The madame with overall authority over Purewater's Pearl -- the proprietors, Constantine among them, answer to her. A consummate social power broker (Influence 85, Insight 82, Commerce 82) who keeps the pleasure district running and resents the disorder the Baron and Santo have brought to it.
- [Murgeroch](characters/npcs/murgeroch.json) — Temerach Nebulo's squire and go-between -- the steady, competent young fighter who carries the knight's messages, screens her meetings, and tends her gear. Usually the first of Temerach's people the party deals with.
- [Nus](characters/npcs/nus.json) — A quick-fingered Purewater street thief and loyal friend of Randall -- lookout, fence, and second pair of hands for a job; nimble, streetwise, and easy to underestimate.
- [Prince Emeric](characters/npcs/prince-emeric.json) — The young Governor of Purewater -- the King's nephew, perhaps two-and-twenty: clever, idealistic, genuinely decent, and entirely unsuited to govern a city like this. He wants to reform Purewater; the factions humor him, manage him, and run rings around his good intentions.
- [Ravella](characters/npcs/ravella.json) — Half-merfolk proprietor of The Siren's Call -- pleasure house and information market in one. Subtle waterfolk tells (webbed fingers, water-reflecting eyes, Swim 90). A master broker (Insight 85, Streetwise 88, Commerce 80) with light innate water magic, secretly protecting the city's hidden waterfolk.
- [Santo di Teufel](characters/npcs/santo-di-teufel.json) — Baron Hanzo's cruel son and heir -- a sadistic young fire-mage who taught himself demonology by tracing his father's work and can open a channel but **cannot seat a binding**. He is no part of his father's scheme and is not building anything: he wants **one girl** -- Emmeralda of the Sylph's Embrace -- kept on the barge and glad to be there, and he has exactly one stolen scroll with which to make her willing. He spends it, botches it, opens her the length of her body, and runs leaving the knife, the scroll and his own coat in the room.
- [Sana](characters/npcs/sana.json) — Nineteen, dark red hair chopped ragged on the left side. High Priestess Nerissa's niece, six weeks at the temple, and the one who notices what nobody else notices.
- [Sinnit](characters/npcs/sinnit.json) — A brutish Purewater canal-rat and rival thief who nurses a hard grudge against Randall -- a brawling enforcer-type with a long memory and a short temper.
- [Tat Atarer](characters/npcs/tat-atarer.json) — Captain of the Dragon Knights -- a hardened, pragmatic mercenary commander who serves Baron Hanzo for pay, not ideology. Master fighter (combat 97%); 'the Baron pays for our swords, not our opinions.'
- [Temerach Nebulo](characters/npcs/temerach-nebulo.json) — Elf knight of the Swords of the Lake, called 'the Lakelady's Javelin'; a deadly archer and peerless martial fighter tracking Baron Hanzo to expose his crimes.
- [Thorne](characters/npcs/thorne.json) — Elderly storyteller of The Moist Oyster -- frail-seeming but with penetrating blue eyes and a cane that hides a blade. Secretly a former Order of the Lake initiate and Dragon-Knight-raid survivor with peerless historical lore (Dragon Kings era 92) and knowledge of possession-ritual weaknesses.
- [Thuban Eta](characters/npcs/thuban-eta.json) — The ancient dragon-knight spirit bound inside Cailan. A betrayed tactical genius from the Dragon Kings era, held in thrall by Baron Hanzo's ritual through his bones and the binding locket. Indomitable will (Willpower 95), peerless tactics, honors the old codes -- a potential ally if freed.

**Creatures**
- [Ruhi](characters/creatures/ruhi.json) — Gardwen's befriended companion -- a loyal she-wolf; swift, keen-nosed and savage in the bite.

## Factions

- [Crowbill's Underworld](factions/crowbill-s-underworld.md) — Purewater's criminal underground -- canal smuggling, gambling, protection -- run to a code by the unremarkable crime lord Crowbill. Signaled by crow marks.
- [The Awake the Dragon Movement](factions/the-awake-the-dragon-movement.md) — A shadowy movement to revive the ancient draconic order and transform men into Dragon Kings. Baron Hanzo's true cause; an existential threat to water magic.
- [The City Watch](factions/the-city-watch.md) — Purewater's ordinary police, ninety-odd in blue-grey under Watch-Captain Ottilie Sarn -- and under written orders to record complaints against the Baron's people rather than act on them. Sergeant Abel Weir keeps the book.
- [The Currents](factions/the-currents.md) — A leaderless network of spies and informants trading in secrets, not contraband. Marked by chalk water-signs; the hidden 'Source' directs it.
- [The Dragon Knights](factions/the-dragon-knights.md) — Baron Hanzo's 20-30 sworn warriors -- brutal mercenaries armored in dragon heraldry, enhanced with fire demonology. In the streets daily and behaving like an army of occupation, because the watch has been told not to touch them. Locally despised as the 'dragonshits'.
- [The Dredgers](factions/the-dredgers.md) — Labor guild and mutual-aid society of Purewater's working poor -- canal-clearers, dockers, fishers. Black armbands, white wave. Led by Marda Blackwater.
- [The Harbor Masters](factions/the-harbor-masters.md) — The regulatory guild of Purewater's docks and shipping -- tariffs, berths, maritime law. Dark blue uniforms; a harbor tower HQ. Led by Velen Deepkeel.
- [The Mermaid's Court](factions/the-mermaid-s-court.md) — A secretive society of pure-water practitioners bound to merfolk, preserving water magic older than the city. Hidden under Lost Isle; led by the enigmatic 'Pearl'.
- [The Order of the Blue Star](factions/the-order-of-the-blue-star.md) — An institutional order of mages marked by a blue star at the brow. Trained Conall (through Old Johz) in arcane magic and investigation; takes a careful interest in dangerous power.
- [The Order of the Lake Lady](factions/the-order-of-the-lake-lady.md) — The water-faith of Purewater: priesthood of the lake goddess, guardians of pure water magic, political power over the sacred waters. Robed in blue-green with silver wave patterns.
- [The Pleasure Houses of the Pearl](factions/the-pleasure-houses-of-the-pearl.md) — The courtesan network of the Pearl, under the madame Marisette's near-absolute authority. Constantine's Sylph's Embrace and Ravella's Siren's Call among them.
- [The Quiet Hand](factions/the-quiet-hand.md) — A secret, centuries-old fellowship that steers the world toward the good from the shadows -- by knowing first and acting unseen. Espionage as mercy. Hesper is their agent in Purewater. (GM: a benevolent hidden patron.)
- [The Swords of the Lake](factions/the-swords-of-the-lake.md) — An elite knightly order sworn to the Lake Lady (Nimue) and the protection of the realm and its water magic. Temerach Nebulo is their most famous blade.
- [The Watercrafters Guild](factions/the-watercrafters-guild.md) — Artisan-mages of boats, canals, and water enchantment. Indigo sashes; workshops on Merchant's and Forge Quarter. Led by the blue-handed Guildmaster Torval.

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
