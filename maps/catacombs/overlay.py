# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow", "pyyaml"]
# ///
"""GM ONLY. Draws where the Catacombs run, over the city map.

    uv run maps/catacombs/overlay.py          # -> catacombs-overlay.jpg, the GM sheet
    uv run maps/catacombs/overlay.py plain    # -> request-*.png, unlettered crops for ElevenLabs

The plan is in plan.yaml (fractions of maps/purewater-map.png). This is a
planning sheet for the GM and for briefing an image model, not a player map.
"""
import os
import sys
import yaml
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(HERE, "..", "purewater-map.png")
FONT = "/System/Library/Fonts/Supplemental/BigCaslon.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"

STYLE = {  # layer -> (colour, width as fraction of W, dash)
    "ossuary": ((150, 60, 20), 0.0055, None),
    "oldwater": ((20, 90, 170), 0.0075, None),
    "smugglers": ((20, 20, 20), 0.0030, (0.012, 0.007)),
    "uncertain": ((120, 120, 120), 0.0025, (0.006, 0.006)),
}


def dashed(d, pts, col, w, dash):
    on, off = dash
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        t = 0.0
        while t < L:
            a, b = t / L, min(t + on, L) / L
            d.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a), (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)], fill=col, width=w)
            t += on + off


def main():
    plan = yaml.safe_load(open(os.path.join(HERE, "plan.yaml")))
    base = Image.open(MASTER).convert("RGB")
    W, H = base.size
    base = ImageEnhance.Contrast(ImageEnhance.Brightness(base).enhance(1.08)).enhance(0.55)
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    P = lambda p: (p[0] * W, p[1] * H)

    for a in plan.get("areas", []):          # tinted extents
        col = STYLE[a["layer"]][0]
        d.polygon([P(p) for p in a["poly"]], fill=col + (60,), outline=col + (200,))
    for r in plan["runs"]:
        col, w, dash = STYLE[r["layer"]]
        pts = [P(p) for p in r["path"]]
        if dash:
            dashed(d, pts, col + (255,), round(W * w), (W * dash[0], W * dash[1]))
        else:
            d.line(pts, fill=col + (230,), width=round(W * w), joint="curve")
    for c in plan.get("chambers", []):        # pools and halls
        col = STYLE[c["layer"]][0]
        x, y = P(c["at"]); R = W * c.get("r", 0.010)
        d.ellipse([x - R, y - R, x + R, y + R], fill=col + (200,), outline=(255, 255, 255, 255), width=3)

    img = Image.alpha_composite(base.convert("RGBA"), over).convert("RGB")
    if len(sys.argv) > 1 and sys.argv[1] == "plain":
        for name, (x0, y0, x1, y1) in plan["requests"].items():
            img.crop((round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H))).save(
                os.path.join(HERE, "request-%s.png" % name))
            print("request-%s.png" % name)
        return
    d = ImageDraw.Draw(img)
    nf = ImageFont.truetype(BOLD, round(W * 0.012))
    lf = ImageFont.truetype(FONT, round(W * 0.0105))
    for n, e in enumerate(plan["entrances"], 1):   # numbered red triangles
        x, y = P(e["at"]); R = W * 0.007
        d.polygon([(x, y - R), (x + R, y + R * 0.8), (x - R, y + R * 0.8)], fill=(200, 20, 20), outline=(255, 255, 255), width=3)
        d.text((x + R * 1.2, y - R * 1.2), str(n), font=nf, fill=(200, 20, 20), stroke_width=4, stroke_fill=(255, 255, 255))
    for c in plan.get("chambers", []):
        if c.get("label"):
            x, y = P(c["at"])
            d.text((x, y + W * c.get("r", 0.010) + 6), c["label"].upper(), font=lf, anchor="ma",
                   fill=STYLE[c["layer"]][0], stroke_width=4, stroke_fill=(255, 255, 255))

    # key, over the master's own legend corner
    kx, ky = W * 0.012, H * 0.555
    rows = [("GM ONLY -- THE CATACOMBS", None)]
    rows += [(t, l) for l, t in (("ossuary", "The Ossuary (dry chalk galleries)"),
                                  ("oldwater", "The Old Water (flooded, older than the city)"),
                                  ("smugglers", "Smugglers' runs"),
                                  ("uncertain", "Unmapped / rumoured"))]
    rows += [("ENTRANCES", None)] + [("%d. %s" % (n, e["name"]), "entrance") for n, e in enumerate(plan["entrances"], 1)]
    lh = lf.size * 1.55
    kw, kh = W * 0.30, lh * (len(rows) + 1)
    d.rectangle([kx, ky, kx + kw, ky + kh], fill=(246, 242, 232), outline=(30, 30, 30), width=4)
    for i, (t, l) in enumerate(rows):
        y = ky + lh * (i + 0.9)
        if l in STYLE:
            col, w, dash = STYLE[l]
            if dash:
                dashed(d, [(kx + 20, y), (kx + 90, y)], col, round(W * w), (W * dash[0], W * dash[1]))
            else:
                d.line([(kx + 20, y), (kx + 90, y)], fill=col, width=round(W * w))
            d.text((kx + 110, y), t, font=lf, fill=(30, 30, 30), anchor="lm")
        elif l == "entrance":
            d.text((kx + 30, y), t, font=lf, fill=(30, 30, 30), anchor="lm")
        else:
            d.text((kx + 20, y), t, font=nf if i == 0 else lf, fill=(160, 20, 20) if i == 0 else (30, 30, 30), anchor="lm")
    out = os.path.join(HERE, "catacombs-overlay.jpg")
    img.save(out, quality=88)
    print(out)


if __name__ == "__main__":
    main()
