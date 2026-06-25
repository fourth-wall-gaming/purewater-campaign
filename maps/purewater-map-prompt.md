# AI Map-Generation Prompt — The City of Purewater

A prompt for generating a top-down city map of **Purewater** in the style of the
classic 1980s tabletop **City of Sanctuary** map (the supplied reference): black
ink line-art on aged parchment with grey ink-wash, labeled districts and streets,
hatched water and terrain, a compass rose, a scale bar, and a decorative title
cartouche.

The one essential adaptation: **Sanctuary is a single walled landmass with a river
and a harbour; Purewater is a strait-city** — built across **the Mouth**, the narrow
choke-point where the sacred lake drains south to the open sea. A great triangular
central island splits the flow between two land-jaws (a western promontory and an
eastern dock-peninsula), with a scatter of smaller islands across the calmer lake to
the north — all threaded by canals and stitched together by arched bridges.

---

## 0. THE THREE RULES (read first — these are what most renders get wrong)

1. **Strict flat plan view — no 3D.** A true top-down orthographic projection
   (camera pointing straight down, 90° overhead), like an **architect's floor plan**
   or an antique **cadastral / land-survey map**. **No** bird's-eye, oblique,
   isometric, or perspective view; **no** little 3D house icons with visible
   walls/roofs; **no** cast shadows, hill-shading, relief, vignette, or "epic
   fantasy atlas" flourishes. Flat, even, diffuse — technical and archival.
2. **Organic, irregular islands.** Ragged, asymmetrical coastlines and canal banks
   like a real silted **lagoon or river delta** (the irregular islands of Venice),
   with crooked, branching canals of varying width. **No** smooth ovals, round
   blobs, concentric rings, or symmetrical shapes.
3. **Resolvable to individual houses.** Every building is a **separate tiny
   rectangular footprint** seen from directly overhead, packed tightly along streets
   so the city reads house-by-house — exactly like the reference *City of Sanctuary*
   map (one inch ≈ 200 ft). **Not** impressionistic blocks or texture.

## 1. Master prompt (paste-ready)

> A **strict top-down orthographic plan-view** map of **Purewater**, a Venice-like
> canal city of many irregular islands where a sacred lake (top / north) meets the
> open sea (bottom / south) — drawn flat like an antique **cadastral survey** or
> **architect's floor plan**, **not** a 3D, bird's-eye, oblique or isometric view.
> Hand-drawn black pen-and-ink line-art on aged off-white parchment with light grey
> wash, in the style of the classic 1980s *City of Sanctuary* tabletop map. **Every
> building is a separate tiny rectangular footprint seen from directly overhead**,
> packed tightly along the streets so the city resolves house-by-house. Districts are
> dense blocks of these footprints divided by a web of **narrow, crooked, branching
> canals** of varying width, crossed by many small bridges; boats drawn as simple
> flat ovals on the water. The **islands have ragged, organic, asymmetrical
> coastlines** like a real silted lagoon or river delta — no smooth ovals or regular
> blobs. The city straddles **the Mouth** -- the narrow strait where the lake
> empties south to the sea. A great irregular **triangular central island (High
> Isle)** is wedged in the strait, split by the broad branching **Grand Canal** into
> quarters: a governor's palazzo and walled tournament ground on its north-east, a
> merchant quarter on its south-west, smoking forges on its east. A thin **promontory**
> with a land-gate (the Caravan Square outcrop) reaches in from the west to form the
> southern jaw of the Mouth; a **peninsula of docks and wharves** (the Shoals) forms
> the eastern, seaward jaw. Across a canal east of High Isle sprawls a low
> **slum-and-thieves quarter** of the narrowest, most tangled canals. Off the
> north-east, alone and **unbridged**, sits a small **temple island** with a round
> sacred pool. Scattered north across the calmer lake lie a handful of small islands
> -- pleasure-houses, court retreats, and half-drowned ruins. A single
> **dragon-prowed barge** sits at a pier on High Isle's eastern, seaward side, steam
> rising where its hull meets the water. Margins, all drawn
> flat and plain: reedy lake-shore and low hills north, open sea south, mainland
> marsh, farms and a caravan road to a land-gate west. Hand-lettered labels; a
> decorative title cartouche "THE CITY OF PUREWATER"; compass rose; scale bar; small
> legend; thin border. **Flat, even, shadowless lighting; no relief shading.**
> Monochrome black / grey / parchment. Landscape ~3:2. Crisp, technical, archival
> pen-and-ink cartography.

### 1a. Negative prompt (paste into the negative field)

> 3D, isometric, oblique, bird's-eye perspective, axonometric, dimetric, fake depth,
> little house icons, pitched roofs in perspective, building elevations, drop
> shadows, cast shadows, ambient occlusion, hill shading, relief, bump-mapped
> terrain, dramatic lighting, atmospheric haze, vignette, golden-hour glow, painterly,
> epic fantasy atlas style, smooth oval island, round blobby island, concentric
> rings, symmetrical coastline, blurry blocks, impressionistic massing, low detail.

