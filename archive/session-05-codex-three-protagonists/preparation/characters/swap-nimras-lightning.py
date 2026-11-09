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
spells = json.loads(json.dumps(before['myth-spells-json']).replace('Fireball', 'Lightning Bolt'))
extras = json.loads(json.dumps(before['myth-extras-json']).replace('Fireball', 'Lightning Bolt'))
cli('update-character', '--id', cid, '--spells', json.dumps(spells),
    '--extras', json.dumps(extras), '--extras-replace')
after = cli('get-character', '--id', cid, '--campaign', campaign)['character']
assert 'Fireball' not in json.dumps(after['myth-spells-json'])
assert after['myth-spells-json']['sorcery'].count('Lightning Bolt') == 1
assert after['myth-extras-json']['spell_ranks']['2'] == ['Dispel Magic', 'Lightning Bolt', 'Locate Object']
assert after['myth-extras-json']['prepared_spells']['2'] == ['Dispel Magic', 'Lightning Bolt', 'Locate Object']
for key in ['myth-characteristics-json', 'myth-skills-json', 'myth-attributes-json',
            'myth-luck-current', 'myth-magic-current', 'myth-hit-locations-json']:
    assert before[key] == after[key]
for name in ['nimras-rank-2.json', 'nimras.md', 'build-nimras.py']:
    path = root / name
    path.write_text(path.read_text().replace('Fireball', 'Lightning Bolt'))
(root / 'nimras-db-readback.json').write_text(json.dumps(after, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'saved': True, 'rank_2_known_and_prepared': extras['spell_ranks']['2'], 'other_mechanics_unchanged': True}))
