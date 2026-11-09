"""Prepare selected Long Shore chapter using the Mythras CLI; never hand-edit DB."""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
GM = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
C = 'myth-campaign-purewater-s1'
H = 'myth-char-07bc6645bb49'
MAELIN = 'myth-char-078dcfaf82f3'
MANIFEST = ROOT / 'hrill-edda-ids.json'
M = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}

def save():
    MANIFEST.write_text(json.dumps(M, indent=2) + '\n')

def cli(*args):
    result = subprocess.run(['uv', 'run', '-q', '--project', GM, 'python',
                             GM + '/mythras_gm.py', *args], capture_output=True, text=True)
    rows = [s for s in result.stdout.splitlines() if s.startswith('{')]
    if result.returncode or not rows:
        raise RuntimeError(result.stdout + result.stderr)
    obj = json.loads(rows[-1])
    if not obj.get('success'):
        raise RuntimeError(obj)
    return obj

def create(key, *args):
    if key not in M:
        M[key] = cli(*args)['id']
        save()
    return M[key]

def once(key, *args):
    if not M.get(key):
        out = cli(*args)
        M[key] = out
        save()
    return M[key]

if 'before' not in M:
    M['before'] = cli('get-context', '--campaign', C, '--compact')
    save()

places = {
 'hythe': ('Hythe — East Arm cargo quay', 'The established lake town at the end of the eastern arm, reached in three days from Three Hearths by Wool Gate and the Downs road.',
 'SENSE: wet hemp, wool bales, dock mallets. SHAPE: eighty-foot cargo quay, sound ladder, carpenter shed, street exit and open water. LIVES: Grey Heron crew preparing boat; public harbour officers may be approached. HANDS: loading planks, marked soundings, coils, cargo tally. COSTS: berth fees and actual loading time, not a mandatory ambush. TURNS: inspect, prepare, provision or depart. KEY: uncharted northern gaps on a working chart.'),
 'boat': ('Grey Heron', 'Edda Vale owned twenty-eight-foot supply boat, presently moored at Hythe cargo quay.',
 'SENSE: creaking blocks, pitch and lake water. SHAPE: twenty-eight-foot deck, small covered forward berth, low cargo hatch, stern helm, ladder and three-person eight-foot tender. HANDS: two sixty-foot ropes, pole, sounding lead, spare oars, repair kit; six small supply bales. COSTS: real section damage, food and finite crew. TURNS: planned transfer, exposed boarding or evacuation. KEY: painted heron almost rubbed off the bow. Geography follows actual travel, never teleport.'),
 'bell': ('Bell Reed Landing', 'Two ordinary sailing days from Hythe along the eastern arm then into the main lake.',
 'SENSE: reeds rasping, fish smoke. SHAPE: eighty-foot bank, thirty-foot outer timber stage with visibly sagging middle, sound inner stone steps forty feet west in three-foot shallows, farmhouse and inland path. HANDS: mooring rings, reed-marked rock patch, landing timber. LIVES: Nera Quill and ordinary fishing families. COSTS: unsafe plank and wind if approached carelessly; tender/stone steps/rope work. TURNS: secure supply landing and hear independent local accounts. KEY: net floats drying on a broken railing.'),
 'shingle': ('White Shingle Isle', 'Half a sailing day north of Bell Reed, one of the lake islets; distinct from Lady\'s Isle.',
 'SENSE: shingle under boots, gulls and wood smoke. SHAPE: two-hundred-foot beach, shallow jetty, two channels one hundred twenty feet apart, safe inland path and sheltered inlet. HANDS: Garr\'s harpoon trestles, towline, open buyer estimate, public campfire. LIVES: Garr and three paid crew at present. COSTS: exposed shoals, finite armed opposition if actually provoked. TURNS: bargain, inspect, scout, retreat or fight. KEY: horn-plate sketches weighted with white stones.'),
 'narrow': ('Narrow Water', 'Half a sailing day north of White Shingle; middle-to-upper lake, several days short of the head.',
 'SENSE: water sucking around reed roots, a distant pole tapping. SHAPE: sixty-foot channel, north/south exits, low fish-weir cover, two reef patches legible by water colour; reed islet punt. LIVES: Ilyen and two scouts patrol. HANDS: poles, shore markers, cover and open southern withdrawal. COSTS: informed local permission for inner channels; crowded boats and harpoon lines are real hazards. TURNS: hospitality, charting or intervention in an actual hunt. KEY: old cut marks on stone below newer wooden markers.'),
 'enclave': ('Listening Reeds', 'Independent mixed elven and fishing enclave, two hours through inner channels from Narrow Water; no Deep Glades access implied.',
 'SENSE: cooking smoke, reed flutes used as ordinary instruments, children at work and play. SHAPE: twelve small houses on firm banks and floating stages, teaching house with records above flood line, three boat approaches and two foot exits. LIVES: twelve adults and four children, including Selith. HANDS: historic shore records, household supplies, ordinary landing tools. COSTS: consent and trust; no automatically hostile inhabitants or magic test. TURNS: a chosen supply relationship and historical knowledge. KEY: old refuge routes taught beside today\'s fishing marks.'),
 'grounds': ('Reedback shallows', 'Broad grazing shoals off White Shingle, separated from beach by four hundred feet of open water.',
 'SENSE: broad wake, clipped weed, moving reed mats. SHAPE: shallow grazing ground, two open channels, stable beach escape; outer observation possible beyond sixty feet. LIVES: one migratory reedback, ordinary birds. HANDS: reed fragments, weed trail, sounding line, water-colour depth clues. COSTS: crowding or harpooning can provoke warning, shove or dive; cold water and entanglement. TURNS: observe, chart, withdraw, approach or free an actual snag. KEY: a reed bed moving against the wind.'),
 'junction': ('Wool Gate junction', 'New plotted upland link one day west of Three Hearths, two days north along Downs road to Hythe.',
 'SENSE: sheep, dry stone and wagon axles. SHAPE: broad cart junction and ordinary village overnight shelter. HANDS: road sign to Hythe, trough and market stalls. COSTS: food/lodging paid or agreed normally. TURNS: northern road or return to hospice. KEY: wool caught on a gate kept open for carts.'),
}
M['hospice'] = 'myth-loc-73eaff6c3e38'
save()
for key, (name, desc, staging) in places.items():
    ident = create(key, 'add-location', '--campaign', C, '--name', name,
                   '--type', 'vessel' if key == 'boat' else 'lake-site',
                   '--description', desc, '--narrative', staging)
    cli('update-location', '--id', ident, '--staging-notes', staging)
