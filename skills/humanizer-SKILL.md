---
name: humanizer
description: Rewrite AI-sounding prose so it reads like a person wrote it, without changing what it says. Use when the user says humanize, de-AI, make this sound human, remove AI tells, this reads like ChatGPT, or asks to clean AI voice out of an article, draft, essay, email, report, documentation, or web copy. Handles inflated significance claims, sales language, vague attribution, shallow -ing analysis, stock AI vocabulary, forced triads, false depth, filler, and chatbot artifacts. Not for code, and not for stripping required AI-use disclosures.
license: MIT
metadata:
  version: "3.0.0"
---

# Humanizer

Rewrite text so it stops reading as machine-generated. Keep every fact. Invent nothing.

Pattern catalogue derived from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup), merged with a field-tested pattern set covering modern LLM prose habits the Wikipedia guide does not yet catalogue.

## The governing principle: cut, don't swap

Most AI tells are **additions**, padding the model bolted on: significance claims, shallow analysis, puffery, manufactured depth. They carry no information from the source.

So the default move is deletion, and it gives a clean decision procedure:

> Delete the flagged span. Did a fact disappear?
> **No** → it was padding. Leave it deleted.
> **Yes** → restate that fact in the plainest form available.

This is what makes "remove AI tells" compatible with "add nothing new" and "keep every fact." Synonym-swapping fails both, it keeps the padding and re-dresses it. `pivotal role` → `crucial role` is not an edit.

The corollary matters as much. Surface tells usually sit on a **real writing defect**: an unsupported inference, a vague attribution, a claim no source carries, a sentence that asserts nothing. Fix the defect. Sanding off the wording while leaving the defect hides the problem instead of solving it, and the prose is still empty. That is the difference between editing and laundering.

## Workflow

