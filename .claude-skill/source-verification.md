---
name: wsg-source-verification
description: Load before drafting or revising any WSG article. Enforces a verification protocol for every named entity (coaches, mentorship platforms, recruiting firms / headhunters, boutique firms, niche programs, named deals, named individuals, specific tools / books / courses). The protocol exists to prevent fabricated entries that hurt WSG's credibility. Trigger on any task that involves naming a third-party firm, person, tool, or program in a WSG article.
---

# WSG Source Verification Skill

## Why this skill exists

In May 2026, two fabricated entries shipped in the "Top 10 Places to Find an Investment Banking Career Coach" article ("The Banker's Pillar" and "GoodPath" were named as IB coaching platforms — neither exists in that space). The error was caught before publish, but the cost would have been real: every reader who clicked the fake link and got a 404 would have updated their mental model of WSG's editorial quality downward, permanently.

**This skill is the gate that prevents a repeat.** Read it before drafting or revising any WSG article. Apply the verification protocol below to every named entity in the article. If you can't verify, remove the name. No exceptions.

## The verification hierarchy

Three tiers of named entities, with different verification requirements.

### Tier 1: Household-name entities (no verification required)

The brand is so well-established that fabrication risk is zero. Skip verification.

- **Bulge bracket banks:** Goldman Sachs, JPMorgan / J.P. Morgan, Morgan Stanley, Bank of America, Citi / Citigroup, Barclays, Deutsche Bank, UBS, Wells Fargo, RBC Capital Markets.
- **MBB:** McKinsey & Company, Boston Consulting Group (BCG), Bain & Company.
- **Big 4:** Deloitte, EY (Ernst & Young), KPMG, PwC.
- **Mega-fund PE:** Blackstone, KKR, Apollo, Carlyle, Bain Capital, Vista Equity Partners, Thoma Bravo, Silver Lake.
- **Top-tier VC:** Sequoia Capital, Andreessen Horowitz (a16z), Benchmark, Accel, Founders Fund, Kleiner Perkins, NEA, Greylock.
- **Top-tier hedge funds:** Citadel, Millennium, Bridgewater, Point72, Two Sigma, Renaissance Technologies.
- **Wall Street Journal, Financial Times, Bloomberg, Reuters** as media references.
- **Public companies you'd find on the S&P 500.**

### Tier 2: Industry-known but verifiable (always verify)

The name is plausible but not household-level. Verification required.

- **Elite boutique banks:** Evercore, PJT, Centerview, Moelis, Lazard, Greenhill, Houlihan Lokey, Guggenheim, Perella Weinberg, Qatalyst.
- **Upper-middle-market PE:** Audax, GTCR, Madison Dearborn, Hellman & Friedman, Berkshire Partners, Genstar, Veritas Capital.
- **Growth equity:** Insight Partners, General Atlantic, TA Associates, Summit Partners, Spectrum Equity, Susquehanna Growth Equity.
- **Tier 2 strategy consulting:** Oliver Wyman, Strategy& (PwC), A.T. Kearney / Kearney, L.E.K., Roland Berger, Accenture Strategy.
- **Big 4 strategy practices:** Monitor Deloitte, EY-Parthenon, PwC Strategy&, KPMG Strategy.
- **Boutique consulting firms:** ZS Associates, Putnam Associates, Clearview Healthcare Partners, Health Advances, Altman Solon, Simon-Kucher, Prophet, Innosight.
- **Economic consulting:** Analysis Group, Cornerstone Research, NERA, Compass Lexecon, Bates White, Brattle Group, Charles River Associates.
- **PE headhunters:** Henkel Search Partners, CPI Partners, Amity Search Partners, SG Partners, Ratio Advisors, BellCast Partners, Glocap, Oxbridge Group, DSP, Gold Coast Search.
- **Established prep platforms:** Wall Street Prep, Breaking Into Wall Street, Mergers & Inquisitions, Macabacus, Wall Street Oasis.
- **VC fellowships:** Kleiner Perkins Fellows, Dorm Room Fund, Contrary, NEO Scholars, General Catalyst Venture Fellows.

