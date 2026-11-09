import json
import os
import pathlib
import subprocess

ROOT = pathlib.Path('/Users/gullyburns/Documents/ChatGPT/mythras')
GM = '/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
CLI = GM + '/mythras_gm.py'
CAM = 'myth-campaign-purewater-s1'
PC = 'myth-char-07bc6645bb49'
SL = 'myth-storyline-0fea5d34980f'
AVEL = 'myth-char-87c2db0593fc'
ELEN = 'myth-char-1e3facc43b6a'
CORL = 'myth-char-ed1a4282d985'
DANE = 'myth-char-e1868d3d940c'
LYSA = 'myth-char-9566e8a59e69'
MARDEN = 'myth-char-c15f519326d9'
VANE = 'myth-char-9ea95fe01beb'
CASSIAN = 'myth-char-6d2b81f7c904'
MOVEMENT = 'myth-faction-c0a9a96aa980'
HARL = 'myth-char-85f99a7f28b1'
SELLA = 'myth-char-786b3af53c81'
OTHIN = 'myth-char-64a3662e6aed'
MARA = 'myth-char-937a61a1e9c1'
HALL = 'myth-loc-e7d28bb092c5'
CAUSEWAY = 'myth-loc-d6eaa9caf9aa'
HYTHE = 'myth-loc-c9b08e8a741a'
STRATEGIC = 'myth-agenda-892c66b201bf'
OLD_RECOVERY = 'myth-beat-ed7adcfed5dd'
OLD_INITIATION = 'myth-beat-55f48fbe0074'
DOCTRINE = 'myth-fact-ed9f33c23a6d'
CUSTOMER = 'myth-fact-3973284f0787'
LORE = 'myth-lore-c82e9705c994'
OUT = ROOT / 'docs/scenarios/hrill-unbroken-crown-plan-ids.json'
M = json.loads(OUT.read_text()) if OUT.exists() else {}
os.environ['MYTHRAS_CAMPAIGN'] = CAM

NO_CAMPAIGN = {
    'revise-fact', 'forget', 'retire-canon', 'update-lore', 'update-location',
    'update-agenda', 'revise-beat', 'require-fact', 'add-consequence',
    'join-faction'
}


def call(*args):
    scope = ['--pc', PC] if args[0] in NO_CAMPAIGN else ['--campaign', CAM, '--pc', PC]
    p = subprocess.run(
        ['uv', 'run', '-q', '--project', GM, 'python', CLI, *args, *scope],
        text=True, capture_output=True)
    assert p.returncode == 0, p.stdout + p.stderr
    data = json.loads(p.stdout)
    assert data.get('success'), data
    return data


def once(key, *args):
    if key not in M:
        M[key] = call(*args)
        OUT.write_text(json.dumps(M, indent=2) + '\n')
    return M[key]


def rid(key):
    value = M[key]
    return value.get('id') or value.get('character', {}).get('id') or value.get('agenda', {}).get('id') or value.get('beat', {}).get('id') or value.get('fact', {}).get('id')


context = call('get-context', '--compact')
assert context['storyline']['now'] == 'd41/day'
assert context['storyline']['minute_in_watch'] == 280

prep = (ROOT / 'docs/scenarios/hrill-unbroken-crown-preparation.md').read_text()
ops = (ROOT / 'docs/scenarios/hrill-unbroken-crown-operations.md').read_text()
story = ROOT / 'docs/scenarios/hrill-unbroken-crown-story.md'

once('reedgate_bend', 'add-location', '--name', 'Reedgate road bend', '--type', 'road',
     '--description', 'Quartermile south of Reedgate Tollhouse. Road between three-foot drainage ditch and low thorn bank; field footpath exits sixty feet before bend; eighty feet open sight unless actual concealment succeeds. Prepared U5 site, no trap or second hidden party.',
     '--narrative', 'Use only actual actors and current assets. Edra can detect, leave by field path, flee, fight, surrender documents or receive help. The cell cannot close every exit without people actually positioned there.')
ROAD_BEND = rid('reedgate_bend')

# Correct existing GM truths without teaching them to Hrill or Lysa.
once('doctrine_revision', 'revise-fact', '--id', DOCTRINE,
     '--statement', 'The Unbroken Crown cell led by Caldus Vane uses a plain-language internal oath renouncing human kings, promising obedience to the inhuman Dragon Kings and accepting the subjection of unwilling humans. Its public appeal is veteran fellowship, rank and order. Vane authorises intimidation, abduction and armed resistance with finite people and resources. There is no cell spellcaster, working compulsion, confirmed living Dragon King or established Hanzo command. This is prepared GM background, not new PC knowledge.',
     '--narrative', 'Authoritative details and operations: docs/scenarios/hrill-unbroken-crown-operations.md')
once('customer_revision', 'revise-fact', '--id', CUSTOMER,
     '--statement', 'Merrit Dane knows Caldus Vane as an arms customer and veteran-meeting host at Reedgate. Dane has the d43/dusk invitation and heard “brothers of the oath,” but has not read the internal oath or learned the plan against Mara. Dane’s receipt packet contains Vane’s old introduction asking him to receive Dame Avel Veyr and her ancestral proofs; Dane treated it as a commercial referral and did not know or fund her Greywatch plan. No PC or Lysa has yet been given Vane’s name, place, invitation or introduction.',
     '--narrative', 'The specific Vane-Avel introduction is an independent evidence route. It does not make Dane party to Greywatch.')

