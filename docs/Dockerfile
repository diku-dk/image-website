FROM ruby:2.7-alpine3.15

# Add Jekyll dependencies to alpine
RUN apk update
RUN apk add --no-cache build-base gcc cmake git

# Install the bundler version pinned in Gemfile.lock
RUN gem install bundler -v 2.3.23

# Install the Jekyll gems pinned in Gemfile.lock
WORKDIR /site
COPY Gemfile Gemfile.lock ./
RUN bundle install
