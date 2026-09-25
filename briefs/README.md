# Briefs

One brief per article. The brief is the source of truth for what gets written.

## How to use

1. Copy `_brief-template.md` (in the `templates/` folder) to this folder
2. Rename it to match the article (e.g., `brief-how-hard-is-restructuring.md`)
3. Fill in the fields
4. Tell Claude: "Write the WSG article from `briefs/brief-how-hard-is-restructuring.md`"

The generator will load the brief, apply the right template based on the format you specified, pull the matching samples from `samples/`, and produce the draft in `drafts/`.

## When you don't need a brief

If you just want a quick article and don't want to fill out a brief, you can tell Claude:

> "Write a WSG listicle on the top 8 free modeling resources for 2026, target keyword 'free financial modeling resources', for sophomores."

The skill will infer the brief from your message and ask anything missing before drafting.
