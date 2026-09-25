---
name: wsg-article
description: "Use this skill any time the user asks to write, draft, generate, outline, edit, format, or review a WallStreetGuide.net (WSG) blog article: ultimate guides, listicles, niche posts, intros and hooks, formatting, prose editing, plain-language or thoroughness passes, or WSG keyword research."
---

# WSG Article Generator

You are generating a blog article for WallStreetGuide.net (WSG), a site helping ambitious American undergraduates break into investment banking and consulting.

The WSG project is the `wsg-content` repo folder this skill ships in — every path below is relative to its root. When working outside the repo, ask the user to attach or point you at the repo (or the Claude Content project mirror) before drafting.

**Path tolerance.** Paths below follow the August 20, 2026 reorganized layout (the Claude Content project mirror). If the attached repo still has the pre-reorg layout, use the equivalents: `style-guide/publication-standards.md` section 2 → `style-guide/seo-checklist.md`; section 3 → `style-guide/link-verification.md`; section 1 → `style-guide/formatting-standards.md`; `style-guide/editorial-rules.md` Part 1 → `style-guide/editorial-feedback-may-2026.md`; Part 2 → `style-guide/editorial-feedback-july-2026.md`; `prose-editing.md` → `editorial-feedback-july-2026.md`; `markdown_to_docx_v2.py` → `markdown_to_docx.py` if v2 is absent. The `.claude-skill/intros.md`, `.claude-skill/plain-language.md` and `.claude-skill/thorough-explanations.md` modules exist in both layouts.

## Package modules (consolidated August 2026, extended September 2026 — load on demand)

This package absorbed the former standalone `wsg-article-formatting` and `wsg-prose-editing` skills as modules. Sibling files in this package (repo copies live in `.claude-skill/`):

- `source-verification.md` — entity-verification gate. Loads with EVERY article task (step 1 below).
- `intros.md` — the opening: one rotating hook type (decision moment, scene, friend/roommate story, stat, claim, question, first-call quote), the Stephen Turban intro always present, story polarity (WSG never looks bad), no fake-precise effort counts, and the "would Stephen say this out loud" wording test. Loads on every draft and revision. (Also on the account as the standalone `wsg-intros` skill.)
- `plain-language.md` — technical ideas explained in plain words at first use, one idea per sentence, no odd syntax; the bar is a sharp high schooler could explain it back. Loads on every draft and revision. (Also available on the account as the standalone `plain-language` skill for non-WSG writing.)
- `thorough-explanations.md` — catches jumpy or over-condensed explanations, expands them before delivery, and defines the mandatory post-delivery Thoroughness Report. Loads on every draft and revision. (Also available on the account as the standalone `thorough-explanations` skill.)
- `prose-editing.md` — prose-level pruning and variance rules (echo enders, burstiness, perplexity, and rule 9, the say-it-out-loud diction test). Loads on every draft, revision, or "humanize/de-AI this" pass, after the modules above.
- `formatting.md` — Title / Heading 2 / Normal structure and spacing spec for .docx / Google Doc output. Loads whenever a draft is formatted or built to .docx.
- `consulting.md` — consulting-vertical addendum. Loads whenever the topic is consulting.
- `recruiting-relevance.md` — 1-5 relevance + F/S-fit scoring. Loads on keyword research and content-calendar tasks.

## Word counts are guidelines, not limits (September 2026)

Length guideline: ultimate guide ~2,000-2,500, listicle ~1,800-2,200, niche ~1,800-2,200. These are starting points, not caps. The article runs as long as a thorough, plain-language explanation needs, and going over is expected on technical topics. Short is the failure to watch for: never cut an explanation to hit a number, and never pad to reach one. `scripts/check_article.py` reports length as info and warns only when a draft runs short; there is no upper cap.

## CRITICAL: First steps before writing anything

**Step 1 is non-negotiable. Skipping it is what shipped the May 2026 fabrications.**

1. **Load the source-verification skill.** Read `.claude-skill/source-verification.md` FIRST. This is the gate that prevents fabricated coaches, firms, deals, and individuals from making it into the article. Apply its three-tier protocol (household-name / industry-known / niche) to every named entity you plan to reference.

2. **Read the style guide.** `style-guide/style-guide.md` — voice, structure, dos, don'ts.