print('Lake locations persisted', flush=True)

# key, name, pronouns, place, armour, relevant skills, wants, actor notes, ignorance
cast = [
 ('edda','Edda Vale','she/her','hospice',0,{'Boating':70,'Commerce':60,'Influence':45,'Insight':45,'Willpower':50,'Perception':55,'Survival':45,'Swim':55,'Combat Skill':40},
 'Keep her supply contracts, crew and boat alive',
 'Weathered woman, cropped silvering hair, tar-darkened cuffs. Brisk and warm, occasional affectionate profanity; names concrete jobs. Makes fair bounded offers and retreats from losing battles. Wants her boat and customers to outlast a bad season.',
 'Knows Maelin professionally and reports of unsafe landings; has not seen reedback, secret inner channels, Garr plan, Hrill history or other PCs.'),
 ('perrin','Perrin Moss','he/him','hythe',0,{'Boating':45,'Engineering':55,'Perception':60,'Swim':50,'Influence':35,'Willpower':40,'Combat Skill':30},
 'Make a reliable chart and keep his job',
 'Young chartmaker with pencil smudges. Curious, asks literal useful questions, sketches while listening. Can be distracted by a measurement but wants living crew more than fame.',
 'Knows old chart and local depths, not uncharted northern channels or magical answers.'),
 ('ressa','Ressa Dain','she/her','hythe',0,{'Boating':75,'Perception':65,'Survival':60,'Swim':70,'Brawn':45,'Athletics':50,'Influence':35,'Willpower':55,'Combat Skill':50},
 'Bring crew home and earn wages',
 'Broad-shouldered pilot with a knitted cap. Laconic, blunt about weather, dry amusement at landfolk. Recommends shelter and acts on ropes rather than lecturing. No wish to command Hrill\'s life.',
 'Knows lake shelters and sailing, recent storm; no northern enclave secret or hunter plan.'),
 ('tovin','Tovin Reed','they/them','hythe',0,{'Boating':45,'Brawn':45,'Athletics':55,'Swim':60,'Perception':45,'Influence':35,'Willpower':40,'Combat Skill':35},
 'Earn a share in a boat and be useful',
 'Lanky deckhand with neatly spliced rope bracelet. Eager, good at accepting teasing, practical under instruction. Will drop cargo to save someone; not a compulsory victim.',
 'Knows cargo and own duties, dock gossip only; no hidden loyalties.'),
 ('nera','Nera Quill','she/her','bell',0,{'Boating':65,'Survival':65,'Perception':60,'Swim':65,'Influence':45,'Willpower':50,'Combat Skill':35},
 'Keep fishers supplied and waters usable',
 'Net-mender with broad laugh and weather-split fingers. Earthy jokes, ordinary commercial sense, no solemn philosophy. Wants safe nets and meals; suspicious of costly schemes.',
 'Has seen animal grazing and hunter questions, knows broken landing; uncertain whether fish are displaced permanently. No imperial secrets.'),
 ('garr','Garr Hew','he/him','shingle',2,{'Combat Skill':65,'Boating':65,'Brawn':60,'Athletics':55,'Swim':60,'Perception':60,'Influence':55,'Deceit':45,'Insight':40,'Willpower':55,'Survival':60},
 'Take valuable horn plates and build his hunting reputation',
 'Square hunter with an easy grin and a sunburnt nose. Jovial over business, direct when refused, short threats when cornered. Wants profit and reputation, will endanger an obstructing boat when a hunt is genuinely at stake; surrenders or retreats if outmatched. No secret imperial employer.',
 'Knows last grazing area, his harpoons, crew, buyer estimate. Does not know Hrill exists or the safe enclave channel.'),
 ('berrin','Berrin Holt','they/them','shingle',2,{'Combat Skill':50,'Boating':50,'Athletics':45,'Brawn':45,'Swim':55,'Perception':50,'Willpower':40,'Influence':30},
 'Take promised pay and share, return alive',
 'Working bow hand with repaired leather sleeve. Plain practical answers, watches ropes when others boast. Will cut dangerous towline and surrender rather than die for horn.',
 'Knows announced hunt and wages, not inner channel or broader history.'),
 ('ula','Ula Marrick','she/her','shingle',2,{'Combat Skill':55,'Boating':55,'Engineering':50,'Brawn':50,'Swim':60,'Perception':50,'Willpower':45,'Influence':35},
 'Get paid and keep brother Dorr alive',
 'Stocky harpoon rigger with a patched glove. Clipped operational speech. Prefers a workable rig to a brave speech, refuses plainly suicidal ramming when shown its danger.',
 'Knows lines/harpoons and Garr announced hunt. No enclave route.'),
 ('dorr','Dorr Marrick','he/him','shingle',2,{'Combat Skill':45,'Boating':40,'Athletics':45,'Brawn':40,'Swim':50,'Perception':40,'Willpower':35,'Influence':30},
 'Prove useful and get paid',
 'Young crew hand whose tunic is too large. Jokes when nervous, follows clear instructions, can surrender and learn. No automatic betrayal or last stand.',
 'Knows own hunt duties and sister Ula, not all Garr intentions.'),
 ('ilyen','Ilyen','they/them','narrow',2,{'Combat Skill':60,'Boating':65,'Perception':70,'Survival':70,'Stealth':60,'Swim':65,'Influence':50,'Insight':50,'Willpower':60,'Lore (Lake History)':55},
 'Protect independent shore households and breeding shallows',
 'Lean elf in reed-brown coat, hands usually occupied with boat pole. Courteous, direct hospitality terms, no courtly riddles. Can welcome peaceful outsiders and bargain; uses force against an actual dangerous intrusion, not an accent.',
 'Knows seasonal animal route, own scouts/enclave and Selith records existence; not all records, Hrill mind or current imperial plots.'),
 ('leth','Leth Aren','she/her','narrow',2,{'Combat Skill':50,'Boating':50,'Perception':60,'Survival':60,'Stealth':55,'Swim':60,'Willpower':45,'Influence':30},
 'Guard the shore and return alive',
 'Young elf with a short bow and worn river boots. Few words, attentive to signals; obeys limited patrol instructions, will withdraw from a needless losing fight.',
 'Knows local patrol paths and Ilyen orders only, not Selith records.'),
 ('siv','Siv Orr','he/him','narrow',2,{'Combat Skill':50,'Boating':55,'Perception':55,'Survival':55,'Stealth':50,'Swim':65,'Willpower':45,'Influence':30},
 'Keep households safe and avoid needless fighting',
 'Older human scout with a sun-faded scarf. Sparse matter-of-fact speech, offers a pole before advice. Patrol allegiance is to neighbours, not an empire.',
 'Knows patrol route and orders, not hidden regional politics.'),
 ('selith','Selith An','she/her','enclave',0,{'Lore (Lake History)':75,'Lore (Imperial History)':70,'Courtesy':55,'Influence':55,'Insight':55,'Willpower':65,'Perception':50,'First Aid':60,'Swim':45,'Combat Skill':25},
 'Keep the community free to teach and live',
 'Older elf with short greying hair, ink on one thumb, mended domestic clothes. Patient plain answers and genuine curiosity about visitors. Can keep records private without playing a mysterious oracle. No automatic spells or omniscience.',
 'Knows historical imperial shore names, resistance/refuge channels and own community; no other PCs or current restorationist operations.'),
]

