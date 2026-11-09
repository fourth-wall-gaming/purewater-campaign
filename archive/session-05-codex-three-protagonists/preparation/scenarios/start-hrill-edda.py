"""Open the verified selected chapter; reversible logistics, no accepted hire."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ns={'__file__':str(ROOT/'setup-hrill-edda.py')}
exec((ROOT/'setup-hrill-edda.py').read_text().split("if 'before' not in M:")[0],ns)
cli,once,M=ns['cli'],ns['once'],ns['M']
C,H,MAELIN=ns['C'],ns['H'],ns['MAELIN']
assert M.get('readiness_verified'), 'Must verify before opening'
before=M['before']

# Tick is the only clock mutation. Pending parallel scenes have their own audit.
once('opening_tick','tick','--campaign',C,'--to','d18/day')
for ident in (H,MAELIN):
    once('opening_move_'+ident,'move-character','--id',ident,'--location',M['hospice'])

# One actual elapsed day: finite new crews eat and receive pay; no infinite fund.
once('elapsed_edda','update-character','--id',M['npcs']['edda'],'--extras',json.dumps({
 'assets':{'gp':39.1,'food_person_days':76,'food_distribution':{'boat':71,'edda_carried':5},'crew_wages_paid_through':'d17/night','wage_payments':[{'for_day':'d17','total_gp':0.9,'Ressa_gp':0.5,'Perrin_gp':0.2,'Tovin_gp':0.2}]},
 'hiring_offer':{'status':'Opening offer made, awaiting response; no accepted contract or advance'},
 'doing':{'goal':'Hire dependable help and return to supply boat','next':'Introduced to Hrill by Maelin, offers1GP/day plus board, asks if he wants details; no answer yet','where':M['hospice'],'as_of_session':8}}))
for key,amount in [('ressa',0.5),('perrin',0.2),('tovin',0.2)]:
    once('elapsed_pay_'+key,'update-character','--id',M['npcs'][key],'--extras',json.dumps({'wealth':{'gp':amount},'wages_received_gp':amount}))
once('elapsed_garr','update-character','--id',M['npcs']['garr'],'--extras',json.dumps({'assets':{'gp':17,'food_person_days':20,'wages_paid_through':'d17/night','crew_wage_payments':[{'for_day':'d17','gp':1}]}}))
once('elapsed_ilyen','update-character','--id',M['npcs']['ilyen'],'--extras',json.dumps({'assets':{'food_person_days':15}}))
once('elapsed_selith','update-character','--id',M['npcs']['selith'],'--extras',json.dumps({'assets':{'food_days':11}}))

# Return of earlier chapter's anonymous workers/tools follows known half-day lane.
once('road_crew_return','update-character','--id','myth-char-0d84d89645ea','--extras',json.dumps({
 'assets':{'labourer_deployment':{'status':'Returned White Cairn with borrowed tools d17/dusk after completed prepaid two-session job'},'deployment':{'at_camp':{'labourers':4}}},
 'road_clearance_offer':{'status':'Completed and reported d17/dusk; all borrowed tools returned, no further pay incurred'},
 'doing':{'goal':'Maintain bounded lawful roadwork within actual remaining resources','next':'Received crew and completed lower-road report, ordinary payroll remains underfunded; no renewed coercion or new deployment','where':'myth-loc-1518aa5a203b','as_of_session':8}}))
once('road_report_fact','add-fact','--campaign',C,'--status','established','--when','d17/dusk','--learned-by','myth-char-0d84d89645ea','--source','told','--about','myth-loc-4425c616d679',
     '--statement','The four paid clearance workers returned along the known half-day lane to White Cairn with borrowed tools at d17/dusk and reported lower Wind Stair connection cleared to cart width under Maelin with Hrill. Vaust now receives this report; no extra work/pay or restored coercion.')
once('road_return_log','log-event','--campaign',C,'--type','scene','--session','8','--visibility','offscreen','--involves','myth-char-0d84d89645ea',
     '--summary','Paid clearance workers return borrowed tools and report success at White Cairn.',
     '--narrative','At d17/dusk, after actual half-day ridge journey, the four anonymous labourers return tools and report completed two-session work. No further deployment, unpaid extra session, new funding or coercive scheme. Hrill not present and does not automatically learn delivery completed.')

dialogue='I need someone steady for a supply voyage out of Hythe—unsafe landings, uncertain channels, and no promise of a quiet trip. One gold a day and your board; would you hear the details?'
narrative='Hrill accompanies Maelin from Wind Stair to Three Hearths after selected chapter transition, with quiet road camp and full ordinary walking time, arriving d18/day. Workers were left packing tools for their separate return, not omnisciently observed at White Cairn. Peat smoke crosses the courtyard. Maelin introduces Hrill and Edda Vale, a weathered woman with tar-darkened cuffs, at a table holding a rough lake chart. Edda shifts chart aside to make room and says: “'+dialogue+'” No reply, accepted hire, wage/advance, meal, knowledge of hunter/animal/enclave or northward departure established. Hrill10GP/no trailrations/fullhealth/Fresh/Luck4 unchanged.'
once('opening_fact','add-fact','--campaign',C,'--status','established','--when','d18/day','--learned-by',','.join([H,MAELIN,M['npcs']['edda']]),'--source','witnessed','--about',','.join([H,M['npcs']['edda'],M['hythe']]),
     '--statement','Maelin introduces Hrill Helmdance and Edda Vale at Three Hearths d18/day after actual return walk. Edda owns a supply boat based in Hythe and offers1GP/day plus board for unsafe landing/uncertain channel work. She asks if Hrill wants details. Offer unanswered/unpaid, no accepted employment, meal or boat journey; no creature, hunter or enclave secrets disclosed.')
once('opening_event','log-event','--campaign',C,'--type','scene','--session','8','--visibility','played','--involves',','.join([H,MAELIN,M['npcs']['edda']]),
     '--summary','At Three Hearths Maelin introduces Edda, who offers Hrill practical lake work.', '--narrative',narrative)
once('opening_beat','fire-beat','--campaign',C,'--id',M['opening'],'--outcome','played','--no-facts','--no-move')
once('opening_pc_state','update-character','--id',H,'--extras',json.dumps({'active_thread':{
 'title':'The Long Shore','story':'docs/scenarios/hrill-edda-story.md','preparation':'docs/scenarios/hrill-edda-preparation.md','session':8,
 'scene':'d18/day Three Hearths courtyard, after actual return walk with Maelin/quiet road camp. Introduced to Edda Vale at chart table; Edda offers1GP/day plus board to help supply voyage from Hythe, unsafe landings/uncertain channels. Asks if Hrill wants details. Offer unanswered/unpaid; no job/advance/meal/boat travel accepted. Hrill10GP,no trailrations,fullhealth/Fresh/Luck4. Completed road/restitution/boundedlease stand. Workers last seen packing tools; Vaust report not PCknowledge. No new northern secrets or otherPCknowledge. OtherPC scenes preserved.'}}))
once('opening_maelin_state','update-character','--id',MAELIN,'--extras',json.dumps({'doing':{'goal':'Report completed road and make ordinary useful introductions','next':'At Three Hearths, introduced Edda and Hrill; no automatic lake crew appointment or new paid job','where':M['hospice'],'as_of_session':8}}))
once('opening_audit','log-event','--campaign',C,'--type','gm-note','--session','8','--visibility','meta',
     '--summary','Opening travel and prior due-beat audit preserve parallel protagonists.',
     '--narrative','Maro/Ivo contact beats have no triggering contact. Halla Quiet War pending attempts require owning-camera prerequisite audit; unresolved Halla/Nimras scenes not advanced through Hrill journey. Northern contact beats not fired without arrival; Garr timed attempts later, actual resources/food/wages/location/weather and resistance required. One elapsed day new crew food/wages debited actual finite resources, no money conjured. Current calendar d18/day, other PC scene text unchanged.')

after=cli('get-context','--campaign',C,'--compact')
assert {p['id']:p for p in before['player_characters'] if p['id']!=H}=={p['id']:p for p in after['player_characters'] if p['id']!=H}
assert after['campaign']['myth-current-scene']==before['campaign']['myth-current-scene']
view=cli('character-view','--campaign',C,'--id',H,'--compact')
assert not any('Garr intends' in v.get('statement','') or 'Selith holds' in v.get('statement','') for v in view.get('knows',[]))
M['opening_complete']=True
M['opening_dialogue']=dialogue
ns['save']()
print(json.dumps({'opened':True,'clock':after['world_clock'],'no_hire_accepted':True,'other_pcs_preserved':True}),flush=True)
