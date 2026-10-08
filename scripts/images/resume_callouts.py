#!/usr/bin/env python3
"""Numbered callouts on a rendered resume page (October 2026, resume articles).

Page 1 of a sample resume PDF is rasterized with pdftoppm at 150 dpi, the text lines are
located with pdfplumber (so every box sits exactly on the line it marks), and Pillow draws
thin colored boxes around the regions plus numbered labels in a margin strip. A second
function lays the same page out twice, side by side, for the "banking read vs consulting
read" graphic. Fonts are Liberation Sans (Arial metrics). Colors come from wsg_viz.

Usage from a build script (run from the repo root):

    import sys; sys.path.insert(0, "scripts/images")
    from resume_callouts import *
    page, lines = load_page("published/assets/Sample Finance Resume (Jane Doe).pdf")
    box = region(lines, "GPA: 3.78")                       # one line, full text width
    box = region(lines, "Built the trading", last="buyers") # a wrapped bullet
    draw_callouts(page, [(box, "GPA on its own line", "Two decimals, out of 4.00."), ...],
                  "published/assets/images/slug/01-page.png")
"""
import subprocess
import tempfile
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from wsg_viz import BLUE, ORANGE, GRID, TEXT_PRIMARY, TEXT_SECONDARY

DPI = 150
PT = DPI / 72.0   # points -> pixels at 150 dpi

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
FONT_REG = FONT_DIR / "LiberationSans-Regular.ttf"
FONT_BOLD = FONT_DIR / "LiberationSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


# ---------------------------------------------------------------- page and text lines
def load_page(pdf_path):
    """Return (PIL image of page 1 at 150 dpi, list of text lines with pixel boxes)."""
    import pdfplumber
    pdf_path = Path(pdf_path)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-r", str(DPI), "-f", "1", "-l", "1", "-png", str(pdf_path),
                        str(Path(td) / "page")], check=True, capture_output=True, timeout=120)
        png = next(Path(td).glob("page*.png"))
        page = Image.open(png).convert("RGB")
        page.load()
    with pdfplumber.open(str(pdf_path)) as pdf:
        raw = pdf.pages[0].extract_text_lines()
    lines = [{"text": l["text"], "x0": l["x0"] * PT, "x1": l["x1"] * PT,
              "top": l["top"] * PT, "bottom": l["bottom"] * PT} for l in raw]
    return page, lines


def text_extent(lines):
    """Left and right edge of the page's text block, in pixels."""
    return min(l["x0"] for l in lines), max(l["x1"] for l in lines)


def find_line(lines, contains, after=-1):
    for i, l in enumerate(lines):
        if i > after and contains in l["text"]:
            return i
    raise KeyError(f"no line containing {contains!r} after index {after}")


def region(lines, first, last=None, full_width=True, pad=5, until=None):
    """Pixel box (x0, y0, x1, y1) around the line containing `first` through the line
    containing `last` (searched after `first`), or through the line before the one
    containing `until`. full_width spans the text block."""
    i = find_line(lines, first)
    if until:
        j = find_line(lines, until, after=i) - 1
    else:
        j = find_line(lines, last, after=i) if last else i
    block = lines[i:j + 1]
    if full_width:
        x0, x1 = text_extent(lines)
    else:
        x0, x1 = min(l["x0"] for l in block), max(l["x1"] for l in block)
    y0, y1 = min(l["top"] for l in block), max(l["bottom"] for l in block)
    return (x0 - pad, y0 - pad, x1 + pad, y1 + pad)


# ---------------------------------------------------------------- drawing primitives
def _hex(c):
    c = c.lstrip("#")
    return tuple(int(c[k:k + 2], 16) for k in (0, 2, 4))


def _badge(draw, cx, cy, n, color, d=46, fsize=26):
    draw.ellipse((cx - d / 2, cy - d / 2, cx + d / 2, cy + d / 2), fill=_hex(color))
    f = font(fsize, bold=True)
    draw.text((cx, cy + 1), str(n), font=f, fill="white", anchor="mm")


def _wrap(text, f, max_px):
    words, out, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if f.getlength(trial) <= max_px or not cur:
            cur = trial
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def _box(draw, box, color, width=4, radius=10):
    draw.rounded_rectangle(box, radius=radius, outline=_hex(color), width=width)