3. **Read the weak vs strong calibration examples** — the "Calibration: weak vs strong drafts" section at the end of `style-guide/style-guide.md`.

4. **Identify the vertical.** WSG covers two verticals: investment banking / PE / VC (the default), and consulting. If the article topic is consulting (MBB, tier 2 strategy, Big 4 strategy, boutiques, economic consulting, case interviews, consulting recruiting), **also read `.claude-skill/consulting.md` and the canonical context bundle at `consulting/`**.

5. **Identify the format.** Every WSG article is one of:
   - **ultimate-guide** — insight-led definitive guides (e.g., "How Hard Is It to Get Into IB? 6 Things That Actually Matter")
   - **listicle** — curated resource roundups with exact counts (e.g., "Top 10 Free Resources for IB Interview Questions")
   - **niche** — hyper-specific firm/role posts, edge-case student situations, or honest reviews

   If unclear, ask the user before drafting. Do not assume.

6. **Load the matching template.** Based on format:
   - `templates/ultimate-guide.md`
   - `templates/listicle.md`
   - `templates/niche.md` (with sub-type: firm-or-role / edge-case-student / review)

7. **Check for a deep dive.** If the topic has a corresponding `deep-dives/{topic}.md` (or `deep-dives/consulting/{topic}.md` for a consulting topic), read it in full before drafting. Use its specifics — named firms, real numbers, scenarios — to ground the article.

8. **Pull at least one matching sample.** Look in `samples/{format}/` and `published/`. Read 1-2 samples of the same format to anchor voice and structure. If no samples exist for that format yet, tell the user, and lean harder on the style guide.

9. **Look for a brief.** If the user pointed to `briefs/brief-{slug}.md`, read it. If they didn't, gather the brief fields conversationally:
   - Exact headline
   - Format (and sub-type if niche)
   - Target keyword
   - Target reader (who specifically)
   - Any deep dive to anchor in
   - Specific numbers/scenarios/named firms to include
   - Technical concepts that need a full walk-through
   - Hooks or contrarian angles to land
   - Items to avoid

   If the user asked casually ("write a WSG listicle on free modeling resources"), infer what you can and ask only for what's truly missing.

## Generation workflow

Once briefed:

1. **Outline first.** Show the user the outline (headline, meta, intro hook type, sub-questions, body section H2s, conclusion direction, and which technical concepts will get a step-by-step walk-through) before writing the full draft. Wait for approval or adjustments.

2. **Draft the article** into `drafts/draft-{slug}-v1.md`. Open it per `.claude-skill/intros.md`: one hook type, different from the last article, plus the Stephen intro and a promise of value, in two to three short paragraphs. Length guideline (not a limit):
   - Ultimate guide: ~2,000-2,500
   - Listicle: ~1,800-2,200
   - Niche: ~1,800-2,200

   See "Word counts are guidelines, not limits" above. Write the complete explanation first; the number takes care of itself.

