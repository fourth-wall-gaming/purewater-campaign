# Review of the first render pass

> **Acted on.** Five sheets are kept as finished; the other fourteen have had
> their specs rewritten with a `revision:` note naming the faults below, and are
> ready to re-roll with `mapgen render <slug> --revise`, which passes the
> previous image back as a second reference. The seven cross-cutting faults are
> fixed in `_style-cadastral.md` and `_style-floorplan.md`.
>
> **Kept (4+ in all three):** caravan-square · temple-isle · the-forge-quarter ·
> the-moist-oyster · the-siren-s-call

Nineteen sheets, scored out of 5 for **(A) playability** — can you run a scene
off it; **(B) fidelity** — is it true to the setting and consistent with
`../purewater-map.png`; **(C) creativity** — does it add something.

| sheet | A | B | C | the one thing to fix |
|---|:-:|:-:|:-:|---|
| the-siren-s-call | 4 | 5 | 5 | no room labels at all |
| temple-isle | 4 | 5 | 5 | cartouche says "The City of Purewater" |
| the-forge-quarter | 4 | 4 | 5 | forges indistinguishable from houses |
| the-moist-oyster | 5 | 4 | 4 | no room labels; no cellar drawn |
| caravan-square | 5 | 4 | 4 | "Carravan"; Land Gate on the wrong side |
| high-isle-palace-quarter | 5 | 4 | 3 | Tournament Ground drawn empty |
| the-sylph-s-embrace | 5 | 4 | 3 | nowhere for the women to *live* |
| the-merchant-s-quarter | 5 | 3 | 4 | street grid too regular; no inner canals |
| high-isle-seaward | 4 | 4 | 3 | duplicates the Harbour Master's Tower |
| the-lullwater | 4 | 4 | 3 | canals not tangled enough for a maze |
| the-northern-isles | 4 | 3 | 5 | every island a smooth oval |
| the-vantt-estate | 5 | 3 | 4 | scale ~4x too small; 4 gates unmarked |
| the-ford-and-the-ashwick-road | 4 | 3 | 4 | distant city drawn in elevation |
| the-shoals | 4 | 3 | 3 | Harbour Master's Tower in the wrong place |
| the-tournament-grounds | 5 | 2 | 4 | water is south; on the master it is north |
| the-catacombs | 4 | 2 | 3 | generic dungeon, not a *drowned* one |
| the-pearl | 3 | 2 | 2 | five identical boxes in a row |
| purewater-region | 3 | 1 | 3 | High Isle is not one triangular island |
| the-mother-of-pearl | 1 | 2 | 2 | **no rooms for the women to work in** |

## The premise did not actually land

**Every sheet is 1024x768** — identical to the master. The point of the exercise
was higher resolution, and we have none. The per-sheet aspect ratios were also
ignored: `purewater-region` and `the-ford` were specified 16:9, the set-pieces
3:2, and all nineteen came back 4:3.

The sheets *are* zoomed — scale bars read 50 or 100 feet to the inch against the
master's 200 — so the framing worked. There are just no more pixels to carry it.
Re-run at `--res 4K` with the aspect honoured and most of the detail complaints
below soften on their own.

## Cross-cutting faults, worth fixing once in the style blocks

1. **Eighteen of nineteen cartouches read "THE CITY OF PUREWATER".** The style
   block says to reproduce the master's furniture, and the model dutifully
   reproduced its *title* too. Only `purewater-region` named itself. Fix: state
   that the cartouche must read this sheet's own title, never the master's.
2. **Smooth coastlines.** Rule 2 is the most-broken rule in the set — the
   Northern Isles are lozenges, the Pearl is a smooth lenticular blob, the region
   map's islands are rounded. Fix: move rule 2 to the top, and say explicitly
   that an island whose outline could be drawn with one smooth curve is wrong.
3. **Regularised street grids.** The Merchant's Quarter and the Shoals read as
   rectilinear planned towns. The setting is a silted delta where gondolas are
   the streets. Fix: demand that most blocks be irregular quadrilaterals, that
   streets bend and dead-end, and that **canals thread the interior** of every
   district rather than only bounding it.
4. **Three-dimensionality creeping back.** Floorplan walls are drawn with a
   bevel and drop-shadow; the tournament stands are tiered in perspective; the
   Ford's distant city is a skyline *elevation* on a top-down sheet. Fix:
   restate that walls are flat filled lines with no shading, and that distance
   is shown by drawing less, never by drawing a horizon.
