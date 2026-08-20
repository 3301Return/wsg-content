# WSG Article Generator — Project Instructions

This project generates SEO-optimized blog articles for **WallStreetGuide.net (WSG)**, a site helping ambitious American undergrads break into investment banking and consulting.

When the user asks you to write, draft, or generate any WSG content — articles, blog posts, listicles, ultimate guides, niche posts — **immediately load `.claude-skill/SKILL.md`** and follow that workflow exactly.

## Quick orientation (so you know where things live)

- `style-guide/style-guide.md` — voice, dos, don'ts, post structure, AI sniff test. **Read before drafting anything.**
- `style-guide/weak-vs-strong-examples.md` — calibration examples
- `style-guide/seo-checklist.md` — run before delivering any draft
- `templates/` — `ultimate-guide.md`, `listicle.md`, `niche.md`, `deep-dive.md`, `_brief-template.md`
- `samples/` — gold-standard published WSG articles, organized by format
- `writers/` — one Markdown profile per WSG contributor; loaded when a byline is assigned
- `briefs/` — one brief per article in progress
- `drafts/` — working drafts (`draft-{slug}-v1.md`, v2, etc.)
- `published/` — final published versions
- `deep-dives/` — internal long-form guides that spawn multiple articles. See `deep-dives/INDEX.md` for the IB gap list. Consulting deep dives live in `deep-dives/consulting/` with their own `INDEX.md` gap list.
- `consulting/` — canonical consulting context bundle (firm profiles for MBB / tier 2 / Big 4 / boutiques / economic consulting, recruiting timeline, case-interview framework library, voice cues, sources index). **Required reading whenever the article topic is consulting.**
- `content-calendar/` — keyword + headline plan. Run `python3 scripts/parse_calendar.py` to refresh `calendar.md` from the xlsx.
- `scripts/` — `check_article.py` (compliance gate), `markdown_to_wix_html.py` (publishing prep), `markdown_to_docx.py` (locked-format .docx builder), `parse_calendar.py` (calendar refresh), `check_links.py` (link verifier), `check_style.py` (prose-level style guard)
- `publishing/wix-publishing-checklist.md` — manual steps for moving drafts into Wix without losing formatting
- `.claude-skill/SKILL.md` — full skill definition (workflow, hard rules, edge cases, VERIFY protocol, writer profile loading)
- `.claude-skill/consulting.md` — consulting-vertical addendum. Loads ALONGSIDE the main skill whenever the article topic is consulting.
- `.claude-skill/source-verification.md` — source-verification protocol. **Loads ALONGSIDE every article task.** Three-tier entity-verification system (household-name / industry-known / niche), pre-delivery audit checklist, the May 2026 fabrication case study. Prevents fictional coaches / firms / programs from shipping.
- `.claude-skill/recruiting-relevance.md` — 1-5 recruiting-relevance score for filtering keyword research and content-calendar planning. **Loads on any keyword research, topic generation, or content-calendar task.** Filters out instrument explainers (Score 1-2) that don't convert to mentorship interest. Surfaces "how to break into X" / "X interview questions" / firm career guides (Score 4-5) as the ship-first tier. References M&I as the IB-side competitor benchmark.

## The three article formats

1. **Ultimate guide** — insight-led definitive guide. ~2,000-2,500 words. 6-10 opinionated section claims.
2. **Listicle** — curated resource roundup. ~1,800-2,200 words. Exact count from headline.
3. **Niche** — firm/role specific, edge-case student situation, or honest review. ~1,800-2,200 words. Pulls from a deep dive when one exists.

## Hard rules (always enforce)

