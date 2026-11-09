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

def swap(spells):
    replacements = {'Armor': 'Invisibility', 'Feather Fall': 'Change Appearance'}
    return [replacements.get(spell, spell) for spell in spells]

before = cli('get-character', '--id', cid, '--campaign', campaign)['character']
spells = before['myth-spells-json']
spells['sorcery'] = swap(spells['sorcery'])
extras = before['myth-extras-json']
extras['spell_ranks']['1'] = swap(extras['spell_ranks']['1'])
extras['prepared_spells']['1'] = ['Magic Missile', 'Shield', 'Detect Magic', 'Invisibility', 'Change Appearance']
assert len(extras['spell_ranks']['1']) == 7
assert len(extras['prepared_spells']['1']) == extras['spell_memory_capacity']['1'] == 5
assert set(extras['prepared_spells']['1']) <= set(extras['spell_ranks']['1'])
assert len(spells['sorcery']) == len(set(spells['sorcery'])) == 25
cli('update-character', '--id', cid, '--spells', json.dumps(spells),
    '--extras', json.dumps(extras), '--extras-replace')
after = cli('get-character', '--id', cid, '--campaign', campaign)['character']
assert after['myth-spells-json']['sorcery'] == spells['sorcery']
assert after['myth-extras-json']['prepared_spells']['1'] == extras['prepared_spells']['1']
assert 'Armor' not in after['myth-spells-json']['sorcery'] and 'Feather Fall' not in after['myth-spells-json']['sorcery']
for key in ['myth-characteristics-json', 'myth-attributes-json', 'myth-skills-json',
            'myth-powers-json', 'myth-passions-json', 'myth-combat-styles-json',
            'myth-hit-locations-json', 'myth-luck-current', 'myth-magic-current']:
    assert before[key] == after[key]
sheet_path = root / 'nimras-rank-2.json'
sheet = json.loads(sheet_path.read_text())
sheet['sorcery_spells'] = after['myth-spells-json']['sorcery']
sheet['spell_ranks'] = extras['spell_ranks']
sheet['prepared_spells'] = extras['prepared_spells']
sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + '\n')
(root / 'nimras-db-readback.json').write_text(json.dumps(after, indent=2, ensure_ascii=False) + '\n')
path = root / 'nimras.md'
text = path.read_text()
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith('**Rank 1 known:'):
        lines[i] = '**Rank 1 known:** ' + ', '.join(extras['spell_ranks']['1']) + '.'
    if line.startswith('**Rank 1 prepared'):
        lines[i] = '**Rank 1 prepared (5/5):** ' + ', '.join(extras['prepared_spells']['1']) + '.'
lines += ['', 'Creation revision: Invisibility and Change Appearance replace Armor and Feather Fall. Both new spells are prepared; Sleep and Web remain in the spellbook and may be prepared through normal rest and study.', '']
path.write_text('\n'.join(lines))
print(json.dumps({'saved': True, 'rank_1_known': extras['spell_ranks']['1'],
                  'rank_1_prepared': extras['prepared_spells']['1'], 'total_known': 25}))
