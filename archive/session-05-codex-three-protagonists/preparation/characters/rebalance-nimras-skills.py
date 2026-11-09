import json
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
engine = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
campaign = 'myth-campaign-purewater-s1'
source = json.loads((root / 'new-human-mage-standard-rolls.json').read_text())
cid = source['character_id']

def cli(*args):
    run = subprocess.run(['uv', 'run', '-q', '--project', engine, 'python',
                          engine + '/mythras_gm.py', *args], text=True, capture_output=True)
    if run.returncode:
        raise RuntimeError(run.stdout + run.stderr)
    result = json.loads([line for line in run.stdout.splitlines() if line.startswith('{')][-1])
    if not result.get('success'):
        raise RuntimeError(result)
    return result

before = cli('get-character', '--id', cid, '--campaign', campaign)['character']
sheet_path = root / 'nimras-rank-2.json'
sheet = json.loads(sheet_path.read_text())
allocation = sheet['skill_allocation']
allocation['culture']['Deceit'] = 10
allocation['culture']['Commerce'] = 5
allocation['bonus'].update({'Willpower': 10, 'Insight': 11, 'Courtesy': 0,
                            'Locale (Home region)': 2, 'Endurance': 10,
                            'Stealth': 30, 'Deceit': 21})
assert sum(allocation['culture'].values()) == 100
assert all(5 <= n <= 15 for n in allocation['culture'].values())
assert sum(allocation['class'].values()) == 100
assert sum(allocation['bonus'].values()) == 300 and max(allocation['bonus'].values()) <= 30
skills = {name: base + sum(allocation[pool].get(name, 0) for pool in ['culture', 'class', 'bonus'])
          for name, base in allocation['base'].items()}
qualifying = {name: skills[name] for name in allocation['rank_qualifying_skills'] if skills[name] >= 70}
assert len(qualifying) >= 5
assert skills['Stealth'] == 56 and skills['Deceit'] == 60
allocation['rank_qualifying_skills'] = qualifying
sheet['skills'] = skills
sheet['combat_styles'][0]['value'] = skills['Combat Skill (Mage)']
extras = before['myth-extras-json']
extras['skill_allocation'] = allocation
cli('update-character', '--id', cid,
    '--skills', json.dumps({k:v for k,v in skills.items() if k != 'Combat Skill (Mage)'}),
    '--extras', json.dumps(extras), '--extras-replace')
after = cli('get-character', '--id', cid, '--campaign', campaign)['character']
assert after['myth-skills-json']['Stealth'] == 56
assert after['myth-skills-json']['Deceit'] == 60
assert after['myth-extras-json']['skill_allocation'] == allocation
for key in ['myth-characteristics-json', 'myth-attributes-json', 'myth-spells-json',
            'myth-powers-json', 'myth-passions-json', 'myth-combat-styles-json',
            'myth-hit-locations-json', 'myth-luck-current', 'myth-magic-current']:
    assert before[key] == after[key]
sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + '\n')
(root / 'nimras-db-readback.json').write_text(json.dumps(after, indent=2, ensure_ascii=False) + '\n')
path = root / 'nimras.md'
text = path.read_text()
start = text.index('| Skill | Base |')
end = text.index('\nPools:', start)
table = ['| Skill | Base | Culture | Class | Experienced bonus | Total |',
         '|---|---:|---:|---:|---:|---:|']
for name, value in skills.items():
    table.append(f'| {name} | {allocation["base"][name]} | {allocation["culture"].get(name,0)} | {allocation["class"].get(name,0)} | {allocation["bonus"].get(name,0)} | {value} |')
text = text[:start] + '\n'.join(table) + '\n' + text[end:]
text += '\nCreation revision: Stealth 56%, Deceit 60%. No extra skill points granted. Rank 2 prerequisites, spellbook, resources and weapon skill preserved.\n'
path.write_text(text)
print(json.dumps({'saved': True, 'stealth': skills['Stealth'], 'deceit': skills['Deceit'],
                  'qualifying_class_skills': qualifying,
                  'reduced_skills': {k: [before['myth-skills-json'][k], skills[k]] for k in skills
                                     if k in before['myth-skills-json'] and skills[k] < before['myth-skills-json'][k]},
                  'professional_skills': {k: skills[k] for k in allocation['culture_professional'] + allocation['class_professional'] + [allocation['hobby_professional']]}}))