def score(want, notes, ignorance):
    return {'want':want,'ought':'Keep agreed duties while protecting people actually in their care.',
            'driver':want,'stated_reason':want,'blind_spot':'May overvalue own familiar methods; does not automatically read deception.',
            'rhythm':notes,'physical':notes.split('.')[0], 'secret':ignorance,
            'status':{'Hrill':'Unknown; no prior relationship.'},
            'tactics':['ordinary request or warning','concrete bargain','protect or withdraw','force only when actual motive and means justify it'],
            'when_lied_to':'miss','observed':[]}

if 'npcs' not in M:
    existing = cli('list-characters','--campaign',C)['characters']
    assert not {v['name'] for v in existing}.intersection(v[1] for v in cast), 'Inspect duplicate names before retry'
    sheets=[]
    for key,name,pronouns,where,armour,skills,want,notes,ignorance in cast:
        armed=key in ('garr','berrin','ula','dorr','ilyen','leth','siv')
        weapon={'name':'Spear','damage':'1d8','size':'M','traits':['Impale']}
        if key=='garr': weapon={'name':'Billhook','damage':'1d8','size':'M'}
        gear=[weapon,{'name':'Short bow','damage':'1d6','size':'L','range':'45/300/600 feet','reload':2,'traits':['Impale']}] if armed else [{'name':'Knife','damage':'1d4+1','size':'S'}]
        stats={'STR':13 if armed else 11,'CON':12,'SIZ':12,'DEX':12,'INT':13,'POW':12,'CHA':11}
        locations=[{'name':n,'range':r,'hp':hp,'ap':armour} for n,r,hp in [('Right Leg','01-03',5),('Left Leg','04-06',5),('Abdomen','07-09',6),('Chest','10-12',7),('Right Arm','13-15',4),('Left Arm','16-18',4),('Head','19-20',5)]]
        sheets.append({'name':name,'stats':stats,'skills':skills,'attributes':{'action_points':2,'luck_points':0,'magic_points':0,'initiative_bonus':12,'damage_modifier':'+0','movement':'20 feet','healing_rate':2},'hit_locations':locations,'combat_styles':[{'name':'Arms','value':skills['Combat Skill'],'weapons':[]}],'equipment':gear,'notes':pronouns+'. '+ignorance,'race':'Elf' if key in ('ilyen','leth','selith') else 'Human','passions':{},'score':score(want,notes,ignorance),'role':key,'pronouns':pronouns})
    file=ROOT/'hrill-edda-npcs.json';file.write_text(json.dumps(sheets,indent=2)+'\n')
    imported=cli('import-characters','--campaign',C,'--type','npc','--file',str(file))['imported']
    M['npcs']={row[0]:ident['id'] for row,ident in zip(cast,imported)}
    save()
