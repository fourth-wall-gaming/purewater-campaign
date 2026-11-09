"""Persist the player-reviewed investigation/agent revision through the game CLI."""
import json,pathlib,subprocess,os,re
D=pathlib.Path(__file__).resolve().parent;R=D.parent.parent
C='myth-campaign-purewater-s1';N='myth-char-4fc52ae14026';V='myth-char-1aa1d6892d3a';VEY='myth-char-fd2973412ca1'
E='/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
base=json.loads((D/'glass-hounds-ids.json').read_text());P=D/'glass-hounds-v2-ids.json';M=json.loads(P.read_text()) if P.exists() else {}
def cli(*a):
 r=subprocess.run(['uv','run','-q','--project',E,'python',E+'/mythras_gm.py',*map(str,a)],capture_output=True,text=True,env={**os.environ,'MYTHRAS_CAMPAIGN':C,'MYTH_CAMPAIGN':C})
 if r.returncode:raise RuntimeError(r.stdout+r.stderr)
 d=json.loads([s for s in r.stdout.splitlines() if s.startswith('{')][-1]);assert d.get('success'),d
 return d
def save(k,v):M[k]=v;P.write_text(json.dumps(M,indent=2)+'\n');return v
def new(k,*a):return M[k] if k in M else save(k,cli(*a)['id'])
def j(x):return json.dumps(x,ensure_ascii=False)
def fact(key,statement,knowers,about=None,status='established',source='witnessed'):
 a=['add-fact','--campaign',C,'--statement',statement,'--status',status,'--about',','.join(about or knowers)]
 if status=='established':a+=['--when','d6/night','--learned-by',','.join(knowers),'--source',source]
 return new(key,*a)
if M.get('ready'):raise SystemExit('Revision already saved; use live context for play.')
ctx=cli('get-context','--campaign',C,'--compact');assert ctx['world_clock']=='d6/night'
n0=cli('get-character','--id',N,'--campaign',C)['character'];save('before_pc',n0)
# Withdraw the rejected rooftop opening, both event and all its knowledge.
cli('retire-canon','--id',base['opening_event'],'--status','retracted')
for f in [base['opening_visible'],base['vey_lead']]:
 know=cli('who-knows','--campaign',C,'--fact',f)['knowers']
 for e in know:cli('forget','--knower',e['knower'],'--fact',f)
 cli('supersede-fact','--id',f,'--campaign',C)
for k in ['g1','g2','g3','g4','g5']:cli('revise-beat','--id',base[k],'--status','cancelled','--summary','Superseded by player-reviewed Glass Hounds v2 situation cards; do not resume the immediate rooftop opening.')
locdata={
 'arrival':('West Lantern Landing','public-quay','Public ferry landing at the edge of the Merchant Quarter, with boat berths, unloading platform and covered route-board.','SENSE: wet rope, hulls knocking, lamps in canal water. SHAPE: ferry steps to open landing, covered route-board and public footbridge exit; ordinary boat berths. HANDS: mooring post, route-board marking High Isle and House of Small Windows water-stair. COSTS: ordinary public landing; no compulsory fee or confrontation. TURNS: visitors can arrange transport or approach by footbridges. KEY: a new city opens across black water.'),
 'rooms':('Three Steps Rooms','lodging','Canal-side boarding house where Rennic rented a room before withdrawing to shelter.','SENSE: cooking onions, damp wool, footsteps overhead. SHAPE: common room, upper stair, rear service landing; guest room has lockable door, canal window over rope-work awning. HANDS: Elna spare key; receipt from Doria and binding sketch in Rennic room. COSTS: guest privacy; hirelings require actual access. TURNS: window, stair and rear landing permit escape or flank. KEY: an occupied lodging in a city of strangers.'),
 'loft':('Sailmakers’ Loft','loft','Disused sail store above a working chandlery, offered by Doria to Rennic as temporary shelter.','SENSE: canvas, tar, block-and-tackle creak. SHAPE: main stair, loading hatch, roof hatch, canal rope ladder; cloth bales provide cover. HANDS: worktable, lamp, manuscript and Kest letter while Rennic holds them. COSTS: private shelter, ordinary access and consent. TURNS: several exits; no scripted collapse, explosion or ambush. KEY: folded sails above the water.')}
