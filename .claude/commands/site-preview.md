# Site Preview

Build and preview the Jekyll site locally.

## Instructions

1. Check if Jekyll is installed: `jekyll --version`
   - If not installed, tell the user to run: `gem install jekyll bundler`

2. Check if Bundler dependencies are installed:
   - If `Gemfile` exists, run `bundle install`
   - If not, the site uses basic Jekyll without a Gemfile

3. Run the Jekyll server:
   ```
   cd site/ && jekyll serve --livereload
   ```

4. Tell the user:
   - The site is running at `http://localhost:4000`
   - Changes will auto-reload
   - Press Ctrl+C to stop

5. If there are build errors, diagnose and help fix them.
