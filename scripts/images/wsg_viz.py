#!/usr/bin/env python3
"""Shared image toolkit for WSG article illustrations (October 2026).

Three things live here so every article's images look like one set:

1. The chart style: Arial (Liberation Sans in the sandbox, same metrics), the validated
   categorical palette from the dataviz reference (blue, orange, aqua, yellow), one hue
   for sequential ramps, recessive grid, no chartjunk, 2200 px wide PNGs at 200 dpi.
2. Excel formatting helpers for the model workbooks the articles are illustrated with:
   blue hardcodes, black formulas, green cross-sheet links, bold section headers,
   banker number formats, column widths. The screenshots come from these workbooks.
3. render_range(): turn a sheet range of an .xlsx into a PNG that looks like an Excel
   screenshot (row and column headings, gridlines) via LibreOffice -> PDF -> pdftoppm,
   then trimmed with Pillow.

Usage from a build script:

    import sys; sys.path.insert(0, "scripts/images")
    from wsg_viz import *
    fig, ax = new_figure()                      # styled matplotlib figure
    ...
    save_figure(fig, "published/assets/images/lbo-model/03-debt-paydown.png")

    wb = new_workbook()                         # openpyxl workbook with Arial 10 default
    ws = wb.active; ws.title = "LBO"
    put(ws, "B4", "Purchase price", bold=True)   # label
    put(ws, "C4", 1000, kind="input", fmt=FMT_NUM)       # blue hardcode
    put(ws, "C5", "=C4*0.6", kind="formula", fmt=FMT_NUM) # black formula
    wb.save("scripts/images/models/targetco-lbo.xlsx")
    render_range("scripts/images/models/targetco-lbo.xlsx", "LBO", "B2:H20",
                 "published/assets/images/lbo-model/01-sources-and-uses.png")

Every PNG that goes on the site also gets an entry in the article folder's manifest.json
(see images.md in the skill package) with alt text and a caption.
"""
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

# ---------------------------------------------------------------- palette (dataviz reference, light mode)
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
BLUE, ORANGE, AQUA, YELLOW = SERIES[:4]
SEQ_BLUE = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
            "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]
DIVERGING = ("#2a78d6", "#f0efec", "#e34948")   # blue, neutral gray midpoint, red
TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED = "#0b0b0b", "#52514e", "#8a8984"
# Banking chart style (October 7, 2026 founder review): black text, no gridlines, no boxes or
# frames, a single thin baseline, direct data labels, a "Source:" line under every chart.
# BANK_SERIES is the default categorical order for new charts: navy, mid blue, gray, light blue.
BLACK = "#000000"
NAVY, MID_BLUE, GRAY, LIGHT_BLUE = "#0b2a4a", "#4a7ab5", "#8c8c8c", "#a9c4e2"
BANK_SERIES = [NAVY, MID_BLUE, GRAY, LIGHT_BLUE]
SURFACE, GRID = "#ffffff", "#e6e5e1"
GOOD, WARN, BAD = "#008300", "#eda100", "#e34948"

FONT_FAMILY = ["Arial", "Liberation Sans", "DejaVu Sans"]
PNG_DPI = 200
FIG_W_IN, FIG_H_IN = 11.0, 6.2   # 2200 x 1240 px at 200 dpi

