# Changelog: skill and tooling update (October 7, 2026)

Source: Stephen's comments on the MECE draft, Sanskar's Slack notes on negatives and image sourcing, and the founder's review of the October 5 batch. Previous articles were not revised.

## Writing rules

- **No author voice or byline.** Articles are written as WSG in "we" and "you." No "I," no Stephen Turban intro or credentials, no first-person memories, no `byline:` frontmatter. Meta descriptions lead with the topic. `writers/stephen-turban.md` retired for drafting.
- **Intros are optional and short.** Zero to three plain sentences: topic, why it matters, what the article covers. No hooks, stories, scenes or buildup. Model intro: "If you're in consulting, you've probably heard about the MECE framework..." (`.claude-skill/intros.md`, rewritten).
- **Plain headers.** A reader who sees only the header knows what's under it. No metaphors or clever colon halves ("start with a room, not a business" is the flagged example). Same rule for word choice in the body.
- **No negatives.** Nothing about what the writer, WSG or the article isn't or won't do ("I'm not a banker"), and no negative framing of the reader. Factual downsides the reader needs stay.

## Images

- **Source line under every image** in the article, from the manifest's new `source` field. `scripts/images/insert_images.py` writes `*Source: ...*` under the image; `markdown_to_docx_v2.py` renders it centered, italic, 9 pt; `markdown_to_wix_html.py` renders it as an italic paragraph.
- **Banking chart format** in `scripts/images/wsg_viz.py`: black text, no gridlines, no frames, navy / mid blue / gray / light blue series (`BANK_SERIES`), direct labels, `add_source()` for a bottom-left source line, and `bank_table()` for tables as clean graphics (no cell borders, rules under the header and above totals). `style_axes()` now turns gridlines off for every chart, including rebuilds of older scripts.
- **More variety and outside images.** Statista-style charts preferred, mixed with tables, timelines, diagrams, model screenshots and credited outside images. Bloomberg, WSJ, FT, Reuters and CNBC charts and graphics are now allowed with a source line (founder approval, October 7). Watermarked stock-agency photos, AI images, logos as images and private people stay out.

## Files changed

`.claude-skill/` SKILL.md (October 7 rules at the top), intros.md, images.md, prose-editing.md (rules 9 to 11), consulting.md, formatting.md; `CLAUDE.md`; `style-guide/style-guide.md`, `style-guide/formatting-standards.md`; `templates/niche.md`, `ultimate-guide.md`, `_brief-template.md`; `consulting/voice-cues.md`; `writers/stephen-turban.md`, `writers/README.md`; `scripts/images/wsg_viz.py`, `scripts/images/insert_images.py`, `scripts/markdown_to_docx_v2.py`; `skills/` wsg-article, wsg-intros, wsg-prose-editing, wsg-article-formatting rebuilt, wsg-article-images added.
