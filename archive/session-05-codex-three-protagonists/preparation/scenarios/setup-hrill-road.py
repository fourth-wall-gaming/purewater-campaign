"""Persist Hrill's prepared opening through the approved Mythras CLI only."""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
GM = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
C = 'myth-campaign-purewater-s1'
HRILL = 'myth-char-07bc6645bb49'
MANIFEST = ROOT / 'hrill-road-ids.json'
M = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}

def persist():
    MANIFEST.write_text(json.dumps(M, indent=2) + '\n')

def cli(*args):
    r = subprocess.run(['uv', 'run', '-q', '--project', GM, 'python',
                        GM + '/mythras_gm.py', *args], capture_output=True, text=True)
    lines = [x for x in r.stdout.splitlines() if x.startswith('{')]
    if r.returncode or not lines:
        raise RuntimeError(r.stdout + r.stderr)
    d = json.loads(lines[-1])
    if not d.get('success'):
        raise RuntimeError(d)
    return d

def create(key, *args):
    if key not in M:
        M[key] = cli(*args)['id']
        persist()
    return M[key]

if 'before' not in M:
    M['before'] = cli('get-context', '--campaign', C, '--compact')
    persist()

places = {
 'span': ('Ashen Span', 'Bridge on the old upland road north-east of Wendlow.',
   'SENSE: water over stone, wet grit and creaking rope. SHAPE: forty-foot bridge, twelve-foot compromised deck, ten-foot drop to stony shallows; sound central beam, southern rope post, downstream bank thirty feet away. LIVES: Maelin and Len at opening. HANDS: jack, sixty-foot rope, two six-foot timbers, loose mule on southern bank, cart with medicine and food, hospice destination board. COSTS: unstable load shifts with unsecured movement. TURNS: sound anchor and organised lift can recover Len; unchecked cart movement can trap or drop him. KEY: old stone pier beneath a newer rotten deck.'),
 'hospice': ('Three Hearths Hospice', 'Half-day north of Ashen Span, with sheep-track detour if bridge closed.',
   'SENSE: peat smoke, bread and wind at shutters. SHAPE: sixty-by-forty-foot courtyard, two gates, kitchen rear door, trough and low wall cover. LIVES: Anwen and six residents. HANDS: repair-licence copy, grain bins, beds, tools and map. COSTS: twelve days food; aid can carry conditions. TURNS: refuge, meeting place or disputed garrison depending on actual decisions. KEY: household hearthstones built from old imperial masonry.'),
 'pass': ('Wind Stair', 'A day north of Three Hearths in the eastern Downs and Greyspine foothills.',
   'SENSE: wind piping through drilled mile-stones, grit under boots. SHAPE: eighty-foot traverse on five-foot shelf, two refuge niches; lower ravine track visible, camp lane north. HANDS: mile-stones, rope anchors, fallen masonry and three old road cuts. COSTS: squalls and loose shale; safe belays and waiting work. TURNS: controlling main shelf matters until a bypass is found and made usable. KEY: successive kingdoms have carved over the same stone faces.'),
 'camp': ('White Cairn road camp', 'Half-day ridge lane from Wind Stair; Vaust company base.',
   'SENSE: sawdust, horses, hammering. SHAPE: quarry basin one hundred by sixty feet, two cart entrances, twenty-foot shelves, timber shed and command tent. HANDS: toll frames, marked chains, four carts, twenty grain sacks, command strongbox, relic chest in shed wagon. LIVES: Vaust finite company, less deployed personnel. COSTS: visible sentries and numerical strength; reconnaissance and bargaining are viable. TURNS: missing workers, guards, cart or chest materially stop dependent operations. KEY: a small camp stocked for a larger occupation.'),
 'hame': ('Alder Hame', 'Elven teaching household two hours down eastern ravine from Wind Stair; displaced community, not the Deep Glades.',
   'SENSE: springwater, woodsmoke and slate scratching. SHAPE: thirty-by-twenty-foot house, front garden, rear ravine path and dry spring shelter. LIVES: Serevan and two adult pupils. HANDS: funerary rubbing, packed teaching slates, route sketches and house tools. COSTS: cooperation needs consent; there is no blanket access to elven knowledge. TURNS: potential departure, refuge or defended home only through actual actions. KEY: chalk lessons packed beside cooking pots.'),
}
for k, (name, desc, staging) in places.items():
    lid = create(k, 'add-location', '--campaign', C, '--name', name,
                 '--description', desc, '--narrative', staging)
    cli('update-location', '--id', lid, '--staging-notes', staging)
