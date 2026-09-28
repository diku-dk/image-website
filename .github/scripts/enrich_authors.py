#!/usr/bin/env python3
"""Fill in complete author lists for publications whose author list is truncated.

Google Scholar truncates long author lists with "...", which hides authors from
the search on the publications page. This script looks each truncated entry up
in Crossref and, when that fails, falls back to the SerpApi citation endpoint.
The complete list is stored in an extra `authors_full` field, which the site
includes in its search index but does not display.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

from fetch_publications import fetch_author, read_authors

DATA = Path("docs/_data/publications.yml")
CROSSREF = "https://api.crossref.org/works"
SERPAPI = "https://serpapi.com/search.json"
PAUSE_SECONDS = 0.2
FIELD_ORDER = ["title", "author", "authors_full", "year", "journal"]


def normalize(text):
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def crossref_authors(title):
    params = {
        "query.bibliographic": title,
        "rows": 3,
        "select": "title,author",
        "mailto": "image@di.ku.dk",
    }
    url = CROSSREF + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=60) as response:
            items = json.load(response)["message"]["items"]
    except (urllib.error.URLError, json.JSONDecodeError, KeyError):
        return None

    target = normalize(title)
    for item in items:
        item_title = (item.get("title") or [""])[0]
        if normalize(item_title) != target:
            continue
        names = []
        for author in item.get("author", []):
            name = " ".join(part for part in (author.get("given"), author.get("family")) if part).strip()
            if name:
                names.append(name)
        if names:
            return ", ".join(names)
    return None


def serpapi_citation_map(api_key):
    mapping = {}
    for author_id in read_authors():
        for article in fetch_author(author_id, api_key):
            citation_id = article.get("citation_id")
            if citation_id:
                mapping.setdefault(normalize(article.get("title")), citation_id)
        time.sleep(PAUSE_SECONDS)
    return mapping


def serpapi_authors(citation_id, api_key):
    params = {
        "engine": "google_scholar_author",
        "view_op": "view_citation",
        "citation_id": citation_id,
        "hl": "en",
        "api_key": api_key,
    }
    url = SERPAPI + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=60) as response:
            data = json.load(response)
    except (urllib.error.URLError, json.JSONDecodeError):
        return None
    citation = data.get("citation") or data
    authors = (citation.get("authors") or "").strip()
    return authors or None


def main():
    entries = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    api_key = os.environ.get("SERPAPI_API_KEY")

    missing = []
    for entry in entries:
        author = entry.get("author") or ""
        if not author.rstrip().endswith("..."):
            entry.pop("authors_full", None)
            continue
        if entry.get("authors_full"):
            continue
        full = crossref_authors(entry["title"])
        if full:
            entry["authors_full"] = full
        else:
            missing.append(entry)
        time.sleep(PAUSE_SECONDS)

    from_serpapi = 0
    if missing and api_key:
        citation_map = serpapi_citation_map(api_key)
        for entry in missing:
            citation_id = citation_map.get(normalize(entry["title"]))
            if not citation_id:
                continue
            full = serpapi_authors(citation_id, api_key)
            if full:
                entry["authors_full"] = full
                from_serpapi += 1
            time.sleep(PAUSE_SECONDS)

    ordered = [{key: entry[key] for key in FIELD_ORDER if key in entry} for entry in entries]
    with DATA.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(ordered, handle, allow_unicode=True, sort_keys=False, width=1000)

    enriched = sum(1 for entry in entries if entry.get("authors_full"))
    print(f"Enriched {enriched} entries with full author lists ({from_serpapi} via SerpApi).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