for key,(name,typ,desc,card) in locdata.items():
 lid=new(key,'add-location','--campaign',C,'--name',name,'--type',typ,'--description',desc,'--narrative',desc)
 cli('update-location','--id',lid,'--staging-notes',card)
# Prepared new cast: an innkeeper and the actual buyer, no extra enemy army.
for key,name,stats,skills,notes,want,ought,tactics in [
 ('elna','Elna Pike',{'STR':10,'CON':12,'SIZ':11,'DEX':12,'INT':14,'POW':12,'CHA':14},{'Influence':60,'Insight':65,'Willpower':55,'Perception':60,'Streetwise':65,'Evade':40},'Adult keeper of Three Steps Rooms; plain-spoken, commercially shrewd, wants safe guests and a solvent lodging. Does not hide useful leads behind riddles.','Protect guests and keep the lodging open','Protect guest privacy',['Ask business plainly','Refuse intrusive strangers','Seek help when threatened','Retreat from lethal force']),
 ('varro','Leth Varro',{'STR':10,'CON':12,'SIZ':12,'DEX':13,'INT':15,'POW':13,'CHA':15},{'Influence':75,'Commerce':80,'Insight':65,'Deceit':65,'Willpower':60,'Perception':55,'Evade':50,'Dagger':45},'Itinerant private recovery broker. Polished patient speech, treats coercive work as a purchase. No Crown warrant, personal guards or secret command over Purewater masters.','Buy a proven means of capturing resistant practitioners','Refuse trade in coercive capture',['Ask for the demonstration','Withhold payment without proof','Offer terms for his own safety','Flee or surrender rather than die'])]:
 if key not in M:
  sheet={'name':name,'stats':stats,'skills':skills,'attributes':{'action_points':2,'luck_points':0,'magic_points':stats['POW']},'equipment':[{'name':'Dagger','damage':'1d4','size':'S'}] if key=='varro' else [],'notes':notes,'score':{'want':want,'ought':ought,'driver':'Independent livelihood and personal control','stated_reason':want,'tactics':tactics,'when_lied_to':'miss','rhythm':'Plain practical replies.' if key=='elna' else 'Polished patient questions; offers prices rather than speeches.','observed':[]}}
  p=D/('glass-v2-'+key+'.json');p.write_text(j(sheet));save(key,cli('import-characters','--campaign',C,'--type','npc','--file',p)['imported'][0]['id'])
 cli('update-character','--id',M[key],'--actor-notes','LOOKS: '+notes+' CORE/WANTS: '+want+'. PRESSURE: '+tactics[-1]+'. KEY: answers direct questions, no automatic lie detection.')
