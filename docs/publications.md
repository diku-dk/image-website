---
layout: page
title: Publications
permalink: /publications/
---

Browse the section's publications. Newest first, one year at a time. Use the search box to filter by title, author, or venue.

<style>
  .post-title,
  .post-content h1 {
    font-size: 1.5em;
    line-height: 1.25;
  }
  .pub-controls {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    margin-top: 20px;
  }
  .pub-search {
    flex: 1 1 260px;
    padding: 8px 14px;
    border: 1px solid #ccc;
    border-radius: 16px;
    background: #fff;
    font-size: 0.95em;
    color: #333;
  }
  .pub-search:focus {
    outline: 2px solid #33475b;
    outline-offset: 1px;
    border-color: #33475b;
  }
  .post-content .pub-year-heading {
    margin: 28px 0 14px 0;
    padding-bottom: 6px;
    border-bottom: 2px solid #e0e0e0;
    font-size: 1.25em;
    color: #33475b;
  }
  .pub-cards {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .pub-card {
    border: 1px solid #e0e0e0;
    border-left: 4px solid #33475b;
    border-radius: 8px;
    background: #fff;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
    transition: transform 0.1s ease, box-shadow 0.15s ease;
    color: inherit;
    text-decoration: none;
  }
  .pub-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  .pub-card.is-hidden,
  .pub-year-group.is-hidden {
    display: none;
  }
  .post-content .pub-title {
    margin: 0;
    font-size: 0.9em;
    line-height: 1.3;
  }
  .pub-card:hover .pub-title {
    text-decoration: underline;
  }
  .pub-authors {
    margin: 0;
    font-size: 0.85em;
    color: #555;
    flex: 1;
  }
  .pub-venue {
    margin: 0;
  }
  .pub-venue-badge {
    display: inline-block;
    font-size: 0.72em;
    font-weight: bold;
    letter-spacing: 0.04em;
    padding: 2px 8px;
    border-radius: 10px;
    background: #e0f2f1;
    color: #00695c;
  }
  .pub-count {
    margin: 10px 0 0 0;
    font-size: 0.85em;
    color: #555;
  }
  .pub-more {
    display: block;
    margin: 20px auto 0 auto;
    padding: 8px 20px;
    border: none;
    border-radius: 16px;
    background: #33475b;
    color: #fff;
    font-size: 0.9em;
    font-weight: bold;
    letter-spacing: 0.03em;
    cursor: pointer;
    transition: background 0.15s ease, transform 0.05s ease;
  }
  .pub-more:hover {
    background: #26394a;
  }
  .pub-more:active {
    transform: translateY(1px);
  }
  .pub-more:focus-visible {
    outline: 2px solid #33475b;
    outline-offset: 2px;
  }
  .pub-empty {
    margin: 20px 0 0 0;
    font-size: 0.9em;
    color: #555;
  }
</style>

<div class="pub-controls">
  <input type="search" class="pub-search" id="pub-search" placeholder="Search by title, author, or venue" aria-label="Search publications">
</div>
<p class="pub-count" id="pub-count"></p>
<p class="pub-empty" id="pub-empty" hidden>No publications match your search.</p>

<div id="pub-list">
  {% assign years = site.data.publications | map: "year" | uniq | sort | reverse %}
  {% for year in years %}
  <section class="pub-year-group">
    <h2 class="pub-year-heading">{{ year }}</h2>
    <div class="pub-cards">
      {% assign year_pubs = site.data.publications | where: "year", year %}
      {% for publication in year_pubs %}
      <a class="pub-card" href="https://scholar.google.com/scholar?q={{ publication.title | url_encode }}" target="_blank" rel="noopener noreferrer" title="Search on Google Scholar" data-search="{{ publication.title | downcase | escape }} {{ publication.author | downcase | escape }} {{ publication.journal | downcase | escape }} {{ publication.year }}">
        <h3 class="pub-title">{{ publication.title }}</h3>
        <p class="pub-authors">{{ publication.author }}</p>
        {% if publication.journal != "" %}
        <p class="pub-venue"><span class="pub-venue-badge">{{ publication.journal }}</span></p>
        {% endif %}
      </a>
      {% endfor %}
    </div>
  </section>
  {% endfor %}
</div>

<button type="button" class="pub-more" id="pub-more">Show more</button>

<script>
(function () {
  var PAGE_SIZE = 12;
  var list = document.getElementById('pub-list');
  if (!list) return;

  var cards = Array.prototype.slice.call(list.querySelectorAll('.pub-card'));
  var groups = Array.prototype.slice.call(list.querySelectorAll('.pub-year-group'));
  var search = document.getElementById('pub-search');
  var count = document.getElementById('pub-count');
  var more = document.getElementById('pub-more');
  var empty = document.getElementById('pub-empty');
  var limit = PAGE_SIZE;

  function matches(card) {
    var query = (search.value || '').trim().toLowerCase();
    return !query || card.getAttribute('data-search').indexOf(query) !== -1;
  }

  function apply() {
    var matched = cards.filter(matches);
    var visible = 0;

    cards.forEach(function (card) {
      var show = matched.indexOf(card) !== -1 && matched.indexOf(card) < limit;
      card.classList.toggle('is-hidden', !show);
      if (show) visible++;
    });

    groups.forEach(function (group) {
      group.classList.toggle('is-hidden', !group.querySelector('.pub-card:not(.is-hidden)'));
    });

    count.textContent = 'Showing ' + visible + ' of ' + matched.length + ' publications';
    empty.hidden = matched.length !== 0;
    more.hidden = matched.length <= limit;
    if (!more.hidden) more.textContent = 'Show more (' + (matched.length - limit) + ' remaining)';
  }

  search.addEventListener('input', function () {
    limit = PAGE_SIZE;
    apply();
  });

  more.addEventListener('click', function () {
    limit += PAGE_SIZE;
    apply();
  });

  apply();
})();
</script>
