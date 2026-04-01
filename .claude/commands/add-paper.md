# Add a Research Paper

Add a research paper, industry report, or survey to a field's knowledge base.

## Input
$ARGUMENTS — The field name or slug

## Instructions

1. Identify the field directory from the argument. Check `fields/` for matching slug.
2. If the field doesn't exist, tell the user and suggest running `/add-field` first.
3. Ask the user for (if not already provided):
   - **Title** — Full title of the paper/report
   - **Authors/Organization** — Who published it
   - **URL** — Link to the paper
   - **Type** — One of: academic, industry-report, survey, whitepaper
   - **Key findings** — 3-5 bullet points of the most relevant findings
   - **What sections does this affect?** — One or more of: tools, automation, skills, career

4. If a URL is provided, try to fetch and read the paper to extract key findings and a summary. Use WebFetch if available.

5. Create a new file at: `fields/{slug}/papers/YYYY-MM-{org-or-author-slug}.md`

6. Write the file with:
   - YAML frontmatter (date, title, authors, url, type, key_findings as list, affects)
   - A 2-3 paragraph summary of the paper's relevance to this field
   - Key data points that should inform the field's curated files
   - Direct quotes from the paper if available

7. Update the field's `README.md`:
   - In the "Research & Papers" section, replace the "No papers added yet" placeholder (if present) or add to the existing list
   - Show the paper as a bullet: `- **Title** — Organization/Author, YYYY-MM ([link](url))` with a one-line finding
   - Keep only the 5 most recent papers in the README; older ones are in the `papers/` directory
   - Update the `Last updated` date in the README footer

8. After creating, tell the user:
   - The paper has been logged in both `papers/` and `README.md`
   - Which curated files should be updated with the paper's findings
   - Any data points from the paper that could update career.md salary/job market info