cli('move-character','--id',M['elna'],'--location',M['rooms'])
# Varro has not entered Purewater; an offstage staging record prevents false local presence.
new('outer_berth','add-location','--campaign',C,'--name','Varro’s outward anchorage','--type','offstage-berth','--description','Outside the current city scene; Varro waits aboard hired ordinary transport for the planned d8/day appointment. No local soldiers.')
cli('move-character','--id',M['varro'],'--location',M['outer_berth'])
cli('move-character','--id',N,'--location',M['arrival']);cli('move-character','--id',V,'--location',M['loft'])
for k in ['iven','bess']:cli('move-character','--id',base[k],'--location',M['rooms'])
for k in ['hound1','hound2','hound3','hound4']:cli('move-character','--id',base[k],'--location',base['kiln'])
cli('update-character','--id',base['hound1'],'--extras',j({'construct_state':{'animated':True,'sample':'Vaur demonstration residue, expires at end of d6/night','standing_order':'Hold at Kiln; no deployment without actual trail','finite_body_number':1}}))
# Intentions and location are not private thoughts exposed to the player.
activities=[(V,'Disable Senn’s hunting conversion and settle manuscript custody','Study accessible bindings in shelter; meet Doria at dawn',M['loft']),
 (base['senn'],'Capture Rennic, obtain the shutdown book and sell proven capture capacity','Await lodging-search report; then deploy surviving resources',base['kiln']),
 (base['kest'],'Preserve original salvage work and end coerced human hunting','Seek Doria through an actual messenger or exit',base['kiln']),
 (base['doria'],'Protect workers and help Rennic reach Kest','Keep workshop open and expect Rennic at dawn',base['court']),
 (base['iven'],'Earn company wages by locating Rennic','With Bess seek access to the former rented room',M['rooms']),
 (base['bess'],'Earn wages and avoid being caught for a violent search','Help Iven search only if access is secured',M['rooms']),
 (M['elna'],'Keep guests safe and lodging solvent','Require an explanation before giving access to Rennic’s room',M['rooms']),
 (M['varro'],'Buy a demonstrated means of taking unwilling casters','Wait for Senn’s invitation and proof before travelling to payment',M['outer_berth'])]
for cid,goal,nxt,loc in activities:cli('set-doing','--id',cid,'--campaign',C,'--goal',goal,'--next',nxt,'--where',loc)
cli('update-character','--id',base['iven'],'--description','Local hired blade and hound handler in Senn’s six-person company. Assigned room search with Bess; knows only orders and reports he receives.','--skills',j({'Stealth':45}))
cli('update-character','--id',base['bess'],'--description','Local burglar and intimidation specialist in Senn’s six-person company. Assigned room search with Iven. Wages and survival, not fanatic allegiance.','--skills',j({'Stealth':45,'Mechanisms':55}))
cli('update-agenda','--id',base['senn_agenda'],'--goal','Find and capture Rennic, secure book and manufacture, demonstrate involuntary capture and obtain Varro payment','--narrative','V2 active antagonist. Six company people total, four completed hounds and two inert shells. Orders require information; search report before retargeting. No automatic trace or capture. Detail in v2 GM lore.')
cli('update-agenda','--id',base['vaur_new_agenda'],'--goal','Reach Kest, stop human-hunting conversion, then settle book custody and return','--narrative','Rennic knows his refuge, Doria, Kest and Senn, not buyer or Nimras arrival. Can hand book over or return early; no forced escape. V2 situation cards govern.')
# Each starting fact is only held by people with a recorded route.
fact('arrival_brief','Nimras arrives in Purewater for the first time at West Lantern Landing during d6/night. His fellowship introduction names Oren Vey at the House of Small Windows, High Isle. He is a freelance mage hunter seeking Rennic alive and the entrusted manuscript; no local warrant or state employment is supplied.',[N],[N,VEY,M['arrival']],'established','told')
fact('old_lodging','Rennic rented a room at Three Steps Rooms and left carrying his satchel, with rent paid through the next day. He instructed Elna to direct a trusted caller to Doria Flint.',[V,M['elna']],[V,M['elna'],M['rooms']])
fact('vey_address','Rennic’s earlier correspondence gave Oren Vey the address Three Steps Rooms. Vey does not know Rennic’s current shelter or Senn’s capture business.',[VEY],[VEY,M['rooms']],'established','told')
fact('shelter','Doria offered Rennic temporary shelter in Sailmakers’ Loft. He is there with the fellowship manuscript and plans to meet her at dawn to seek access to Kest.',[V,base['doria']],[V,base['doria'],M['loft']])
fact('teacher_knowledge','Kest’s letter told Rennic that Senn had converted salvage constructs to hunting living casters. Rennic knows Senn’s name, Kest’s appeal, Doria’s workshop, the Kiln entrance and the manuscript’s shutdown instructions; he does not know buyer, current crew positions or Nimras’s arrival.',[V],[V,base['kest'],base['senn']],'established','told')
fact('training','Rennic taught Nimras a warning convention during their earlier work: three chalk strokes under a latch mean an appointment is unsafe. No such mark has yet been observed in Purewater.',[N,V],[N,V],'established','told')
fact('senn_orders','Senn assigned Iven Toll and Bess Arl to find Rennic or a satchel lead by searching his former room at Three Steps Rooms. They have not gained entry or reported a result. Senn does not know the Sailmakers’ Loft address or Nimras’s arrival.',[base['senn'],base['iven'],base['bess']],[base['senn'],base['iven'],base['bess'],M['rooms']],'established','told')
fact('buyer_terms','Leth Varro offered Senn10GP deposit, included in her18GP chest, and40GP balance for a working pack with reproducible capture method, conditional on a demonstration against an unwilling active caster. Payment is planned for d8/day only if an invitation and demonstration arrangement survive. Varro has no local guards or warrant.',[base['senn'],M['varro']],[base['senn'],M['varro']],'established','told')
fact('senn_report','Senn has received a credible report identifying Nimras as an obstacle and explaining where her observer can recognise him.',[],[base['senn'],N],status='not-yet-true')
# Retire the old claim of an already-deployed hound, including all obsolete holders.
for key in ['senn_sample','transport']:
 f=base[key]
 for e in cli('who-knows','--campaign',C,'--fact',f)['knowers']:cli('forget','--knower',e['knower'],'--fact',f)
 cli('supersede-fact','--id',f,'--campaign',C)
