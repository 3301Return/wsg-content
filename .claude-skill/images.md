---
name: wsg-article-images
description: "Add pictures and graphs to a WallStreetGuide (WSG) article: banking-style charts and tables from the article's numbers, Excel screenshots rebuilt from its worked model, diagrams, annotated sample pages, and credited images from outside sources (Bloomberg, WSJ, FT, filings, firm pages, photos). Every image gets a source line, and every word on or under an image (titles, labels, callouts, captions, alt text) goes through built-in plain-language and humanizer passes so it reads plain, clear and professional, not AI-written. Use when asked for images, screenshots, charts, photos or visuals for a WSG article, or to fix AI-sounding text in existing images."
---

# WSG Article Images

An article's pictures teach the same way its worked examples do: a reader who skims should be able to look at the chart or the screenshot and get the point without reading the paragraph. This skill says what to illustrate, how each kind of image should look, how the words on it should read, where outside images can come from, how every image is sourced, and how the files get into the .docx and onto Wix.

Repo copy of this module: `.claude-skill/images.md`. Toolkit: `scripts/images/wsg_viz.py`. Inserter: `scripts/images/insert_images.py`. Worked examples: `scripts/images/build_*.py`, `scripts/images/models/`, `published/assets/images/*/manifest.json`. If the repo isn't attached, ask for it (or the Claude Content project mirror) before starting.

## What changed on October 8, 2026 (Stephen via Sanskar)

