# QA instructions: October 11, 2026 IB batch

You are the independent second pair of eyes on one WSG draft. You did not write it. Work from `/home/claude/repo`. Today is Sunday, October 11, 2026. Edit the draft in place (same v1 file) with surgical changes; never rewrite sections for taste. Every edit traces to a rule or a verified fact.

## 1. Read first

1. `.claude-skill/SKILL.md`: the October 8 and October 7 rules at the top, the hard rules, the recruiting timeline math section, the VERIFY protocol.
2. `.claude-skill/intros.md`, `.claude-skill/prose-editing.md` (rules 1 to 16 and the mechanical spot checks), `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md`, `.claude-skill/source-verification.md`, `.claude-skill/reference-articles.md`.
3. `style-guide/recruiting-timeline-glossary.md` if the draft mentions any recruiting year.
4. The humanizer skill: `/root/.claude/skills/synced/37fa8fbb-96dc-473e-ae57-5dce92d68ec3_c2846f6b-18df-4d08-a8e7-8471d3775030/humanizer/SKILL.md`.
5. The draft, in full, twice: once as a reader, once as an auditor.
6. The fact sheet the writer used: `claude/research/{slug}.md`. The writer's report (pasted in your prompt) lists the facts it fetched beyond the sheet and the spots it called thin.

## 2. Verify (the part that matters most)

- Pick every fact a reader could act on or quote: numbers, dates, deadlines, rates, pay, program names, quotes, firm process claims. Re-open at least 15 of them at the primary source with WebFetch (firm page, help-center article, filing, the named article). Confirm the draft states them exactly. Fix any drift (a number rounded the wrong way, a date off by a day, a quote paraphrased inside quote marks, a claim attributed to the wrong source, a "typically" that the source states as a one-time report).
- Recompute every calculation in Python (percentages, ratios, worked examples, word splits, time splits). Fix prose, tables and bolds together so they agree.
- Recruiting years: check every sentence with a year against the glossary (application year 2027 with a fall 2026 first wave, internship Summer 2028, graduation 2029; sophomore-summer programs run on their own math).
- Quotes: anything inside quotation marks must be verbatim from the source. If you can't confirm it, remove the quote marks and paraphrase, or cut it.
- Named entities: every firm, program, person, publication and tool outside the Tier 1 list must exist with the description the draft gives. Confirm each one you haven't seen before. Remove any you can't confirm.
- Conflicts: where sources disagree, the draft gives a range or says "reported" and carries a `[VERIFY: ...]` tag. Don't resolve a conflict by picking one.
- Add `[VERIFY: ...]` tags where a moving fact lacks one; remove tags that sit on stable facts.

## 3. Editorial audit

- Intro: first sentence answers the headline with the keyword; a bolded full-sentence fact; last sentence says what the article covers; two to five sentences; no story, no opinion about readers, no bio.
- Headers read alone: plain, literal; numbered insights are short plain claims (under 12 words); questions end with "?"; nothing clever.
- Bolds: `grep -oE "\*\*[^*]+\*\*"` and read them top to bottom. Each is a full sentence with a fact or rule, and together they tell the argument. Every H2 section has at least one.
- Prose rules 1 to 16: echo enders, dashes, lists vs prose, burstiness, register words, say-it-out-loud, no negatives about the writer or WSG or the reader, no unsupported "most candidates" opinions, length cut order.
- Plain language: every technical term explained at first use in plain words; one idea per sentence in technical passages; no stacked noun phrases; no cause-to-effect jumps.
- Thoroughness: any process named but not walked, any worked example missing a step, any sub-question answered in one line. Expand within the length target; pay for it by cutting repetition.
- Humanizer: inflated significance, sales words, vague attribution ("experts say"), shallow "-ing" tails, stock vocabulary, forced triads, filler, chatbot artifacts. Keep facts and voice.
- Sample text (say/don't lines, worked answers) is edited hardest: concrete, no throat-clearing, no triads.
- Contractions in prose. "Investment Banking Summer Analyst" capitalized as the role title.
- Links: inline anchors only; no rotating job postings; internal WSG links go to live posts (list in `claude/wsg-live-urls-oct-11-2026.txt`).

## 4. Gates after your edits (fix and re-run until clean)

```
python3 scripts/check_article.py drafts/draft-{slug}-v1.md   # PASS; read warnings
python3 scripts/check_style.py drafts/draft-{slug}-v1.md     # exit 0 ("TOO CHUNKY" acceptable on question-listicle items)
python3 scripts/check_links.py drafts/draft-{slug}-v1.md     # all live (some domains block the workspace; if WebFetch shows the page live, unlink it, keep the source named in text, and list it for a click-test at publish)
grep -nP "—|–|−| - " drafts/draft-{slug}-v1.md               # nothing
python3 - << 'EOF'
import re,sys;t=open("drafts/draft-{slug}-v1.md",encoding="utf-8").read()
bad=[(i,c,hex(ord(c))) for i,c in enumerate(t) if ord(c) in (0x200B,0x200C,0x200D,0x2060,0xFEFF,0x00AD,0x2014,0x2013,0x2212)]
print("invisible/dash codepoints:",len(bad))
EOF
wc -w drafts/draft-{slug}-v1.md                              # 5,000 to 6,000 (article 3: up to about 6,500)
```

## 5. Report back (under 600 words)

1. Facts re-verified: count, and every correction made (old → new, source).
2. Calculations recomputed: count, and every fix.
3. Editorial edits: each one with the rule it traces to (one line each).
4. Anything still thin or unresolved, for the founder.
5. Links unlinked for a click-test at publish (page name and URL).
6. Final word count, tags count, gate results.

## 6. Founder feedback from October 12 (Sanskar's review of the previous batch; apply to every draft, over any older rule)

1. **Stay on the article's own subject.** The consulting resume draft spent its opening comparing a consulting resume to a banking resume. Sanskar: "it's deflecting the point into banking resume opposed to explaining what is actually the issue." Cut any passage that explains this article's topic by way of an adjacent topic (another product, another seat, another firm's process, another WSG article's subject). A one-clause contrast is fine; a paragraph of comparison is not. Links to other posts stay short.
2. **Cut the "why" the student doesn't need.** The same draft explained how the MBB resume screen scores a resume (volume, "the firm's side of the table," what the screen exists for) and added a Leonardo da Vinci resume history. Sanskar: "the student doesn't need the 'why' behind resume screenings." Delete history, origin stories, firm-perspective rationales, industry background and "here's why this process exists" passages unless the reader needs that fact to act. The reader needs what to do, when, with what numbers. The old "lead with the company's perspective" rule is retired where it produces this kind of passage.
3. **Use judgment, not the checklist.** Sanskar: the process "seems like it's following instructions too much without using its own intelligence." Where a rule in a module produces a passage a sharp student would skip, cut the passage. Don't add a section because a template lists it; don't keep a worked example because a rule says one per mechanism if the point is already clear.

For this batch that means, specifically: cut any history of HireVue the company, of DDI and the STAR method's origin, of rating agencies or the loan market, beyond one sentence where a date matters; cut passages explaining why banks run early programs or why a screen exists; cut comparisons that drift into private equity, consulting or another seat; keep the validity numbers in the STAR article to two sentences. Report every such cut.
