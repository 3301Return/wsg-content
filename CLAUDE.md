# WSG Article Generator: Project Instructions

This project generates SEO-optimized blog articles for **WallStreetGuide.net (WSG)**, a site helping ambitious American undergrads break into investment banking and consulting.

When the user asks you to write, draft, or generate any WSG content (articles, blog posts, listicles, ultimate guides, niche posts), **immediately load `.claude-skill/SKILL.md`** and follow that workflow exactly.

## Quick orientation (so you know where things live)

- `style-guide/style-guide.md`: voice, dos, don'ts, post structure, AI sniff test. **Read before drafting anything.**
- `samples/reference-articles.md`: **Stephen's October 2026 calibration set** (six good published articles, two bad ones, his notes). Read on every draft. Packaged as `.claude-skill/reference-articles.md`.
- `style-guide/weak-vs-strong-examples.md`: older calibration examples
- `style-guide/seo-checklist.md`: run before delivering any draft
- `templates/`: `ultimate-guide.md`, `listicle.md`, `niche.md`, `deep-dive.md`, `_brief-template.md`
- `samples/`: curated articles by format. Mixed provenance; only the three Stephen endorsed (see `samples/README.md`) count as voice samples.
- `writers/`: contributor profiles (retired for drafting: no byline, no author bio in articles)
- `briefs/`: one brief per article in progress
- `drafts/`: working drafts (`draft-{slug}-v1.md`, v2, etc.). **AI-written; never used as voice samples.**
- `published/`: `ai-written/` and `human-written/`. Only `human-written/` is a voice sample.
- `deep-dives/`: internal long-form guides that spawn multiple articles. See `deep-dives/INDEX.md`. Consulting deep dives live in `deep-dives/consulting/`.
- `consulting/`: canonical consulting context bundle. **Required reading whenever the article topic is consulting.**
- `content-calendar/`: keyword + headline plan. Run `python3 scripts/parse_calendar.py` to refresh `calendar.md`.
- `scripts/`: `check_article.py` (compliance gate), `check_style.py` (prose-level style guard), `check_links.py` (link verifier), `markdown_to_docx_v2.py` (current .docx builder), `markdown_to_wix_html.py` (publishing prep), `parse_calendar.py`, `sync_samples.py`, `verified-brands.txt`
- `.claude-skill/SKILL.md`: full skill definition (October 8 and October 7 rules at the top, then workflow, hard rules, VERIFY protocol)
- `.claude-skill/consulting.md`: consulting-vertical addendum. Loads ALONGSIDE the main skill whenever the topic is consulting.
- `.claude-skill/source-verification.md`: three-tier entity-verification protocol. **Loads ALONGSIDE every article task.**
- `.claude-skill/intros.md`: the opening (October 8, 2026): answer the question in sentence one, a bolded full-sentence fact, one line on what the article covers. No narrative openings, no bio. **Loads on every draft and revision.**
- `.claude-skill/plain-language.md`: technical ideas in plain words at first use. **Loads on every draft and revision.**
- `.claude-skill/thorough-explanations.md`: catches jumpy explanations, expands them within the length target, defines the Thoroughness Report. **Loads on every draft and revision.**
- `.claude-skill/prose-editing.md`: prose rules 1 to 16 (echo enders, say-it-out-loud test, plain and signposted headers, question headers, full-sentence bolds, no unsupported opinions, length cut). Loads on every draft and revision after the modules above.
- `.claude-skill/formatting.md`: Title / Heading 2 / Normal structure and spacing spec for .docx output.
- `.claude-skill/images.md`: pictures and graphs (banking-format charts, model screenshots, diagrams, credited outside images, source lines), plus the October 8 image-text humanizer pass.
- `.claude-skill/recruiting-relevance.md`: 1-5 recruiting-relevance score for keyword research and content-calendar planning.
- `skills/`: the account skills as `.skill` zips. `wsg-article.skill` is a zip of `.claude-skill/`; after editing any module, rebuild it and re-save to your Claude account. The standalone `wsg-intros`, `plain-language`, `thorough-explanations`, `wsg-prose-editing`, `wsg-article-formatting` and `wsg-article-images` packages carry the same content for use outside the repo; `humanizer`, `clean-user-facing-text` and `remove-ai-marks` are the cleanup skills.
- `claude/`: correction, batch and change logs.

## The three article formats

1. **Ultimate guide**: insight-led guide. About 5,000 to 6,000 words. 6-8 sections; numbered insights use short plain claim headings.
2. **Listicle**: curated roundup. About 4,500 to 6,000 words. Exact count from headline.
3. **Niche**: firm/role, edge-case student, or honest review. About 4,500 to 5,500 words. Pulls from a deep dive when one exists.

**Length target (October 8, 2026):** about 20 to 25 pages in the built .docx before images (roughly 250 words a page at WSG spacing). Recent drafts ran about 35 pages. Shorter is fine; longer only when the topic truly needs it, with the reason in the Thoroughness Report. Cut repetition and side material, never explanation steps.

