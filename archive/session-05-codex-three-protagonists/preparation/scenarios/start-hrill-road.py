"""Start the prepared Hrill camera without advancing the shared world clock."""
import json
import pathlib
import subprocess

ROOT=pathlib.Path(__file__).resolve().parent
GM='/Users/gullyburns/.codex/plugins/cache/fourth-wall-gaming/mythras-gm/1.0.0/skills/mythras-gm'
C='myth-campaign-purewater-s1'
H='myth-char-07bc6645bb49'
M=json.loads((ROOT/'hrill-road-ids.json').read_text())

def cli(*args):
    r=subprocess.run(['uv','run','-q','--project',GM,'python',GM+'/mythras_gm.py',*args],capture_output=True,text=True)
    lines=[x for x in r.stdout.splitlines() if x.startswith('{')]
    if r.returncode or not lines:raise RuntimeError(r.stdout+r.stderr)
    d=json.loads(lines[-1])
    if not d.get('success'):raise RuntimeError(d)
    return d

if M.get('opening_logged'):
    raise SystemExit('Opening already logged; resume, do not restart.')

for k,cid in M['npcs'].items():
    pronouns='she/her' if k in ('maelin','anwen','cessa') else 'he/him' if k in ('len','serevan','vaust') else 'they/them'
    cli('update-character','--id',cid,'--extras',json.dumps({'pronouns':pronouns}))
cli('set-doing','--id',M['npcs']['cessa'],'--campaign',C,'--goal','Keep the company paid and avoid pointless losses','--next','Travel a day and a half with Harl and Oda and six grain sacks; earliest aid arrival d9/day','--where',M['camp'])
for k in ('aid','occupation','eviction','export'):
    b=cli('brief','--id',M[k])
    # Narrative dates are advisory; explicit live when and physical travel govern.
    narrative=(b.get('narrative') or b.get('content') or '')
    if narrative:
        narrative=narrative.replace('a full day needed back to camp','a day and a half needed back to camp')
        cli('revise-beat','--id',M[k],'--narrative',narrative)

before=cli('get-context','--campaign',C,'--compact')
assert before['campaign']['myth-time-index']==93, 'Shared clock moved; reconcile before opening'
M['parallel_state_before_opening']=before
(ROOT/'hrill-parallel-state-at-opening.json').write_text(json.dumps(before,indent=2)+'\n')
session=before['campaign']['myth-session-number']+1
M['session']=session
opening_scene='d7/day late afternoon: Hrill at Ashen Span beyond Wendlow, on foot with full saved kit. Len boot trapped under tilted cart shaft on surviving beam; Maelin holds a rope belayed to sound southern post; jack and timbers on bank, loose mule safe. No injuries or rescue action resolved; no contract accepted. Hrill opening action pending.'
cli('log-event','--campaign',C,'--type','gm-note','--visibility','meta','--session',str(session),'--involves',H,'--summary','Hrill camera starts at same d7/day; parallel PCs preserved','--narrative','Snapshot docs/scenarios/hrill-parallel-state-at-opening.json. Prior shared scene: '+before['campaign']['myth-current-scene']+'. Preserve its actual progression, not older opening text. Hrill story and preparation are in hrill-road-story.md and hrill-road-preparation.md. Same clock, no rewind, no cross-PC knowledge. Refresh only Hrill, the PC being started here; other protagonists retain their own session resources.')
cli('update-character','--id',H,'--status','active','--luck','4','--extras',json.dumps({'build_status':'In play. Player accepted characteristics and refined skills, age and Passions; current default Fighter kit, Civilized culture, longsword specialization and Mounted Combat used. Alignment and home/affiliation remain open.','active_thread':{'title':'The Road Beyond the Banners','scene':opening_scene,'story':'docs/scenarios/hrill-road-story.md','preparation':'docs/scenarios/hrill-road-preparation.md','session':session}}))
cli('move-character','--id',H,'--location',M['span'])
cli('update-campaign','--campaign',C,'--session-number',str(session),'--played',H)
cli('set-scene','--campaign',C,'--scene',opening_scene+' Parallel Nimras: '+before['campaign']['myth-current-scene'])

narrative='Beyond Wendlow, water rattles over stones beneath Ashen Span. A cart hangs crooked through the bridge’s broken decking; its driver straddles a beam, his boot pinned under the shaft. Beside you, a woman braces a rope around a stone post. A jack and loose timbers lie at her feet. “Can you hold this?”'
cli('log-event','--campaign',C,'--type','session-start','--visibility','played','--session',str(session),'--involves',','.join([H,M['npcs']['maelin'],M['npcs']['len']]),'--summary','Hrill opens at Ashen Span; a woman requests help with a belayed cart rope','--narrative',narrative)
cli('add-fact','--campaign',C,'--statement','At Ashen Span the woman holding the belayed cart rope asks Hrill, “Can you hold this?” Hrill has not yet answered or taken it.','--status','established','--when','d7/day','--about',H+','+M['npcs']['maelin'],'--learned-by',H+','+M['npcs']['maelin']+','+M['npcs']['len'],'--source','witnessed')
after=cli('get-context','--campaign',C,'--compact')
assert after['campaign']['myth-time-index']==before['campaign']['myth-time-index']
for pc in before['player_characters']:
    if pc['id']!=H:
        current=next(x for x in after['player_characters'] if x['id']==pc['id'])
        assert current==pc, 'Another PC changed during opening; inspect concurrent activity'
char=cli('get-character','--campaign',C,'--id',H)['character']
assert char['myth-skills-json']['Willpower']==50 and char['myth-extras-json']['age']==42
M['opening_logged']=True
M['opening_text']=narrative
M['readiness_verified']={'other_pc_cards_unchanged':True,'clock_unchanged':True,'hrill_active':True,'skills_and_age_verified':True,'no_outcome_rolled':True}
(ROOT/'hrill-road-ids.json').write_text(json.dumps(M,indent=2)+'\n')
print(json.dumps({'opened':True,'session':session,'clock':after['campaign']['myth-game-date'],'readiness':M['readiness_verified']}))
