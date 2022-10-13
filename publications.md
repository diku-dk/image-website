---
layout: page
title: Publications
permalink: /publications/
publications: 
  - title: Benefits of auxiliary information in deep learning-based teeth segmentation
    author: Tudor Laurentiu Dascalu, Artem Kuznetsov, Bulat Ibragimov
    journal: SPIE
    year: 2022
    paper_link: https://doi.org/10.1117/12.2610765
    video_link: https://doi.org/10.1117/12.2610765
---

<table border="0" cellspacing="0" cellpadding="0">
  {% for publication in page.publications %}
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