# ---------------------------------------------------------------- one page + margin labels
def draw_callouts(page, callouts, out_png, color=BLUE, strip_w=800, gap=56, margin=28,
                  title_size=36, body_size=31, heading=None):
    """callouts: list of (box, title, detail[, corner]). Boxes are drawn on the page, numbered
    in reading order, and each number repeats in the right margin with its title and detail.
    corner puts the page badge at the box's top left ("tl", default), bottom left ("bl") or
    top right ("tr") so badges on adjacent lines don't collide."""
    W = margin + page.width + gap + strip_w + margin
    top_pad = margin + (90 if heading else 0)
    H = top_pad + page.height + margin
    im = Image.new("RGB", (W, H), "white")
    im.paste(page, (margin, top_pad))
    draw = ImageDraw.Draw(im)
    draw.rectangle((margin - 1, top_pad - 1, margin + page.width, top_pad + page.height),
                   outline=_hex(GRID), width=2)
    if heading:
        draw.text((margin, margin + 10), heading, font=font(40, bold=True), fill=_hex(TEXT_PRIMARY))

    ft, fb = font(title_size, bold=True), font(body_size)
    lh_t, lh_b = int(title_size * 1.25), int(body_size * 1.3)
    label_x = margin + page.width + gap
    text_x = label_x + 64
    text_w = strip_w - 64

    # Layout: each label wants to sit at its box's vertical center; push down to avoid overlap.
    blocks = []
    for n, c in enumerate(callouts, start=1):
        box, title, detail = c[0], c[1], c[2]
        corner = c[3] if len(c) > 3 else "tl"     # where the page badge sits: tl, bl or tr
        x0, y0, x1, y1 = [v + (margin if k % 2 == 0 else top_pad) for k, v in enumerate(box)]
        t_lines = _wrap(title, ft, text_w)
        d_lines = _wrap(detail, fb, text_w) if detail else []
        h = len(t_lines) * lh_t + len(d_lines) * lh_b
        blocks.append({"n": n, "box": (x0, y0, x1, y1), "t": t_lines, "d": d_lines, "h": h,
                       "want": (y0 + y1) / 2 - h / 2, "corner": corner})
    y_cursor = top_pad
    for b in blocks:
        y = max(b["want"], y_cursor)
        b["y"] = y
        y_cursor = y + b["h"] + 34
    overflow = (blocks[-1]["y"] + blocks[-1]["h"]) - (H - margin) if blocks else 0
    if overflow > 0:   # slide the whole column up if the last label runs off the page
        for b in blocks:
            b["y"] -= overflow

    for b in blocks:
        x0, y0, x1, y1 = b["box"]
        _box(draw, (x0, y0, x1, y1), color)
        cy = (y0 + y1) / 2
        ly = b["y"] + lh_t / 2
        # leader from the box's right edge to the margin badge
        draw.line((x1, cy, x1 + gap / 2, cy, label_x - 8, ly), fill=_hex(color), width=3)
        draw.ellipse((x1 - 6, cy - 6, x1 + 6, cy + 6), fill=_hex(color))
        bx, by = {"tl": (x0 - 26, y0 + 4), "bl": (x0 - 26, y1 - 4), "tr": (x1 + 26, y0 + 4)}[b["corner"]]
        _badge(draw, bx, by, b["n"], color)   # in the page margin, outside the box
        _badge(draw, label_x + 23, ly, b["n"], color)
        y = b["y"]
        for t in b["t"]:
            draw.text((text_x, y), t, font=ft, fill=_hex(TEXT_PRIMARY))
            y += lh_t
        for d in b["d"]:
            draw.text((text_x, y), d, font=fb, fill=_hex(TEXT_SECONDARY))
            y += lh_b

    out_png = Path(out_png)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    if im.width > 2200:
        im = im.resize((2200, int(im.height * 2200 / im.width)), Image.LANCZOS)
    im.save(out_png, "PNG", optimize=True, dpi=(200, 200))
    return out_png


# ---------------------------------------------------------------- the same page twice
def draw_two_reads(page, left, right, out_png, page_w=1000, margin=40, gap=90,
                   legend_size=36, title_size=48, sub_size=31):
    """left/right: dict(title, subtitle, color, callouts=[(box, legend_text[, "right"]), ...]).
    The page is drawn twice at page_w pixels wide with each side's boxes, badges 1..n, and a
    numbered legend under each page. A third item "right" puts the badge on the box's top
    right corner (for a box nested inside another one)."""
    s = page_w / page.width
    small = page.resize((page_w, int(page.height * s)), Image.LANCZOS)
    ft, fs, fl = font(title_size, bold=True), font(sub_size), font(legend_size)
    lh = int(legend_size * 1.32)
    head_h = int(title_size * 1.3 + sub_size * 1.5 + 24)
    legend_w = page_w - 70
    sides = [left, right]
    legends = []
    for side in sides:
        rows = []
        for n, c in enumerate(side["callouts"], start=1):
            rows.append((n, _wrap(c[1], fl, legend_w)))
        legends.append(rows)
    legend_h = max(sum(len(r[1]) * lh + 14 for r in rows) for rows in legends)
    W = margin + page_w + gap + page_w + margin
    H = margin + head_h + small.height + 36 + legend_h + margin
    im = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(im)
    for k, side in enumerate(sides):
        ox = margin + k * (page_w + gap)
        oy = margin + head_h
        color = side["color"]
        draw.text((ox, margin), side["title"], font=ft, fill=_hex(TEXT_PRIMARY))
        draw.text((ox, margin + int(title_size * 1.3) + 4), side["subtitle"], font=fs,
                  fill=_hex(TEXT_SECONDARY))
        draw.line((ox, oy - 14, ox + page_w, oy - 14), fill=_hex(color), width=6)
        im.paste(small, (ox, oy))
        draw.rectangle((ox - 1, oy - 1, ox + page_w, oy + small.height), outline=_hex(GRID), width=2)
        for n, c in enumerate(side["callouts"], start=1):
            box = c[0]
            x0, y0, x1, y1 = box[0] * s + ox, box[1] * s + oy, box[2] * s + ox, box[3] * s + oy
            _box(draw, (x0, y0, x1, y1), color, width=4, radius=8)
            bx = x1 + 23 if len(c) > 2 and c[2] == "right" else x0 - 23
            _badge(draw, bx, y0 + 4, n, color, d=40, fsize=23)
        y = oy + small.height + 36
        for n, rows in legends[k]:
            _badge(draw, ox + 20, y + lh / 2, n, color, d=38, fsize=22)
            for r in rows:
                draw.text((ox + 56, y), r, font=fl, fill=_hex(TEXT_PRIMARY))
                y += lh
            y += 14
    out_png = Path(out_png)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    if im.width > 2200:
        im = im.resize((2200, int(im.height * 2200 / im.width)), Image.LANCZOS)
    im.save(out_png, "PNG", optimize=True, dpi=(200, 200))
    return out_png


__all__ = ["load_page", "region", "find_line", "text_extent", "draw_callouts", "draw_two_reads",
           "font", "BLUE", "ORANGE"]
