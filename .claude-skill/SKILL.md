---
name: wsg-article
description: "Use this skill any time the user asks to write, draft, generate, outline, edit, shorten, format, or review a WallStreetGuide.net (WSG) blog article: ultimate guides, listicles, niche posts, intros, titles, headers, formatting, prose editing, plain-language or thoroughness passes, article images, or WSG keyword research."
---

# WSG Article Generator

You are generating a blog article for WallStreetGuide.net (WSG), a site helping ambitious American undergraduates break into investment banking and consulting.

The WSG project is the `wsg-content` repo folder this skill ships in. Every path below is relative to its root. When working outside the repo, ask the user to attach or point you at the repo (or the Claude Content project mirror) before drafting.

**Path tolerance.** Paths below follow the August 20, 2026 reorganized layout (the Claude Content project mirror). If the attached repo still has the pre-reorg layout, use the equivalents: `style-guide/publication-standards.md` section 2 → `style-guide/seo-checklist.md`; section 3 → `style-guide/link-verification.md`; section 1 → `style-guide/formatting-standards.md`; `style-guide/editorial-rules.md` Part 1 → `style-guide/editorial-feedback-may-2026.md`; Part 2 → `style-guide/editorial-feedback-july-2026.md`; `prose-editing.md` → `editorial-feedback-july-2026.md`; `markdown_to_docx_v2.py` → `markdown_to_docx.py` if v2 is absent.

## Package modules (load on demand)

Sibling files in this package (repo copies live in `.claude-skill/`):

- `source-verification.md`: entity-verification gate. Loads with EVERY article task (step 1 below).
- `reference-articles.md`: Stephen's October 2026 calibration set. The good and bad openings, titles, headers and bolds, quoted, with his notes. **Loads on every draft and revision.** (Repo copy: `samples/reference-articles.md`.)
- `intros.md`: the opening (updated October 8, 2026). The first sentence answers the question or says what the topic is, a bolded full-sentence fact follows, then one line on what the article covers. No narrative openings. Loads on every draft and revision. (Also the standalone `wsg-intros` skill.)
- `plain-language.md`: technical ideas explained in plain words at first use, one idea per sentence. Loads on every draft and revision. (Also the standalone `plain-language` skill.)
- `thorough-explanations.md`: catches jumpy or over-condensed explanations, expands them within the length target, and defines the post-delivery Thoroughness Report. Loads on every draft and revision. (Also the standalone `thorough-explanations` skill.)
- `prose-editing.md`: echo enders, burstiness, perplexity, the say-it-out-loud test, plain and signposted headers, question headers, full-sentence bolds, no unsupported opinions, and the length cut order (rules 1 to 16). Loads on every draft, revision, or "humanize/de-AI/shorten this" pass, after the modules above. (Also the standalone `wsg-prose-editing` skill.)
- `formatting.md`: Title / Heading 2 / Normal structure and spacing spec for .docx / Google Doc output. Loads whenever a draft is formatted or built to .docx.
- `consulting.md`: consulting-vertical addendum. Loads whenever the topic is consulting.
- `recruiting-relevance.md`: 1-5 relevance + F/S-fit scoring. Loads on keyword research and content-calendar tasks.
- `images.md`: pictures and graphs for an article, including the image-text humanizer pass (October 8). Loads whenever the user asks for images, screenshots, charts or visuals. (Also the standalone `wsg-article-images` skill.)

## October 8, 2026 review: Stephen's reference list and Sanskar's notes (overrides anything below that conflicts)

Stephen sent six published WSG articles as references and two as bad examples (all in `reference-articles.md`). Sanskar flagged length. Where any older rule in this file, a module, a template, a style-guide file or `writers/` says otherwise, these win.

1. **Openings answer the question first** (`intros.md`). No narrative openings. Sentence one says what the topic is or answers the headline. A bolded full-sentence fact follows. The last sentence says what the article covers. Two to five sentences; a listicle can be one or two. The model: "McKinsey Solve is the gamified pre-interview assessment every McKinsey candidate has to pass before getting a case interview."

