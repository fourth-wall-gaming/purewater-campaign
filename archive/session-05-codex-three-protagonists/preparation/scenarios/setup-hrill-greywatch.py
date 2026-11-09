"""Persist selected Greywatch preparation through CLI, with resumable IDs."""
import json, pathlib, subprocess, os
P=pathlib.Path(__file__).resolve().parent
GM='/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
C='myth-campaign-purewater-s1'; H='myth-char-07bc6645bb49'
S=['--campaign',C,'--pc',H]
MFILE=P/'hrill-greywatch-ids.json'
M=json.loads(MFILE.read_text()) if MFILE.exists() else {}
def save(): MFILE.write_text(json.dumps(M,indent=2)+'\n')
def cli(*a, scope=True):
    env=dict(os.environ,MYTHRAS_CAMPAIGN=C)
    r=subprocess.run(['uv','run','-q','--project',GM,'python',GM+'/mythras_gm.py',*a,*(S if scope else ['--pc',H])],capture_output=True,text=True,env=env)
    if r.returncode: raise RuntimeError(r.stdout+r.stderr)
    d=json.loads(r.stdout)
    if not d.get('success'): raise RuntimeError(d)
    return d
def once(k,*a,scope=True):
    if k not in M: M[k]=cli(*a,scope=scope);save()
    return M[k]
def entity(k,*a): return once(k,*a)['id']
before=once('before','list-storylines')
assert next(s for s in before['storylines'] if s['name']=='Hrill')['now']=='d25/dusk'
places={
'tower':('Greywatch Beacon','Crown signal tower on outer eastern lake shore, two boat-hours south of Listening Reeds. Ground door AP4 HP20; three Crown soldiers and Bess inside, six-person Avel company outside. Quay below40ft stair, yard40x50ft, old maintenance stair to north. No assault result established.'),
'quay':('Greywatch rock quay and cistern ledge','Thirty-foot stone quay with chest-high bollards;40ft stair to yard, rail with visible gap. Cistern arch60ft north,3ft ledge above water, dry locked service stair into tower. No mandatory swimming. Sentries have limited sight, retreat by boat possible.'),
'cove':('Flint Cove','Sheltered60ft beach15minutes rowing south of Greywatch quay,20minutes footpath to tower. Pike boat landing, unlocked fee-chit locker, oilcloth provisions; no second boat or spontaneous recruits.')}
for k,(name,desc) in places.items():
    ident=entity(k,'add-location','--name',name,'--type','military-site' if k=='tower' else 'landing','--description',desc,'--narrative',desc)
    once(k+'_staging','update-location','--id',ident,'--staging-notes','SENSE: lake wash, wet rope, wood smoke. SHAPE: '+desc+' HANDS: mooring rope, stones, doors and cover. COSTS: real travel and exposed hostile action. TURNS: defend, infiltrate, withdraw, surrender; finite opposition.',scope=False)