for key,name,pronouns,where,armour,skills,want,notes,ignorance in cast:
    ident=M['npcs'][key]
    once('configure_'+key,'update-character','--id',ident,'--description',pronouns+'. '+ignorance,'--actor-notes',notes,
         '--luck','0','--magic-current','0','--extras',json.dumps({'pronouns':pronouns,'doing':{'goal':want,'next':'Initial activity and limits in docs/scenarios/hrill-edda-preparation.md','where':M[where],'as_of_session':8},'plan_reference':'docs/scenarios/hrill-edda-preparation.md'}))
    once('place_'+key,'move-character','--id',ident,'--location',M[where])

if 'beast' not in M:
    creature={'name':'Reedback of the northern shallows','stats':{'STR':30,'CON':22,'SIZ':36,'DEX':8,'INT':5,'POW':12,'CHA':3},
      'attributes':{'action_points':2,'luck_points':0,'magic_points':0,'initiative_bonus':7,'damage_modifier':'+2d6','movement':'10 feet land; 30 feet swimming','healing_rate':5},
      'skills':{'Swim':85,'Brawn':80,'Endurance':80,'Perception':50,'Evade':20,'Combat Skill':55,'Willpower':50},
      'hit_locations':[{'name':n,'range':r,'hp':hp,'ap':ap} for n,r,hp,ap in [('Right Hind Flipper','01-03',11,3),('Left Hind Flipper','04-06',11,3),('Shell','07-12',16,7),('Right Fore Flipper','13-15',11,3),('Left Fore Flipper','16-18',11,3),('Head','19-20',12,3)]],
      'combat_styles':[{'name':'Natural defences','value':55,'weapons':['Bite','Body buffet']}],
      'equipment':[{'name':'Bite','damage':'1d8','size':'L'},{'name':'Body buffet','damage':'1d6','size':'H'}],
      'race':'Reedback','notes':'Single migratory herbivore; custom aquatic anatomy. No Luck, spells, intelligence in Common, prophecy or imperative to fight. Grazes and retreats.',
      'passions':{},'role':'reedback'}
    file=ROOT/'hrill-edda-reedback.json';file.write_text(json.dumps(creature,indent=2)+'\n')
    M['beast']=cli('import-characters','--campaign',C,'--type','creature','--file',str(file))['imported'][0]['id'];save()
