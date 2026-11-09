"""Prepare and open Nimras's session through the official CLI only."""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
ENGINE = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
CAMPAIGN = 'myth-campaign-purewater-s1'
NIMRAS = 'myth-char-4fc52ae14026'
HALLA = 'myth-char-77a79270f637'
MARKET = 'myth-loc-aca5cfa7ff7c'
CISTERNS = 'myth-loc-e8c76cddd3ea'
manifest_path = ROOT / 'nimras-session-start-manifest.json'
manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

def remember(key, value):
    manifest[key] = value
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    return value

def cli(*args):
    run = subprocess.run(['uv', 'run', '-q', '--project', ENGINE, 'python',
                          ENGINE + '/mythras_gm.py', *args], capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(run.stdout + run.stderr)
    result = json.loads([line for line in run.stdout.splitlines() if line.startswith('{')][-1])
    if not result.get('success'):
        raise RuntimeError(result)
    return result

before = cli('get-context', '--campaign', CAMPAIGN, '--compact')
assert before['world_clock'] == 'd6/dusk', 'Opening preparation is specific to the approved live dusk.'
if manifest.get('opened'):
    raise RuntimeError('Session already opened; read the manifest and live save rather than repeat it.')

if 'house' not in manifest:
    remember('house', cli('add-location', '--campaign', CAMPAIGN,
        '--name', 'The House of Small Windows', '--type', 'house',
        '--description', 'Oren Vey’s private house, library and workrooms on High Isle, entered from a footbridge or a small canal landing.',
        '--narrative', 'A narrow old High Isle house. A front workroom receives visitors; a passage leads to the private library and rear stair. The canal landing is accessible by ordinary boat. Dry book storage, an ink-stained worktable and window shutters matter more than grandeur. No automatic magical barrier, trap or teleport is established.')['id'])
house = manifest['house']
cli('update-location', '--id', house, '--staging-notes',
    'SENSE: beeswax, warm paper, canal water and hulls knocking below the open window. SHAPE: front workroom with table, low canal window, front door to footbridge and inner passage to rear stair; the front and rear exits are ordinary physical exits. LIVES: Oren Vey; household staff remain offstage unless needed. HANDS: cedar case, waxed cord, lamp, blotting paper, chair. COSTS: private property and Vey’s ordinary consent; no compulsory admission fee or spell toll. TURNS: shutters can close and objects can be carried off, but no new wards appear without preparation. KEY: daylight admitted through many small windows to keep it off the books.')

if 'fellowship' not in manifest:
    remember('fellowship', cli('add-faction', '--campaign', CAMPAIGN,
        '--name', 'Nimras’s independent fellowship',
        '--description', 'The independent fellowship that trained Nimras; his former home and current client. Formal name remains unchosen.',
        '--narrative', 'An independent fellowship outside Purewater which trains and employs magicians, including mage hunters. Nimras left amicably to establish his own career. It has commissioned him to recover Rennic Vaur alive and an entrusted manuscript. Its ownership claim and concern about uncontrolled waterworks plans are genuine; it is not automatically a villain. No Crown warrant, local command, unlimited reinforcements or specified contract advance is supplied. No knowledge of Purewater’s current private affairs is presumed.')['id'])
fellowship = manifest['fellowship']

def hit_locations(con, siz, bonus):
    band = (con + siz - 1) // 5
    rows = [('Right Leg','01-03',1+band),('Left Leg','04-06',1+band),
            ('Abdomen','07-09',2+band),('Chest','10-12',3+band),
            ('Right Arm','13-15',max(1,band)),('Left Arm','16-18',max(1,band)),
            ('Head','19-20',1+band)]
    return [{'name':n,'range':r,'hp':hp+bonus,'ap':0} for n,r,hp in rows]

profiles = [
 {'name':'Oren Vey','stats':{'STR':8,'CON':11,'SIZ':12,'DEX':12,'INT':18,'POW':18,'CHA':15},
  'skills':{'Arcane Casting':120,'Arcane Knowledge':120,'Willpower':115,'Insight':85,'Perception':90,'Influence':95,'Courtesy':95,'Streetwise':55,'Evade':55,'Language (Common)':90,'Lore (Arcane history)':120,'Lore (Old manuscripts)':115},
  'attributes':{'action_points':4,'magic_points':18,'luck_points':0,'movement':'6.096m (20 feet)'},
  'hit_locations':hit_locations(11,12,2),'class':'Magic-User','rank':4,'rank_title':'Arch Mage',
  'sorcery_spells':['Read Magic','Avert','Protection','Magic Tricks','Repair','Preserve','Appraise','Detect Magic','Identify','Shield','Armor','Change Appearance','Illusion','Invisibility','Sleep','Magic Missile','Dispel Magic','Detect Invisibility','Locate Object','Mage Lock','Mirror Image','Fly','Hold Person','Dimension Door','Invisibility, Greater','Wizard Sight','Confusion','Enchant Item','Permanency'],
  'powers':[{'name':'Mental Strength','effect':'Once per day, mental magic resistance two grades easier; disbelieve illusions one grade easier.'}],
  'prepared_spells':{'0':['Read Magic','Avert','Protection','Magic Tricks','Repair','Preserve','Appraise'],
                     '1':['Detect Magic','Identify','Shield','Armor','Change Appearance','Illusion','Invisibility','Sleep','Magic Missile'],
                     '2':['Dispel Magic','Detect Invisibility','Locate Object','Mage Lock','Mirror Image','Fly','Hold Person'],
                     '3':['Dimension Door','Invisibility, Greater','Wizard Sight','Confusion'],
                     '4':['Enchant Item','Permanency']},
  'equipment':['Pale grey coat','Silver-mounted spectacles','Correspondence case'],
  'notes':'Established independent master of divination, illusion and old texts, resident at the House of Small Windows on High Isle. Private library and patronage support a pursuit of a vanished magician’s dispersed library. Has limited professional exchanges with Hesper; does not know Hesper’s private allegiance. No Crown office.',
  'score':{'want':'Have visiting scholars entrust rare material to his care.',
           'ought':'Return another person’s property when asked, even if he could preserve it better.',
           'driver':'Fear that the most important work of his life will leave his reach.',
           'stated_reason':'Good scholarship needs dry rooms and responsible custodians.',
           'focus':'prevention','status':{'Nimras':'Established host addressing a younger professional; becomes more formal if treated as an obstacle.','Rennic Vaur':'Colleague whose impatience he indulges.'},
           'tactics':['Offer ordinary hospitality and useful access','Offer an exchange or ask for a copy','Withhold his own private material','Withdraw and protect himself if attacked'],
           'when_lied_to':'miss','blind_spot':'Calls his own collecting preservation and other collectors possessive.',
           'rhythm':'Unhurried complete sentences, occasional scholarly digressions; answers ordinary questions readily.',
           'physical':'Handles papers and spectacles carefully; attire is worn comfortably rather than displayed.',
           'secret':'A prized fragment in his private collection is only a copy; he has not admitted the mistake.',
           'observed':[]},
  'actor_notes':'LOOKS: elderly man in a pale grey coat, ink at a cuff, silver-mounted spectacles. CORE: a hospitable collector who believes access to knowledge depends on someone keeping it safe. NATURE: sociable with scholars, patient with questions, pleased by an exact observation. WOUND: discoveries which were lost because he could not obtain them in time. WANTS: useful exchanges without losing custody of what he already has. PRESSURE: formality replaces warmth; he protects his own property and retreats before risking his life. KEY: register is cultivated and conversational; he does not enumerate or issue military commands.'},
 {'name':'Rennic Vaur','stats':{'STR':10,'CON':13,'SIZ':13,'DEX':14,'INT':16,'POW':16,'CHA':12},
  'skills':{'Arcane Casting':95,'Arcane Knowledge':95,'Willpower':95,'Insight':90,'Perception':75,'Influence':60,'Streetwise':55,'Survival':65,'Stealth':60,'Deceit':50,'Evade':75,'Athletics':45,'Lore (Magical traditions)':85,'Lore (Waterworks surveys)':70},
  'attributes':{'action_points':3,'magic_points':16,'luck_points':0,'movement':'6.096m (20 feet)'},
  'hit_locations':hit_locations(13,13,1),'class':'Magic-User','rank':3,'rank_title':'Adept Mage',
  'sorcery_spells':['Read Magic','Avert','Protection','Coordination','Repair','Appraise','Magic Tricks','Befuddle','Shield','Armor','Magic Missile','Detect Magic','Change Appearance','Invisibility','Sleep','Web','Dispel Magic','Lightning Bolt','Locate Object','Mirror Image','Fly','Hold Person','Dimension Door','Invisibility, Greater','Wizard Sight'],
  'prepared_spells':{'0':['Read Magic','Avert','Protection','Coordination','Repair','Appraise','Magic Tricks'],
                     '1':['Shield','Magic Missile','Detect Magic','Change Appearance','Invisibility','Sleep','Web','Armor'],
                     '2':['Dispel Magic','Lightning Bolt','Locate Object','Mirror Image','Fly','Hold Person'],
                     '3':['Dimension Door','Wizard Sight']},
  'powers':[{'name':'Mental Strength','effect':'Once per day, mental magic resistance two grades easier; disbelieve illusions one grade easier.'}],
  'equipment':['Weathered travelling coat','Manuscript carrying case','Survey notes','Surveying tools'],
  'notes':'Nimras’s former teacher and an experienced mage hunter trained by the same independent fellowship. Has retained an entrusted manuscript beyond his authority and come to Purewater to compare its old surveys with physical structures. Believes that the work matters; that belief does not prove every claim. Not possessed, not part of Hanzo’s household and not automatically hostile to Nimras.',
  'score':{'want':'Get his former colleagues to allow him to complete his comparison before returning the manuscript.',
           'ought':'Honour the fellowship’s trust and return material entrusted for limited study.',
           'driver':'Wants to produce work of his own after years finishing other people’s assignments.',
           'stated_reason':'The comparison could keep public access from being lost through ignorance.',
           'focus':'promotion','status':{'Nimras':'Treats him as a capable former pupil, initially overlooking how independent he has become.','Oren Vey':'Useful peer whom he finds overprotective of books.'},
           'tactics':['Show physical findings and ask for time','Offer a bounded comparison or escorted visit','Negotiate custody and copying','Withdraw from unlawful force; defend himself only as actually needed'],
           'when_lied_to':'miss','blind_spot':'Treats his own overdue return as urgent scholarship and others’ similar conduct as evasive.',
           'rhythm':'Plain short statements; direct replies; technical detail only when asked.',
           'physical':'Practical tools and repaired clothing; studies an object by turning it rather than declaiming about it.',
           'secret':'He has not yet proved the survey interpretation on which he staked his reputation.',
           'observed':[]},
  'actor_notes':'LOOKS: lean middle-aged traveller with closely cropped grey hair, a repaired coat and callused hands. CORE: a former hunter trying to make a discovery without admitting how much he needs it to be right. NATURE: practical, blunt, capable of affectionate teasing with old pupils; generally answers directly. WOUND: decades of useful service remembered under other people’s names. WANTS: enough time to test his findings without forfeiting his own judgement. PRESSURE: becomes terse and seeks a physical exit before escalating to force. KEY: no riddles, no counted preambles, no speeches about what another person feels.'}
]

if 'vey' not in manifest or 'vaur' not in manifest:
    names = cli('list-characters', '--campaign', CAMPAIGN)['characters']
    found = {c['name']:c['id'] for c in names}
    missing = [p for p in profiles if p['name'] not in found]
    if missing:
        sheet_path = ROOT / 'nimras-opening-npcs.json'
        sheet_path.write_text(json.dumps(missing, indent=2, ensure_ascii=False) + '\n')
        imported = cli('import-characters', '--campaign', CAMPAIGN, '--type', 'npc', '--file', str(sheet_path))
        found.update({c['name']:c['id'] for c in imported['imported']})
    remember('vey', found['Oren Vey'])
    remember('vaur', found['Rennic Vaur'])
vey, vaur = manifest['vey'], manifest['vaur']
for profile, cid, location in [(profiles[0],vey,house),(profiles[1],vaur,MARKET)]:
    cli('update-character', '--id', cid, '--luck', '0',
        '--actor-notes', profile['actor_notes'], '--narrative', profile['notes'])
    cli('move-character', '--id', cid, '--location', location)
cli('join-faction', '--id', vaur, '--faction', fellowship)

if 'vey_agenda' not in manifest:
    remember('vey_agenda', cli('add-agenda', '--campaign', CAMPAIGN, '--holder', vey,
        '--title', 'Preserve a library worth finding', '--goal', 'Acquire reliable knowledge of rare manuscripts without surrendering his independence.',
        '--clock', '6', '--priority', '2', '--narrative', 'Existing private collecting pursuit. Offers Vaur’s case freely; does not make its handover conditional on service. Gain progress only through an actual acquisition or scholarly result. Hesper’s private affairs are not known to Vey.')['id'])
if 'vaur_agenda' not in manifest:
    remember('vaur_agenda', cli('add-agenda', '--campaign', CAMPAIGN, '--holder', vaur,
        '--title', 'Finish the comparison before returning', '--goal', 'Test the old survey against current structures and settle custody of the manuscript.',
        '--clock', '4', '--priority', '2', '--target', fellowship,
        '--narrative', 'Current workbench at Lantern Float Market. Wants a bounded physical comparison of old freshwater-intake and access plans. No assured discovery, teleport or flight. Can return early by agreement or be opposed honestly. No auto-completion with time. Full preparation: docs/scenarios/nimras-the-missing-teacher.md.')['id'])

beats = [
 ('n1',manifest['vey_agenda'],'The case at the House of Small Windows','d6/dusk',house,vey,
  'Vey offers a sealed case Vaur left for an agent of the fellowship; Nimras decides how to handle it.',
  'Run N1 in docs/scenarios/nimras-the-missing-teacher.md. Do not reveal case contents before opening. Ordinary voluntary handover requires no roll; contested actions do. The case contains a cracked surveying lens and a note to the Lantern Float Market. Offering the case does not prove the teacher innocent.'),
 ('n2',manifest['vaur_agenda'],'A bench among the boats','d7/dusk',MARKET,vaur,
  'A paying researcher’s workbench gives Nimras a physical route to his former teacher.',
  'Run N2 in docs/scenarios/nimras-the-missing-teacher.md. This is a contact opportunity with d7/dusk as late backstop, not an escape scheduled to foil Nimras. Teacher at the market initially; later movement is actual play. Can conclude recovery early. Do not turn a conversation into an automatic attack.'),
 ('n3',manifest['vaur_agenda'],'The survey at the locked side route','d8/night',CISTERNS,vaur,
  'If Vaur still needs a site comparison, his work may intersect the existing attempt to close cistern access.',
  'Shared angle on myth-beat-5eb5f7f64743, not a second closure. Read both briefs and existing resource ledger. No new Crowbill powers or soldiers. Requires actual continuing research and actual arrival; cancel or revise if recovered earlier. Full N3 in docs/scenarios/nimras-the-missing-teacher.md.'),
 ('n4',manifest['vaur_agenda'],'A working left live','d12/night',None,vaur,
  'Nimras can counter a real magical obstacle if one arises during the hunt.',
  'Contact opportunity only, with late backstop. No automatic casting. Only if Vaur actually casts a prepared defensive Web or an established spell actually obstructs action. Spend resources and roll the caster’s real attempt. Dispel is not automatic. Do not grant the waterfront mercenaries a magical ally. Full N4 in docs/scenarios/nimras-the-missing-teacher.md.'),
 ('n5',manifest['vaur_agenda'],'The teacher’s return passage','d11/dusk',MARKET,vaur,
  'If recovery remains unresolved, any agreed departure or handover uses the waterfront routes that survived play.',
  'Conditional opportunity; early recovery cancels or rewrites this beat. No forced theft, teacher sacrifice, hostage or compulsory duel. Existing Q7 may affect carriage if its prerequisites survive, but cannot close every route. Nimras chooses promises and his report. Full N5 in docs/scenarios/nimras-the-missing-teacher.md.')
]
for key, agenda, title, when, location, cast, summary, narrative in beats:
    if key in manifest:
        continue
    args = ['add-beat','--campaign',CAMPAIGN,'--agenda',agenda,'--title',title,
            '--when',when,'--cast',cast,'--summary',summary,'--narrative',narrative,
            '--onscreen-if','Nimras is actually present or has earned contact with this opportunity; otherwise inspect prerequisites and current outcomes. A late date does not force a scene.']
    if location:
        args += ['--at',location]
    remember(key, cli(*args)['id'])

if 'commission_fact' not in manifest:
    remember('commission_fact', cli('add-fact','--campaign',CAMPAIGN,
        '--statement','Nimras has been commissioned by his former independent fellowship to find Rennic Vaur alive and recover an entrusted manuscript; his first introduction is to Oren Vey.',
        '--status','established','--truth','true','--when','d6/dusk',
        '--about',','.join([NIMRAS,vaur,vey,fellowship]),'--learned-by',NIMRAS,
        '--source','told','--narrative','Agreed starting background, registered at session opening. Does not establish the truth of every allegation, a payment amount, arrest authority or Vaur’s location.')['id'])
if 'case_fact' not in manifest:
    remember('case_fact', cli('add-fact','--campaign',CAMPAIGN,
        '--statement','Rennic Vaur left a sealed cedar case with Oren Vey for whoever his former fellowship sent after him.',
        '--status','established','--truth','true','--when','d6/dusk',
        '--about',','.join([vaur,vey,house]),'--learned-by',','.join([vey,vaur]),
        '--source','witnessed','--narrative','Starting private custody. Nimras learns the statement when Vey offers the case in the opening. Contents are a separate discovery.')['id'])
if 'vaur_location_fact' not in manifest:
    remember('vaur_location_fact', cli('add-fact','--campaign',CAMPAIGN,
        '--statement','At the opening of Nimras’s hunt, Rennic Vaur is working from a rented bench at Lantern Float Market.',
        '--status','established','--truth','true','--when','d6/dusk',
        '--about',','.join([vaur,MARKET]),'--learned-by',vaur,'--source','witnessed',
        '--narrative','GM starting location, not a clue handed to Nimras or Vey. Revise or supersede after actual movement.')['id'])

cli('update-campaign','--campaign',CAMPAIGN,'--arc-file',str(ROOT/'purewater-nimras-live-arc.md'),
    '--played',NIMRAS)
session = manifest.get('session')
if session is None:
    session = before['campaign']['myth-session-number'] + 1
    remember('session',session)
cli('update-campaign','--campaign',CAMPAIGN,'--session-number',str(session))
cli('update-character','--id',NIMRAS,'--status','active',
    '--extras',json.dumps({'build_status':'Active player character; session begun at d6/dusk.',
                          'opening_manifest':'docs/scenarios/nimras-session-start-manifest.json'}))
cli('move-character','--id',NIMRAS,'--location',house)
for cid in [HALLA,NIMRAS]:
    character = cli('get-character','--campaign',CAMPAIGN,'--id',cid)['character']
    cli('update-character','--id',cid,'--luck',str(character['myth-attributes-json']['luck_points']))
cli('set-scene','--campaign',CAMPAIGN,'--scene',
    'd6/dusk. Nimras is the played PC, beginning his hunt at Oren Vey’s House of Small Windows on High Isle. Vey offers a sealed cedar case left by Rennic Vaur for an agent of the fellowship. Case not opened or accepted yet; Nimras has not learned Vaur’s current location. Halla remains home with Dagna in the Forge Quarter. No watch has elapsed; no old Tourney beat or cloth seizure is replayed.')

if 'start_event' not in manifest:
    remember('start_event', cli('log-event','--campaign',CAMPAIGN,'--type','session-start',
        '--session',str(session),'--visibility','meta','--involves',','.join([NIMRAS,HALLA]),
        '--summary','Nimras’s first session begins at the existing d6/dusk; current player focus Nimras. Session Luck refreshed for Halla and Nimras. No clock advance or replay.',
        '--narrative','Nimras’s approved Rank 2 sheet is active. Halla stays home with Dagna. Independent fellowship and Vaur thread prepared within the existing waterfront arc. Stale Tourney-era beats and old Q1 are not permission to undo played history.')['id'])

# Read the actual saved people, place, beat and PC knowledge before speaking.
reads = {key: cli('brief','--id',manifest[key]) for key in ['vey','house','n1']}
reads['nimras_view'] = cli('character-view','--id',NIMRAS,'--campaign',CAMPAIGN,'--compact')
(ROOT/'nimras-opening-briefs.json').write_text(json.dumps(reads,indent=2,ensure_ascii=False)+'\n')
cli('learn','--campaign',CAMPAIGN,'--knower',NIMRAS,'--fact',manifest['case_fact'],
    '--certainty','knows','--source','told','--at','d6/dusk')
if 'opening_event' not in manifest:
    remember('opening_event',cli('log-event','--campaign',CAMPAIGN,'--type','scene',
        '--session',str(session),'--visibility','played','--involves',','.join([NIMRAS,vey]),
        '--summary','Nimras begins at Vey’s House of Small Windows; Vey offers the sealed case Vaur left for an agent of the fellowship. Nimras has not accepted or opened it.',
        '--narrative','Dusk in the House of Small Windows on High Isle. Beeswax, warm paper and canal sounds in the front workroom. Nimras has his letter of introduction. Oren Vey, elderly in a pale grey coat with an ink-stained cuff, offers a cedar case bound with wax-sealed cord and addressed in Rennic Vaur’s hand. Vey says: “Rennic left this for whoever they sent after him. Do you want it opened here?” No response or action by Nimras has yet occurred.')['id'])
remember('opened',True)
after = cli('get-context','--campaign',CAMPAIGN,'--compact')
assert after['world_clock'] == 'd6/dusk'
nimras = next(c for c in after['player_characters'] if c['id'] == NIMRAS)
assert nimras['location'] == house and nimras['luck_current'] == 5
assert next(c for c in after['player_characters'] if c['id'] == HALLA)['luck_current'] == 3
print(json.dumps({'success':True,'session':session,'world_clock':after['world_clock'],
                  'vey':vey,'vaur':vaur,'house':house,'opening_beat':manifest['n1'],
                  'opening_scene_logged':True,'case_opened':False,'briefs':reads},ensure_ascii=False))
