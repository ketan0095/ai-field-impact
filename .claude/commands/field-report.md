# Field Report

Generate a comprehensive status report for a field.

## Input
$ARGUMENTS — The field name or slug

## Instructions

1. Identify the field directory from the argument. Check `fields/` for matching slug.
2. If the field doesn't exist, list all available fields and ask the user to pick one.

3. Read ALL files in the field directory:
   - `overview.md` — frontmatter and content
   - `tools.yml` — count tools by category and adoption level
   - `automation.md` — count fully/partially/assisted automated tasks
   - `skills.md` — count gaining/losing/stable skills
   - `career.md` — salary trends and role changes
   - `voices.md` — count practitioner quotes
   - `updates/` — list recent updates (last 5)
   - `papers/` — list papers (last 5)
   - `README.md` — check if it exists and whether it reflects current content

4. Generate a summary report in this format:

```
## Field Report: {Field Name}
Status: {status} | Confidence: {confidence} | Last verified: {date}

### Coverage
- Tools tracked: X (Y widespread, Z growing, W emerging, V experimental)
- Tasks documented: X fully automated, Y partial, Z assisted, W human-only
- Skills mapped: X gaining, Y losing, Z stable
- Practitioner voices: X quotes
- Updates logged: X (latest: YYYY-MM-DD)
- Papers cited: X (latest: YYYY-MM-DD)

### Freshness
- Overview: {last_updated} {OK/STALE}
- Tools: {most recent last_verified} {OK/STALE}
- Career data: {last_updated} {OK/STALE}

### Gaps
- List any sections that are empty or have placeholder content
- Flag any tools with last_verified > 6 months ago

### Recent Activity
- Last 3 updates
- Last 2 papers added
```

5. Check if the field's `README.md` is in sync with the actual content:
   - Does the tools table match `tools.yml`?
   - Does the snapshot table match `overview.md`?
   - Are recent updates and papers reflected?
   - If out of sync, flag it and offer to regenerate the README

6. After reporting, suggest specific actions to improve the field's coverage.
