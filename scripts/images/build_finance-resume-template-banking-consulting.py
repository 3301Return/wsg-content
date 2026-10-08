#!/usr/bin/env python3
"""Images for drafts/draft-finance-resume-template-banking-consulting-v1.md (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_finance-resume-template-banking-consulting.py

1. 01-jane-doe-page-callouts.png      page 1 of the Jane Doe sample PDF with five numbered callouts
2. 02-bullet-formula.png              the verb, what, how, number bullet built from a weak one
3. 03-banking-read-vs-consulting-read.png  the same page twice with the six tilts marked

Idempotent: every run rewrites the three PNGs and the manifest.
"""
import sys
from pathlib import Path

sys.path.insert(0, "scripts/images")
from wsg_viz import *                      # noqa: F401,F403
from resume_callouts import *              # noqa: F401,F403
from matplotlib.patches import FancyBboxPatch

SLUG = "finance-resume-template-banking-consulting"
OUT = Path("published/assets/images") / SLUG
PDF = "published/assets/Sample Finance Resume (Jane Doe).pdf"
OUT.mkdir(parents=True, exist_ok=True)
entries = []


# ---------------------------------------------------------------- 01 the sample page with callouts
page, lines = load_page(PDF)
callouts = [
    (region(lines, "JANE DOE", last="linkedin.com/in/jane-doe-sample", full_width=False),
     "One header line",
     "Name in capitals, then phone, email, city and LinkedIn. No street address and no objective under it."),
    (region(lines, "GPA: 3.78", full_width=False),
     "GPA on its own line",
     "Two decimals, out of 4.00, with honors and the ACT sharing the line. The expected graduation date stays on the degree line above it."),
    (region(lines, "Built the trading comparables", last="buyers"),
     "Verb, what, how, number",
     "Built (verb) the comps and precedents (what) for a $45MM sell-side mandate (how); the range set bid guidance sent to 9 buyers (number). This is the one bullet a banking screener is sure to read."),
    (region(lines, "LEADERSHIP & ACTIVITIES", last="without advertising"),
     "Leadership carries real weight",
     "Three entries with numbers from the organization: 35 members, $3,000 raised, 90 to 140, second of 18. A consulting screener scores this section as hard as the internships."),
    (region(lines, "ADDITIONAL INFORMATION", last="Basketball"),
     "Three lines of Additional Information",
     "Tools actually used, languages with an honest proficiency word, and interests specific enough to start a conversation."),
]
f1 = draw_callouts(page, callouts, OUT / "01-jane-doe-page-callouts.png")
entries.append({
    "file": "01-jane-doe-page-callouts.png",
    "alt": "Jane Doe sample resume with five numbered callouts on the header, GPA line, first bullet, Leadership section and Additional Information.",
    "caption": "The whole page at a glance: five places a screener's eyes land, and the rule each one follows.",
    "method": "Page 1 of published/assets/Sample Finance Resume (Jane Doe).pdf rendered with pdftoppm at 150 dpi; callouts drawn with Pillow from pdfplumber line positions (scripts/images/resume_callouts.py).",
    "anchor": "That's the whole page: twelve bullets across Experience and ",
})


# ---------------------------------------------------------------- 02 the bullet formula
fig, ax = new_figure(width=11.0, height=6.4)
ax.axis("off")
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.text(0.04, 0.93, "Four parts turn a duty into a bullet a screener can use",
         fontsize=17, fontweight="bold", color=TEXT_PRIMARY, va="center")
fig.text(0.04, 0.855, "Don't write:", fontsize=12.5, color=TEXT_SECONDARY, va="center", fontweight="bold")
fig.text(0.175, 0.855, "“Assisted the deal team with financial analysis and presentation materials.”",
         fontsize=12.5, color=TEXT_MUTED, va="center", style="italic")

rows = [
    ("Verb", BLUE, "Built", "the verb for the thing you actually did, not “assisted”"),
    ("What", ORANGE, "the trading comparables and precedent transactions analyses",
     "name the artifact, so an interviewer knows what to ask about"),
    ("How", AQUA, "for a $45MM sell-side mandate for a founder-owned logistics company",
     "what it was for and how big it was"),
    ("Number", YELLOW, "the valuation range from the analysis set the first-round bid guidance the bank sent to 9 buyers",
     "what happened because the thing existed"),
]
y = 0.745
for label, color, segment, note in rows:
    chip = FancyBboxPatch((0.04, y - 0.034), 0.11, 0.068, boxstyle="round,pad=0,rounding_size=0.012",
                          transform=fig.transFigure, facecolor=color, edgecolor="none")
    fig.patches.append(chip)
    ink = "white" if color != YELLOW else TEXT_PRIMARY
    fig.text(0.095, y, label, fontsize=13, fontweight="bold", color=ink, ha="center", va="center")
    fig.text(0.175, y + 0.013, segment, fontsize=13, color=TEXT_PRIMARY, va="center")
    fig.text(0.175, y - 0.030, note, fontsize=11.5, color=TEXT_SECONDARY, va="center")
    y -= 0.135