3. **Run the plain-language pass** (`.claude-skill/plain-language.md`). Every technical term, mechanism, or process in the draft gets explained in plain words at first use, one idea per sentence, no odd syntax. The bar: a sharp high schooler could read it once and explain it back. Define the machinery, never the field (don't explain what IB is; do explain how a cov-lite loan works). Simplify the words, never the substance.

4. **Run the thoroughness pass** (`.claude-skill/thorough-explanations.md`). Find every place the explanation jumps (cause to effect with no mechanism, a process named but not walked, a sub-question answered in one line) or is over-condensed (three ideas in one sentence, a bolded claim with nothing under it, a worked example that skips the arithmetic). Expand each one before delivery. Longer is expected here.

5. **Run the prose pass** (`.claude-skill/prose-editing.md`) on the expanded draft: echo enders, dashes, burstiness, perplexity, register words, and the "would Stephen say this out loud" test on every sentence (rule 9). This pass trims fat; it never removes a step the thoroughness pass added.

6. **Run the SEO checklist** in `style-guide/publication-standards.md` (section 2) against the draft before delivering. Fix anything that fails.

7. **Run the 4-question gut check** (see style guide):
   - Does this sound like real experience?
   - Would a smart junior find this useful?
   - Could another blog have written this?
   - If I cut a paragraph, would it matter?

   Target: yes / yes / no / yes. If off, revise before delivery.

8. **Deliver the file** with a `computer://` link and a 2-3 sentence summary of what was built.

9. **Post the Thoroughness Report (fail-safe, mandatory).** Right after the file link, append the report defined in `.claude-skill/thorough-explanations.md`:

   ```
   Thoroughness Report
   - Expanded before delivery: {N} passages
     - {section}: {what was jumpy and what was added}
   - Still thin (needs a source, a number, or the user's input): {N}
     - {section}: {what's missing and why}
   - Plain-language rewrites: {N} paragraphs (terms explained at first use: {...})
   - Word count: {final} (guideline for this format: {range}; over is fine)
   ```

   Post it with zeros if nothing was expanded. An article without the report has not finished the workflow. Never fill a "still thin" spot with generic filler to shorten the list; flag it and let the user decide.

## Hard rules (do not violate)

These come straight from the style guide. Always enforce:

- **Use the exact headline** from the brief or content calendar. Never tweak it.
- **Include 1-2 H2 sub-questions** right after the intro, each answered in 2-4 sentences.
- **Listicles must hit the exact count in the headline.** "Top 10" means exactly 10 items.
- **Inline anchor-word hyperlinks only.** Never list URLs below items.
- **No em-dashes or hyphens as structural punctuation** in body copy.
- **No filler phrases** ("highly competitive," "in today's landscape," "many students find," "it's important to note").
- **Every major section needs a specific** — named firm, real number, named scenario, or first-person experience. Generic = fail.
- **Bolded sentences are full claims**, never random words.
- **No definitions of basic terms.** Reader is a smart undergrad who already knows what IB is. (Basic = the field. Technical machinery still gets a plain-words explanation at first use.)
- **Openings follow `intros.md`.** Hook type rotates article to article, Stephen intro is always present (credentials from `writers/stephen-turban.md` only), WSG never looks bad in its own stories, no invented effort counts, every sentence passes the say-it-out-loud test.
- **Explain the machinery in plain words and walk every step.** No jumps from cause to effect, no three-ideas-in-one-sentence, no one-line answers to how-does-X-work questions. Word count never justifies skipping a step.
- **CTA only if it lands naturally.** Per user instruction: "no need to really plug in WSG at the end unless you think it can be done flawlessly." Default to no CTA.
- **Reviews must include real cons.** If you can't find a real con, you haven't researched the product.

## Editorial rules from the May 2026 review (mandatory)

Reference: `style-guide/editorial-rules.md` Part 1 (May 2026). Also apply Part 2 (July 2026 prose-level rules; packaged here as `prose-editing.md`) to every draft and every revision pass. These came from real published-version edits and override any conflicting older guidance.

1. **Listicle items must use bullet structure, not chunky paragraphs.** For each program/firm/resource item: Website link, Where to apply, Application deadline, Eligibility, Who it's for / why apply, then a 2-3 sentence description. Big strategy paragraphs prevent skimming. (For question-listicles, the answer walk-through under the bullets gets the room it needs; the bullets stay tight.)

2. **Bolded sentences must be self-contained.** Read only the bolded sentences in order — they should convey the article's argument. Bolding "It is not" or "the third path" is wrong because they're not standalone.

3. **Use contractions.** "don't" not "do not", "you're" not "you are", "it's" not "it is".

4. **Lead with the company's perspective first** on program/firm articles. What is the bank trying to achieve through this program? Then back-derive what makes a competitive candidate.

5. **Drop stock sub-headers like "The honest read:"** when they add bulk without skimming value. Replace with program description, who is competitive, and how to apply.

6. **Frame positively.** Not "Most candidates under-prepare for behaviorals." Yes "Behaviorals are one of the most important factors in offer decisions."

7. **Tighten intros to 1-2 short paragraphs** with a quantifiable lead claim where possible. No four-paragraph buildup. (Thoroughness expands the body, not the intro.)

8. **For recruiting/internship articles, target the next open cycle, not the one that just closed.** SEO ranking takes 2-3 months. Default to cycles opening 6+ months from publication.

9. **For behavioral / how-to-answer articles, include explicit "say this / don't say that" examples** at the end, as direct callouts:
   > **Why this firm?**
   > Don't say: "Goldman Sachs is very prestigious."
   > Say: "I spoke to Sarah in your healthcare group last month and she described [specific]."

10. **Use clear blank-line paragraph spacing** in Markdown so the rendered article reads as discrete paragraphs, not a wall.

11. **Address top firms not on the list (May 23 review).** For any "Top N" curated list where well-known top firms don't use the listed channels (e.g., a16z and Sequoia don't recruit undergrads directly through VC fellowships), include a short section explaining how readers should approach those firms. The reader will notice the gap.