print('Locations saved', flush=True)

weapon = {'name': 'Longsword', 'damage': '1d8', 'size': 'M'}
shield = {'name': 'Round shield', 'damage': '1d4', 'size': 'L'}
dagger = {'name': 'Dagger', 'damage': '1d4+1', 'size': 'S'}
cast = [
 ('maelin', 'Maelin Voss', 'span', 0, {'Engineering':65,'Perception':55,'Influence':45,'Insight':35,'Athletics':40,'Brawn':35,'Evade':40,'First Aid':40,'Willpower':45,'Combat Skill':35},
  'LOOKS: road-browned young woman in a patched surveying coat. CORE: work must stand up after she leaves. NATURE: brisk, sociable when unhurried, delighted by a well-made thing. WOUND: once trusted a contractor whose work injured a colleague. WANTS: help freeing the carrier and getting the supplies north. PRESSURE: insists on controlling tasks she should delegate. KEY: short concrete verbs, impatient with grand promises.',
  'Free Len and establish a usable independent road', 'Stabilise cart, then find repair timber',
  'Wants Hrill to help people coordinate; owes Len safe practical help; will take sheep-track rather than sacrifice him for the load.'),
 ('len', 'Len Rook', 'span', 0, {'Ride':45,'Drive':45,'Brawn':40,'Athletics':40,'Perception':40,'Influence':35,'Willpower':40,'Evade':35,'Combat Skill':30},
  'LOOKS: broad carrier with a sun-bleached cap and a boot caught beneath a cart shaft. CORE: a delivery is a promise to an actual person. NATURE: plain, companionable, complains without malice. WOUND: dislikes being treated as expendable labour. WANTS: be free of this cart. PRESSURE: becomes terse and fiercely literal. KEY: rough short clauses, ordinary road idiom.',
  'Deliver hospice medicine and return with mule and cart', 'Stay balanced on beam until cart is secured',
  'Wants his property safe; owes delivery but will abandon cart to save himself.'),
 ('anwen', 'Mother Anwen', 'hospice', 0, {'Influence':60,'Insight':55,'Willpower':60,'First Aid':65,'Commerce':50,'Perception':45,'Evade':30,'Combat Skill':20},
  'LOOKS: stout grey-haired woman in a flour-marked apron. CORE: a guest need not agree with her to deserve a bed. NATURE: warm, busy, capable of broad unkind jokes about pretension. WOUND: has seen shelter used to select who deserves to survive. WANTS: supplies and freedom to keep the door open. PRESSURE: becomes immovable over small practical details. KEY: homely directness; no sermon unless asked.',
  'Keep the hospice independent and supplied', 'Hear the aid proposal without promising exclusion',
  'Wants immediate stores; owes all guests welcome. Can close and disperse supplies rather than admit a garrison.'),
 ('serevan', 'Serevan Ashleaf', 'hame', 0, {'Courtesy':60,'Influence':50,'Insight':60,'Willpower':65,'Perception':60,'Survival':60,'Stealth':55,'Lore (Imperial Funerary Practice)':70,'Combat Skill':45},
  'LOOKS: lean elf with ink-stained sleeves and a travelling cloak repaired at both shoulders. CORE: teaching is how a household survives being driven away. NATURE: dry humour, patient with learners, impatient with flattery. WOUND: forced to choose what books and possessions could be carried. WANTS: pupils safe and stolen heritage returned. PRESSURE: retreats into exact answers and independent action. KEY: measured plain speech, sparse figurative language.',
  'Keep pupils safe and recover the funerary standard', 'Check the ravine escape path',
  'Wants restitution but owes living pupils safety. Can leave, trade information or demand an actual protective plan.'),
 ('vaust', 'Sir Aldren Vaust', 'camp', 5, {'Combat Skill':75,'Athletics':60,'Brawn':60,'Endurance':65,'Evade':50,'Influence':65,'Deceit':60,'Insight':50,'Willpower':65,'Perception':55,'Lore (Strategy and Tactics)':70,'Ride':65},
  'LOOKS: tall weathered knight, neatly repaired mail and a plain red cloak. CORE: order belongs to whoever has the nerve to impose it. NATURE: energetic, courteous, enjoys practical accomplishments and competent company. WOUND: royal employers discarded his service when peace made it inconvenient. WANTS: a permanent command and recognition. PRESSURE: turns bargains into tests of obedience, then force. KEY: confident soldierly brevity, makes tangible offers.',
  'Control Wind Stair and secure restorationist patronage', 'Send Cessa with limited aid and conditional protection offer',
  'Wants personal permanence; owes lawful road protection. Aid is real, coercion is chosen. Bargains or surrenders when survival requires it.'),
 ('cessa', 'Sergeant Cessa Dorn', 'camp', 2, {'Combat Skill':60,'Athletics':50,'Brawn':50,'Endurance':55,'Evade':45,'Influence':50,'Deceit':35,'Insight':45,'Willpower':55,'Perception':55,'Ride':50},
  'LOOKS: compact woman with close-cropped hair, leather armour and a mended shield strap. CORE: promises to soldiers mean wages and a route home. NATURE: blunt, likes good meals and undramatic company. WOUND: survived a commander who spent people to save face. WANTS: paid people and no futile fight. PRESSURE: narrows demands, withdraws if she can, fights if trapped. KEY: economical speech, no military philosophy.',
  'Keep the company paid and avoid pointless losses', 'Take Harl and Oda with six grain sacks to hospice, no earlier than d9/day',
  'Wants a quiet contract; owes obedience. Accepts lawful restraint or paid withdrawal when credible, not by automatic defection.'),
]
for i, name in enumerate(['Harl Teven','Oda Vennick','Merrit Caul','Fenn Ash','Joss Veller','Ina Kett']):
    cast.append(('guard'+str(i),name,'camp',2,
      {'Combat Skill':55,'Athletics':45,'Brawn':45,'Endurance':50,'Evade':40,'Perception':45,'Willpower':40,'Influence':30},
      'LOOKS: working retainer in maintained leather armour. CORE: paid work ought to end with pay and a living worker. NATURE: ordinary, hungry, responds to ordinary decency. WOUND: insecure employment. WANTS: wages and survival. PRESSURE: follows the sergeant, then seeks safe retreat. KEY: plain short answers.',
      'Earn wages and survive the road contract','Wait for a specific deployment order',
      'Knows own assignment; no automatic knowledge of relic identity or commander secrets.'))

