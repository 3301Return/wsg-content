# WSG Consulting Context Bundle

This folder is the source of truth for any WSG article in the **consulting** vertical. It runs in parallel to the IB content and inherits every editorial rule from `style-guide/` and `.claude-skill/SKILL.md`. The consulting-specific rules live in `.claude-skill/consulting.md`.

## What lives here

```
consulting/
├── README.md                          # this file
├── firm-profiles/
│   ├── mbb.md                         # McKinsey, BCG, Bain — the three firms most readers ask about
│   ├── tier-2-strategy.md             # OW, Strategy&, Kearney, LEK, Roland Berger, Accenture Strategy
│   ├── big-4-strategy.md              # Monitor Deloitte, EY-Parthenon, PwC Strategy&, KPMG
│   ├── boutiques.md                   # Putnam, ZS, Simon-Kucher, Altman Solon, Health Advances, etc.
│   └── economic-consulting.md         # Analysis Group, Cornerstone, NERA, Compass Lexecon, Bates White
├── recruiting-timeline.md             # The undergrad recruiting cycle, MBB-anchored
├── case-interview-frameworks.md       # Profitability, market entry, M&A, ops, market sizing
├── voice-cues.md                      # Consulting-specific voice rules layered on top of the WSG style guide
└── sources/
    ├── INDEX.md                       # Catalog of every external source used to build this bundle
    └── _raw/                          # PDF extracts (UChicago 2020 guide, Vault 2007 guide)
```

## How to use it when writing an article

1. **Read `.claude-skill/consulting.md`** before drafting any consulting article. It tells you the byline rule (mix: first-person on recruiting/pipeline, operator framing on firm comparisons), the firm-list defaults, and the case-interview vocabulary.
2. **Pull from the firm-profile file** matching the article's scope. If the article is "Top 10 Strategy Firms for Undergrads," read all five profile files. If the article is "How to Get Into McKinsey," read `mbb.md` only.
3. **For any recruiting-timeline claim, read `recruiting-timeline.md`** and cite the specific cycle the article targets.
4. **For any case-interview article, read `case-interview-frameworks.md`** for the canonical framework set.
5. **Cite from `sources/INDEX.md`.** Every factual claim that comes from a public source should be traceable. Use the source index to grab evergreen URLs (Dartmouth Career Design, Tufts career center, MIT Sloan CDO, university career pages) rather than rotating blog posts.

## What this bundle is NOT

- Not a deep dive. Deep dives go in `deep-dives/consulting/` and are long-form internal guides that spawn multiple articles. The bundle is canonical reference material.
- Not a content calendar. The keyword + headline plan still lives in `content-calendar/`.
- Not a writer profile. Stephen Turban's profile is at `writers/stephen-turban.md`. This bundle assumes you've already loaded that.

## Open update commitments

The MBB recruiting timeline shifts every year. Run a freshness check on `recruiting-timeline.md` in February of any cycle year before publishing a recruiting article — the 2026 cycle moved deadlines up by 2-4 months. Don't trust the bundle on a fast-moving recruiting deadline without verifying the firm's current career page or a 2026+ university career-center post.
