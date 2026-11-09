"""Verify preparation, then resume exactly at Hrill's held position."""
import json,pathlib,subprocess,os
P=pathlib.Path(__file__).resolve().parent
GM='/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
C='myth-campaign-purewater-s1';H='myth-char-07bc6645bb49'
MF=P/'hrill-greywatch-ids.json';M=json.loads(MF.read_text())
def save():MF.write_text(json.dumps(M,indent=2)+'\n')
def cli(*a):
 scope=['--pc',H] if a[0] in ['update-lore'] else ['--campaign',C,'--pc',H]
 r=subprocess.run(['uv','run','-q','--project',GM,'python',GM+'/mythras_gm.py',*a,*scope],capture_output=True,text=True,env=dict(os.environ,MYTHRAS_CAMPAIGN=C))
 if r.returncode:raise RuntimeError(r.stdout+r.stderr)
 d=json.loads(r.stdout)
 if not d.get('success'):raise RuntimeError(d)
 return d
def once(k,*a):
 if k not in M:M[k]=cli(*a);save()
 return M[k]
cast=M['cast']
# Import adapter also emits name-only weapon placeholders: replace only these
# freshly created NPC inventories with their complete prepared structured gear.
sheets=json.loads((P/'hrill-greywatch-npcs.json').read_text())
for key,sheet in zip(cast,sheets):
 gear=sheet['equipment']
 if key=='essa':gear=gear+[{'name':'Handaxe','damage':'1d6','size':'M'}]
 once('structured_gear_'+key,'update-character','--id',cast[key],'--equipment',json.dumps(gear))
once('ladder_correction','update-character','--id',cast['avel'],'--extras',json.dumps({'assets':{'ladder_feet':24}}))
once('prep_lore_corrected','update-lore','--id',M['prep_lore']['id'],'--narrative',(P/'hrill-greywatch-preparation.md').read_text())
once('task_fact','add-fact','--statement','Pike has tasked Mar, Toll and Arlo with recovering the fleeing Greywatch keeper; the keeper is seeking shelter and has not consented to their custody.','--status','established','--learned-by',','.join(cast[k] for k in ['pike','mar','toll','arlo','halwen']),'--source','witnessed')
once('demand_fact','add-fact','--statement','Avel and five armed followers have demanded surrender of Greywatch; Dera, Noll, Vela and Bess remain inside the shut tower. No breach outcome is yet resolved.','--status','established','--learned-by',','.join(cast[k] for k in ['avel','enna','corl','venn','essa','jerr','dera','noll','vela','bess','halwen']),'--source','witnessed')
# Actual readback gates opening; no test attacks or luck changes.
for key in cast:
 d=cli('get-character','--id',cast[key])['character']
 assert d['myth-luck-current']==0
 assert d['myth-attributes-json']['action_points'] in [2,3]
 assert all('damage' in x and 'size' in x for x in d['myth-equipment-json'])
 assert all(x['current_hp']==x['hp'] for x in d['myth-hit-locations-json'])
ctx=cli('get-context','--compact');(P/'greywatch-ready-context.json').write_text(json.dumps(ctx,indent=2)+'\n')
print('Context keys:',','.join(ctx),flush=True)
print('Selected scene:',ctx.get('storyline'),flush=True)
for ident in [M['g1']['id'],cast['halwen'],cast['mar']]:
 d=cli('brief','--id',ident);(P/('greywatch-brief-'+ident+'.json')).write_text(json.dumps(d,indent=2)+'\n')
for key in ['halwen','mar']:
 d=cli('character-view','--id',cast[key],'--compact');(P/('greywatch-knowledge-'+key+'.json')).write_text(json.dumps(d,indent=2)+'\n')
clock=cli('list-storylines');hrill=next(s for s in clock['storylines'] if s['name']=='Hrill')
if 'opening_tick' not in M:assert hrill['now']=='d25/dusk' and hrill['minute_in_watch']==92
once('readiness_log','log-event','--type','gm-note','--visibility','meta','--session','8','--involves',H,'--summary','Greywatch readiness passed:15 named full sheets, structured gear, zero NPC Luck, knowledge boundaries, locations, four conditional situations and three-act arc read back.','--narrative','Corrected24ft ladder for20ft wall. No future occupation established. Refusal, negotiation, authority travel, early victory, alternate entries and surrender tested in preparation. Clock held25dusk92 until opening. No change to other PC clocks or completed route.')
t=once('opening_tick','tick','--minutes','2');(P/'greywatch-opening-tick.json').write_text(json.dumps(t,indent=2)+'\n')
print('Tick keys:',','.join(t),flush=True)
print('Due beats:',json.dumps(t.get('due',t.get('beats',t.get('due_beats',[]))))[:4000],flush=True)
spoken='Boots hammer across the landing. A woman in a soot-stained wool coat stumbles through the teaching-house doorway, clutching a large iron key. Behind her, a leather-clad woman with a drawn sword and a man carrying a cudgel approach along the path. Your mail and shield are still aboard Grey Heron.\n\n“Shelter, please! They mean to take the beacon.”\n\nThe swordswoman calls from outside: “Hand her over, and we leave.”'
w=[H,'myth-char-56116fd29c52','myth-char-65109cb24a47',cast['halwen'],cast['mar'],cast['toll']]
once('opening_played','fire-beat','--id',M['g1']['id'],'--outcome','played','--log','--session','8','--witnesses',','.join(w),'--summary','Keeper seeks shelter at Listening Reeds teaching house; two armed pursuers demand her return. Hrill has not acted.','--narrative',spoken+'\nNo attack, injury, draw, armor, travel, new commission or answer to Edda assumed. Pike/Arlo remain in their boat30yards beyond doorway; G1 is contact, not successful custody.','--no-move')
once('opening_observation','add-fact','--statement','A keeper carrying an iron key has asked shelter in Listening Reeds teaching-house, saying they mean to take the beacon. A swordswoman and a cudgel-armed man outside demand she be handed over. No attack or consent has occurred.','--status','established','--learned-by',','.join(w),'--source','witnessed','--origin',M['opening_played'].get('event_id',M['g1']['id']))
scene='d25/dusk minute94, Listening Reeds teaching-house. Edda departure question interrupted, unanswered. Halwen inside at table with Hrill/Selith asks shelter, says they mean to take beacon; Mar drawn sword and Toll cudgel on path10yards from door demand return. Pike/Arlo remain boat30yards beyond doorway, bow available not aimed. No attack or initiative yet; Hrill action pending. Sword sheathed, bow lowered unnocked20arrows, AP0mail/shield stowed GreyHeron40yardsaway; fullHP Fresh Luck4 18GP. No sailing/rest/newservice/equipment assumed. Prior supply success and Garr unresolved hunt preserved. Active arc Crown Last Light.'
once('opening_scene','set-scene','--scene',scene)
after=cli('list-storylines');(P/'greywatch-opening-state.json').write_text(json.dumps(after,indent=2)+'\n')
assert next(s for s in after['storylines'] if s['name']=='Hrill')['minute_in_watch']==94
print(json.dumps({'success':True,'scene':scene}))
