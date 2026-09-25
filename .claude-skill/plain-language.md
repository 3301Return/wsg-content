---
name: plain-language
description: "Break technical or complex material down into plain English a sharp high schooler could follow, without dumbing it down. Auto-applies to WSG article drafts; use on any writing when asked to simplify or fix jargon-heavy, oddly worded passages."
---

# Plain Language

Complex topics are fine. Complex sentences are not. This skill makes sure any technical idea in a draft (a covenant-lite loan, an EBITDA add-back, a MECE issue tree, a DCF terminal value) lands with a reader who is smart but has never seen the mechanism before.

The bar: **a sharp high schooler could read the passage once and explain it back to a friend.** Not because the topic was avoided, but because it was actually explained.

## When this runs

- Automatically on every WSG article: after the first full draft, and again on every revision pass, before the prose-editing pass.
- On request for anything else the user is writing (essays, study guides, explainers, emails, internal docs).

## The three tests, applied to every paragraph that touches a technical idea

Run them in order. Rewrite the paragraph until all three pass.

**1. The term test.** Every technical term the reader might not already know gets a plain-words explanation the first time it appears, in the same sentence or the one right after. Not a dictionary definition. Say what it does and why it matters here.

> Not: "Covenant-lite loans lack maintenance covenants."
> Yes: "Covenant-lite loans skip the regular financial check-ins that older loans required. The borrower doesn't have to prove every quarter that its earnings still cover its debt, so lenders find out about trouble later than they used to."

The reconciliation with the WSG "no basic definitions" rule: **the reader knows the field exists; they don't know how the machinery works.** Don't explain what investment banking is or what an internship is. Do explain what a leveraged loan actually does, what "sponsor-backed" means in practice, or why a market-sizing case cares about the top-down vs bottom-up choice. Define the machinery, never the field.

**2. The syntax test.** Read the sentence out loud. If it would sound odd spoken to a friend across a table, rewrite it. Specific things to catch:

- Stacked noun phrases ("post-close leverage covenant compliance risk"). Unstack them into a short sentence with a verb.
- Sentences carrying more than one idea. Split them. One idea per sentence is the default for anything technical.
- Passive voice that hides who does what ("the debt is refinanced"). Say who: "the company refinances the debt."
- Nominalizations ("the utilization of," "the implementation of"). Use the verb: "using," "putting in place."
- Inverted or literary word order ("Rare is the analyst who..."). Put it back in normal order.
- Latinate or register words where a plain one exists: utilize → use, facilitate → help, leverage (verb) → use, commence → start, subsequent to → after, in order to → to, prior to → before, with respect to → about, constitutes → is.
- Abstract subjects ("The dynamics of the process suggest..."). Make a person, firm, or thing the subject.

**3. The walk-through test.** For any mechanism or process, the reader must be able to follow the chain from cause to effect without filling in a step themselves. If a paragraph says A leads to C, write B. Use a concrete example with real-feeling numbers whenever the idea involves quantities, ratios, or timing.

> Not: "Higher rates compress LBO returns."
> Yes: "Say a private equity firm buys a company for $500 million and borrows $300 million of it. If the interest rate on that debt goes from 6 percent to 9 percent, the company now pays $27 million a year in interest instead of $18 million. That extra $9 million comes straight out of the cash the firm was counting on to pay down the loan, so the deal earns less by the time they sell."

## What this skill does not do

- It does not remove the topic or make it shallow. Simplifying the words never means cutting the substance. If the plain version is longer than the original, that is normal and expected.
- It does not make the writing childish. No "Imagine you have a lemonade stand" framings unless the topic is genuinely being taught from zero. Analogies are welcome when they fit; forced analogies are worse than none.
- It does not touch quotes, formulas, code, or the exact wording of named programs, titles, and legal terms.
- It does not override voice. Contractions, first person, specifics, and opinion all stay. Plain is a floor for clarity, not a ceiling on personality.

## Working through a draft

1. Skim the draft and mark every paragraph that contains a technical term, a mechanism, a process, or a number that depends on a mechanism.
2. For each marked paragraph, run the three tests. Rewrite in place.
3. Re-read the rewritten paragraph out loud once. If any sentence is over about 30 words and carries a technical idea, split it.
4. Read the bolded sentences alone (WSG skim test). They must still read as plain, self-contained claims after the rewrite.
5. If a term appears again later in the piece, do not re-explain it. One explanation, at first use, is enough.

## Quick reference: the sniff test for "weird syntax"

If any of these are true, the sentence needs work:

- You had to read it twice.
- The verb is more than eight words away from its subject.
- It contains a word you would not say out loud to a student.
- It uses a colon, semicolon, or parenthetical to hold a second idea that deserves its own sentence.
- The sentence explains a term by using another term the reader also might not know.

## Pairing with other skills

- Runs before `wsg-prose-editing` / the wsg-article `prose-editing.md` pass, so the prose pass edits plain sentences rather than fighting jargon.
- Runs alongside `thorough-explanations`, which checks that no step is skipped. Plain language makes each step readable; thoroughness makes sure every step is present.
- Never introduces em dashes or en dashes. Split with a period or use a comma or colon.