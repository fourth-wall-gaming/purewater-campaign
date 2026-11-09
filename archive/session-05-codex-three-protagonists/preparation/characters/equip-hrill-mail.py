"""Narrow CLI adapter for wearing Hrill's existing full mail.

Installed update-character lacks hit-location AP updates. Use its own driver,
loader and attribute writer, preserving every HP and all other character data.
Requires the explicit PC/campaign and a live existing AP5 full-mail item.
"""
import argparse, json, os, pathlib, subprocess, sys
p=argparse.ArgumentParser()
p.add_argument('--pc',required=True)
p.add_argument('--campaign',required=True)
a=p.parse_args()
assert a.pc=='myth-char-07bc6645bb49'
assert a.campaign=='myth-campaign-purewater-s1'
os.environ['MYTHRAS_CAMPAIGN']=a.campaign
G='/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
sys.path.insert(0,G)
import mythras_gm as gm
root=pathlib.Path(__file__).resolve().parent
with gm.get_driver() as driver:
    before=gm._load_character(driver,a.pc)
    assert any('Chainmail' in x.get('name','') and 'AP 5' in x.get('name','') for x in before['myth-equipment-json'])
    (root/'hrill-before-donning-mail.json').write_text(json.dumps(before,indent=2)+'\n')
    locations=[dict(x,ap=5) for x in before['myth-hit-locations-json']]
    assert len(locations)==7
    gm._set_attr(driver,'myth-character',a.pc,'myth-hit-locations-json',json.dumps(locations))
    after=gm._load_character(driver,a.pc)
    for old,new in zip(before['myth-hit-locations-json'],after['myth-hit-locations-json']):
        assert old['hp']==new['hp'] and old['current_hp']==new['current_hp'] and new['ap']==5
    for key in ['myth-skills-json','myth-equipment-json','myth-extras-json','myth-luck-current','myth-magic-current','myth-fatigue']:
        assert before[key]==after[key]
print(json.dumps({'success':True,'pc':a.pc,'worn_ap':5,'hp_preserved':True}))
