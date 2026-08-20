---
name: wsg-consulting-addendum
description: Load alongside the main wsg-article skill whenever the article topic is consulting — MBB (McKinsey, BCG, Bain), tier 2 strategy (OW, Strategy&, Kearney, LEK, Roland Berger, Accenture Strategy), Big 4 strategy (Monitor Deloitte, EY-Parthenon, KPMG Strategy, PwC Strategy&), boutiques (ZS, Putnam, Clearview, Altman Solon, Simon-Kucher, Prophet), economic consulting (Analysis Group, Cornerstone, NERA, Compass Lexecon, Bates White), case interviews, MBB recruiting timeline, MBB sophomore programs (McKinsey Insight, BCG Bridge to BCG, Bain Build), or consulting exits and careers. Trigger on phrases like "case interview," "MBB," "McKinsey," "BCG," "Bain," "management consulting," "consulting recruiting," "Oliver Wyman," "Monitor Deloitte," "EY-Parthenon," "consulting firms," "consulting internship," "consulting exit options," "PEI," "Solve / Casey / SOVA," "profitability case," or whenever a WSG article references consulting roles. This skill layers on top of `.claude-skill/SKILL.md` and `style-guide/style-guide.md` — it does NOT replace them.
---

# WSG Consulting Addendum

This skill loads in addition to `.claude-skill/SKILL.md` and `style-guide/style-guide.md` whenever the article topic is consulting. Every editorial rule and format rule from the main skill still applies. The notes below are consulting-specific.

## Mandatory reading before drafting any consulting article

In this order:

1. `style-guide/style-guide.md` — voice, dos, don'ts, AI sniff test. (Same as always.)
2. `style-guide/formatting-standards.md` — .docx output spec.
3. `style-guide/editorial-feedback-may-2026.md` section 12 — headline rules (under 8-10 words, opportunity/value-led, no college-essay framing).
4. `writers/stephen-turban.md` — default byline. (Same as always.)
5. `consulting/voice-cues.md` — Stephen's consulting-specific angle. **First-person on recruiting / case prep / behavioral / day-in-the-life. Operator framing on firm-by-firm comparisons.**
6. `consulting/recruiting-timeline.md` — the canonical timeline. Read before any article that mentions a year.
7. `content-calendar/consulting-keywords.md` — the approved headline list. Use the right-column (approved) version of the headline, not the original.
8. The firm-profile file(s) that match the article's scope:
   - MBB-only article → `consulting/firm-profiles/mbb.md`
   - Listicle covering multiple tiers → all five firm-profile files
   - Boutique-specific article → `consulting/firm-profiles/boutiques.md`
   - Econ consulting article → `consulting/firm-profiles/economic-consulting.md`