once('beast_notes','update-character','--id',M['beast'],'--luck','0','--magic-current','0','--actor-notes',
     'Large reed-matted shelled herbivore. Grazes, migrates, warns at crowding, dives or shoves if attacked. Withdraws at serious wound if able. No human moral judgement or magical awareness. Behaviour and range limits in prepared creature card.',
     '--extras',json.dumps({'doing':{'goal':'Graze and migrate through safe shallows','next':'Feed offshore; move or retreat from actual disturbance','where':M['grounds'],'as_of_session':8},'plan_reference':'docs/scenarios/hrill-edda-preparation.md'}))
once('beast_place','move-character','--id',M['beast'],'--location',M['grounds'])
print('Named cast and creature sheets persisted',flush=True)

def extra_once(key, npc, extras):
    once(key,'update-character','--id',M['npcs'][npc],'--extras',json.dumps(extras))

extra_once('edda_assets','edda',{'assets':{'gp':40,'boat':M['boat'],'boat_name':'Grey Heron','crew':[M['npcs'][k] for k in ('edda','perrin','ressa','tovin')],
 'food_person_days':80,'supply_bales':6,'supply_bales_wholesale_gp':18,'ropes_sixty_feet':2,'tender_capacity':3,
 'hull_sections':[{'name':n,'ap':4,'hp':20,'current_hp':20} for n in ('Bow','Midships','Stern')],
 'tender':{'ap':3,'hp':10,'current_hp':10},'crew_daily_gp':0.9,'crew_wages_paid_through':'d17/dawn',
 'reserves_included_in_cash':{'crew_up_to14days_gp':13,'hrill10days_gp':10,'fees_and_road_gp':4,'repairs_gp':6},
 'location':M['hythe']},'hiring_offer':{'status':'Not offered in play or accepted','daily_gp':1,'initial_days':10,'advance_gp':2,'food_and_lodging':True,'scope':'Travel from hospice, landing inspections/supply work; no policing or mandatory fight; safe return if ends remotely'},
 'doing':{'goal':'Hire dependable help and return to her supply boat','next':'At Three Hearths trading ordinary goods, available for Maelin introduction; no prior Hrill contact','where':M['hospice'],'as_of_session':8}})