## Hard rules (always enforce)

- Use the exact headline from the brief or content calendar, unless it breaks the simple-title rule; then suggest the simpler title and confirm
- **Simple, direct titles (October 8):** the count, the topic in search words, the year if it applies. "Top 10 Sophomore Insights Programs for IB."
- **Openings follow `.claude-skill/intros.md` (October 8):** sentence one says what the topic is or answers the headline; a bolded full-sentence fact follows; the last sentence says what the article covers. No narrative openings, no opinions about what readers get wrong.
- 1-2 H2 sub-questions right after the intro, phrased as the student's exact search question, answered in the first sentence
- Listicle counts must match the headline exactly
- Inline anchor-word hyperlinks (never URL footers)
- No em dashes or hyphens as structural punctuation in body copy
- Every section needs a specific (named firm, real number, or named scenario)
- **Voice:** "you" for the reader, "we" for WSG, light first-person framing allowed ("In this article, I lay out..."). No byline, no bio, no credentials, no personal memories or composite-student stories in the intro.
- Plain, literal headers; numbered insight headings are short plain claims ("1. Your school matters but probably not in the way you think")
- No negatives about the writer, WSG, the article or the reader
- Bolded sentences are full sentences with a fact, and reading only the bolds conveys the argument
- Every image carries a source line, built charts use the banking format, and **all image text goes through the humanizer pass** in `images.md`
- No filler phrases, no basic definitions. (Basic = the field. Technical machinery still gets a plain-words explanation at first use.)
- **Explain the machinery in plain words and walk every step, once.** One worked example per mechanism.
- CTA only if it lands naturally; default to no CTA
- **Calibrate on Stephen's picks** (`samples/reference-articles.md` and the three endorsed samples). Never on `drafts/` or `published/ai-written/`.
- **For any article referencing recruiting years, read `style-guide/recruiting-timeline-glossary.md` first.** Standard sophomore cycle: apply year `A` → intern Summer `A+1` → graduate Spring `A+2`.
- **Run `python3 scripts/check_style.py drafts/{file}.md` before docx build.**
- **Verify every link before delivery** with `python3 scripts/check_links.py drafts/{file}.md`. Never link to rotating job-posting URLs. Better no link than a wrong one.
- **Tag every time-sensitive claim with `[VERIFY: <what to verify>]` inline.**
- **Listicle items use bullet structure** (Website, Apply Link, Deadline, Eligibility, Who/Why) + short description.
- **Use contractions.**
- **For recruiting articles, target the next open cycle.**
- **For how-to-answer articles, include "say this / don't say that" callouts** at the end (four or five).
- **For "Top N" lists, address the top firms NOT on the list** in a short section.
- **Hard paragraph breaks at logical pivots within sections.**
- **Run a niche-specific freshness check before finalizing a curated list.**
- **Don't recite timeline math at the reader.**
- **RX is an Elite Boutique product, not a BB coverage group.**
- **Capitalize "Investment Banking Summer Analyst"** as a defined role title.
- **Locked .docx formatting standard.** Arial throughout. H1 24pt bold black. H2 18pt bold black. H3 14pt bold underline black. Body 11pt black. 2.0 line spacing. Build via `python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"`.
- **Consulting articles auto-load the consulting addendum** (`.claude-skill/consulting.md` plus the relevant `consulting/` files).
- **Headlines are tight and value-led.** Under 8-10 words, no college-essay colon phrases.
- **NEVER fabricate a named entity.** `.claude-skill/source-verification.md` is the source of truth.

## Workflow when asked to write

1. Read `.claude-skill/SKILL.md`
2. Read `style-guide/style-guide.md` and `samples/reference-articles.md`
3. **Check the vertical.** If consulting, also read `.claude-skill/consulting.md` and the relevant `consulting/` files.
4. Identify format (ask if unclear)
5. Load matching template from `templates/`
6. Check `deep-dives/` for relevant source material
7. Read one of Stephen's endorsed samples of the same format if one exists
8. Outline first (including the intro's first sentence and the word target), get approval
9. Draft to `drafts/draft-{slug}-v1.md`, opening per `.claude-skill/intros.md`. Tag every time-sensitive claim with `[VERIFY: ...]`.
10. Run the plain-language pass, then the thoroughness pass, then the prose pass (including the length cut)
11. Run `python3 scripts/check_article.py drafts/{file}.md`
12. Run the SEO checklist and the gut check
13. Build the .docx with `python3 scripts/markdown_to_docx_v2.py`
14. Deliver, followed by the Thoroughness Report (with word count, target and pages)

## Important limitation

This skill auto-loads only when Claude is working inside this project folder. Outside it, point Claude at `.claude-skill/SKILL.md` or include the folder context in your first message.
