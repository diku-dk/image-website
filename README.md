# Scope

The files within the docs folder are publicly displayed on the Image section's website.

# Add publications

To include your latest publications from Google Scholar, update the list of author ids included in the "env" file. To find your author id, navigate to your google scholar page and extract the id from the "user" query parameter in the URL. "user=<your_id>". Then, include a comma followed by your author id in the env > AUTHOR list, i.e ",<your_id>".

For more details regarding the scraping mechanism, refer to [scholar-scraper](https://github.com/tudordascalu/scholar-scraper).

# Development

Follow [the jekyll website tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) to develop and compile the pages locally.

# Run site locally

To run the site locally, we can use docker. 