1. **Scope it.** Identify the prose readers will see. Protect byte-for-byte: code and fences, commands, paths, URLs, identifiers, formulas, exact figures, citations, and anything quoted verbatim. Never rewrite a watched phrase that appears inside a quotation, title, proper name, or an example discussing the phrase rather than using it.
2. **Match the writer, if you can.** If the user supplied a writing sample, read it first, see [Voice](#voice). A real sample overrides every default in this skill.
3. **Strip machine artifacts.** Mechanical, no judgment: `oai_citation`, `turn0search0`, `[cite: 1]`, `(start_span)`, `grok_card`, `【85†…】`, `[attached_file:1]`, `utm_source=chatgpt.com`, unfilled `[Placeholder]` slots. Table in `references/artifacts.md`. Zero meaning, so removal cannot cost a fact.
4. **Scan.** Run `scripts/scan.py` for a density read. It finds candidates. You decide.
5. **Diagnose before rewriting.** Per hit: is there a fact here, or only decoration? Is an inference being asserted that no source supports?
6. **Cut the padding.** Apply the decision procedure. Delete unsupported analysis outright, do not rewrite it into subtler unsupported analysis.
7. **Restore plain syntax.** Put back what LLMs avoid (`references/restore.md`): `is`/`are`, `wrote` not `authored`, `has` not `boasts`.
8. **Fix the rhythm.** AI output is metronomic. Vary sentence length by **cutting**, never by padding.
9. **Verify.** Read the draft aloud, then ask two questions and treat either answer as an error:
   - *What still sounds AI-generated?*
   - *Did the rewrite add or lose any fact, name, number, date, quote, citation, or ranking?*
10. **Report.** Say what you cut and why. Flag anything a reader might consider a fact that you changed.

Write the final version by stating each point naturally, not by patching flagged phrases one at a time. If a sentence stays awkward, rewrite the paragraph around its main point.

## Voice

**With a sample** (the user's own earlier writing): read it before rewriting. Note sentence length, word choice, paragraph openings, punctuation, recurring phrases, transitions. Match those habits. Do not formalize casual words or sand off deliberate quirks. A sample overrides the default style guidance here, except the dash ban, which holds unless the user explicitly says to keep their dashes.

**Without a sample:** infer register from the text itself and hold it.

**Personality** belongs in blog posts, essays, opinion, and personal writing. Keep reference, technical, legal, and factual text neutral. Where personality fits, preserve the writer's opinions, uncertainty, mixed feelings, humor, asides, and uneven rhythm, but never invent a fact to manufacture warmth. You may add a reaction the writer's voice calls for; you may not add a claim.

## Output modes

- **Pasted text (default).** Return the rewrite, plus a short note on what you cut and anything still weak.
- **File mode.** When a file is named, run the full process but write only the final text. Prose only, leave code blocks, front matter, data, and link targets untouched. Then summarize.
- **Embedded mode.** When another task calls this skill (PR body, commit message, doc), return only the final text.

## The five highest-yield cuts

Full catalogue with before/after pairs in `references/patterns.md`.

**1. Inflated significance.** `stands/serves as a testament to`, `marking a pivotal moment`, `underscores its importance`, `reflects broader`, `evolving landscape`. Ordinary details asserted to prove a legacy. Almost always pure addition.

**2. Shallow `-ing` analysis.** A real fact, a comma, then a participial clause interpreting it: *"The station opened in 1884, **cementing its role as a regional hub**."* The tail is the model's inference. Delete it, keep the sentence.

**3. Sales register.** `nestled`, `in the heart of`, `boasts`, `vibrant`, `rich cultural heritage`, `renowned`, `breathtaking`. Replace with the specific fact, or cut.

**4. Vague attribution.** `experts argue`, `observers have noted`, `industry reports suggest`, `widely regarded as`. Name the real source or cut the claim. Never leave the weasel.

**5. Manufactured depth.** `at its core`, `the real question is`, `what really matters`, `X is the language of Y`, `Honestly?`, `Let's dive in`. Ordinary points dressed as revelations. State the point.

## Aggression setting

**Cut aggressively.** When a pattern in `references/patterns.md` is arguably present, remove it. A false positive on a stylistic pattern costs a slightly plainer sentence; a false negative leaves the draft reading like a chatbot. Prefer the plainer sentence.

This applies to *removable style*: dashes, triads, negative parallelism, curly quotes, decorative bold, emoji, title case, filler, hedge stacking, false depth, staged openers. Strip them by default and do not agonize.

It does **not** license three things, because these make the writing worse rather than plainer:

- Anything on the not-a-tell list in `references/do-not-overcorrect.md`. Formal diction, clean grammar, and ordinary transitions are not AI markers, and flattening them damages good prose without removing a tell.
- Losing or inventing a fact. The hard constraints below are absolute at every aggression level.
- Faking humanity with planted errors, tics, or padding.

### The dash rule

**No em dashes (`—` U+2014) or en dashes (`–` U+2013) in the output.** Before returning, search for both characters and remove every one.

- **Em dash in prose** → period, comma, colon, semicolon, or parentheses, or recast the sentence.
- **Spaced dashes (` — `, ` – `) and double hyphens (` -- `)** → same treatment.
- **En dash in a number, date, score, or page range** → plain hyphen. `pp. 12–15` becomes `pp. 12-15`, `1914–18` becomes `1914-18`. Never a comma or period here; that changes the value.
- **En dash joining names** (`Tokyo–Osaka line`) → hyphen.

Exception: dashes inside quoted material, titles, or proper names stay. You do not edit a quotation.

## Hard constraints

- **Never invent.** No new fact, name, number, date, quote, citation, or causal claim unless it comes from the source or the user. If a sentence needs a detail you lack, ask, or write a simpler sentence. (Fiction is exempt, invented detail is the task.)
- **Never delete a fact to remove a tell.** Restate it plainly. You may shorten dull passages, expand useful ones, and merge or split paragraphs, the information survives the restructuring.
- **Never fake humanity.** No planted typos, no injected errors, no forced slang, no hedges the writer did not write. These degrade the work, and added hedges violate "add nothing" outright.
- **Never alter text encoding to defeat detection.** Swapping in Unicode lookalike spaces or zero-width characters changes no words, improves no sentence, and breaks search, copy-paste, screen readers, and diffs. It is sabotage of the document, not editing.
- **Preserve the English variety.** Several models default to American English, so drafts drift mid-document. Detect the variety from the author's own text, not the topic, and make the piece consistent. Never flip a deliberately British, Australian, Canadian, or Indian draft.
- **Preserve required disclosures.** Academic, legal, platform, and regulatory disclosure of AI assistance stays. This skill improves prose; it does not defeat a disclosure obligation, and a cleaner draft is not a human-authored one.
- **Prose only.** Never rename a variable, alter a string literal, or reformat code.

## References

- `references/patterns.md`, full catalogue, ~40 patterns, each with before/after
- `references/do-not-overcorrect.md`, **read this**; over-correction is this skill's failure mode
- `references/restore.md`, what to put back, not just what to remove
- `references/artifacts.md`, machine residue, by vendor

## Scanner

```bash
python C:/Users/Alex/.claude/skills/humanizer/scripts/scan.py DRAFT.md
```

`--json` for machine-readable output, `-` for stdin, `--top N` to cap listings per category.

A high score means "look here," not "this is AI." A low score clears nothing, the deepest tell, prose that asserts nothing, has no keyword signature. Judge the writing, not the score.

## Related skills

Invisible Unicode, curly quotes, and non-breaking spaces are encoding concerns, handled by `clean-user-facing-text`. Chain it after this one before publication.

## Attribution

Pattern set merged from a community `humanizer` skill (MIT) and Wikipedia:Signs of AI writing (CC BY-SA 4.0), with corrections noted in `references/do-not-overcorrect.md`.
