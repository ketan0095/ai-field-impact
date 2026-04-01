# Add a Field Update

Log a timestamped update about a development in a field — new tool launch, industry shift, acquisition, regulation, etc.

## Input
$ARGUMENTS — The field name or slug

## Instructions

1. Identify the field directory from the argument. Check `fields/` for matching slug.
2. If the field doesn't exist, tell the user and suggest running `/add-field` first.
3. Ask the user for (if not already provided):
   - **What happened?** — Brief description of the event
   - **Source URL** — Link to announcement, article, or report
   - **Type** — One of: tool-launch, tool-update, industry-shift, company-news, regulation, acquisition
   - **Impact level** — low, medium, high, or critical
   - **What does this affect?** — One or more of: tools, automation, skills, career

4. Create a new file at: `fields/{slug}/updates/YYYY-MM-DD-{event-slug}.md`
   - Use today's date
   - Create a short slug from the event description

5. If you need to verify details or fetch the source, use the `/playwright-browser` skill to browse URLs and extract content. Prefer Playwright over WebSearch/WebFetch.

6. Write the file with proper YAML frontmatter and a 2-3 paragraph summary including:
   - What happened
   - What changed as a result
   - What this means for practitioners in this field

6. Update the field's `README.md`:
   - In the "Latest Updates" section, replace the "No updates yet" placeholder (if present) or add to the existing list
   - Show the update as a bullet: `- **YYYY-MM-DD** — Brief description ([source](url))` with impact badge
   - Keep only the 5 most recent updates in the README; older ones are in the `updates/` directory
   - Update the `Last updated` date in the README footer

7. After creating, tell the user:
   - The update has been logged in both `updates/` and `README.md`
   - Which curated files (overview.md, automation.md, skills.md, career.md) might need updating based on the `affects` tags
   - Whether tools.yml needs a new entry if this was a tool-launch
