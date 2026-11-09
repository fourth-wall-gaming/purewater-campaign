"""Activate the selected adventure via the official Mythras CLI; resumable manifest."""
import json, pathlib, subprocess, re, os
ROOT=pathlib.Path(__file__).resolve().parent
E='/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
C='myth-campaign-purewater-s1'; N='myth-char-4fc52ae14026'; V='myth-char-1aa1d6892d3a'; VEY='myth-char-fd2973412ca1'
P=ROOT/'glass-hounds-ids.json'; M=json.loads(P.read_text()) if P.exists() else {}
def remember(k,v):
 M[k]=v; P.write_text(json.dumps(M,indent=2)+'\n'); return v
def cli(*a):
 r=subprocess.run(['uv','run','-q','--project',E,'python',E+'/mythras_gm.py',*map(str,a)],capture_output=True,text=True,env={**os.environ,"MYTH_CAMPAIGN":C,"MYTHRAS_CAMPAIGN":C})
 if r.returncode: raise RuntimeError(r.stdout+r.stderr)
 d=json.loads([s for s in r.stdout.splitlines() if s.startswith('{')][-1])
 if not d.get('success'): raise RuntimeError(d)
 return d
def new(k,*a):
 return M[k] if k in M else remember(k,cli(*a)['id'])
def j(x):return json.dumps(x,ensure_ascii=False)
def fact(k,s,about,knowers,source='witnessed',status='established'):
 a=['add-fact','--campaign',C,'--statement',s,'--status',status,'--about',','.join(about),'--narrative','Glass Hounds selected setup. GM plan is separate from player knowledge.']
 if status=='established': a+=['--when','d6/night','--learned-by',','.join(knowers),'--source',source]
 return new(k,*a)
if M.get('activated'): raise SystemExit('Already activated; read live save, do not repeat opening.')
before=cli('get-context','--campaign',C,'--compact')
assert before['world_clock']=='d6/night'
remember('before_clock',before['world_clock'])
# Retire the failed episode, preserving audit and approved commission.
if not M.get('withdrawn'):
 events=json.loads((ROOT.parent.parent/'checkpoints/nimras-before-adventure-rebuild-2026-10-23/journal/events.json').read_text())
 retired=[]
 for ev in events:
  if ev.get('session')==6 and ev.get('id')!='myth-event-7b16359138b9' and ev.get('visibility')=='played':
   cli('retire-canon','--id',ev['id'],'--status','retracted'); retired.append(ev['id'])
 fs=[]
 for p in (ROOT.parent.parent/'checkpoints/nimras-before-adventure-rebuild-2026-10-23/facts').glob('*.md'):
  t=p.read_text()
  if N in t or V in t:
   fid=re.search(r'id: "([^"]+)"',t)[1]
   if fid!='myth-fact-ec06999e5416': cli('supersede-fact','--id',fid,'--campaign',C); fs.append(fid)
 remember('withdrawn',{'events':retired,'facts':fs})
if not M.get('events_retracted'):
 events=json.loads((ROOT.parent.parent/'checkpoints/nimras-before-adventure-rebuild-2026-10-23/journal/events.json').read_text())
 ids=[]
 for ev in events:
  if ev.get('session')==6 and ev.get('id')!='myth-event-7b16359138b9' and ev.get('visibility') in [None,'played']:
   cli('retire-canon','--id',ev['id'],'--status','retracted');ids.append(ev['id'])
 remember('events_retracted',ids)
