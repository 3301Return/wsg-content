---
name: wsg-article-formatting
description: Heading and spacing rules for WallStreetGuide (WSG) article documents. Use this skill any time a WSG article draft needs formatting, styling, or layout cleanup — applying Title / Heading 2 / Normal styles, fixing empty-line spacing between paragraphs, headings, and lists, or preparing a draft for publication as a Word doc or Google Doc. Trigger on requests like "format this article," "apply the WSG formatting spec," "fix the headings and spacing," "clean up the styling in this draft," or whenever a WSG article is being converted to or delivered as a .docx — even if the user doesn't explicitly mention formatting.
---

# WSG Article Formatting Spec

Instructions for applying heading structure and paragraph spacing to a Wall Street Guide article. Apply these rules to any article draft, whether it arrives with no styling at all or with inconsistent styling.

## Heading levels: there are only two

| Element | Style | How many |
|---|---|---|
| Article title | **Title** | Exactly one, always the first line |
| Section heading | **Heading 2** | As many as the article has sections |
| Everything else | **Normal** (body) | The rest |

Do not use Heading 1. Do not use Heading 3 or deeper. If the article seems to need a sub-subheading, make it a bold body paragraph instead.

## Document skeleton, in order

1. **Title** style. The article title, once, on the first line.
2. Body paragraph beginning with the bold label `Meta description:` followed by the meta description text.
3. One to three body paragraphs of intro. No heading above them.
4. First **Heading 2**, then its body paragraphs. Repeat for every section.

## Spacing: one empty line between blocks

Nothing should sit on the line immediately after the block above it. Insert one empty paragraph between blocks, using this table:

| Between | Empty lines |
|---|---|
| Two body paragraphs | 1 |
| Body paragraph and the heading below it | 1 |
| Heading and the body paragraph below it | 0 |
| Two items in a bullet or numbered list | 0 |
| Body paragraph and the list below or above it | 1 |
| Meta description and the intro paragraph below it | 1 |
| A "Say this, don't say that" question and its Don't say / Say lines | 0 |
| One "Say this, don't say that" triplet and the next question | 1 |

Never more than one empty line anywhere. The Title at the top needs nothing above it.

```
...end of the previous body paragraph.
                              <- one empty line
Next body paragraph starts here.
                              <- one empty line
Heading 2 text here
Body starts on the very next line.
```

The asymmetry is intentional. Body paragraphs are separated from each other and from the heading below them, but a heading sits tight against the body it introduces. Do not "correct" this by adding a line after headings.

## Body text

Body text is Normal style. Bold is used inside body text for three purposes, and heading styles are never used for any of them:

- **Emphasis sentences.** One key sentence in a section may be fully bold. Keep this sparing, roughly one per section.
- **Inline labels.** `Meta description:`, `Don't say:`, `Say:` and similar are bold, followed by unbold text.
- **Sub-labels.** In sections like "Say this, don't say that," each interview question is a bold body paragraph, not a heading.

## Do not

- Do not apply a heading style to an empty paragraph. An empty heading pollutes the document outline and breaks navigation and table-of-contents generation.
- Do not leave two or more consecutive empty paragraphs anywhere in the document.
- Do not run body paragraphs together with no empty line between them.
- Do not fake a heading by bolding a body paragraph and putting it on its own line. If it is a section heading, it gets Heading 2 style.
- Do not bold heading text. The Heading 2 style already carries its own weight.
- Do not add or remove section numbering. If the incoming headings are numbered, keep the numbers as written. If they are not, do not introduce them.
- Do not change the wording of the title, headings, or body. This task is styling and spacing only.

## Worked example

Input, with no styling and no paragraph spacing:

```
Private Credit Salary 2026: Full Breakdown
Meta description: WSG founder Stephen Turban breaks down private credit salary in 2026.
Private credit pays banking-level compensation on roughly two-thirds of banking's hours.
A first-year analyst at a top private credit platform earns $180,000 to $250,000 all-in.
How much does a private credit analyst make in 2026?
First-year analysts at top platforms earn $130,000 to $150,000 in base salary.
```

Output:

```
[Title]     Private Credit Salary 2026: Full Breakdown
[Normal]    **Meta description:** WSG founder Stephen Turban breaks down private credit salary in 2026.
[Normal]    (empty)
[Normal]    Private credit pays banking-level compensation on roughly two-thirds of banking's hours.
[Normal]    (empty)
[Normal]    **A first-year analyst at a top private credit platform earns $180,000 to $250,000 all-in.**
[Normal]    (empty)
[Heading 2] How much does a private credit analyst make in 2026?
[Normal]    First-year analysts at top platforms earn $130,000 to $150,000 in base salary.
```

## Check before returning the document

1. First line is Title style, and it is the only Title in the document.
2. Every section heading is Heading 2. No Heading 1, no Heading 3.
3. No heading is empty.
4. Every body paragraph has exactly one empty line between it and the paragraph before it.
5. Every heading has exactly one empty line above it and none below it.
6. List items are tight against each other, with one empty line before the first and after the last.
7. No two empty paragraphs sit next to each other.
8. The meta description is a body paragraph with a bold label, not a heading.
9. Sub-labels and emphasis sentences are bold body text, not headings.
10. Wording is unchanged from the input.

## Visual spec (locked May 24, 2026 — still current)

The structure rules above say which style each paragraph gets; these rules say what the styles look like. Canonical copy: `style-guide/publication-standards.md` section 1.

### Font

- **Arial, throughout.** Body, headings, bullets, numbered lists, hyperlinks all use Arial. No mixed fonts.

### Sizes

| Element | Size | Weight | Other |
| --- | --- | --- | --- |
| H1 title | 24pt | Bold | Black |
| H2 section header | 18pt | Bold | Black |
| H3 firm name / sub-header | 14pt | Bold | **Underlined**, Black — v1-era row: under the current structure spec above, markdown H3s render instead as full-bold 11pt Normal paragraphs |
| Body paragraph | 11pt | Regular | Black |
| Bullets and numbered lists | 11pt | Regular | Black |
| Inline links | matches surrounding size | Regular | Blue (#0563C1), underlined |

Bold text inside body or headings keeps the same size as the surrounding text. Markdown `**bold**` becomes bold runs inline.

### Line spacing

**2.0 (double) on everything.** Body, headings, bullets, numbered lists. No exceptions.

- `space_before` = 0
- `space_after` = 0
- `line_spacing_rule` = WD_LINE_SPACING.DOUBLE

The visual rhythm comes from the line spacing itself plus the size delta between body and headings, not from extra space-before/after.

### Color

- Black for all text except inline hyperlinks.
- Word's default heading styles render in blue. **Override to black.** The builder script does this; if hand-editing in Word, set all heading text to black explicitly.
- Hyperlinks: `#0563C1` (Word's default accent blue), underlined.

### Page setup

Default 1-inch margins on all sides. Letter size (8.5 x 11). No headers or footers — Wix supplies its own page chrome.

### Builder

`python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"` enforces this entire spec (structure + visuals). v1 `markdown_to_docx.py` (direct-formatting, May 2026 spec) is retained for history only; new builds always go through v2.

When auditing a docx before publish, look for these five tells of a non-conforming file:
1. Times New Roman or Calibri creeping in (Word's defaults).
2. Blue headings (Word default for H1/H2 styles).
3. Single-spaced body.
4. H3 firm names without underline.
5. H1 smaller than 24pt or H2 smaller than 18pt.

Fix any of those before delivery.