- Use the exact headline from the brief or content calendar — never edit it
- 1-2 H2 sub-questions right after intro (real search queries, 2-4 sentence answers)
- Listicle counts must match the headline exactly
- Inline anchor-word hyperlinks (never URL footers)
- No em-dashes or hyphens as structural punctuation in body copy
- Every section needs a specific (named firm, real number, named scenario, or first-person experience)
- No filler phrases, no basic definitions, no random bolded words
- CTA only if it lands naturally — default to no CTA
- **For any article referencing recruiting years, read `style-guide/recruiting-timeline-glossary.md` first.** Application year, internship year, and graduation year are three different variables. Standard sophomore cycle: apply year `A` → intern Summer `A+1` → graduate Spring `A+2`. The "10 IB Internships to Apply To in 2027" article is about Summer 2028 internships, not Summer 2027.
- **Run prose-level style check before docx build.** Run `python3 scripts/check_style.py drafts/{file}.md`. Catches non-self-contained bolded sentences, random-bolded firm-name lists, chunky listicle items, missing H2 sub-questions, missing say/don't-say callouts. Exit 1 = hard-rule violation; fix before building. Added June 2026 after the batch shipped with style violations.
- **Verify every link before delivery.** Run `python3 scripts/check_links.py drafts/{file}.md`. Never link to rotating job-posting URLs (Greenhouse `gh_jid=`, BofA Job IDs, iCIMS postings, Citi numeric postings). For forward-looking articles, use evergreen firm landing pages only. Better no link than a wrong one. Full protocol in `style-guide/link-verification.md`.
- **Tag every time-sensitive claim with `[VERIFY: <what to verify>]` inline.** Deadlines, comp, eligibility, deal references, live posting URLs. See full protocol in `.claude-skill/SKILL.md`.
- **Check `writers/{slug}.md` if the article is assigned to a specific writer.** Override generic voice with writer's actual background and pull one signature scenario.
- **Listicle items use bullet structure** (Website, Apply Link, Deadline, Eligibility, Who/Why) + short description. No chunky paragraphs per item.
- **Bolded sentences must be self-contained.** Reading only the bolded text should convey the article's argument.
- **Use contractions** ("don't" not "do not"). Tighten intros to 1-2 short paragraphs.
- **For recruiting articles, target the next open cycle**, not one already closed.
- **For how-to-answer articles, include "say this / don't say that" callouts** at the end.
- **For "Top N" lists, address the top firms NOT on the list.** If a16z and Sequoia don't recruit undergrads directly through VC fellowships, include a short section explaining the realistic path for those firms. Same logic for any ranked list with notable absentees.
- **Hard paragraph breaks at logical pivots within sections.** Between "right for X" and "right for Y" style transitions, always insert a blank line — even mid-section.
- **Run a niche-specific freshness check before finalizing a curated list.** One web search for "best [niche] firm/program for [profile] 2026" to confirm the list is current. NEO Capital is a known prior miss for technical-VC undergrads.
- **Don't recite timeline math at the reader.** The recruiting-timeline-glossary exists for Claude. Don't pad the intro with "the students applying are sophomores in 2026-2027 academic year, Class of 2029." Headline + eligibility lines convey the math.
- **RX is an Elite Boutique product, not a BB coverage group.** Never list RX in a BB group-preference list. BB groups to name: TMT, healthcare, FIG, industrials, consumer, energy, M&A. RX firms: Houlihan Lokey, PJT, Lazard, Moelis, Evercore, Greenhill.
- **Capitalize "Investment Banking Summer Analyst"** as a defined role title. Lowercase only for generic descriptions ("a summer banking internship"), not when naming the role.
- **Default byline is Stephen Turban (WSG founder).** Add `byline: stephen-turban` to every article frontmatter. Read `writers/stephen-turban.md` before drafting. Never use "As an IB analyst..." framings — Stephen is Harvard / McKinsey / Lumiere / WSG founder, not a banker. Meta description must lead with "WSG founder Stephen Turban...".
- **Locked .docx formatting standard.** Arial throughout. H1 24pt bold black. H2 18pt bold black. H3 14pt bold underline black. Body 11pt black. 2.0 line spacing on everything. Always build .docx via `python3 scripts/markdown_to_docx_v2.py drafts/{file}.md "published/ai-written/{Title}.docx"` so the standard is enforced. Full standard at `style-guide/formatting-standards.md`.
- **Consulting articles auto-load the consulting addendum.** If the article is about MBB, tier 2 strategy, Big 4 strategy, consulting boutiques, economic consulting, case interviews, or consulting recruiting, also read `.claude-skill/consulting.md` and the relevant files in `consulting/` (firm profiles, recruiting timeline, case-interview frameworks, voice cues). The consulting cycle is junior-summer (apply spring A → intern Summer A → graduate Spring A+1) — DIFFERENT from IB. Stephen's byline angle is mixed: first-person McKinsey on recruiting/case prep/behavioral; operator framing on firm comparisons.
- **Headlines must be tight, opportunity/value-led, and free of essay framing.** Under 8-10 words. Lead with the opportunity set ("10 Boutique Consulting Firms to Apply To") or the value-delivery ("Ultimate Guide to the MECE Framework"). Never use colon-phrases that read like college papers ("Beyond the Case:", "From Panic to Passed:", "The Insider Blueprint:"). Full rules at `style-guide/editorial-feedback-may-2026.md` section 12. Consulting-article queue lives at `content-calendar/consulting-keywords.md`.
- **NEVER fabricate a named entity.** Coaches, mentorship platforms, recruiting firms, boutique firms, specific deals, named individuals, books, simulators — all of them must be verifiable via web search and the entity's own site. If you can't verify, remove the name from the article. **`.claude-skill/source-verification.md` is the source of truth.** Apply its three-tier protocol before delivering any draft. Two fabricated entries (The Banker's Pillar, GoodPath) shipped in May 2026 and were caught only post-draft; that's the bar this rule exists to prevent re-crossing.
- See `style-guide/editorial-feedback-may-2026.md` for the full editorial protocol.

## Workflow when asked to write

1. Read `.claude-skill/SKILL.md`
2. Read `style-guide/style-guide.md` (including the new AI sniff test section)
3. **Check the vertical.** If the topic is consulting, also read `.claude-skill/consulting.md` and the relevant files in `consulting/` (firm profiles, recruiting timeline, case-interview frameworks, voice cues).
4. Identify format (ask if unclear). Default byline is Stephen Turban unless brief or user says otherwise.
5. Read `writers/stephen-turban.md` (or `writers/{slug}.md` if a different writer is assigned) and use that writer's voice.
6. Load matching template from `templates/`
7. Check `deep-dives/` (or `deep-dives/consulting/` for consulting topics) for relevant source material
8. Pull 1-2 samples from `samples/{format}/` or `published/`
9. Outline first, get approval
10. Draft to `drafts/draft-{slug}-v1.md`. Tag every time-sensitive claim with `[VERIFY: ...]`.
11. Run the compliance script: `python3 scripts/check_article.py drafts/{file}.md`
12. Run `style-guide/seo-checklist.md` and the 4-question gut check
13. Deliver with a `computer://` link

## Important limitation

This skill auto-loads only when Claude is working inside this project folder. If you open a Claude conversation outside this folder, you must explicitly point it at `.claude-skill/SKILL.md` or include the folder context in your first message. The skill does not trigger from arbitrary "write me a WSG article" requests in unrelated workspaces.
