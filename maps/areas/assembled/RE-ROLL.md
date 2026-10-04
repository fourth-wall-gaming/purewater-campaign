# The re-roll: 17 sheets at 4K

Seventeen sheets to redo. Two forms of each prompt — see `README.md` — and for
doing this by hand the simpler one is usually right:

**`assembled/single-reference/<slug>.txt`** — attach only
`maps/purewater-map.png`. All the corrections are written in as positive
instructions.

**`assembled/<slug>.txt`** — attach `maps/purewater-map.png` **first** and
`maps/areas/<slug>.png` **second**. Names the faults to fix and keeps what the
previous render got right. Better, when the tool takes two references and you
get the order right.

Render at **4K**, quality **max**. The first pass came back at 1024x768 — the
same size as the master — which is the single biggest reason the fine detail did
not survive.

`temple-isle` and `the-siren-s-call` are not listed: they are finished.

## By hand

| sheet | prompt file (either folder) | 2nd ref, revision form only | aspect |
|---|---|---|:-:|
| Caravan Square and the Gate of Triumph | `assembled/caravan-square.txt` | `caravan-square.png` | 4:3 |
| High Isle — the Palace Quarter | `assembled/high-isle-palace-quarter.txt` | `high-isle-palace-quarter.png` | 4:3 |
| High Isle — the Seaward Quarter | `assembled/high-isle-seaward.txt` | `high-isle-seaward.png` | 4:3 |
| The Mouth — Purewater and its Hinterland | `assembled/purewater-region.txt` | `purewater-region.png` | 16:9 |
| Beneath the City | `assembled/the-catacombs.txt` | `the-catacombs.png` | 3:2 |
| The Ford and the Ashwick Road | `assembled/the-ford-and-the-ashwick-road.txt` | `the-ford-and-the-ashwick-road.png` | 16:9 |
| The Forge Quarter | `assembled/the-forge-quarter.txt` | `the-forge-quarter.png` | 4:3 |
| The Lullwater | `assembled/the-lullwater.txt` | `the-lullwater.png` | 4:3 |
| The Merchant's Quarter | `assembled/the-merchant-s-quarter.txt` | `the-merchant-s-quarter.png` | 4:3 |
| The Moist Oyster | `assembled/the-moist-oyster.txt` | `the-moist-oyster.png` | 3:2 |
| The Mother of Pearl | `assembled/the-mother-of-pearl.txt` | `the-mother-of-pearl.png` | 3:2 |
| The Northern Isles | `assembled/the-northern-isles.txt` | `the-northern-isles.png` | 4:3 |
| The Pearl and Pearl Quay | `assembled/the-pearl.txt` | `the-pearl.png` | 4:3 |
| The Shoals | `assembled/the-shoals.txt` | `the-shoals.png` | 4:3 |
| The Sylph's Embrace | `assembled/the-sylph-s-embrace.txt` | `the-sylph-s-embrace.png` | 3:2 |
| The Tournament Grounds | `assembled/the-tournament-grounds.txt` | `the-tournament-grounds.png` | 3:2 |
| The Vantt Estate | `assembled/the-vantt-estate.txt` | `the-vantt-estate.png` | 3:2 |

## Or, once the workspace is on a Pro plan

`mapgen` does all of it, attaching both references and writing a provenance
sidecar per sheet. The previous image is copied to `previous/` before being
overwritten, so a revision stays repeatable.

```bash
export ELEVENLABS_API_KEY=...
bash maps/areas/reroll.sh              # all 17
bash maps/areas/reroll.sh the-pearl    # or one at a time
```

Prove the style on one sheet before committing to the full run: seventeen
generations at 4K/max is the most expensive setting there is.
