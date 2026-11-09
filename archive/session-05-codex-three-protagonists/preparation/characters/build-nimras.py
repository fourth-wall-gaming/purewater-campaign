"""Build Nimras from CFI pools; save via the campaign CLI with an audit trail."""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
ENGINE = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
CAMPAIGN = 'myth-campaign-purewater-s1'
source_path = ROOT / 'new-human-mage-standard-rolls.json'
data = json.loads(source_path.read_text())
stats = data['assigned_characteristics']

def cli(*args):
    run = subprocess.run(['uv', 'run', '-q', '--project', ENGINE, 'python',
                          ENGINE + '/mythras_gm.py', *args], capture_output=True, text=True)
    lines = [line for line in run.stdout.splitlines() if line.startswith('{')]
    if run.returncode or not lines:
        raise RuntimeError(run.stderr + run.stdout)
    result = json.loads(lines[-1])
    if not result.get('success'):
        raise RuntimeError(result)
    return result

base = {
    'Athletics': 23, 'Boating': 26, 'Brawn': 21, 'Conceal': 27,
    'Customs (Home culture)': 68, 'Dance': 27, 'Deceit': 29, 'Drive': 27,
    'Endurance': 30, 'Evade': 24, 'First Aid': 26, 'Influence': 30,
    'Insight': 29, 'Locale (Home region)': 28, 'Perception': 29, 'Ride': 27,
    'Sing': 30, 'Stealth': 26, 'Swim': 26, 'Unarmed': 23, 'Willpower': 30,
    'Language (Common)': 69, 'Commerce': 29, 'Courtesy': 29, 'Streetwise': 30,
    'Arcane Casting': 29, 'Arcane Knowledge': 28, 'Language (Elven)': 29,
    'Lore (Magical traditions)': 28, 'Lore (Dangerous creatures)': 28,
    'Survival': 30, 'Combat Skill (Mage)': 23,
}
culture = {
    'Conceal': 5, 'Deceit': 5, 'Drive': 5, 'Influence': 10, 'Insight': 15,
    'Locale (Home region)': 10, 'Willpower': 15, 'Streetwise': 15,
    'Courtesy': 10, 'Commerce': 10,
}
career = {
    'Arcane Casting': 15, 'Arcane Knowledge': 15, 'Willpower': 15,
    'Insight': 15, 'Influence': 10, 'Perception': 15, 'Evade': 15,
}
bonus = {
    'Arcane Casting': 26, 'Arcane Knowledge': 27, 'Willpower': 20,
    'Insight': 21, 'Influence': 20, 'Perception': 26, 'Evade': 30,
    'Survival': 30, 'Streetwise': 25, 'Courtesy': 16,
    'Locale (Home region)': 12, 'Endurance': 15, 'Athletics': 12,
    'Combat Skill (Mage)': 20,
}
assert sum(culture.values()) == 100 and all(5 <= n <= 15 for n in culture.values())
assert sum(career.values()) == 100 and max(career.values()) <= 15
assert sum(bonus.values()) == 300 and max(bonus.values()) <= 30
assert set(culture) <= set(base) and set(career) <= set(base) and set(bonus) <= set(base)
skills = {name: value + culture.get(name, 0) + career.get(name, 0) + bonus.get(name, 0)
          for name, value in base.items()}
class_skills = ['Evade', 'First Aid', 'Influence', 'Insight', 'Locale (Home region)',
                'Perception', 'Willpower', 'Arcane Casting', 'Arcane Knowledge',
                'Language (Elven)', 'Lore (Magical traditions)', 'Lore (Dangerous creatures)']
qualifying = {name: skills[name] for name in class_skills if skills[name] >= 70}
assert len(qualifying) >= 5

cantrips = ['Read Magic', 'Appraise', 'Avert', 'Befuddle', 'Chill', 'Cleanse',
            'Coordination', 'Deflect', 'Dry', 'Ignite', 'Magic Tricks', 'Might',
            'Protection', 'Repair', 'Preserve']
