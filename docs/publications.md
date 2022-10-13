---
layout: page
title: Publications
permalink: /publications/
---

<table border="0" cellspacing="0" cellpadding="0">
  {% for publication in site.data.publications %}
  <tr valign="top">
    <td>
      {{publication.author}}: {{publication.title}}, {{publication.journal}}, {{publication.year}}.<br>
      {% if publication.paper_link %}
      <a href="{{publication.paper_link}}">paper</a>
      {% endif %}
      {% if publication.code_link %}
      <a href="{{publication.code_link}}">code</a>
      {% endif %}
      {% if publication.video_link %}
      <a href="{{publication.video_link}}">video</a>
      {% endif %}
    </td>
  </tr>  
  {% endfor %}
</table>