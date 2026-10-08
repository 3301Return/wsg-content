---
name: thorough-explanations
description: Catch and fix "jumpy" or over-condensed explanations in articles and drafts, where a technical question or concept skips steps, compresses several ideas into one sentence, or answers in a summary when the reader needed the full walk-through, while keeping WSG articles near their length target. Auto-applies to every WallStreetGuide (WSG) article draft and revision and appends a Thoroughness Report after delivery. Use on any other draft when the user says an explanation feels rushed, jumps around, is too condensed, or needs to be more thorough.
---

# Thorough Explanations

The failure this skill exists for: a draft explains a technical question or concept, and the explanation *jumps*. It states a conclusion without the steps that got there, compresses three ideas into one sentence, or answers a "how does X work" question with a one-line summary and moves on.

The rule: **an explanation is done when the reader could act on it or teach it, not when the writer has mentioned it.**

The October 2026 counterweight: **complete is not the same as long.** Recent WSG drafts ran about 35 pages, and Sanskar's target is about 20 to 25 pages before images (SKILL.md has the word ranges). A thorough article explains each mechanism once, fully, and then moves on. It doesn't explain it three times with three worked examples, and it doesn't wrap every section in a recap.

## When this runs

- Automatically on every WSG article: after the plain-language pass, before the prose-editing pass. Again on every revision.
- On request for any other draft.
- **The fail-safe (mandatory on WSG articles):** after the article is delivered, append the Thoroughness Report (format below).

## What "jumpy" and "over-condensed" look like

**Jumps (missing steps)**

- A sentence goes from cause to effect with no mechanism. "Rising rates hurt LBO returns." How?
- A process is named but not walked. "Run the comps, then triangulate."
- A "why" is asserted, not shown. "Banks prefer sophomores who network early."
- A term of art is used as if it were the explanation. "Because of the waterfall."
- An H2 sub-question answered in one sentence when it needed three or four.
- A heading promises a how-to and the body delivers a what.

**Over-condensation (steps present but crushed)**

- One sentence carrying three ideas joined by commas or "and."
- A bolded claim doing the whole job of a paragraph, with no support under it.
- A numbered list where each item is a label, not an explanation.
- A worked example that names the inputs and the result but skips the arithmetic.
- A comparison that gives the verdict without the two or three axes it was decided on.

## What "bloated" looks like (October 2026)

These are the opposite failure. They add length without adding a step.

- The same mechanism worked twice with different numbers.
- A table and a paragraph saying the same thing.
- A section that ends by restating what the section said.
- An "honest read," "the trade-off" or "what this means for you" section that repeats earlier sections.
- Background the reader didn't come for (a firm's founding story at full length, every deal of the year).
- A closing section that summarizes the article.

## The fix, in order

For each jumpy or crushed passage:

1. **Name the question the passage is really answering.** One line, for yourself.
2. **List the steps a reader needs** to get from the question to the answer. Usually three to six. If you can't list them, research before expanding.
3. **Write each step as its own sentence or short paragraph.** One idea per sentence for anything technical. One concrete example with plausible numbers when quantities are involved.
4. **Check the chain.** At every sentence: could the reader have predicted this from the one before? If there's a gap, add the bridge.
5. **Keep the bolded claim**, and make sure the text under it now earns it.

Then **pay for it.** For every passage you expand, look for bloat (list above) in the same section or elsewhere and cut it. The goal is a complete article near the target length, not a complete article that's 40 pages.

Expanding is not padding. Padding restates; expanding adds a step, a reason, a number, or an example that wasn't there.

## What this skill protects

- The WSG skim narrative: bolded sentences stay self-contained full sentences, and the bold-only read still tells the argument.
- Intros stay short (`intros.md`). This skill works on the body only.
- Listicle items keep their bullet structure. Expansion goes into the description and the takeaway, not into a wall of prose per item.
- Prose editing still runs afterward (`prose-editing.md`), including rule 16, the length cut. It cuts repetition and side material; it never cuts a step this pass added.

## The fail-safe: Thoroughness Report

After delivering any WSG article, append this report in the chat after the file. Keep it short.

```
Thoroughness Report
- Expanded before delivery: {N} passages
  - {section or H2}: {what was jumpy and what was added}
- Cut for length: {N} passages
  - {section}: {what was cut}
- Still thin (needs a source, a number, or the user's input): {N}
  - {section}: {what's missing and why it couldn't be filled}
- Plain-language rewrites: {N} paragraphs (terms explained at first use: {term, term, term})
- Word count: {final} (target for this format: {range}; about {pages} pages before images)
- Over target? {no | yes, because ...}
```

Post it with zeros if nothing was expanded or cut. A missing report means the check didn't run.

"Still thin" entries are the important ones: passages that can't be fixed without information Claude doesn't have (a real deadline, a comp number). Never paper over a thin spot with filler. Flag it and let the user decide.

## Pairing with other skills

- `plain-language` runs first and makes each explanation readable. This skill makes sure each explanation is complete, once.
- The wsg-article package's `prose-editing.md` runs after both.
- Outside WSG, use the user's own length guidance; if there is none, the expand-then-pay rule still applies.