9. For any case-interview article: `consulting/case-interview-frameworks.md`.
10. The relevant deep-dive at `deep-dives/consulting/{topic}.md` if one exists. (Most don't yet — see `deep-dives/consulting/INDEX.md` for the gap list.)
11. `consulting/sources/INDEX.md` for the canonical link list.

## The consulting recruiting timeline (read this carefully)

The undergrad consulting cycle is DIFFERENT from the IB cycle. Most WSG-reader confusion comes from this.

**Consulting standard path (junior summer):** apply in spring of year A → intern Summer of year A → graduate Spring A+1.

| Cycle name | Apply | Intern | Graduate |
| --- | --- | --- | --- |
| 2026 cycle | Spring 2026 | Summer 2026 | Spring 2027 (Class of 2027) |
| 2027 cycle | Spring 2027 | Summer 2027 | Spring 2028 (Class of 2028) |

Compare to IB: IB sophomores apply in year A for Summer A+1 internship (graduating A+2). Don't conflate the two cycles in an article. If the article references both IB and consulting recruiting, name the cycle precisely for each.

**Sophomore-summer affinity programs** (McKinsey Insight, BCG Bridge to BCG, Bain Build) are the exception. Apply fall of sophomore year → intern Summer of the sophomore year → graduate two years later.

## Byline rule (mix angle)

Stephen Turban is a former McKinsey consultant. The byline angle depends on the article type:

### Use first-person McKinsey experience on:

- Recruiting timeline articles
- Case interview prep articles
- Behavioral interview articles
- Networking articles
- "How to break in" articles
- Day-in-the-life or culture articles
- Career-path / exit-options articles

### Use operator framing (NOT first-person) on:

- Firm-by-firm comparisons (MBB vs tier 2 vs Big 4)
- Specific firm profiles other than McKinsey (BCG, Bain, OW, EYP, etc.)
- Ranked lists ("Top 10 Consulting Firms")
- Industry analysis (consulting as a sector)
- Salary / comp comparisons

### Hard rule

Stephen is NOT a banker, NOT a current consultant, NOT a partner. He was a McKinsey BA / Associate. Don't write "as a partner..." or "in my MD role..." or anything that overclaims. See `writers/stephen-turban.md` for the full do/don't list.

## Firm-list defaults

Use these canonical names. Don't substitute or invent.

- **MBB:** McKinsey & Company, Boston Consulting Group (BCG), Bain & Company.
- **Tier 2 strategy:** Oliver Wyman, Strategy& (PwC), Kearney (A.T. Kearney), L.E.K. Consulting, Roland Berger, Accenture Strategy.
- **Big 4 strategy:** Monitor Deloitte, EY-Parthenon, PwC Strategy& (often classified as tier 2 too), KPMG Strategy.
- **Healthcare and life sciences boutiques:** ZS Associates, Putnam Associates, Clearview Healthcare Partners, Health Advances, L.E.K. Life Sciences (sub-practice of L.E.K.).
- **TMT boutique:** Altman Solon.
- **Pricing specialist:** Simon-Kucher.
- **Brand and marketing:** Prophet.
- **Economic consulting:** Analysis Group, Cornerstone Research, NERA Economic Consulting, Compass Lexecon, Bates White, Brattle Group, Charles River Associates (CRA).
- **Innovation / disruption specialist:** Innosight.
- **Decision analysis specialist:** Strategic Decisions Group (SDG).

## Case-interview vocabulary

- **Five canonical case types:** profitability, market entry, M&A, operations / cost reduction, market sizing.
- **MECE** (mutually exclusive, collectively exhaustive). Capitalize. Don't pad articles with the term — use it when teaching structure, not as filler.
- **Drivers, not frameworks.** WSG articles should reinforce that interviewers want to see custom structure, not memorized templates. Cite Porter's Five Forces ONLY for industry-structure cases.
- **Pre-interview assessments by firm:** McKinsey Solve, BCG Casey, Bain Online Test / SOVA. Spell them out.
- **Personal Experience Interview (PEI).** McKinsey-specific. Three dimensions: personal impact, entrepreneurial drive, inclusive leadership.

## Five tells of a low-credibility consulting article (always avoid)

1. Recommends Porter's Five Forces for every case.
2. Conflates "Big 4 advisory" with "Big 4 strategy."
3. Lists 20+ case-interview frameworks to memorize.
4. Treats MBB as the only credible path.
5. Cites only Victor Cheng or only Case in Point with no firm-published resources.

## Five tells of a high-credibility consulting article (always aim for)

1. Names specific cases by type with one named drill per type.
2. Names specific firms by sub-practice (Oliver Wyman Financial Services, EY-Parthenon Education, ZS Pharma Decision Analytics).
3. References actual 2026 cycle dates (McKinsey BAI March 29, Bain ACI July 19) with VERIFY tags.
4. Distinguishes sophomore-program affinity tracks from junior-summer main tracks.
5. Acknowledges that boutique > MBB for some candidate profiles (e.g., pharma → ZS or Putnam over McKinsey healthcare).

## VERIFY-tag protocol for consulting

Same protocol as the main skill. Tag every:

- Deadline (e.g., "McKinsey BAI March 29, 2026 [VERIFY: live McKinsey careers page]")
- Comp figure
- Class size
- Acceptance rate
- Live posting URL
- Firm-specific assessment threshold (Solve cutoff, etc.)
- Specific engagement reference

## Link verification

Same protocol as the main skill. For consulting articles:

**Always link to:** firm career pages (mckinsey.com/careers, etc.), university career-center posts (Tufts careers, MIT Sloan CDO, Columbia Career Ed, Dartmouth Career Design, Yale OCS).

**Sometimes link to:** Management Consulted, PrepLounge, Hacking the Case Interview, IGotAnOffer, Crafting Cases.

**Never link to:** rotating Workday or Greenhouse posting URLs. Same rule as IB. Run `python3 scripts/check_links.py drafts/{file}.md` before publish.

## Article-format defaults

The three article formats still apply (ultimate guide, listicle, niche). Consulting-specific notes:

- **Listicle on consulting firms.** Always include at least 1 boutique and 1 econ consulting firm in the list if the count is 10+. Generic MBB-only lists fail the AI sniff test.
- **Ultimate guide on consulting.** Open with the cycle math (sophomore vs junior, when to apply). Most WSG readers conflate IB and consulting timelines.
- **Niche on a specific firm.** Use the firm-profile file as the spine. Pull at least one Stephen first-person McKinsey scenario if the niche is McKinsey; otherwise use operator framing.

## Listicle structure for consulting articles

Same bullet structure as IB listicles: Website, Apply Link (if open), Deadline, Eligibility, Who they hire / why apply, then 2-3 sentence description. Don't use chunky paragraphs per firm.

## Word count targets

Same as main skill:

- Ultimate guide: 2,000-2,500
- Listicle: 1,800-2,200
- Niche: 1,800-2,200

## Output

Same as main skill — Markdown to `drafts/draft-{slug}-v1.md`, then `.docx` to `published/` via `python3 scripts/markdown_to_docx.py`. Frontmatter must include `byline: stephen-turban` and the meta description must lead with "WSG founder Stephen Turban...".
