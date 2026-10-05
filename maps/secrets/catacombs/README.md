# The Catacombs -- GM ONLY

**Nothing in this folder is for players.** The Catacombs are never lettered on a
player map (see `../../README.md`). The canon is the GM guide
`lore/gm-guide/gm-guide-the-catacombs.md`.

- `plan.yaml`: where the three layers run (the Ossuary, the Old Water, the
  smugglers' runs), their chambers and the nine entrances, as fractions of the
  city map.
- `overlay.py`: draws `catacombs-overlay.jpg`, the plan over the city map with a key.
  `overlay.py plain` cuts `request-ossuary.png` (4:3) and `request-oldwater.png`
  (3:4), the plan without labels, as images for ElevenLabs to edit.
- `prompt-ossuary.txt`, `prompt-oldwater.txt`: the redraw prompts. The coloured
  lines in the request images pin where every tunnel goes, the way the city crop
  pins every coastline on the district sheets. The prompts turn them into
  pen-and-ink galleries and conduits under a ghosted city, with no lettering.
- `the-ossuary.jpg`, `the-oldwater.jpg`: the finished GM sheets, lettered by
  `maps/sheet.py secrets/catacombs/ossuary label` and `... secrets/catacombs/oldwater label`
  from `ossuary/labels.yaml` and `oldwater/labels.yaml`. Their ▲ marks are the ways
  in; the numbers match nothing on the overlay, which keeps its own.

The Old Water redraw zoomed out and painted invented city around the request
image. The sheet is cropped back to where the request sits inside it (found by
template matching), so the city on it is the canon map, ghosted.