fig.text(0.04, 0.215, "Put together:", fontsize=12.5, color=TEXT_SECONDARY, va="center", fontweight="bold")
full = ("“Built the trading comparables and precedent transactions analyses for a $45MM sell-side mandate "
        "for a founder-owned logistics company; the valuation range from the analysis set the first-round "
        "bid guidance the bank sent to 9 buyers.”")
import textwrap
for k, line in enumerate(textwrap.wrap(full, 108)):
    fig.text(0.175, 0.215 - k * 0.05, line, fontsize=12.5, color=TEXT_PRIMARY, va="center")
fig.text(0.175, 0.055, "Two lines, one semicolon, four pieces of information a screener can use.",
         fontsize=11.5, color=TEXT_SECONDARY, va="center")
save_figure(fig, OUT / "02-bullet-formula.png", tight=False)
entries.append({
    "file": "02-bullet-formula.png",
    "alt": "Diagram splitting Jane's comps bullet into four labeled parts: verb, what, how and number, above the assembled bullet.",
    "caption": "Every strong bullet on the page is these four parts in this order, and the weak version at the top has none of them.",
    "method": "Matplotlib text diagram from the article's section 4 worked example (scripts/images/build_finance-resume-template-banking-consulting.py).",
    "anchor": "Put together: \"Built the trading comparables and precedent t",
})


# ---------------------------------------------------------------- 03 banking read vs consulting read
coursework = region(lines, "Relevant Coursework", last="Intermediate Microeconomics")
skills = region(lines, "Technical Skills", last="Conversational Portuguese")
margin_bullet = region(lines, "Built a menu-level margin analysis", last="over the following quarter", pad=4)
left = {
    "title": "Banking read", "subtitle": "The sample as shown in section 3", "color": BLUE,
    "callouts": [
        (region(lines, "Regional Boutique Investment Bank", last="weekly client call"),
         "The banking summer sits first under Experience."),
        (region(lines, "Built the trading comparables", last="buyers", pad=4),
         "The comps bullet leads: its range set the bid guidance.", "right"),
        (region(lines, "Built and maintained a buyer list", last="weekly client call", pad=4),
         "The buyer list keeps its own bullet; the case competition gets one.", "right"),
        (coursework, "Coursework leads with Corporate Finance, Financial Accounting, Valuation."),
        (skills, "Skills lead with Excel modeling, Capital IQ, PitchBook; Wall Street Prep first."),
        (margin_bullet, "Bullets open on the artifact: “Built a menu-level margin analysis of 40 items...”"),
    ],
}
right = {
    "title": "Consulting read", "subtitle": "What the six changes in section 7 move on the same page", "color": ORANGE,
    "callouts": [
        (region(lines, "Student Pro Bono Consulting Group", last="approve two new sites"),
         "The pro bono consulting group moves to the top; it runs to Present, so the order stays honest."),
        (region(lines, "Drafted 14 pages", last="bidders", pad=4),
         "The CIM bullet leads: written synthesis a managing director put in front of a client."),
        (region(lines, "Regional Undergraduate Case Competition", last="consultants and operators"),
         "The case competition gets a second bullet; the buyer list bullet shrinks to one line to pay for it."),
        (coursework, "Coursework leads with Econometrics, Business Statistics, Intermediate Micro."),
        (skills, "Skills lead with Stata, Python, SQL; Fluent Spanish moves to the front of its line."),
        (margin_bullet, "Bullets open on the team and the client: “Led a 5-person team on a 10-week pricing project...”", "right"),
    ],
}
draw_two_reads(page, left, right, OUT / "03-banking-read-vs-consulting-read.png")
entries.append({
    "file": "03-banking-read-vs-consulting-read.png",
    "alt": "Jane Doe's resume shown twice, with six numbered boxes marking what the banking and consulting versions each lead with.",
    "caption": "Same page, same facts: the six boxes are the only things that move between the banking version and the consulting version.",
    "method": "Page 1 of published/assets/Sample Finance Resume (Jane Doe).pdf rendered twice at 150 dpi with Pillow boxes on the six regions section 7 describes (scripts/images/resume_callouts.py).",
    "anchor": "Here are the six changes marked on Jane's page, the banking ",
})

write_manifest(OUT, entries)
print(f"wrote {len(entries)} images to {OUT}")
