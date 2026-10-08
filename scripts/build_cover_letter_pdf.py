#!/usr/bin/env python3
"""Build the sample IB cover letter PDF (one page, letter size) from drafts/sample-ib-cover-letter-john-doe.md.

Usage: python3 scripts/build_cover_letter_pdf.py [input.md] [output.pdf]
Metadata is set to Wall Street Guide; no personal identifiers are embedded.
"""
import sys
from pathlib import Path

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "drafts/sample-ib-cover-letter-john-doe.md")
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "published/assets/Sample Investment Banking Cover Letter (John Doe).pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

lines = SRC.read_text(encoding="utf-8").splitlines()

# Split into blocks on blank lines
blocks, cur = [], []
for ln in lines:
    if ln.strip() == "":
        if cur:
            blocks.append(cur)
            cur = []
    else:
        cur.append(ln.rstrip())
if cur:
    blocks.append(cur)

body = ParagraphStyle("body", fontName="Helvetica", fontSize=11, leading=14.5, alignment=TA_LEFT, spaceAfter=0)
name = ParagraphStyle("name", parent=body, fontName="Helvetica-Bold", fontSize=14, leading=17)
contact = ParagraphStyle("contact", parent=body, fontSize=10.5, leading=13)

story = []
for i, blk in enumerate(blocks):
    if i == 0:
        # Header block: name line bold, contact line under it
        story.append(Paragraph(blk[0], name))
        for extra in blk[1:]:
            story.append(Paragraph(extra.replace("|", "&nbsp;|&nbsp;"), contact))
        story.append(Spacer(1, 14))
        continue
    # Multi-line blocks (recipient block, sign-off) keep their line breaks
    text = "<br/>".join(blk)
    story.append(Paragraph(text, body))
    story.append(Spacer(1, 11))

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    leftMargin=1 * inch,
    rightMargin=1 * inch,
    topMargin=0.9 * inch,
    bottomMargin=0.9 * inch,
    title="Sample Investment Banking Cover Letter (John Doe)",
    author="Wall Street Guide",
    subject="Sample cover letter for an Investment Banking Summer Analyst application",
    creator="Wall Street Guide",
    producer="Wall Street Guide",
)
doc.build(story)
print(f"wrote {OUT}")
