# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow", "pyyaml"]
# ///
"""A district sheet: cut it from the city map, then letter whatever comes back.

    uv run maps/sheet.py SHEET request          # request.png: the master crop to redraw
    uv run maps/sheet.py SHEET prep             # crop.png, edit-me.jpg, lines.png
    uv run maps/sheet.py SHEET label [IMAGE]    # IMAGE-labelled.png (default crop.png)

SHEET is a directory under maps/ holding a labels.yaml (districts/lullwater, buildings/the-lists).

The generator never letters anything. It edits edit-me.jpg, sharpening and adding
house-level detail inside a frame it is not allowed to move. The names are set
afterwards by `label`, at fixed fractions of the frame, so they are spelled
right, sit in the right place, and never include a secret.
"""
import os
import sys

import yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

MAPS = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(MAPS, "purewater-map.png")
HERE = None  # the sheet directory, set in main
FONT = "/System/Library/Fonts/Supplemental/BigCaslon.ttf"
# lining figures: Big Caslon's old-style 1 reads as a capital I
DIGITS = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"
INK = (28, 28, 30)
PAPER = (236, 231, 218)


def spec():
    with open(os.path.join(HERE, "labels.yaml")) as f:
        return yaml.safe_load(f)


def cmd_request():
    """The master crop to hand an image model for a text-free, high-resolution
    redraw -- the step that made lullwater_no_text.png. Same frame, 16:9."""
    m = spec()["master_crop"]
    im = Image.open(MASTER).convert("RGB").crop((m["x"], m["y"], m["x"] + m["w"], m["y"] + m["h"]))
    im.save(os.path.join(HERE, "request.png"))
    print("request.png %dx%d from the master at (%d, %d)" % (*im.size, m["x"], m["y"]))


def cmd_prep():
    sp = spec()
    c = sp["crop"]
    src = Image.open(os.path.join(HERE, sp["source"])).convert("RGB")
    crop = src.crop((c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]))
    crop.save(os.path.join(HERE, "crop.png"))
    # the image to hand an edit model: JPEG, at most 2048 on the long side
    small = crop.copy()
    small.thumbnail((2048, 2048), Image.LANCZOS)
    small.save(os.path.join(HERE, "edit-me.jpg"), quality=92)
    # black lines on white, for a ControlNet lineart / canny guide
    g = ImageOps.autocontrast(ImageOps.grayscale(crop), cutoff=2)
    g.point(lambda v: 0 if v < 110 else 255).save(os.path.join(HERE, "lines.png"))
    print("crop.png %dx%d, edit-me.jpg %dx%d, lines.png" % (c["w"], c["h"], *small.size))


def tracked(d, pos, text, font, anchor, halo, tracking=0.16):
    """Letter-spaced capitals, as the master sets them. Pillow has no tracking,
    so each letter is placed by hand; the anchor applies to the whole word."""
    text = text.upper()
    gap = font.size * tracking
    widths = [font.getlength(ch) for ch in text]
    total = sum(widths) + gap * (len(text) - 1)
    x, y = pos
    x0 = {"l": x, "m": x - total / 2, "r": x - total}[anchor[0]]
    xs = []
    for w in widths:
        xs.append(x0)
        x0 += w + gap
    # every halo first, then every letter, so no halo paints over a neighbour
    for ch, xi in zip(text, xs):
        d.text((xi, y), ch, font=font, fill=PAPER, anchor="l" + anchor[1],
               stroke_width=halo, stroke_fill=PAPER)
    # Big Caslon's hairlines (the bar of the H) vanish at small sizes; a thin
    # stroke in the ink colour keeps them
    weight = max(1, round(font.size * 0.022))
    for ch, xi in zip(text, xs):
        d.text((xi, y), ch, font=font, fill=INK, anchor="l" + anchor[1],
               stroke_width=weight, stroke_fill=INK)


def cross(d, x, y, r, halo):
    """A cross pattee: four arms flaring from a narrow waist. Unlike anything the
    pen-work draws, so a site mark can't be mistaken for a well or a post."""
    def arms(r, w0, w1):
        pts = []
        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            px, py = -dy, dx                      # perpendicular
            pts.append([(x + dx * w0 * r + px * w0 * r, y + dy * w0 * r + py * w0 * r),
                        (x + dx * r + px * w1 * r, y + dy * r + py * w1 * r),
                        (x + dx * r - px * w1 * r, y + dy * r - py * w1 * r),
                        (x + dx * w0 * r - px * w0 * r, y + dy * w0 * r - py * w0 * r)])
        return pts
    for arm in arms(r + halo, 0.22, 0.5):
        d.polygon(arm, fill=PAPER)
    d.rectangle([x - 0.22 * (r + halo), y - 0.22 * (r + halo), x + 0.22 * (r + halo), y + 0.22 * (r + halo)], fill=PAPER)
    for arm in arms(r, 0.16, 0.42):
        d.polygon(arm, fill=INK)
    d.rectangle([x - 0.16 * r, y - 0.16 * r, x + 0.16 * r, y + 0.16 * r], fill=INK)


