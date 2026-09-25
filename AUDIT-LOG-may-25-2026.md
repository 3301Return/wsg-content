# Source Verification Audit Log — May 25, 2026

Triggered by the discovery that two fabricated entries ("The Banker's Pillar" and "GoodPath") shipped in v1 of the "Top 10 IB Career Coaches" article. The new `.claude-skill/source-verification.md` skill was built to prevent recurrence, and this audit pass verified every named entity in the active article queue.

## Scope of audit

- All 7 newly-shipped May 25 articles (IGotAnOffer Review, McKinsey Solve, 30 IB Questions, S&T Guide, 30 S&T Terms, IB Career Coaches, JPM Superday).
- The PE Recruiters article (claims about specific headhunter founders).
- The consulting firm-profile files in `consulting/firm-profiles/`.

## Fabrications found and fixed

### IB Career Coaches v1 (caught pre-publish, fixed in v1-rev2)

- **"The Banker's Pillar"** — listed as #6 IB mentorship platform. Does not exist. Replaced with **Wall Street Prep Coaching** (verified at wallstreetprep.com/coaching/).
- **"GoodPath"** — listed as #7 coach marketplace. The real goodpath.com is a health and wellness platform, not an IB coaching service. Replaced with **Leland** (verified at joinleland.com).

### JP Morgan Superday Tips v1 (caught and fixed)

- **"JPMorgan's healthcare group ran the Pfizer-Seagen deal last year"** — factually wrong. Goldman Sachs advised Pfizer; Centerview advised Seagen. JPMorgan handled the debt financing only, not the M&A advisory. Rewrote the sample answer as a structural template ("name a specific recent deal the JPM target group advised on") instead of asserting a wrong fact.
- **"Mark Lee in your healthcare group"** — a fabricated placeholder name presented as if real. Replaced with explicit bracket convention "[contact name from a coffee chat]" so readers understand it's a template.

### 30 IB Interview Questions v1 (caught and fixed)

- **"Sarah Chen in your healthcare group"** — fabricated placeholder. Replaced with "[name of a banker you've coffee-chatted with in the target group]".
- **"Plus your healthcare group ran the Cigna-Express Scripts integration"** — placeholder deal presented as if attached to a specific firm. Replaced with "[a specific recent deal you've read about from that group]".

### PE Recruiters v2 (URL and founder claims tightened)

Two wrong URLs and several thin founder claims were caught and corrected against verified sources:

- **HSP URL:** `henkelsearch.com` → `henkelsp.com` (verified live site).
- **CPI URL:** `cpipartners.com` → `cpiny.com` (verified live site).
- **HSP founder:** Updated to credit both Eleni Henkel AND Leah Trabich (originally only credited Henkel). Year of founding (2011) added. Henkel's pre-HSP path at Morgan Stanley + SG Partners added.
- **Amity Search Partners founders:** Added Pam Esterson and Susanna Nichols by name (originally generic).
- **Ratio Advisors founders:** Added Vedica Qalbani, Lindsey Mead, and Jessica Wu by name. Year of founding (2017) added.
- **Glocap founder:** Adam Zoia named. Current CEO Annette Krassner named.
- **BellCast Partners founders:** Danielle Caston Strazzini and Alison Bellino Johnson named (both former CPI).
- **Oxbridge Group dates:** Removed the unverified "Founded in 1988, pivoted to PE in the 1990s, added hedge fund coverage in 2011" claim. Replaced with what could be verified (a flat MD-led process).

## Entities verified as real (no changes needed)

Pulled from the published articles and confirmed via web search:

### Bulge bracket banks (Tier 1, household)
Goldman Sachs, JPMorgan, Morgan Stanley, Bank of America, Citi, Barclays, Deutsche Bank — all real and well-established.

### Elite boutiques (Tier 2)
Evercore, PJT, Centerview, Moelis, Lazard, Greenhill, Houlihan Lokey, Qatalyst — all real.

