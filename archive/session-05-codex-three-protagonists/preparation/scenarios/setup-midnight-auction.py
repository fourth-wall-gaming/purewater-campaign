"""Idempotent preparation of Nimras's selected auction chapter via installed CLI.
Does not accept a contract, deliver the offer, roll dice or advance time.
"""
import json,subprocess,os
from pathlib import Path
W=Path('/Users/gullyburns/Documents/ChatGPT/mythras');E='/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm';C='myth-campaign-purewater-s1';N='myth-char-4fc52ae14026';V='myth-char-fd2973412ca1'
P=W/'docs/scenarios/midnight-auction-ids.json';ids=json.loads(P.read_text()) if P.exists() else {}
def cli(cmd,**kw):
 a=[cmd,'--pc',N]
 if cmd not in ('update-location','join-faction','get-lore','update-lore'):
  a+=['--campaign',C]
 for k,v in kw.items():
  if v is None or v is False:continue
  a.append('--'+k.replace('_','-'))
  if v is not True:a.append(str(v))
 r=subprocess.run(['uv','run','-q','--project',E,'python',E+'/mythras_gm.py',*a],capture_output=True,text=True,env={**os.environ,'MYTHRAS_CAMPAIGN':C})
 if r.returncode:raise RuntimeError(cmd+': '+r.stdout+r.stderr)
 d=json.loads(next(l for l in r.stdout.splitlines() if l.startswith('{')));assert d.get('success'),d;return d

def once(key,cmd,**kw):
 if key not in ids:
  ids[key]=cli(cmd,**kw)['id'];P.write_text(json.dumps(ids,indent=2)+'\n')
 return ids[key]

