# The Lullwater sheet

*The method is written up for all the sheets in `../../README.md`; this is the
first one, and its notes on tools still apply.*

A detailed map of the Lullwater. Its source is `lullwater_no_text.png`, a text-free
redraw of the Lullwater and its surroundings made from the city map
(`../../purewater-map.png`, canon). `prep` crops the island from it, and every later
step keeps that frame.

Earlier attempts gave a model the city map as a *reference* and asked it to draw a
district. It redrew the district from scratch, wrongly. This sheet never asks a
model to draw the shape or to letter anything:

1. **The shape is cut, not drawn.** `prep` crops the island from the source.
2. **The model only edits.** It gets `edit-me.jpg` as the image to *edit*, not as a
   reference, and `prompt.txt` asks it to sharpen and add house-level detail inside
   the frame, with no lettering at all.
3. **The names are set by script.** `label` letters `labels.yaml` onto whatever
   comes back, at fixed fractions of the frame. The spelling, the placement and
   the absence of any secret are guaranteed.

```bash
uv run maps/sheet.py districts/lullwater prep                       # crop.png, edit-me.jpg, lines.png
# edit edit-me.jpg with prompt.txt; save the result here as render.png
uv run maps/sheet.py districts/lullwater label maps/districts/lullwater/render.png        # render-labelled.png
```

## Which tool, which mode

- **Use an edit mode**: an image *edit*, inpaint or img2img mode, never "generate
  with a reference image". GPT-image and Gemini both have one.
- **img2img with a strength setting:** 0.3–0.45. Higher than that and it redesigns.
- **For a hard lock** (Stable Diffusion or Flux): put `lines.png` into a ControlNet
  lineart or canny model at full weight, and `edit-me.jpg` into img2img. The
  linework cannot move.
- **Check the result against `crop.png` before labelling.** If the outline moved,
  re-roll; the labels will not line up with a moved coast.

## Names

`labels.yaml` sets the title and the key in ruled panels off the island, marks
each site with a numbered cross named in the key (the Moist Oyster, the Dredgers'
Hall, Shilling Stairs, the Still, the Gutter), and letters the Hook and Eel Bay
where they lie. All of them are recorded in `locations/the-lullwater.md`. Move a
name by editing its `x`, `y` and re-running `label`. Never letter the Quiet Hand,
the Mermaid's Court or the Catacombs.

`lullwater_no_text.png` is about 42 MB, and `crop.png` and `lines.png` are full
size. Decide deliberately before committing them (see the repo-size note in the
root README).
