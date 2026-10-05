#!/usr/bin/env python3
"""Fetch publications for the authors in the env file using the SerpApi Google Scholar Author API."""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ENV_FILE = Path("env")
DATA_FILE = Path("docs/_data/publications.yml")
OUTPUT = Path("updated-publications.yml")
CITATION_IDS = Path("updated-citation-ids.json")
API_URL = "https://serpapi.com/search.json"
RESULTS_PER_PAGE = 100
MAX_PAGES = 3


def normalize(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text or "").lower()).strip()


def read_authors():
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("AUTHORS="):
            return [author for author in line[len("AUTHORS="):].split(",") if author]
    raise SystemExit("No AUTHORS= line found in env")


def read_known_titles():
    if not DATA_FILE.exists():
        return set()
    entries = yaml.safe_load(DATA_FILE.read_text(encoding="utf-8")) or []
    return {normalize(entry.get("title")) for entry in entries}


def request_page(author_id, api_key, start):
    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "hl": "en",
        "sort": "pubdate",
        "num": RESULTS_PER_PAGE,
        "start": start,
        "api_key": api_key,
    }
    url = API_URL + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as response:
        data = json.load(response)
    if "error" in data:
        raise SystemExit(f"SerpApi error for {author_id}: {data['error']}")
    return data.get("articles", [])


def fetch_author(author_id, api_key, known_titles):
    """Return the author's articles, newest first.

    Every page costs one search, so once a page ends on a title we already have we
    stop: the results are sorted by publication date, so everything after it is
    stored as well. A regular run therefore needs a single search per author.
    """
    articles = []
    for page_number in range(MAX_PAGES):
        page = request_page(author_id, api_key, page_number * RESULTS_PER_PAGE)
        articles.extend(page)
        if len(page) < RESULTS_PER_PAGE:
            break
        if normalize(page[-1].get("title")) in known_titles:
            break
        time.sleep(1)
    return articles


def clean_journal(publication):
    if not publication:
        return ""
    text = publication
    patterns = [
        r",\s*\d{4}$",
        r",\s*e?\d+([-\u2013]\d+)?$",
        r",\s*\d+\s*\(\d+\)$",
        r"\s+\d+\s*\(\d+\)$",
        r",\s*\d+$",
        r"\s+\d+$",
    ]
    while True:
        before = text
        for pattern in patterns:
            text = re.sub(pattern, "", text)
        if text == before:
            break
    return text.strip(" ,.")


def to_entry(article):
    title = (article.get("title") or "").strip()
    authors = (article.get("authors") or "").strip()
    try:
        year = int(article.get("year"))
    except (TypeError, ValueError):
        return None
    if not title or not authors:
        return None
    return {
        "title": title,
        "author": authors,
        "year": year,
        "journal": clean_journal(article.get("publication")),
    }


def main():
    api_key = os.environ.get("SERPAPI_API_KEY")
    if not api_key:
        raise SystemExit("SERPAPI_API_KEY is not set")

    known_titles = read_known_titles()
    entries = []
    seen = set()
    citation_ids = {}
    skipped = 0
    without_articles = []
    for author_id in read_authors():
        articles = fetch_author(author_id, api_key, known_titles)
        if not articles:
            without_articles.append(author_id)
            continue
        for article in articles:
            entry = to_entry(article)
            if entry is None or entry["title"].lower() in seen:
                skipped += 1
                continue
            seen.add(entry["title"].lower())
            entries.append(entry)
            citation_id = article.get("citation_id")
            if citation_id:
                citation_ids[normalize(entry["title"])] = citation_id
        time.sleep(1)

    if without_articles:
        print(
            "Warning: Google Scholar returned no articles for "
            + ", ".join(without_articles)
            + " (private or empty profile?).",
            file=sys.stderr,
        )

    if not entries:
        print("SerpApi returned no publications; keeping the existing file.", file=sys.stderr)
        return 1

    with OUTPUT.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(entries, handle, allow_unicode=True, sort_keys=False, width=1000)
    with CITATION_IDS.open("w", encoding="utf-8") as handle:
        json.dump(citation_ids, handle, sort_keys=True)

    print(f"Fetched {len(entries)} publications ({skipped} duplicates/skipped).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
