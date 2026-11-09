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
                          engine + '/mythras_gm.py', *args], capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(run.stdout + run.stderr)
    result = json.loads([line for line in run.stdout.splitlines() if line.startswith('{')][-1])
    if not result.get('success'):
        raise RuntimeError(result)
    return result

def rename(value):
    if isinstance(value, dict):
        return {key.replace('Lore (Alchemy)', 'Lore (Magical traditions)'): rename(item)
                for key, item in value.items()}
    if isinstance(value, list):
        return [rename(item) for item in value]
    if isinstance(value, str):
        return value.replace('Lore (Alchemy)', 'Lore (Magical traditions)')
    return value

before = cli('get-character', '--id', cid, '--campaign', campaign)['character']
skills = rename(before['myth-skills-json'])
extras = rename(before['myth-extras-json'])
cli('update-character', '--id', cid, '--skills', json.dumps(skills),
    '--extras', json.dumps(extras), '--replace-json')
after = cli('get-character', '--id', cid, '--campaign', campaign)['character']
assert after['myth-skills-json']['Lore (Magical traditions)'] == 28
assert 'Lore (Alchemy)' not in after['myth-skills-json']
assert after['myth-extras-json']['skill_allocation'] == extras['skill_allocation']
assert after['myth-skills-json']['Stealth'] == 56 and after['myth-skills-json']['Deceit'] == 60
for key in ['myth-characteristics-json', 'myth-attributes-json', 'myth-spells-json',
            'myth-powers-json', 'myth-passions-json', 'myth-combat-styles-json',
            'myth-hit-locations-json', 'myth-luck-current', 'myth-magic-current']:
    assert before[key] == after[key]
for name in ['nimras-rank-2.json', 'nimras.md', 'build-nimras.py']:
    path = root / name
    path.write_text(path.read_text().replace('Lore (Alchemy)', 'Lore (Magical traditions)'))
(root / 'nimras-db-readback.json').write_text(json.dumps(after, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'saved': True, 'new_professional_skill': {'Lore (Magical traditions)': 28},
                  'old_skill_removed': True, 'other_mechanics_unchanged': True}))
