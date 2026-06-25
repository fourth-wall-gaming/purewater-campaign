# AI Map-Generation Prompt — The City of Purewater

A prompt for a top-down city map of **Purewater** in the style of the classic 1980s
*City of Sanctuary* tabletop map (the supplied reference): black pen-and-ink on aged
parchment with grey wash, labeled districts, hatched water, compass rose, scale bar,
title cartouche. The whole document is kept under ~9000 characters so it can be
pasted whole or section-by-section.

## THE THREE RULES (what renders get wrong)

1. **Flat plan view, no 3D.** Strict top-down orthographic projection (camera straight
   down, 90° overhead) — an **architect's floor plan / cadastral survey**. NO
   bird's-eye, oblique, isometric or perspective; NO 3D house icons; NO cast shadows,
   hill-shading, relief, vignette or "epic fantasy atlas" flourishes. Flat and archival.
2. **Organic, irregular islands.** Ragged, asymmetrical coastlines and canal banks like
   a real silted lagoon or river delta (Venice). NO smooth ovals, round blobs,
   concentric rings or symmetry.
3. **Resolvable to individual houses.** Every building a separate tiny rectangular
   footprint seen from directly overhead, packed tightly along streets so the city
   reads house-by-house — like the reference map. NOT impressionistic blocks.

## MASTER PROMPT (paste this)

> A strict **top-down orthographic plan-view** map of **Purewater**, a Venice-like
> canal city, drawn flat like an antique **cadastral survey / architect's floor plan**
> — NOT 3D, bird's-eye, oblique or isometric. Hand-drawn black **pen-and-ink** on aged
> off-white parchment with light grey wash, in the style of the 1980s *City of
> Sanctuary* tabletop map. Flat, even, **shadowless** lighting; no relief. Every
> building is a **separate tiny rectangular footprint** seen from straight overhead,
> packed along the streets so the city resolves **house-by-house**; one-storey =
> plain outline, two-or-more = double-lined box. Districts are dense blocks of these
> footprints divided by a web of **narrow, crooked, branching canals** of varying
> width, crossed by **many small bridges**; boats as simple flat ovals. Islands have
> **ragged, organic, asymmetrical** coastlines like a silted delta — no smooth ovals.
>
> LAYOUT — a **strait-city** across "the Mouth," where a sacred **Lake (top/north)**
> drains south to the **open Sea (bottom/south)**. A great irregular **triangular
> central island, HIGH ISLE**, is wedged in the strait and split by the broad
> branching **Grand Canal** into quarters: a **governor's palazzo, hall of justice,
> barracks and walled tournament ground** on its north-east; a **merchant quarter**
> (guild halls, market plaza) on its south-west; **smoking forges and foundries** on
> its east point; dense housing along the north edge sloping rich-to-poor eastward. A
> thin **promontory** reaches in from the west to a land-gate outcrop (**Caravan
> Square**, the only road in) — the southern jaw of the Mouth. A **peninsula of docks,
> wharves and fish-markets** (**the Shoals**, with a harbor-master's tower) forms the
> eastern, seaward jaw. Across a canal east of High Isle sprawls a low
> **slum-and-thieves quarter** of the narrowest, most tangled canals (**the
> Lullwater**). Off the north-east, alone and **unbridged**, a small **temple island**
> drawn as formal sacred architecture — a temple precinct and a round **sacred pool**.
> Scattered north across the calmer lake, a handful of small islands: lamp-lit
> **pleasure-houses**, quiet **noble retreats**, and **half-drowned ruins**. A single
> **dragon-prowed barge** at a pier on High Isle's eastern, seaward side, faint steam
> where its hull meets the water.
>
> MARGINS (flat, plain): reedy lake-shore and low hills north; open sea south;
> mainland marsh, farms and a caravan road to the western land-gate. Hand-lettered
> labels for districts and key buildings; a decorative title cartouche **"THE CITY OF
> PUREWATER"** with a small **scale bar** ("ONE INCH = 200 FEET"); an ornate **compass
> rose** (N up); a small **legend** (bridge, one-storey, two-storey, temple, canal); a
> thin decorative border; subtle aged-paper texture. Monochrome black / grey /
> parchment. Crisp, technical, archival pen-and-ink cartography. Landscape ~3:2.

## NEGATIVE PROMPT (paste into the negative field)

> 3D, isometric, oblique, bird's-eye perspective, axonometric, fake depth, little
> house icons, pitched roofs in perspective, building elevations, drop shadows, cast
> shadows, ambient occlusion, hill shading, relief, dramatic lighting, atmospheric
> haze, vignette, glow, painterly, epic fantasy atlas style, smooth oval island,
> round blobby island, concentric rings, symmetrical coastline, blurry blocks,
> impressionistic massing, low detail.

## LABELS (for hand-placement if the AI mangles text)

**Waters:** The Lake · The Mouth · The Sacred Confluence · The Grand Canal · The Open Sea
**Districts/islands:** High Isle (Merchant's Quarter · Forge Quarter · Palace Square) ·
The Lullwater · The Shoals · Caravan Square · Temple Isle · The Pearl · Lost Isle ·
The Northern Isles
**Sites:** Governor's Palazzo · Hall of Justice · Barracks · Tournament Grounds · The
DragonBarge (pier) · Watercrafters' Guild · The Sylph's Embrace · The Siren's Call ·
The Promise of Heaven · The Moist Oyster · The Dredgers' Hall · Harbor Masters' Tower
**Ways/gates:** Pearl Quay · The Gate of Triumph · the Processional (High Isle's grand
east–west way)

> *Secret — do NOT label:* the Quiet Hand, the Mermaid's Court, the Catacombs (the last
> may be hinted with a couple of stair-mouth symbols by the Lullwater and the temples).

## NOTES

- **Model drift:** GPT-image / DALL·E default to the oblique "fantasy atlas" look.
  Counter it by leading with the projection words (**"architect's floor plan,"
  "cadastral survey," "orthographic top-down," "site plan"**) and pasting the negative
  prompt. If it still renders 3D, add *"flat 2D blueprint, zero perspective,
  nadir/zenithal view"* and drop any cinematic/stylize setting.
- **Reference image:** feed the *City of Sanctuary* map as a style reference (Midjourney
  `--sref` or image prompt) to lock the pen-and-ink + parchment look, while following
  the layout above. Add `--ar 3:2`.
- **Two-pass (best results):** dense house-level detail and many labels rarely survive
  one generation. (1) Generate flat island-and-canal coastlines + districts; (2)
  inpaint individual building footprints district by district; (3) typeset the labels
  by hand.

## SPATIAL GUIDE

```
 N ^            T H E   L A K E   (sacred, inland)
   [Pearl] [Lost Isle] ...Northern Isles...   [Temple Isle]
                                              (unbridged; temple
   ~~~~~~~~~ the lake flows south ~~~~~~~~~~    + round pool)
                 ___________________
   (Caravan     /  HIGH ISLE (tri.) \
    Sq. + gate)/  NW pt   official/  \
   ===W jaw===<  Merchant | noble(NE) >=== E pt ===>  [THE SHOALS]
               \  (SW) ~Grand Canal~  /   (docks, seaward jaw)
                \__ Forge(E); barge _/          |
                      | canal east of High Isle |
                   [ THE  LULLWATER ] (slum+thieves)
 S v            T H E   O P E N   S E A
 (the Mouth = the strait the lake drains through; bridges everywhere;
  Catacombs run unseen beneath)
```
