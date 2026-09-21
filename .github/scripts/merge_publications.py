#!/usr/bin/env python3
"""Merge freshly scraped publications into the existing list.

The Google Scholar scraper only returns the latest publications per author, so
older entries can drop out of a new scrape. This script keeps the existing
entries and adds or updates them with the freshly scraped ones.
"""

import re
import sys
from pathlib import Path

import yaml

EXISTING = Path("docs/_data/publications.yml")
UPDATED = Path("updated-publications.yml")

FIELDS = ("title", "author", "year", "journal")


def normalize(title):
    return re.sub(r"\s+", " ", str(title or "")).strip().lower()


def clean(entry):
    return {field: entry.get(field, "") for field in FIELDS}


def load(path):
    if not path.exists():
        return []
    return yaml.safe_load(path.read_text(encoding="utf-8")) or []


def main():
    fresh = [clean(entry) for entry in load(UPDATED) if entry]
    existing = [clean(entry) for entry in load(EXISTING) if entry]

    fresh = [entry for entry in fresh if normalize(entry["title"])]
    if not fresh:
        print("Scraper returned no publications; keeping the existing file.", file=sys.stderr)
        return 1

    merged = []
    seen = set()
    for entry in fresh + existing:
        key = normalize(entry["title"])
        if not key or key in seen:
            continue
        seen.add(key)
        merged.append(entry)

    with EXISTING.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(merged, handle, allow_unicode=True, sort_keys=False, width=1000)

    print(f"Merged {len(fresh)} scraped publications into {len(merged)} total.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
