# Maps

`purewater-map.png` is the city map, and it is **canon**: the geography in
`lore/geography/the-city-and-its-islands.md` and the location files is written to
match it. Where a text and the map disagree, the map wins and the text is wrong.

The district sheets below are enlargements of it, one per part of the city. They
are player-facing: nothing secret is lettered on any of them (the Quiet Hand, the
Mermaid's Court and the Catacombs never are).

## The sheets

| Sheet | Folder | Covers | Location files |
|---|---|---|---|
| [The Lullwater](districts/lullwater/the-lullwater.jpg) | `districts/lullwater/` | the whole island, the Still, the Gutter, Crowbill's haunts, Kag's place | `the-lullwater.md`, `the-moist-oyster.md` |
| [The Pearl](districts/pearl/the-pearl.jpg) | `districts/pearl/` | the Quay and its five houses, the Widow's House, the four Pearl bridges | `the-pearl.md`, the house files |
| [The Shoals](districts/shoals/the-shoals.jpg) | `districts/shoals/` | the Fishmarket, the Low Canals, the jetties, Kag's round, the eastern bridges | `the-shoals.md` |
| [The Lists and Temple Isle](districts/tournament/the-lists-and-temple-isle.jpg) | `districts/tournament/` | the Tournament Ground, Temple Isle, the official quarter's east end | `the-lists.md`, `the-long-butts.md`, `temple-isle.md` |
| [Caravan Square](districts/caravan/caravan-square.jpg) | `districts/caravan/` | the land gate, the Triumph Bridge, the staging grounds | `caravan-square.md` |
| [The Forges and the Docks](districts/forges/the-forges-and-the-docks.jpg) | `districts/forges/` | the Forges, the Seaward Quarter, the DragonBarge pier, the Harbour Master's Tower | `the-forge-quarter.md`, `high-isle.md` |
| [The North Quarter](districts/grandcanal/the-north-quarter.jpg) | `districts/grandcanal/` | the North Quarter, the Palazzo, the Grand Canal and its ferries | `high-isle.md` |
| [The Merchant's Quarter](districts/merchants/the-merchants-quarter.jpg) | `districts/merchants/` | Market Square, the guildhalls, the councillors' palazzi, the cut and its bridges | `the-merchant-s-quarter.md` |

**GM only:** `secrets/catacombs/` holds the plan of what runs underneath the city: an
overlay on this map and the requests for redrawing it. It is never shown to
players; see `secrets/catacombs/README.md`.

**Layout.** `districts/` holds the eight district sheets, `buildings/` the floor
plans of key buildings (one folder each, with a shared `_style-plan.txt`),
`realm/` the map of the kingdom, `secrets/` the GM-only sheets (the Catacombs), and
`encounters/` encounter maps (the DragonBarge). `sheet.py SHEET ...` takes the
folder relative to `maps/`, e.g. `districts/lullwater` or `buildings/the-lists`.

Not yet drawn: the outlying isles (Lost Isle, the Singer's Rest, Northlight) and
the country beyond the city (the Vantt Estate, the Ford and the Ashwick Road).

## What the marks mean

Each sheet has a title panel, a key, and three kinds of numbered mark:

- **✚ a cross** — a place: a building, bridge, stair or landmark that matters in play.
- **● a disc** — a tavern or amenity: inns, baths, physicians, shops, shrines, stalls.
- **■ a square** — a post of the city watch.

Areas and waters are lettered where they lie. Every mark has a matching entry in
the canon: places in the location files' "The lie of it" paragraphs, taverns,
amenities and watch posts in their "Taverns, amenities and the watch" sections,
and every watch post again in `factions/the-city-watch.md`.

## How a sheet is made

The shape of the city must never drift, so no model is ever asked to draw it.

1. **Crop.** `uv run maps/sheet.py SHEET request` cuts the sheet's frame
   (`master_crop` in `labels.yaml`) out of the city map as `request.png`.
2. **Redraw, without lettering.** `request.png` goes into ElevenLabs (a GPT Image
   model, 16:9, 4K) as **the image to edit**, never as a style reference, with the
   sheet's `prompt.txt`. The prompt says to trace everything, keep the frame, add
   house-level detail, and remove every label. The result is saved in the folder
   as `unlabeled.png`. If the redraw has faults, a short fix prompt (see
   `districts/grandcanal/fix-prompt.txt`) asks for those corrections only; small faults can
   be patched by hand.
3. **Crop the drawing.** `sheet.py SHEET prep` cuts `crop` out of the redraw as
   `crop.png` (the whole image, unless the model padded it).
4. **Letter it.** `sheet.py SHEET label` sets the title, marks and key from
   `labels.yaml` onto `crop.png`, as `crop-labelled.png`. Positions are fractions
   of the frame, so they survive a re-roll that keeps the frame; check them anyway.
   Export a JPEG of that for the repo.

`labels.yaml` holds the sheet: `title`, `key` (anchored by `bottom` or `top`,
optionally `columns`), `sites` (each with `type`: `place`, `amenity` or `watch`,
an optional `num` corner for its number, and a `note` that is the canon text for
it), `areas`, and `do_not_label`.

## What is tracked

Only the small files and each sheet's lettered JPEG. The working images
(`request.png`, `unlabeled.png`, `crop.png`, `lines.png`, `edit-me.jpg`,
`crop-labelled.png`) are tens of megabytes each and are ignored: every player
downloads this repository. Keep the redraws somewhere safe, because a sheet cannot
be re-lettered from a clone without its `unlabeled.png`.
