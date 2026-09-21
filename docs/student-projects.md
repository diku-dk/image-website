---
layout: page
title: Student Projects
permalink: /student-projects/
---
The IMAGE section regularly publishes project opportunities for BSc and MSc students. 

The board below shows the current projects. This board is a read-only showcase: if you are interested in a project, contact the supervisor directly by e-mail.

<style>
  .post-title,
  .post-content h1 {
    font-size: 1.5em;
    line-height: 1.25;
  }
  .project-board {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 20px;
    margin-top: 24px;
  }
  .project-card {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
    background: #fff;
    display: flex;
    flex-direction: column;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  }
  .project-card img {
    width: 100%;
    height: 160px;
    object-fit: cover;
    display: block;
  }
  .project-card .project-body {
    padding: 12px 16px 16px 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex: 1;
  }
  .post-content .project-card h3 {
    margin: 0;
    font-size: 1.05em;
    line-height: 1.3;
  }
  .project-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .project-badge {
    font-size: 0.72em;
    font-weight: bold;
    letter-spacing: 0.04em;
    padding: 2px 8px;
    border-radius: 10px;
    background: #eef2f7;
    color: #33475b;
  }
  .project-badge.status-open { background: #d9f2e3; color: #1c6b3a; text-transform: uppercase; }
  .project-badge.status-taken { background: #eceff1; color: #78909c; text-transform: uppercase; }
  .project-badge-level { background: #e8f0fe; color: #1a56a8; }
  .project-badge-topic { background: #f3e8fd; color: #6b3fa0; }
  .project-card p.project-description {
    margin: 0;
    font-size: 0.9em;
    flex: 1;
  }
  .project-supervisor {
    margin: 0;
    font-size: 0.85em;
    color: #555;
  }
  .project-card.is-hidden {
    display: none;
  }
  .project-filters {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    gap: 16px;
    margin-top: 20px;
  }
  .project-filter {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .project-filter-label {
    font-size: 0.78em;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #33475b;
  }
  .project-filter select {
    padding: 5px 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background: #fff;
    font-size: 0.9em;
    color: #333;
  }
  .project-filter-options {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .project-chip {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    border: 1px solid #ccc;
    border-radius: 14px;
    background: #fff;
    font-size: 0.85em;
    color: #333;
    cursor: pointer;
    user-select: none;
  }
  .project-chip input {
    margin: 0;
  }
  .project-chip.is-active {
    background: #33475b;
    border-color: #33475b;
    color: #fff;
  }
  .project-reset {
    padding: 6px 16px;
    border: none;
    border-radius: 14px;
    background: #33475b;
    color: #fff;
    font-size: 0.85em;
    font-weight: bold;
    letter-spacing: 0.03em;
    cursor: pointer;
    transition: background 0.15s ease, transform 0.05s ease;
  }
  .project-reset:hover {
    background: #26394a;
  }
  .project-reset:active {
    transform: translateY(1px);
  }
  .project-reset:focus-visible {
    outline: 2px solid #33475b;
    outline-offset: 2px;
  }
  .project-count {
    margin: 12px 0 0 0;
    font-size: 0.85em;
    color: #555;
  }
</style>

<div class="project-filters" id="project-filters" hidden>
  <div class="project-filter">
    <label class="project-filter-label" for="filter-status">Status</label>
    <select id="filter-status" data-filter="status"><option value="">All</option></select>
  </div>
  <div class="project-filter">
    <span class="project-filter-label">Level</span>
    <div class="project-filter-options" id="filter-levels"></div>
  </div>
  <div class="project-filter">
    <span class="project-filter-label">Topic</span>
    <div class="project-filter-options" id="filter-topics"></div>
  </div>
  <button type="button" class="project-reset" id="project-reset">Reset</button>
</div>
<p class="project-count" id="project-count"></p>
<p class="project-empty" id="project-empty" hidden>No projects match the selected filters.</p>

<div class="project-board">
  {% assign sorted_projects = site.data.student_projects | sort: "status" %}
  {% for project in sorted_projects %}
  <div class="project-card" data-status="{{ project.status | default: '' }}" data-levels="{{ project.levels | join: '|' }}" data-topics="{{ project.topics | join: '|' }}">
    {% if project.image %}
    <img src="{{ site.baseurl }}/{{ project.image }}" alt="{{ project.title }}">
    {% endif %}
    <div class="project-body">
      <h3>{{ project.title }}</h3>
      <div class="project-badges">
        {% if project.status %}<span class="project-badge status-{{ project.status }}">{{ project.status }}</span>{% endif %}
        {% for level in project.levels %}<span class="project-badge project-badge-level">{{ level }}</span>{% endfor %}
        {% for topic in project.topics %}<span class="project-badge project-badge-topic">{{ topic }}</span>{% endfor %}
      </div>
      <p class="project-description">{{ project.description }}</p>
      <p class="project-supervisor">
        Supervisor: {{ project.supervisor }}
        {% if project.contact %}(<a href="mailto:{{ project.contact }}">{{ project.contact }}</a>){% endif %}
        {%- if project.paper_link %} &middot; <a href="{{ project.paper_link }}">paper</a>{% endif -%}
        {%- if project.code_link %} &middot; <a href="{{ project.code_link }}">code</a>{% endif -%}
      </p>
    </div>
  </div>
  {% endfor %}
</div>

<script>
(function () {
  var board = document.querySelector('.project-board');
  if (!board) return;

  var cards = Array.prototype.slice.call(board.querySelectorAll('.project-card'));
  var filters = document.getElementById('project-filters');
  var count = document.getElementById('project-count');
  var empty = document.getElementById('project-empty');
  var statusSelect = document.querySelector('select[data-filter="status"]');

  function uniqueValues(attribute) {
    var values = [];
    cards.forEach(function (card) {
      (card.getAttribute(attribute) || '').split('|').forEach(function (value) {
        if (value && values.indexOf(value) === -1) values.push(value);
      });
    });
    return values.sort(function (a, b) { return a.localeCompare(b); });
  }

  function buildChips(container, attribute) {
    if (!container) return;

    uniqueValues(attribute).forEach(function (value) {
      var label = document.createElement('label');
      label.className = 'project-chip';

      var checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.value = value;
      checkbox.setAttribute('data-filter', attribute);
      checkbox.addEventListener('change', function () {
        label.classList.toggle('is-active', checkbox.checked);
        applyFilters();
      });

      label.appendChild(checkbox);
      label.appendChild(document.createTextNode(' ' + value));
      container.appendChild(label);
    });
  }

  buildChips(document.getElementById('filter-levels'), 'data-levels');
  buildChips(document.getElementById('filter-topics'), 'data-topics');

  if (statusSelect) {
    uniqueValues('data-status').forEach(function (value) {
      var option = document.createElement('option');
      option.value = value;
      option.textContent = value.charAt(0).toUpperCase() + value.slice(1);
      statusSelect.appendChild(option);
    });
    statusSelect.addEventListener('change', applyFilters);
  }

  function selectedValues(attribute) {
    return Array.prototype.slice
      .call(document.querySelectorAll('input[data-filter="' + attribute + '"]:checked'))
      .map(function (input) { return input.value; });
  }

  function matchesAny(card, attribute, selected) {
    if (selected.length === 0) return true;
    var values = (card.getAttribute(attribute) || '').split('|');
    return selected.some(function (value) { return values.indexOf(value) !== -1; });
  }

  function applyFilters() {
    var selectedLevels = selectedValues('data-levels');
    var selectedTopics = selectedValues('data-topics');
    var status = statusSelect ? statusSelect.value : '';
    var visible = 0;

    cards.forEach(function (card) {
      var matches =
        (!status || card.getAttribute('data-status') === status) &&
        matchesAny(card, 'data-levels', selectedLevels) &&
        matchesAny(card, 'data-topics', selectedTopics);
      card.classList.toggle('is-hidden', !matches);
      if (matches) visible++;
    });

    count.textContent = 'Showing ' + visible + ' of ' + cards.length + ' projects';
    empty.hidden = visible !== 0;
  }

  document.getElementById('project-reset').addEventListener('click', function () {
    document.querySelectorAll('input[data-filter]:checked').forEach(function (input) {
      input.checked = false;
      input.parentNode.classList.remove('is-active');
    });
    if (statusSelect) statusSelect.value = '';
    applyFilters();
  });

  filters.hidden = false;
  applyFilters();
})();
</script>
