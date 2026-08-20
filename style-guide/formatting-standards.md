# WSG Formatting Standards (locked May 24, 2026)

This document is the single source of truth for how every WSG .docx output must look. The `scripts/markdown_to_docx.py` builder enforces this. Manual edits in Word must match the same standard so files are visually consistent across the entire library.

## Default byline

Every WSG article is ghostwritten for **Stephen Turban** (founder of WallStreetGuide.net) unless the brief or content calendar explicitly names a different writer.

- Frontmatter must include `byline: stephen-turban`.
- The writer profile lives at `writers/stephen-turban.md` and contains the approved voice templates and "what NOT to write" guardrails (no banker self-references).
- Meta description must lead with "WSG founder Stephen Turban..." so the byline shows in SERP and OG cards.

## Font

- **Arial, throughout.** Body, headings, bullets, numbered lists, hyperlinks all use Arial. No mixed fonts.

## Sizes

| Element | Size | Weight | Other |
| --- | --- | --- | --- |
| H1 title | 24pt | Bold | Black |
| H2 section header | 18pt | Bold | Black |
| H3 firm name / sub-header | 14pt | Bold | **Underlined**, Black |
| Body paragraph | 11pt | Regular | Black |
| Bullets and numbered lists | 11pt | Regular | Black |
| Inline links | matches surrounding size | Regular | Blue (#0563C1), underlined |

Bold text inside body or headings keeps the same size as the surrounding text. Markdown `**bold**` becomes bold runs inline.

## Line spacing

**2.0 (double) on everything.** Body, headings, bullets, numbered lists. No exceptions.

- `space_before` = 0
- `space_after` = 0
- `line_spacing_rule` = WD_LINE_SPACING.DOUBLE

The visual rhythm comes from the line spacing itself plus the size delta between body and headings, not from extra space-before/after.

## Color

- Black for all text except inline hyperlinks.
- Word's default heading styles render in blue. **Override to black.** The builder script does this; if hand-editing in Word, set all heading text to black explicitly.
- Hyperlinks: `#0563C1` (Word's default accent blue), underlined.

## What this means for the docx builder

The builder script at `scripts/markdown_to_docx.py` already enforces every rule above. If you change the standard, change the constants at the top of that file (`FONT_NAME`, `BODY_PT`, `H1_PT`, `H2_PT`, `H3_PT`, `BLACK`, `LINK_BLUE`) — don't override per-article.

## What this means for hand edits in Word

If Stephen or any editor opens the .docx in Word and adds new paragraphs:

1. Highlight the new content, set font to Arial.
2. Body = 11pt, H1 = 24pt, H2 = 18pt, H3 = 14pt with underline.
3. Set line spacing to 2.0 (Home → Line Spacing → 2.0).
4. Set color to Black (Home → Font Color → Black).

Or, simpler: re-export the markdown via `python3 scripts/markdown_to_docx.py drafts/{file}.md "published/{Title}.docx"` and re-paste into Wix.

## Page setup

Default 1-inch margins on all sides. Letter size (8.5 x 11). No headers or footers — Wix supplies its own page chrome.

## Why this matters

Consistent formatting across the library is what makes WSG read as a serious editorial brand rather than a junk content farm. A single inconsistent doc (mixed fonts, blue Word default headings, single-spaced body) undermines the whole library.

When auditing a docx before publish, look for these five tells of a non-conforming file:
1. Times New Roman or Calibri creeping in (Word's defaults).
2. Blue headings (Word default for H1/H2 styles).
3. Single-spaced body.
4. H3 firm names without underline.
5. H1 smaller than 24pt or H2 smaller than 18pt.

Fix any of those before delivery.
