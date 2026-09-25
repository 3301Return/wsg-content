---
name: wsg-prose-editing
description: Prose-level editing rules from the WSG July 2026 editorial review, plus the September 2026 "say it out loud" diction test. Use when writing, editing, or reviewing WallStreetGuide (WSG) articles or any draft that should not read as AI-written. Trigger on requests to cut AI tells, remove echo sentences or em-dashes, humanize a draft, improve sentence variety, fix odd or off-register wording, or apply burstiness and perplexity principles to writing.
---

# WSG Prose Editing

Pruning and variance rules from the July 2026 editorial review. They layer on top of the WSG style guide when working in the WSG repo, and stand alone for any other prose. They tell you what to cut and how to vary, not how to restructure. The WSG format itself (bolded skim narrative, H2 sub-questions, say/don't blocks) stays exactly as specified in the main skill.

Canonical repo copy: `style-guide/editorial-rules.md` Part 2. This module is the packaged mirror so the rules travel with the skill; edit the repo copy first, then re-mirror here and repackage.

Source: the July 12, 2026 edit pass on the consulting cover letter draft. These rules layer on top of `style-guide/style-guide.md` (especially the AI sniff test section) and the May 2026 editorial protocol (`style-guide/editorial-rules.md` Part 1). Every existing rule still applies.

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

## 9. The "say it out loud" test (September 2026, from the Aug 27 founder review)

Every sentence in the article, not just the intro, has to pass one test: **would Stephen say this sentence out loud to a student across a table?** If not, write the plain version. This catches a class of problem the AI-register list in rule 7 misses: sentences that are not filler and not clichés, but that sound written rather than said.

Real lines flagged and removed in the August 27 batch, with the reason:

| Cut this | Why |
| --- | --- |
| "That's the headline." | Nobody talks like this. |
| "the caveats the recruiting brochures leave out" | Nobody hands out brochures. Odd object, odd rhythm. |
| "before counting retirement money" | Unclear and strange. Say "before the 401(k) match" or cut it. |
| "life happens in deposits," "which kind of tired you want to be," "the smallest interesting number" | Copywriter lines. They sound written, not said. |
| "the interview's real center of gravity," "reads as a future engagement summary," "pressure-tested for your fingerprint" | Metaphor stacked on metaphor. Say the plain thing. |
| "in every way that counts," "an embarrassment of material," "no faking automatic," "choosing on noise," "holdouts need dragging," "case clock," "cheap homework," "mental math under a clock" | Off-register, compressed, or cute. Plain version every time. |
| "Rent is not national." | A fragment pretending to be an insight. Say what you mean. |

The pattern: a phrase that reads as clever on the page but that no one would say in conversation. The fix follows rule 4: replace it with something concrete (a number, a name, a mechanism), not with a safer cliché.

Two related checks from the same review:

- **No fake-precise effort counts.** "Ran 47 practice cases," "two hundred flashcards," "40 hours of Moyer" read as invented. Use roundable language ("a semester of cases," "a fall working through Moyer"). Real outcome numbers stay.
- **WSG never looks bad in its own stories.** Setbacks happen before someone finds WSG, or to a roommate or friend. Students advised by WSG win. Full rules for openings are in `intros.md`.

Spot check: read the article aloud once, start to finish. Every sentence you stumble on or would rephrase mid-sentence gets rewritten.

## Mechanical spot checks (run before docx build)

- Dashes: `grep -nE "—|–| - " drafts/{file}.md` should return nothing in body copy.
- Echo suspects: `grep -inE "which means|in other words|put simply|ultimately," drafts/{file}.md` and apply the delete test to each hit.
- Register words: `grep -inE "not just|at the end of the day|game.chang|crucial|navigate|landscape" drafts/{file}.md`
- Say-it-out-loud suspects: `grep -inE "the headline|brochure|retirement money|center of gravity|in every way that counts|case clock|cheap homework|under a clock" drafts/{file}.md` and apply rule 9 to each hit (the list is a starting point, not the whole rule).
- Effort counts: `grep -nE "\b[0-9]{2,3} (practice )?(cases|flashcards|mocks|hours)" drafts/{file}.md` and round anything that reads as invented.
- Skim test: `grep -oE "\*\*[^*]+\*\*" drafts/{file}.md` and read the bolds top to bottom. They must still tell the argument after your cuts.
- `python3 scripts/check_style.py drafts/{file}.md` still gates the build, same as always.

## Where these rules live

1. This file (`style-guide/editorial-rules.md`, Part 2) is the canonical copy.
2. The packaged wsg-article skill carries the same rules as its `prose-editing.md` module so they travel with the skill outside the repo. Edit here first, then mirror into `.claude-skill/prose-editing.md` and repackage `skills/wsg-article.skill`.
3. `python3 scripts/check_style.py drafts/{file}.md` still gates every build. Optional, later: add warnings-only greps to `check_style.py` for dash detection, echo-opener detection, and paragraph-length variance. Warnings, not hard fails — echo detection needs human judgment per rule 1.
