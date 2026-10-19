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


## 17. Stay in the article's own field (October 12, 2026)

Sanskar's flag on the consulting resume draft: it opened its skeleton by comparing consulting resumes with banking resumes, and a later paragraph said "students treat a consulting resume as a banking resume with the order changed." His note: "a bug in the system where a lot of consulting banking becomes interlinked... deflecting the point into banking resume opposed to explaining what is actually the issue."

A consulting article explains consulting. A banking article explains banking. Don't explain one by contrasting it with the other ("unlike banking," "a banker would," "the banking version of this"). Explain the thing directly.

A comparison belongs in an article only when the reader is choosing between the two (salary, hours, "consulting vs banking"), and then once, in its own clearly labeled section or sub-question, kept short. Nowhere else.

## 18. No history or trivia the reader can't act on (October 12, 2026)

Flagged: a consulting resume paragraph built on Leonardo da Vinci's 1482 letter to Ludovico Sforza as "the earliest known resume." Reaction: "🤢."

Cut founding dates, reorganization timelines, who coined a term and when, "the earliest known," famous-person anecdotes, and firm-level revenue and headcount in articles about a junior role. **The test:** if a student deleted the sentence, would they do anything differently? If not, it goes. A one-clause attribution ("the pyramid principle, from Barbara Minto's book") is fine. A biography isn't.

## 19. Say what to do, not why the firm does it (October 12, 2026)

Flagged: a section that opened "Start on the firm's side of the table. McKinsey receives roughly 1 million resumes annually... The resume screen exists to get the stack down to the people worth 45 minutes of a consultant's time." Sanskar: "the student doesn't need the 'why' behind resume screenings."

Cut firm-side setups ("start on the firm's side," "the screen exists to," "the firm is trying to," "to understand X you have to understand why firms...") and application-volume statistics used to justify a process. Give the student the what and the how. Keep a "why" only when it changes what the student does, and then as one clause attached to the instruction ("Put GPA on its own line, because the screener checks it first").

This narrows the older "lead with the company's perspective" rule (SKILL.md editorial rule 4), which was being over-applied.

## 20. Judge every section against the headline (October 12, 2026)

The founder's note on the same batch: "the process just seems like it's following instructions too much without using its own intelligence." Templates, briefs and outlines list sections that might help. They're not a checklist.

Before delivering, give every H2 a verdict: keep, cut, shrink or rewrite. **The question:** does a student reading this headline need this section to do what the headline promises? Background sections, "how this differs from X" sections, tables that repeat the prose, and closers that recap all fail it. Cut them or fold their one useful fact into a section that passes. Shorter is fine when the topic is covered; never pad back to the length target.


## 21. Conversational, not absolute (October 14, 2026)

The founder: "The writing is still a little AI-y and absolute in places. Things like 'five stories cover every behavioural question' or making very definite statements about how recruiters score candidates aren't really the tone we're going for, and aren't necessarily true in every case... Whenever it sounds like a Nat Geo narrator, that's an issue."

Recruiting varies by firm, office, team, interviewer and year. Write like someone who knows the field talking to a student: "usually," "often," "most firms," "some banks," "in most first rounds," "a common approach is." Use a qualifier where it's true, not on every sentence; a plain fact ("Goldman's first round is a HireVue") stays plain.

| Cut this | Write this |
| --- | --- |
| "Five stories cover every behavioral question." | "Five stories usually cover most of what you'll be asked." |
| "The interviewer is scoring Partnership." | "A Goldman interviewer will often be listening for teamwork." |
| "Banks score your answers against a rubric." | "Many banks use a set list of qualities when they review answers." |
| "That's the format at the banks." | "That's how most large banks run it." |
| "Every one of the six fixes can be run in ten minutes." | "Most of these fixes take a few minutes on a written story." |

Narrator voice is a sentence that pronounces on how the world works from above: sweeping, certain, slightly dramatic. "The structure has to be automatic by the time the question appears." "A smaller true story beats a bigger invented one." "This is how influence works inside a bank." Say it as advice instead: "It helps to have the structure down before the first question." Bolded sentences follow the same rule.

## 22. Say each point once, and teach the doing, not the system (October 14, 2026)

The founder on the STAR draft: "we've spent so much time explaining how banks score interviews, the research behind structured interviews... does a student really need all of that to learn how to give a better STAR answer?" And: "eight full sample answers, explanations after each, a table mapping 19 questions, and then another 'say this, don't say that' section... the student should get the meat of it quicker."

Two failures, one fix each:

- **Explaining the system.** How firms score, what the research says, why a method exists, how a process works behind the scenes. If the reader's goal is to do something (give an answer, apply, pass a test), the system gets two lines at most. The words go to the doing.
- **Repeating a point in several formats.** An example, then an explanation of the example, then a table, then a say/don't block, all landing the same lesson. Pick the one format that teaches it fastest. Three or four sample answers that each show something different beat eight that show the same shape. A short note after an example is fine only when it adds what the example doesn't show.

Also: no two sections with the same purpose. If section 1 explains why the Action matters and section 6 has a mistake about the Action, merge them.

## 23. Match the reader's level (October 14, 2026)

The founder: "The Accenture article goes into Managing Director salaries; for someone looking at an entry-level Analyst role, I don't think all of that is necessary."

Cover the reader's seat in detail. Anything above or beside it gets a line: "Consultants (two to three years in) earn about $X; pay rises from there." A full pay ladder, a senior career path or partner economics belongs in an article about those roles.

## 24. Keep examples in proportion (October 14, 2026)

The founder: "multiple pages going across the kitchen cabinet case doesn't make sense as this isn't the interview or how-to-break-in guide; we can keep it sure, but like 1 page."

A worked example illustrates the section it sits in. In a career or role guide, a practice case or sample answer runs about a page. In an article whose whole question is that example (a case interview guide, a sample-answers article), it can run longer. Size the example to the article's question, not to how much there is to say about it.