cast=[
('avel','Dame Avel Veyr','she',70,5,'tower','Blunt soldier, convivial off duty. Wants an imperial foothold and permanent command; owes followers survival and promised wages. Knows own plan, not Hrill or cistern. Attempts capture, accepts lawful custody if defeated.'),
('pike','Captain Surn Pike','he',55,2,'village','Familiar sailor idiom. Wants unpaid12GP and sound boat; owes crew pay. Knows own contract and visible pursuit, not garrison interior. Withdraws rather than lose boat or fight entire village.'),
('dera','Corporal Dera Venn','she',60,3,'tower','Short practical directions and ordinary humor. Wants keepers and Crown post safe; owes soldiers sensible orders. Knows cistern and visible besiegers, not contract. Welcomes help, can evacuate instead of last stand.'),
('halwen','Halwen Tarr','she',30,0,'village','Plain, ordinarily gossipy keeper. Wants shelter and adult sibling Bess safe. Knows pursued route, demand and cistern maintenance; no political secret or enemy roster. Seeks refuge, guides only by consent.'),
('bess','Bess Tarr','they',30,0,'tower','Dry working speech. Wants household freedom and tower maintained. Knows cistern/fuel, not enemy contracts. Braces door, helps evacuate; no fighting specialist.'),
('arlo','Arlo Fen','he',50,2,'village','Laconic sailor; wants wages and no drowning. Knows pursuit task only. Bow available in boat with Pike, no shot ordered. Yields if isolated.'),
('mar','Mar Lusk','she',55,2,'village','Brusque, mocks hesitation; wants Pike respect and pay. Knows custody task only, underestimates lone older knight. Drawn sword approaching house; bow slung. Backs down when outmatched.'),
('toll','Toll Reed','he',45,1,'village','Repeats captain wording; wants berth and passage home. Knows custody task only. Cudgel ready beside Mar, no attack made. Surrenders at serious threat.'),
('enna','Enna Rusk','she',50,2,'tower','Quiet precise crossbow hand; wants contracted pay and comrades alive. Knows employer imperial aspiration, not Hanzo or unrelated people sharing surname. Covers quay after actual deployment.'),
('corl','Corl Hen','he',50,2,'tower','Talkative cook and spearman; wants home money and regular meals. Knows own employer and task only; guards track, yields if cut off.'),
('venn','Venn Tal','they',50,2,'tower','Gruff spear carrier; wants unit intact, dislikes wasted lives. Knows own employer and task only; holds yard, retreats under half strength.'),
('essa','Essa Gant','she',50,2,'tower','Young, direct spear carrier; wants wages, owes comrades cover. Knows own employer and task only; carries ladder, yields at credible defeat.'),
('jerr','Jerr Low','he',50,2,'tower','Genial spearman off duty; wants recognized military work, fears captivity. Knows own employer and task only; carries ladder, will accept clear safe surrender.'),
('noll','Noll Beck','he',50,3,'tower','Cautious guard; wants civilians safe and corporal supported. Knows tower and demands only. Holds door with spear and shield; evacuation acceptable.'),
('vela','Vela Sorn','she',55,3,'tower','Outspoken guard; wants keepers free and Crown flag flying. Knows tower and demands only. Crossbow at shutter, obeys sensible withdrawal.')]
if 'cast' not in M:
    sheets=[]
    for k,name,pron,combat,ap,where,notes in cast:
        strong=k=='avel'; civilian=k in ['halwen','bess']
        stats=dict(STR=14 if strong else 12,CON=13 if strong else 12,SIZ=14 if strong else 12,DEX=13 if strong else 12,INT=14 if strong else 13,POW=12,CHA=13 if strong else 11)
        sword=k in ['avel','pike','mar']; bow=k in ['arlo','mar']; crossbow=k in ['enna','vela']
        weapon={'name':'Longsword','damage':'1d8','size':'M'} if sword else {'name':'Knife','damage':'1d4+1','size':'S'} if civilian else {'name':'Cudgel','damage':'1d6','size':'M'} if k=='toll' else {'name':'Spear','damage':'1d8','size':'M','traits':['Impale']}
        gear=[weapon]
        if not civilian and k not in ['pike','arlo','mar','toll','enna','vela']:gear.append({'name':'Shield','damage':'1d4','size':'L'})
        if bow or crossbow:gear.append({'name':'Short bow' if bow else 'Crossbow','damage':'1d6' if bow else '1d8','size':'L','reload':2 if bow else 3,'traits':['Impale']})
        skills={'Combat Skill':combat,'Arms':combat,'Athletics':45,'Brawn':55 if strong else 45,'Perception':55 if strong else 45,'Willpower':60 if strong else 45,'Influence':55 if strong else 40,'Evade':40,'Endurance':60 if strong else 45,'Boating':60 if k=='pike' else 50 if k in ['halwen','arlo','mar','toll'] else 30,'Swim':45,'Engineering':45 if k=='dera' else 40,'Stealth':40,'Strategy':65 if strong else 50 if k=='dera' else 30,'First Aid':40}
        hpbase=1 if strong else 0
        locs=[dict(name=n,range=r,hp=hp+hpbase,ap=ap) for n,r,hp in [('Right Leg','01-03',5),('Left Leg','04-06',5),('Abdomen','07-09',6),('Chest','10-12',7),('Right Arm','13-15',4),('Left Arm','16-18',4),('Head','19-20',5)]]
        sheets.append(dict(name=name,stats=stats,skills=skills,attributes=dict(action_points=3 if strong else 2,luck_points=0,magic_points=0,initiative_bonus=14 if strong else 12,damage_modifier='+1d2' if strong else '+0',movement='20 feet',healing_rate=2),hit_locations=locs,combat_styles=[dict(name='Arms',value=combat,weapons=[x['name'] for x in gear])],equipment=gear,passions={},race='Human',notes=pron+'. '+notes))
    f=P/'hrill-greywatch-npcs.json';f.write_text(json.dumps(sheets,indent=2)+'\n')
    M['cast']={row[0]:r['id'] for row,r in zip(cast,cli('import-characters','--type','npc','--file',str(f))['imported'])};save()