once('vane_join_movement', 'join-faction', '--id', VANE, '--faction', MOVEMENT)
once('relic_demonology_revision', 'revise-fact', '--id', 'myth-fact-5ff48c6853e0',
    '--statement', 'Avel’s inherited ceremonial mail reads PEACE THROUGH OBEDIENCE and praises an ancestor for returning reed households to their appointed lord. Beneath the inner collar, THE CROWNED BREATH ENTERS THE WORTHY CAPTAIN is a historical possession dedication, not an active spell or usable ritual. Her dragon signet shows a kneeling human whose worn lower edge retains a collar-chain. The Veyr chronicle calls refugees strayed dependants, forced levies restored households and executions the quieting of disorder. These objects are authentic propaganda, not enchanted mind control.',
    '--narrative', 'The inner formula made literal return seem plausible to Avel. Vane and Cassian recognized its historical connection to captain-possession while withholding every practical dependency.')
once('cassian_knows_relic_formula', 'learn', '--knower', CASSIAN, '--fact', 'myth-fact-5ff48c6853e0', '--source', 'told')
once('pledge_movement_revision', 'revise-fact', '--id', 'myth-fact-2d468adaab6d',
    '--statement', 'The locked travelling box at Reedgate holds Vane’s counterpart of Avel’s preliminary Unbroken Crown pledge, his written promise of permanent command, a draft disavowal to use if she failed, and Cassian Bree’s Ember-watermarked introduction and coded road instruction. None has yet been removed or shown to the Crown or Hrill.',
    '--narrative', 'Cassian’s instruction says establish a lawful face at Reedgate, keep a roster of suitable veterans and report when the road can receive the old campaign dead. It proves a wider Movement link but contains no ritual procedure.')
once('movement_link_fact', 'add-fact',
    '--title', 'Vane is a lay organizer for Awake the Dragon’s demonological programme',
    '--statement', 'Cassian Bree selected Caldus Vane through a private Ember Society reading as a sworn lay organizer of the Awake the Dragon Movement. Vane is to secure Reedgate as a transport screen and recruit disciplined veterans for possible higher service. He knows literal restoration and funerary material matter but does not know a possession procedure, caster, spirit, host or current working.',
    '--status', 'established', '--about', f'{VANE},{CASSIAN},{MOVEMENT}',
    '--learned-by', f'{VANE},{CASSIAN}', '--source', 'witnessed',
    '--narrative', 'Compartmented global connection. Hanzo and Vane serve the same movement without an established command relationship or knowledge of one another’s operations.')
once('cassian_letter_fact', 'add-fact',
    '--title', 'Cassian and Vane hold counterpart Reedgate correspondence',
    '--statement', 'Vane’s Reedgate box and Cassian Bree’s Purewater correspondence file hold counterpart Ember-watermarked letters. They direct Vane to create a lawful face at Reedgate, roster suitable veterans and report readiness for the old campaign dead. Othin knows the correspondent and words, not the hidden possession method.',
    '--status', 'established', '--about', f'{VANE},{CASSIAN},{OTHIN},{HALL}',
    '--learned-by', f'{VANE},{CASSIAN},{OTHIN}', '--source', 'witnessed',
    '--narrative', 'Either physical copy can expose the organizational connection. Neither proves Hanzo command or supplies demonological mechanics.')

vane_avel = once('vane_avel_fact', 'add-fact',
    '--title', 'Vane recruited Avel but Avel planned and financed Greywatch',
    '--statement', 'Before Greywatch, Caldus Vane recruited Dame Avel Veyr into the Unbroken Crown, exploited her inherited imperial family story and promised permanent command to a veteran who established a first foothold. Vane did not select, command or finance Greywatch. Avel chose the target, spent her own sixty gold and recruited her own followers.',
    '--status', 'established', '--about', f'{AVEL},{VANE}',
    '--learned-by', f'{AVEL},{VANE}', '--source', 'witnessed',
    '--narrative', 'Human persuasion and voluntary culpability; no magical compulsion. Evidence exists through Dane’s packet, Corl, Vane’s papers and any approved Avel letter.')

relics = once('relic_propaganda_fact', 'add-fact',
    '--title', 'The Veyr heirlooms are imperial propaganda for human subjection',
    '--statement', 'Avel’s inherited ceremonial mail reads PEACE THROUGH OBEDIENCE and praises an ancestor for returning reed households to their appointed lord. Her dragon signet shows a kneeling human whose worn lower edge retains a collar-chain. The Veyr chronicle calls refugees strayed dependants, forced levies restored households and executions the quieting of disorder. These objects are authentic propaganda, not enchanted mind control.',
    '--status', 'established', '--about', f'{AVEL},{ELEN}',
    '--learned-by', f'{AVEL},{ELEN},{VANE}', '--source', 'witnessed',
    '--narrative', 'The illustrated red reed route corresponds to Selith’s independent refugee history already known to Hrill, but Hrill has not yet examined or learned these details.')

intro = once('dane_intro_fact', 'add-fact',
    '--title', 'Dane’s receipt packet preserves Vane’s specific introduction of Avel',
    '--statement', 'The receipt packet for Avel’s honest sixty-gold sale contains an earlier line from Caldus Vane asking Dane to receive the Veyr lady and her ancestral proofs and treat her fairly. Dane knows the commercial introduction but did not know Avel’s attack plan or internal oath.',
    '--status', 'established', '--about', f'{DANE},{AVEL},{VANE}',
    '--learned-by', f'{DANE},{AVEL},{VANE}', '--source', 'witnessed',
    '--narrative', 'Physical evidence remains in Dane’s packet at the quarry. It may be disclosed or inspected only through actual play.')

