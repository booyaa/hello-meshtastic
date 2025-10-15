# Use Ruby 3.4.x official image
FROM ruby:3.4.1-slim

# Install essential dependencies
RUN apt-get update -qq && \
    apt-get install -y build-essential git && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Gemfile and Gemfile.lock
COPY Gemfile Gemfile.lock ./

# Install bundler and gems
RUN gem install bundler && \
    bundle install

# Copy the application code
COPY . .

# Run the Ruby application
CMD ["ruby", "hello.rb"]
