# Add a New Field

Scaffold a new professional field directory from the template.

## Input
$ARGUMENTS — The field name (e.g., "Graphic Design", "Cybersecurity", "Contract Law")

## Instructions

1. Convert the field name to a kebab-case slug (e.g., "Graphic Design" → "graphic-design")
2. Determine the appropriate category based on the field:
   - `engineering` — Software Engineering, Data Science, DevOps, Civil Engineering, etc.
   - `creative` — UIUX Design, Graphic Design, Copywriting, Music Production, Video/Film, etc.
   - `security` — Cybersecurity, Information Security, etc.
   - `business` — Product Management, Marketing, Sales, Consulting, etc.
   - `healthcare` — Radiology, Nursing, Mental Health, Pharmacy, etc.
   - `legal` — Contract Law, Litigation, Compliance, etc.
   - `education` — K-12 Teaching, Higher Education, Corporate Training, etc.
   - `finance` — Accounting, Investment Banking, Financial Planning, etc.
   - `science` — Research, Lab Work, etc.
   - If unclear, ask the user.

3. Create the field directory: `fields/{slug}/`
4. Copy ALL template files from `fields/_template/` into the new directory, **including `README.md`**
5. In each file, replace `FIELD_NAME` with the actual field name and `field-slug` with the slug
6. Set the `category` in overview.md frontmatter
7. Set `last_updated` and `last_verified` to today's date
8. Set the contributor to `ketanshetye` with role `author`
9. Create `updates/` and `papers/` subdirectories with `.gitkeep` files
10. Customize the `README.md`:
    - Replace `FIELD_NAME` with the actual field name
    - Update status badges with today's date for `last_verified`
    - Replace the generic tool categories line with the field's actual tool categories from `tools.yml`
    - Set the `Last updated` footer to today's date
11. Customize `tools.yml` categories — choose domain-appropriate categories for the field (not the generic template ones). Add YAML comments listing them at the top.

After scaffolding, tell the user:
- The directory has been created at `fields/{slug}/`
- Which files to fill in first (overview.md and tools.yml are highest priority)
- The README.md is ready to share — it will auto-reflect content as files are filled in
- Remind them to update the root README.md field table when ready to publish