corl_clue = once('corl_clue_fact', 'add-fact',
    '--title', 'Corl heard Avel use Vane’s first-light phrase',
    '--statement', 'Before Greywatch, Corl Hen heard Avel say Greywatch would be the first light and saw her burn one envelope bearing a Reedgate endorsement. Corl does not know Vane’s cell structure, full oath or later plans.',
    '--status', 'established', '--about', f'{CORL},{AVEL},{VANE}',
    '--learned-by', CORL, '--source', 'witnessed')

pledge = once('pledge_cache_fact', 'add-fact',
    '--title', 'Vane’s box contains Avel’s preliminary pledge and his draft disavowal',
    '--statement', 'The locked travelling box at Reedgate holds Vane’s counterpart of Avel’s preliminary Unbroken Crown pledge, his written promise of permanent command for a first foothold and a draft disavowal to use if she failed. None of these papers has yet been removed or shown to the Crown or Hrill.',
    '--status', 'established', '--about', f'{AVEL},{VANE},{HALL}',
    '--learned-by', f'{VANE},{OTHIN}', '--source', 'witnessed')

# Current intentions. Existing HP, wounds, money and equipment are deliberately untouched.
once('avel_current', 'update-character', '--id', AVEL,
    '--actor-notes', 'Blunt veteran, convivial off duty, proud and responsible for Greywatch. She chose and financed the attack after Vane exploited her inherited imperial propaganda and promised permanent command. In lawful Hythe custody awaiting final judgement; no implausible escape. Wants followers paid and defended. May reconsider only through actual proof of Vane’s abandonment; no automatic redemption or magical excuse.',
    '--extras', json.dumps({
        'plan_reference': 'docs/scenarios/hrill-unbroken-crown-operations.md',
        'score': {
            'want': 'Secure an advocate and the promised wages for surviving Greywatch followers; defend her choice as honourable imperial service.',
            'ought': 'Keep her surrender, protect followers and answer lawful judgement; she remains responsible for choosing Greywatch.',
            'tactics': 'At d42/dawn request a supervised letter to Vane. No escape attempt. If shown his disavowal, choose in play whether followers or oath come first.',
            'catches_lies': 'No automatic detection; weigh letters, relics and conduct.'},
        'doing': {
            'goal': 'Await final judgement in lawful Hythe custody and seek aid for her followers.',
            'next': 'At d42/dawn request permission for a supervised letter to Caldus Vane asking for an advocate and promised follower wages; offer 5SP from own purse only if approved.',
            'where': HYTHE},
        'custody': {'status': 'lawfully held at Hythe pending final judgement', 'escape_plan': None, 'letter_cost_sp_unspent': 5},
        'ideological_history': {'source': 'Veyr heirlooms and household chronicle; Vane deliberately reframed them as knightly duty', 'magic_compulsion': False, 'responsibility': 'Avel chose, funded and led Greywatch'}}))

once('vane_current', 'update-character', '--id', VANE,
    '--actor-notes', 'Former knight with damaged left ear and clipped military speech. Fanatic human agent of inhuman Dragon Kings. Recruited Avel by exploiting her family propaganda, but did not command Greywatch. Now seeks an armed Reedgate enclave through recruits, stolen Crown credentials, forgery and a staffed roadblock. Authorises abduction and armed resistance; lethal force only to preserve escape or cell. Bargains, retreats and surrenders at serious wound or credible encirclement. No spells, reinforcements or omniscience.',
    '--extras', json.dumps({
        'plan_reference': 'docs/scenarios/hrill-unbroken-crown-operations.md',
        'score': {
            'want': 'Make Reedgate an armed enclave owing allegiance to the Dragon Kings.',
            'ought': 'Preserve the oath and those who accept it; in his corrupt ethic human sovereignty must yield.',
            'tactics': 'U0 surveillance; U1 witness recovery; U2 named recruitment; U3 initiation; U4 resupply; U5 courier interception; U6 forgery; U7 checkpoint. Reconcile losses before every attempt.',
            'catches_lies': 'No automatic detection; requires observed contradiction or actual report.'},
        'doing': {'goal': 'Build enough sworn force and documentary cover to hold Reedgate.', 'next': 'Send Othin to observe Mara and the Crown post at d42/dawn180 if still free; Vane currently has no news of Hrill, Lysa, Avel’s capture or Dane’s inquiry.', 'where': HALL},
        'assets': {'gp': 45, 'food_person_days': 10, 'crew_total': 4, 'reinforcements': 0, 'horses': 0, 'cart': 0, 'magic_communication': False, 'access_to_Dane_cache': False,
                   'reserved_existing_guard_pay_gp': 12, 'planned_extension_pay_gp': 12, 'planned_recruit_max_gp': 12, 'planned_food_gp': 3, 'planned_information_max_gp': 2,
                   'note': 'Reservations are not spent; same 45GP pool, never duplicated.'}}))
once('vane_movement_role', 'update-character', '--id', VANE,
    '--extras', json.dumps({'movement_role': {
        'faction': MOVEMENT,
        'role': 'lay provincial military organizer',
        'handler_contact': CASSIAN,
        'knows': 'Literal restoration; funerary material matters; Reedgate wanted as transport screen; veterans rostered for higher service.',
        'does_not_know': 'Possession procedure, caster, spirit, intended host, current consignment, Hanzo operations.',
        'magic_capability': False},
        'assets': {'planned_success_report_cost_sp': 5}}))
once('cassian_vane_file', 'update-character', '--id', CASSIAN,
    '--extras', json.dumps({'unbroken_crown_connection': {
        'knows_vane': True,
        'role': 'Selected Vane through private reading and retained counterpart correspondence.',
        'current_limit': 'Has no news of Hrill, Lysa, Avel custody or local interference; receives nothing without an actual delivered report.',
        'vane_file_place': 'Cassian’s existing locked correspondence file in Purewater'}}))
