#!/usr/bin/env python3
"""
WSG markdown -> docx builder (v2), current standard.

Usage:
    python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"

Structure (wsg-article skill, formatting.md module; August 2026 spec):
- Title style: the article title, exactly one, first line. Any later "# " line becomes Heading 2.
- Heading 2 style: every section heading. No Heading 1 or Heading 3 in the body.
- Markdown H3s become full-bold Normal paragraphs (sub-labels, firm names).
- One empty Normal paragraph between blocks. A heading sits tight against the body below it,
  and has exactly one empty line above it. Never two empty paragraphs in a row.
- List items stay tight; one empty line before the first item and after the last.
- Consecutive non-blank lines in one markdown paragraph stay tight
  (the "Say this, don't say that" question / Don't say / Say triplets).
- Heading text is never bolded by hand: the Title and Heading 2 styles carry the weight.
- Empty headings are dropped. Numbered lists restart at 1 for each new list.

Visuals (style-guide/formatting-standards.md, locked May 24 spec): Arial throughout;
Title 24pt bold black; Heading 2 18pt bold black; body, bullets and numbered lists 11pt black;
links #0563C1 underlined; 2.0 line spacing everywhere with 0pt before/after; Letter paper,
1-inch margins, no headers or footers.

To change the standard, edit the constants below. Don't override per article.
"""
import re
import sys

import docx
from docx import Document
from docx.enum.text import WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

FONT_NAME = "Arial"
BODY_PT = 11
H1_PT = 24          # Title style
H2_PT = 18          # Heading 2 style
H3_PT = 14          # v1-era size; v2 renders markdown H3 as bold body text at BODY_PT
BLACK = RGBColor(0x00, 0x00, 0x00)
LINK_BLUE = "0563C1"
PAGE_WIDTH_IN = 8.5
PAGE_HEIGHT_IN = 11
MARGIN_IN = 1.0

BULLET_RE = re.compile(r"^\s*[-*+] +")
NUMBER_RE = re.compile(r"^\s*\d+[.)] +")
TOKEN = re.compile(
    r"\[([^\]]+)\]\(([^)\s]+)\)"      # 1,2 link
    r"|\*\*(.+?)\*\*"                 # 3 bold (may contain links)
    r"|(?<!\*)\*(?!\s)([^*]+?)\*(?!\*)"  # 4 italic
)


# ---------------------------------------------------------------- styles

def _set_fonts(rpr_owner_element, font=FONT_NAME):
    """Force an explicit font on a style or run, removing theme-font overrides."""
    rpr = rpr_owner_element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rfonts.get(qn(attr)) is not None:
            del rfonts.attrib[qn(attr)]
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(attr), font)


def _format_style(style, size, bold=False):
    style.font.name = FONT_NAME
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.italic = False
    style.font.color.rgb = BLACK
    _set_fonts(style.element)
    pf = style.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    # Drop borders (the default Title style has a bottom rule).
    ppr = style.element.get_or_add_pPr()
    for bdr in ppr.findall(qn("w:pBdr")):
        ppr.remove(bdr)


def setup_document():
    doc = Document()
    for section in doc.sections:
        section.page_width = Inches(PAGE_WIDTH_IN)
        section.page_height = Inches(PAGE_HEIGHT_IN)
        for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
            setattr(section, side, Inches(MARGIN_IN))
    _format_style(doc.styles["Normal"], BODY_PT)
    _format_style(doc.styles["Title"], H1_PT, bold=True)
    _format_style(doc.styles["Heading 2"], H2_PT, bold=True)
    _format_style(doc.styles["List Bullet"], BODY_PT)
    _format_style(doc.styles["List Number"], BODY_PT)
    return doc


# ---------------------------------------------------------------- inline

def _run(paragraph, text, bold=False, italic=False):
    run = paragraph.add_run(text)
    run.font.name = FONT_NAME
    _set_fonts(run._element)
    if bold:
        run.font.bold = True
    if italic:
        run.font.italic = True
    return run


def _hyperlink(paragraph, text, url, bold=False, italic=False):
    r_id = paragraph.part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(attr), FONT_NAME)
    rpr.append(rfonts)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    color = OxmlElement("w:color")
    color.set(qn("w:val"), LINK_BLUE)
    rpr.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    rpr.append(underline)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def add_inline(paragraph, text, bold=False, italic=False):
    """Render **bold**, *italic* and [links](url), including links inside bold."""
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            _run(paragraph, text[pos:m.start()], bold, italic)
        if m.group(1) is not None:
            _hyperlink(paragraph, m.group(1), m.group(2), bold, italic)
        elif m.group(3) is not None:
            add_inline(paragraph, m.group(3), True, italic)
        else:
            add_inline(paragraph, m.group(4), bold, True)
        pos = m.end()
    if pos < len(text):
        _run(paragraph, text[pos:], bold, italic)


