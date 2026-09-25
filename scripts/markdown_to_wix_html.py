#!/usr/bin/env python3
"""
Markdown to Wix-ready HTML converter.

Strips frontmatter, converts the body to clean HTML, and writes a sibling .html
file you can open in a browser, select-all, and paste into Wix without losing
formatting.

Usage:
    python3 scripts/markdown_to_wix_html.py published/article.md
"""

import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Need: pip install markdown --break-system-packages")
    sys.exit(1)


def strip_frontmatter(text):
    """Remove YAML frontmatter block at top of file."""
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)


def convert(md_path):
    md_path = Path(md_path)
    text = md_path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    html_body = markdown.markdown(
        body,
        extensions=["extra", "sane_lists"],
    )

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{md_path.stem}</title>
<style>
  body {{ font-family: Georgia, serif; max-width: 720px; margin: 2em auto; line-height: 1.5; padding: 0 1em; }}
  h1, h2, h3 {{ font-family: -apple-system, system-ui, sans-serif; }}
  h1 {{ font-size: 2em; }}
  h2 {{ font-size: 1.5em; margin-top: 1.5em; }}
  h3 {{ font-size: 1.2em; margin-top: 1.2em; }}
  p {{ margin: 0.8em 0; }}
  a {{ color: #0066cc; }}
  strong {{ font-weight: 700; }}
  ol, ul {{ margin: 0.8em 0; padding-left: 1.5em; }}
  li {{ margin: 0.4em 0; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""
    out_path = md_path.with_suffix(".html")
    out_path.write_text(full_html, encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"Open in a browser, select all, copy, paste into Wix.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/markdown_to_wix_html.py <file.md>")
        sys.exit(1)
    for path in sys.argv[1:]:
        convert(path)


if __name__ == "__main__":
    main()