once('othin_forgery', 'update-character', '--id', OTHIN, '--skills', json.dumps({'Forgery': 60}),
     '--extras', json.dumps({'plan_reference': 'docs/scenarios/hrill-unbroken-crown-operations.md', 'tools': {'ordinary_forgery_kit': 1, 'ink_paper_wax': 'finite hall stock; one order attempt plus scraps'}}))
once('dane_connection', 'update-character', '--id', DANE,
    '--extras', json.dumps({'plan_reference': 'docs/scenarios/hrill-unbroken-crown-operations.md',
        'assets': {'vane_avel_introduction': {'quantity': 1, 'place': 'receipt packet in survey case', 'shown_to_Hrill': False}},
        'score': {'knowledge_limits': 'Knows Vane introduced Avel for the honest relic sale and hosts veteran meetings. Did not know Greywatch plan, full oath, Mara operation or courier plan.'},
        'doing': {'goal': 'Continue legitimate salvage and answer bounded Crown inquiry into customer connections.', 'next': 'At safe arsenal entry during OOC hold. Vane invitation and specific Avel introduction remain in survey case and have not yet been disclosed.', 'where': 'myth-loc-1123ef0edce9'}}))
once('corl_connection', 'update-character', '--id', CORL,
    '--extras', json.dumps({'plan_reference': 'docs/scenarios/hrill-unbroken-crown-operations.md',
        'score': {'knowledge_limits': 'Knows Avel used the phrase first light and burned a Reedgate envelope before Greywatch; does not know Vane’s cell, full oath or current operations.'}}))

# Named future participants. They are not cell members unless persuaded in play.
sword = {'name': 'Broadsword', 'damage': '1d8', 'size': 'M', 'ap': 6, 'hp': 12, 'traits': ['Bleed']}
shield = {'name': 'Round shield', 'damage': '1d4', 'size': 'L', 'ap': 4, 'hp': 12, 'traits': ['Ranged Parry', 'Passive Block 4 locations']}
spear = {'name': 'Short spear', 'damage': '1d8+1', 'size': 'M', 'ap': 4, 'hp': 5, 'traits': ['Impale']}
leather = {x: 2 for x in ['Chest', 'Abdomen', 'Head', 'Right Arm', 'Left Arm', 'Right Leg', 'Left Leg']}

def make_npc(key, name, pronouns, stats, skills, gear, armor, notes, where):
    once(key, 'create-character', '--name', name, '--type', 'npc', '--species', 'humanoid',
         '--stats', json.dumps(stats), '--skills', json.dumps(skills),
         '--combat-styles', json.dumps({'Arms': skills['Arms']}), '--equipment', json.dumps(gear),
         '--armor', json.dumps(armor), '--description', notes)
    cid = rid(key)
    once(key + '_cfg', 'update-character', '--id', cid, '--luck', '0', '--magic-current', '0',
         '--attributes', json.dumps({'action_points': 2, 'luck_points': 0, 'magic_points': 0, 'damage_modifier': '+0', 'initiative_bonus': 12, 'movement': '20 feet'}),
         '--actor-notes', notes,
         '--extras', json.dumps({'pronouns': pronouns, 'plan_reference': 'docs/scenarios/hrill-unbroken-crown-operations.md',
             'doing': {'goal': notes, 'next': 'Prepared future participant only; no recruitment, travel or allegiance has occurred.', 'where': where},
             'score': {'want': notes, 'ought': 'Choose from actual information; no automatic allegiance.', 'tactics': notes, 'catches_lies': 'No automatic detection.'}}))
    once(key + '_where', 'move-character', '--id', cid, '--location', where)
    return cid

tamsin = make_npc('tamsin', 'Tamsin Hale', 'she',
    {'STR': 12, 'CON': 12, 'SIZ': 12, 'DEX': 13, 'INT': 12, 'POW': 13, 'CHA': 11},
    {'Arms': 50, 'Willpower': 55, 'Insight': 45, 'Perception': 50, 'Athletics': 50, 'Endurance': 50, 'Evade': 40},
    [spear, shield], leather,
    'Unemployed veteran with a direct manner. Wants paid work and comradeship, dislikes lordly evasions. Invited to hear Vane’s offer but has not accepted or seen the full oath; can refuse and disclose it.', 'myth-loc-a76869d1528e')
ruan = make_npc('ruan', 'Ruan Cale', 'he',
    {'STR': 11, 'CON': 13, 'SIZ': 12, 'DEX': 12, 'INT': 13, 'POW': 12, 'CHA': 12},
    {'Arms': 45, 'Willpower': 50, 'Insight': 50, 'Perception': 50, 'Athletics': 45, 'Endurance': 55, 'Evade': 40},
    [sword, shield], leather,
    'Former caravan guard, careful and short of money. Wants regular pay but asks what authority stands behind orders. Invited to hear Vane’s offer; no oath or allegiance yet.', 'myth-loc-a76869d1528e')
edra = make_npc('edra', 'Edra Morn', 'she',
    {'STR': 11, 'CON': 13, 'SIZ': 11, 'DEX': 14, 'INT': 13, 'POW': 13, 'CHA': 11},
    {'Arms': 50, 'Willpower': 55, 'Perception': 55, 'Athletics': 65, 'Endurance': 60, 'Evade': 50, 'Bureaucracy': 55},
    [sword, shield, {'name': 'Crown route wallet', 'quantity': 1}, {'name': 'Travel food', 'quantity': 3}], leather,
    'Professional Crown foot courier. Carries a sealed route token and specific appointment/report orders, never a blank royal seal. Avoids a known ambush, seeks help when warned and surrenders documents only under actual threat.', HYTHE)

