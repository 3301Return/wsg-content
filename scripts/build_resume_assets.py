#!/usr/bin/env python3
"""Build the WSG sample resume assets (one-page .docx and .pdf, letter size) from the
plain-text resume blocks in drafts/sample-resume-*.md.

Usage:
    python3 scripts/build_resume_assets.py                 # builds every asset listed in ASSETS
    python3 scripts/build_resume_assets.py input.md "Title"  # builds one (docx + pdf)

Source format is the one used inside the resume articles:
    NAME LINE
    contact | line
    (blank)
    SECTION HEADER (all caps)
    (blank)
    Org, City, ST. Title, Mon Year to Mon Year      <- entry line
    (blank)
    - bullet
    - bullet

Layout: Arial 10 (Liberation Sans in the PDF, same metrics), 0.6 inch margins, name 14 bold
centered, section headers bold with a bottom rule, entry line split into org / location and
title / dates on two lines with right-aligned tabs, bullets with a hanging indent, no blank
paragraphs between entries. Metadata (docx core properties and PDF Author / Creator /
Producer / Title) is set to Wall Street Guide; no personal identifiers are embedded.
The PDF is produced by LibreOffice from the .docx, then its metadata is rewritten.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pikepdf
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

FONT = "Arial"
BODY_PT = 10          # overridden per build by the auto-fit loop (10 to 11)
NAME_PT = 14
MARGIN_IN = 0.5
# Vertical spacing, in points, scaled by the auto-fit loop so each resume fills its page.
SPACE = {"name_after": 0, "contact_after": 2, "section_before": 7, "section_after": 2,
         "entry_before": 3, "bullet_after": 0}
SCALE = 1.0
PAGE_W_IN, PAGE_H_IN = 8.5, 11
RIGHT_TAB_IN = PAGE_W_IN - 2 * MARGIN_IN
AUTHOR = "Wall Street Guide"

ASSETS = [
    ("drafts/sample-resume-template-blank.md", "WSG One-Page Resume Template", ("docx",)),
    ("drafts/sample-resume-jane-doe.md", "Sample Finance Resume (Jane Doe)", ("docx", "pdf")),
    ("drafts/sample-resume-alex-doe.md", "Sample Consulting Resume - Junior (Alex Doe)", ("docx", "pdf")),
    ("drafts/sample-resume-sam-doe.md", "Sample Consulting Resume - Sophomore (Sam Doe)", ("docx", "pdf")),
]
OUT_DIR = Path("published/assets")

STATE_RE = re.compile(r"^[A-Z]{2}$")
DATE_TAIL_RE = re.compile(
    r",\s*((?:Expected\s+)?(?:\[[^\]]*\]|[A-Z][a-z]{2}\s+\d{4}|\d{4})"
    r"(?:\s+to\s+(?:\[[^\]]*\]|[A-Z][a-z]{2}\s+\d{4}|\d{4}|Present))?)\s*$"
)


# ---------------------------------------------------------------- parsing
def parse(text):
    lines = [ln.rstrip() for ln in text.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    name = lines.pop(0).strip()
    contact = lines.pop(0).strip() if lines and lines[0].strip() else ""
    sections, cur = [], None
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("- "):
            if cur is None:
                continue
            if not cur["entries"]:
                cur["entries"].append({"line": None, "bullets": []})
            cur["entries"][-1]["bullets"].append(s[2:].strip())
        elif s == s.upper() and len(s) > 3 and not s.startswith("["):
            cur = {"header": s, "entries": []}
            sections.append(cur)
        else:
            cur["entries"].append({"line": s, "bullets": []})
    return name, contact, sections


def split_entry(line):
    """'Org, City, ST. Title, dates' -> (org, location, title, dates)."""
    m = DATE_TAIL_RE.search(line)
    dates = ""
    if m:
        dates = m.group(1).strip()
        line = line[: m.start()].rstrip()
    if ". " in line:
        left, title = line.split(". ", 1)
    else:
        left, title = line, ""
    parts = [p.strip() for p in left.split(",")]
    location = ""
    if len(parts) >= 3 and (STATE_RE.match(parts[-1]) or parts[-1].startswith("[")):
        location = ", ".join(parts[-2:])
        org = ", ".join(parts[:-2])
    elif len(parts) >= 2 and parts[-1].startswith("["):
        location = parts[-1]
        org = ", ".join(parts[:-1])
    else:
        org = left
    return org, location, title.strip(), dates


# ---------------------------------------------------------------- docx helpers
def set_run_font(run, size=None, bold=False, italic=False):
    size = BODY_PT if size is None else size
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)


def tight(p, before=0, after=0, line=1.0):
    pf = p.paragraph_format
    pf.space_before = Pt(before * SCALE)
    pf.space_after = Pt(after * SCALE)
    pf.line_spacing = line


def add_bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "000000")
    pbdr.append(bottom)
    pPr.append(pbdr)


def add_right_tab(p):
    p.paragraph_format.tab_stops.add_tab_stop(Inches(RIGHT_TAB_IN), WD_TAB_ALIGNMENT.RIGHT)


def two_col_line(doc, left, right, bold=False, italic=False, before=0):
    p = doc.add_paragraph()
    tight(p, before=before)
    add_right_tab(p)
    r = p.add_run(left)
    set_run_font(r, bold=bold, italic=italic)
    if right:
        r2 = p.add_run("\t" + right)
        set_run_font(r2, bold=False, italic=italic)
    return p


def bullet(doc, text):
    p = doc.add_paragraph()
    tight(p)
    pf = p.paragraph_format
    pf.left_indent = Inches(0.2)
    pf.first_line_indent = Inches(-0.15)
    r = p.add_run("•  " + text)
    set_run_font(r)
    return p


def build_docx(src_path, title, out_path):
    name, contact, sections = parse(Path(src_path).read_text(encoding="utf-8"))
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(PAGE_W_IN), Inches(PAGE_H_IN)
    sec.left_margin = sec.right_margin = Inches(MARGIN_IN)
    sec.top_margin = sec.bottom_margin = Inches(MARGIN_IN)
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(BODY_PT)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tight(p, after=SPACE["name_after"])
    set_run_font(p.add_run(name), size=NAME_PT, bold=True)
    if contact:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        tight(p, after=SPACE["contact_after"])
        set_run_font(p.add_run(contact))

    for s in sections:
        h = doc.add_paragraph()
        tight(h, before=SPACE["section_before"], after=SPACE["section_after"])
        add_bottom_border(h)
        set_run_font(h.add_run(s["header"]), bold=True)
        for e in s["entries"]:
            if e["line"]:
                org, loc, ttl, dates = split_entry(e["line"])
                two_col_line(doc, org, loc, bold=True, before=SPACE["entry_before"])
                if ttl or dates:
                    two_col_line(doc, ttl, dates, italic=True)
            for b in e["bullets"]:
                bp = bullet(doc, b)
                tight(bp, after=SPACE["bullet_after"])

    cp = doc.core_properties
    cp.author = cp.last_modified_by = AUTHOR
    cp.title = title
    cp.comments = cp.keywords = cp.subject = cp.category = ""
    doc.save(out_path)
    return out_path


def _render(docx_path, pdf_dir):
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(pdf_dir), str(docx_path)],
        check=True, capture_output=True, timeout=180,
    )
    return Path(pdf_dir) / (Path(docx_path).stem + ".pdf")


def _page_stats(pdf_path):
    """(pages, fill) where fill is how far down the printable area the last line sits, 0 to 1."""
    with pikepdf.open(pdf_path) as pdf:
        pages = len(pdf.pages)
    out = subprocess.run(["pdftotext", "-bbox", str(pdf_path), "-"], capture_output=True, text=True).stdout
    ymax = max((float(m) for m in re.findall(r'yMax="([\d.]+)"', out)), default=0.0)
    page_h = PAGE_H_IN * 72
    top, bottom = MARGIN_IN * 72, page_h - MARGIN_IN * 72
    fill = (ymax - top) / (bottom - top)
    return pages, fill


def _stamp_metadata(produced, pdf_path, title):
    with pikepdf.open(produced) as pdf:
        if "/Metadata" in pdf.Root:
            del pdf.Root["/Metadata"]
        for k in list(pdf.docinfo.keys()):
            del pdf.docinfo[k]
        pdf.docinfo["/Title"] = title
        pdf.docinfo["/Author"] = AUTHOR
        pdf.docinfo["/Creator"] = AUTHOR
        pdf.docinfo["/Producer"] = AUTHOR
        pdf.save(pdf_path)


def build_fitted(src, title, docx_out, pdf_out=None, target_fill=0.965):
    """Pick the largest body size (11 -> 10) that fits one page, then stretch the spacing so the
    page is filled to about target_fill. Writes the .docx (and .pdf when pdf_out is given)."""
    global BODY_PT, SCALE
    best = None
    with tempfile.TemporaryDirectory() as td:
        for pt in (11.0, 10.5, 10.0):
            BODY_PT, SCALE = pt, 1.0
            build_docx(src, title, docx_out)
            pages, fill = _page_stats(_render(docx_out, td))
            if pages == 1:
                best = (pt, 1.0, fill)
                break
        if best is None:
            raise SystemExit(f"{title}: does not fit on one page even at 10pt; trim the source")
        pt, scale, fill = best
        # Stretch spacing: binary search on SCALE between 1 and 6 for fill ~ target without spilling.
        lo, hi = 1.0, 4.0
        for _ in range(9):
            mid = (lo + hi) / 2
            BODY_PT, SCALE = pt, mid
            build_docx(src, title, docx_out)
            pages, fill = _page_stats(_render(docx_out, td))
            if pages == 1 and fill <= target_fill + 0.01:
                lo, best = mid, (pt, mid, fill)
            else:
                hi = mid
            if pages == 1 and abs(fill - target_fill) < 0.01:
                break
        pt, scale, fill = best
        BODY_PT, SCALE = pt, scale
        build_docx(src, title, docx_out)
        produced = _render(docx_out, td)
        pages, fill = _page_stats(produced)
        if pdf_out:
            _stamp_metadata(produced, pdf_out, title)
    return pt, scale, pages, fill


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    jobs = ASSETS
    if len(sys.argv) >= 3:
        jobs = [(sys.argv[1], sys.argv[2], ("docx", "pdf"))]
    for src, title, kinds in jobs:
        docx_out = OUT_DIR / f"{title}.docx"
        if "pdf" in kinds:
            pdf_out = OUT_DIR / f"{title}.pdf"
            pt, scale, pages, fill = build_fitted(src, title, docx_out, pdf_out)
            print(f"built {docx_out} and {pdf_out}: {pt}pt, spacing x{scale:.2f}, {pages} page, {fill:.0%} of page used")
        else:
            global BODY_PT, SCALE
            BODY_PT, SCALE = 10.5, 1.0
            build_docx(src, title, docx_out)
            print(f"built {docx_out} (template, no fit)")


if __name__ == "__main__":
    main()
