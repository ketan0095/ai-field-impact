# Freshness Check

Scan all fields for stale data and generate a maintenance report.

## Instructions

1. List all field directories in `fields/` (exclude `_template/`)

2. For each field, read `overview.md` frontmatter and check:
   - `last_verified` date — flag if older than 6 months from today
   - `last_updated` date — flag if older than 3 months from today
   - `status` — note if still "draft"
   - `confidence` — note if "low"

3. For each field, read `tools.yml` and check:
   - Each tool's `last_verified` date — flag if older than 6 months
   - Count tools that need re-verification

4. Generate a report in this format:

```
## Freshness Report — YYYY-MM-DD

### Summary
- Total fields: X
- Published: X | Draft: X | Review: X
- Fields needing attention: X

### Field Status
| Field | Status | Last Verified | Last Updated | Stale Tools | Action Needed |
|-------|--------|--------------|--------------|-------------|---------------|
| UIUX Design | Published | 2026-03-15 | 2026-04-01 | 0 | None |
| ... | ... | ... | ... | ... | ... |

### Stale Tools (not verified in 6+ months)
| Field | Tool | Last Verified | Days Stale |
|-------|------|--------------|------------|
| ... | ... | ... | ... |

### Fields Missing Content
| Field | Missing Sections |
|-------|-----------------|
| ... | tools.yml empty, no voices, no papers |

### Recommended Actions
1. Priority action items based on staleness and gaps
```

5. After reporting, ask if the user wants to:
   - Start updating a specific stale field
   - Create GitHub issues for stale items (if the repo is connected)