def plain_heading_text(text):
    """Headings carry no manual bold; keep links and italics as plain text."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"\*+", "", text).strip()


# ---------------------------------------------------------------- lists

def _new_numbering(doc):
    """Create a fresh w:num on the List Number abstract so each list restarts at 1."""
    numbering = doc.part.numbering_part.element
    style_ppr = doc.styles["List Number"].element.pPr
    base_num_id = style_ppr.numPr.numId.val
    abstract_id = None
    for num in numbering.findall(qn("w:num")):
        if num.get(qn("w:numId")) == str(base_num_id):
            abstract_id = num.find(qn("w:abstractNumId")).get(qn("w:val"))
            break
    existing = [int(n.get(qn("w:numId"))) for n in numbering.findall(qn("w:num"))]
    new_id = max(existing) + 1
    num = OxmlElement("w:num")
    num.set(qn("w:numId"), str(new_id))
    abstract = OxmlElement("w:abstractNumId")
    abstract.set(qn("w:val"), abstract_id)
    num.append(abstract)
    override = OxmlElement("w:lvlOverride")
    override.set(qn("w:ilvl"), "0")
    start = OxmlElement("w:startOverride")
    start.set(qn("w:val"), "1")
    override.append(start)
    num.append(override)
    numbering.append(num)
    return new_id


def _apply_num_id(paragraph, num_id):
    ppr = paragraph._p.get_or_add_pPr()
    numpr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), "0")
    numid = OxmlElement("w:numId")
    numid.set(qn("w:val"), str(num_id))
    numpr.append(ilvl)
    numpr.append(numid)
    ppr.append(numpr)


# ---------------------------------------------------------------- blocks

def classify(line):
    if BULLET_RE.match(line):
        return "bullet"
    if NUMBER_RE.match(line):
        return "number"
    return "text"


def group_lines(lines):
    """Split one markdown block into runs of bullet / number / text lines."""
    groups = []
    for line in lines:
        kind = classify(line)
        if groups and groups[-1][0] == kind:
            groups[-1][1].append(line)
        else:
            groups.append((kind, [line]))
    return groups


class Builder:
    def __init__(self, doc):
        self.doc = doc
        self.started = False        # anything written yet
        self.last = None            # "heading" | "body" | "empty"
        self.has_title = False

    def empty(self):
        if self.started and self.last not in ("empty", "heading"):
            self.doc.add_paragraph(style="Normal")
            self.last = "empty"

    def heading(self, text, level):
        text = plain_heading_text(text)
        if not text:
            return  # never style an empty paragraph as a heading
        if level == 1 and not self.has_title and not self.started:
            p = self.doc.add_paragraph(style="Title")
            add_inline(p, text)
            self.has_title = True
        else:
            if self.started and self.last != "empty":
                self.doc.add_paragraph(style="Normal")
            p = self.doc.add_paragraph(style="Heading 2")
            add_inline(p, text)
        self.started = True
        self.last = "heading"

    def body_group(self, kind, lines):
        self.empty()
        if kind == "bullet":
            for line in lines:
                p = self.doc.add_paragraph(style="List Bullet")
                add_inline(p, BULLET_RE.sub("", line, count=1).strip())
        elif kind == "number":
            num_id = _new_numbering(self.doc)
            for line in lines:
                p = self.doc.add_paragraph(style="List Number")
                _apply_num_id(p, num_id)
                add_inline(p, NUMBER_RE.sub("", line, count=1).strip())
        else:
            for line in lines:
                p = self.doc.add_paragraph(style="Normal")
                add_inline(p, line.strip())
        self.started = True
        self.last = "body"

    def subheading(self, text, rest):
        """Markdown H3 -> full-bold Normal paragraph; continuation lines stay tight."""
        self.empty()
        p = self.doc.add_paragraph(style="Normal")
        add_inline(p, re.sub(r"\*\*", "", text).strip(), bold=True)
        self.started = True
        self.last = "body"
        for kind, lines in group_lines(rest):
            if kind == "text":
                for line in lines:
                    q = self.doc.add_paragraph(style="Normal")
                    add_inline(q, line.strip())
            else:
                self.body_group(kind, lines)


def strip_frontmatter(raw):
    m = re.match(r"^---\s*\n.*?\n---\s*\n", raw, flags=re.DOTALL)
    return raw[m.end():] if m else raw


def build(md_path, out_path):
    with open(md_path, encoding="utf-8") as fh:
        body = strip_frontmatter(fh.read())

    doc = setup_document()
    b = Builder(doc)

    for block in re.split(r"\n\s*\n", body.strip()):
        lines = [re.sub(r"^\s*> ?", "", l).rstrip() for l in block.split("\n")]
        lines = [l for l in lines if l.strip() and not re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", l)]
        while lines:
            first = lines[0]
            h = re.match(r"^(#{1,6})(?:\s+(.*))?$", first)
            if not h:
                break
            level = len(h.group(1))
            if level >= 3:
                b.subheading(h.group(2) or "", lines[1:])
                lines = []
                break
            b.heading(h.group(2) or "", level)
            lines = lines[1:]
        if not lines:
            continue
        for kind, group in group_lines(lines):
            b.body_group(kind, group)

    doc.save(out_path)
    print(f"built {out_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit('usage: markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"')
    build(sys.argv[1], sys.argv[2])