# Strategic agenda and all concrete operations.
once('strategic_update', 'update-agenda', '--id', STRATEGIC,
    '--title', 'Establish an Unbroken Crown enclave at Reedgate',
    '--goal', 'Gain one voluntary sworn recruit, control genuine Crown route credentials, produce a forged appointment and staff a hostile Reedgate checkpoint with surviving finite assets.',
    '--clock', '4', '--filled', '0', '--priority', '4', '--narrative', ops)
once('strategic_movement_refresh', 'update-agenda', '--id', STRATEGIC,
    '--title', 'Establish an Unbroken Crown enclave and Awake the Dragon route at Reedgate',
    '--goal', 'Gain one voluntary sworn recruit, control Crown credentials, forge an appointment, staff a hostile Reedgate checkpoint and only then attempt a physical readiness report to Cassian Bree.',
    '--clock', '4', '--filled', '0', '--priority', '4', '--narrative', ops)

def beat(key, title, when, at, cast, summary, onscreen, narrative):
    return once(key, 'add-beat', '--agenda', STRATEGIC, '--title', title, '--when', when,
                '--trigger', 'time', '--at', at, '--cast', cast, '--summary', summary,
                '--onscreen-if', onscreen, '--narrative', narrative)

once('u0_watch', 'add-beat', '--agenda', STRATEGIC, '--title', 'U0 — Othin watches Mara and the Crown post',
    '--when', 'd42/dawn', '--trigger', 'time', '--at', 'myth-loc-a76869d1528e', '--cast', f'{OTHIN},{MARA}',
    '--summary', 'Conditional surveillance: 60min walk,30min observation,60min report; learns only what Othin actually sees.',
    '--onscreen-if', 'Hrill/watch/livery staff notice or follow Othin, or protection changes Mara’s route.',
    '--narrative', 'Othin leaves d42/dawn180 only if free, observes livery/post thirty minutes, returns sixty. Stealth/Deceit versus actual observers. Missing rendezvous tells Vane only that Othin is absent after d42/day90, not why. No automatic discovery or knowledge.')
once('u1_revise', 'revise-beat', '--id', OLD_RECOVERY,
    '--title', 'U1 — Attempt to recover Mara and the oath sheet', '--when', 'd42/day',
    '--at', CAUSEWAY, '--cast', f'{OTHIN},{HARL},{SELLA},{MARA}',
    '--summary', 'Conditional three-person recovery at causeway; request, grapple or combat, never automatic abduction.',
    '--onscreen-if', 'Warning/following/protection/interception or actual target encounter. Absence or changed route ends attempt.',
    '--narrative', 'Requires free trio and route information not disproved by U0. Depart dawn270,walk90,expected day60,wait30,return90. Uses listed gear and rope only. Success may control person or paper; losses, absence or protection cancel. Report requires survivor return. Suppressing evidence earns no strategic milestone.')
once('u2_recruit', 'add-beat', '--agenda', STRATEGIC, '--title', 'U2 — Offer paid guard service to Tamsin Hale and Ruan Cale',
    '--when', 'd42/dusk', '--trigger', 'time', '--at', HALL, '--cast', f'{VANE},{OTHIN},{tamsin},{ruan}',
    '--summary', 'Two named veterans hear separate paid offers; no automatic recruit or oath.',
    '--onscreen-if', 'Hrill learns invitations, observes departures, contacts either veteran or visits Reedgate.',
    '--narrative', 'Requires Vane/Othin free and at least2GP advances. Offer1GP each plus5GP after full oath/3days service, max12GP. Influence versus individual Willpower only if uncertain. Refusal/withdrawal/disclosure valid. One actual voluntary pledge earns one agenda milestone.')
once('u3_revise', 'revise-beat', '--id', OLD_INITIATION,
    '--title', 'U3 — Initiate only actual willing attendees', '--when', 'd43/dusk', '--at', HALL,
    '--cast', f'{VANE},{HARL},{SELLA},{OTHIN},{tamsin},{ruan}',
    '--summary', 'Full plain oath offered to actual attendees; no mind control, captive recruitment or unnamed soldiers.',
    '--onscreen-if', 'Actual attendee, witness, invitation, watch action or PC visit leads to Reedgate.',
    '--narrative', 'Requires Vane free, hall usable and at least one actual attendee. Two hours. Refusers can leave unless available guards make and resolve an actual detention attempt. A captive Mara never counts as a recruit. Arrest, exposure or no attendees cancels.')
once('u4_supply', 'add-beat', '--agenda', STRATEGIC, '--title', 'U4 — Buy food and retain surviving core followers',
    '--when', 'd44/day', '--trigger', 'time', '--at', 'myth-loc-05ba898b3929', '--cast', f'{OTHIN},{HARL},{SELLA}',
    '--summary', 'Conditional 3GP food purchase and up to12GP d44–46 retention from the single 45GP pool.',
    '--onscreen-if', 'Market inquiry, surveillance or actual contact with Othin/Harl/Sella.',
    '--narrative', 'Requires Othin free and available money. Four-hour round trip. Thirty person-days cost3GP if stock exists; Harl/Sella offered1GP each per day d44–46. Nothing is prepaid now. Loss/refusal/capture leaves actual remaining food and unpaid followers choose whether to stay.')