rank1 = ['Magic Missile', 'Shield', 'Armor', 'Detect Magic', 'Sleep', 'Feather Fall', 'Web']
rank2 = ['Dispel Magic', 'Lightning Bolt', 'Locate Object']
prepared = {
    '0': ['Read Magic', 'Avert', 'Protection', 'Coordination', 'Repair'],
    '1': ['Magic Missile', 'Shield', 'Detect Magic', 'Sleep', 'Web'],
    '2': rank2,
}
capacity = {'0': stats['INT'] // 4 + 2, '1': stats['INT'] // 4 + 2, '2': stats['INT'] // 4}
assert len(cantrips) == 1 + 2 * (skills['Arcane Knowledge'] // 10)
assert len(rank1) == skills['Arcane Knowledge'] // 10 and len(rank2) == 3
for rank, known in [('0', cantrips), ('1', rank1), ('2', rank2)]:
    assert len(set(known)) == len(known)
    assert set(prepared[rank]) <= set(known) and len(prepared[rank]) <= capacity[rank]

before = cli('get-context', '--campaign', CAMPAIGN, '--compact')
if 'starting_wealth_roll' not in data:
    data['starting_wealth_roll'] = cli('roll', '--dice', '3d6')
    source_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
wealth = data['starting_wealth_roll']['total']
assert wealth >= 3
weapons = [
    {'name': 'Quarterstaff', 'damage': '1d8', 'size': 'M', 'hands': 2, 'traits': ['Stun Location']},
    {'name': 'Dart', 'damage': '1d4', 'size': 'S', 'quantity': 3, 'range': '15/30/60 ft', 'traits': ['Impale']},
]
gear = ['Common travelling clothes', 'Spellbook', 'Spell component pouch', 'Backpack',
        'Waterskin', 'Trail rations (7 days)', 'Bedroll', 'Small empty sack',
        'Flint and tinder', 'Two-hour candles (10)', 'Parchment pages (10)',
        'Quill', 'Bottle of ink', 'Belt pouch', 'Hemp rope (30 ft; purchased for 1 GP)']
locations = [
    {'name': 'Right Leg', 'range': '01-03', 'hp': 6, 'ap': 0},
    {'name': 'Left Leg', 'range': '04-06', 'hp': 6, 'ap': 0},
    {'name': 'Abdomen', 'range': '07-09', 'hp': 7, 'ap': 0},
    {'name': 'Chest', 'range': '10-12', 'hp': 8, 'ap': 0},
    {'name': 'Right Arm', 'range': '13-15', 'hp': 5, 'ap': 0},
    {'name': 'Left Arm', 'range': '16-18', 'hp': 5, 'ap': 0},
    {'name': 'Head', 'range': '19-20', 'hp': 6, 'ap': 0},
]
sheet = {
    'name': 'Nimras', 'stats': stats, 'skills': skills,
    'combat_styles': [{'name': 'Combat Skill (Mage)', 'value': skills['Combat Skill (Mage)'], 'weapons': weapons}],
    'hit_locations': locations,
    'attributes': {'action_points': 3, 'damage_modifier': '+0', 'initiative_bonus': 13,
                   'magic_points': 15, 'luck_points': 5, 'movement': '6.096m (20 feet)',
                   'healing_rate': 3, 'experience_modifier': 1},
    'equipment': gear, 'sorcery_spells': cantrips + rank1 + rank2,
    'powers': [{'name': 'Mental Strength', 'type': 'CFI mage Rank 1 ability',
                'prerequisite': 'Arcane Casting 60%', 'cost': 'Free character-creation ability',
                'effect': 'Once per day, mental-magic resistance Willpower tests are two difficulty grades easier. Disbelieving illusions and phantasms is one grade easier.',
                'uses_per_day': 1, 'uses_remaining': 1}],
    'passions': {}, 'class': 'Magic-User', 'rank': 2, 'rank_title': 'Mage',
    'race': 'Human', 'species': 'humanoid', 'culture': 'Civilized', 'pronouns': 'he/him',
    'build_status': 'Review draft; alignment and passions await player choice; not yet introduced in a scene.',
    'notes': 'Nimras: human Rank 2 Magic-User, freelance mage hunter trained by an independent fellowship. Left amicably to spread his wings. Review draft; not yet in play.',
    'background': data['concept'],
    'skill_allocation': {'base': base, 'culture': culture, 'class': career, 'bonus': bonus,
                         'culture_professional': ['Streetwise', 'Courtesy', 'Commerce'],
                         'class_professional': ['Arcane Casting', 'Arcane Knowledge', 'Language (Elven)', 'Lore (Magical traditions)', 'Lore (Dangerous creatures)'],
                         'hobby_professional': 'Survival', 'rank_qualifying_skills': qualifying,
                         'limits': '100 culture (5-15 each), 100 class (max 15), 300 Rank 2 bonus (max 30 each).'},
    'spell_ranks': {'0': cantrips, '1': rank1, '2': rank2},
    'prepared_spells': prepared, 'spell_memory_capacity': capacity,
    'spell_learning': 'Read Magic plus 14 cantrips and 7 Rank 1 spells at Arcane Knowledge 70; 3 spells gained on reaching Rank 2. No extra spells awarded.',
    'wealth': {'gp': wealth - 1, 'sp': 0, 'cp': 0,
               'starting_roll': data['starting_wealth_roll'], 'purchases_gp': {'Hemp rope (30 ft)': 1},
               'contract_advance': 'Amount not established; not added to starting wealth.'},
    'cfi_rules_notes': ['Rank 2: base 2 AP +1; base POW Luck 3 + human 1 + Rank 2 table 1 =5.',
                        'CON+SIZ 25: use CFI HP table, then +1 in each location at Rank 2.',
                        'INT/4 memory fractions rounded down following engine skill guidance.',
                        'Rank 2 spells cost normally; lower-rank spell final costs reduced by 2 per rank difference, minimum 1 MP.',
                        'No spell is forgotten merely by successful casting. Arcane casting requires freedom from armour and shields.',
                        'No additional paid Rank abilities granted; no unspent advancement budget invented.',
                        'Locale and Customs refer to his home region, not automatic knowledge of Purewater. Home region and fellowship name remain undecided.',
                        'Navigation and Track are untrained Professional skills and have not been added under other names.'],
    'pending_player_choices': ['Alignment', 'Passions', 'Home region and fellowship name'],
    'suggested_passions_not_applied': {'Loyalty (Former fellowship)': 69, 'Uphold (Independence)': 60, 'Respect (Rennic Vaur)': 50},
}
sheet_path = ROOT / 'nimras-rank-2.json'
sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + '\n')

if data.get('character_id'):
    raise RuntimeError('Nimras already has a character id; update explicitly instead of re-importing.')
existing = cli('list-characters', '--campaign', CAMPAIGN)
assert not any(c['name'] == 'Nimras' for c in existing['characters']), 'Nimras already exists in campaign'
saved = cli('import-characters', '--campaign', CAMPAIGN, '--type', 'pc', '--file', str(sheet_path))
cid = saved['imported'][0]['id']
data['character_id'] = cid
data['character_created'] = True
data['creation_status'] = 'Review draft; core mechanics and equipment saved; alignment/passions unchosen.'
source_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
cli('update-character', '--id', cid, '--status', 'creation-draft', '--luck', '5',
    '--magic-current', '15', '--narrative',
    'Nimras is a freelance mage hunter trained by an independent fellowship. He left on good terms to choose his own work and establish his independence. The fellowship has commissioned him to find his former teacher Rennic Vaur in Purewater and recover an entrusted manuscript. His introduction to Oren Vey is his first proposed lead. He holds no Crown warrant. Alignment and passions remain the player’s choice. No arrival, target sighting or scene has been played.')
cli('link-lore', '--id', data['concept_lore_id'], '--subject', cid)
cli('update-lore', '--id', data['concept_lore_id'], '--summary', 'Nimras: human Rank 2 freelance mage hunter; mechanical review draft created, social/travel skills included, alignment and passions pending.',
    '--narrative', 'Nimras’s character record is ' + cid + '. Core concept and characteristics are agreed. A mechanical review draft has been created with CFI culture 100, class 100 and Rank 2 bonus 300 skill points. He has Mental Strength, a 25-spell book and standard equipment plus purchased rope. Civilized culture and Elven as a scholarly language are draft implementation choices. Alignment and passions remain unset. Fellowship name and home region remain unchosen. No current-scene change, arrival, contract payment amount, quarry sighting or in-world action has been established. The earlier Tavin Reed proposal is unadopted.')

character = cli('get-character', '--id', cid, '--campaign', CAMPAIGN)['character']
(ROOT / 'nimras-db-readback.json').write_text(json.dumps(character, indent=2, ensure_ascii=False) + '\n')
assert character['myth-characteristics-json'] == stats
assert character['myth-attributes-json']['action_points'] == 3
assert character['myth-attributes-json']['luck_points'] == 5
assert character['myth-luck-current'] == 5 and character['myth-magic-current'] == 15
assert character['myth-status'] == 'creation-draft'
assert character['myth-spells-json']['sorcery'] == sheet['sorcery_spells']
assert character['myth-skills-json']['Survival'] == 60
assert character['myth-skills-json']['Streetwise'] == 70
assert character['myth-combat-styles-json']['Combat Skill (Mage)'] == 43
assert all(location['hp'] == expected['hp'] for location, expected in zip(character['myth-hit-locations-json'], locations))
after = cli('get-context', '--campaign', CAMPAIGN, '--compact')
assert before['campaign'] == after['campaign']
halla = lambda context: next(p for p in context['player_characters'] if p['name'] == 'Halla')
assert halla(before) == halla(after)

lines = ['# Nimras — Rank 2 Magic-User', '',
         'Review draft. Freelance mage hunter; human, Civilized culture. Left his independent fellowship amicably. The current commission is to recover his former teacher Rennic Vaur and an entrusted manuscript in Purewater.', '',
         '**Characteristics:** ' + ', '.join(f'{k} {v}' for k, v in stats.items()), '',
         '**Resources:** 3 Action Points; 15 Magic Points; 5 Luck; initiative 13; movement 20 feet; damage modifier +0.', '',
         '**Hit points:** head/legs 6; arms 5; abdomen 7; chest 8. No worn armour.', '',
         '## Skills', '', '| Skill | Base | Culture | Class | Experienced bonus | Total |',
         '|---|---:|---:|---:|---:|---:|']
for name in skills:
    lines.append(f'| {name} | {base[name]} | {culture.get(name,0)} | {career.get(name,0)} | {bonus.get(name,0)} | {skills[name]} |')
lines += ['', 'Pools: 100 culture, 100 class, 300 experienced bonus. Six class skills reach 70% or more. Survival is the extra Professional skill; Navigation and Track remain untrained.', '',
          '## Ability', '', '**Mental Strength:** once daily, resist mental magic with Willpower two grades easier; disbelieve illusions one grade easier. Free qualifying Rank 1 ability. Other paid Rank abilities are not awarded.', '',
          '## Spellbook and preparation', '']
for rank, spells in [('0',cantrips),('1',rank1),('2',rank2)]:
    lines += [f'**Rank {rank} known:** ' + ', '.join(spells) + '.', '',
              f'**Rank {rank} prepared ({len(prepared[rank])}/{capacity[rank]}):** ' + ', '.join(prepared[rank]) + '.', '']
lines += ['The book contains 15 cantrips, 7 Rank 1 spells and 3 Rank 2 spells. Casting does not consume a prepared spell. Spell preparation is a draft loadout; it can be changed through normal rest and study. Rank 2 cost reductions apply to lower-rank spells, with a 1 MP minimum.', '',
          'Lightning Bolt provides force; Dispel Magic supports counterspelling; Locate Object supports pursuit subject to the spell’s actual conditions. Sleep and Web offer capture options. No automatic immunity, detection or target location is granted.', '',
          '## Equipment and money', '', 'Quarterstaff, three darts, ordinary clothes, spellbook, component pouch, backpack, waterskin, seven days of rations, bedroll, sack, fire-lighting kit, candles, writing materials, belt pouch and 30 feet of rope.', '',
          f'Starting wealth: official engine 3d6 roll {data["starting_wealth_roll"]["rolls"]} = {wealth} GP. Rope costs 1 GP; remaining purse {wealth-1} GP. No unspecified contract advance added.', '',
          '## Choices still belonging to the player', '',
          'Alignment and passions remain unset. Possible passions for review: Loyalty to former fellowship 69; Uphold independence 60; Respect Rennic Vaur 50. They have not been applied.', '',
          'The fellowship’s name, home region, age and appearance are open. Civilized upbringing and Elven reading are draft choices. Customs and Locale concern his home, not Purewater. No starting scene has been played.', '',
          '## Rules used', '',
          'CFI SRD: Characters steps 4–8 and experienced-character table; Civilized human culture; Magic-User class, rank table, abilities and spell list; Magic, spell learning and memorisation; equipment tables. Actual rolls use the Mythras CLI.', '',
          'Saved as a creation draft in the existing Purewater database at d6/dusk. Halla, the campaign scene and world clock are unchanged.', '']
(ROOT / 'nimras.md').write_text('\n'.join(lines))
print(json.dumps({'success': True, 'character_id': cid, 'wealth_roll': data['starting_wealth_roll'],
                  'purse_gp': wealth - 1, 'rank_qualifying_skills': qualifying,
                  'social': {k:skills[k] for k in ['Influence','Insight','Streetwise','Courtesy','Commerce']},
                  'travel': {k:skills[k] for k in ['Survival','Endurance','Athletics','Locale (Home region)']},
                  'campaign_scene_clock_and_halla_unchanged': True, 'build_status': 'creation-draft'}))
