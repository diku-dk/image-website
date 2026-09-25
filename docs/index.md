---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title:
layout: page
title: Image section
permalink: /
---
## Image Analysis, Computational Modelling, and Geometry

![Image Section Logo](assets/img/ImageLogo.png)

The IMAGE section hosts researchers in image analysis and processing, computer vision, computer simulation, numerical optimization, machine learning, computational modelling, geometry and geometric statistics. The work ranges from theoretical analyses, over algorithm development, to solving concrete problems for science, industry and society. We are part of the recently launched SCIENCE AI Centre at the University of Copenhagen.

For formal information about the IMAGE section please look at our department  [web-site](https://di.ku.dk/english/research/image/). On this site we present public complementary information. Private information for employees can be found on [github](https://github.com/diku-dk/IMAGE).

Want to see what we do? Have a look at some of our publications.

<style>
  .post-title,
  .post-content h1 {
    font-size: 2.5em;
    line-height: 1.25;
  }
  .post .post-content h2 {
    font-size: 2em;
  }
  .latest-pubs {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin: 14px 0;
  }
  .latest-pub {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    border: 1px solid #e0e0e0;
    border-left: 3px solid #33475b;
    border-radius: 6px;
    background: #fff;
    padding: 7px 12px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    color: inherit;
    text-decoration: none;
  }
  .latest-pub:hover .latest-pub-title {
    text-decoration: underline;
  }
  .latest-pub-year {
    flex: 0 0 auto;
    font-size: 0.65em;
    font-weight: bold;
    padding: 2px 7px;
    border-radius: 9px;
    background: #e8f0fe;
    color: #1a56a8;
  }
  .post-content .latest-pub-title {
    margin: 0;
    font-size: 0.85em;
    line-height: 1.3;
  }
  .latest-pub-meta {
    margin: 1px 0 0 0;
    font-size: 0.75em;
    color: #555;
  }
</style>

<div class="latest-pubs">
  {% assign latest_pubs = site.data.publications | slice: 0, 5 %}
  {% for publication in latest_pubs %}
  <a class="latest-pub" href="https://scholar.google.com/scholar?q={{ publication.title | url_encode }}" target="_blank" rel="noopener noreferrer" title="Search on Google Scholar">
    <span class="latest-pub-year">{{ publication.year }}</span>
    <div>
      <h3 class="latest-pub-title">{{ publication.title }}</h3>
      <p class="latest-pub-meta">{{ publication.author }}{% if publication.journal != "" %} &middot; {{ publication.journal }}{% endif %}</p>
    </div>
  </a>
  {% endfor %}
</div>

[All publications &rarr;]({{ site.baseurl }}{% link publications.md %})

## Student Projects
The section regularly publishes projects for BSc and MSc students.

- [Student Projects]({{ site.baseurl }}{% link student-projects.md %})

## Infrastructure
IMAGE provides a wide range of physical and virtual reserach infrastructure. 

- [Robot lab space]({{ site.baseurl }}{% link robotlab.md %})
- [Toolshop]({{ site.baseurl }}{% link toolshop.md %})
- [GPU Cluster]({{ site.baseurl }}{% link cluster.md %})

## Open Data and Open Source
Researchers from IMAGE has been part of creating many open source projects and data-sets that are freely available online. Below is a subset of those repositories.

- [Open-Full-Jaw](https://github.com/diku-dk/Open-Full-Jaw)
- [CarGen](https://github.com/diku-dk/CarGen)
- [LibHip](https://github.com/diku-dk/libhip)
- [DiffCal](https://github.com/diku-dk/DiffCal)
- [OpenTissue](https://github.com/erleben/OpenTissue)
- [PROX](https://github.com/diku-dk/PROX) 
- [PROX MATCHSTICK](https://github.com/erleben/matchstick)
- [Num4LCP](https://github.com/erleben/num4lcp)
- [HessianIK](https://github.com/sheldona/hessianIK)
- [libRAINBOW](https://github.com/diku-dk/libRAINBOW)