once('u5_courier', 'add-beat', '--agenda', STRATEGIC, '--title', 'U5 — Attempt to seize Edra Morn’s Crown route wallet',
    '--when', 'd45/day', '--trigger', 'time', '--at', ROAD_BEND, '--cast', f'{VANE},{HARL},{SELLA},{OTHIN},{edra}',
    '--summary', 'Conditional road interception requiring actual route intelligence and at least two free fighters.',
    '--onscreen-if', 'Hrill escorts/warns Edra, discovers scout or road position, or investigates a missing courier.',
    '--narrative', 'Edra departs Hythe d42dawn, expected Ashwick d44dusk, north d45day0, Reedgate road about day60. Requires credible route report, actual travel, unaltered route and two combatants. Thirty-minute wait. Edra may detect, escape, surrender wallet, be rescued or fight. Wallet has specific token/orders, not blank seal. Success alone earns credential milestone; protection/failure removes U6.')
once('u5_place_revision', 'revise-beat', '--id', rid('u5_courier'), '--at', ROAD_BEND,
    '--narrative', 'At Reedgate road bend: quartermile south of tollhouse, road between three-foot ditch and thorn bank, field path sixty feet before bend and eighty feet open warning unless actual concealment succeeds. Edra departs Hythe d42dawn, expected Ashwick d44dusk, north d45day0, bend about day60. Requires credible route report, actual travel, unaltered route and two free combatants. Thirty-minute wait. Edra may detect, escape, surrender wallet, be rescued or fight. Wallet has specific token/orders, not blank seal. Success alone earns credential milestone; protection/failure removes U6.')
once('u6_forge', 'add-beat', '--agenda', STRATEGIC, '--title', 'U6 — Othin attempts a forged Reedgate appointment',
    '--when', 'd45/dusk', '--trigger', 'time', '--at', HALL, '--cast', f'{OTHIN},{VANE}',
    '--summary', 'One three-hour Forgery60 attempt, only with intact stolen Crown material.',
    '--onscreen-if', 'Search, infiltration, captured clerk, practice scraps or comparison with Edra’s genuine orders.',
    '--narrative', 'Requires Othin free, intact stolen route wallet/token/order and uninterrupted tools/time. One actual Forgery60 resolution. Failure consumes one usable sheet and leaves defects. Success creates a limited forged order but does not make anyone believe it or grant lawful authority.')
once('u7_checkpoint', 'add-beat', '--agenda', STRATEGIC, '--title', 'U7 — Attempt to staff an armed Reedgate checkpoint',
    '--when', 'd46/dawn', '--trigger', 'time', '--at', HALL, '--cast', f'{VANE},{HARL},{SELLA},{OTHIN},{tamsin},{ruan}',
    '--summary', 'Earliest hostile checkpoint, requiring Vane plus two free willing combatants, food and actual documentary or openly illegal cover.',
    '--onscreen-if', 'Road travellers, Crown response, visible barrier or direct visit reaches Reedgate.',
    '--narrative', 'Two hours to set hall furniture as barriers. No new palisade/troops. Travellers assess orders and choose compliance/retreat/resistance with actual contests. Holds one road point only. Lost credentials, inadequate staffing, arrest, surrender or no food cancels/weakens. Open blockade without U6 supplies no credential milestone.')
once('u8_report', 'add-beat', '--agenda', STRATEGIC,
    '--title', 'U8 — Attempt a coded readiness report to Cassian Bree', '--trigger', 'clock>=4', '--at', HALL,
    '--cast', f'{VANE},{OTHIN}',
    '--summary', 'Only after all four milestones: one-hour coded draft and5SP to a verified southbound carrier; no automatic delivery.',
    '--onscreen-if', 'The draft, Ember watermark, carrier inquiry, seized box or intercepted physical letter becomes accessible.',
    '--narrative', 'Requires Vane/Othin free, checkpoint still held, sheet/ink/seal,5SP from same pool and an actual willing carrier. Report says Reedgate can receive funerary consignments and names voluntary higher-service veterans. Carrier may refuse, be warned/searched/delayed or complete actual journey. Cassian learns nothing until delivery and supplies no instant troops, ritual parts or knowledge of Hrill. Interception exposes wider link and leaves Cassian unaware.')

# Avel and the real Crown courier have their own conditional plans.
avel_agenda = once('avel_agenda', 'add-agenda', '--holder', AVEL,
    '--title', 'Seek lawful aid for the Greywatch followers',
    '--goal', 'Request a supervised letter to Vane for an advocate and promised follower wages while remaining in custody.',
    '--clock', '2', '--filled', '0', '--priority', '2', '--status', 'active', '--target', VANE,
    '--narrative', 'Avel asks rather than escapes. Approval, copying, payment and delivery are separate actual steps. Proof of Vane disavowal can change her choices but does not force redemption.')
avel_agenda_id = rid('avel_agenda')
once('avel_letter_request', 'add-beat', '--agenda', avel_agenda_id,
    '--title', 'Avel requests a supervised letter to Vane', '--when', 'd42/dawn', '--trigger', 'time', '--at', HYTHE,
    '--cast', f'{AVEL},{MARDEN}', '--summary', 'Future request only: advocate and follower wages;5SP offered only if approved.',
    '--onscreen-if', 'Hrill remains for judgement, asks officials, or later receives a copied letter/report.',
    '--narrative', 'No escape. Warden may read/copy/refuse or approve. Avel names Vane only when the request is actually made. Her24GP remains unchanged during preparation. Delivery requires actual courier space and travel.')

courier_agenda = once('courier_agenda', 'add-agenda', '--holder', MARDEN,
    '--title', 'Carry Hythe reports to Ashwick and Reedgate',
    '--goal', 'Send Edra Morn on foot with sealed specific reports and route credentials; carry any approved copied Avel correspondence without making it secret.',
    '--clock', '3', '--filled', '0', '--priority', '2', '--status', 'active', '--target', f'{LYSA},{HALL}',
    '--narrative', 'Three actual walking stages. Edra has2GP and3 food-days. No blank royal seal or supernatural communication. Warnings, escorts and route changes can prevent U5.')
