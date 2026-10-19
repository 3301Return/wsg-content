# Revision brief: October 12, 2026 (founder and Sanskar feedback on the October 11 batch)

Repo root `/home/claude/repo`. Today is Monday, October 12, 2026. You are revising ONE article from the October 11 batch.

## The feedback (verbatim, from Slack, about a sibling consulting resume draft; it applies to this whole batch)

> "I think overall the process just seems like it's following instructions too much without using its own intelligence, like it's starting off the consulting skeleton by spending a lot of time talking about similarities/difference between banking resumes."

> (On a paragraph that opens with Leonardo da Vinci's 1482 letter to Ludovico Sforza as "the earliest known resume") "like 🤢"

> "let's also do one thing where we stop asking it to explain these redundant parts. I think the student doesn't need the 'why' behind resume screenings." (On a section that opened "Start on the firm's side of the table. McKinsey receives roughly 1 million resumes annually and hires less than 1 percent... The resume screen exists to get the stack down to the people worth 45 minutes of a consultant's time, and everything about how it works follows from that.")

> "this is what I think is a bug in the system where a lot of consulting banking becomes interlinked, like this is kind of deflecting the point into banking resume opposed to explaining what is actually the issue." (On "Ana's problem is the one I see most often: students treat a consulting resume as a banking resume with the order changed.")

## What the feedback means, as four problems to find and fix

1. **Cross-vertical deflection.** The article drifts into another career (usually banking) instead of explaining its own subject. A consulting article explains consulting. Mention banking only where the reader is actually choosing between the two, and then once, briefly, in its own clearly labeled place. Never use banking as the frame for explaining a consulting thing ("a consulting X is like a banking X but...", "unlike banking...", "a first-year banker would..."). Delete the comparison and explain the consulting thing directly.

2. **Off-topic history and trivia.** Founding dates, reorganization histories, who coined a term and when, "the earliest known," famous-person anecdotes, a firm's corporate timeline. Cut it unless the reader needs the fact to act. Test: if a student deleted the sentence, would they do anything differently? If not, cut it. A one-clause attribution ("the pyramid principle, from Barbara Minto's book") is fine; a biography isn't.

3. **Redundant "why" explanations.** Sections that explain why the firm does something, from the firm's side, before (or instead of) telling the student what to do: "Start on the firm's side of the table," "the screen exists to...," "the firm is trying to...," "to understand X you have to understand why firms...," application-volume statistics used to justify a process. The student needs the what and the how. Keep a "why" only when it changes what the student does, and then in one sentence attached to the instruction. Note: the older rule "lead with the company's perspective first" (editorial rule 4) was being over-applied and is now narrowed; don't follow it here.

4. **Instruction-following instead of judgment.** Sections that exist because a template or brief listed them, not because the reader needs them: a comparison table that repeats the prose, a "how this differs from X" section, a background section, a firm's revenue and headcount when the article is about a junior role. For every H2, ask: "Does a student reading this headline need this section to do the thing the headline promises?" If the honest answer is no, cut it or fold its one useful fact into a section that earns its place.

Also re-check (these are already banned, and the feedback examples break them): no composite or named student stories ("Ana's problem"), no "the one I see most often," no first-person memories.

## How to work

1. Read, in this order: this brief; `.claude-skill/SKILL.md` (top sections); `.claude-skill/prose-editing.md`; `.claude-skill/reference-articles.md` (Stephen's good set is short and direct; aim for that); `.claude-skill/intros.md`. Then read your draft in full, slowly, as the student in the headline.
2. **Make a section-by-section verdict first**, in a scratch note: for every H2 and every paragraph that touches problems 1 to 4, write keep / cut / shrink / rewrite and one reason. Use your own judgment; the goal is an article a sharp student finds direct and useful, not one that passes a checklist.
3. Edit. Write the new version to the file named in your assignment (never overwrite the old version: copy it first, then edit the copy). Cut, shrink and rewrite. Don't pad to recover length: shorter is fine when the topic is covered. Where cutting exposes a thin spot in the article's own subject (a consulting mechanism explained in one line), expanding that explanation is welcome.
4. Keep everything that already passed: the intro shape (intros.md), the two H2 sub-questions, full-sentence bolds in every H2 section with the bold-only read still telling the argument, plain headers, no dashes, contractions, VERIFY tags on moving facts, inline anchor links only to live pages. If you cut a section that held a bold or a link, make sure the rest still meets the rules.
5. Update the frontmatter `status:` to the new version.
6. **Images.** Your article's images are already inserted as `![...](...)` lines, each followed by a `*Source: ...*` line. If an edit removes the passage an image illustrates (a banking chart, a history diagram), delete that image line and its source line from the draft, delete the PNG, and remove the image from the build script and manifest. Then point the build script at your new draft file (it has a `DRAFT` path or similar constant and regex assertions against the draft text), fix any assertions your edits broke, re-run `python3 scripts/images/build_{slug}.py` until it exits 0, renumber nothing (gaps in NN are fine), and run `python3 scripts/images/insert_images.py {slug} drafts/{new file}` (idempotent; it adds any image whose anchor moved and was lost). Confirm with `grep -c '^!\[' drafts/{new file}` that the count matches the manifest. If an image's anchor line was rewritten, update the manifest anchor to the new line's first 60 characters.
7. Gates: `python3 scripts/check_article.py`, `python3 scripts/check_style.py`, `python3 scripts/check_links.py` on the new file; the mechanical spot checks at the end of prose-editing.md; plus these greps, and justify or fix every hit:
   - `grep -inE "bank|banker|goldman|jpmorgan|wall street" {file}` (should be zero outside the one allowed comparison, if your assignment allows one)
   - `grep -inE "firm's side|exists to|is trying to|the reason (firms|the firm)|receives (roughly |about )?[0-9]|history|historically|founded|in 1[0-9]{3}|first (woman|female|known)|earliest" {file}`
   - `grep -inE "see most often|my (student|client)|a student (I|named)" {file}`
8. `wc -w` the new file.

Only edit your own article's files (the new draft, its build script, its manifest and PNG folder).

## Report (under 450 words)

1. The section-by-section verdict, condensed: each H2 with keep / cut / shrink / rewrite and the reason, in one line each.
2. The cuts by problem (1 to 4), with the removed or rewritten text summarized in a few words each.
3. Images removed or changed, and the build/insert result.
4. Gate results and word count (old → new; body without VERIFY tags).
5. Anything you left in on purpose that a reviewer might question, with the reason.
