import json
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
engine = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
campaign = 'myth-campaign-purewater-s1'
source_path = root / 'new-human-mage-standard-rolls.json'
source = json.loads(source_path.read_text())
cid = source['character_id']
portrait = {
    'path': str(root / 'nimras-portrait-v1.png'),
    'workspace_relative_path': 'docs/characters/nimras-portrait-v1.png',
    'status': 'Approved by the player as Nimras’s appearance reference.',
    'generation': 'Built-in image generation; graphite and ink character sketch.',
    'appearance': 'Compact, healthy human man around thirty, dark tousled hair, light stubble, amiable self-possessed expression; worn practical travelling coat over ordinary unarmoured clothes, boots, spellbook satchel and component pouch. Plain wooden quarterstaff and a small suggestion of lightning.',
    'scope': 'Appearance reference only; no added powers or equipment. Quarterstaff is already on the mechanical sheet.',
    'prompt': 'Quick expressive graphite and ink character sketch on warm off-white paper of Nimras, a compact human male freelance mage hunter around thirty, healthy and moderately athletic, intelligent personable face, small easy smile, steady gaze, practical worn travelling coat over plain unarmoured clothes, boots, component pouch, well-used spellbook in a weatherproof satchel, plain wooden quarterstaff and a small fork of lightning at his free hand. Loose canal-city background inspired by Venice, confident hatching, natural human anatomy. No armour, shield, pointed hat, ornate robes, fireball, glowing eyes, text or watermark.',
}
assert pathlib.Path(portrait['path']).is_file()

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
cli('update-character', '--id', cid, '--extras', json.dumps({'portrait': portrait, 'appearance': portrait['appearance']}))
after = cli('get-character', '--id', cid, '--campaign', campaign)['character']
assert after['myth-extras-json']['portrait']['path'] == portrait['path']
for key in ['myth-status', 'myth-skills-json', 'myth-spells-json', 'myth-passions-json',
            'myth-equipment-json', 'myth-attributes-json', 'myth-combat-styles-json',
            'myth-luck-current', 'myth-magic-current']:
    assert before[key] == after[key]
sheet_path = root / 'nimras-rank-2.json'
sheet = json.loads(sheet_path.read_text())
sheet['portrait'] = portrait
sheet['appearance'] = portrait['appearance']
sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + '\n')
source['portrait'] = portrait
source_path.write_text(json.dumps(source, indent=2, ensure_ascii=False) + '\n')
(root / 'nimras-db-readback.json').write_text(json.dumps(after, indent=2, ensure_ascii=False) + '\n')
path = root / 'nimras.md'
text = path.read_text()
if '![Nimras — approved character sketch]' not in text:
    text = text.replace('# Nimras — Rank 2 Magic-User\n', '# Nimras — Rank 2 Magic-User\n\n![Nimras — approved character sketch](nimras-portrait-v1.png)\n\nApproved appearance reference, generated with the built-in image tool. Quarterstaff already included in equipment.\n', 1)
    path.write_text(text)
print(json.dumps({'saved': True, 'portrait': portrait['path'], 'linked_to_character': cid, 'game_state_unchanged': True}))