# Locations, with playable geometry.
locs={
 'court':('Furnace Court','courtyard','Public glassworking court in the Merchant Quarter; east stair reaches the Glasswalk, west canal stair, north glass workshop, south alley.','SENSE: hot mineral smell, furnace draught, ringing tools. SHAPE: 20x15m court; east stair rises3m to roof terrace; west canal stair, north Doria workshop, south6m alley. LIVES: glassworkers including Doria. HANDS: cooling trough, sand cart, tongs, ladders, shutters. COSTS: public access; active furnaces are real hazards only on contact. TURNS: shutters shelter civilians; cart blocks alley; canals provide escape. KEY: furnacelight beneath blue night.'),
 'walk':('The Glasswalk','rooftops','Tiled working roofs and a stone pedestrian bridge above a narrow canal, adjoining Furnace Court.','SENSE: claws ring on tile, canal water against stone. SHAPE: east stair ->12x8m terrace ->12m bridge2mwide/3mhigh -> west storehouse landing/downstair/roofladder; waist-high parapet. Canal4mwide/2mdeep, ladder each side. HANDS: chimneys, shutters, bridge rail. COSTS: exposed crossing with solid footing; ordinary movement no roll unless contested/rushing hazardous edge. TURNS: blocked bridge leaves canal, roof and stairs. KEY: blue light through moving glass.'),
 'kiln':('The Drowned Kiln','workshop','Partially flooded former glassworks island; Senn holds yard and dock while Kest occupies the annealing room.','SENSE: wet ash, ropes creak under loading platform. SHAPE: upperyard18x12m, streetgate, shoreladder, loadingplatform, annealingroom with inwardlock and crawlable old flue. Lowerroom waistdeep with canalexit. COURT distance10minwalk/5minboat. LIVES: finite company guards, Kest, waiting pilot. HANDS: crates, padded cradles, sample jars, sliding door, mooring ropes. COSTS: private worksite; no automatic wards. TURNS: cargo can be detained or moved, room can be approached through gate/shore/flue. KEY: a dead furnace with live cargo.')}
for key,(name,typ,desc,card) in locs.items():
 lid=new(key,'add-location','--campaign',C,'--name',name,'--type',typ,'--description',desc,'--narrative',desc)
 cli('update-location','--id',lid,'--staging-notes',card)

def hp(con,siz,bonus=0):
 b=(con+siz-1)//5
 return [{'name':n,'range':r,'hp':h+bonus,'ap':0} for n,r,h in [('Right Leg','01-03',b+1),('Left Leg','04-06',b+1),('Abdomen','07-09',b+2),('Chest','10-12',b+3),('Right Arm','13-15',b),('Left Arm','16-18',b),('Head','19-20',b+1)]]
def score(want,ought,driver,tactics,rhythm):
 return {'want':want,'ought':ought,'driver':driver,'stated_reason':want,'focus':'promotion','status':{'Nimras':'Unknown visiting professional; no awareness of his thoughts or commission until learned.'},'tactics':tactics,'when_lied_to':'miss','blind_spot':'Trusts familiar professional habits.','rhythm':rhythm,'observed':[]}
def person(name,stats,skills,weapons,notes,sc,rank=None):
 d={'name':name,'stats':stats,'skills':skills,'attributes':{'action_points':3 if rank==2 else 2,'magic_points':stats['POW'],'luck_points':0,'movement':'20 feet'},'hit_locations':hp(stats['CON'],stats['SIZ'],1 if rank else 0),'equipment':weapons,'notes':notes,'score':sc}
 if rank:d.update({'class':'Magic-User','rank':rank,'prepared_spells':{'0':['Read Magic','Repair','Protection','Avert','Magic Tricks'],'1':['Shield','Detect Magic','Invisibility','Magic Missile','Web'],'2':['Dispel Magic','Locate Object','Mirror Image']},'sorcery_spells':['Read Magic','Repair','Protection','Avert','Magic Tricks','Shield','Detect Magic','Invisibility','Magic Missile','Change Appearance','Dispel Magic','Locate Object','Web','Mirror Image']})
 return d