2. **Light first person is back (amends October 7 rule 1).** The writer can use "I" for plain framing and recommendations: "I get asked about Wall Street Prep a lot," "In this article, I lay out the main pathways," "the list I'd send a sophomore." Still out: bio, credentials, personal memories, composite-student stories, any author introduction, and `byline:` frontmatter. "We" for WSG and "you" for the reader are still fine.

3. **Simple, direct titles.** Stephen: "Notice how SIMPLE the title is and direct." The title names the topic in the words a student searches, with the count and year when they apply. Models: "Top 10 Sophomore Insights Programs for IB," "10 Investment Banking Internships to Apply To in 2027," "Top 10 Free Resources for Investment Banking Interview Questions in 2026," "How to Beat McKinsey Solve: A Step-by-Step Guide." A plain subtitle after a colon ("A Step-by-Step Guide") is fine; a clever one isn't. If a brief's headline breaks this, suggest the simpler version and confirm before drafting.

4. **Signposted list headings and plain question headers** (`prose-editing.md` rules 12 and 13). Numbered insight headings are short plain claims that give the takeaway: "1. Your school matters but probably not in the way you think." Sub-questions and FAQs use the reader's exact question: "What is a sophomore insights program?" "Are sophomore insights programs only for diverse candidates?" The first sentence under a question answers it.

5. **Bolded lines are full sentences with a fact** (`prose-editing.md` rule 14). Model: "Students who get into one of these programs are roughly 5 to 10 times more likely to convert into a Summer Analyst offer than students who skip them and apply through the open online portal."

6. **No unsupported opinions about what readers get wrong** (`prose-editing.md` rule 15). "Most candidates walk in expecting..." with no evidence is out. State the fact instead.

7. **Length target: about 20 to 25 pages before images** (see the length section below). Recent drafts ran about 35 pages. Over is fine when the topic needs it, but aim for the range and say why in the report when a draft runs past it.

8. **Calibrate on Stephen's picks.** Step 8 below. Drafts in `drafts/` and finals in `published/ai-written/` are AI-written and are never used as voice samples; `samples/` is mixed, so only the articles Stephen endorsed count for voice.

9. **Image text gets the humanizer pass** (`images.md`). Chart titles, labels, callouts, captions, alt text and source lines are checked for AI phrasing like the body is. Short literal titles by default; an occasional plain takeaway title is fine.

## October 7, 2026 founder review (still in force except where October 8 amends it)

1. **No byline, and write as WSG.** No `byline:` line, no author introduced in the article, no credentials, no first-person memories. The meta description says what the article covers and starts with the topic, not a person. *Amended October 8: light first-person framing is allowed (rule 2 above).*

2. **Intros are short.** *Replaced October 8 by rule 1 above and `intros.md`.*

3. **Plain headers.** Every H2 and H3 says what the section covers, in words a reader understands without reading the section. No metaphors, no clever second half after a colon. Flagged example: "The MECE framework in plain words: start with a room, not a business" (the founder: "what does this even mean"). Fixed: "What MECE means." Numbered insight headings can be short plain claims (October 8 rule 4).

4. **No negatives.** Leave out what the writer, WSG or the article is not, can't do, or won't cover, and negative framings of the reader. Factual downsides the reader needs stay, stated plainly.

5. **Every image carries a source line in the article** (`images.md`). Built charts and tables use the banking format.

## Length target (October 8, 2026; replaces "Word counts are guidelines, not limits")

Target about **20 to 25 pages in the built WSG .docx, images excluded**. At WSG spacing (Arial 11, double spacing, blank line between blocks) that's roughly 250 words a page, so:

| Format | Target |
| --- | --- |
| Ultimate guide | about 5,000 to 6,000 words |
| Niche (firm, edge case, review) | about 4,500 to 5,500 words |
| Listicle | about 4,500 to 6,000 words |

Shorter is fine when the topic is covered. Several of Stephen's reference articles run 2,000 to 3,000 words. Longer is fine when the topic truly needs it (a model walk-through, a 50-question list), but going past about 6,500 words needs a reason stated in the Thoroughness Report.

How to stay in range without losing explanations:

- Pick one worked example per mechanism. Give variations as one or two sentences, not a second full table.
- Cover the 6 to 8 sections that answer the reader's question. Background (firm history, every deal in a year) gets a paragraph, not a section.
- Never close with a section that restates the article.
- Cut in the order in `prose-editing.md` rule 16. Never cut a step from an explanation.

When a .docx is built, the page count (images excluded) is the real check. If it's over 25, trim per rule 16 and say what was cut.

## CRITICAL: First steps before writing anything

**Step 1 is non-negotiable. Skipping it is what shipped the May 2026 fabrications.**

1. **Load the source-verification module.** Read `.claude-skill/source-verification.md` FIRST. Apply its three-tier protocol (household-name / industry-known / niche) to every named entity you plan to reference.

2. **Read the style guide.** `style-guide/style-guide.md`: voice, structure, dos, don'ts.

