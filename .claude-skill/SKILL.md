---
name: "wsg-article"
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
- `thorough-explanations.md`: makes sure the core (what the reader came to learn how to do) is explained deeply from researched how-to material, keeps background short, and defines the post-delivery Thoroughness Report. Loads on every draft and revision. (Also the standalone `thorough-explanations` skill.)
- `prose-editing.md`: echo enders, burstiness, perplexity, the say-it-out-loud test, plain and signposted headers, question headers, full-sentence bolds, no unsupported opinions, the length cut order, staying in the article's own field, no trivia, no firm-side why, the section verdict, no absolutes, saying each point once, reader level, and proportion (rules 1 to 24). Loads on every draft, revision, or "humanize/de-AI/shorten this" pass, after the modules above. (Also the standalone `wsg-prose-editing` skill.)
- `formatting.md`: Title / Heading 2 / Normal structure and spacing spec for .docx / Google Doc output. Loads whenever a draft is formatted or built to .docx.
- `consulting.md`: consulting-vertical addendum. Loads whenever the topic is consulting.
- `recruiting-relevance.md`: 1-5 relevance + F/S-fit scoring. Loads on keyword research and content-calendar tasks.
- `images.md`: pictures and graphs for an article, including the image-text humanizer pass (October 8). Loads whenever the user asks for images, screenshots, charts or visuals. (Also the standalone `wsg-article-images` skill.)

## October 14, 2026 review: decide what the reader needs before writing (overrides anything below that conflicts)

The founder reviewed the STAR method and Accenture Strategy drafts. Good research, but: too much overexplanation ("we've spent so much time explaining how banks score interviews, the research behind structured interviews... does a student really need all of that to learn how to give a better STAR answer?"), material that isn't relevant to the reader (Managing Director salaries in an entry-level Analyst guide; several pages on one practice case in a career guide), repetition (eight sample answers, an explanation after each, a 19-question mapping table and a say/don't section, all making the same points), and a tone that's "a little AI-y and absolute," like "a Nat Geo narrator." His summary: **"the model needs to make better editorial decisions before writing and have more quality controls in place... I'd rather have a focused article that properly answers the question than a very comprehensive one where the important information gets buried."**

1. **Write an editorial plan before drafting** (the plan is in the Generation workflow below). It names the reader and the one question they came with, gives the answer in three sentences, sorts every candidate topic into *explain fully / two lines / cut*, gives every section one distinct purpose, and sets a length budget. The draft follows the plan. The plan goes in the delivery report so the founder can see the editorial calls.

2. **Go deep on the core, short on the system.** Every article has a core: the thing the reader came to learn how to do (answer this question, build a strong resume, structure a STAR answer). Explain the core fully: what it's asking for, the steps, what each step means, how to do it well, a worked example with what each part is doing. Background (the history of resumes, how banks score interviews, research on structured interviews, why firms use a method) gets two lines at most, often none. Drafts fail both ways, too thin on the core and too long on the background; `thorough-explanations.md` catches both.

3. **Match the reader's level.** An entry-level article covers the entry-level seat in detail and everything above it in a line (one row or one sentence for the senior ladder, not a full pay table to Managing Director).

4. **Keep supporting examples in proportion.** In a career or role guide, a worked case or sample answer illustrates; it isn't the article. About a page, not several. Interview-prep articles can go deeper on the answer itself.

5. **Say each point once, in the best format for it.** If sample answers show the point, don't also explain it after every answer, map it in a table and repeat it in a say/don't block. Pick the format that teaches it fastest. Say/don't blocks are optional now, not a default; use one only when it adds something the article hasn't shown.

6. **One purpose per section.** If two sections make essentially the same point, merge them.

7. **Conversational, not absolute.** Real recruiting varies by firm, office, team and year. Write the way a person who knows the field talks: "usually," "often," "most firms," "some banks," "in our experience," where that's true. Cut sweeping certainty ("five stories cover every behavioral question," "the interviewer is scoring X," "this is what the firm wants") and narrator lines that sound like a documentary voiceover. Bolded sentences can and should carry these qualifiers.