if 'npcs' not in M:
    existing = cli('list-characters','--campaign',C)['characters']
    assert not {x['name'] for x in existing}.intersection(x[1] for x in cast), 'Unexpected duplicate cast; inspect before import'
    sheets=[]
    for key,name,place,ap,skills,notes,goal,next_,summary in cast:
        soldier=key in ('vaust','cessa') or key.startswith('guard')
        stats={'STR':13 if soldier else 10,'CON':12,'SIZ':12,'DEX':12,'INT':13,'POW':12,'CHA':11}
        locs=[{'name':n,'range':r,'hp':hp,'ap':ap} for n,r,hp in [('Right Leg','01-03',5),('Left Leg','04-06',5),('Abdomen','07-09',6),('Chest','10-12',7),('Right Arm','13-15',4),('Left Arm','16-18',4),('Head','19-20',5)]]
        sheets.append({'name':name,'stats':stats,'skills':skills,'attributes':{'action_points':2,'luck_points':0,'magic_points':12,'initiative_bonus':12,'damage_modifier':'+0','movement':'20 feet','healing_rate':2},'hit_locations':locs,'combat_styles':[{'name':'Arms','value':skills['Combat Skill'],'weapons':[]}],'equipment':[weapon,shield] if soldier else [dagger], 'notes':summary,'passions':{},'race':'Human' if key!='serevan' else 'Elf','score':{'want':goal,'ought':summary,'focus':'promotion' if key=='vaust' else 'prevention','status':{'Hrill':'stranger; no prior relationship'},'tactics':['ordinary specific request','offer a practical bargain','withdraw or resist a concrete threat'],'when_lied_to':'miss','observed':[]},'role':key})
    file=ROOT/'hrill-road-npcs.json';file.write_text(json.dumps(sheets,indent=2)+'\n')
    ids=cli('import-characters','--campaign',C,'--type','npc','--file',str(file))['imported']
    M['npcs']={row[0]:saved['id'] for row,saved in zip(cast,ids)};persist()