extra_once('garr_assets','garr',{'assets':{'gp':18,'crew':[M['npcs'][k] for k in ('garr','berrin','ula','dorr')],
 'hunting_boats':1,'heavy_harpoons':2,'sixty_foot_towlines':2,'bows':2,'arrows':40,'food_person_days':24,
 'hull_sections':[{'name':n,'ap':3,'hp':18,'current_hp':18} for n in ('Bow','Stern')],
 'initial_crew_wage_reserve_included_gp':6,'crew_total_daily_gp':1,'wages_paid_through':'d17/dawn','repair_reserve_included_gp':3},
 'doing':{'goal':'Take valuable horn plates and secure reputation','next':'Finish harpoon rigs, scout only with fit crew and paid food; earliest site approach d24/day, actual hunt d26/day conditional','where':M['shingle'],'as_of_session':8}})
extra_once('ilyen_assets','ilyen',{'assets':{'patrol':[M['npcs'][k] for k in ('ilyen','leth','siv')],'punt_capacity':4,'bows':3,'arrows':36,'food_person_days':18},
 'doing':{'goal':'Keep enclave independent and shallows safe','next':'Patrol Narrow Water, warn actual visitors, offer terms before force unless attacked','where':M['narrow'],'as_of_session':8}})
extra_once('selith_assets','selith',{'assets':{'adult_households_population':12,'children':4,'food_days':12,'historical_record_chests':1}})

create('crew_faction','add-faction','--campaign',C,'--name','Grey Heron supply crew','--narrative','Four working boat people; Edda assets are authoritative. Honest bounded employment and ordinary trading. No implicit police authority or secret imperial patron.')
create('hunter_faction','add-faction','--campaign',C,'--name','Garr Hew hunting crew','--narrative','One boat, Garr and three named paid workers; assets in Garr character. Independent commercial hunter, not restorationist replacement boss. Individuals can refuse, surrender or withdraw.')
create('shore_faction','add-faction','--campaign',C,'--name','Listening Reeds shore households','--narrative','Independent consenting community and finite three-person patrol. Existing older refuge knowledge remains theirs to share. Twelve adults/four children, no secret army, no universal magic answer.')