12. **Hard paragraph breaks at logical pivots (May 23 review).** Within a section, insert a blank line whenever the argument pivots between two distinct ideas ("this path is right for X" vs "this path is right for Y"). No exceptions — always start a new paragraph at the pivot.

13. **Niche-specific freshness check (May 23 review).** Before finalizing any curated list, run one web search for "best [niche] firm/program for [specific student profile] 2026" to confirm the list is current. Past misses include NEO Capital for technical-undergrad VC. Swap in or add an honorable mention if a clearly-better-than-listed firm exists for a real sub-niche.

14. **Don't recite timeline math at the reader (May 23 second review).** The recruiting-timeline-glossary exists for me, not the article. If the headline says the cycle year and the eligibility line says the graduation year, the reader has what they need. Do not add paragraphs explaining "the students applying are sophomores in 2026-2027 academic year, Class of 2029." That's condescending and pads word count.

15. **RX is an Elite Boutique product, not a BB coverage group (May 23 second review).** Never list RX in a BB group-preference list. BB group preferences to name: TMT, healthcare, FIG, industrials, consumer & retail, energy, real estate, M&A, leveraged finance, ECM/DCM. RX firms to name when discussing restructuring: Houlihan Lokey, PJT, Lazard, Moelis, Evercore, Greenhill.

16. **Capitalize "Investment Banking Summer Analyst" as a defined role title (May 23 second review).** Capitalize each word when referring to the role or program as a title: "Investment Banking Summer Analyst," "Summer Analyst Program," "Sophomore Summer Analyst Program." Lowercase is only acceptable when describing the work generically ("a summer banking internship") — not when naming the role.

17. **Default writer is Stephen Turban (May 24 update).** Every article carries `byline: stephen-turban` in the frontmatter unless explicitly assigned to another writer. Use `writers/stephen-turban.md` voice templates — no "as an IB analyst" framings, ever. Meta description must lead with "WSG founder Stephen Turban...".

18. **Locked .docx formatting standard (May 24 update).** Every .docx file shipped from `published/` must match `style-guide/publication-standards.md` (and this package's `formatting.md` module): Arial throughout, H1 24pt bold black, H2 18pt bold black, H3 14pt bold + underline black, body 11pt black, 2.0 line spacing everywhere. The current builder `scripts/markdown_to_docx_v2.py` enforces this (Title / Heading 2 / Normal styles, empty-line spacing — the August 2026 spec) — always build .docx through that script rather than copy-pasting markdown into Word. v1 `markdown_to_docx.py` is retained for history only.

19. **Headline rules (May 25 update — applies to ALL articles).** Headlines must be (a) under 8-10 words, (b) lead with opportunity or value (not abstract opinion), and (c) avoid college-essay colon-phrases ("Beyond the Case:", "From Panic to Passed:", "The Insider Blueprint:", "Cracking the Code:", "The Rise of..."). The headline must answer either "what opportunities does this give me?" or "how do I get to a specific outcome?" If a brief or content-calendar entry violates these rules, rewrite the headline before drafting and confirm with the user. Full rule set at `style-guide/editorial-rules.md` Part 1 section 12.

20. **Source verification (May 25 update — applies to ALL articles).** Before naming any coach, mentorship platform, recruiting firm, boutique firm, specific deal, named individual, book, or simulator in an article, verify the entity exists. Load `.claude-skill/source-verification.md` and apply the three-tier protocol: skip verification for Tier 1 household-name entities (Goldman, McKinsey, Sequoia, etc.), verify Tier 2 industry-known names via a single web search + URL fetch, verify Tier 3 niche names with multi-source confirmation. If you can't verify, remove the name. The May 2026 fabrications (The Banker's Pillar, GoodPath) document the failure mode this rule exists to prevent.

## Standing rules from the August 2026 batches

From `claude/corrections-aug-21-2026.md` and `claude/batch-log-aug-27-2026.md`. Rules 21-24 are expanded in `intros.md` (openings) and `prose-editing.md` rule 9 (diction, whole article).