for key,name,place,ap,skills,notes,goal,next_,summary in cast:
    cid=M['npcs'][key]
    cli('update-character','--id',cid,'--actor-notes',notes)
    cli('move-character','--id',cid,'--location',M[place])
    cli('set-doing','--id',cid,'--campaign',C,'--goal',goal,'--next',next_,'--where',M[place])
print('Cast, mechanics, scores and activities saved',flush=True)

assets={'retainers':[M['npcs']['guard'+str(i)] for i in range(6)],'officers':[M['npcs']['vaust'],M['npcs']['cessa']],'labourers':4,'riding_horses':2,'draft_horses':2,'carts':4,'grain_sacks':20,'aid_sacks_reserved':6,'gp':60,'relic_chests':1,'retainer_daily_gp':1,'labourer_daily_sp':2}
cli('update-character','--id',M['npcs']['vaust'],'--extras',json.dumps({'assets':assets,'plan_reference':'docs/scenarios/hrill-road-preparation.md'}))
create('company','add-faction','--campaign',C,'--name','Vaust road company','--narrative','Finite independent company: '+json.dumps(assets)+'. New restorationist venture, not Hanzo original possession logistics. Members know only their own assignments.')
create('households','add-faction','--campaign',C,'--name','Three Hearths road households','--narrative','Eight households, twelve willing part-time workers; six hospice residents, ten beds. Not a militia. May accept, negotiate, resist or leave. Current food twelve days. Independent of Crown and forest polities.')

def agenda(key,holder,title,clock,body):
    return create(key,'add-agenda','--campaign',C,'--holder',holder,'--title',title,'--goal',title,'--clock',str(clock),'--status','active','--narrative',body)
agenda('road_agenda',M['npcs']['maelin'],'Hrill road: a usable independent crossing',3,'Progress on actual crossing security, surveyed bypass and work completed; never by date. Assets and outcomes in preparation H1,H3,H6.')
agenda('vaust_agenda',M['npcs']['vaust'],'Hrill road: impose exclusive pass command',4,'Aid proposal, actual support, toll frame deployment, enforced control; each is an uncertain operation. See preparation. No automatic support, eviction or confiscation.')
agenda('relic_agenda',M['npcs']['vaust'],'Hrill road: sell one stolen funerary standard',3,'Chest, paid crew, cart/team, safe route and actual buyer needed. Letter in command strongbox. Earliest departure d13/day, not guaranteed. No active ritual scheduled.')

operations=[
 ('aid','vaust_agenda','Cessa offers shelter with conditions','d9/day','hospice',['cessa','guard0','guard1'],'H2. Earliest attempt after real journey; requires six sacks, Cessa and Harl/Oda. Proposed pledge is readable physical evidence. Opposed Influence only for an actual disputed bargain. No signing or violence predetermined. Full operation card in preparation. If no bargain return all unspent assets and report; a day and a half needed back to camp.'),
 ('occupation','vaust_agenda','The timber frames go toward Wind Stair','d11/dusk','pass',['vaust','cessa'],'H3/H5. Requires report or reconnaissance, four fit armed personnel, two workers, frame cart and access. Revise cast to actual deployed guards. Warn via marked timbers/orders and visible departure. Resolve opposed community resistance; time schedules attempt, never possession. Independent route or lawful settlement may make operation pointless.'),
 ('eviction','vaust_agenda','Vaust attempts to clear Alder Hame','d12/day','hame',['vaust','cessa','serevan'],'H4/H6. Requires a refusal actually known to Vaust, available deployed men and route. Notice must precede attempt. If opposed, roll actual resistance and choices; do not establish expelled or captured people automatically. Surrender, withdrawal, negotiated access and official restraint all work.'),
 ('export','relic_agenda','The relic wagon attempts the eastern road','d13/day','camp',['vaust'],'H5/H6. Requires actual chest, cart, team, paid crew, safe route and destination. No departure if any dependency absent. Telegraph through loading, transport order and buyer letter. Resolve interception/flight normally. One portable antique with no active working, not an army or universal ritual key.'),
]
for key,a,title,when,place,castkeys,body in operations:
    create(key,'add-beat','--campaign',C,'--agenda',M[a],'--title',title,'--when',when,'--at',M[place],'--cast',','.join(M['npcs'][k] for k in castkeys),'--onscreen-if','Hrill is present or has chosen to intervene; otherwise resolve only if dependencies hold.','--summary','Conditional attempt; read the full preparation before resolving.','--narrative',body)
