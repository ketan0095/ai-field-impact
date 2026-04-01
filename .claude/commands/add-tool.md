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

5. Add the new entry to `tools.yml` in alphabetical order within its category
6. Set `added` to today's date
7. Set `last_verified` to today's date

8. After adding, tell the user:
   - The tool has been added
   - Suggest creating an update file in `updates/` if this is a notable launch