5. **Room labels are inconsistent.** Sylph's Embrace and Mother of Pearl label
   every room; Siren's Call and Moist Oyster label none, which badly hurts two
   otherwise excellent sheets. Fix: make the instruction non-optional in
   `_style-floorplan.md`.
6. **Lettering garbles.** "PRŎHĬSE OF E HEAVEN", "The Carravan Road",
   "ONE-STOBEY", "The The Shoals", "T VAnTT ESTATE". Expected, and the reason
   each spec carries a `labels:` list — these need a typesetting pass or a
   re-roll.
7. **Warm sepia drift.** The set is browner than the master, which is cooler
   black-grey on off-white. Fix: name the master's palette as the target
   explicitly and forbid sepia and brown ink.

## Contradictions between sheets

- **The Harbour Master's Tower appears twice**, on `high-isle-seaward` and
  `the-shoals`, in different places. The master puts it on High Isle's seaward
  point, so the Shoals sheet is the wrong one. My spec caused this by saying
  "mark it if it falls within this sheet's frame" — delete that line.
- **The Tournament Ground is an empty walled rectangle** on
  `high-isle-palace-quarter` but a full set-piece on `the-tournament-grounds`.
  The district sheet should show the lists and butts in outline.
- **The tournament sheet puts the water south.** On the master that ground faces
  the Sacred Lake to the **north**, with Temple Isle north-east — which is the
  whole reason the Washing is visible from the stands. Re-render with the lake
  north.
- **`purewater-region` contradicts the master's basic geography.** High Isle is
  one great irregular *triangular* island split by the Grand Canal; the region
  sheet draws four or five separate blobs and moves the Shoals to the south-east.
  This sheet needs the master's island outline stated in the brief, not inferred.

## Buildings that do not work as buildings

This is the class of fault worth most attention, because a plan can be beautiful
and still be useless if the rooms do not match what happens in the building.

- **The Mother of Pearl has no rooms for the women to see clients.** It is the
  oldest and most powerful house on the Pearl, and the plan gives it a doorman's
  lodge, a receiving room, a garden court, a linen room and the mistress's
  apartments. That is a merchant's villa. **This is my spec's fault** — I wrote
  the brief around Marisette's control of approach and never said what the
  building is for. It also needs to be much bigger than its 25-foot scale bar.
  It should have: a tier of well-appointed client chambers above the receiving
  floor, better furnished than the Sylph's; **private quarters for the women who
  work there**, which is what "a night is for sale; a person is not" implies in
  architecture; a discreet second stair so a guest never crosses a resident; and
  a back landing for arrivals who must not use the front door.
- **The Sylph's Embrace** has six client chambers and nowhere for the courtesans
  to sleep. Add a garret or a rear range.
- **The Vantt Estate** is the softer target precisely because it is porous, and
  the plan does not mark the four gates that make it so. Add them, and the
  farrier's boy's route through the horse lines.
- **The Moist Oyster** needs its cellar drawn — the hatch is there, the cellar
  is not, and a smuggling tavern in the Lullwater without a cellar is a missed
  opportunity sitting right next to an unlabelled stair-mouth.
- **The Pearl's five houses are blank boxes** of identical size. They are the
  campaign's opening scene. Each needs its own footprint, its own water-stair,
  and the Mother of Pearl visibly the largest and plainest.

## What went right, and should not be lost

- `temple-isle` is exactly what its location file's "For the mapmaker" note
  asked for: formal, axial, geometric, unbridged.
- `the-siren-s-call`'s **undercroft** — vaulted, water running in, a boat moored
  inside, labelled only "Undercroft" so the secret holds — is the best single
  idea in the set.
- The **drowned bell-tower** on the Northern Isles, showing only its top above
  water, was one line in a spec and came back perfectly.
- The Pearl's **strung lamps** drawn as actual catenary lines between houses.
- `the-forge-quarter`'s **slipways with part-built hulls**, and the DragonBarge
  in plan at its private pier.
- The district sheets carry the master's legend, compass and scale idiom almost
  exactly. The house style transferred; it is the geography and the function
  that need work.
- **No secret was leaked.** Nothing on any sheet names the Quiet Hand, the
  Mermaid's Court or the Catacombs, and `the-catacombs` is unlabelled apart from
  its title, as instructed.