**Verification step:** A single Web Fetch or Web Search to confirm the firm has an active website and the brand description matches what you're about to write. 30-second check.

### Tier 3: Niche or unfamiliar names (always verify, with elevated scrutiny)

Anything that doesn't sit in Tier 1 or 2 requires a higher bar:

- Coaches and mentorship platforms outside the Tier 2 list (Wall Street Mastermind, IGotAnOffer, Leland, Office Hours, Peak Frameworks, GoodPath, The Banker's Pillar, etc.).
- Named individuals (founders, recruiters, professors, alumni) unless they are widely-known public figures.
- Specific deal references (acquirer, target, deal size, advisors).
- Specific cycle deadlines, current-cycle compensation figures, current-cycle program sizes.
- Books, podcasts, simulators, or apps you're citing as a resource.

**Verification step:** Multiple-source verification. Confirm the entity exists, the brand description is right, and the URL is live. If the entity is named after a person (e.g., "Sam Shiah of Wall Street Mastermind"), confirm that person is publicly associated with that entity.

## The verification protocol

Before naming any Tier 2 or Tier 3 entity in an article:

### Step 1: Web search the brand

A single web search for `"[Brand Name]" [industry context]` — e.g., `"The Banker's Pillar" investment banking coaching`. If the first page of results doesn't return a website that matches your assumed description, the entity may not exist or may not be what you think it is. **Stop. Do not name it.**

### Step 2: Web fetch the official URL

If a URL exists, fetch the homepage. Confirm:

- The site loads (HTTP 200).
- The brand's self-description on the site matches what you intend to write.
- The site is current (recent copyright year, active blog posts within last 12 months, or other signals of being live).

### Step 3: Cross-check on a third-party source

For Tier 3 entities especially: confirm the brand has a presence beyond its own site. A Wall Street Oasis thread, a Trustpilot page, a Reddit discussion, an LinkedIn company page, a press article — any of these count as a third-party signal. **A brand with zero third-party footprint is a red flag.** Either the brand is too new to verify, or it doesn't exist.

### Step 4: For named individuals, verify the LinkedIn

If you're naming a person (e.g., "Sam Shiah, founder of Wall Street Mastermind"), confirm the LinkedIn profile or a credible bio page that ties the person to the entity. Do not assert someone's background or firm history without verifying.

### Step 5: For specific deals, verify both parties

Naming an M&A deal in an article? Confirm the acquirer, target, deal size, and at least one of the advisors via a press release, an SEC filing, or a published deal database. Generic deal names ("the recent healthcare M&A wave") don't need verification; specific deals do.

## What to do when verification fails

If verification fails at any step, you have three options, in order of preference:

1. **Remove the entity from the article entirely.** Replace with a verified alternative or restructure the section so the named entity isn't needed.
2. **Replace with a verified alternative.** If the article needs a coach / firm / tool in that slot, swap to one that passes verification.
3. **NEVER:** Ship the article with a placeholder, a `[VERIFY: ...]` tag in place of actual verification, or a hedge like "platforms like X" where X is unverified. The reader doesn't read VERIFY tags. They read the brand name and click the link.

## Pre-delivery audit checklist

Before any article moves from `drafts/` to `published/`, run this checklist:

- [ ] Every named coach, mentorship platform, or training program has a verified URL.
- [ ] Every named firm outside Tier 1 has been confirmed via web search and the firm's own site.
- [ ] Every named individual has been confirmed via LinkedIn or a credible bio.
- [ ] Every named deal has acquirer + target + at least one advisor confirmed.
- [ ] Every URL in the article returns HTTP 200 (run `python3 scripts/check_links.py drafts/{file}.md`).
- [ ] No `[VERIFY: ...]` tag is being used as a substitute for actual verification of a name. (VERIFY tags are fine for moving targets like prices and deadlines; they are NOT fine for "does this entity exist.")

## How to add a verified entity to the WSG knowledge base

When you verify a new entity for an article, add it to one of the canonical files:

- Coaches and prep platforms → add to `consulting/sources/INDEX.md` (consulting-side) or create a new IB-side index if needed.
- Boutique consulting firms → add to `consulting/firm-profiles/boutiques.md`.
- Recruiting firms / headhunters → add to the relevant deep dive.
- Books and tools → add to the relevant style-guide or skill file.

The audit work compounds: an entity verified once doesn't need re-verification in the next article. Build the canon as you go.

## The May 2026 fabrications (case study)

Two entries that shipped in v1 of the "Top 10 IB Career Coaches" article and would have damaged credibility:

- **"The Banker's Pillar"** — listed as an IB mentorship program. Web search returns no IB coaching service by this name. The brand was confabulated.
- **"GoodPath"** — listed as a vetted coach marketplace. The real GoodPath (goodpath.com) is a health and wellness platform, NOT an IB coaching marketplace. The brand exists but in a different industry; the article would have linked to the wrong company.

Both were caught and replaced with verified entities (Wall Street Prep Coaching, Leland) in v1-rev2. The cost would have been a 404 click for "Banker's Pillar" and a confused click to a health-tech site for "GoodPath" — both signals that WSG hadn't done its work. **This protocol exists so the next batch doesn't repeat the mistake.**

## When to skip this skill

You can skip the full verification protocol when:

- The article only references Tier 1 household-name entities.
- The article is a recap or summary of content that has already been verified in a deep dive or context file.
- The user explicitly tells you to skip (e.g., "I know these are real, just write").

In all other cases, run the protocol before delivering the draft.

## Required delivery-summary format

Every article delivered to the user must close with a structured summary that distinguishes what was verified from what is provisional. The template:

```
Delivery summary
----------------
- Word count: NNNN (target X-Y)
- Em-dashes: N
- Named entities verified: N of N (list any that remain provisional)
- URLs verified live: N of N (list any 404s)
- VERIFY tags remaining: N (list each one and why it's kept)
- Compliance check: PASS / FAIL with specific failures
```

If any line says FAIL or any unverified entity remains, the article does not ship until the gap is closed or the user explicitly accepts the risk.

## The verification subagent pattern

For high-stakes articles (Top N lists, firm comparisons, anything naming 5+ third-party entities), spawn an independent verification subagent BEFORE delivering the article. The subagent does not see your draft — it gets only the list of named entities and the questions to verify.

Subagent prompt template:

```
Verify the following named entities exist and match the descriptions provided.
For each one, report PASS (verified via official site + at least one third-party source)
or FAIL (cannot verify; likely fabricated or wrong URL).

Entities:
1. {Name 1} — described as: {short description}
2. {Name 2} — described as: {short description}
...

For each FAIL, suggest a verified alternative if one exists in the same category.
Report in under 250 words.
```

Spawn via the Agent tool with subagent_type="general-purpose". The subagent's independent fresh eyes catch fabrications a self-review pass misses.

## Workaround: bash heredoc when Edit / Write desync

Cowork's Edit/Write tool and the bash tool sometimes operate against slightly different filesystem snapshots. Symptom: Edit appears to succeed (returns "file state is current") but bash sees a truncated or older version. This breaks builds that go through bash.

When writing or rewriting any file larger than ~5KB or when the file has been edited multiple times in the same turn:

1. Use `cat > /path/to/file << 'MDEOF' ... MDEOF` via bash directly.
2. Reserve the Edit tool for ≤ 5-line surgical changes where the surrounding context was Read in the same turn.
3. After any Edit on a file > 1KB, verify via `wc -l` and `tail` in bash before proceeding to a build step that uses the file.

This is a tool limitation in the current Cowork setup, not a project rule. Document the symptom if you hit it so we know whether the limitation has been fixed.
