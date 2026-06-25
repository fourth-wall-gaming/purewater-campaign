# AI Map-Generation Prompt — The City of Purewater

A prompt for generating a top-down city map of **Purewater** in the style of the
classic 1980s tabletop **City of Sanctuary** map (the supplied reference): black
ink line-art on aged parchment with grey ink-wash, labeled districts and streets,
hatched water and terrain, a compass rose, a scale bar, and a decorative title
cartouche.

The one essential adaptation: **Sanctuary is a single walled landmass with a river
and a harbour; Purewater is an archipelago** — a Venice-like web of islands threaded
by canals and stitched together by arched bridges, set where the sacred lake pours
out to meet the open sea.

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
> blobs. A large central island (**High Isle**) ringed by a broad **Grand Canal**
> holds a governor's palazzo and a walled tournament ground; a northern **Temple
> Isle** holds a round sacred pool; a western **Pearl Quarter** of pleasure-houses
> lines a quay; an eastern **Forge Isle**; a half-sunken ruined isle to the
> south-west; crowded slum and dock districts (**the Maze, the Warren, the Shoals**)
> along the southern seaward edge with wharves jutting into the harbour; a single
> **dragon-prowed barge** at a pier on High Isle's eastern side. Margins, all drawn
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

## 3. Geography & orientation

- **North (top) = the Lake.** The sacred inland waters; reedy, calm, with low hills
  on the far shore.
- **South (bottom) = the Open Sea.** The working harbour, wharves, and the horizon.
- **The city sits in the meeting-zone**, its islands divided by a web of canals and
  joined by bridges. The whole place reads as *water first, land second*.
- **West (left) = the mainland approach:** marsh, farms, and a caravan road running
  to a landward gatehouse and a caravan staging-square.
- **East (right) = open water and the seaward forge-isle.**

## 4. Islands & districts (placement + what to draw)

| Island / district | Position | Draw |
|---|---|---|
| **Temple Isle** | north / top-centre, nearest the lake | white-stone temples, domes, sacred pools; a great **round Sacred Confluence pool** where lake meets sea |
| **High Isle** (the heart) | centre, encircled by the broad **Grand Canal** | the **Governor's Palazzo** (Prince Emeric's seat), the **Hall of Justice**, walled **Tournament Grounds** (archery ranges firing across water, combat lists), grand noble palazzi |
| **The DragonBarge** | a private pier on High Isle's **eastern** side | a huge **dragon-prowed war-barge**, steam/smoke rising where its hull meets the water; a few guard-boxes |
| **Merchant's Isle** | north-east | guild halls, the **Watercrafters' Guild**, counting-houses, a market plaza, merchant-prince palazzi |
| **The Pearl Quarter** (Pleasure Islands) | west, across from High Isle | lamp-lit pleasure houses along the **Pearl Quay**; label the **Sylph's Embrace**, the **Siren's Call**, the Aphrodisia House, the Promise of Heaven |
| **Forge Isle** | east / south-east | dwarven forges and foundries, chimneys trailing smoke, ironwork |
| **The Maze** | south-centre | a dense tangle of crooked islets and the narrowest canals; crowded tenements; the **Moist Oyster** tavern |
| **The Warren** | south, beside the Maze | the poor district; the **Dredgers' Hall**; washing strung over the canals |
| **Lost Isle** | south-west | half-sunken **drowned ruins** rising from weed-choked water; deserted |
| **The Shoals** | far south, seaward edge | working **docks and fish-markets**; wharves and jetties jutting into the harbour; the **Harbor Masters' tower**; smugglers' moorings |
| **Caravan Square & the Gate of Triumph** | west, landward edge | a walled land-gate and caravan staging-yard where the borderland road meets the first island |

> *Not shown:* the **Catacombs** run beneath the whole city (optionally hint with a
> couple of stair-mouth symbols by the Maze and the temples). The **Quiet Hand** and
> the **Mermaid's Court** are secret and must NOT be labeled.

## 5. Water, bridges & boats

- A **Grand Canal** ring around High Isle, broad enough for barges.
- A dense network of **lesser canals** dividing every district; the Maze's are
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

**Waters:** The Lake · The Sacred Confluence · The Grand Canal · The Open Sea · the Harbour
**Islands/districts:** Temple Isle · High Isle · Merchant's Isle · The Pearl Quarter · Forge Isle · The Maze · The Warren · Lost Isle · The Shoals
**Buildings/sites:** Governor's Palazzo · Hall of Justice · Tournament Grounds · The DragonBarge (pier) · Watercrafters' Guild · The Sylph's Embrace · The Siren's Call · The Promise of Heaven · The Aphrodisia House · The Moist Oyster · The Dredgers' Hall · Harbor Masters' Tower
**Ways/gates:** Pearl Quay · The Gate of Triumph · Caravan Square · the Processional (High Isle's grand way)

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
            N  ^    THE   LAKE   (sacred, inland)
        ~~~~~~ Sacred Confluence ~~~~~~
        [Temple Isle]        [Merchant's Isle]
   [Pearl Quarter] --(Grand Canal ring)-- 
        [ ~~~  H I G H   I S L E  ~~~ ]==[Forge Isle]
              Governor's Palazzo;  DragonBarge pier (E)
        [Lost Isle]   [The Maze]==[The Warren]
   (Gate of Triumph,        |
    Caravan Sq. — W)   [ T H E   S H O A L S ]  docks/wharves
            S  v    THE   OPEN   SEA
   ( bridges everywhere; canals between every island;
     the Catacombs run unseen beneath it all )
```