8. **Research how to do the core well, and use that as the explanation.** Before drafting, research how strong sources teach the core task (career-office guides, firms' candidate pages, established prep sites, practitioners) and reuse what they agree on, in WSG's plain words and credited where a source is named, as the article's explanations. Research about the system (history, scoring, studies) is for getting facts right and stays in the notes. A fact earns its place by changing what the student does or decides.

9. **Length follows the question** (see the length section). Shorter, focused pieces land around 2,500 to 3,500 words; in-depth guides can run to 20 to 25 pages. There's no minimum to hit.

10. **A separate quality review checks the draft against the plan** before delivery (workflow step 9). It reads as the student and cuts.

## October 12, 2026 review: use judgment, stay on topic (overrides anything below that conflicts)

The founder and Sanskar reviewed the consulting resume draft and the October 11 batch. Founder: "the process just seems like it's following instructions too much without using its own intelligence, like it's starting off the consulting skeleton by spending a lot of time talking about similarities/difference between banking resumes." Full rules in `prose-editing.md` rules 17 to 20 (if the packaged module predates October 12, the four rules below are the complete version).

1. **Stay in the article's own field** (rule 17). A consulting article explains consulting. Don't explain it by contrast with banking ("unlike banking," "a banker would," "students treat a consulting resume as a banking resume with the order changed"). A comparison appears only when the reader is choosing between the two (pay, hours, "X vs Y"), once, in its own short section or sub-question. Sanskar: "a bug in the system where a lot of consulting banking becomes interlinked... deflecting the point into banking resume opposed to explaining what is actually the issue."

2. **No history or trivia the reader can't act on** (rule 18). Founding dates, reorganizations, who coined a term and when, famous-person anecdotes ("the earliest known resume is a letter Leonardo da Vinci wrote in 1482"), firm revenue and headcount in a junior-role article. If deleting the sentence changes nothing the student does, delete it. A one-clause attribution is fine; a biography isn't.

3. **Say what to do, not why the firm does it** (rule 19). No "start on the firm's side of the table," no "the screen exists to," no "the firm is trying to," no application-volume statistics used to justify a process. Sanskar: "the student doesn't need the 'why' behind resume screenings." A "why" survives only as one clause attached to an instruction it changes ("Put GPA on its own line, because the screener checks it first").

4. **Templates and briefs are options, not a checklist** (rule 20). Before delivery, give every H2 a verdict (keep, cut, shrink, rewrite) against one question: does a student reading this headline need this section to do what the headline promises? Background sections, "how this differs from X" sections, tables that repeat prose and recap closers fail it. Shorter is fine; don't pad to the length target.

Mechanical checks for these (run with the prose-editing spot checks): in a consulting article `grep -inE "bank|banker|goldman|jpmorgan|wall street"` (every hit sits in the one comparison section, or goes); `grep -inE "history|historically|founded|in 1[0-9]{3}|earliest|first (woman|female|known)|renamed|reorganiz"`; `grep -inE "firm's side|side of the table|exists to|is trying to|the reason (firms|the firm)|receives (roughly |about )?[0-9]"`.

## October 8, 2026 review: Stephen's reference list and Sanskar's notes (overrides anything below that conflicts)

Stephen sent six published WSG articles as references and two as bad examples (all in `reference-articles.md`). Sanskar flagged length. Where any older rule in this file, a module, a template, a style-guide file or `writers/` says otherwise, these win.

1. **Openings answer the question first** (`intros.md`). No narrative openings. Sentence one says what the topic is or answers the headline. A bolded full-sentence fact follows. The last sentence says what the article covers. Two to five sentences; a listicle can be one or two. The model: "McKinsey Solve is the gamified pre-interview assessment every McKinsey candidate has to pass before getting a case interview."

2. **Light first person is back (amends October 7 rule 1).** The writer can use "I" for plain framing and recommendations: "I get asked about Wall Street Prep a lot," "In this article, I lay out the main pathways," "the list I'd send a sophomore." Still out: bio, credentials, personal memories, composite-student stories, any author introduction, and `byline:` frontmatter. "We" for WSG and "you" for the reader are still fine.

3. **Simple, direct titles.** Stephen: "Notice how SIMPLE the title is and direct." The title names the topic in the words a student searches, with the count and year when they apply. Models: "Top 10 Sophomore Insights Programs for IB," "10 Investment Banking Internships to Apply To in 2027," "Top 10 Free Resources for Investment Banking Interview Questions in 2026," "How to Beat McKinsey Solve: A Step-by-Step Guide." A plain subtitle after a colon ("A Step-by-Step Guide") is fine; a clever one isn't. If a brief's headline breaks this, suggest the simpler version and confirm before drafting.

4. **Signposted list headings and plain question headers** (`prose-editing.md` rules 12 and 13). Numbered insight headings are short plain claims that give the takeaway: "1. Your school matters but probably not in the way you think." Sub-questions and FAQs use the reader's exact question: "What is a sophomore insights program?" "Are sophomore insights programs only for diverse candidates?" The first sentence under a question answers it.

5. **Bolded lines are full sentences with a fact** (`prose-editing.md` rule 14). *October 14: bold the one thing worth remembering where there is one, with qualifiers where the fact varies; don't manufacture a bold for every section.* Model: "Students who get into one of these programs are roughly 5 to 10 times more likely to convert into a Summer Analyst offer than students who skip them and apply through the open online portal."

6. **No unsupported opinions about what readers get wrong** (`prose-editing.md` rule 15). "Most candidates walk in expecting..." with no evidence is out. State the fact instead.

7. **Length** (*replaced October 14*: length follows the question; see the length section below).

8. **Calibrate on Stephen's picks.** Step 8 below. Drafts in `drafts/` and finals in `published/ai-written/` are AI-written and are never used as voice samples; `samples/` is mixed, so only the articles Stephen endorsed count for voice.

9. **Image text gets the humanizer pass** (`images.md`). Chart titles, labels, callouts, captions, alt text and source lines are checked for AI phrasing like the body is. Short literal titles by default; an occasional plain takeaway title is fine.

## October 7, 2026 founder review (still in force except where October 8 amends it)

1. **No byline, and write as WSG.** No `byline:` line, no author introduced in the article, no credentials, no first-person memories. The meta description says what the article covers and starts with the topic, not a person. *Amended October 8: light first-person framing is allowed (rule 2 above).*

2. **Intros are short.** *Replaced October 8 by rule 1 above and `intros.md`.*

3. **Plain headers.** Every H2 and H3 says what the section covers, in words a reader understands without reading the section. No metaphors, no clever second half after a colon. Flagged example: "The MECE framework in plain words: start with a room, not a business" (the founder: "what does this even mean"). Fixed: "What MECE means." Numbered insight headings can be short plain claims (October 8 rule 4).

4. **No negatives.** Leave out what the writer, WSG or the article is not, can't do, or won't cover, and negative framings of the reader. Factual downsides the reader needs stay, stated plainly.

5. **Every image carries a source line in the article** (`images.md`). Built charts and tables use the banking format.

## Length (October 14, 2026; replaces the October 8 20-to-25-page target)

Length follows the question. The editorial plan sets a budget before drafting, and the draft stops when the question is answered. There's no minimum.

| Article type | Typical range |
| --- | --- |
| Focused piece (one question: a method, a firm's role, a test, a salary, a single process) | about 2,500 to 3,500 words |
| In-depth guide (a full process with several stages, a model walk-through, a long numbered list) | up to about 5,000 to 6,000 words (20 to 25 pages in the built .docx) |

Stephen's reference articles run 1,700 to 3,000 words. Most WSG articles are focused pieces. Going over about 6,000 words needs a reason in the report.

How to stay focused:

- Explain fully only what the plan puts in "explain fully." Everything else gets two lines or goes.
- One worked example per mechanism, sized to the article: about a page in a career guide.
- Say each point once (October 14 rule 5). No closing recap.
- Cut in the order in `prose-editing.md` rule 16.

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

1. **Write the editorial plan** (October 14, 2026), before any drafting, after research. Save it at the top of the report and keep it to one screen:

   ```
   Editorial plan
   - Reader: {who is searching this, at what stage, e.g. "a sophomore with a first HireVue in three weeks"}
   - Their question: {the one thing they came for, in their words}
   - The answer in three sentences: {what the article will tell them}
   - The core (what the reader came to learn how to do): {one line}
   - Explain fully (the core's steps and what each means, researched from how good sources teach it): {2 to 5 items, each with the sources the explanation will draw on}
   - Two lines each (context they need, not a lesson; background on the system goes here or in Cut): {items}
   - Cut (true and researched, but not for this reader): {items, with a few words on why}
   - Sections: {H2 → its one purpose; no two sections share a purpose}
   - Formats: {for each key point, the ONE format that teaches it: example, table, list or prose}
   - Length: {focused 2,500 to 3,500 | in-depth up to 6,000}, with a rough word budget per section
   ```

   Ask for each candidate topic: does the reader need this to do what the headline promises? Would they miss it if it were gone? Is it at their level? Then outline from the plan. The founder sees the plan in the report and doesn't need to approve it first unless they ask to.

2. **Draft the article** into `drafts/draft-{slug}-v1.md`, following the plan's sections and budget. Open it per `intros.md`. Write conversationally and hedge where things vary (October 14 rule 7).

3. **Run the plain-language pass** (`plain-language.md`). Every technical term, mechanism, or process gets explained in plain words at first use, one idea per sentence. Define the machinery, never the field.

4. **Run the thoroughness pass** (`thorough-explanations.md`) both ways: add depth wherever the core is thin (steps, what each means, how to do it well, what each part of an example does), and cut background that grew past two lines.

5. **Run the section verdict** (`prose-editing.md` rule 20). For every H2: keep, cut, shrink or rewrite, with one reason. Cut cross-field comparisons, history and trivia, and firm-side "why" setups (rules 17 to 19) before anything else. Use judgment; the template's section list is a menu.

6. **Run the prose pass** (`prose-editing.md`): echo enders, dashes, burstiness, perplexity, register words, headers (rules 10, 12, 13), bolds (rule 14), unsupported opinions (rule 15), the say-it-out-loud test, and the length cut (rule 16). This pass trims fat; it never removes a step the thoroughness pass added.

7. **Run the SEO checklist** in `style-guide/publication-standards.md` (section 2). Fix anything that fails.

8. **Run the gut check:**
   - Does the first sentence answer the headline?
   - Would a smart sophomore find this useful?
   - Could another blog have written this?
   - If I cut a paragraph, would it matter?
   - Does it read like Stephen's reference articles, not like the two bad examples?
   - Is every section about this article's subject, with no detour into another field, history, or the firm's reasons?
   - Could the article be a third shorter without losing anything the reader needs?

   Target: yes / yes / no / yes / yes / yes / no. If off, revise before delivery.

9. **Run the quality review** (October 14, 2026). A separate pass (a fresh agent when one is available) that hasn't seen the drafting reads the draft as the reader in the plan and answers, with a cut list:
   - Can the reader find the answer to their question on the first screen?
   - Is the core explained deeply enough that the reader could do it themselves: steps, what each means, a worked example? (add depth where thin)
   - Which passages explain how the system works when the reader only needed what to do? (cut or two lines)
   - What's above or beside the reader's level? (one line or cut)
   - Which points are made twice, in two formats or two sections? (keep the better one)
   - Which sentences are absolute or narrator-voiced where real practice varies? (hedge or cut)
   - Is any example out of proportion to its role? (trim)
   - Does every section match the plan's purpose for it?
   Apply the cuts, then rerun the gates.

10. **Deliver the file** with a 2-3 sentence summary, the editorial plan, and the quality review's main cuts.

11. **Post the Thoroughness Report (mandatory).** Right after the file, append the report defined in `thorough-explanations.md`:

   ```
   Thoroughness Report
   - Core depth added: {N} passages
     - {section}: {what was thin and what was added, and its source}
   - Off-core passages cut or shortened: {N}
     - {section}: {what was cut back}
   - Cut for length: {N} passages
     - {section}: {what was cut}
   - Still thin (needs a source, a number, or the user's input): {N}
     - {section}: {what's missing and why}
   - Plain-language rewrites: {N} paragraphs (terms explained at first use: {...})
   - Word count: {final} (plan budget: {focused or in-depth, range}; about {pages} pages before images)
   - Over budget? {no | yes, because ...}
   ```

   Post it with zeros if nothing was expanded or cut. Never fill a "still thin" spot with generic filler; flag it and let the user decide.

## Hard rules (do not violate)

- **Use the exact headline** from the brief or content calendar, unless it breaks the title rule (October 8 rule 3); then suggest the simpler title and confirm.
- **Include 1-2 H2 sub-questions** right after the intro, phrased as the student's exact question, each answered directly in the first sentence and in 2-4 sentences total.
- **Listicles must hit the exact count in the headline.**
- **Inline anchor-word hyperlinks only.** Never list URLs below items.
- **No em dashes or hyphens as structural punctuation** in body copy.
- **No filler phrases** ("highly competitive," "in today's landscape," "many students find," "it's important to note").
- **Be specific where it helps the reader**: a named firm, a real number or a concrete example beats a generic line. Don't add a specific to a section just to have one.
- **Bolded sentences are full sentences with a fact or a clear rule**, never fragments or random words.
- **No definitions of basic terms.** The reader knows what IB is. Technical machinery still gets a plain-words explanation at first use.
- **Openings follow `intros.md`.** Direct answer first, no narrative opening, no bio.
- **Headers are plain** (October 7 rule 3); numbered insights are short plain claims; questions are the reader's exact question.
- **No negatives about the writer, WSG, the article or the reader**, and no unsupported opinions about what readers get wrong.
- **Explain the core fully, in plain words, every step, from researched how-to material; give background two lines or none** (October 14). No thin how-to, no lessons on how the system works.
- **Length follows the question** (October 14): focused pieces about 2,500 to 3,500 words, in-depth guides up to about 6,000. Write the editorial plan first; run the quality review before delivery.
- **Say each point once; match the reader's level; hedge where practice varies** (October 14 rules 3, 5 and 7).
- **CTA only if it lands naturally.** Default to no CTA.
- **Reviews must include real cons.**
- **Stay in the article's field; no trivia; no firm-side why; judge every section** (October 12, rules 17 to 20). One short comparison section only when the reader is choosing between fields.

## Editorial rules from the May 2026 review (mandatory)

Reference: `style-guide/editorial-rules.md` Part 1 (May 2026). Also apply Part 2 (packaged here as `prose-editing.md`) to every draft and revision.

1. **Listicle items use bullet structure, not chunky paragraphs.** For each item: Website link, Where to apply, Application deadline, Eligibility, Who it's for / why apply, then a 2-3 sentence description.

2. **Bolded sentences must be self-contained.** Read only the bolded sentences in order; they should convey the article's argument.

3. **Use contractions.**

4. **Narrowed October 12, 2026.** On program and firm articles, say what the program is and what the firm looks for in a candidate, as facts the student acts on. Don't open sections from the firm's side of the table or explain the firm's motives (`prose-editing.md` rule 19).

5. **Drop stock sub-headers like "The honest read:"** when they add bulk without skimming value.

6. **Frame positively.** Not "Most candidates under-prepare for behaviorals." Yes "Behaviorals are one of the most important factors in offer decisions."

7. **Intros follow `intros.md`** (updated October 8, 2026): direct answer first, two to five sentences, no buildup.

8. **For recruiting/internship articles, target the next open cycle**, not the one that just closed.

9. **Say this / don't say that callouts are optional** (October 14). Use a short block only when it shows something the article's examples haven't. Two or three is plenty.

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

25. **Bolding (relaxed October 14):** bold the sentence worth remembering in a section when there is one. The bold-only read should still tell the argument, but don't manufacture a bold claim for every section, and keep qualifiers in bolded sentences where the fact varies.

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
- Talk like someone who knows the field: "usually," "often," "most firms," "some banks" where that's true. No documentary-narrator certainty.
- Use specific numbers, timelines, real examples.
- Plain headers and plain words. Simple, direct titles.
- Say what to do, not what's wrong with the reader.
- Explain what the reader will do plainly and completely, then stop. Background gets a line. Don't restate.
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

Output a new version: `draft-{slug}-v2.md`. Don't overwrite v1. Every revision re-runs the intro check, plain-language, thoroughness, section-verdict and prose passes on the changed sections, then the quality review, and ends with a fresh Thoroughness Report. A revision asked to fix specific problems fixes those problems in place; it isn't a rewrite. A "make it shorter" request runs `prose-editing.md` rule 16 on the whole draft.

## Delivery to Google Docs (known limitation)

The Drive MCP `create_file` tool doesn't reliably convert `text/html` to a native Google Doc.

1. **Default: build .docx into `published/ai-written/`.** Run `python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"` and deliver that file. Drive converts it to a Google Doc on open.
2. **If uploading to Drive directly**, upload the built `.docx`, never `text/html`.
3. **Never paste raw Markdown or HTML into Drive** expecting auto-conversion.