for k,name,pron,combat,ap,where,notes in cast:
    ident=M['cast'][k];loc='myth-loc-7352c04bb679' if where=='village' else M[where]['id']
    score={'want':notes,'ought':'Keep comrades alive and honor any actual surrender; does not command Hrill.','driver':notes.split('.')[1].strip(),'status':'Stranger to Hrill; no prior relationship','tactics_ladder':'Demand or guard first; use force if own feasible objective requires it; retreat or surrender at serious injury or credible defeat. Never infinite resources.','catches_lies':'No automatic detection; roll only when evidence warrants.','knowledge_limits':notes,'observed':[]}
    once('cfg_'+k,'update-character','--id',ident,'--luck','0','--magic-current','0','--actor-notes',notes,'--extras',json.dumps({'pronouns':pron,'score':score,'doing':{'goal':notes,'next':'Prepared current placement; no successful attack yet','where':loc},'plan_reference':'docs/scenarios/hrill-greywatch-preparation.md'}))
    once('loc_'+k,'move-character','--id',ident,'--location',loc)
def cid(k):return M['cast'][k]
once('avel_assets','update-character','--id',cid('avel'),'--extras',json.dumps({'assets':{'gp':24,'food_person_days':36,'fighters':[cid(k) for k in ['avel','enna','corl','venn','essa','jerr']],'ladder_feet':18,'rope_feet':60,'pitch_pots':2,'reinforcements':0}}))
once('pike_assets','update-character','--id',cid('pike'),'--extras',json.dumps({'assets':{'gp':4,'fee_unpaid_gp':12,'food_person_days':16,'arrows':36,'bows':2,'crew':[cid(k) for k in ['pike','arlo','mar','toll']],'hull_sections':[{'name':n,'ap':3,'hp':18,'current_hp':18} for n in ['Bow','Stern']],'rope_feet':60,'oars':2}}))
once('dera_assets','update-character','--id',cid('dera'),'--extras',json.dumps({'assets':{'food_person_days':150,'bolts':60,'wood_bundles':12,'oil_jars':2,'skiff_location':'myth-loc-7352c04bb679','skiff_capacity':2}}))
agendas={
'seize':('avel','Take Greywatch as an imperial foothold','Take signal, stores and landing with finite force; no successful assault yet.'),
'pursuit':('pike','Recover keeper and protect boat fee','Seize Halwen if practicable, avoid whole village battle; bargain or withdraw at credible defeat.'),
'defend':('dera','Keep Greywatch people free and post independent','Resist actual assault, welcome help and evacuate if necessary; no obligatory last stand.')}
for key,(holder,title,goal) in agendas.items():entity(key,'add-agenda','--holder',cid(holder),'--title',title,'--goal',goal,'--clock','3','--filled','0','--status','active','--narrative',goal+' Full executable conditions in hrill-greywatch-preparation.md.')
for key,title,ag,when,place,castkeys,card in [
('g1','G1 Keeper seeks shelter from armed pursuit','pursuit','d25/dusk','village',['halwen','mar','toll','pike','arlo'],'G1 — Doorway seizure'),
('g2','G2 Reach Greywatch quay or cistern','defend','d28/day','quay',['dera'],'G2 — Rock quay and cistern approach; OPPORTUNITY ONLY, actual voyage required; do not move Dera out of tower.'),
('g3','G3 Remove contracted transport dependency','pursuit','d28/day','cove',['pike'],'G3 — Flint Cove contract and boat; OPPORTUNITY ONLY, Pike must actually return after two hours, never teleport.'),
('g4','G4 Conditional Greywatch breach attempt','seize','d26/dawn','tower',['avel','enna','corl','venn','essa','jerr','dera','noll','vela','bess'],'G4 — Breach or sortie; requires free Avel, at least three fit attackers, ladder and access. Attempt only, no automatic success.')]:
    loc='myth-loc-7352c04bb679' if place=='village' else M[place]['id']
    entity(key,'add-beat','--agenda',M[ag]['id'],'--title',title,'--when',when,'--at',loc,'--cast',','.join(cid(k) for k in castkeys),'--onscreen-if','Actual presence or intervention; opportunity cards need player approach, backstop is not automatic travel.','--summary',card,'--narrative',card+'\n\n'+(P/'hrill-greywatch-preparation.md').read_text())