fact('new_transport','Senn booked Neral to pilot construct cargo from the Drowned Kiln, with proposed loading d8/dawn. His agreement excludes unwilling living captives. No loading, departure or consent to captive transport has occurred.',[base['senn'],base['neral']],[base['senn'],base['neral'],base['kiln']],'established','told')
cli('set-knowledge','--knower',V,'--subject',base['kest'],'--campaign',C,'--depth','knows','--route','told','--note','Kest warned me that Senn is turning his salvage invention against living casters; the fellowship would probably recall the book before I could help. That expectation is my judgement, not their stated policy.','--attitude','Help Kest, then justify my unauthorised retention of the manuscript.','--since','91')
# Separate surveillance agenda is gated by the captain actually receiving a report.
new('counter_agenda','add-agenda','--campaign',C,'--holder',base['senn'],'--title','Identify and obstruct the interfering mage','--goal','Learn Nimras’s contacts and isolate him for restraint or recovery','--clock','3','--status','dormant','--narrative','May wake only when Senn actually learns the report fact. One or two surviving local blades, never extra troops. Tail and ambush require successful actual positioning and information.')
cli('require-fact','--agenda',M['counter_agenda'],'--fact',M['senn_report'])
plan=(D/'glass-hounds-situations-v2.md').read_text();legacy=(D/'glass-hounds-gm.md').read_text()
cli('update-lore','--id',base['gm_lore'],'--summary','Glass Hounds v2: outsider agent investigation, active adversary, knowledge and playable situations. V2 overrides first-draft opening and operations.','--narrative',plan+'\n\n## Original mechanical reference (v2 above takes precedence)\n\n'+legacy)
# Cards saved individually, not solely in a GM document.
cards=re.findall(r'^### ([ABC]\d) — (.+?)\n\n(.*?)(?=\n### |\n## Act transitions)',plan,re.M|re.S)
assert len(cards)==9,len(cards)
settings={'A1':(base['senn_agenda'],M['rooms'],[base['iven'],base['bess'],M['elna']],'d7/dawn'),
 'A2':(M['counter_agenda'],M['rooms'],[base['iven']],'d7/dusk'),
 'A3':(base['senn_agenda'],base['court'],[base['iven'],base['bess'],base['doria']],'d7/day'),
 'A4':(base['vaur_new_agenda'],M['loft'],[V],'d7/dawn'),
 'B1':(base['senn_agenda'],base['court'],[base['senn'],base['hound1']],'d7/dawn'),
 'B2':(base['kest_agenda'],base['kiln'],[base['kest'],base['pell'],base['jory']],'d7/dawn'),
 'B3':(base['senn_agenda'],base['kiln'],[base['senn'],M['varro']],'d7/day'),
 'C1':(base['senn_agenda'],base['kiln'],[base['senn'],base['neral'],base['nel']],'d8/dawn'),
 'C2':(base['senn_agenda'],base['kiln'],[base['senn'],M['varro']],'d8/day')}