common={'STR':12,'CON':12,'SIZ':12,'DEX':12,'INT':12,'POW':11,'CHA':11}
profiles={
 'kest':person('Sivren Kest',{**common,'INT':16,'POW':16,'DEX':13},{'Arcane Casting':80,'Arcane Knowledge':80,'Willpower':75,'Craft (Glass bindings)':95,'Mechanisms':75,'Evade':55,'Stealth':55,'Perception':65,'Influence':45,'Insight':50},[{'name':'Dagger','damage':'1d4','size':'S'},'Service key','Original binding notebook'],'Independent arcane artificer; apprentice of no newly invented city institution. Clipped technical speech, stained hands, battered spectacles. Full selected plan in Glass Hounds GM lore.',score('Recover original research and end human hunting conversion','Warn the people endangered by his invention','Professional independence',['Propose safe dismantling','Trade service key for original notebook','Refuse destruction of originals','Defend escape and surrender before fatal injury'],'Clipped technical statements, impatient with praise.'),2),
 'senn':person('Captain Mara Senn',{**common,'STR':13,'CON':14,'DEX':14,'INT':14,'CHA':14},{'Company Arms':70,'Evade':60,'Endurance':65,'Willpower':60,'Influence':65,'Deceit':55,'Insight':60,'Perception':65,'Boating':65,'Streetwise':65},[{'name':'Shortsword','damage':'1d6','size':'M'},'Padded coat','Brass command whistle','Chest key'],'Independent recovery captain. Cropped hair, well-cut patched coat, short offers and dockside humour. Commands exactly five other company members; no institutional immunity.',score('Make a profitable exit with saleable constructs','Honour the limited demonstration agreement','Refusal to become an unpaid retainer',['Offer purchase','Leverage custody','Order restraint','Withdraw if outmatched'],'Short plain offers; dockside humour.')),
 'doria':person('Doria Flint',{**common,'STR':13,'DEX':15,'INT':14,'CHA':13},{'Craft (Glassworking)':85,'Mechanisms':60,'Perception':60,'Influence':55,'Insight':50,'Evade':45,'Athletics':50},[{'name':'Kiln tongs','damage':'1d4','size':'M'},'Leather apron','Glass cutters','Kiln receipt'],'Adult master glassblower of Furnace Court; no spellcasting. Burn mark at wrist; blunt and warm. Gives useful evidence freely when danger is clear.',score('Keep workers safe and paid','Disclose who ordered the hunting bodies','Responsibility for the work of her hands',['Help immediate safety','Show receipts and name workshop','Ask compensation for further labour','Shut workshop against threats'],'Warm blunt speech, everyday craft idiom.')),
 'neral':person('Neral Brinehand',{**common,'STR':14,'DEX':14,'INT':14,'CHA':12},{'Boating':80,'Swim':90,'Navigation':75,'Insight':60,'Perception':65,'Influence':55,'Evade':50,'Spear':55,'Willpower':60},[{'name':'Spear','damage':'1d8','size':'L'},'Copper earrings','Pilot contract'],'Independent merfolk pilot; no Council mandate, no spell repertoire granted. Dark green tail; direct questions. Prior working introduction to Thessa; cannot speak for her.',score('Keep an independent pilot business','Refuse transport of unwilling living captives','Never become a surface patron’s servant',['Inspect questionable cargo','Offer lawful passage','Refuse breached contract','Depart under threat'],'Direct complete questions, no water metaphors.'))}
profiles['neral']['hit_locations']=[{'name':n,'range':r,'hp':h,'ap':0} for n,r,h in [('Tail','01-06',6),('Abdomen','07-09',6),('Chest','10-12',7),('Right Arm','13-15',4),('Left Arm','16-18',4),('Head','19-20',5)]]
profiles['neral']['attributes']['movement']='Swim40 feet; land5 feet with support'
for key,name in [('iven','Iven Toll'),('bess','Bess Arl'),('pell','Pell Dask'),('jory','Jory Fen'),('nel','Nel Aster')]:
 profiles[key]=person(name,common,{'Company Arms':50,'Athletics':50,'Evade':45,'Perception':50,'Insight':40,'Willpower':40,'Boating':50,'Brawn':50,'Deceit':35},[{'name':'Cudgel','damage':'1d6','size':'M'},'Rope','Net']+(['Brass command whistle'] if key=='iven' else []),'Paid recovery company member; short practical speech, wants wages and survival. Will retreat or surrender when defeated; no fanatic allegiance.',score('Earn wages and get home','Avoid unnecessary injury','Ordinary livelihood',['Demand space','Attempt restraint under orders','Defend self','Surrender when defeated'],'Short workaday sentences.'))
for key,p in profiles.items():
 if key not in M:
  path=ROOT/('glass-hounds-'+key+'.json');path.write_text(j(p))
  remember(key,cli('import-characters','--campaign',C,'--type','npc','--file',path)['imported'][0]['id'])
 cli('update-character','--id',M[key],'--actor-notes','LOOKS: '+p['notes']+' CORE/WANTS: '+p['score']['want']+'. PRESSURE: follows tactics in score; no lie detection. KEY: '+p['score']['rhythm'])
 cli('move-character','--id',M[key],'--location',M['court'] if key in ['doria','iven','bess'] else M['kiln'])