def agenda(key, holder, title, size, narrative):
    return create(key,'add-agenda','--campaign',C,'--holder',M['npcs'][holder],
                  '--title',title,'--goal',title,'--clock',str(size),'--status','active','--narrative',narrative)

agenda('route_agenda','edda','Long Shore: dependable consenting supply passage',3,
       'Advance only for actual first secure landing/delivery, verified seasonal channel and consenting northern supply connection. No date-based progress; existing landings/wages survive withdrawal. Preparation L0-L7.')
agenda('hunt_agenda','garr','Long Shore: take reedback horn plates',3,
       'Rig paid boat, locate actual feeding animal, attempt harpoon hunt; no kill by date. Requires surviving crew/boat/lines and tolerable weather. Negotiated replacement work, defeat or withdrawal ends hunt. Never replace assets for free. Preparation L4/L6.')
agenda('shore_agenda','ilyen','Long Shore: preserve independent safe shallows',3,
       'Warn actual visitors, secure a workable access agreement, protect people/ecology when actual threat known. No compulsory shooting or omniscient report. Preparation L5-L7.')

operations=[
 ('opening','route_agenda','Edda offers work at Three Hearths','d18/day','hospice',['edda'],'contact','L0'),
 ('departure','route_agenda','Prepare Grey Heron at Hythe','d21/day','hythe',['edda','perrin','ressa','tovin'],'contact','L1'),
 ('landing','route_agenda','The damaged Bell Reed landing','d23/day','bell',['edda','nera'],'contact','L2'),
 ('observation','route_agenda','A reed bed moves against the wind','d24/day','grounds',['nera'],'contact','L3'),
 ('hunter_offer','hunt_agenda','Garr fits the hunting lines','d24/day','shingle',['garr','berrin','ula','dorr'],'time','L4'),
 ('hospitality','shore_agenda','Ilyen offers shore terms','d25/day','narrow',['ilyen','leth','siv'],'contact','L5'),
 ('hunt','hunt_agenda','Garr attempts the harpoon hunt','d26/day','narrow',['garr','berrin','ula','dorr','ilyen'],'time','L6'),
 ('connection','route_agenda','A consenting northern supply landing','d28/day','enclave',['edda','ilyen','selith'],'contact','L7'),
]
for key, a, title, when, place, actors, trigger, card in operations:
    create(key,'add-beat','--campaign',C,'--agenda',M[a],'--title',title,'--when',when,'--trigger',trigger,
           '--at',M[place],'--cast',','.join(M['npcs'][k] for k in actors),
           '--onscreen-if','Actual contact/arrival or informed chosen intervention. For timed opponent attempts, audit actual resources, information, weather and opposition before any outcome.',
           '--summary','Conditional prepared situation '+card+'; no automatic PC travel, harm or successful NPC action.',
           '--narrative',(ROOT/'hrill-edda-preparation.md').read_text().split('### '+card+' — ')[-1].split('\n### ')[0] if card!='L7' else (ROOT/'hrill-edda-preparation.md').read_text().split('### L7 — ')[-1].split('\n## ')[0])

def fact(key, text, knowers=(), about=(), future=False):
    args=['add-fact','--campaign',C,'--statement',text,'--status','not-yet-true' if future else 'established','--truth','true']
    if about:args+=['--about',','.join(about)]
    if not future:
        args+=['--when','d17/day','--learned-by',','.join(MAELIN if k=='maelin' else M['npcs'][k] for k in knowers),'--source','witnessed']
    return create(key,*args)