for key,title,body in cards:
 ag,loc,cast,when=settings[key]
 new(key,'add-beat','--campaign',C,'--agenda',ag,'--title',key+' '+title,'--when',when,'--at',loc,'--cast',','.join(cast),'--summary',body.split('.')[0]+'.','--narrative',body,'--onscreen-if','Only actual presence or earned contact. Card is an attempt, not an outcome or teleport. Earliest useful contact can occur before listed review window. Evaluate actor knowledge, location, surviving assets and travel; skip or revise impossible attempts.')
# Reusable method in the live game's GM reference as well as workspace discovery.
new('method_lore','add-lore','--campaign',C,'--title','Reusable adventure construction after pitch selection','--category','gm-method','--visibility','gm','--summary','Cast, active antagonists, knowledge, acts, dangerous playable situations and model verification.','--narrative',(D/'adventure-construction-method.md').read_text())
cli('update-campaign','--campaign',C,'--arc-file',str(D/'glass-hounds-arc.md'),'--played',N)
new('review_event','log-event','--campaign',C,'--type','gm-note','--visibility','meta','--summary','Player approved investigative adversarial revision and fantasy-agent tone. Nimras’s first arrival replaces the rooftop opening; knowledge, cast, operations and reusable method saved. Shared d6/night and PC resources stand.','--narrative','V2 is authoritative over original operations. All previously described rooftop action is withdrawn, not an in-world memory. No extra character power, warrant or state allegiance. OOC review consumes no time. Situation cards A1–C2 contain contingent encounters.','--involves',','.join([N,V,base['senn']]))
cli('set-scene','--campaign',C,'--scene','Glass Hounds v2. d6/night, session6. Nimras arrives in Purewater for the FIRST TIME at West Lantern Landing, carrying fellowship introduction to Oren Vey at House of Small Windows, High Isle. Agent-style freelance mage hunter, travelling-magician cover; no alias or state warrant imposed. Nobody in town met yet. Fellowship recovery commission stands; no rooftop hound seen, no surveying episode. Contact and city route-board provide first leads. PC resources unchanged. Play may begin after preparation verification; current player action pending. GM lore '+base['gm_lore']+' and glass-hounds-situations-v2.md govern.')
# Read live records, never claim setup solely from successful writes.
n1=cli('get-character','--id',N,'--campaign',C)['character']
for f in ['myth-characteristics-json','myth-skills-json','myth-hit-locations-json','myth-magic-current','myth-luck-current','myth-fatigue']:
 assert n0.get(f)==n1.get(f),f
view=cli('character-view','--campaign',C,'--id',N,'--compact');check=cli('check-consistency','--campaign',C);assert check.get('ok'),check
ctx=cli('get-context','--campaign',C,'--compact');assert ctx['world_clock']=='d6/night'
brief=cli('brief','--id',M['arrival']);(D/'glass-v2-arrival-brief.json').write_text(j(brief))
(D/'glass-v2-verification.json').write_text(j({'context':ctx,'pc':n1,'knowledge':view,'check':check,'arrival_brief':brief}))
save('ready',True)
print(j({'ready':True,'cards':[k for k,_,_ in cards],'clock':ctx['world_clock'],'check_ok':check.get('ok'),'arrival_brief':brief,'pc_knowledge':view}))
