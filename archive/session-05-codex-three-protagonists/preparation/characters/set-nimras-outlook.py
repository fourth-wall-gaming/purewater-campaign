import json
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
engine = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
campaign = 'myth-campaign-purewater-s1'
source_path = root / 'new-human-mage-standard-rolls.json'
source = json.loads(source_path.read_text())
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

before = cli('get-character', '--id', cid, '--campaign', campaign)['character']
extras = before['myth-extras-json']
outlook = {
    'player_defined': True,
    'manner': 'Tries to be pleasant and amiable.',
    'ethics': 'Pragmatic; exercises his own judgement.',
    'boundaries': 'Does not tolerate people messing with him.',
    'lethal_force': 'Willing to kill when he thinks it necessary; the player decides when that is.',
}
alignment = {'name': 'True Neutral', 'elements': ['Pragmatic', 'Freedom of action'], 'value': 59,
             'calculation': 'INT 14 + POW 15 + 30'}
extras['alignment'] = alignment
extras['outlook'] = outlook
extras['pending_player_choices'] = [item for item in extras['pending_player_choices'] if item != 'Alignment']
extras['build_status'] = 'Review draft; alignment defined, personal passions await player choice; not yet introduced in a scene.'
cli('update-character', '--id', cid,
    '--extras', json.dumps(extras), '--extras-replace',
    '--passions', json.dumps({'True Neutral (Pragmatic; freedom of action)': 59}))
after = cli('get-character', '--id', cid, '--campaign', campaign)['character']
assert after['myth-passions-json']['True Neutral (Pragmatic; freedom of action)'] == 59
assert after['myth-extras-json']['outlook'] == outlook
for key in ['myth-characteristics-json', 'myth-skills-json', 'myth-attributes-json',
            'myth-luck-current', 'myth-magic-current', 'myth-spells-json']:
    assert before[key] == after[key]
sheet_path = root / 'nimras-rank-2.json'
sheet = json.loads(sheet_path.read_text())
sheet['alignment'] = alignment
sheet['outlook'] = outlook
sheet['passions']['True Neutral (Pragmatic; freedom of action)'] = 59
sheet['pending_player_choices'] = extras['pending_player_choices']
sheet['build_status'] = extras['build_status']
sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + '\n')
source['outlook'] = outlook
source['alignment'] = alignment
source['creation_status'] = extras['build_status']
source_path.write_text(json.dumps(source, indent=2, ensure_ascii=False) + '\n')
(root / 'nimras-db-readback.json').write_text(json.dumps(after, indent=2, ensure_ascii=False) + '\n')
path = root / 'nimras.md'
text = path.read_text().replace('Alignment and passions remain unset.',
    '**Alignment: True Neutral (Pragmatic; freedom of action) 59%.** Nimras tries to be pleasant and amiable, holds firm personal boundaries, and is willing to kill when he judges it necessary. The player decides when that threshold is met. Personal passions remain unchosen.')
path.write_text(text)
print(json.dumps({'saved': True, 'alignment': alignment, 'personal_passions_unchosen': True}))