fact('f_professional','Edda Vale owns Grey Heron supply boat at Hythe, supplies northern landings and knows Maelin from prior ordinary quay survey work. They have no prior relationship with Hrill. Edda currently visits Three Hearths selling salt/needles and looking for dependable practical help.',['edda','maelin'],[M['npcs']['edda'],MAELIN])
fact('f_offer','Edda is prepared to offer1GP/day plus board for initial10days from acceptance,2GP advance against wages, landing/supply/access work and safe return if work ends remotely. No offer made or accepted yet.',['edda'],[M['npcs']['edda']])
fact('f_landing','Bell Reed outer timber landing visibly sags after storm; inner stone steps40ft west remain sound. Nera knows this from daily use; Edda has only heard the landing is damaged.',['nera'],[M['bell']])
fact('f_report','Edda has received reports that Bell Reed landing is damaged and northern approaches need checking. Crew know chart has unverified northern gaps. None has yet seen the reedback or Garr hunting plan.',['edda','perrin','ressa','tovin'],[M['boat']])
fact('f_animal','One nonmagical migratory reedback grazes waterweed and carries living reed mats through northern shallows. It warns at crowding and retreats if possible; seasonal movement can reveal an accessible channel, not prophecy or automatic navigation. Ilyen/Selith know fuller pattern; Nera knows grazing and recent sightings.',['ilyen','selith'],[M['beast'],M['grounds']])
fact('f_nera_animal','Nera has personally seen a great reed-covered shelled animal grazing and broad wakes near fishing water. She suspects it may displace fish, has not verified long-term effects or full seasonal channel.',['nera'],[M['beast']])
fact('f_hunt','Garr intends to hunt the reedback for valuable horn plates with one boat/four people and two tethered harpoons; crew know announced hunt. No hunt launched, animal struck or other boat rammed.',['garr','berrin','ula','dorr'],[M['npcs']['garr'],M['beast']])
fact('f_enclave','Ilyen patrols Narrow Water with Leth and Siv, protects independent Listening Reeds and requests peaceful visitors sheath weapons and refrain from hunting inside inlet. No universal Crown jurisdiction or hostility to all strangers.',['ilyen','leth','siv','selith'],[M['enclave']])
fact('f_records','Selith holds historical imperial shore-place names and seasonal refuge-channel records at Listening Reeds. These are knowledge and logistics of resistance to Dragon Kings, not an active spell or universal ritual key. No current imperial operation or other PC secrets known.',['selith'],[M['enclave'],M['npcs']['selith']])
fact('f_chest_known','Ilyen knows Selith keeps community records but not all contents or every historical route.',['ilyen'],[M['npcs']['selith']])
fact('f_hunt_ended','Garr\'s current reedback hunt has actually ended by agreement, defeat or voluntary withdrawal.',future=True)
fact('f_route_achieved','A safe consenting northern supply connection has actually been established.',future=True)
once('hunt_consequence','add-consequence','--fact',M['f_hunt_ended'],'--agenda',M['hunt_agenda'],'--effect','abandon')
once('route_consequence','add-consequence','--fact',M['f_route_achieved'],'--agenda',M['route_agenda'],'--effect','complete')

for key,file,title in [('prep_lore','hrill-edda-preparation.md','Hrill: The Long Shore — selected preparation and operations'),('story_lore','hrill-edda-story.md','Hrill: The Long Shore — three-act development')]:
    create(key,'add-lore','--campaign',C,'--title',title,'--category','scenario','--visibility','gm','--about',H,'--narrative',(ROOT/file).read_text())

once('selected_note','log-event','--campaign',C,'--type','gm-note','--session','8','--visibility','meta','--involves',H,
     '--summary','Player selects Edda storyline and explicitly asks for real risk; full preparation held at d17/day.',
     '--narrative','Reuse approved exploration/social/mythic/global preferences. Latest player: Continue. Make it risky though. New locations/cast/operations/knowledge prepared, no lake employment or PC actions assumed. Prior road/lease/restitution gains and other PCs preserved. Full readiness/readback needed before opening.')
M['preparation_saved']=True
save()
print(json.dumps({'prepared':True,'manifest':str(MANIFEST),'edda':M['npcs']['edda'],'operations':len(operations)}),flush=True)