if __name__=='__main__':
 checkpoint=W/'checkpoints/nimras-auction-before-20261027';checkpoint.mkdir(parents=True,exist_ok=True)
 for name,cmd,kw in [('context','get-context',{'compact':True}),('character','get-character',{'id':N})]:
  f=checkpoint/(name+'.json')
  if not f.exists():f.write_text(json.dumps(cli(cmd,**kw),indent=2))
 clock=cli('get-context',compact=True)['storyline'];assert clock['now']=='d9/dawn' and clock['minute_in_watch']==145,clock
 plan=(W/'docs/scenarios/midnight-exchange-auction-live.md').read_text()
 lore=once('preparation','add-lore',title='Midnight Exchange auction chapter — live preparation',category='scenario-preparation',summary='Selected arc chapter: voluntary Vey appraisal, guarded preview and conditional recovery; finite cast, knowledge and executable operations.',narrative=plan,visibility='gm',about=N)
 locations={
  'barge':('Velvet Hold auction barge','vessel','Seressa Venn auction vessel, moored at Merchant Quarter public quay.','SENSE:beeswax, varnished wood and water on hull. SHAPE:70x20ft,two decks,bow gangplank20ft,stern cargo hatch,shore ladder,30x15ft display,15x10ft office aft. Fourguards total:2entrance,1display,1reserve. HANDS:paired locked cabinets,visible mundane bell-wire across reserve door,mooring ropes,boat access. COSTS:supervised examiner appointment free; private cabins require permission. EXITS:gangplank,shore ladder,cargo hatch. No antimagic, hidden curse or automatic alarm. Register display byday/reserve bynight; ledger office drawer.'),
  'quay':('Velvet Hold public quay','landing','Merchant Quarter public quay and ordinary water-stair serving Velvet Hold.','SENSE:wet stone,boat traffic,voices. SHAPE:30x20ft apron,crate stacks,water-stair,street to either side,barge gangplank. HANDS:crates,rope,skiffs; ordinary pedestrians six at preview peak. EXITS:two waterside passages,stair,gangplank. No automatic ambush or toll.'),
  'depot':('Rusk Ashwick depot','estate depot','Offstage Ashwick estate compound; later travel and encounters require refreshed preparation.','SHAPE:80x50ftcompound,gatehouse,stable loft,rear culvert,office window,locked study. RESOURCES:Rusk,fourretainers,onecart,twohorses,50GPremaining. This is offstage now; no host, possession, completed demonstration or standing raid. Later chapter mechanics/rite require readiness before entry.'),
  'road':('South approach road lodgings','road lodging','Ordinary road lodging on the Purewater approach; Rusk agents stage here before their d10/day arrival.','SENSE:road mud,stable straw. SHAPE:public lodging and ordinary hired boat connection toward Purewater. Actors:Mina/Davren with30GP purchase fund,order and Register sketch. Next travel arrivald10/day; no surveillance of Nimras or guaranteed road violence.')}
 for key,(name,kind,desc,staging) in locations.items():
  loc=once(key,'add-location',name=name,type=kind,description=desc)
  cli('update-location',id=loc,staging_notes=staging)
 for key,name,desc in [('auction_company','Velvet Hold auction business','Independent Venn auction staff; fourguards,captain,two ordinarycrew. No allegiance to Rusk.'),('rusk_company','Rusk recovery venture','Finite derivative estate venture: Rusk,sixretainers total,80GP originally; two agents carry30GP,remaining50GP and fourretainers at Ashwick. No replacement army.'),('marek_company','Marek claimant purchase party','Marek and twoescorts,20GP real purchase funds; independent of Venn and Rusk.')]:
  once(key,'add-faction',name=name,description=desc)
 stats={'STR':12,'CON':12,'SIZ':12,'DEX':12,'INT':12,'POW':10,'CHA':12}
 sword={'name':'Short Sword','damage':'1d6','size':'M','reach':'S','ap':6,'hp':6}
 staff={'name':'Cudgel','damage':'1d6','size':'M','reach':'S','ap':4,'hp':6}
 dagger={'name':'Dagger','damage':'1d4','size':'S','reach':'S','ap':4,'hp':4}
 roles=[
 ('venn','Seressa Venn','she/her','Auction proprietor, independently owns the consignment and controls her staff.',70,55,45,'barge','auction_company',{'goal':'Earn auction proceeds without sacrificing business or crew.','knows':'Clearance chain and ledger; dubious provenance; no host experiment or Nimras identity.','inventory':{'Register':'locked display/reserve','ledger':'office drawer','guards':4,'captain':1,'crew':2},'limits':'Negotiate fair purchase or evidence-backed custody; surrender rather than die for a fee.'}),
 ('marek','Olt Marek','he/him','Independent antiquities buyer acting for a dispossessed claimant.',65,55,45,'quay','marek_company',{'goal':'Acquire authentic Register and trace claimant property.','knows':'Estate seal and duplicate seizure receipt, not demonological purpose or Nimras identity.','funds_gp':20,'escorts':2,'limits':'Evidence, shared purchase or authority acceptable; no public bloodbath over bidding.'}),
 ('rusk','Severin Rusk','he/him','Former estate factor pursuing his own derivative binding venture; no current office over Purewater.',65,60,55,'depot','rusk_company',{'goal':'Recover authentic anchor for later demonstration and patronage.','knows':'Old confiscations,Malrec need,agents orders; no Nimras or his lodging.','funds_gp':50,'allocated_agent_funds_gp':30,'assets':{'retainers_at_depot':4,'travelling_agents':2,'cart':1,'horses':2},'limits':'Buy first; informed witness exposure can motivate lethal order; needs real means/location. Can bargain/flee/surrender. No completed ritual.'}),
 ('mina','Mina Krail','she/her','Rusk purchasing agent and tracker; carries30GP shared purchase fund and signed order.',55,55,65,'road','rusk_company',{'goal':'Buy Register up to30GP,then bring back to Rusk.','knows':'Rusk issuer,object sketch,Ashwick route; no Nimras,inn,Malrec rite.','funds_gp':30,'Stealth':55,'limits':'No attack without target identified and reachable; surrender isolated or badlyhurt. Fund not duplicated with Davren.'}),
 ('davren','Davren Vetch','he/him','Rusk second purchasing/recovery agent, knows the sketch and return route.',45,55,65,'road','rusk_company',{'goal':'Protect Mina and recover authentic Register.','knows':'Object sketch,Rusk old office/route; no Nimras or complete binding procedure.','funds_gp':0,'Stealth':60,'limits':'Follow only observed holder; withdraw for injury or capture; no suicidal crowd attack.'}),
 ('captain','Istra Den','she/her','Velvet Hold captain; protects vessel and ordinary crew.',40,50,45,'barge','auction_company',{'goal':'Keep vessel and crew safe.','limits':'Castoff needs two crew,clear lines and actual time; not instant disappearance.'}),
 ('crew1','Nedo Harrow','he/him','Ordinary Velvet Hold sailor.',30,40,35,'barge','auction_company',{'goal':'Earn wage and avoid violence.','limits':'Escape/help crew; not a combat reinforcement.'}),
 ('crew2','Fenn Rook','they/them','Ordinary Velvet Hold sailor.',30,40,35,'barge','auction_company',{'goal':'Earn wage and avoid violence.','limits':'Escape/help crew; no secret spells or fighting rank.'}),
 ]
 for i,(name,pron) in enumerate([('Rovan Hest','he/him'),('Mila Quern','she/her'),('Derrit Sahl','he/him'),('Hobb Marrin','he/him')]):
  roles.append(('guard'+str(i),name,pron,'Paid Velvet Hold guard; one of four total.',35,55,55,'barge','auction_company',{'goal':'Protect business,not Rusk.','station':['entrance','entrance','display','reserve'][i],'limits':'Warn/block/call colleague,restraint first. No magic detection,free action or immunity. Surrender/evacuate for defeat or fire.'}))
 for i,(name,pron) in enumerate([('Balin Tuck','he/him'),('Kessa Rane','she/her')]):
  roles.append(('escort'+str(i),name,pron,'Marek escort; one of two total.',35,50,60,'quay','marek_company',{'goal':'Protect Marek,not enforce Rusk claim.','limits':'No starting a lethal bidding quarrel or replacing Rusk agents.'}))
 for i in range(4):
  roles.append(('depotguard'+str(i),'Rusk depot retainer '+str(i+1),'they/them','One of four retainers staying at Ashwick; no simultaneous deployment.',30,50,55,'depot','rusk_company',{'goal':'Guard paid depot post.','limits':'Not activated for a Purewater encounter; travel/order/pay needed before redeployment.'}))
 for key,name,pron,desc,commerce,insight,combat,where,company,extra in roles:
  armed=key in ('mina','davren','rusk') or 'guard' in key or 'escort' in key
  gear=[sword] if armed else [staff] if key=='captain' else [dagger]
  if key=='davren':gear+=[{'name':'Light Crossbow','damage':'1d8','size':'L','reach':'ranged','range':60,'ammo':6}]
  skill={'Commerce':commerce,'Insight':insight,'Influence':50 if key in ('venn','marek','rusk') else 40,'Perception':55 if armed else 45,'Stealth':extra.get('Stealth',40),'Deceit':55 if key in ('mina','davren','rusk') else 40,'Willpower':55 if armed else 45,'Evade':50 if armed else 40,'Streetwise':60 if key in ('venn','mina','davren') else 45,'Boating':65 if key in ('captain','crew1','crew2') else 30}
  armor={loc:2 if armed else 0 for loc in ['Right Leg','Left Leg','Abdomen','Chest','Right Arm','Left Arm','Head']}
  char=once(key,'create-character',name=name,type='npc',species='humanoid',stats=json.dumps(stats),skills=json.dumps(skill),combat_styles=json.dumps({'Dockside weapons':combat}),equipment=json.dumps(gear),armor=json.dumps(armor),description=pron+'. '+desc)
  # Scores describe dispositions, not a predetermined scene; all NPC Luck0/CFI base2AP.
  role='commercial host' if key=='venn' else 'persistent collector' if key=='marek' else 'ambitious former subordinate' if key=='rusk' else 'paid professional'
  notes='LOOKS:Adult '+role+', practical travel clothes; details may vary with actual scene. CORE:Values a workable agreement within personal limits. NATURE:Businesslike in work,ordinary in company; no compulsive interrogation. WANTS:'+extra.get('goal','Complete paid work safely')+' PRESSURE:'+extra.get('limits','Bargain or retreat before ruin')+' KEY:Venn uses warm direct sales talk; Marek asks pointed provenance questions; Rusk gives clipped instructions; agents speak plainly; guards give short warnings.'
  cli('update-character',id=char,luck=0,attributes=json.dumps({'luck_points':0,'action_points':2}),actor_notes=notes,extras=json.dumps({'pronouns':pron,'rank':0,'preparation':'midnight-exchange-auction-live.md','resources_and_intentions':extra,'score':{'want':extra.get('goal','Complete work'),'ought':'Keep agreements without sacrificing ordinary people.','driver':extra.get('goal','Complete paid work'),'stated_reason':'This is the work I agreed to do.','focus':'promotion','status':{'Nimras':'Unknown at opening'},'tactics':['Seek agreement','Use actual leverage','Withdraw or surrender at stated limit'],'when_lied_to':'miss','blind_spot':'Overestimates own familiar trade.','rhythm':'Plain words; no exposition speech.','physical':'Practical working clothes and kit.','secret':'No additional secret beyond documented own knowledge.'}}))
  cli('move-character',id=char,location=ids[where]);cli('join-faction',id=char,faction=ids[company])
  cli('set-doing',id=char,goal=extra.get('goal','Complete paid work safely'),next='Follow actual operation prerequisites in midnight-exchange-auction-live.md; no automatic victory or knowledge.',where=ids[where])
 print('Cast and finite assets saved.',flush=True)
 # Different acts within this chapter; the existing three-adventure arc remains selected.
 avey=once('vey_agenda','add-agenda',holder=V,title='Midnight Exchange: independent examination of advertised papers',clock=3,narrative='Reserve5GP=4fee+1expensecap. Offer terms, obtain independent report, settle fee; no automatic acceptance/purchase/theft.')
 av=once('venn_agenda','add-agenda',holder=ids['venn'],title='Midnight Exchange: sell the genuine clearance consignment',clock=3,narrative='Preview9day to10dusk; sell10night only if lot still held/no lawful stop. Can negotiate earlier purchase or custody on evidence. Independent of Rusk.')
 ar=once('rusk_agenda','add-agenda',holder=ids['rusk'],title='Midnight Exchange: recover the authentic Ash Register',clock=4,narrative='Two agents carry30GP from original80GP;50 and fourguards remain Ashwick. Travel10day,buyfirst. Only losing bid and learning holder permits follow/demand/theft. No omniscient hunt or replacement anchor.')
 am=once('marek_agenda','add-agenda',holder=ids['marek'],title='Midnight Exchange: recover claimant property by purchase or evidence',clock=3,narrative='20GP,twoescorts,duplicate receipt. Negotiate custody; may cooperate with independent examiner. No supernatural knowledge.')
 beats=[('offer',avey,'Vey offers a paid independent examination','d9/day','contact','myth-loc-ddabdb0593f3',[V,N],'Nimras receives Vey note while waiting for work. Routine delivery to supplied address; no acceptance. FourGP appraisal fee,1includedadvance,up to1GP agreedexpenses.','Card1 of live preparation. Appointment provides supervised preview; no bidding/recovery obligation. Delivery routine competent post, no hostile opposition.'),('preview',av,'The Velvet Hold preview','d9/day','contact',ids['barge'],[ids['venn']],'On actual PC visit during advertised preview or later negotiated examination.','Card2. Fourguards total/finite stations, mundane locks and bell-wire, no hostile magic. Register and survey/receipt physically accessible under supervision. Full tactical card in preparation.'),('arrival',ar,'Rusk agents arrive with their purchase fund','d10/day','time',ids['quay'],[ids['mina'],ids['davren']],'Actual journey completes with agents alive,30GP/order/sketch present.','Travel from recorded roadlodging then quay; no private PCknowledge. They learn catalogue arrangements before bidding. Record actual arrival/cost/losses once; do not clone fund.'),('sale',av,'The advertised auction can transfer the Register','d10/night','time',ids['barge'],[ids['venn'],ids['marek'],ids['mina'],ids['davren']],'Only if actual Register still owned/held by Venn and no negotiated withdrawal or lawful stop.','Card4; no automatic sale on tick. Marek20GP/agents30GP,real bids and custody. Commerce only for contested bargain. Established evidence can stop sale; guards remain independent.'),('recover',ar,'Conditional pursuit of an identified Register holder','d11/day','contact',ids['quay'],[ids['mina'],ids['davren']],'Agents lose purchase opportunity,identify actual holder and route,remain fit/reachable. No fixed mandatory encounter.','Card5. Observe/ask/tail through opposed rolls; warning and multiple exits. Offer/demand/theft/force as actual circumstances warrant. No attack at unknown inn, no replacements, retreat/surrender possible.'),('settle',avey,'Vey settles an agreed examination commission','d11/day','contact','myth-loc-1f1ed691536c',[V,N],'Actual contract accepted,report delivered,fees/advance accounted.','Pay total4GP less actuallypaidadvance;actual agreedexpenses≤1GP. A negative appraisal or dangerous finding is a valid report. Further recovery or theft requires separate consent and terms.')]
 for key,ag,title,when,trigger,loc,cast,condition,text in beats:
  once(key,'add-beat',agenda=ag,title=title,when=when,trigger=trigger,at=loc,cast=','.join(cast),onscreen_if=condition,summary=condition,narrative=text+'\n\n'+plan)
 def fact(key,text,knowers,about):
  return once(key,'add-fact',statement=text,status='established',when='d9/dawn',about=','.join(about),learned_by=','.join(knowers))
 fact('f_catalogue','A public Velvet Hold catalogue advertises the Ash Register, a brass reliquary/name-tablet with folded estate papers. Previewd9/day throughd10/dusk,auctiond10/night at MerchantQuarter public quay. The catalogue includes a printed facsimile.',[V,ids['venn'],ids['marek']],[ids['barge']])
 fact('f_comparison','Vey sees a possible handwriting match between the catalogue facsimile and a fragment of the vanished magician library he is tracing. This is an unverified attribution; he reserves4GP examination fee plus1GP actualagreedexpenses and knows Nimras ThreeSteps address from their courtesy meeting.',[V],[V,ids['barge']])
 fact('f_custody','Venn owns the clearance consignment and holds the authentic Ash Register in Velvet Hold display/reserve. Ledger in locked office drawer records clearance chain; Venn knows its physical custody and seller, not the nature of the old funerary working.',[ids['venn']],[ids['venn'],ids['barge']])
 fact('f_claim','Olt Marek has a duplicate seizure receipt matching the Ash Register estate seal and20GP to buy for a dispossessed claimant. He knows confiscation connection but not a host experiment; his two escorts know only duty and their employer.',[ids['marek']],[ids['marek'],ids['barge']])
 fact('f_rusk','Rusk cleared the Ash Register before Malrec identified its use as a particular authentic anchor. He now needs to buy it back for his proposed derivative binding demonstration. He has50GP/fourretainers/cart/twohorses at Ashwick;Mina andDavren carry the other30GP,order/sketch and know no Nimras/lodging. Demonstration requires further ritual/host/notes/remains preparation, unactivated this chapter.',[ids['rusk']],[ids['rusk'],ids['depot']])
 fact('f_agents','Mina and Davren carry Rusk signed purchase order,Register sketch,return route to Ashwick,and30GP inMina purse. They are directed to buy up to30GP; if purchase fails they must identify and reach the actual holder before any recovery. They know Rusk old estate role,not complete rite or Nimras identity.',[ids['mina'],ids['davren'],ids['rusk']],[ids['mina'],ids['davren']])
 # Explicit, meaningful readback. No live encounter is started by preparing sheets.
 before=json.loads((checkpoint/'character.json').read_text())['character'];after=cli('get-character',id=N)['character'];assert before==after,'PC changed during preparation'
 assert cli('get-context',compact=True)['storyline']==clock,'Clock or scene advanced during preparation'
 for key,*_ in roles:
  c=cli('get-character',id=ids[key])['character'];assert c['myth-luck-current']==0 and c['myth-attributes-json']['action_points']==2
  assert c['myth-equipment-json'] and c['myth-hit-locations-json']
 for key,*_ in beats:
  assert cli('brief',id=ids[key])['status']=='pending'
 assert cli('get-lore',id=lore)['lore']['content']==plan
 view=cli('character-view',id=N);assert not any(f['id'] in [ids[k] for k in ids if k.startswith('f_')] for f in view.get('knows',[]))
 ids['ready']=True;P.write_text(json.dumps(ids,indent=2)+'\n')
 (W/'docs/scenarios/midnight-auction-readiness.json').write_text(json.dumps({'ready':True,'clock':clock,'pc_unchanged':True,'new_secrets_unlearned':True,'cast_sheets':len(roles),'conditional_operations':len(beats),'review':'Refusal/authorities/negotiation/earlydefeat/outoforder checked in live-preparation document; no accepted contract or later ritual activated.'},indent=2)+'\n')
 print('Verified readiness; offer not yet delivered; clock held.',flush=True)