print('Agendas and conditional operations saved',flush=True)

def fact(key,statement,knowers,about='',origin=None,future=False):
    args=['add-fact','--campaign',C,'--statement',statement,'--status','not-yet-true' if future else 'established','--truth','true']
    if about:args+=['--about',about]
    if origin:args+=['--origin',origin]
    if not future:
        args+=['--when','d7/day','--learned-by',','.join(HRILL if k=='hrill' else M['npcs'][k] for k in knowers),'--source','witnessed']
    return create(key,*args)
fact('f_bridge','At d7/day Ashen Span the cart is tilted on a broken timber deck; its driver has a boot caught under the shaft on the surviving beam. A woman holds a rope belayed to the sound southern post. Loose timber and jack are on the bank. No injury yet resolved.',['hrill','maelin','len'],M['span'])
fact('f_destination','The stranded cart destination board reads Three Hearths Hospice and points north.',['hrill','maelin','len'],M['span'])
fact('f_detour','The sheep-track bypass adds an hour to the half-day walk from Ashen Span to Three Hearths; cart passage needs work.',['maelin','len','anwen'],M['span']+','+M['hospice'])
fact('f_licence','Vaust holds a genuine Wendlow road-repair licence; it authorises repairs and a toll proposal, not forced recruitment or eviction. Copies at hospice and camp.',['vaust','cessa','anwen'],M['camp']+','+M['hospice'])
fact('f_pledge','Vaust intends six sacks of real aid in exchange for exclusive patrol/toll rights and exclusion of Serevan household from the hospice; proposed pledge in Cessa bag and camp. Not yet offered or accepted.',['vaust','cessa'],M['npcs']['vaust'])
fact('f_theft','Vaust holds one stolen imperial funerary standard in the shed wagon chest at White Cairn and plans a collector sale beyond Hythe. Buyer letter in his command strongbox. No active ritual exists.',['vaust'],M['camp'])
fact('f_claim','Serevan has a funerary rubbing identifying the standard and witnessed Vaust retained men remove it at a local dig. He does not know its present chest location.',['serevan'],M['hame'])
fact('f_crown','Hrill is a knight loyal to the Crown, seeking to be a good man and stop the killing; no particular road commission, special warrant, military posting or prior NPC acquaintance established.',['hrill'],HRILL)
fact('f_settlement','A lawful nonexclusive settlement has ended Vaust coercive road programme.',[],M['npcs']['vaust'],future=True)
fact('f_recovered','The sole funerary standard is secured beyond Vaust control.',[],M['camp'],future=True)
if 'consequences' not in M:
    cli('add-consequence','--fact',M['f_settlement'],'--agenda',M['vaust_agenda'],'--effect','thwart')
    cli('add-consequence','--fact',M['f_recovered'],'--agenda',M['relic_agenda'],'--effect','thwart')
    M['consequences']=True;persist()

for key,filename,title in [('prep_lore','hrill-road-preparation.md','Hrill: The Road Beyond the Banners — live preparation'),('story_lore','hrill-road-story.md','Hrill: Road Beyond the Banners — three-act development')]:
    create(key,'add-lore','--campaign',C,'--title',title,'--category','scenario','--visibility','gm','--about',HRILL,'--narrative',(ROOT/filename).read_text())

M['ready_review']={'mechanics':True,'finite_resources':True,'knowledge_seeded':True,'operations_conditional':True,'opening_requires_player_action':True,'full_scene_not_yet_narrated':True}
persist()
print(json.dumps({'saved':True,'manifest':str(MANIFEST),'principal_npcs':M['npcs'],'locations':{k:M[k] for k in places},'preparation':M['prep_lore']}),flush=True)
