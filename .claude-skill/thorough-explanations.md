---
name: thorough-explanations
description: "Catch and fix jumpy or over-condensed explanations that skip steps or crush ideas together, expand them, and append a Thoroughness Report after every WSG article delivery. Use on any draft that feels rushed or too condensed."
---

# Thorough Explanations

The failure this skill exists for: a draft explains a technical question or concept, and the explanation *jumps*. It states a conclusion without the steps that got there, compresses three ideas into one sentence, or answers a "how does X work" question with a one-line summary and moves on. The reader is left doing the work the article was supposed to do.

The rule: **an explanation is done when the reader could act on it or teach it, not when the writer has mentioned it.** If that takes more words, it takes more words. Word counts are guidelines, never a reason to cut a step.

## When this runs

- Automatically on every WSG article: after the plain-language pass, before the prose-editing pass. It runs again on every revision.
- On request for any other draft.
- **The fail-safe (mandatory on WSG articles):** after the article is delivered, append a short Thoroughness Report (format below). No article ships without one.

## What "jumpy" and "over-condensed" look like

Scan for these. Any hit is a candidate for expansion.

**Jumps (missing steps)**

- A sentence goes from cause to effect with no mechanism. "Rising rates hurt LBO returns." How? Through what?
- A process is named but not walked. "Run the comps, then triangulate." Which steps, in what order, what decisions along the way?
- A "why" is asserted, not shown. "Banks prefer sophomores who network early." The reader needs the reason banks care.
- A term of art is used as if it were the explanation. "Because of the waterfall." The waterfall is the thing that needs explaining.
- The answer to an H2 sub-question is a single sentence when the question deserved three or four.
- A section heading promises a how-to and the body delivers a what.

**Over-condensation (steps present but crushed)**

- One sentence carrying three ideas joined by commas or "and."
- A bolded claim doing the whole job of a paragraph, with no support under it.
- A numbered list where each item is a label, not an explanation ("3. Understand the deal.").
- A worked example that names the inputs and the result but skips the arithmetic in between.
- "In short" or "simply put" closing a paragraph that was already short.
- A comparison ("X vs Y") that gives the verdict without the two or three axes it was decided on.

## The fix, in order

For each flagged passage:

1. **Name the question the passage is really answering.** Write it in one line for yourself ("How does a cov-lite structure change what a lender knows and when?").
2. **List the steps a reader needs to get from the question to the answer.** Usually three to six. If you can't list them, you don't understand it well enough to write it; research before expanding.
3. **Write each step as its own sentence or short paragraph.** One idea per sentence for anything technical. Use a concrete example with plausible numbers when quantities are involved.
4. **Check the chain.** Read the expanded passage and ask at every sentence: could the reader have predicted this sentence from the one before? If there's a gap, add the bridge.
5. **Keep the bolded claim**, but make sure the text under it now earns it.

Expanding is not padding. Padding restates; expanding adds a step, a reason, a number, or an example that wasn't there. The test for every added sentence: does it carry something the reader didn't have? If not, cut it.

## What this skill protects

- The WSG skim narrative: bolded sentences stay self-contained claims, and reading only the bolds must still tell the argument.
- Intros stay tight. This skill expands the body, not the opening. Intros keep their 1-2 short paragraphs.
- Listicle items keep their bullet structure. Expansion in a listicle goes into the description and the takeaway, not into a wall of prose per item.
- The prose-editing rules still apply afterwards: no echo enders, no em dashes, burstiness, perplexity. Thoroughness adds substance; prose editing then trims fat. They are not in conflict.

## The fail-safe: Thoroughness Report

After delivering any WSG article (and any other draft where this skill was invoked), append this report in the chat, after the file link. Keep it short. The point is that the user sees at a glance whether anything is still thin.

```
Thoroughness Report
- Expanded before delivery: {N} passages
  - {section or H2}: {one line on what was jumpy and what was added}
  - ...
- Still thin (needs a source, a number, or the user's input): {N}
  - {section}: {what's missing and why it couldn't be filled}
- Plain-language rewrites: {N} paragraphs (terms explained at first use: {term, term, term})
- Word count: {final} (guideline for this format: {range}; over is fine)
```

If nothing was expanded and nothing is thin, still post the report with zeros. A missing report means the check didn't run.

"Still thin" entries are the important ones. They are the passages the skill could not fix without information it doesn't have (a real deadline, a comp number, a scenario from the writer's own experience). Never paper over a thin spot with generic filler to make the list shorter. Flag it and let the user decide.

## Pairing with other skills

- `plain-language` runs first and makes each explanation readable. This skill makes sure each explanation is complete. Run both on every technical passage.
- The wsg-article package's `prose-editing.md` runs after both, on the expanded draft.
- `check_article.py` reports word count as info only (no upper cap, September 2026). A "below guideline" warning from that script is a prompt to look for skipped steps, not a prompt to pad.