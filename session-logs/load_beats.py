import sys, types, argparse
sys.path.insert(0, "/Users/gullyburns/mythras-gm/skills/mythras-gm")
sys.path.insert(0, ".")
import mythras_gm as gm
from beats_part1 import BEATS
from beats_part2 import BEATS2
from beats_part3 import BEATS3

CAMPAIGN = "myth-campaign-8327f8687a98"
ALL = BEATS + BEATS2 + BEATS3
ALL.sort(key=lambda b: b[0])
print(f"{len(ALL)} beats to load")

# silence the per-call JSON output
gm.out = lambda d: None

ok = 0
for at, typ, involves, summary, narrative in ALL:
    args = argparse.Namespace(
        campaign=CAMPAIGN, type=typ, summary=summary,
        narrative=narrative.strip(), session=1,
        involves=involves, at=at)
    try:
        gm.cmd_log_event(args)
        ok += 1
    except Exception as e:
        print("FAIL", at, summary[:50], repr(e)[:200])
print(f"loaded {ok}/{len(ALL)}")
