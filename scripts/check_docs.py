#!/usr/bin/env python3
"""Offline documentation checks for README Badges (Python 3.9+, stdlib only).

Checks local links/anchors, translation parity, catalog counts, static badge
syntax, and image alt text. Optionally validates named logos against the
Simple Icons data file: --simple-icons /path/to/simple-icons.json.

This is intentionally not a network health checker. A syntactically valid
third-party URL can still be unavailable, rate-limited, or misconfigured.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TRANSLATIONS = (
    "docs/i18n/README.es.md",
    "docs/i18n/README.pt-BR.md",
    "docs/i18n/README.ru.md",
    "docs/i18n/README.zh-CN.md",
    "docs/i18n/README.ja.md",
)
CATALOG = ROOT / "docs/BADGE_CATALOG.md"
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
LINK_RE = re.compile(r"\[[^\[\]]*\]\(([^)\s]+)\)")
LINKED_IMAGE_RE = re.compile(r"\[!\[[^\]]*\]\([^)]+\)\]\(([^)\s]+)\)")
CSS_COLORS = set("""
aliceblue antiquewhite aqua aquamarine azure beige bisque black blanchedalmond
blue blueviolet brown burlywood cadetblue chartreuse chocolate coral
cornflowerblue cornsilk crimson cyan darkblue darkcyan darkgoldenrod darkgray
darkgreen darkgrey darkkhaki darkmagenta darkolivegreen darkorange darkorchid
darkred darksalmon darkseagreen darkslateblue darkslategray darkslategrey
darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue
firebrick floralwhite forestgreen fuchsia gainsboro ghostwhite gold goldenrod
gray green greenyellow grey honeydew hotpink indianred indigo ivory khaki
lavender lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan
lightgoldenrodyellow lightgray lightgreen lightgrey lightpink lightsalmon
lightseagreen lightskyblue lightslategray lightslategrey lightsteelblue
lightyellow lime limegreen linen magenta maroon mediumaquamarine mediumblue
mediumorchid mediumpurple mediumseagreen mediumslateblue mediumspringgreen
mediumturquoise mediumvioletred midnightblue mintcream mistyrose moccasin
navajowhite navy oldlace olive olivedrab orange orangered orchid palegoldenrod
palegreen paleturquoise palevioletred papayawhip peachpuff peru pink plum
powderblue purple rebeccapurple red rosybrown royalblue saddlebrown salmon
sandybrown seagreen seashell sienna silver skyblue slateblue slategray slategrey
snow springgreen steelblue tan teal thistle tomato turquoise violet wheat white
whitesmoke yellow yellowgreen transparent currentcolor
""".split()) | {
    "brightgreen", "success", "important", "critical", "informational", "inactive"
}


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def fenced_blocks(text: str) -> list[str]:
    return re.findall(r"^```[^\n]*\n(.*?)^```\s*$", text, re.M | re.S)


def heading_anchors(text: str) -> set[str]:
    """Approximate GitHub slugs; explicit HTML IDs are also supported."""
    anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    seen: Counter[str] = Counter()
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not re.match(r"^#{1,6}\s", line):
            continue
        heading = re.sub(r"^#{1,6}\s+", "", line).lower()
        heading = re.sub(r"[^\w\s-]", "", heading, flags=re.UNICODE)
        heading = heading.replace(" ", "-")
        suffix = seen[heading]
        seen[heading] += 1
        anchors.add(heading if not suffix else f"{heading}-{suffix}")
    return anchors


def local_destinations(text: str) -> list[str]:
    # Remove fenced examples: placeholder links inside them are not navigation.
    text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
    text = re.sub(r"`[^`\n]+`", "", text)
    return LINK_RE.findall(text) + LINKED_IMAGE_RE.findall(text)


def valid_color(value: str) -> bool:
    color = unquote(value).lower()
    if color in CSS_COLORS:
        return True
    if color.startswith("#"):
        color = color[1:]
    return bool(re.fullmatch(r"[0-9a-f]{3}|[0-9a-f]{4}|[0-9a-f]{6}|[0-9a-f]{8}", color))


def check_links(path: Path, text: str, anchors: dict[Path, set[str]], errors: list[str]) -> None:
    for raw in local_destinations(text):
        url = urlsplit(raw)
        if url.scheme or url.netloc:
            continue
        target = path.parent / unquote(url.path) if url.path else path
        try:
            target = target.resolve()
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: local link escapes repository: {raw}")
            continue
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing local link target: {raw}")
        elif url.fragment and target.suffix == ".md":
            if unquote(url.fragment) not in anchors.get(target, set()):
                errors.append(f"{path.relative_to(ROOT)}: missing anchor: {raw}")


def check_catalog(text: str, logo_slugs: set[str] | None, errors: list[str]) -> tuple[int, int]:
    badges = IMAGE_RE.findall(text)
    categories = re.findall(r"^## (.+)$", text, re.M)
    categories = [h for h in categories if h != "Contents"]
    declared = re.search(r"\*\*(\d+) copy-paste Markdown badges\*\*", text)
    if not declared or int(declared[1]) != len(badges):
        errors.append(f"Catalog count mismatch: declared {declared[1] if declared else '?'}, actual {len(badges)}")
    for alt, url in badges:
        if not alt.strip():
            errors.append(f"Catalog: empty alt text: {url}")
        parsed = urlsplit(url)
        if parsed.scheme != "https" or parsed.netloc != "img.shields.io" or not parsed.path.startswith("/badge/"):
            errors.append(f"Catalog: expected a static HTTPS Shields badge: {url}")
            continue
        if parsed.fragment:
            errors.append(f"Catalog: unexpected URL fragment (unescaped #?): {url}")
        query = parse_qs(parsed.query, keep_blank_values=True)
        if query.get("style") != ["for-the-badge"]:
            errors.append(f"Catalog: inconsistent/missing style: {url}")
        if "logoColor" in query and "logo" not in query:
            errors.append(f"Catalog: logoColor without logo: {url}")
        if logo_slugs is not None and "logo" in query:
            slug = unquote(query["logo"][0])
            if slug not in logo_slugs:
                errors.append(f"Catalog: unknown current Simple Icons slug {slug!r}: {url}")
        path = re.sub(r"\.svg$", "", parsed.path[len("/badge/"):])
        fields = re.split(r"(?<!-)-(?!-)", path)
        if len(fields) not in (2, 3):
            errors.append(f"Catalog: ambiguous static fields; check hyphen escaping: {url}")
        elif not valid_color(fields[-1]):
            errors.append(f"Catalog: invalid color {fields[-1]!r}: {url}")
    return len(badges), len(categories)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--simple-icons", type=Path, help="Optional path to Simple Icons simple-icons.json")
    args = parser.parse_args()
    errors: list[str] = []
    files = markdown_files()
    texts = {p: p.read_text(encoding="utf-8") for p in files}
    anchors = {p: heading_anchors(t) for p, t in texts.items()}
    logo_slugs = None
    if args.simple_icons:
        data = json.loads(args.simple_icons.read_text(encoding="utf-8"))
        logo_slugs = {entry["slug"] for entry in data}

    for path, text in texts.items():
        check_links(path, text, anchors, errors)
        if text.count("```") % 2:
            errors.append(f"{path.relative_to(ROOT)}: unbalanced code fences")
        if "<!-- TOC -->" in text:
            errors.append(f"{path.relative_to(ROOT)}: unresolved TOC placeholder")
        # Rendered images need alt text; code examples are templates and may vary.
        rendered = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
        for alt, url in IMAGE_RE.findall(rendered):
            if not alt.strip() and not url.endswith("height=2&"):
                errors.append(f"{path.relative_to(ROOT)}: rendered image lacks alt text: {url}")

    if not CATALOG.exists():
        errors.append("Missing docs/BADGE_CATALOG.md")
        count, categories = 0, 0
    else:
        count, categories = check_catalog(texts[CATALOG], logo_slugs, errors)

    source = texts[ROOT / "README.md"]
    source_images = Counter(url for _, url in IMAGE_RE.findall(source))
    source_fences = fenced_blocks(source)
    source_h2 = len(re.findall(r"^## ", source, re.M))
    source_table_rows = len(re.findall(r"^\|", source, re.M))
    for rel in TRANSLATIONS:
        path = ROOT / rel
        if path not in texts:
            errors.append(f"Missing translation: {rel}")
            continue
        text = texts[path]
        if Counter(url for _, url in IMAGE_RE.findall(text)) != source_images:
            errors.append(f"{rel}: image URLs differ from English README")
        if fenced_blocks(text) != source_fences:
            errors.append(f"{rel}: code examples differ from English README")
        if len(re.findall(r"^## ", text, re.M)) != source_h2:
            errors.append(f"{rel}: section count differs from English README")
        if len(re.findall(r"^\|", text, re.M)) != source_table_rows:
            errors.append(f"{rel}: table row count differs from English README")
        if str(count) not in text or str(categories) not in text:
            errors.append(f"{rel}: catalog count/category count is stale")
        if "../../README.md" not in text:
            errors.append(f"{rel}: missing link back to English README")
    if str(count) not in source or str(categories) not in source:
        errors.append("README.md: catalog count/category count is stale")

    if errors:
        print(f"Documentation checks failed ({len(errors)} issue(s)):")
        for error in errors:
            print(f"  - {error}")
        return 1
    logo_status = f"; {len(logo_slugs)} current logo slugs checked against" if logo_slugs else ""
    print(f"OK: {len(files)} Markdown files; {count} badges in {categories} categories; {len(TRANSLATIONS)} complete translations{logo_status}.")
    print("Offline checks only: external service availability and live badge values are not verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
