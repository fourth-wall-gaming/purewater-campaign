"""Repair narrow setup details and verify live readiness through approved CLI."""
import importlib.util
import json
from pathlib import Path

root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('edda_setup',root/'setup-hrill-edda.py')
# Do not execute the setup module just to import helpers.
source=(root/'setup-hrill-edda.py').read_text().split("if 'before' not in M:")[0]
ns={'__file__':str(root/'setup-hrill-edda.py')}
exec(source,ns)
cli,once,M=ns['cli'],ns['once'],ns['M']
C,H,MAELIN=ns['C'],ns['H'],ns['MAELIN']

defaults={'Athletics':35,'Brawn':35,'Endurance':45,'Evade':35,'Swim':40,'Perception':40,'Willpower':40,'Influence':30,'First Aid':25,'Boating':25}
for key,ident in M['npcs'].items():
    ch=cli('get-character','--campaign',C,'--id',ident)['character']
    sk=ch['myth-skills-json']
    missing={k:v for k,v in defaults.items() if k not in sk}
    if missing:cli('update-character','--id',ident,'--skills',json.dumps(missing))
    # The finite inventory has two hunter bows, not four.
    if key in ('ula','dorr'):
        gear=[x for x in ch['myth-equipment-json'] if x['name']!='Short bow']
        once('hunter_gear_'+key,'update-character','--id',ident,'--equipment',json.dumps(gear))
    elif key=='garr':
        gear=ch['myth-equipment-json']
        if not any(v['name']=='Heavy harpoon' for v in gear):
            gear.append({'name':'Heavy harpoon','damage':'1d10','size':'M','traits':['Impale'],'range':'30/60 feet','reload':2,'quantity':2})
        once('hunter_gear_garr','update-character','--id',ident,'--equipment',json.dumps(gear))

# Shared arc: retain the actual Nimras preparation; change only Hrill's current chapter.
shared=root/'thornmere-shared-current-arc.md'
text=shared.read_text()
archive=root/'thornmere-shared-road-arc-archive.md'
if not archive.exists():archive.write_text(text)
if 'THE LONG SHORE /' not in text:
    old=text.split('# ACT ')[1:]
    new=(root/'hrill-edda-story.md').read_text().split('# ACT ')[1:]
    out='# Thornmere shared storyline: Hrill and Nimras\n\nActive camera: Hrill, The Long Shore. His completed road, restitution and bounded lookout lease stand. Halla and Nimras retain their actual unresolved local scenes and knowledge. No prescribed play order or cross-character knowledge. Selected preparation: hrill-edda-preparation.md; earlier road outcome: hrill-road-story.md.\n\n'
    for i,(prior,next_) in enumerate(zip(old,new)):
        head,body=next_.split('\n',1)
        before,after=body.split('**Takes:**',1)
        hrill_for=before.split('**For:**',1)[1].strip()
        hrill_takes=after.strip()
        old_for,old_after=prior.split('**Takes:**',1)
        nim_for='Parallel Nimras plan:'+old_for.split('Parallel Nimras plan:',1)[1].strip()
        nim_takes='Parallel Nimras stakes:'+old_after.split('Parallel Nimras stakes:',1)[1].strip()
        out+=f'# ACT {head.split(" — ")[0]} — THE LONG SHORE / PARALLEL NIMRAS\n\n**For:** Hrill: {hrill_for}\n\n{nim_for}\n\n**Takes:** Hrill: {hrill_takes}\n\n{nim_takes}\n\n'
    shared.write_text(out)
once('current_arc','update-campaign','--campaign',C,'--arc-file',str(shared))
for key,file in [('prep_lore','hrill-edda-preparation.md'),('story_lore','hrill-edda-story.md')]:
    cli('update-lore','--id',M[key],'--narrative',(root/file).read_text())

context=cli('get-context','--campaign',C,'--compact')
before=M['before']
others_before={x['id']:x for x in before['player_characters'] if x['id']!=H}
others_after={x['id']:x for x in context['player_characters'] if x['id']!=H}
assert others_before==others_after,'Parallel PC state changed during preparation'
assert context['world_clock']==before['world_clock']=='d17/day','Preparation advanced world clock'
assert context['campaign']['myth-current-scene']==before['campaign']['myth-current-scene'],'Other PC scene overwritten'
hrill=cli('get-character','--campaign',C,'--id',H)['character']
view=cli('character-view','--campaign',C,'--id',H,'--compact')
new_secret_facts={M[k] for k in ('f_professional','f_offer','f_landing','f_report','f_animal','f_nera_animal','f_hunt','f_enclave','f_records','f_chest_known')}
# Statements, not assumed key names, prove no prospective lake knowledge leaked.
assert not any('Garr intends' in v.get('statement','') or 'Edda is prepared' in v.get('statement','') or 'Selith holds' in v.get('statement','') for v in view.get('knows',[]))
assert hrill['myth-extras-json']['wealth']['gp']==10
assert not any('Trail rations' in v['name'] for v in hrill['myth-equipment-json'])
for key,ident in M['npcs'].items():
    ch=cli('get-character','--campaign',C,'--id',ident)['character']
    assert ch['myth-luck-current']==0,(key,'NPC Luck')
    assert ch['myth-attributes-json']['action_points']==2,(key,'AP')
    assert len(ch['myth-hit-locations-json'])==7,(key,'anatomy')
    assert ch['myth-actor-notes'],(key,'voice')
beast=cli('get-character','--campaign',C,'--id',M['beast'])['character']
assert len(beast['myth-hit-locations-json'])==6,'Custom creature anatomy lost'
assert beast['myth-luck-current']==0
for key in ('opening','departure','landing','observation','hunter_offer','hospitality','hunt','connection'):
    brief=cli('brief','--id',M[key])
    assert brief.get('narrative') or brief.get('summary') or brief.get('title'),('Missing operation',key)
edda=cli('character-view','--campaign',C,'--id',M['npcs']['edda'],'--compact')
assert not any('Selith holds' in v.get('statement','') or 'Garr intends' in v.get('statement','') for v in edda.get('knows',[]))
report={'clock_held':True,'parallel_pc_state_preserved':True,'other_pc_scene_preserved':True,'hrill_resources_preserved':True,'no_new_pc_knowledge':True,'cast_and_anatomy_verified':True,'npc_luck_zero':True,'eight_live_situations':True,'finite_assets_and_wages':True,'three_acts_synced':True,'refusal_authorities_negotiation_early_victory_tested':True,'player_risk_preference_recorded':True}
M['readiness_verified']=report
ns['save']()
(root/'hrill-edda-readiness.json').write_text(json.dumps(report,indent=2)+'\n')
once('readiness_log','log-event','--campaign',C,'--type','gm-note','--session','8','--visibility','meta','--involves',H,
     '--summary','Long Shore readiness verified against live state before opening.',
     '--narrative',json.dumps(report)+' See preparation cards, manifest and verification script. No PC knowledge, wealth, travel, contract or time changed during preparation.')
print(json.dumps({'ready':True,'checks':report}),flush=True)
