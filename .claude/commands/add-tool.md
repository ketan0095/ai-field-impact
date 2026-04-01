# Add an AI Tool

Add a new AI tool to a field's tools.yml file.

## Input
$ARGUMENTS — The field name or slug (e.g., "uiux-design" or "UIUX Design")

## Instructions

1. Identify the field directory from the argument. Check `fields/` for matching slug.
2. If the field doesn't exist, tell the user and suggest running `/add-field` first.
3. Read the existing `tools.yml` for that field to understand current categories and entries.
4. Ask the user for the following information (if not already provided):
   - **Tool name** — What's the tool called?
   - **URL** — Link to the tool
   - **Category** — Use existing categories from the file, or propose a new one
   - **What it does** — One-line description
   - **What it replaces** — What manual work does this reduce?
   - **Adoption level** — experimental, emerging, growing, or widespread
   - **Pricing** — free, freemium, paid, or enterprise

5. If you need to verify the tool exists or check its current status, use the `/playwright-browser` skill to browse the tool's URL. Prefer Playwright over WebSearch/WebFetch for web research.
6. Add the new entry to `tools.yml` in alphabetical order within its category
6. Set `added` to today's date
7. Set `last_verified` to today's date

8. Update the field's `README.md` tools table:
   - Add the new tool to the appropriate category table in the "AI Tools Landscape" section
   - Use the same format as existing entries: linked tool name, what it does, adoption indicator (🟢 Widespread, 🟡 Growing, 🟠 Emerging, ⚪ Experimental), pricing
   - If the README still has the "No tools added yet" placeholder, replace it with a real table
   - Update the `Last updated` date in the README footer

9. After adding, tell the user:
   - The tool has been added to both `tools.yml` and `README.md`
   - Suggest creating an update file in `updates/` if this is a notable launch