courier_agenda_id = rid('courier_agenda')
once('courier_depart', 'add-beat', '--agenda', courier_agenda_id, '--title', 'Edra departs Hythe with specific sealed reports',
    '--when', 'd42/dawn', '--trigger', 'time', '--at', HYTHE, '--cast', f'{edra},{MARDEN}',
    '--summary', 'Conditional foot departure; begins three-stage journey only when orders and provisions are actually issued.',
    '--onscreen-if', 'Hrill is at Hythe, asks for passage/report, or arranges warning/escort.',
    '--narrative', 'No result pre-established. If delayed, detained, warned or reassigned, revise all later timing. Any approved Avel letter is supervised/copyable; it does not secretly inform Vane.')
once('courier_ashwick', 'add-beat', '--agenda', courier_agenda_id, '--title', 'Edra reaches Ashwick before taking the north road',
    '--when', 'd44/dusk', '--trigger', 'time', '--at', 'myth-loc-b31a0ced1c1e', '--cast', f'{edra},{LYSA}',
    '--summary', 'Conditional arrival after three stages; opportunity for warning, escort or route change before U5.',
    '--onscreen-if', 'Hrill/watch are in Ashwick or seek the courier/report.',
    '--narrative', 'Only if prior travel actually completed. Edra plans north d45day0. Lysa can act on actual reports and evidence; no automatic Vane knowledge.')

# Reactions are gated on actual knowledge, not a calendar deadline.
interference = once('interference_fact', 'add-fact',
    '--title', 'Vane receives a credible report of interference',
    '--statement', 'Caldus Vane receives a credible specific report that a witness is protected, an operative is lost, Crown officers are investigating, Avel is captured, the courier is protected or another planned prerequisite has changed.',
    '--status', 'not-yet-true', '--about', VANE,
    '--narrative', 'Establish only when an actual witness, messenger, letter or observed absence reaches Vane after the stated travel delay; teach Vane in the same call.')
interference_id = rid('interference_fact')
reaction = once('reaction_agenda', 'add-agenda', '--holder', VANE,
    '--title', 'Respond only to interference Vane actually learns',
    '--goal', 'Preserve remaining people, evidence and escape while revising or cancelling operations whose prerequisites are lost.',
    '--clock', '4', '--filled', '0', '--priority', '5', '--status', 'dormant', '--target', f'{MARA},{LYSA},{AVEL}',
    '--narrative', ops)
reaction_id = rid('reaction_agenda')
once('reaction_gate', 'require-fact', '--agenda', reaction_id, '--fact', interference_id)
once('reaction_matrix_beat', 'add-beat', '--agenda', reaction_id,
    '--title', 'Apply the saved report-and-capacity reaction matrix', '--trigger', 'clock>=0', '--at', HALL,
    '--cast', f'{VANE},{HARL},{SELLA},{OTHIN}',
    '--summary', 'No reaction until Vane actually knows interference; then use only surviving assets and cancel impossible operations.',
    '--onscreen-if', 'Actual report reaches Vane and produces movement, negotiation, evidence destruction or retreat observable in play.',
    '--narrative', 'Mara protected: abort U1 after survivor report; max2GP public offer/bribe, never storm staffed post. Dane cuts contact: lose sales/cache route, no revenge. Lost follower: reduce force after actual report/missed rendezvous, no replacements. Watch exposed:20min burn specified hall copies,1h move portable cash/pledge/seal with present people; external copies survive, no new hideout. Infiltrator detected: challenge/disarm/detain only with actual guards. Recruit refuses: withdraw/persuade or actual detention, no mind control. Courier protected: cancel U5/U6; open blockade only with three fighters/food. Avel capture: only after letter/report, draft disavowal and max2GP lawful visitor/bribe; no raid/assassin. Defeat: surrender/retreat, all Vane-led operations cease.')
once('reaction_matrix_movement_refresh', 'revise-beat', '--id', rid('reaction_matrix_beat'),
    '--narrative', 'Mara protected: abort U1 after survivor report; max2GP public offer/bribe, never storm staffed post. Dane cuts contact: lose sales/cache route, no revenge. Lost follower: reduce force after actual report/missed rendezvous, no replacements. Watch exposed:20min burn specified hall copies,1h move portable cash/pledge/seal with present people; external copies survive, no new hideout. Infiltrator detected: challenge/disarm/detain only with actual guards. Recruit refuses: withdraw/persuade or actual detention, no mind control. Courier protected: cancel U5/U6; open blockade only with three fighters/food. Avel capture: only after letter/report, draft disavowal and max2GP lawful visitor/bribe; no raid/assassin. Awake-the-Dragon link exposed: burn only the local Cassian letter if still held, cancel U8; Cassian is not warned and his Purewater counterpart survives. Defeat: surrender/retreat, all Vane-led operations cease.')

defeated = once('vane_defeated_fact', 'add-fact',
    '--title', 'Vane is captured, surrenders or the Reedgate cell is broken',
    '--statement', 'Caldus Vane is lawfully captured, surrenders under credible defeat, or the Reedgate cell loses the people and means required to continue its operations.',
    '--status', 'not-yet-true', '--about', VANE,
    '--narrative', 'Establish only from actual play. Local victory is effective: no replacement leader or automatic successor conspiracy.')
defeated_id = rid('vane_defeated_fact')
once('defeat_thwarts_strategic', 'add-consequence', '--fact', defeated_id, '--agenda', STRATEGIC, '--effect', 'thwart')
once('defeat_thwarts_reaction', 'add-consequence', '--fact', defeated_id, '--agenda', reaction_id, '--effect', 'thwart')