# Physical construct sheets; exact locations and bounded powers live in GM lore.
for i in range(1,5):
 key='hound'+str(i)
 if key in M:continue
 p={'name':'Glass Hound '+str(i),'stats':{'STR':14,'CON':10,'SIZ':8,'DEX':15,'INT':3,'POW':10,'CHA':1},'skills':{'Bite':55,'Evade':45,'Athletics':65,'Perception':65,'Endurance':50,'Willpower':35,'Track':60},'attributes':{'action_points':2,'initiative_bonus':9,'damage_modifier':'+0','magic_points':0,'luck_points':0,'movement':'30 feet'},'hit_locations':[{'name':n,'range':r,'hp':h,'ap':1} for n,r,h in [('Rear Right Leg','01-03',3),('Rear Left Leg','04-06',3),('Hindquarters','07-09',5),('Chest','10-12',6),('Front Right Leg','13-15',3),('Front Left Leg','16-18',3),('Head','19-20',4)]],'equipment':[{'name':'Bite','damage':'1d6','size':'S'}],'notes':'Physical animated glass hunting construct. Exact scenario rules in Glass Hounds GM lore. No spell immunity or electricity resistance. Removable tracking throat. No free attacks or pounce.','construct_state':{'animated':i<3,'sample':'Rennic residue' if i==1 else None,'standing_order':'Retrieve Vaur satchel' if i==1 else 'Hold','finite_body_number':i}}
 path=ROOT/('glass-hounds-'+key+'.json');path.write_text(j(p))
 remember(key,cli('import-characters','--campaign',C,'--type','creature','--file',path)['imported'][0]['id'])
 cli('move-character','--id',M[key],'--location',M['walk'] if i==1 else M['kiln'])
