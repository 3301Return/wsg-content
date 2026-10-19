# Drafting instructions: October 11, 2026 IB batch (five articles)

You are drafting one WallStreetGuide.net (WSG) article. Work from the repo root `/home/claude/repo`. Today is Sunday, October 11, 2026. US spelling. Follow this file exactly; where anything here conflicts with an older file in the repo, the October 8 rules in `.claude-skill/SKILL.md` and this file win.

## 1. Read first, in this order (all of it, before writing a word)

1. `.claude-skill/SKILL.md` (the October 8 and October 7 rules at the top override everything below them)
2. `.claude-skill/source-verification.md`
3. `.claude-skill/reference-articles.md` (Stephen's good and bad openings; the voice to match)
4. `.claude-skill/intros.md`
5. `.claude-skill/plain-language.md`
6. `.claude-skill/thorough-explanations.md`
7. `.claude-skill/prose-editing.md` (rules 1 to 16 and the mechanical spot checks)
8. `style-guide/style-guide.md` (Writing DOS and DON'TS, post structure, the AI sniff test)
9. `style-guide/recruiting-timeline-glossary.md` (any article that mentions a recruiting year)
10. `style-guide/seo-checklist.md`
11. The template for your format: `templates/ultimate-guide.md` or `templates/listicle.md`
12. One Stephen-endorsed sample of your format for shape (never copy its voice if it predates October 8 rules on bylines): `samples/ultimate-guides/How to Beat the McKinsey Solve Game in 2026.md` or `samples/listicles/Top 10 Sophomore Insights Programs for IB.md`
13. The humanizer skill: `/root/.claude/skills/synced/37fa8fbb-96dc-473e-ae57-5dce92d68ec3_c2846f6b-18df-4d08-a8e7-8471d3775030/humanizer/SKILL.md`
14. Your article's section of the batch brief: `claude/batch-brief-oct-11-2026-ib.md`
15. Your fact sheet: `claude/research/{slug}.md`. Every number, date, quote and name in the article comes from here or from a page you fetched yourself and cite in your report.

Never use `drafts/` or `published/ai-written/` as voice samples. They are AI drafts.

## 2. Facts, names and links

- Every fact in the draft traces to the fact sheet or to a page you fetched in this session. If you need a fact that isn't there, fetch it (WebFetch or WebSearch) and record the URL in your report. If you can't verify it, leave it out. Never invent a number, a date, a program name, a person, a deal, a quote or a URL.
- Named entities: Tier 1 household names need no check. Anything else must be in the fact sheet (already verified) or verified by you now. Use the current program names the brief gives; never the legacy names it lists as unverified.
- Fact-sheet items marked UNVERIFIED or CONFLICT: use only with the conflict stated as a range or with a `[VERIFY: ...]` tag, never resolved by guessing. Don't use anything the fact sheet says not to use.
- Links: inline anchor-word hyperlinks only, never bare URLs, never a URL list. Link only evergreen pages (firm careers landing pages, help-center articles, named news articles, WSG posts). Never link rotating job postings (Greenhouse `gh_jid`, Workday posting IDs, iCIMS `/jobs/N/`, LinkedIn jobs, `evercore.tal.net` vacancy pages). Two to five internal links to live WSG posts from the list at the end of the brief, placed where they help.
- Tag moving facts inline: `[VERIFY: what to check]` after deadlines, pay, rates, program windows, "as of" claims, and any figure a reader could act on that may change by publication. Don't tag stable facts.

## 3. Structure (the docx builder and the checkers depend on this)

```
---
headline: "{exact headline from the brief}"
target_keyword: {keyword}
secondary_keywords: [{kw1}, {kw2}, ...]
format: {ultimate-guide | listicle}
word_count_target: 5000-6000
status: draft-v1
---

# {Headline}

**Meta description:** {topic first, what the article covers, 150 to 160 characters, keyword included, no author}.

{Intro per intros.md: one or two short paragraphs, two to five sentences total. At most three paragraphs before the first H2 or check_style fails.}

## {Sub-question 1, the reader's exact search phrasing, ends with ?}
{First sentence answers it. Two to four sentences.}

## {Sub-question 2?}
...

## {Body sections: numbered claim headings for insight articles ("1. A GPA above 3.5 is the first filter, so protect it from day one") or plain descriptive headers for period and explainer sections. Listicle: plain H2 group headers, then "### N. {the question}?" items, numbered 1 to 20 across the groups.}

## Say this, don't say that   (articles 3, 4 and 5; four or five triplets)
**{The question}**

Don't say: "..."

Say: "..."

## {Conclusion header, plain: "What to do this week" or similar}
```

- No `byline:` line. No author bio, credentials, memories or composite students anywhere. Light first person for framing only ("In this article, I lay out...", "the list I'd send a sophomore").
- Headers: plain and literal; numbered insight headings are short plain claims under 12 words; question headers are the reader's exact question and end with "?"; no clever colon halves, no metaphors.
- Bolds: full sentences carrying a fact or a clear rule, one or more per H2 section, never a fragment or a label. Reading only the bolds in order must tell the article's argument. Listicle items each carry a bolded lead claim and a bolded takeaway.
- Every section has a specific: a named firm, a real number or a named scenario.
- Technical machinery gets explained in plain words at first use and walked step by step, once, with one worked example using the numbers from the fact sheet. Variations get a sentence, not a second table.
- Markdown pipe tables are fine (they become Word tables). Blank line before and after every list and table.
- Lists: bullets for sequences or fields; prose for arguments.
- Never close with a recap. The last section gives the next step.
- Images are added later by another agent. Leave no image placeholders.

## 4. Banned in body copy (the checkers block some of these; all of them are rules)

- Em dashes, en dashes, spaced hyphens as pause punctuation, Unicode minus signs. Use periods, commas, colons, parentheses. Hyphens inside compound words ("one-page," "first-lien") are fine.
- Filler: "highly competitive," "in today's landscape," "many students find," "it's important to note," "in this guide we will," "at the end of the day," "needless to say," "that being said," "in conclusion," "as previously mentioned," "let's dive in," "the truth is," "here's the thing."
- AI register: "navigate," "landscape," "leverage" as a verb, "crucial," "game-changer," "not just X, it's Y," "X is not Y dressed up as Z," "best-kept secret," "more than people realize," adjective triplets, "the key takeaway," "ultimately," echo sentences that restate the paragraph.
- Negatives about the writer, WSG, the article or the reader. "Most candidates get this wrong" and any opinion about what readers get wrong without evidence in the next sentence.
- Narrative openings, scenes, stories, "picture this," drama words ("rattled," "a clock that never stops").
- Fake-precise effort counts ("sent 47 emails"). Round language for effort, real numbers for outcomes and facts.
- Definitions of the field ("investment banking is..."). The reader knows the field; explain the machinery.

## 5. Passes, in order, after the full first draft

1. Intro check against `intros.md`'s checklist.
2. Plain-language pass (three tests on every technical paragraph).
3. Thoroughness pass (find every jump or crushed passage; expand; pay for it by cutting bloat). Keep notes for the report.
4. Prose pass: rules 1 to 16 in `prose-editing.md`, including burstiness (one paragraph under 15 words and one over 100 in any five-paragraph stretch; sentence lengths from under 6 to over 30 words), the say-it-out-loud test on every sentence and header, and the length cut order in rule 16.
5. Humanizer pass per the humanizer SKILL.md (inflated significance, sales language, vague attribution, shallow "-ing" analysis, stock vocabulary, forced triads, false depth, filler, chatbot artifacts), without changing any fact.
6. SEO checklist (`style-guide/seo-checklist.md`): keyword in H1, meta, first 100 words, at least two H2s.
7. The gut check: first sentence answers the headline; a smart sophomore would use it; no other blog could have written it; every paragraph earns its place; it reads like Stephen's good set, not the bad set.

## 6. Gates (run from the repo root; fix and re-run until clean)

```
python3 scripts/check_article.py drafts/draft-{slug}-v1.md      # must PASS; read every warning
python3 scripts/check_style.py drafts/draft-{slug}-v1.md        # must exit 0; "TOO CHUNKY" warnings are acceptable on question-listicle items
python3 scripts/check_links.py drafts/draft-{slug}-v1.md        # every link live
grep -nP "—|–|−| - " drafts/draft-{slug}-v1.md                  # must return nothing in body copy
grep -nP "[\x{200B}\x{200C}\x{200D}\x{2060}\x{FEFF}\x{00AD}]" drafts/draft-{slug}-v1.md   # must return nothing
wc -w drafts/draft-{slug}-v1.md                                 # target 5,000 to 6,000 (article 3 may reach about 6,500)
```

Plus the mechanical spot checks in `prose-editing.md` (echo suspects, register words, negatives, unsupported opinions, bio grep, headers read alone, effort counts, the bold-only read-through).

Link failures: some domains refuse the workspace (mckinsey.com times out; some sites return 403 to python-requests). If WebFetch shows the page live, keep the link, note it in your report under "links to click-test at publish," and if `check_links.py` still fails on it, remove the link and keep the source named in the text so it can be restored at publish. A dead page gets removed.

Length: if `wc -w` lands over 6,000 (6,500 for article 3), cut in rule 16 order and say what was cut. If it lands under 4,500, look for skipped steps and one-line answers; never pad.

## 7. Writing the file

Write the draft with a bash heredoc (`cat > drafts/draft-{slug}-v1.md << 'MDEOF' ... MDEOF`) or the Write tool, then confirm with `wc -l` and `tail -5` before running gates. For edits after that, re-read the surrounding lines before each Edit and verify with grep afterward.

## 8. Report back (your final message; keep it under 700 words)

1. **Thoroughness Report** in the exact format from `thorough-explanations.md` (expanded, cut, still thin, plain-language rewrites, word count with the format target and pages at about 250 words a page, over target yes/no and why).
2. **Delivery summary** in the format from `source-verification.md` (word count, em-dashes, named entities verified, URLs verified live, VERIFY tags remaining, compliance PASS/FAIL).
3. **Facts fetched beyond the fact sheet:** fact, URL, date seen.
4. **Links to click-test at publish** (removed because the workspace couldn't reach them, with the page named).
5. **Image plan for the image agent:** five to six images, each as: file name idea, type (bar chart, table, timeline, diagram, sequence), the exact numbers or rows it shows (copied from the draft), the source line, and the anchor (the first 60 characters, verbatim, of the draft line the image should follow; never a line inside the intro, a list, a table or a quote).
6. **Dated content** that should be regenerated or re-checked at publish.
