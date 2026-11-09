import json
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
path = root / 'new-human-mage-standard-rolls.json'
data = json.loads(path.read_text())
engine = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
def cli(*args):
    result = subprocess.run(['uv', 'run', '-q', '--project', engine, 'python',
                             engine + '/mythras_gm.py', *args], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    result = json.loads([s for s in result.stdout.splitlines() if s.startswith('{')][-1])
    if not result.get('success'):
        raise RuntimeError(result)
    return result

narrative = 'Nimras — agreed character concept and build in progress.\n\n'
narrative += 'Human Magic-User, target Rank 2. Characteristics: ' + json.dumps(data['assigned_characteristics']) + '.\n\n'
narrative += '\n\n'.join(key + ': ' + value for key, value in data['concept'].items())
narrative += '\n\nThe player selected the name Nimras. The Tavin Reed proposal was not adopted. No personal thoughts, dialogue, alignment or passion scores are assigned. The commission is the agreed premise; whether an employer’s account is true must be established through preparation and play. No quarry location, crime beyond the stated allegation, contract payment amount or arrival event has been resolved. No live PC sheet has yet been created.'
summary = 'Nimras: human Rank 2 mage-hunter build; freelance, independent fellowship trained, amicable departure, pursuing former teacher Rennic Vaur.'
if data.get('concept_lore_id'):
    saved = cli('update-lore', '--id', data['concept_lore_id'], '--narrative', narrative, '--summary', summary)
else:
    saved = cli('add-lore', '--campaign', 'myth-campaign-purewater-s1', '--title', 'Nimras — character creation in progress',
                '--category', 'character-creation', '--visibility', 'player', '--summary', summary, '--narrative', narrative)
    data['concept_lore_id'] = saved['id']
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
verified = cli('get-lore', '--id', data['concept_lore_id'])
assert verified['lore']['content'] == narrative
print(json.dumps({'saved': True, 'name': data['name'], 'lore_id': data['concept_lore_id'], 'sheet_complete': False}))