21. **Every article opens with a hook plus the Stephen Turban intro**, varied article to article. Composite people get single-letter names. Intros stay tight (2-3 short paragraphs) with the target keyword in the first 100 words.

22. **WSG never looks bad in its own stories.** Setbacks happen before someone finds WSG; students advised by WSG win.

23. **No implausible effort counts in stories.** Use plausible, roundable language; real outcome numbers stay.

24. **Cut copywriter-isms and off-register phrases.** The test: would Stephen say this sentence out loud to a student? If not, write the plain version.

25. **Bolding density matches the published library:** every H2 section and every H2 sub-question answer carries at least one bolded self-contained claim; the bold-only read-through must still tell the argument.

## Recruiting timeline math (mandatory before any recruiting article)

Before writing any article that references IB / PE / consulting / VC recruiting years, **read `style-guide/recruiting-timeline-glossary.md` in full**. Conflating application year, internship year, and graduation year is the most common factual mistake in WSG drafts.

The standard sophomore junior-summer cycle:

`application year A` → `internship year A + 1` → `graduation year A + 2`

Quick examples:

- "10 IB Internships to Apply To in 2026" → applications submitted in 2026 → **Summer 2027 internship** → graduation Spring 2028 (Class of 2028). Eligibility: "sophomores graduating December 2027 to June 2028."
- "10 IB Internships to Apply To in 2027" → applications submitted in 2027 → **Summer 2028 internship** → graduation Spring 2029 (Class of 2029). Eligibility: "sophomores graduating December 2028 to June 2029."
- "10 IB Internships to Apply To in 2028" → applications submitted in 2028 → **Summer 2029 internship** → graduation Spring 2030 (Class of 2030).

Sophomore-summer programs (BofA Sophomore SA, JPMorgan Launching Leaders, Apollo Sophomore SA) have different math: `application year A` → `sophomore-summer internship year A + 1` → `graduation year A + 3`.

The check before writing any sentence with a year: does this refer to the year of application, internship, or graduation? Does the year I'm writing match what the article headline implies? Does the eligibility language match the internship year, not the application year?

## Link verification protocol (mandatory before delivery)

Every URL in a WSG article must point to a page that exists, works today, and is appropriate for the article's time horizon. **If a link is broken, speculative, or points to content that doesn't exist yet, remove it.** Better no link than a wrong one.

Three categories to catch:

1. **Dead links.** 404s, redirects, renamed pages. Test by clicking.
2. **Rotating job-posting URLs.** Greenhouse `gh_jid=`, BofA `/job-detail/{N}/`, iCIMS `/jobs/{N}/`, Citi numeric posting IDs, Workday specific job posting IDs, LinkedIn job postings. These rotate every cycle and will 404 by the time the article ranks on SEO.
3. **Speculative URLs.** Pages that don't exist yet (e.g., "Goldman Sachs 2028 SA Program" page before applications open for 2028). Never invent or guess.

**The rule for forward-looking articles** (e.g., a 2027 article written in 2026): link only to evergreen firm careers landing pages, not cycle-specific posting URLs.

**Before any draft moves from `drafts/` to `published/`, run:**

```bash
python3 scripts/check_links.py drafts/{file}.md
```

The script extracts every link, attempts to reach each, flags suspicious patterns (Greenhouse / Workday / iCIMS posting IDs, mismatched cycle years), and returns nonzero if anything fails. Address every flagged link before publishing: fix, replace with an evergreen alternative, or remove and keep the text un-hyperlinked.

Full protocol with safe-vs-unsafe URL patterns is in `style-guide/publication-standards.md` (section 3).

## VERIFY-tag protocol (mandatory)

Any factual claim that could be wrong by publication time must be tagged `[VERIFY: <what to verify>]` inline in the draft. The user or an editor will then ctrl-F for `[VERIFY` before publishing and confirm or correct each one.

**Always tag:**
- Application deadlines, program windows, and "applications open/closed" claims
- Compensation figures (salaries, bonuses, fees)
- Eligibility rules (GPA cutoffs, graduation year requirements, citizenship)
- Specific deal references (deal size, parties, advisor roles)
- Live job posting URLs (link can rot between research and publishing)
- Acceptance rates and class sizes
- Any "as of [date]" claim

**Example:**
> Applications close December 14, 2026 [VERIFY: live posting on Stifel careers].

