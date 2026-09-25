---
name: wsg-recruiting-relevance
description: Load before doing any keyword research, content-calendar planning, or topic prioritization for WSG. Enforces a 1-5 recruiting-relevance score that filters keywords by how useful they are to a freshman or sophomore who is RECRUITING into a finance or consulting role, NOT to someone learning what a financial instrument is. Trigger on any task involving Ahrefs research, content-calendar updates, topic generation, or prioritizing articles to write.
---

# WSG Recruiting Relevance Skill

## Why this skill exists

The May 25 keyword research pulls (consulting, RX, PC, healthcare) surfaced many high-volume keywords like `what is dip financing`, `unitranche`, `liability management exercise`, and `mezzanine financing`. **These are instrument explainers, not recruiting content.** A freshman or sophomore searching for them is curious about a financial instrument, not about how to land an analyst seat at the firms that use it.

WSG's audience is the ambitious undergrad **actively recruiting** into IB, PE, VC, hedge funds, private credit, restructuring, consulting, or related career paths. Content that lands a reader and converts to mentorship interest is content that helps them break in — not content that defines a term they could look up on Investopedia.

This skill exists to put a recruiting-relevance filter on every keyword the keyword research process surfaces, so we ship articles that grow WSG's mentorship pipeline instead of articles that teach finance vocabulary to a general audience.

## The Recruiting Relevance Score (1-5)

Score every candidate keyword before adding it to the content calendar. The score is mandatory in `content-calendar/` xlsx files going forward.

### Score 5 — Direct recruiting content (ship first)

The keyword is explicitly about getting hired into a role. Examples:

- `how to break into restructuring`
- `how to get into private credit`
- `private credit interview questions`
- `restructuring interview questions`
- `consulting resume`
- `how to get into McKinsey`
- `healthcare consulting interview questions`
- `Goldman Sachs HireVue questions`
- `Bain SOVA assessment`
- `how to get into [firm name]`
- `[role] cover letter`
- `[role] recruiting timeline`
- `[firm] career path`

**Article framing for Score 5 keywords:** "How to Break Into X," "Ultimate Guide to X Interview," "X Recruiting Timeline for Undergrads in [year]."

### Score 4 — Career-orientation / firm-specific (ship second)

The keyword is about firms, career paths, salaries, or comparisons that an undergrad uses to decide WHERE to apply or HOW to position. Examples:

- `top private credit firms`
- `Antares Capital` (a firm career destination)
- `Clearview Healthcare Partners` (firm)
- `private credit vs private equity`
- `Big 4 vs MBB`
- `Houlihan Lokey restructuring`
- `Evercore restructuring`
- `private credit salary`
- `mckinsey salary`
- `consulting exit opportunities`
- `mbb to private equity`
- `top 10 consulting firms`

**Article framing for Score 4 keywords:** "[Firm] Career Guide," "X vs Y: Which Should You Pick?," "Top 10 X Firms for Undergrads in [year]," "X Salary Breakdown 2026."

### Score 3 — Career-adjacent explainer (ship if low KD)

The keyword is a "what is X" query where X is a career path or work category, NOT an instrument or transaction structure. Worth writing if the article can be framed for an undergrad-audience reader who is exploring whether to recruit into that path. Examples:

- `what is private credit` (only if framed as "what does the work look like and how do undergrads break in")
- `biotech consulting` (the career)
- `healthcare strategy consulting`
- `pharma consulting`
- `restructuring investment banking` (the career)
- `case interview`
- `mece framework`

**Article framing for Score 3 keywords:** Always lead with the career angle. The article should answer "should I recruit into this path" before "what is this thing." If it ends up being 80% instrument-definition, downgrade to Score 1 and skip.

### Score 2 — Industry-practitioner content (deprioritize)

The keyword is about deal flow, market trends, or analysis that a working analyst cares about. An undergrad doesn't search for this until they're already in the role. Examples:

- `private credit deals 2026`
- `healthcare M&A deals`
- `restructuring deal trends`
- `LBO market 2026`
- `pharma M&A deals`
- `private credit market size`

**Default action:** Skip. WSG is not a markets publication. If a Score 2 keyword has unusually high volume and low KD, frame as a "what undergrads should know about [trend] for their interview" angle and upgrade to Score 3-4.