# GM lore, storyline arc and held scene.
once('lore_update', 'update-lore', '--id', LORE,
    '--summary', 'Full Avel causal dossier, inherited imperial propaganda, Vane U0–U7 baseline and knowledge-gated reaction matrix.',
    '--narrative', prep + '\n\n' + ops)
once('lore_refresh_named_cast_and_bend', 'update-lore', '--id', LORE,
    '--summary', 'Full Avel causal dossier, inherited imperial propaganda, named cast, Vane U0–U7 baseline and knowledge-gated reaction matrix.',
    '--narrative', prep + '\n\n' + ops)
once('lore_refresh_movement_link', 'update-lore', '--id', LORE,
    '--summary', 'Avel propaganda and possession dedication; Vane’s lay Awake the Dragon role; named cast; U0–U8 baseline and knowledge-gated reactions.',
    '--narrative', prep + '\n\n' + ops)
once('arc_update', 'update-storyline', '--id', SL, '--arc-file', str(story))
once('review_note', 'log-event', '--type', 'gm-note', '--visibility', 'meta',
    '--summary', 'OOC rebuild: Avel causal history and Vane executable plan/reactions persisted',
    '--narrative', 'At unchanged Hrill d41/day280, prepared and persisted: authentic Veyr propaganda heirlooms; Vane recruitment/pledge/disavowal; Avel voluntary self-funded Greywatch and future supervised-letter request; named veterans Tamsin/Ruan; courier Edra; U0-U7 finite operations; knowledge-gated reaction agenda; defeat consequences. No operation occurred, resource was spent, wound healed, PC knowledge added or clock advanced.',
    '--involves', f'{PC},{AVEL},{VANE}')
scene = ('OOC REVIEW HOLD d41/day280, FULL UNBROKEN CROWN REBUILD SAVED. '
         'Active GM docs: hrill-unbroken-crown-preparation.md, -operations.md, -story.md. '
         'Physical state unchanged: H/Lysa/Dane safe arsenal entry; Jo/Ivo at quarry camp with Kett/Willa/Bera; no weapons drawn; salvage left alone. '
         'Pending in-play exchange remains Lysa asking Dane whether customers arm sworn Dragon-King adherents; not yet spoken. '
         'GM truth now includes authentic Veyr propaganda, Vane recruitment without command/funding of Greywatch, Avel custody letter intention, and U0-U7 finite conditional operations/reaction matrix. '
         'NONE of Vane/Avel connection, relic details, named cell/witness/recruits/courier or operations is new Hrill/Lysa knowledge. '
         'H fullHP Fresh MP8 Luck1 26GP3SP5CP own mail/sword/shield/bow20. Other PC clocks untouched. Play/time held.')
once('scene_hold', 'set-scene', '--scene', scene)
once('scene_hold_movement_link', 'set-scene', '--scene', scene + ' GM-only expansion: Vane is a compartmented lay Awake-the-Dragon organizer recruited by Cassian Bree; Veyr inner-collar possession dedication is inert historical evidence; U8 physical report only after actual U7 success. No new Hrill/Lysa knowledge or global operation outcome.')

# Read-back assertions.
ctx = call('get-context', '--compact')
assert ctx['storyline']['now'] == 'd41/day' and ctx['storyline']['minute_in_watch'] == 280
h = ctx['player_characters'][0]
assert h['luck_current'] == 1 and h['magic_current'] == 8
for cid in [tamsin, ruan, edra]:
    c = call('get-character', '--id', cid)['character']
    assert c['myth-luck-current'] == 0 and c['myth-magic-current'] == 0
for cid in [PC, LYSA]:
    view = json.dumps(call('character-view', '--id', cid, '--compact'))
    for secret in ['Tamsin Hale', 'Ruan Cale', 'Edra Morn', 'Caldus Vane', 'PEACE THROUGH OBEDIENCE', 'old campaign dead', 'captain-making art']:
        assert secret not in view, (cid, secret)
    assert rid('movement_link_fact') not in view
    assert rid('cassian_letter_fact') not in view
avel = call('get-character', '--id', AVEL)['character']
assert avel['myth-extras-json']['assets']['gp'] == 24
stories = call('list-storylines')
by_name = {s['name']: (s['now'], s['minute_in_watch']) for s in stories['storylines']}
assert by_name == {'Nimras': ('d9/day', 115), 'Halla': ('d6/dusk', 0), 'Hrill': ('d41/day', 280)}
agenda = call('get-agenda', '--id', STRATEGIC)['agenda']
titles = {b['title'] for b in agenda['beats']}
for expected in ['U0 — Othin watches Mara and the Crown post', 'U1 — Attempt to recover Mara and the oath sheet', 'U2 — Offer paid guard service to Tamsin Hale and Ruan Cale', 'U3 — Initiate only actual willing attendees', 'U4 — Buy food and retain surviving core followers', 'U5 — Attempt to seize Edra Morn’s Crown route wallet', 'U6 — Othin attempts a forged Reedgate appointment', 'U7 — Attempt to staff an armed Reedgate checkpoint']:
    assert expected in titles, expected
assert 'U8 — Attempt a coded readiness report to Cassian Bree' in titles
print(json.dumps({'success': True, 'clock': 'd41/day280 held', 'operations': 9,
                  'reaction_agenda': reaction_id, 'new_cast': {'Tamsin': tamsin, 'Ruan': ruan, 'Edra': edra},
                  'pc_secret_leaks': False, 'Avel_gp': 24, 'other_clocks_unchanged': True}, indent=2))