Do not over-tag. A general claim like "Goldman is highly selective" does not need verification. A specific claim like "Goldman's 2027 SA acceptance rate is below 1 percent" does.

## Writer profile loading

**Default byline: Stephen Turban (WSG founder).** Every WSG article is ghostwritten for Stephen unless the brief, content calendar, or user explicitly names a different writer. Always:

1. Add `byline: stephen-turban` to the article frontmatter.
2. Read `writers/stephen-turban.md` in full before drafting.
3. Use one of the approved byline-paragraph templates from that profile, or a varied first-person intro per `intros.md`. Do NOT write "As an IB analyst who..." — Stephen has never been a banker. He's a Harvard alum, former McKinsey consultant, Bridgewater alum, Lumiere co-founder, WSG founder. Never add a credential that isn't on the profile.
4. Frame named-student scenarios as "a student I mentored" or "a student I worked with through WSG" — not "an analyst on my team." Roommate, friend, and family stories are also fine and keep the openings varied.
5. The meta description must lead with "WSG founder Stephen Turban..." so the byline shows in SERP and OG previews.

If a different writer is assigned, read `writers/{writer-slug}.md` for their profile. The profile contains:

- Background and credentials (what they actually did)
- Voice tells (the specific phrasing they use)
- Signature scenarios they have used before (real students, deals, situations)
- Topics they should not write about (outside their expertise)

Pull at least one specific scenario from the writer's profile into the article as a credibility moment.

## Voice cues (read the style guide for full guidance)

- Write to one person — a sophomore at a state school googling at 11pm. Use "you."
- Open with the reader's assumption or a sharp observation, not a definition.
- Lead with substance — short intro, then immediate value.
- Use specific numbers, timelines, real examples.
- Sound like someone who has been through it.
- Explain the machinery plainly and completely. Simple words, every step, no jumps.
- Every sentence should sound like something Stephen would say out loud to a student.

## Deep-dive workflow (the restructuring pattern)

When the user wants articles spawned from a deep dive:

1. They write `deep-dives/{topic}.md` — a comprehensive internal guide (no SEO constraints, no length limits) containing the full picture: what it is, how it works, players, recruiting, day-to-day, exits, named scenarios.

2. When they ask for an article anchored in that deep dive (e.g., "write an ultimate guide on how to break into restructuring"), you:
   - Read the deep dive in full
   - Pull the slice relevant to the article
   - Use the named scenarios from the "Specific stories" section as the credibility moments
   - Flag if anything depends on info in the deep dive's "Open questions" section

3. The deep dive is internal. Never publish it. It's the well the articles draw from.

## Output format

Always write the final article as Markdown to `drafts/draft-{slug}-v1.md`. Use this frontmatter at the top:

```
---
headline: {exact headline}
byline: stephen-turban
target_keyword: {keyword}
secondary_keywords: [{kw1}, {kw2}]
format: {ultimate-guide | listicle | niche}
sub_type: {if niche: firm-or-role | edge-case-student | review}
hook_type: {decision-moment | scene | friend-story | stat | claim | question | first-call-quote}
word_count_target: {~1800-2200 | ~2000-2500, guideline only, no cap}
status: draft-v1
---

# {Headline}

**Meta description:** WSG founder Stephen Turban {what the article does}.

{Article body starts here}
```

## When the user revises

If the user asks for revisions ("rewrite section 3, make it harder-hitting"), output a new version: `draft-{slug}-v2.md`. Do not overwrite v1. Every revision re-runs the intro check, plain-language, thoroughness, and prose passes on the changed sections and ends with a fresh Thoroughness Report.

## Delivery to Google Docs (known limitation)

The Drive MCP `create_file` tool does **not** reliably auto-convert `text/html` to a native Google Doc. Files uploaded as `text/html` land in Drive as HTML, requiring the user to right-click → Open with → Google Docs to convert.

**Reliable delivery patterns:**

1. **Default: build .docx into `published/ai-written/`.** Run `python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"` and deliver that file. The user drags it into Drive, and Drive converts the .docx to a native Google Doc on open.
2. **If uploading to Drive directly**, upload the built `.docx` (never `text/html`) so Drive's converter handles it, and tell the user to open it with Google Docs.
3. **Never paste raw Markdown or HTML into Drive** expecting auto-conversion — it lands as a plain file and the formatting is lost.