import json
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
engine = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
campaign = 'myth-campaign-purewater-s1'
source_path = root / 'new-human-mage-standard-rolls.json'
source = json.loads(source_path.read_text())
cid = source['character_id']
passions = {'Uphold (My independence)': 70,
            'Loyalty (The fellowship)': 59,
            'Respect (Rennic Vaur)': 50}

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
extras.pop('suggested_passions_not_applied', None)
extras['confirmed_personal_passions'] = passions
extras['pending_player_choices'] = [s for s in extras.get('pending_player_choices', []) if s != 'Passions']
extras['build_status'] = 'Core character mechanics and personality approved; not yet introduced in a scene. Fellowship name and home region remain open.'
cli('update-character', '--id', cid, '--passions', json.dumps(passions),
    '--extras', json.dumps(extras), '--extras-replace')
after = cli('get-character', '--id', cid, '--campaign', campaign)['character']
assert all(after['myth-passions-json'][key] == value for key, value in passions.items())
assert after['myth-passions-json']['True Neutral (Pragmatic; freedom of action)'] == 59
assert set(after['myth-passions-json']) == set(passions) | {'True Neutral (Pragmatic; freedom of action)'}
for key in ['myth-characteristics-json', 'myth-attributes-json', 'myth-skills-json',
            'myth-spells-json', 'myth-powers-json', 'myth-combat-styles-json',
            'myth-hit-locations-json', 'myth-luck-current', 'myth-magic-current']:
    assert before[key] == after[key]
sheet_path = root / 'nimras-rank-2.json'
sheet = json.loads(sheet_path.read_text())
sheet['passions'] = after['myth-passions-json']
sheet.pop('suggested_passions_not_applied', None)
sheet['confirmed_personal_passions'] = passions
sheet['pending_player_choices'] = extras['pending_player_choices']
sheet['build_status'] = extras['build_status']
sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + '\n')
source['confirmed_personal_passions'] = passions
source['creation_status'] = extras['build_status']
source_path.write_text(json.dumps(source, indent=2, ensure_ascii=False) + '\n')
(root / 'nimras-db-readback.json').write_text(json.dumps(after, indent=2, ensure_ascii=False) + '\n')
path = root / 'nimras.md'
text = path.read_text()
text = text.replace('Personal passions remain unchosen. Possible passions for review: Loyalty to former fellowship 69; Uphold independence 60; Respect Rennic Vaur 50. They have not been applied.',
    'Confirmed personal passions: **Uphold my independence 70%; Loyalty to the fellowship 59%; Respect Rennic Vaur 50%.**')
path.write_text(text)
cli('update-lore', '--id', source['concept_lore_id'],
    '--summary', 'Nimras: approved human Rank 2 freelance mage hunter build; True Neutral, independence 70, fellowship loyalty 59, respect for Vaur 50; not yet introduced in play.',
    '--narrative', 'Nimras’s existing character record is ' + cid + '. Human, Rank 2 Magic-User and freelance mage hunter. He left his independent fellowship amicably to spread his wings. The fellowship is his current client: find his former teacher Rennic Vaur in Purewater, bring him home alive and recover an entrusted manuscript. An introduction to Oren Vey is the proposed first lead. No Crown warrant. Characteristics STR11 CON15 SIZ10 DEX12 INT14 POW15 CHA15. True Neutral (Pragmatic; freedom of action)59. Confirmed passions: independence70, fellowship loyalty59, respect for Vaur50. He tries to be amiable, has firm boundaries and is willing to kill when he judges necessary. Player controls his choices. Lightning Bolt replaces Fireball; Stealth56, Deceit60 and Lore(Magical traditions)28 are confirmed revisions. Core mechanics and personality approved. Fellowship name and home region remain open. No arrival, quarry sighting, contract payment amount or starting scene has been resolved. Campaign remains d6/dusk after Hanzo’s departure; no rewind. Tavin Reed was an unadopted proposal.')
print(json.dumps({'saved': True, 'passions': passions, 'alignment_preserved': True}))
