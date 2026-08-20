# Writers

One Markdown file per WSG contributor. The generator loads the matching profile when an article is assigned to a specific byline, then writes in that writer's actual voice using their real background instead of the generic "IB analyst" persona.

## How to use

1. Copy `_template.md` to `writers/{slug}.md` (kebab-case, e.g., `writers/erin-bettigole.md`).
2. Fill in the fields. Specifics matter more than completeness.
3. When you assign an article, say: *"Write the WSG article from `briefs/brief-{slug}.md`, byline Erin Bettigole."* The generator will load `writers/erin-bettigole.md` automatically.

## Why this exists

The current samples are all written in the same "IB analyst with offers at Goldman, JPM, MS, Evercore" persona. Without a writer profile, the AI defaults to that voice for every article, regardless of who the byline says. That is the single biggest reason WSG articles can still read like AI even when they pass the style guide.

A writer profile fixes this by:

- Replacing the default persona with the writer's actual background
- Providing real scenarios the writer has used in past articles (the credibility moments)
- Flagging topics the writer should not write about (outside their expertise)
- Capturing voice tells unique to the writer (phrasing patterns, structural quirks)

## Priority writers to profile first

Based on the content calendar (Mar 30, 2026), these writers have multiple active or upcoming assignments and should be profiled before more articles ship:

- Erin Bettigole (IB industry background)
- Jackson Laite (IB recruitment manager)
- Kevin Huang (M&A background, technical voice)
- Veronika Raiffe (recruitment manager, compliance/risk perspective)
- Fin Panton (sales and trading / markets)
- Bhumika Bhadriraju (consulting recruitment)
- Giovanni Coeli (consulting industry)
- Arjun Kalyandurg (asset and wealth management, GS interview firsthand)
- Reya (consulting, junior writer)
- Akanksha (general finance editor)
- Nikson (founder, IB mentor — current de facto byline)

Profiles do not need to be long. Half a page per writer is usually enough.