# Repair Vaur's rejected plot-specific portrayal, retaining his approved abilities.
vaur=cli('get-character','--campaign',C,'--id',V)['character']
sc=score('Stop the conversion of salvage constructs into mage hunters','Return the fellowship manuscript when recalled','Make his experience useful beyond other people’s errands',['Explain plainly','Ask bounded help','Hand over book and offer testimony','Defend only against actual unlawful violence'],'Plain irreverent replies; affectionate teasing with old pupils.')
sc['status']={'Nimras':'Respected former pupil now independent; no foreknowledge of his decisions.'};sc['observed']=[]
cli('update-character','--id',V,'--narrative','Former teacher of Nimras and experienced mage hunter. Retained the fellowship manuscript beyond his loan to assist Kest in disabling hunting constructs; motive does not excuse breach. No water-survey purpose, possession or compulsory betrayal.','--equipment',j(['Weathered travelling coat','Staff','Satchel containing The Pursuit and Severance of Bound Workings']),'--extras',j({'score':sc,'doing':{'goal':'End living-caster hunts and resolve manuscript custody','next':'Reach safety from Hound I','where':M['walk']}}),'--actor-notes','LOOKS: lean middle-aged traveller, close-cropped grey hair, repaired coat. CORE: practical affectionate teacher who acts before asking permission. WANTS: help Kest stop dangerous conversion, then settle fellowship obligations. PRESSURE: terse, seeks real exits. KEY: plain irreverent answers, no riddles or water-survey explanations.')
cli('move-character','--id',V,'--location',M['walk'])
nim=cli('get-character','--campaign',C,'--id',N)['character'];gear=nim.get('myth-equipment-json',[])
clean=[g for g in gear if not any(w in j(g).lower() for w in ['survey','reel','rennic’s note','rennic\u2019s note','landing sketch'])]
if clean!=gear:cli('update-character','--id',N,'--equipment',j(clean))
cli('move-character','--id',N,'--location',M['court'])
# Persist complete selected design in DB, not only local notes.
plan=(ROOT/'glass-hounds-gm.md').read_text()
lore=new('gm_lore','add-lore','--campaign',C,'--title','Glass Hounds: selected adventure and finite operations','--category','scenario','--visibility','gm','--summary','Nimras’s chosen pursuit adventure; full operations, map, asset limits, creature rules and outcomes.','--narrative',plan,'--about',','.join([N,V]+[M[k] for k in ['kest','senn','doria','neral','court','walk','kiln']]))
new('reset_event','log-event','--campaign',C,'--type','gm-note','--visibility','meta','--summary','Player chose Glass Hounds. Failed surveying episode retracted; replacement opening at unchanged d6/night. Approved character, fellowship commission and Purewater history preserved.','--narrative','Explicit OOC replacement. Survey-only events/facts are retired with audit preserved. No shared clock rewind; no new resource refresh, purchases or damage. Whole selected design stored in '+lore+'. Unchosen candidates are not live.','--involves',','.join([N,V,VEY]))
# Current facts and restricted knowledge.
fact('premise','Rennic Vaur retained the fellowship manuscript The Pursuit and Severance of Bound Workings beyond his loan and came to Purewater to help Kest disable constructs converted to hunting living casters.',[V,M['kest']],[V,M['kest']])
fact('company_assets','Senn commands five other recovery workers; four completed hounds exist, with two additional inert bodies at the Drowned Kiln. No replacements exist.',[M['senn'],M['kest'],M['kiln']],[M['senn'],M['kest']])
fact('transport','Senn hired Neral Brinehand to pilot construct cargo from the Drowned Kiln; his contract excludes unwilling living captives. Planned loading begins d7/dawn and departure is conditional on loading and his agreement.',[M['senn'],M['neral'],M['kiln']],[M['senn'],M['neral']])
fact('doria_route','Doria Flint made glass bodies for Sivren Kest; her receipt gives the Drowned Kiln address. She knows the court and workshop, not the manuscript shutdown method.',[M['doria'],M['kest'],M['kiln']],[M['doria'],M['kest']])
fact('senn_sample','Senn sent Iven Toll and Bess Arl with Hound I and Vaur’s demonstration residue to recover his manuscript satchel. The handlers know that assignment, not every rival’s plan.',[M['senn'],M['iven'],M['bess'],M['hound1'],V],[M['senn'],M['iven'],M['bess']])
fact('vey_lead','Oren Vey directed Nimras to Furnace Court to find Rennic Vaur. This replaces the rejected market-survey lead.',[N,VEY,V,M['court']],[N,VEY],'told')
# Agendas and executable pending operations.
for key,holder,title,goal,clock in [('senn_agenda','senn','Sell the hunting pack','Secure control, load surviving bodies, depart and complete a real sale',4),('kest_agenda','kest','End the hunting conversion','Contact an ally, recover control and dismantle the human-hunting conversion',3),('vaur_new_agenda',None,'Settle the missing teacher’s commission','Make evidence accessible, settle manuscript custody and arrange return/report',3)]:
 new(key,'add-agenda','--campaign',C,'--holder',M[holder] if holder else V,'--title',title,'--goal',goal,'--clock',clock,'--priority','3','--narrative','Full executable operations in GM lore '+lore+'. Advance only for completed concrete objectives. No automatic success or replacement resources. Dates are attempts, not guaranteed events.')
ops=[('g1','senn_agenda','Hound on the Glasswalk','d6/night','walk',['hound1','iven','bess'],'G1: Retrieve Vaur’s satchel. Opening is a threat frame, no attack resolved. Resolve all contested movement, commands and combat honestly. No automatic Vaur escape or capture.'),('g2','kest_agenda','Kest seeks an ally','d7/dawn','kiln',['kest'],'G2: If still isolated with an exit, Kest attempts to send a service-key offer through Doria. Contested exit uses Stealth55 vs actual guard Perception50. Contact can occur early by PC approach. No free teleport or fixed injury.'),('g3','senn_agenda','Load the surviving pack','d7/dawn','kiln',['senn','neral','nel'],'G3: Attempt loading only actual surviving bodies and notes. Requires crew, lighter, physical access and Neral contract compliance. Informed opposition can prevent it. Roll actual contested attempt once; update finite inventory and dependent operations.'),('g4','senn_agenda','Outward passage','d7/day','kiln',['senn','neral'],'G4: Attempt departure only if G3 actually secured loading and a willing pilot. No automatic export. Opponents with learned route can intervene. Losing boat or crew cancels until recorded replacement, alternate pilot costs2GP and1watch.'),('g5','vaur_new_agenda','Book and teacher in whose custody','d8/day','court',[],'Recovery opportunity if commission unresolved. May occur immediately at opening or any earned contact; no forced attendance or delayed handover. Book and teacher may be recovered early. Client offers8GP on completed live return; no payment before fulfilment.')]
for key,ag,title,when,loc,cast,desc in ops:
 args=['add-beat','--campaign',C,'--agenda',M[ag],'--title',title,'--when',when,'--at',M[loc],'--cast',','.join([M[c] for c in cast]+([V] if key in ['g1','g5'] else [])),'--summary',desc,'--narrative',desc+' Full prerequisites, warnings, counterplay and outcomes: '+lore,'--onscreen-if','Only if Nimras is actually present or can witness the event. Evaluate real prerequisites; offscreen opposition is rolled and knowledge travels by actual witnesses.']
 new(key,*args)
