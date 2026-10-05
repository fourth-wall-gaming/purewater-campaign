# The Pearl sheet

Made the same way as the Lullwater sheet (see `../lullwater/README.md`), with the
shared script `../../sheet.py`.

```bash
uv run maps/sheet.py districts/pearl request    # request.png: the master crop
# edit request.png in ElevenLabs with prompt.txt; save it here as unlabelled.png
uv run maps/sheet.py districts/pearl prep       # crop.png from it (whole frame)
uv run maps/sheet.py districts/pearl label      # crop-labelled.png
```

Until the redraw exists, `label preview.png` letters a 3x enlargement of the
master crop, to check where the crosses and panels fall.

The sites are the five houses of the Quay, the four named bridges, and the walled
islet the Widow's Bridge reaches. Their placings are recorded in
`locations/the-pearl.md`.