# ---------------------------------------------------------------- matplotlib
def new_figure(width=FIG_W_IN, height=FIG_H_IN, nrows=1, ncols=1, **kw):
    """A styled figure. Call once per chart; returns (fig, ax) or (fig, axes)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": FONT_FAMILY,
        "font.size": 13, "text.color": BLACK,
        "axes.titlesize": 16, "axes.titleweight": "bold", "axes.titlecolor": BLACK,
        "axes.labelsize": 13, "axes.labelcolor": BLACK,
        "axes.edgecolor": BLACK, "axes.linewidth": 0.8,
        "axes.grid": False, "axes.axisbelow": True,
        "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
        "xtick.color": BLACK, "ytick.color": BLACK, "xtick.labelsize": 12, "ytick.labelsize": 12,
        "xtick.major.size": 0, "ytick.major.size": 0,
        "axes.prop_cycle": __import__("cycler").cycler(color=BANK_SERIES),
        "legend.frameon": False, "legend.fontsize": 12,
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "lines.linewidth": 2.2, "lines.markersize": 7,
    })
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(width, height), **kw)
    return fig, ax


def style_axes(ax, title=None, xlabel=None, ylabel=None, ygrid_only=True, value_axis=False):
    """Banking style: no gridlines, no frame, black text, one thin baseline.

    ygrid_only is kept so older build scripts still run; gridlines stay off either way.
    Set value_axis=True only for line charts that need a readable value scale; bar charts
    carry direct labels (bar_labels) instead of a value axis.
    """
    if title:
        ax.set_title(title, loc="left", pad=14, color=BLACK)
    if xlabel:
        ax.set_xlabel(xlabel, color=BLACK)
    if ylabel:
        ax.set_ylabel(ylabel, color=BLACK)
    ax.grid(False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(BLACK)
    ax.spines["bottom"].set_linewidth(0.8)
    ax.tick_params(length=0, colors=BLACK)
    if not value_axis:
        ax.set_yticks([])


def add_source(fig, text, fontsize=10):
    """Source line under a chart, flush with the left edge of everything drawn: 'Source: X'."""
    if not text.lower().startswith("source"):
        text = "Source: " + text
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = [ax.get_tightbbox(renderer) for ax in fig.axes if ax.get_visible()]
    x0 = min(b.x0 for b in boxes) if boxes else 0
    y0 = min(b.y0 for b in boxes) if boxes else 0
    fx, fy = fig.transFigure.inverted().transform((x0, y0))
    fig.text(fx, fy - 0.03, text, ha="left", va="top", fontsize=fontsize, color=BLACK)


def bar_labels(ax, bars, fmt="{:,.0f}", color=BLACK, pad=3, fontsize=12):
    """Direct value labels on a bar series (use selectively, never on every point of a dense chart)."""
    for b in bars:
        h = b.get_height()
        ax.annotate(fmt.format(h), (b.get_x() + b.get_width() / 2, h), ha="center",
                    va="bottom" if h >= 0 else "top", xytext=(0, pad if h >= 0 else -pad),
                    textcoords="offset points", fontsize=fontsize, color=color)


def save_figure(fig, out_path, tight=True):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    kw = {"dpi": PNG_DPI, "metadata": {"Software": "Wall Street Guide", "Author": "Wall Street Guide"}}
    if tight:
        kw["bbox_inches"] = "tight"
        kw["pad_inches"] = 0.15
    fig.savefig(out_path, **kw)
    import matplotlib.pyplot as plt
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------- openpyxl helpers
FMT_NUM = '#,##0.0;(#,##0.0);"-"'
FMT_INT = '#,##0;(#,##0);"-"'
FMT_PCT = '0.0%;(0.0%);"-"'
FMT_MULT = '0.0"x"'
FMT_MULT2 = '0.00"x"'
FMT_DOLLAR = '"$"#,##0.0;("$"#,##0.0);"-"'

XL_FONT = "Arial"
XL_SIZE = 10
COLOR_INPUT, COLOR_FORMULA, COLOR_LINK = "0000FF", "000000", "008000"
FILL_HEADER = "0B2545"   # dark navy section bar, white text
FILL_SUBTLE = "F2F2F2"
FILL_INPUT = "FFF9E6"    # pale yellow behind hardcodes, the common banker convention


def new_workbook():
    from openpyxl import Workbook
    from openpyxl.styles import Font
    wb = Workbook()
    wb._named_styles["Normal"].font = Font(name=XL_FONT, size=XL_SIZE)
    return wb


def put(ws, ref, value, kind="label", fmt=None, bold=False, italic=False, fill=None, align=None,
        indent=0, border_bottom=False, border_top=False, color=None, size=None):
    """Write one cell with the house formatting.

    kind: "label" (black text), "input" (blue hardcode on pale yellow), "formula" (black),
          "link" (green, a value pulled from another sheet), "header" (white on navy bar),
          "total" (bold with a top border).
    """
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    c = ws[ref]
    c.value = value
    font_color = {"input": COLOR_INPUT, "formula": COLOR_FORMULA, "link": COLOR_LINK,
                  "label": COLOR_FORMULA, "header": "FFFFFF", "total": COLOR_FORMULA}[kind]
    if color:
        font_color = color
    c.font = Font(name=XL_FONT, size=size or XL_SIZE, bold=bold or kind in ("header", "total"),
                  italic=italic, color=font_color)
    if kind == "input":
        c.fill = PatternFill("solid", fgColor=FILL_INPUT)
    elif kind == "header":
        c.fill = PatternFill("solid", fgColor=FILL_HEADER)
    if fill:
        c.fill = PatternFill("solid", fgColor=fill)
    if fmt:
        c.number_format = fmt
    thin = Side(style="thin", color="000000")
    if border_bottom or border_top or kind == "total":
        c.border = Border(top=thin if (border_top or kind == "total") else None,
                          bottom=thin if border_bottom else None)
    if align or indent:
        c.alignment = Alignment(horizontal=align, indent=indent)
    return c


def header_bar(ws, row, first_col, last_col, text):
    """A navy section bar spanning first_col..last_col with white bold text in the first cell."""
    from openpyxl.styles import Font, PatternFill
    from openpyxl.utils import get_column_letter
    for col in range(first_col, last_col + 1):
        c = ws.cell(row=row, column=col)
        c.fill = PatternFill("solid", fgColor=FILL_HEADER)
        c.font = Font(name=XL_FONT, size=XL_SIZE, bold=True, color="FFFFFF")
    ws.cell(row=row, column=first_col).value = text


def set_widths(ws, widths):
    """widths: {"A": 2, "B": 34, "C": 11, ...}"""
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


def year_header(ws, row, first_col, years, label_col=None, label=None, bold=True):
    """Write a row of year labels (e.g. 'Year 1' or 2026E) with a bottom border."""
    from openpyxl.styles import Alignment, Border, Font, Side
    thin = Side(style="thin", color="000000")
    if label_col and label:
        ws.cell(row=row, column=label_col, value=label).font = Font(name=XL_FONT, size=XL_SIZE, bold=bold)
    for i, y in enumerate(years):
        c = ws.cell(row=row, column=first_col + i, value=y)
        c.font = Font(name=XL_FONT, size=XL_SIZE, bold=bold)
        c.alignment = Alignment(horizontal="right")
        c.border = Border(bottom=thin)


# ---------------------------------------------------------------- xlsx -> png
def render_range(xlsx_path, sheet, cell_range, out_png, dpi=PNG_DPI, headings=True, gridlines=True,
                 max_width_px=2200, scale_to_fit_width=True):
    """Render one sheet range of a workbook to a PNG that reads as an Excel screenshot.

    Works on a temp copy: every other sheet is hidden, the print area is set to cell_range,
    row/column headings and gridlines are switched on, the page is scaled to one page wide,
    LibreOffice exports a PDF, pdftoppm rasterizes page 1, Pillow trims the margins.
    Formulas are recalculated by LibreOffice on load, so the picture shows live values.
    """
    from openpyxl import load_workbook
    from PIL import Image, ImageChops

    out_png = Path(out_png)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        tmp_xlsx = Path(td) / "render.xlsx"
        wb = load_workbook(xlsx_path)
        for ws in wb.worksheets:
            ws.sheet_state = "visible" if ws.title == sheet else "hidden"
        ws = wb[sheet]
        wb.active = wb.worksheets.index(ws)
        ws.print_area = cell_range
        ws.print_options.gridLines = gridlines
        ws.print_options.headings = headings
        ws.page_setup.orientation = "landscape"
        ws.page_setup.paperSize = ws.PAPERSIZE_TABLOID
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 1 if scale_to_fit_width else 0
        ws.page_margins.left = ws.page_margins.right = 0.2
        ws.page_margins.top = ws.page_margins.bottom = 0.2
        ws.page_margins.header = ws.page_margins.footer = 0
        ws.oddHeader.center.text = ""
        ws.oddFooter.center.text = ""
        wb.save(tmp_xlsx)
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", td, str(tmp_xlsx)],
                       check=True, capture_output=True, timeout=180)
        pdf = Path(td) / "render.pdf"
        subprocess.run(["pdftoppm", "-r", str(dpi), "-f", "1", "-l", "1", "-png", str(pdf), str(Path(td) / "page")],
                       check=True, capture_output=True, timeout=180)
        page = next(Path(td).glob("page*.png"))
        im = Image.open(page).convert("RGB")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bbox = ImageChops.difference(im, bg).getbbox()
        if bbox:
            pad = 18
            bbox = (max(bbox[0] - pad, 0), max(bbox[1] - pad, 0), min(bbox[2] + pad, im.width), min(bbox[3] + pad, im.height))
            im = im.crop(bbox)
        if im.width > max_width_px:
            ratio = max_width_px / im.width
            im = im.resize((max_width_px, int(im.height * ratio)), Image.LANCZOS)
        im.save(out_png, "PNG", optimize=True)
    return out_png


def recalc_values(xlsx_path):
    """Return {sheet: {cell: value}} after a LibreOffice recalculation (to check a model's numbers
    against the article's tables without trusting openpyxl's cached values)."""
    from openpyxl import load_workbook
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / "in.xlsx"
        shutil.copy(xlsx_path, src)
        subprocess.run(["soffice", "--headless", "--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir",
                        str(Path(td) / "out"), str(src)], check=True, capture_output=True, timeout=180)
        out = Path(td) / "out" / "in.xlsx"
        wb = load_workbook(out, data_only=True)
        return {ws.title: {c.coordinate: c.value for row in ws.iter_rows() for c in row if c.value is not None}
                for ws in wb.worksheets}


def write_manifest(folder, entries):
    """entries: list of {"file": "01-x.png", "alt": "...", "caption": "...", "source": "...", "anchor": "..."}"""
    import json
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "manifest.json").write_text(json.dumps(entries, indent=2), encoding="utf-8")


def bank_table(header, rows, out_path, total_rows=(), col_align=None, title=None, source=None,
               width=FIG_W_IN, fontsize=13):
    """Render a table as a clean banking graphic: black text, no cell borders or gridlines,
    a thin rule under the header and above any total row, numbers right-aligned.

    header: list of column labels. rows: list of row lists (strings). total_rows: row indexes
    drawn bold with a rule above. col_align: list of 'left' / 'right' per column.
    """
    n_cols = len(header)
    col_align = col_align or (["left"] + ["right"] * (n_cols - 1))
    height = 0.42 * (len(rows) + 1) + (0.6 if title else 0.2) + (0.4 if source else 0)
    fig, ax = new_figure(width=width, height=height)
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    widths = [2.2] + [1.0] * (n_cols - 1)
    total_w = sum(widths)
    xs, acc = [], 0.0
    for w in widths:
        xs.append((acc, acc + w))
        acc += w
    def x_for(i):
        a, b = xs[i]
        return (a / total_w + 0.005) if col_align[i] == "left" else (b / total_w - 0.005)
    n = len(rows) + 1
    y = lambda r: 1 - (r + 0.5) / n
    for i, h in enumerate(header):
        ax.text(x_for(i), y(0), h, ha=col_align[i], va="center", fontsize=fontsize, fontweight="bold", color=BLACK, transform=ax.transAxes)
    ax.plot([0, 1], [1 - 1 / n, 1 - 1 / n], color=BLACK, lw=0.9, transform=ax.transAxes)
    for r, row in enumerate(rows, start=1):
        bold = (r - 1) in total_rows
        if bold:
            ax.plot([0, 1], [1 - (r) / n, 1 - (r) / n], color=BLACK, lw=0.7, transform=ax.transAxes)
        for i, cell in enumerate(row):
            ax.text(x_for(i), y(r), str(cell), ha=col_align[i], va="center", fontsize=fontsize,
                    fontweight="bold" if bold else "normal", color=BLACK, transform=ax.transAxes)
    if title:
        ax.set_title(title, loc="left", pad=10, color=BLACK)
    if source:
        add_source(fig, source)
    return save_figure(fig, out_path)


__all__ = [n for n in dir() if not n.startswith("_")]