Stephen likes the images, but **the language in them still reads AI/Claude-y.** Image text now gets two passes: plain language (so a reader understands every word) and the humanizer (so it doesn't read as AI). Chart titles written as clever claims, captions that narrate ("and the close is expected the day after this guide's date check"), callouts with a twist at the end. From now on every string on or under an image gets the humanizer pass in this file before the image is rendered for delivery. Short literal titles are the default; an occasional plain takeaway title is fine. Keep it professional: it should read like a bank pitch book or a Statista chart.

## What changed on October 7, 2026 (founder review)

1. **Every image has a source line in the article**, directly under it: "Source: Bloomberg, March 2026," "Source: Company Form 10-K for fiscal 2025, SEC EDGAR." For a chart built from the article's own worked example: "Source: WSG analysis of the worked example in this article." The manifest's `source` field drives it; `insert_images.py` writes the line.
2. **Banking format for every chart and table we build:** black text, no gridlines, no boxes, borders or cell lines, no chart frame, direct data labels instead of a value axis, and the source in the bottom-left corner.
3. **Cleaner images:** fewer words, at most about six bars or five series, labels that don't collide, nothing decorative.
4. **More variety.** Statista-style charts are the default, but an article with four or more images mixes types: charts, clean tables, timelines, diagrams, model screenshots, and outside images.
5. **Outside images are welcome, credited.** News charts and graphics (Bloomberg, WSJ, FT, Reuters, CNBC), filing pages, firm pages, press photos and report charts, each with a source line.

## Three kinds of image

1. **Charts and tables we build** from the article's numbers, in the banking format below. The preferred default.
2. **Model screenshots** of our own rebuilt workbook (model articles only). **Models are rebuilt, not screenshotted from someone else's template file.**
3. **Outside images**: a news chart, a filing page, a firm's page, a photo of the real person, place or document a passage talks about. Credited every time.

Never AI-generated imagery, logos used as the image, or decorative stock pictures. Every image shows the actual subject of the passage beside it.

## The banking format (charts and tables we build)

- **Text:** black (`BLACK` in `wsg_viz`), Arial. Title in bold, left-aligned, written per "Image text" below. No subtitle unless it carries the unit ("$ thousands, first-year analysts").
- **No gridlines, no boxes, no frames, no cell borders.** One thin black baseline where the chart needs one. Bar charts carry direct value labels and drop the value axis; line charts may keep a light value axis (`value_axis=True`) with no gridlines.
- **Color:** `BANK_SERIES` (navy, mid blue, gray, light blue) in that order. Gray for the comparison group, navy for the subject.
- **Tables as graphics:** `bank_table()`: black text, bold header with a thin rule under it, a thin rule above any total row, numbers right-aligned, no cell lines.
- **Source:** `add_source(fig, "...")` puts "Source: ..." in the bottom-left corner. The article's source line repeats it.
- **Clean:** horizontal bars when labels are long; at most about six bars; no legend when direct labels do the job.

Load the `dataviz` skill before drawing and follow its form rules.

## Image text: the built-in humanizer pass (October 8, 2026)

**Image text** means every word a reader sees on or under an image: chart and table titles, subtitles, axis titles, category and data labels, legend entries, annotations and callouts, diagram box labels, timeline entries, the caption, the alt text, and the source line. All of it gets this pass. It's the `humanizer` skill's method cut down for short strings, plus WSG's say-it-out-loud test.

### The rules

1. **Titles are short and literal by default.** Say what the chart shows: the measure, the group, the period. Under about 10 words.
   - "First-year analyst base pay, 2026"
   - "Centerview mandates by deal size"
   - "Paramount and Warner Bros. Discovery: deal timeline"

   **An occasional takeaway title is fine** when the point of the chart is one plain fact, and it's said the way a banker would say it in a meeting: "Debt falls from $360M to $77M over five years." Use takeaway titles on at most about one in three images, and vary the shape across an article.

2. **Captions are one plain sentence that says what to look at.** Under about 20 words. A fact from the chart, not a comment about it. No story, no joke, no twist at the end, no "notice how," no "the day after this guide's date check."

3. **Labels and callouts are nouns and numbers.** "Interest: $25M," "Exit at 8.0x," "Hostile bid launched." No full sentences in a callout unless the callout is a quote.

4. **Alt text is 10 to 20 plain words describing what the image shows**, for a reader who can't see it. No interpretation.

5. **Source lines follow the set format.** "Source: {outlet or filing}, {title or topic}, {month year}." Nothing else in the line.

### What to cut (the AI tells that show up in image text)

| Pattern | Example from past captions | Plain version |
| --- | --- | --- |
| Clever claim as a title | "Centerview pays about a bulge bracket bonus more than a bulge bracket" | "Analyst pay: Centerview vs bulge bracket, 2026" |
| Stacked list that builds to a punchline | "A hostile bid against a signed deal, a board process, a shareholder vote, two regulators and a lawsuit, and the close is expected the day after this guide's date check." | "Paramount's bid took ten months from launch to expected close, including a shareholder vote and a state lawsuit." |
| "X, so Y" reasoning packed into a caption | "Interest shrinks as the debt does, so each year more of the cash goes to principal, and the paydown speeds up from 40 to 74 a year." | "Annual debt paydown rises from $40M in year 1 to $74M in year 5." |
| "It ties," "that's the whole story," "here's the catch" | "...is the $883 million the sponsor takes out, and it ties." | "Sponsor equity grows from $280M to $883M: $320M from EBITDA growth, $283M from debt paydown." |
| Antithesis ("not X, but Y," "X, not Y") | "Speed, not size, decides the bonus" | "Bonus by deal count, 2025" |
| Significance words | "pivotal," "key," "crucial," "striking," "notably," "the real story" | Cut, or give the number |
| Narrating the chart | "This chart shows...," "As you can see...," "Notice how..." | State the fact |
| Sales or drama words | "massive," "staggering," "skyrockets," "plummets" | "rises 40%," "falls by half" |
| Cute compression | "Pay, plainly," "The paydown, visualized" | Literal title |
| Em or en dashes, Unicode minus | "2022–2026," "−5%" | "2022-2026," "-5%" |

### How to run it

1. **Collect every string.** Pull titles and labels from each `build_{slug}.py` (or the chart calls) and `alt`, `caption` and `source` from the manifest. One list, one line per string, labeled by image. Run the plain-language pass (next section) on this list first, then continue here.
2. **If the `humanizer` skill is available, run it on the list in embedded mode** (return only the final text) with this instruction: "These are chart titles, captions and labels for a finance article. Keep every number, name and date. Make them short, literal and professional. No em dashes." Then check its output against the rules above; humanizer doesn't know the title-length or caption rules.
3. **If it isn't available, apply the rules and the cut table above by hand.** Use humanizer's core test on each string: delete the flagged part; if no fact disappeared, it was padding.
4. **Read every string out loud.** Would a banker say it that way in a meeting? If not, rewrite it plainly.
5. **Check the facts didn't move.** Every number, name and date in the rewritten text matches the article.
6. **Write the clean strings back** into the build script and manifest, then re-render. Never fix text by editing the PNG.

## Image text: the plain-language pass (October 8, 2026)

Runs on the same list of strings, before the humanizer pass. It's the `plain-language` skill cut down for chart text. The bar: **a sharp sophomore can read the chart once, without the article, and say what it shows.** The words get simpler; the numbers and facts don't change.

1. **Spell out jargon and abbreviations the article hasn't explained.** "LTM," "PF," "NWC," "TEV," "MoM," "UFCF" become "last 12 months," "pro forma," "net working capital," "enterprise value," "multiple of money," "unlevered free cash flow." If space is tight, spell it out in the title or caption once and use the short form in the labels. Standard units ("$M," "%," "x" for multiples) stay.
2. **Name the machinery in plain words.** A label like "Cov-lite share" becomes "Share of loans without maintenance covenants" or carries a caption that says what that means. Define the mechanism, never the field: "investment banking" needs no explaining.
3. **Unstack noun piles.** "Sponsor equity value creation bridge" becomes "How the sponsor's equity grows." "Post-close leverage covenant headroom" becomes "Room under the debt limit after the deal."
4. **One idea per caption.** If a caption needs "and" or "so" to hold a second idea, cut the second idea or move it to the article.
5. **Diagram boxes and timeline entries use everyday verbs.** "Bidders submit offers," not "Indicative bid submission phase."
6. **Axis titles say the measure and the unit.** "Base pay ($ thousands)," not "Comp (k)."
7. **Read it cold.** Cover the article and look at the image alone. If you'd need the paragraph to understand a label, rewrite the label.

## What to illustrate (and what not to)

Volume is a judgment call based on the article's length and its real subjects, not a quota. Two to four images where they teach something, more where they help; model articles run to 10 or more.

Illustrate:

- **The numbers the article argues from:** pay by firm, a deal's size and timeline, a market statistic, a before and after.
- **Every block of a worked model** (model articles), plus one close-up with the formulas visible.
- **The mechanism the article spends the most words on:** the balance check, the cash conversion cycle, a waterfall, an issue tree.
- **Case exhibits** where a chart reads faster than the table.
- **Processes, funnels and calendars** (dated images; see below).
- **Sample pages with callouts** (resume PDFs).
- **The real thing, from outside sources, wherever the article names one.**

Don't illustrate: a short table that already reads at a glance, say/don't blocks, lists of firms, anything whose only content is the paragraph next to it.

## Images from outside sources

**1. Decide what the picture has to show.** One line: "Bloomberg's chart of 2026 M&A volume, because section 1 argues deal activity sets the bonus pool."

**2. Find it.** Search results are leads; the page the image lives on is where the credit comes from.

- **News outlets and data publishers:** Bloomberg, WSJ, FT, Reuters, CNBC, Business Insider, PitchBook, Statista. Credit: "Source: Bloomberg, {article title or topic}, {month year}."
- **SEC EDGAR** for filing pages. Credit: "Source: {Company} Form 10-K for fiscal {year}, SEC EDGAR."
- **The firm's own pages**, cropped to the part discussed. Credit: "Source: {firm}.com, {page title}, retrieved {date}."
- **US government sources:** FRED, BLS, Census, the Federal Reserve, the National Archives.
- **Wikimedia Commons** for people, buildings, historical documents. Pull author and license through the API: `https://commons.wikimedia.org/w/api.php?action=query&titles=File:{name}&prop=imageinfo&iiprop=url|extmetadata&format=json`. Credit: "Photo: {author} via Wikimedia Commons, {license}."
- **Unsplash, Pexels, company newsrooms and media kits** for photos of real places and objects.

Outside images keep their own text as published. The humanizer pass applies to our caption, alt text and source line only.

**3. What stays out:** watermarked stock-agency photos and anything with a visible watermark; AI-generated images; logos used as the image; photos of students or any private person.

**4. Download the real file, not a thumbnail.** Minimum 1,200 px on the long side; resize to at most 2,200 px wide with Pillow; strip EXIF and XMP on save. Cache under `scripts/images/sources/{slug}-{name}.{ext}`.

**5. Record it in the manifest:** `method: "web"`, `source`, `source_page`, `source_url`, `author`, `license`, `retrieved`, `modifications`.

**6. Check it before it goes in:** it shows the subject the sentence names, it's sharp at article width, no watermark, no private person, and the source line matches the manifest.

## The toolkit

`scripts/images/wsg_viz.py` (import with `sys.path.insert(0, "scripts/images")`):

- **Charts:** `new_figure()`, `style_axes(ax, title=..., value_axis=False)`, `bar_labels()`, `add_source(fig, text)`, `save_figure()`.
- **Tables as graphics:** `bank_table(header, rows, out_png, total_rows=(...), title=..., source=...)`.
- **Workbooks:** `new_workbook()`, `put()`, `header_bar()`, `set_widths()`, `year_header()`, the `FMT_*` formats.
- **Screenshots:** `render_range(xlsx, sheet, "B2:H30", out_png)`.
- **Checks:** `recalc_values(xlsx)`; assert against the article's tables before rendering.
- **Diagrams:** `scripts/images/wsg_diagrams.py` (boxes, arrows, trees, funnels, timelines).

## Workflow

1. **Read the article in full** and list candidate images with the exact line each one follows (its anchor). Plan a mix.
2. **Model articles: rebuild the model with live formulas**, run `recalc_values()` and compare cell by cell with every article table; exit non-zero on any mismatch.
3. **Render each model block** to one readable screenshot (12 to 40 rows, at most about eight columns), plus one formula close-up.
4. **Draw charts and tables in the banking format** from the article's numbers, never from memory, each with `add_source()`.
5. **Source the outside images** by the six steps above.
6. **Name and file.** PNG for anything built, JPEG allowed for photos, at most 2,200 px wide, `published/assets/images/{article-slug}/NN-short-name.{png|jpg}` in reading order. Workbook author "Wall Street Guide".
7. **Write the manifest** `published/assets/images/{slug}/manifest.json`: per image `file`, `alt`, `caption`, `source` (required), `method`, `anchor` (first 60 characters of the draft line the image follows), and for outside images the fields in step 5 above.
8. **Run the image-text passes** on every title, label, callout, caption, alt text and source line: plain language first (jargon spelled out, noun piles unstacked, one idea per caption), then the humanizer pass. Write the clean text back into the build script and manifest, and re-render.
9. **Insert into the draft** with `python3 scripts/images/insert_images.py {slug} drafts/draft-{slug}-v1.md` (`--dry-run` first). Never inside a list, table or quote, never in the intro.
10. **Build and check.** `python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"`; `markdown_to_wix_html.py` for Wix. Run `check_article.py` and `check_style.py` again.
11. **Look at every image** before delivery: black text, no gridlines or boxes on built charts, no clipped or colliding labels, a source line on every image, and every word on it reads plain and literal.
12. **Keep the build script idempotent:** `scripts/images/build_{slug}.py` rebuilds everything and writes the manifest in one run.

## Fixing images already built

When asked to fix AI-sounding or hard-to-read text in existing images: run the plain-language and humanizer passes on the strings in the build script and manifest, write them back, re-run `build_{slug}.py`, and re-insert with `insert_images.py`. List each changed string (old → new) in the batch log.

## Dated images

A recruiting calendar, a "today" marker or a screenshot of a firm's page goes stale. Mark projected windows "expected," put the retrieval date in the source line of any page screenshot, and list these images in the batch log under "regenerate at publish."

## Rules that never bend

- Every number in an image matches the article. Assert it; don't eyeball it.
- Every image has a source line in the article and a `source` in the manifest.
- Every string on or under an image passed the plain-language and humanizer passes: short, literal, professional, no unexplained jargon, no clever lines.
- Built charts and tables: black text, no gridlines, no boxes or cell borders.
- No em dashes, en dashes or Unicode minus signs anywhere: titles, labels, captions, alt text, manifests, source lines.
- An outside image shows the real subject of the passage beside it, is credited, and isn't on the stays-out list.
- Images never replace the explanation. The paragraph still walks every step.
- Wix upload: the PNG or JPEG, the manifest's alt text in the alt field, the caption and source line under the image.