# Useful finite-inventory ledger, not omniscient fiction.
cli('update-character','--id',M['senn'],'--extras',j({'assets':{'company_total':6,'pay_chest_gp':18,'completed_hounds':4,'inert_bodies':2,'blank_lenses':4,'whistles_total':4,'whistles_senn':1,'whistles_iven':1,'whistles_chest':2,'replacement_bodies_days':3},'doing':{'goal':'Recover manuscript then sell surviving pack','next':'Await actual return of retrieval team; load at dawn if resources survive','where':M['kiln']}}))
# Opening knowledge is exactly what is visible, not the private design.
opening='Claws ring against roof tiles above Furnace Court. From the foot of the stair you see Rennic eighteen metres away, crossing a narrow stone bridge with a clasped satchel at his hip. A dog-sized creature of clear glass follows him, blue light burning inside its throat. Rennic spots you. “Nimras! Mind the thing behind me!”'
fact('opening_visible','At Furnace Court during d6/night, Nimras sees Rennic Vaur on the Glasswalk bridge about18m away with a clasped satchel, followed8m behind by a dog-sized clear glass creature with a glowing blue throat. Nimras is at the foot of the east stair; no attack or spell has yet been resolved.',[N,V,M['hound1'],M['court'],M['walk']],[N],'witnessed')
new('opening_event','log-event','--campaign',C,'--type','scene','--visibility','played','--summary','Glass Hounds opens at Furnace Court: Nimras sees Rennic on the bridge pursued by a glass creature; Rennic calls to him. No action resolved yet.','--narrative',opening,'--involves',','.join([N,V,M['hound1'],M['court'],M['walk']]))
cli('update-campaign','--campaign',C,'--arc-file',str(ROOT/'glass-hounds-arc.md'),'--played',N)
cli('set-scene','--campaign',C,'--scene','Glass Hounds selected, d6/night, session6. Nimras at foot of Furnace Court east stair. Vaur18m away on Glasswalk bridge, HoundI8m behind Vaur; no attack/cast resolved, player action pending. Doria north workshop; Iven/Bess south alley not yet seen. Prepared spell and resource state unchanged. Full scenario and exact maps/powers/finite assets in GM lore '+lore+'. Do not resume retracted water-survey episode. Opening NPC line: Nimras! Mind the thing behind me!')
# Readback verifies write effects and invariant player state.
after=cli('get-context','--campaign',C,'--compact'); n2=cli('get-character','--campaign',C,'--id',N)['character']
for f in ['myth-characteristics-json','myth-skills-json','myth-hit-locations-json','myth-magic-current','myth-luck-current','myth-fatigue']:
 assert n2.get(f)==nim.get(f),f
assert after['world_clock']=='d6/night'
checks=cli('check-consistency','--campaign',C)
(ROOT/'glass-hounds-readback.json').write_text(j({'context':after,'nimras':n2,'consistency':checks}))
for key in ['g1','court','walk']:
 r=cli('brief','--id',M[key]);(ROOT/('glass-brief-'+key+'.json')).write_text(j(r))
(ROOT/'glass-brief-vaur.json').write_text(j(cli('brief','--id',V)))
(ROOT/'glass-nimras-view.json').write_text(j(cli('character-view','--campaign',C,'--id',N,'--compact')))
remember('activated',True)
print(j({'activated':True,'ids':M,'clock':after['world_clock'],'invariants':'Approved stats, skills, HP, MP, Luck and fatigue unchanged','consistency':checks}))
