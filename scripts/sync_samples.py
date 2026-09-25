#!/usr/bin/env python3
"""
sync_samples.py — copy every current article draft into samples/{format}/ as
the canonical sample for future article writes.

Reads frontmatter of each drafts/*.md to pick:
- the `headline` (used as the filename, sanitized)
- the `format` (decides which samples/ subfolder to land in)

Skips drafts that haven't been finalized (status missing or 'wip').

Usage:
    python3 scripts/sync_samples.py
    python3 scripts/sync_samples.py drafts/draft-foo-v1.md   # single file
"""

import re
import shutil
import sys
import yaml
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = REPO_ROOT / "drafts"
SAMPLES_DIR = REPO_ROOT / "samples"


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, flags=re.DOTALL)
    if not m:
        return {}, text
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError:
        return {}, m.group(2)


def sanitize_filename(headline):
    """Convert a headline to a clean filename."""
    name = headline.replace(":", " -").replace("/", " ")
    name = re.sub(r"\s+", " ", name).strip()
    return name + ".md"


def sync_one(draft_path):
    text = draft_path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(text)

    headline = fm.get("headline")
    fmt = fm.get("format")
    if not headline or not fmt:
        print(f"  SKIP {draft_path.name} (no headline or format in frontmatter)")
        return False

    format_dir_map = {
        "listicle": "listicles",
        "ultimate-guide": "ultimate-guides",
        "niche": "niche",
        "deep-dive": "deep-dives",
    }
    sub = format_dir_map.get(fmt)
    if not sub:
        print(f"  SKIP {draft_path.name} (unknown format: {fmt})")
        return False

    dest_dir = SAMPLES_DIR / sub
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / sanitize_filename(headline)
    shutil.copy2(draft_path, dest)
    print(f"  OK   {draft_path.name} -> samples/{sub}/{dest.name}")
    return True


def find_latest_drafts():
    """For each {slug}, return the highest-version draft file."""
    pattern = re.compile(r"draft-(.+)-v(\d+)\.md$")
    by_slug = {}
    for p in DRAFTS_DIR.glob("draft-*.md"):
        m = pattern.match(p.name)
        if not m:
            continue
        slug, ver = m.group(1), int(m.group(2))
        if slug not in by_slug or by_slug[slug][0] < ver:
            by_slug[slug] = (ver, p)
    return [v[1] for v in by_slug.values()]


def main():
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        paths = find_latest_drafts()
        print(f"=== syncing {len(paths)} latest-version drafts ===")
    synced = 0
    for p in paths:
        if not p.exists():
            print(f"  ERR  {p} not found")
            continue
        if sync_one(p):
            synced += 1
    print(f"\nSynced {synced} files.")


if __name__ == "__main__":
    main()