TYPES = ("place", "amenity", "watch", "entrance")
HEADINGS = {"place": "Places", "amenity": "Taverns & amenities", "watch": "The watch",
            "entrance": "Ways in"}


def ordered(sites):
    """Places first, then amenities, then the watch, each in listed order."""
    return [lb for t in TYPES for lb in sites if lb.get("type", "place") == t]


def mark(d, kind, x, y, r, halo):
    if kind == "place":
        cross(d, x, y, r, halo)
    elif kind == "amenity":
        # a black disc with a paper ring: a tavern, a shop, a stall
        R = r * 0.72
        d.ellipse([x - R - halo, y - R - halo, x + R + halo, y + R + halo], fill=PAPER)
        d.ellipse([x - R, y - R, x + R, y + R], fill=INK)
        d.ellipse([x - R * 0.38, y - R * 0.38, x + R * 0.38, y + R * 0.38], fill=PAPER)
    elif kind == "entrance":
        # a black triangle with a paper heart: a way down
        R = r * 0.85
        tri = lambda q: [(x, y - q), (x + q, y + q * 0.8), (x - q, y + q * 0.8)]
        d.polygon(tri(R + halo * 1.4), fill=PAPER)
        d.polygon(tri(R), fill=INK)
        d.polygon(tri(R * 0.4), fill=PAPER)
    else:
        # a square within a square: a watch post
        R = r * 0.7
        d.rectangle([x - R - halo, y - R - halo, x + R + halo, y + R + halo], fill=PAPER)
        d.rectangle([x - R, y - R, x + R, y + R], fill=INK)
        d.rectangle([x - R * 0.45, y - R * 0.45, x + R * 0.45, y + R * 0.45], fill=PAPER)
        d.rectangle([x - R * 0.2, y - R * 0.2, x + R * 0.2, y + R * 0.2], fill=INK)


def panel(d, box, U):
    """A parchment panel with the master's double ruled border."""
    x0, y0, x1, y1 = box
    t = max(2, round(U * 0.0012))
    d.rectangle(box, fill=PAPER, outline=INK, width=t * 2)
    g = round(U * 0.004)
    d.rectangle([x0 + g, y0 + g, x1 - g, y1 - g], outline=INK, width=t)