facts=[('intention','Avel seeks Greywatch for an independent imperial restorationist foothold.',['avel','enna','corl','venn','essa','jerr']),('contract','Pike is promised12GP unpaid for supporting occupation of Greywatch; the fee chit is in his boat locker.',['pike','avel']),('cistern','Greywatch has a dry locked maintenance stair through its cistern arch, usable without swimming.',['halwen','bess','dera'])]
for k,statement,knowers in facts:entity('fact_'+k,'add-fact','--title','Greywatch '+k,'--statement',statement,'--status','established','--about',M['tower']['id'],'--learned-by',','.join(cid(x) for x in knowers),'--source','witnessed')
entity('future_occupation','add-fact','--title','Greywatch occupation — unresolved','--statement','Avel has seized Greywatch tower, stores and landing.','--status','not-yet-true','--about',M['tower']['id'],'--narrative','Only establish after actual successful contested occupation; not a guaranteed beat result.')
entity('prep_lore','add-lore','--title','The Crown Last Light — selected executable preparation','--category','scenario-preparation','--visibility','gm','--about',H+','+M['tower']['id'],'--summary','Selected nearby action adventure, full cast, knowledge, finite resources, three acts and four situations.','--narrative',(P/'hrill-greywatch-preparation.md').read_text())
once('arc','update-storyline','--id','myth-storyline-0fea5d34980f','--arc-file',str(P/'hrill-greywatch-story.md'))
once('preference','update-character','--id',H,'--extras',json.dumps({'adventure_review_2026_10_27':{'status':'Greywatch selected by Continue after recommendation; no PC choice of involvement assumed','selected_document':'docs/scenarios/hrill-greywatch-preparation.md'}}))
once('review_log','log-event','--type','gm-note','--visibility','meta','--session','8','--involves',H,'--summary','Selected Crown Last Light after Continue; full preparation saved without clock advancement.','--narrative','Existing interview reused: risky knightly action, protection, tactics, nearby conflict. G1 opens at current teaching house; no forced Edda answer, sailing, rest or equipment. Other PCs and prior victories preserved.')
after=cli('list-storylines');M['verified_clock']=after;save()
assert next(s for s in after['storylines'] if s['name']=='Hrill')['minute_in_watch']==92
for k in ['halwen','mar','pike','avel','dera']:
    d=cli('get-character','--id',cid(k));(P/('greywatch-verify-'+k+'.json')).write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'success':True,'cast':len(M['cast']),'g1':M['g1']['id'],'clock':'d25/dusk minute92','manifest':str(MFILE)}))