---

## 2. Style & medium

- **Technique:** hand-drawn pen-and-ink cartography; the look of a Chaosium/TSR-era
  boxed-set city map. Confident black linework, no digital gloss.
- **Tone/shading:** soft grey ink-wash for water and elevation; the bulk of the
  paper left light. Buildings are outline-only with occasional hatching.
- **Buildings:** drawn as tiny outlined rectangles seen from above — *one-storey* as
  a plain outline, *two-or-more-storey* as a double-lined or lightly hatched box,
  packed into dense blocks for crowded districts and spaced out for grand ones.
- **Water:** rendered with fine parallel contour-hatching and stippling along the
  canal edges and shorelines; broad channels and the sea in light grey wash.
- **Bridges:** small double-line spans crossing the canals — many of them; this is a
  bridge-city.
- **Labels:** hand-lettered. District names in larger serif/italic small-caps; street
  and building names smaller. (See the label list in §8 — AI text is unreliable, so
  either accept stylised lettering or generate clean linework and add labels later.)
- **Palette:** monochrome — black ink, greys, aged off-white parchment. (Optional
  tinted variant in §7.)

## 3. Geography & orientation — the Mouth

Purewater is **not** a concentric ring of districts. It is a **strait-city** built
across **the Mouth**, where the sacred Lake drains to the open Sea.

- **North (top) = the Lake** (sacred, calm, with the scattered Northern Isles and,
  off to the north-east, the unbridged Temple Isle). **South (bottom) = the open
  Sea.** The lake's water flows south through the Mouth, dividing around High Isle
  and rejoining to pour seaward.
- **The two jaws of the Mouth:** a thin **promontory** reaches in from the **west**
  (mainland), ending in the **Caravan Square** outcrop with its land-gate — the
  southern jaw; a **peninsula** set a little north and east carries **the Shoals**
  (docks) — the eastern/seaward jaw.
- **High Isle** sits between the jaws, a great **triangular** island splitting the
  flow: SW point toward Caravan Square, E point toward the Shoals, NW point facing
  the open Lake.

## 4. Islands & districts (placement + what to draw)

| Island / district | Position | Draw |
|---|---|---|
| **High Isle** (the heart) | centre of the Mouth; irregular **triangle**, split by the branching **Grand Canal** | NE: **Governor's Palazzo** (Prince Emeric), **Hall of Justice**, **Barracks**, **Palace Square**, noble palazzi, walled **Tournament Grounds**. SW: the **Merchant's Quarter** (guilds, **Watercrafters**, market plaza). E point: the **Forge Quarter** (smoking forges, foundries). North edge: dense housing sloping rich→middling east toward the canal-mouth |
| **The DragonBarge** | private pier on High Isle's **eastern, seaward** side, by the forges | a huge **dragon-prowed war-barge**, steam/smoke rising where its hull meets the water; guard-boxes |
| **Caravan Square** | tip of the thin **western promontory** | the **Gate of Triumph**, caravan staging-yard, beast-pens; the only land approach |
| **The Shoals** | the **eastern/north-east peninsula** forming the seaward jaw | **docks, fish-markets**, wharves & jetties into the sea, the **Harbor Masters' tower**, smugglers' moorings |
| **The Lullwater** | a low quarter **across the canal east of High Isle**, sloping toward the Shoals | the **densest, most tangled narrow canals**; crowded leaning tenements; the **Moist Oyster** tavern and the **Dredgers' Hall** (poor + criminal, combined) |
| **Temple Isle** | small island **off the NE edge, unbridged** | rendered as **formal sacred architecture** (see §4a): temple precinct + round **Sacred Confluence** pool |
| **The Pearl** | a small island in the **Northern Isles** scatter | lamp-lit pleasure houses along the **Pearl Quay**: the **Sylph's Embrace**, the **Siren's Call**, the Promise of Heaven, the Aphrodisia House |
| **Lost Isle** & other Northern Isles | scattered **north** across the calmer lake | half-drowned **ruins** rising from weedy water; a few quiet **court-retreat** villas; one or two **shunned / haunted** islets |

> **§4a — Temple Isle exception:** draw it *not* as house-rooftops but as a **planned
> architectural ground-plan** — colonnaded approach, the temple, a ring of small
> shrines, and the geometry of the round Confluence pool with its channels and basins.

> *Not shown:* the **Catacombs** run beneath the whole city (optionally hint with a
> couple of stair-mouth symbols by the Lullwater and the temples). The **Quiet Hand**
> and the **Mermaid's Court** are secret and must NOT be labeled.

## 5. Water, bridges & boats

- The **Grand Canal** does not ring High Isle — it **bisects and branches across
  it**, broad enough for barges, carving the island into its quarters.
