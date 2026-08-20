# Editorial Feedback: July 2026 Review (Prose-Level Edits)

Source: the July 12, 2026 edit pass on the consulting cover letter draft. This file layers on top of `style-guide/style-guide.md` (especially the AI sniff test section) and `style-guide/editorial-feedback-may-2026.md`. Every existing rule still applies. Intended repo location: `style-guide/editorial-feedback-july-2026.md`.

These rules are pruning rules. They tell you what to cut and how to vary, not how to restructure. The WSG format itself (bolded skim narrative, H2 sub-questions, say/don't blocks) stays exactly as specified in the main skill.

## 1. Cut echo enders. Keep payoffs.

The July review found 8 to 9 sentences that closed a section by restating the paragraph's point in fancier words. Real examples that were cut:

> "Most weak cover letters fail on generic content and recycled templates, which means specificity is both the fix and the differentiator."

> "Naming a specific contact, practice, or piece of work is the single clearest way to prove your interest in a firm is real."

Both sentences follow paragraphs that already made the same point. A reader who got it the first time reads the restatement as filler. A reader trained on AI text reads it as a tell.

**The delete test:** remove the sentence. If the section lost no information, it was an echo. Cut it.

**The suspect openers:** "which means," "in other words," "put simply," "that's why," "ultimately." A closing sentence that starts with one of these is guilty until proven otherwise.

**The bound, and this is where caution comes in:** do not strip every section ender. Two protections apply.

First, the skim narrative is load-bearing. WSG articles bold self-contained claims so that reading only the bolds tells the argument, and `check_style.py` tests for this. After cutting, at least three sections should still end on a bolded claim, and the bold-only read-through must still carry the article. If it doesn't, you cut a payoff, not an echo. Restore it.

Second, calibration sentences are content, not echo. "The cover letter is a margin tool, not a decider, but margins are exactly where competitive applications are won or lost" was cut in the July pass and should not have been. It sizes the stakes. Nothing before it said that. A sentence that tells the reader how much something matters, with a mechanism attached, earns its place even in closing position.

The distinction in one line: an echo repeats the paragraph at the same level of abstraction, a payoff compresses it into a rule the reader can carry out of the article.

## 2. Dangling verbs get objects, and the fix obeys the punctuation rules

Caught in review: "This is where most letters fall apart and where you can separate." Separate what? The verb needs an object.

The tempting fix used an em-dash. Em-dashes stay banned in body copy, including in edits, including when the dash would genuinely read fine. The dash is the single most recognized AI tell in 2026 and the ban is absolute.

Fix with a period and a short second sentence:

> "This is where most letters fall apart. It's also where you can set yourself apart."

Same rule for en dashes and spaced hyphens used as pause punctuation. Commas, periods, and colons cover every case.

## 3. Sequences become lists. Arguments stay prose.

The cover letter draft explained a four-paragraph structure in four back-to-back sentences: "The first paragraph states... The second explains... The third gives... The fourth closes..." That's a spec wearing a paragraph costume. Convert it to a bulleted list.

The trigger: three or more consecutive sentences sharing the same scaffold ("The first... The second... The third..."), describing steps, parts, or fields. That content is genuinely a list.

The counter-trigger: reasoning is not a list. If the sentences build on each other rather than sit beside each other, bullets would break the argument. Leave it as prose.

Formatting note: blank line before the list, or it renders wrong in Wix and the docx builder mangles it.

## 4. Repair voice with something concrete, not something safer

The review replaced "That last point is the quiet one:" with "That last part matters more than people realize:". The original tried a bit hard. The replacement is worse in a different direction: "more than people realize" sits next to "many students find" in the filler family this style guide already bans.

When a phrase reads as strained, the repair must add information, not subtract personality. Here the concrete fix was available: "That last paragraph is the one screeners actually remember." A specific claim beats both the clever version and the bland one.

## 5. Sample text inside articles follows body-copy rules

Example cover letters, example answers, and say/don't blocks are the most-copied text in any WSG article, so they get edited hardest, not lightest. From the July pass: cut stated-goal throat-clearing ("I want to start my career in consulting because..."), split any sentence carrying three ideas into two or three sentences, and swap abstract language for one concrete detail. A sample that opens with a specific engagement, number, or named conversation teaches the reader what specificity looks like better than any instruction paragraph can.

## 6. Burstiness: vary length on purpose

Burstiness is variance in sentence and paragraph length. AI text runs uniform: sentences of 15 to 25 words, paragraphs of 60 to 90, every section the same shape. Human writing spikes.

The style guide's sniff test already flags symmetric paragraphs and the three-beat rhythm. This rule adds targets to edit against:

- In any five-paragraph stretch, at least one paragraph under 15 words and at least one over 100.
- Sentence lengths in a section should span from under 6 words to over 30. If every sentence lands between 12 and 22 words, split two and merge two.
- At least one section should open with its shortest sentence.

Four words is a paragraph. Use that sparingly and it lands hard.

## 7. Perplexity: predictable phrases teach nothing

Perplexity is how surprising the next word is. If the reader can finish your sentence, the sentence carried no information. "Networking is important because relationships are..." Everyone typed "key" before reaching it.

Two ways to raise perplexity. The honest way: add specifics. Names, numbers, dates, and mechanisms are unpredictable because they're facts, and they're the reason the style guide demands them. The dishonest way: thesaurus swaps and weird diction for its own sake. Don't. "Utilize your network synergistically" has high word-level surprise and reads worse than the cliché it replaced.

Phrase patterns to cut on sight, beyond the existing banned list:

| Cut this | Why |
| --- | --- |
| "It's not just X, it's Y" | The most common AI antithesis scaffold |
| Adjective triplets ("clear, concise, and compelling") | Rule-of-three filler; keep the strongest one |
| "at the end of the day," "the key takeaway" | Pure connective tissue |
| "navigate," "landscape," "leverage" (as a verb), "crucial" | AI register words; say the plain thing |
| "more than people realize" | Filler-adjacent hedge, see rule 4 |

## 8. Restraint is a rule, not a mood

The July pass left the meta description, FAQ, template, mistakes-list content, and section order untouched because no rule fired against them. That's the standard: every edit should be traceable to a named rule in this file or the style guide. If you can't name the rule a sentence breaks, leave the sentence alone. Rewriting for taste creates churn, version noise, and new errors in text that was already working.

## Mechanical spot checks (run before docx build)

- Dashes: `grep -nE "—|–| - " drafts/{file}.md` should return nothing in body copy.
- Echo suspects: `grep -inE "which means|in other words|put simply|ultimately," drafts/{file}.md` and apply the delete test to each hit.
- Register words: `grep -inE "not just|at the end of the day|game.chang|crucial|navigate|landscape" drafts/{file}.md`
- Skim test: `grep -oE "\*\*[^*]+\*\*" drafts/{file}.md` and read the bolds top to bottom. They must still tell the argument after your cuts.
- `python3 scripts/check_style.py drafts/{file}.md` still gates the build, same as always.

## Integration

1. Save this file at `style-guide/editorial-feedback-july-2026.md` in the WSG repo.
2. In `.claude-skill/SKILL.md`, under "Editorial rules from the May 2026 review (mandatory)," add: "Also read `style-guide/editorial-feedback-july-2026.md` (prose-level edit rules: echo enders, burstiness, perplexity). These apply to every draft and every revision pass."
3. In `.claude-skill/consulting.md`, add the same file to the mandatory reading list after `style-guide/editorial-feedback-may-2026.md`.
4. Optional, later: add warnings-only checks to `check_style.py` for the grep patterns above (dash detection, echo-opener detection, paragraph-length variance). Warnings, not hard fails. Echo detection needs human judgment per rule 1, and a hard fail would push writers to game the detector instead of reading their own sections.