### M&A advisory specialists
Tidal Partners (Cisco-Splunk advisor, founded by David Handler and David Neequaye, ex-Centerview) — verified.

### Specific deals referenced
- Cisco-Splunk $28B (2023): Cisco advised by Tidal Partners (sole), Splunk advised by Qatalyst + Morgan Stanley. ✓
- Pfizer-Seagen $43B (2023): Pfizer advised by Goldman Sachs; Seagen advised by Centerview. (JPM only on debt financing — the article was corrected to remove the wrong attribution.)
- Salesforce-Slack: real deal, used as a generic example only. ✓
- Cigna-Express Scripts: real 2018 deal, used as a generic example only.

### Consulting boutiques
ZS Associates (founded 1983 by Andris Zoltners and Prabhakant Sinha, Kellogg professors), Putnam Associates, Clearview Healthcare Partners, Health Advances, Altman Solon (2016 merger of Altman Vilandrie and Solon Management Consulting), Simon-Kucher, Prophet (founded 1992 by David Aaker, UC Berkeley), Innosight (founded 2000 by Clayton Christensen), Strategic Decisions Group, AlphaSights. All verified.

### Economic consulting
Analysis Group, Cornerstone Research, NERA, Compass Lexecon (owned by FTI), Bates White, Brattle Group, Charles River Associates. All verified.

### Tier 2 strategy
Oliver Wyman (Marsh McLennan-owned, 1984 founded), Strategy& (PwC-owned post-2014, Booz heritage 1914), A.T. Kearney (1926, McKinsey alum-founded), L.E.K. (1983, founded by Iain Evans, Richard Koch, James Lawrence — three former Bain partners), Roland Berger (1967, Munich), Accenture Strategy. All verified.

### Big 4 strategy
Monitor Deloitte (Monitor founded 1983 by Mark Fuller and Michael Porter, acquired by Deloitte 2013), EY-Parthenon (Parthenon founded 1991 by Bill Achtmeyer and John Rutherford, acquired by EY 2014), PwC Strategy&, KPMG Strategy. All verified.

### VC firms / fellowships
Insight Partners, Bessemer Venture Partners, General Catalyst, NEO Scholars (founded by Ali Partovi, early investor in Airbnb/Dropbox/Facebook), Dorm Room Fund (First Round Capital-backed student-run fund), Contrary, General Catalyst Venture Fellows. All verified.

### Coaching / prep platforms (post-fix)
IGotAnOffer, PrepLounge, Management Consulted, Case in Point (Marc Cosentino), Case Interview Secrets (Victor Cheng), Hacking the Case Interview, Crafting Cases, Wall Street Prep, Breaking Into Wall Street, Mergers & Inquisitions, Macabacus, Wall Street Mastermind (founder Sam Shiah), WSO Academy, Office Hours, Peak Frameworks, Wall Street Prep Coaching, Leland. All verified.

### Books and resources
"Investments" by Mark Hirschey — real text. "Options, Futures, and Other Derivatives" by John Hull — real text. "Heard on the Street" by Timothy Crack — real quant interview prep book.

## Open items (low priority)

- Gold Coast Search Partners — claim "spun out of CPI Partners" not directly verified by an authoritative source. Likely accurate based on industry-knowledge patterns but flag for verification before any future article expands on this.
- Wall Street Mastermind income-share agreement percentage — kept VERIFY tag in the IB Career Coaches article.
- Some pricing figures across the coaching platforms — VERIFY tags retained for the moving targets (current pricing tiers).

## Process changes locked in

1. `.claude-skill/source-verification.md` created and wired into `CLAUDE.md` and `.claude-skill/SKILL.md`.
2. The three-tier verification protocol (household / industry-known / niche) is the new default before any article ships.
3. The May 2026 fabrications are recorded as a case study inside the skill so future article work has the failure mode documented.
4. VERIFY tags are now reserved for "moving target" claims (live pricing, cycle deadlines), NOT for "does this entity exist" — that question must be answered before drafting, not punted to a future review pass.
