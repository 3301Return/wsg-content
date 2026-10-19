# QA brief: independent review of the October 11, 2026 batch

You are the QA reviewer for ONE WallStreetGuide (WSG) draft. You did not write it. Your job is to catch what the writer missed: wrong facts, arithmetic that doesn't tie, rule breaks, AI tells, broken links, and anything the founder would flag. You fix what can be fixed with surgical edits in the draft itself and report everything else. Work from the repo root /home/claude/repo. Today is Sunday, October 11, 2026.

## Read first (the rules you are checking against)

1. `claude/batch-brief-oct-11-2026.md`: founder decisions (headlines stay exactly as given; two articles are v2 rewrites), the rules index, your article's section.
2. `.claude-skill/SKILL.md`: the October 8 and October 7 rules at the top, the length target, the hard rules, the editorial rules 1 to 25, the VERIFY protocol, the link protocol.
3. `.claude-skill/reference-articles.md`: what good and bad look like to Stephen.
4. `.claude-skill/intros.md`, `.claude-skill/prose-editing.md` (rules 1 to 16 and the mechanical spot checks), `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md`, `.claude-skill/source-verification.md`, `.claude-skill/consulting.md`, `consulting/voice-cues.md`.
5. `style-guide/recruiting-timeline-glossary.md` if the draft names any recruiting year.

## The checks, in order

**A. Facts (the most important check).** Pick at least eight factual claims that matter most to the reader (pay figures, hours, dates, program names, quotes attributed to a firm or a person, process steps) and verify each one yourself with WebFetch or WebSearch against the primary source or the tracker named in the VERIFY tag. Don't trust the writer's citation; open the page. For each: PASS, or FAIL with the correct figure and source. Fix FAILs in the draft. If a source can't be reached, say so and leave the VERIFY tag in place. Every named third-party entity (firm, program, tracker, person, book) must exist and match its description (source-verification.md tiers); an entity that fails is removed from the draft, never tagged.

**B. Arithmetic.** Recompute every calculation in the draft in Python (take-home math, per-hour pay, percentages, sums in tables, year counts). Every figure in the prose must match its table and its own inputs. Fix mismatches.

**C. Timeline math.** Every recruiting year passes the glossary check: application year A, internship Summer A+1, graduation Spring A+2 (sophomore programs: graduation A+3). The internship summer and the class are named.

**D. Rules, mechanically.** Run every grep in the "Mechanical spot checks" section of prose-editing.md and fix every real hit (dashes, echo enders, register words, negatives about the writer/WSG/article, unsupported "most candidates" opinions, bio and first-person memories, say-it-out-loud suspects, fake-precise effort counts). Then: no `byline:` in the frontmatter; the headline in the H1 and frontmatter is exactly the brief's; meta description 150 to 160 characters, topic first, no person named; two H2 sub-questions right after the intro, each phrased as a search question ending in "?" and answered in its first sentence; every H2 section has at least one bolded full sentence with a fact or clear rule; read only the bolds top to bottom and confirm they tell the argument; no bolded fragments or labels; no closing section that recaps the article; no "The honest read" header; headers are plain and literal, numbered insight headers are short plain claims; say/don't callouts present where the brief asked for them; inline anchor-word links only; no rotating job-posting URLs.

**E. Opening (intros.md).** Sentence one says what the topic is or answers the headline, with the target keyword. A bolded full sentence with a concrete verified fact follows. The last sentence says what the article covers. Two to five sentences. No scene, no story, no "most candidates," no bio, no clever line. Compare it to the good openings in reference-articles.md and fix it if it reads like the bad ones.

**F. Plain language and thoroughness.** Read every paragraph that explains a mechanism. Each technical term is explained in plain words at first use, once. No sentence carries three ideas. No step is skipped (cause to effect with no mechanism, a process named but not walked, a verdict with no axes). Fix jumps by adding the missing step and pay for it by cutting repetition in the same section.

**G. AI tells and the humanizer pass.** Apply the WSG prose rules and the humanizer method: cut inflated significance claims, vague attribution ("experts say"), stock AI vocabulary (navigate, landscape, leverage as a verb, crucial, robust, delve, pivotal, seamless, streamline, "it's worth noting," "in today's"), forced triads, antithesis scaffolds ("not just X, it's Y," "X isn't Y, it's Z" outside of a signposted heading that follows Stephen's model), echo enders, filler hedges, copywriter lines, and chatbot artifacts. Check sentence-length variety (burstiness): in any five-paragraph stretch there should be at least one paragraph under 15 words and one over 100. Every sentence and header passes the say-it-out-loud test. Repair with something concrete, never with a safer cliché.

**H. Clean text.** Scan the file for invisible or suspicious Unicode (zero-width spaces, soft hyphens, non-breaking spaces, Unicode minus, curly quotes if the repo's other drafts use straight ones). Fix them. Confirm no personal identifiers (real student names, emails, local file paths) appear.

**I. Gates.** `python3 scripts/check_article.py drafts/{file}` and `python3 scripts/check_style.py drafts/{file}` pass; `python3 scripts/check_links.py drafts/{file}` passes (WSG links sometimes 429 on a fast first pass; rerun once). `wc -w` the body against the format's target (niche about 4,500 to 5,500, ultimate guide about 5,000 to 6,000; VERIFY tags and tables don't count toward the reader-facing length).

## How to edit

Surgical edits only: fix the sentence, the number, the header, the tag. Don't restructure, don't add sections, don't change the headline, don't add images, don't change the voice wholesale. Keep every explanation step. Use the Edit tool for small changes; for a paragraph-sized rewrite, Edit is fine too. After editing, rerun the gates. Only edit your own article's draft file.

## Report (under 600 words)

1. Facts checked: a table of claim, source opened, PASS/FAIL, fix made.
2. Arithmetic: what you recomputed and whether it tied; fixes.
3. Rule and prose fixes: a list of the edits you made (old → new, or a one-line description each).
4. Opening verdict: a one-line comparison to the reference openings.
5. Bold-only skim: does the argument survive? Any bolds fixed?
6. Gate results after your edits (check_article, check_style, check_links, wc -w).
7. Still open for the founder: anything you couldn't verify or that needs a decision (one line each).