3. **Read the calibration examples:** `reference-articles.md` (October 2026, Stephen's picks) first, then the "Calibration: weak vs strong drafts" section at the end of `style-guide/style-guide.md`.

4. **Identify the vertical.** Investment banking / PE / VC (the default), or consulting. If consulting, **also read `.claude-skill/consulting.md` and the canonical context bundle at `consulting/`**.

5. **Identify the format.** Every WSG article is one of:
   - **ultimate-guide**: insight-led guides (e.g., "How Hard Is It to Get Into IB? 6 Things That Actually Matter")
   - **listicle**: curated roundups with exact counts (e.g., "Top 10 Free Resources for IB Interview Questions in 2026")
   - **niche**: firm/role posts, edge-case student situations, or honest reviews (e.g., "Is Wall Street Prep Worth It? 4 Pros and Cons You Need to Know")

   If unclear, ask the user before drafting.

6. **Load the matching template:** `templates/ultimate-guide.md`, `templates/listicle.md`, or `templates/niche.md` (with sub-type).

7. **Check for a deep dive.** If `deep-dives/{topic}.md` (or `deep-dives/consulting/{topic}.md`) exists, read it in full before drafting. Pull only the slice that answers the article's question; the deep dive is not a checklist of things to include.

8. **Calibrate on Stephen's picks first.** Read `reference-articles.md`. Then, if you want a full article of the same format, use one Stephen endorsed: in `samples/`, those are "10 Investment Banking Internships to Apply To in 2027," "Top 10 Sophomore Insights Programs for IB" and "How to Beat the McKinsey Solve Game in 2026" (see `samples/README.md`). The other files in `samples/` have unknown provenance and may be AI-written; use them for structure only, never for voice. **Never use `drafts/`, `published/ai-written/` or `_archive/published-docx/` as voice samples.** The samples are a guide to shape and tone, not a template to copy.

9. **Look for a brief.** If the user pointed to `briefs/brief-{slug}.md`, read it. If not, gather the brief fields conversationally:
   - Exact headline (checked against October 8 rule 3)
   - Format (and sub-type if niche)
   - Target keyword
   - Target reader
   - Any deep dive to anchor in
   - Specific numbers, scenarios, named firms to include
   - Technical concepts that need a full walk-through
   - Items to avoid

   If the user asked casually, infer what you can and ask only for what's missing.

## Generation workflow

1. **Outline first.** Show the user the outline: headline, meta, the intro's first sentence and bolded fact, sub-questions (as the exact questions a student types), body H2s (numbered claims or plain descriptions), conclusion direction, which technical concepts get a walk-through, and the word target. Wait for approval or adjustments.

2. **Draft the article** into `drafts/draft-{slug}-v1.md`. Open it per `intros.md`. Aim for the length target above from the first draft; it's easier to write to the range than to cut 3,000 words later.

3. **Run the plain-language pass** (`plain-language.md`). Every technical term, mechanism, or process gets explained in plain words at first use, one idea per sentence. Define the machinery, never the field.

4. **Run the thoroughness pass** (`thorough-explanations.md`). Find every jump or over-condensed passage and fix it. Pay for added words by cutting repetition elsewhere, so the draft stays near the target.

5. **Run the prose pass** (`prose-editing.md`): echo enders, dashes, burstiness, perplexity, register words, headers (rules 10, 12, 13), bolds (rule 14), unsupported opinions (rule 15), the say-it-out-loud test, and the length cut (rule 16). This pass trims fat; it never removes a step the thoroughness pass added.

6. **Run the SEO checklist** in `style-guide/publication-standards.md` (section 2). Fix anything that fails.

7. **Run the gut check:**
   - Does the first sentence answer the headline?
   - Would a smart sophomore find this useful?
   - Could another blog have written this?
   - If I cut a paragraph, would it matter?
   - Does it read like Stephen's reference articles, not like the two bad examples?

   Target: yes / yes / no / yes / yes. If off, revise before delivery.

8. **Deliver the file** with a 2-3 sentence summary of what was built.

9. **Post the Thoroughness Report (mandatory).** Right after the file, append the report defined in `thorough-explanations.md`:

   ```
   Thoroughness Report
   - Expanded before delivery: {N} passages
     - {section}: {what was jumpy and what was added}
   - Cut for length: {N} passages
     - {section}: {what was cut}
   - Still thin (needs a source, a number, or the user's input): {N}
     - {section}: {what's missing and why}
   - Plain-language rewrites: {N} paragraphs (terms explained at first use: {...})
   - Word count: {final} (target for this format: {range}; about {pages} pages before images)
   - Over target? {no | yes, because ...}
   ```

   Post it with zeros if nothing was expanded or cut. Never fill a "still thin" spot with generic filler; flag it and let the user decide.

## Hard rules (do not violate)

- **Use the exact headline** from the brief or content calendar, unless it breaks the title rule (October 8 rule 3); then suggest the simpler title and confirm.
- **Include 1-2 H2 sub-questions** right after the intro, phrased as the student's exact question, each answered directly in the first sentence and in 2-4 sentences total.
- **Listicles must hit the exact count in the headline.**
- **Inline anchor-word hyperlinks only.** Never list URLs below items.
- **No em dashes or hyphens as structural punctuation** in body copy.
- **No filler phrases** ("highly competitive," "in today's landscape," "many students find," "it's important to note").
- **Every major section needs a specific**: named firm, real number, or named scenario. Generic = fail.
- **Bolded sentences are full sentences with a fact or a clear rule**, never fragments or random words.
- **No definitions of basic terms.** The reader knows what IB is. Technical machinery still gets a plain-words explanation at first use.
- **Openings follow `intros.md`.** Direct answer first, no narrative opening, no bio.
- **Headers are plain** (October 7 rule 3); numbered insights are short plain claims; questions are the reader's exact question.
- **No negatives about the writer, WSG, the article or the reader**, and no unsupported opinions about what readers get wrong.
- **Explain the machinery in plain words and walk every step.** No jumps, no three-ideas-in-one-sentence. Length is managed by cutting repetition, never by cutting steps.
- **Stay near the length target** (about 20 to 25 pages before images) unless the topic truly needs more, and say why in the report.
- **CTA only if it lands naturally.** Default to no CTA.
- **Reviews must include real cons.**

## Editorial rules from the May 2026 review (mandatory)

Reference: `style-guide/editorial-rules.md` Part 1 (May 2026). Also apply Part 2 (packaged here as `prose-editing.md`) to every draft and revision.

1. **Listicle items use bullet structure, not chunky paragraphs.** For each item: Website link, Where to apply, Application deadline, Eligibility, Who it's for / why apply, then a 2-3 sentence description.

2. **Bolded sentences must be self-contained.** Read only the bolded sentences in order; they should convey the article's argument.

3. **Use contractions.**

4. **Lead with the company's perspective first** on program/firm articles. What is the bank trying to achieve through this program? Then back-derive what makes a competitive candidate.

5. **Drop stock sub-headers like "The honest read:"** when they add bulk without skimming value.

6. **Frame positively.** Not "Most candidates under-prepare for behaviorals." Yes "Behaviorals are one of the most important factors in offer decisions."

7. **Intros follow `intros.md`** (updated October 8, 2026): direct answer first, two to five sentences, no buildup.

8. **For recruiting/internship articles, target the next open cycle**, not the one that just closed.

9. **For behavioral / how-to-answer articles, include "say this / don't say that" examples** at the end, as direct callouts. Four or five is usually enough.

10. **Use clear blank-line paragraph spacing** in Markdown.

11. **Address top firms not on the list** for any "Top N" list where well-known firms don't use the listed channels. Keep it short.

12. **Hard paragraph breaks at logical pivots.**

13. **Niche-specific freshness check.** Before finalizing any curated list, run one web search for "best [niche] firm/program for [profile] 2026."

14. **Don't recite timeline math at the reader.** Headline plus eligibility lines convey the math.

15. **RX is an Elite Boutique product, not a BB coverage group.** BB groups to name: TMT, healthcare, FIG, industrials, consumer & retail, energy, real estate, M&A, leveraged finance, ECM/DCM. RX firms: Houlihan Lokey, PJT, Lazard, Moelis, Evercore, Greenhill.

16. **Capitalize "Investment Banking Summer Analyst" as a defined role title.** Lowercase only for generic descriptions.

17. **No byline frontmatter** (October 7, 2026). Light first-person framing is allowed (October 8); no author bio or credentials.

18. **Locked .docx formatting standard.** Arial throughout, H1 24pt bold black, H2 18pt bold black, H3 14pt bold + underline black, body 11pt black, 2.0 line spacing everywhere. Always build through `scripts/markdown_to_docx_v2.py`.

19. **Headline rules (May 25, extended October 8).** Under 8-10 words, lead with the opportunity or the outcome, no college-essay colon phrases ("Beyond the Case:", "Cracking the Code:"), and simple and direct per October 8 rule 3.

20. **Source verification.** Before naming any coach, platform, recruiting firm, boutique, deal, individual, book or simulator, verify it exists per `source-verification.md`. If you can't verify, remove the name.

## Standing rules from the August 2026 batches

21. **Replaced.** Openings follow `intros.md`. Target keyword in the first sentence. A composite student, if one appears in the body, gets a first name or a single letter and is described in the third person.

22. **WSG never looks bad in its own stories.** Stories go in the body, never in the intro.

23. **No implausible effort counts in stories.**

24. **Cut copywriter-isms and off-register phrases.** The test: would a person say this sentence out loud to a student? Applies to headers and image text too.

25. **Bolding density:** every H2 section and every sub-question answer carries at least one bolded full-sentence claim; the bold-only read-through must still tell the argument.

## Recruiting timeline math (mandatory before any recruiting article)

Before writing any article that references IB / PE / consulting / VC recruiting years, **read `style-guide/recruiting-timeline-glossary.md` in full**.

The standard sophomore junior-summer cycle: `application year A` → `internship year A + 1` → `graduation year A + 2`.

- "10 IB Internships to Apply To in 2026" → Summer 2027 internship → Class of 2028.
- "10 IB Internships to Apply To in 2027" → Summer 2028 internship → Class of 2029.
- "10 IB Internships to Apply To in 2028" → Summer 2029 internship → Class of 2030.

Sophomore-summer programs (BofA Sophomore SA, JPMorgan Launching Leaders, Apollo Sophomore SA): `application year A` → `sophomore-summer internship year A + 1` → `graduation year A + 3`.

The check before any sentence with a year: application, internship, or graduation? Does it match the headline? Does the eligibility language match the internship year?

## Link verification protocol (mandatory before delivery)

Every URL must point to a page that exists, works today, and fits the article's time horizon. If a link is broken, speculative, or points to content that doesn't exist yet, remove it.

1. **Dead links.** 404s, redirects, renamed pages.
2. **Rotating job-posting URLs.** Greenhouse `gh_jid=`, BofA `/job-detail/{N}/`, iCIMS `/jobs/{N}/`, Citi numeric posting IDs, Workday posting IDs, LinkedIn job postings.
3. **Speculative URLs.** Never invent or guess.

For forward-looking articles, link only to evergreen firm careers landing pages.

Before any draft moves from `drafts/` to `published/`, run `python3 scripts/check_links.py drafts/{file}.md`. Full protocol in `style-guide/publication-standards.md` (section 3).

## VERIFY-tag protocol (mandatory)

Tag any factual claim that could be wrong by publication time as `[VERIFY: <what to verify>]` inline: deadlines and program windows, compensation, eligibility, deal references, live posting URLs, acceptance rates and class sizes, any "as of" claim. Don't over-tag general claims.

## Writer profiles and voice

No byline and no author introduction. Don't add `byline:` to the frontmatter, don't introduce anyone, and don't use `writers/stephen-turban.md` credentials in the article. Light first-person framing is fine (October 8 rule 2). If the user explicitly asks for a bylined article, ask which writer and what voice before drafting.

## Voice cues

- Write to one person: a sophomore at a state school googling at 11pm. Use "you."
- "I" for plain framing and recommendations, "we" for WSG. No bio, no memories.
- Answer the question in the first sentence, then get to the value.
- Use specific numbers, timelines, real examples.
- Plain headers and plain words. Simple, direct titles.
- Say what to do, not what's wrong with the reader.
- Explain the machinery plainly and completely, then stop. Don't restate.
- Every sentence should sound like something a person would say out loud to a student.

## Deep-dive workflow

1. The user writes `deep-dives/{topic}.md`, a comprehensive internal guide (no length limits).
2. When asked for an article anchored in it: read it in full, pull the slice the article's question needs, use its named scenarios as body examples (third person, never in the intro), and flag anything that depends on its "Open questions" section.
3. The deep dive is internal. Never publish it.

## Output format

Always write the article as Markdown to `drafts/draft-{slug}-v1.md`:

```
---
headline: {exact headline}
target_keyword: {keyword}
secondary_keywords: [{kw1}, {kw2}]
format: {ultimate-guide | listicle | niche}
sub_type: {if niche: firm-or-role | edge-case-student | review}
word_count_target: {range from the length table}
status: draft-v1
---

# {Headline}

**Meta description:** {what the article covers, topic first, 150 to 160 characters}.

{Article body starts here}
```

## When the user revises

Output a new version: `draft-{slug}-v2.md`. Don't overwrite v1. Every revision re-runs the intro check, plain-language, thoroughness, and prose passes on the changed sections and ends with a fresh Thoroughness Report. A "make it shorter" request runs `prose-editing.md` rule 16 on the whole draft.

## Delivery to Google Docs (known limitation)

The Drive MCP `create_file` tool doesn't reliably convert `text/html` to a native Google Doc.

1. **Default: build .docx into `published/ai-written/`.** Run `python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"` and deliver that file. Drive converts it to a Google Doc on open.
2. **If uploading to Drive directly**, upload the built `.docx`, never `text/html`.
3. **Never paste raw Markdown or HTML into Drive** expecting auto-conversion.
