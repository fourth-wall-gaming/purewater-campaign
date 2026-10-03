#!/usr/bin/env bash
#
# Re-roll the area maps that carry a revision note, at 4K.
#
# Each render passes TWO references: the master city map, and the sheet's own
# previous image, which the prompt calls "the previous attempt". That is what
# keeps a re-roll from discarding the parts that already worked.
#
#   bash maps/areas/reroll.sh            # every sheet with a revision note
#   bash maps/areas/reroll.sh the-pearl  # just one
#
# Needs ELEVENLABS_API_KEY and a workspace on a Pro plan or above; the Image API
# is gated behind that tier and returns 402 otherwise.

set -uo pipefail
CAMPAIGN="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
GM="${MYTHRAS_GM_ROOT:-$HOME/mythras-gm}/skills/mythras-gm"

if [ ! -f "$GM/mapgen.py" ]; then
  echo "mapgen not found at $GM. Set MYTHRAS_GM_ROOT to the engine checkout." >&2
  exit 1
fi

run() { uv run -q --project "$GM" python "$GM/mapgen.py" --campaign "$CAMPAIGN" "$@"; }

if [ $# -gt 0 ]; then
  SLUGS="$*"
else
  SLUGS=$(grep -l "^revision:" "$CAMPAIGN"/maps/areas/*.md | sed "s#.*/##; s#\\.md\$##")
fi

fail=0
for s in $SLUGS; do
  echo "--- $s"
  if ! run render "$s" --revise --res 4K --quality max; then
    fail=$((fail+1))
    echo "    ^ failed; continuing" >&2
  fi
done
echo
echo "done; $fail failed"
[ "$fail" -eq 0 ]
