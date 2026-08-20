# Wix Publishing Checklist

Use this for every article moving from `drafts/` (or `published/`) into Wix. Formatting strips silently during paste-in if you do not follow the steps in order.

## Before you start

- [ ] Draft is in `published/` or final `drafts/v{N}.md` form, not v1
- [ ] All `[VERIFY: ...]` tags have been resolved or removed
- [ ] SEO checker has been run: `python3 scripts/check_article.py drafts/{file}.md`
- [ ] Headline matches the content calendar exactly
- [ ] Internal links to existing WSG articles added where natural (1-3 is plenty)

## Convert the Markdown to HTML first

Wix's editor strips Markdown but accepts pasted HTML formatting reliably. Do not paste raw Markdown.

From the project root:

```
python3 scripts/markdown_to_wix_html.py published/{article}.md
```

This outputs `published/{article}.html`. Open it in a browser, select all (Cmd/Ctrl + A), copy, then paste into the Wix blog editor. Headings, bolded sentences, and inline links carry over.

(If the script does not exist yet — see `scripts/` folder — paste the Markdown into a free converter like dillinger.io, copy the rendered output from the right pane, and paste into Wix.)

## In the Wix editor

- [ ] Paste content into the body field (NOT the title field — Wix has a separate title field)
- [ ] Set the **title** field to the exact headline (no Markdown `#`)
- [ ] Set the **SEO title** to the same headline (often a separate field)
- [ ] Set the **meta description** to the 150-160 character line from the draft frontmatter
- [ ] Set the **URL slug** to the kebab-case slug (e.g., `top-10-sophomore-insights-programs-for-ib`)
- [ ] Add a featured image (1200 × 630 minimum for OG card)
- [ ] Add 2-4 category tags
- [ ] Set the **author byline** to match the writer

## Visual cleanup pass in Wix

After pasting:

- [ ] Confirm all H2s and H3s rendered as headings (not bolded body text)
- [ ] Confirm bolded full-sentence claims kept their bold styling
- [ ] Confirm every inline link is clickable (Wix sometimes strips link href on paste)
- [ ] Confirm no horizontal rule artifacts from frontmatter
- [ ] Scroll the article on mobile preview — paragraphs should be readable in short blocks, not walls of text

## SEO and metadata

- [ ] Target keyword appears in H1, in first 100 words, and in at least 2 H2s
- [ ] Meta description is exactly 150-160 characters
- [ ] OG image is set
- [ ] Canonical URL is set (usually auto, double-check on cross-posts)

## Final pre-publish check

- [ ] Read the first paragraph out loud. Does it sound like Nikson or a generic banker? If generic, revise before publishing.
- [ ] Confirm the article passes the 4-question gut check in `style-guide/seo-checklist.md`
- [ ] If the article is in a series, link to the previous and next articles in that series

## After publishing

- [ ] Move the source file from `drafts/` to `published/` and remove the `draft-` prefix
- [ ] Update the frontmatter `status:` field to `published`
- [ ] Add the live URL to the frontmatter as `live_url:`
- [ ] If the article uses scenarios that should be reusable, copy them into the appropriate `deep-dives/{topic}.md` file so future articles can pull from them

## Common Wix paste-in failures (watch for these)

| Problem | Fix |
|---|---|
| All bolded text becomes the same weight (no emphasis) | Re-paste from rendered HTML, not from Markdown |
| Links lose their `href` attributes | Manually re-add each link in Wix's link tool |
| H3 sections render as body text | Highlight, change to "Heading 3" in the Wix toolbar |
| Numbered list resets to 1 after each item | Use the Wix list button instead of pasted numbers |
| Smart quotes get replaced with straight quotes | Acceptable, Wix style preference |