def cmd_label(render):
    s = spec()
    img = Image.open(render).convert("RGB")
    W, H = img.size
    U = max(W, H)  # sizes follow the long side, so a portrait sheet's marks are not tiny
    d = ImageDraw.Draw(img)
    halo = max(2, round(U * 0.003))
    f = lambda k: ImageFont.truetype(FONT, max(10, round(U * k)))

    # areas: lettered where they lie
    for lb in s.get("areas", []):
        tracked(d, (lb["x"] * W, lb["y"] * H), lb["text"], f(lb.get("size", 0.020)), "mm", halo)

    # sites: a numbered mark on the map, the name in the key. Three kinds, each
    # with its own mark: places (cross), taverns and amenities (disc), and the
    # watch (square). Numbered in that order, so the key reads in sections.
    sites = ordered(s["sites"])
    r = round(U * 0.0075)
    nf = ImageFont.truetype(DIGITS, round(U * 0.015))
    for n, lb in enumerate(sites, 1):
        x, y = lb["x"] * W, lb["y"] * H
        mark(d, lb.get("type", "place"), x, y, r, halo)
        dx, dy = {"ne": (1, -1), "nw": (-1, -1), "se": (1, 1), "sw": (-1, 1)}[lb.get("num", "ne")]
        pos = (x + dx * r * 1.1, y + dy * r * 1.1)
        anchor = ("l" if dx > 0 else "r") + ("d" if dy < 0 else "a")
        d.text(pos, str(n), font=nf, fill=INK, anchor=anchor, stroke_width=halo, stroke_fill=PAPER)

    # the title, in its own panel off the island
    t = s["title"]
    tf, sf = f(t.get("size", 0.034)), f(t.get("size", 0.034) * 0.38)
    tw = sum(tf.getlength(c) for c in t["text"].upper()) + tf.size * 0.16 * (len(t["text"]) - 1)
    # `box`: the drawing already has a cartouche; letter inside it, no panel
    if "box" in t:
        bx0, by0, bx1, by1 = t["box"][0] * W, t["box"][1] * H, t["box"][2] * W, t["box"][3] * H
        sub = t.get("subtitle")
        size = (by1 - by0) * (0.42 if sub else 0.55)
        while True:
            tf, sf = ImageFont.truetype(FONT, round(size)), ImageFont.truetype(FONT, round(size * 0.38))
            tw = sum(tf.getlength(c) for c in t["text"].upper()) + tf.size * 0.16 * (len(t["text"]) - 1)
            if tw <= (bx1 - bx0) * 0.86 or size < 8:
                break
            size *= 0.95
        cx, cy = (bx0 + bx1) / 2, (by0 + by1) / 2
        if sub:
            tracked(d, (cx, cy - sf.size * 0.75), t["text"], tf, "mm", 0)
            tracked(d, (cx, cy + tf.size * 0.62), sub, sf, "mm", 0)
        else:
            tracked(d, (cx, cy), t["text"], tf, "mm", 0)
        t = None
    # laid out from the border inward, so a small title never runs into it
    if t:
        g = U * 0.004 + max(2, round(U * 0.0012))
        sub = t.get("subtitle")
        ph = 2 * g + tf.size * 1.5 + (sf.size * 1.9 if sub else 0) + tf.size * 0.3
        sw = (sum(sf.getlength(c) for c in sub.upper()) + sf.size * 0.16 * (len(sub) - 1)) if sub else 0
        pw = max(tw, sw) + U * 0.05
        x0, y0 = t["x"] * W, t["y"] * H
        panel(d, [x0, y0, x0 + pw, y0 + ph], U)
        tracked(d, (x0 + pw / 2, y0 + g + tf.size * 0.9), t["text"], tf, "mm", 0)
        if sub:
            tracked(d, (x0 + pw / 2, y0 + g + tf.size * 1.65 + sf.size * 0.75), sub, sf, "mm", 0)

    # the key, in its own panel off the island; sectioned when there is more
    # than one kind of mark, and split into columns when it would be too tall
    k = s["key"]
    kf = f(k.get("size", 0.0112))
    df = ImageFont.truetype(DIGITS, kf.size)
    line = kf.size * 1.75
    kinds = [t for t in TYPES if any(lb.get("type", "place") == t for lb in sites)]
    rows = []
    for t in kinds:
        if len(kinds) > 1:
            rows.append(("head", HEADINGS[t]))
        rows += [("item", n, t, lb["text"]) for n, lb in enumerate(sites, 1)
                 if lb.get("type", "place") == t]
    ncol = k.get("columns", 1)
    per = -(-len(rows) // ncol)
    cols = [rows[i * per:(i + 1) * per] for i in range(ncol)]
    colw = max(kf.getlength(f"{len(sites)}.  " + r_[3].upper()) * 1.17 + U * 0.06
               for r_ in rows if r_[0] == "item")
    kw = colw * ncol + U * 0.01 * (ncol - 1)
    kh = line * (per + 1.9)
    # anchored at the bottom: the key grows upward as sites are added
    x0 = k["x"] * W
    y0 = k["top"] * H if "top" in k else H * (1 - k["bottom"]) - kh
    panel(d, [x0, y0, x0 + kw, y0 + kh], U)
    tracked(d, (x0 + kw / 2, y0 + line * 0.85), "Key", kf, "mm", 0, tracking=0.4)
    for c, col in enumerate(cols):
        cx = x0 + c * (colw + U * 0.01)
        for i, row in enumerate(col, 1):
            cy = y0 + line * (i + 0.9)
            if row[0] == "head":
                tracked(d, (cx + U * 0.016, cy), row[1], f(k.get("size", 0.0112) * 0.82), "lm", 0, tracking=0.3)
                continue
            _, n, t, name = row
            mark(d, t, cx + U * 0.022, cy, kf.size * 0.42, 0)
            d.text((cx + U * 0.0455, cy), "%d." % n, font=df, fill=INK, anchor="rm")
            tracked(d, (cx + U * 0.050, cy), name, kf, "lm", 0, tracking=0.12)

    root, _ = os.path.splitext(render)
    out = root + "-labelled.png"
    img.save(out)
    print(out)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    HERE = os.path.join(MAPS, sys.argv[1])
    cmd, rest = sys.argv[2], sys.argv[3:]
    if cmd == "request":
        cmd_request()
    elif cmd == "prep":
        cmd_prep()
    elif cmd == "label":
        cmd_label(rest[0] if rest else os.path.join(HERE, "crop.png"))
    else:
        sys.exit(__doc__)
