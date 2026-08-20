# RX / PC / Healthcare Topics — Recruiting Relevance Re-Score (May 25, 2026)

_Re-scored from the prior RX/PC/Healthcare keyword pulls using the **1-5 Recruiting Relevance scale** in `.claude-skill/recruiting-relevance.md`. Original keyword research surfaced too many instrument-explainer queries (`what is dip financing`, `unitranche`, `liability management exercise`) that don't convert WSG's freshman / sophomore audience to mentorship interest. This re-score filters for the topics that actually help an undergrad break into the role._

## The Recruiting Relevance Scale (1-5)

- **Score 5** — Direct recruiting content. "How to break into X." "X interview questions." "X salary." Ship first.
- **Score 4** — Career-orientation + firm-specific. "Top X firms," "X vs Y," "[firm] career guide." Ship next.
- **Score 3** — Career-adjacent explainer (about the work / career path, not the instrument). Conditional ship if KD ≤ 10.
- **Score 2** — Practitioner content (deal flow, market trends). Default skip.
- **Score 1** — Instrument or definition explainers. **Always skip** — Investopedia / CFI already own these queries and they don't convert to WSG mentorship interest.

## Composite ranking formula

```
composite = (volume / max(1, KD)) × recruiting_relevance
```

The composite weights low-KD AND high-relevance AND high-volume together. A Score 5 article at KD 0 with 150 volume (composite 750) outranks a Score 1 article at KD 0 with 800 volume (composite 800 but recruiting relevance 1 means it doesn't convert).

## The new ship list — Top 8 priority articles

These are the articles WSG should write first across the three verticals. Every one is Score 4-5, every one is under KD 10, and every one has a clear recruiting framing.

| # | Vertical | Headline | Keyword | Vol | KD | Score | Composite |
|---|---|---|---|---|---|---|---|
| 1 | PC | **A Beginner's Guide to Private Credit** | how to get into private credit | 150 | 1 | 5 | 750 |
| 2 | RX | **The Ultimate Guide to Break Into Restructuring** | how to break into restructuring | 0 | 0 | 5 | n/a, ship for editorial position |
| 3 | PC | **Top 10 Private Credit Jobs for Undergrads in 2026** | private credit jobs | 600 | 0 | 5 | 3,000 |
| 4 | PC | **20 Private Credit Interview Questions** | private credit interview questions | 150 | 0 | 5 | 750 |
| 5 | PC | **Private Credit Salary 2026: Full Breakdown** | private credit salary | 200 | 0 | 5 | 1,000 |
| 6 | RX | **Restructuring Interview Questions: 20 You Must Know** | restructuring interview questions | 50 | 0 | 5 | 250 |
| 7 | HC | **How to Get Into Healthcare Consulting as an Undergrad** | how to get into healthcare consulting | 90 | 0 | 5 | 450 |
| 8 | HC | **Clearview Healthcare Partners Career Guide** | clearview healthcare partners | 1,700 | 2 | 4 | 3,400 |

**The two flagship articles to ship FIRST:**

### Flagship 1: The Ultimate Guide to Break Into Restructuring

- **Target keyword:** `how to break into restructuring`
- **Format:** Ultimate guide
- **Competitor to beat:** [M&I — Restructuring Investment Banking: How to Get In and What You Do](https://mergersandinquisitions.com/restructuring-investment-banking-group/). 19-min read by Brian DeChesare. Last refreshed April 1, 2020 — **outdated cycle data, generic framing.**
- **WSG angle:** 2027 cycle anchoring, named WSG candidate scenarios, undergrad-specific framing (M&I writes for the IB analyst lateral; WSG writes for the sophomore). Named RX EBs (Houlihan, PJT, Lazard, Moelis, Evercore, Greenhill). Scholarship plug.
- **Why this is a flagship:** RX is the highest editorial-fit IB vertical for WSG's existing content. Building this article lets every other RX firm-career-guide article link back to it as the hub.

### Flagship 2: A Beginner's Guide to Private Credit

- **Target keyword:** `how to get into private credit` (volume 150, KD 1)
- **Format:** Ultimate guide
- **Competitor to beat:** [M&I — Private Credit Interview Questions: Full Guide + Answers](https://mergersandinquisitions.com/private-credit-interview-questions/). M&I owns this query.
- **WSG angle:** Beginner-friendly framing for freshmen / sophomores (M&I writes for the IB analyst recruiting laterally; WSG writes for the sophomore who's never heard of unitranche). 2027 cycle anchoring, named firms (Antares, Golub, Ares — all on the verified-brands list), salary breakdown, day-in-the-life, exit options.
- **Why this is a flagship:** Private credit is the fastest-growing buy-side career path for undergrads, and the SEO competition is dominated by industry trade press rather than student-facing guides. Hub-and-spoke into all other PC articles (interview questions, salary, jobs, firm guides).

## Full re-scored table (S, A, B tier topics worth shipping)

| # | Vert | Tier | Score | Headline | Keyword | Vol | KD | Composite |
|---|---|---|---|---|---|---|---|---|
| 1 | PC | S | 5 | A Beginner's Guide to Private Credit | how to get into private credit | 150 | 1 | 750 |
| 2 | RX | S | 5 | The Ultimate Guide to Break Into Restructuring | how to break into restructuring | 0 | 0 | n/a |
| 3 | PC | S | 5 | Top 10 Private Credit Jobs for Undergrads in 2026 | private credit jobs | 600 | 0 | 3,000 |
| 4 | PC | S | 5 | 20 Private Credit Interview Questions | private credit interview questions | 150 | 0 | 750 |
| 5 | PC | S | 5 | Private Credit Salary 2026: Full Breakdown | private credit salary | 200 | 0 | 1,000 |
| 6 | RX | S | 5 | Restructuring Interview Questions: 20 You Must Know | restructuring interview questions | 50 | 0 | 250 |
| 7 | HC | S | 5 | How to Get Into Healthcare Consulting as an Undergrad | how to get into healthcare consulting | 90 | 0 | 450 |
| 8 | HC | S | 5 | Healthcare Consulting Interview Questions | healthcare consulting interview questions | 10 | 0 | 50 |
| 9 | HC | S | 4 | Clearview Healthcare Partners Career Guide | clearview healthcare partners | 1,700 | 2 | 3,400 |
| 10 | PC | S | 4 | Antares Capital Career Guide | antares capital | 2,200 | 4 | 2,200 |
| 11 | HC | S | 4 | Putnam Associates Career Guide | putnam associates | 700 | 1 | 2,800 |
| 12 | HC | S | 4 | Health Advances Career Guide | health advances | 500 | 0 | 2,000 |
| 13 | RX | S | 4 | Houlihan Lokey Restructuring Career Guide | houlihan lokey restructuring | 100 | 4 | 100 |
| 14 | RX | S | 4 | Evercore Restructuring Career Guide | evercore restructuring | 90 | 0 | 360 |
| 15 | HC | S | 4 | ZS Associates Career Guide | zs associates careers | 350 | 5 | 280 |
| 16 | PC | S | 4 | Private Credit vs Private Equity: Which Should You Pick? | private credit vs private equity | 800 | 3 | 1,067 |
| 17 | HC | A | 4 | Top 10 Healthcare Consulting Firms for Undergrads in 2026 | pharma consulting firms | 100 | 6 | 67 |
| 18 | HC | A | 4 | Healthcare Consulting Salary 2026 | healthcare consulting careers | 40 | 1 | 160 |
| 19 | RX | A | 4 | Lazard Restructuring Career Guide | lazard restructuring | 20 | 0 | 80 |
| 20 | RX | A | 4 | PJT Partners Restructuring Career Guide | pjt rx | 10 | 0 | 40 |
| 21 | PC | A | 4 | Top 10 Private Credit Firms for Undergrads in 2026 | private credit firms | 600 | 21 | 114 |
| 22 | PC | A | 4 | What Is Private Credit? A Career Guide for Undergrads | what is private credit | 4,200 | 21 | 800 |
| 23 | RX | B | 3 | What Is Restructuring Investment Banking? Complete Guide | restructuring investment banking | 250 | 3 | 250 |
| 24 | RX | B | 3 | Distressed Debt Investing: Career Path for Undergrads | distressed debt investing | 350 | 10 | 105 |
| 25 | PC | B | 3 | Direct Lending Career Path for Undergrads | direct lending | 1,100 | 10 | 330 |
| 26 | HC | B | 3 | A Career Guide to Biotech Consulting | biotech consulting | 700 | 7 | 300 |
| 27 | HC | B | 3 | Ultimate Guide to Healthcare Investment Banking | healthcare investment banking | 450 | 14 | 96 |
| 28 | HC | B | 3 | A Career Guide to Pharma Consulting | pharma consulting | 400 | 14 | 86 |
| 29 | HC | B | 3 | Healthcare Strategy Consulting Career Path | healthcare strategy consulting | 300 | 7 | 129 |

## Skipped (Score 1-2 — instrument explainers)

These were in the original list but should NOT be shipped per the recruiting-relevance skill. They compete against Investopedia / CFI / Wikipedia on instrument-definition queries and don't convert to WSG mentorship.

| Vertical | Headline | Keyword | Vol | KD | Score | Reason |
|---|---|---|---|---|---|---|
| RX | What Is DIP Financing? Complete Guide | dip financing | 800 | 2 | 1 | Pure instrument explainer |
| RX | Ultimate Guide to Liability Management Exercises | liability management exercise | 350 | 0 | 1 | Pure instrument / transaction explainer |
| RX | Ultimate Guide to Distressed Debt Investing | distressed debt | 900 | 10 | 2 | Borderline; could be career-framed but instrument-leaning |
| RX | Bankruptcy Advisory: How Restructuring Firms Work | bankruptcy advisory | 100 | 1 | 2 | Practice-area explainer; folds into a flagship |
| PC | Ultimate Guide to Mezzanine Financing | mezzanine financing | 2,000 | 7 | 2 | Instrument. High volume tempting; do not write standalone |
| PC | Ultimate Guide to Unitranche Loans | unitranche | 700 | 1 | 1 | Pure instrument explainer |
| HC | Healthcare M&A: An Undergrad's Career Primer | healthcare m&a | 400 | 3 | 2 | Deal-type explainer; defer |
| HC | Pharma Commercial Strategy Explained | pharma commercial strategy | 150 | 1 | 2 | Work-type explainer; defer |
| HC | Medical Device M&A Deals 2026 | medical device m&a | 150 | 5 | 2 | Deal-flow content; not for undergrads |

**Important note:** the SEO instinct says ship `what is private credit` (4,200 vol) and `mezzanine financing` (2,000 vol). Per the recruiting-relevance skill we are NOT shipping these as instrument explainers. We ARE shipping the same keyword (`what is private credit`) framed as an undergrad career guide (entry #22 above, Score 4 not Score 1). Same query, different article. The article's first paragraph determines the framing; the headline alone doesn't.

## Snapshot

| Tier | Count | Combined volume | Combined TP |
|---|---|---|---|
| S (Score 4-5, ship first) | 16 | ~7,720 | ~17,290 |
| A (Score 4, ship next) | 6 | ~5,540 | ~3,711 |
| B (Score 3, conditional ship) | 7 | ~3,550 | ~4,360 |
| Skip (Score 1-2) | 9 | ~5,550 | ~5,475 |

## Open follow-ups

- Need to verify Antares Capital, Golub Capital, Ares Capital, Blue Owl on the source-verification skill's Tier 2 list. Add to `scripts/verified-brands.txt` before shipping any PC firm-career guide.
- The "How to Break Into Restructuring" flagship needs a content outline before drafting. Suggested H2 structure: (1) What is RX, (2) The five RX EBs, (3) The 2027 RX recruiting timeline, (4) RX technical interview prep, (5) RX behavioral interview prep, (6) RX exit options.
- M&I's existing RX article is dated April 2020. The 2026 RX market (post-rate-cycle, LME boom, private credit competition) is materially different; WSG can win on freshness alone.

## Re-affirming the skill

This entire re-score was generated by applying `.claude-skill/recruiting-relevance.md`. Going forward, every keyword research pull should include the 1-5 relevance column. The composite formula goes in the xlsx by default. Topics scoring 1-2 do not ship without explicit user override.