- A dense network of **lesser canals** dividing every district; the Lullwater's are
  narrowest and most tangled.
- **Many arched stone bridges** — dozens — linking the islands.
- Scattered **gondolas and small boats** on the canals; larger vessels and the
  DragonBarge in the deeper channels; fishing craft and wharf-shipping in the
  southern harbour.
- A faint haze of **steam/mist** around the DragonBarge and the corrupted channels
  near it.

## 6. Cartographic furniture

- **Title cartouche** (bottom corner): an ornate scrolled banner reading
  **"THE CITY OF PUREWATER"**, with a small line beneath: *"MAP SCALE: ONE INCH = 200 FEET."*
- **Compass rose** (bottom corner): ornate, N at top.
- **Scale bar.**
- **Legend box:** symbols for *bridge*, *one-storey house*, *two-or-more storeys*,
  *temple*, *guard-post*, *canal / open water*.
- **Decorative thin border** framing the whole sheet; subtle aged-paper texture and
  a faint fold-crease for authenticity.

## 7. Variations

- **Monochrome (default):** black/grey/parchment, matching the reference.
- **Lightly tinted:** keep the ink style but wash the water in muted **teal-grey**,
  parchment land, and a touch of warm ochre on roofs — restrained, still antique.
- **Clean plate (recommended for legible labels):** generate the linework with
  *blank* or placeholder labels, then typeset the names from §8 by hand — AI tools
  rarely render this much small text correctly.

## 8. Label list (for hand-placement if the AI mangles text)

**Waters:** The Lake · The Mouth · The Sacred Confluence · The Grand Canal · The Open Sea
**Islands/districts:** High Isle (Merchant's Quarter · Forge Quarter · Palace Square) · The Lullwater · The Shoals · Caravan Square · Temple Isle · The Pearl · Lost Isle · The Northern Isles
**Buildings/sites:** Governor's Palazzo · Hall of Justice · Barracks · Tournament Grounds · The DragonBarge (pier) · Watercrafters' Guild · The Sylph's Embrace · The Siren's Call · The Promise of Heaven · The Moist Oyster · The Dredgers' Hall · Harbor Masters' Tower
**Ways/gates:** Pearl Quay · The Gate of Triumph · the Processional (High Isle's grand east–west way)

## 9. Technical notes

- **Aspect ratio:** landscape, ~**3:2** (the reference is roughly 3:2). For Midjourney
  add `--ar 3:2`; raise quality/stylize as desired.
- **Resolution:** request the largest the tool allows, then upscale — fine linework
  and labels need the pixels.
- **Text caveat:** every current image model garbles dense small text. Either accept
  decorative pseudo-lettering for atmosphere, or use the **clean plate** approach (§7)
  and add the §8 labels in an editor afterward.
- **Reference image:** feed the supplied *City of Sanctuary* map as a style reference
  (Midjourney `--sref` / image prompt, or "in the style of this map") to lock the
  pen-and-ink, parchment, and labeling aesthetic — while following the Purewater
  geography above for the actual layout.
- **Model drift (important):** GPT-image / DALL·E and most models *default to the
  oblique "fantasy atlas" look* — little 3D buildings, dramatic shading, smooth oval
  islands. Counter it by leading with the projection words — **"architect's floor
  plan,"** **"cadastral survey,"** **"orthographic top-down,"** **"ichnographic
  plan,"** **"site plan"** — and by pasting the §1a negative prompt. If it still
  renders 3D, add *"flat 2D blueprint, zero perspective, zenithal/nadir view"* and
  reduce any "epic/cinematic" stylize setting.
- **Two-pass option:** because dense house-by-house detail and many labels rarely
  survive one generation, consider (1) generate the **flat island-and-canal
  coastlines + districts** first, then (2) inpaint/redraw individual building
  footprints district by district, and (3) typeset the §8 labels by hand.

---

## 10. Quick spatial guide (for whoever places the labels)

```
   N  ^            T H E   L A K E   (sacred, inland)
        [Pearl] [Lost Isle] ...Northern Isles...    [Temple Isle]
                                                    (unbridged; temple
        ~~~~~~~~~~~~~~ the lake flows south ~~~~~~~~  + Confluence pool)
                   _______________________
                  /  HIGH ISLE (triangle) \\
   (Caravan Sq.  /  NW pt        official/ \\
    + land-gate)/      Merchant's | noble (NE)\\
   ====W jaw===<  SW pt  (SW) ~Grand Canal~     >== E pt ==>  [THE SHOALS]
                \\        branches    Forge (E) /   (docks, seaward jaw)
                 \\___ DragonBarge pier (E) ___/         |
                        |  canal east of High Isle       |
                     [ THE  LULLWATER ]  (slum+thieves) -/
   S  v            T H E   O P E N   S E A
   ( the Mouth = the strait the lake drains through; bridges everywhere;
     the Catacombs run unseen beneath it all )
```
