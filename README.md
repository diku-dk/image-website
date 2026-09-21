# Scope

The files within the docs folder are publicly displayed on the Image section's website.

# Add publications

To include your latest publications from Google Scholar, update the list of author ids included in the "env" file. To find your author id, navigate to your google scholar page and extract the id from the "user" query parameter in the URL. "user=<your_id>". Then, include a comma followed by your author id in the env > AUTHOR list, i.e ",<your_id>".

For more details regarding the scraping mechanism, refer to [scholar-scraper](https://github.com/tudordascalu/scholar-scraper).

The monthly workflow merges newly scraped publications into `docs/_data/publications.yml` instead of replacing the file, so entries that the scraper no longer returns (for example older publications) are kept.

The homepage shows the first five entries of `docs/_data/publications.yml`, i.e. the most recent publications by year in the order they appear in the file. The monthly merge keeps the newest scrape at the top of the file. Ordering within the same year is not meaningful: the scraper shuffles entries before sorting them by year.

# Add student projects

Student projects are listed on the "Student Projects" page from the data file `docs/_data/student_projects.yml`. To publish a project, append an entry with a title, description, supervisor, contact e-mail, levels, topics, and status ("open" or "taken"). `levels` and `topics` are YAML lists, so a project can target several levels and cover several topics. Put the card cover image in `docs/assets/img/projects/` and reference it from the entry as `assets/img/projects/<file>`. Projects with status "open" are listed first. Changes take effect once the change is merged to the main branch.

The status, level, and topic filters are generated automatically from the entries, and the level and topic filters allow selecting several values at once. Use consistent spelling (e.g. always "Master Thesis") so projects group correctly.

The current entries were imported from the [Projects4Students Trello board](https://trello.com/b/GVhtdARX/projects4students): all projects to the left of the "Supervisors to the right do not accept projects" divider are listed. Levels come from the board's color labels, and topics were derived from the project descriptions.

# Development

Follow [the jekyll website tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) to develop and compile the pages locally.

# Run site locally

To run the site locally, we can use docker.

Build the image:

    docker build -t image-site docs

Serve the site:

    docker run --rm -p 4000:4000 -v "$PWD/docs:/site" -w /site image-site bundle exec jekyll serve --host 0.0.0.0 --destination /tmp/_site

The site is then available at http://localhost:4000/image-website/ (the new page is at http://localhost:4000/image-website/student-projects/).