### Score 1 — Pure instrument / definition (skip)

The keyword is asking what a specific financial instrument, transaction structure, or accounting concept is. A reader landing on this content is either an analyst who already has a job or a curious onlooker. Examples:

- `what is dip financing`
- `unitranche`
- `liability management exercise`
- `senior secured loan`
- `mezzanine financing` (the instrument; downgrade from 3 if the article ends up defining the instrument rather than the career)
- `BDC business development company`
- `EBITDA definition`
- `WACC formula`

**Default action:** Skip. These articles do not convert to WSG mentorship interest. They compete against Investopedia, CFI, and Wikipedia — sites with materially higher domain authority on instrument-explainer queries. WSG should not invest editorial effort here even when KD is 0.

## How to apply the score during keyword research

When pulling Ahrefs data:

1. Score every candidate keyword 1-5 before adding it to the content calendar.
2. Filter for Score ≥ 4 as the default ship list. Score 3 is conditional on KD ≤ 10 AND the article can be framed for an undergrad recruiting audience.
3. Drop Score 1-2 unless the user explicitly approves. Do not auto-ship them.
4. Composite score formula for ranking: **volume × ranking probability × recruiting relevance ÷ noise**. Specifically: `(volume / max(1, KD)) × relevance`. This is what should drive the "ship next" list.

## The M&I competitor benchmark

WSG's primary competitor for IB-side recruiting content is [Mergers & Inquisitions (M&I)](https://mergersandinquisitions.com). M&I owns the long-tail SEO for IB-into-X-vertical content. The articles to beat:

- **For restructuring:** [Restructuring Investment Banking: How to Get In and What You Do](https://mergersandinquisitions.com/restructuring-investment-banking-group/). 19-minute read by Brian DeChesare. Last refreshed Apr 1, 2020. Outdated cycle data; broad market coverage. **Beatable on freshness and undergrad framing.**
- **For private credit:** [Private Credit Interview Questions: Full Guide + Answers](https://mergersandinquisitions.com/private-credit-interview-questions/). M&I owns this query. Beatable by adding 2026 cycle anchoring, named WSG-mentored candidate scenarios, and the scholarship plug.

When drafting a Score 4 or Score 5 article in IB or buy-side verticals, **read the equivalent M&I article first**. WSG's job is to write a materially better version — more current, more named-specific, more under-grad-focused. M&I writes for the analyst already considering the lateral; WSG writes for the sophomore who hasn't applied yet.

For consulting-side content, **the equivalent benchmarks are Management Consulted, Case in Point, and IGotAnOffer.** Same logic applies.

## Approved article framings (Score 4-5)

These framings have demonstrated conversion to WSG mentorship interest:

- **The Ultimate Guide to Break Into [X]** — restructuring, private credit, hedge funds, growth equity, life sciences consulting.
- **A Beginner's Guide to [X] for Undergrads** — private credit, restructuring, distressed investing. Strongest framing when targeting freshmen / sophomores who are still exploring.
- **How to Get Into [X] as an Undergrad** — McKinsey, Goldman Sachs IB, Citadel, etc.
- **[X] Interview Questions: Complete Guide** — IB technicals, consulting case, private credit, RX behavioral.
- **Top 10 [X] Firms for Undergrads in [year]** — consulting, PE recruiting, RX boutiques, healthcare consulting boutiques.
- **[Firm] Career Guide** — Clearview Healthcare Partners, Antares Capital, Houlihan Lokey RX.
- **[X] Salary Breakdown [year]** — McKinsey, private credit, RX analyst.
- **[X] vs [Y]: Which Should You Pick?** — Big 4 vs MBB, MBB vs PE direct, private credit vs PE.

## Forbidden article framings (Score 1-2)

Do not write these as standalone articles. If the content is necessary, fold it into a Score 4-5 piece as a section.

- **What Is [Instrument]?** — DIP financing, unitranche, mezzanine, senior secured loan, BDC structure, accretion-dilution math. These belong inside Score 4-5 articles, not as standalone articles.
- **[Instrument] Definition** — any straight-definition query.
- **Recent [Industry] Deals** — Score 2 practitioner content. Skip.
- **[Sector] Market Trends [year]** — same.

## How this skill changes the existing content-calendar files

When this skill loads alongside an existing content-calendar file:

1. Re-score every row with the 1-5 scale.
2. Re-rank by composite score `(volume / max(1, KD)) × relevance`.
3. Drop or move-to-archive any topics with Score 1.
4. Flag Score 2 topics for explicit user approval before drafting.
5. Surface Score 4-5 topics that are missing — e.g., "How to Break Into Restructuring" was missing from the original RX list and should have been there.

## Open enhancements

- A future version of this skill could add a "freshness check" tier — Score 5 articles in fast-moving cycles (private credit, healthcare M&A) need refresh dates noted because the field is evolving.
- A separate "intent strength" tier could differentiate Score 4 firm-career articles by whether the firm hires juniors directly (higher) or only post-IB/post-consulting laterals (lower). For now, treat all firm career guides as Score 4.

## Freshman/Sophomore Fit (F/S Fit) — second dimension (1-5)

The Recruiting Relevance score above answers "is this someone trying to break in?" The Freshman/Sophomore Fit answers a separate question: "is this someone EARLY in the process — exploring, deciding, building foundation — vs already in the interview pipeline?"

WSG's primary audience is freshmen and sophomores who are still exploring paths and building strategy. The mentorship funnel converts best from candidates who land on WSG content BEFORE they pick a specific firm or path. Articles that map to early-stage exploration convert at materially higher rates than articles that map to active-interview prep — even if both score the same on Recruiting Relevance.

### F/S Fit Scale

- **F/S Fit 5** — quintessentially freshman/sophomore. Exploration-stage queries: "what is X," "how to become a X," "X career path," "X salary," "X day in the life," "X vs Y," rankings of firms for undergrads, "how to break into X," consulting recruiting timeline.
- **F/S Fit 4** — sophomore-leaning. Early-recruiting queries: "consulting internships," "X internship application," "how to get a consulting internship," firm-specific salary research, "best firms for undergrads."
- **F/S Fit 3** — sophomore-to-junior crossover. Interview prep that BOTH stages care about: "case interview prep," "consulting interview questions," "consulting case study practice."
- **F/S Fit 2** — junior/senior-leaning. Specific active-recruit queries: "[firm] case interview," "[firm] superday," "[firm] HireVue questions," "[firm] interview prep this week."
- **F/S Fit 1** — post-grad / lateral content. Consultant-to-PE moves, MBA application prep, consultant-to-tech-PM transition. Not the WSG core audience.

### Composite formula with F/S Fit

The composite ranking formula now becomes:

```
composite = (volume / max(1, KD)) × recruiting_relevance × (fresh_soph_fit / 5)
```

The `/5` normalization keeps the F/S Fit multiplier between 0.2 and 1.0 so it weights but doesn't dominate. A Score 5 / F/S Fit 5 article is at full weight. A Score 5 / F/S Fit 3 article is at 0.6 weight. A Score 3 / F/S Fit 5 article that would have ranked low on the prior formula now ranks meaningfully higher.

### Practical implication

This dimension flips a meaningful subset of the prior re-score:

- **"What Is Strategy Consulting?" (Score 3 / F/S Fit 5)** moves UP. It's a career-path explainer keyword that maps perfectly to a sophomore exploring whether to pursue consulting. The "Score 3" label is technically correct, but the F/S Fit makes it strategically a top-tier article.
- **"BCG Case Interview Guide" (Score 5 / F/S Fit 2-3)** moves DOWN. Direct recruiting prep, but candidates landing on this article are mid-recruit juniors who already know what BCG is and what a case interview is. Lower mentorship-conversion likelihood.
- **"Consulting Day in the Life" (Score 5 / F/S Fit 5)** stays at the top. Exploration-stage AND direct recruiting content.

The F/S Fit dimension is NOT a replacement for Recruiting Relevance. Articles still need to be Score 3+ on Recruiting Relevance to ship. The F/S Fit re-weights within the ship-list once the recruiting filter has been applied.

### F/S Fit goes in every keyword-research xlsx column going forward

Every content-calendar spreadsheet should include both columns: `Recruit Rel (1-5)` and `F/S Fit (1-5)`. The composite formula above is the new default sort.
