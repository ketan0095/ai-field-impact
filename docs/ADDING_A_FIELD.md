# Adding a New Field

This guide walks you through adding a new professional field to the knowledge base. You can do this entirely in GitHub's web browser — no terminal needed.

## Before You Start

1. Check if the field already exists in `fields/`
2. Check [open issues](../../issues?q=is%3Aissue+label%3Anew-field) to see if someone is already working on it
3. If not, [open a "New Field" issue](../../issues/new?template=new-field.yml) to claim it

## Step 1: Copy the Template

### Option A: Using GitHub Web UI

1. Go to [`fields/_template/`](../../tree/main/fields/_template/)
2. You'll need to create each file individually in your new directory
3. For each file in `_template/`, create the corresponding file in `fields/{your-field-slug}/`

### Option B: Using Terminal

```bash
cp -r fields/_template fields/your-field-slug
mkdir -p fields/your-field-slug/updates fields/your-field-slug/papers
```

### Option C: Using Claude Code

If you have Claude Code set up with this repo:
```
/add-field "Your Field Name"
```

## Step 2: Choose Your Slug

Use lowercase kebab-case:
- "Graphic Design" → `graphic-design`
- "K-12 Teaching" → `k12-teaching`
- "Investment Banking" → `investment-banking`

## Step 3: Fill In the Files

Start with these two (minimum viable field):

### `overview.md` (required)
- Fill in the YAML frontmatter (title, slug, category, tags)
- Set `status: "draft"`
- Write the AI Adoption Snapshot table
- Write 2-3 overview paragraphs

### `tools.yml` (required)
- List at least 3-5 AI tools relevant to this field
- Include URL, description, adoption level, and pricing
- Set `added` and `last_verified` dates

### Then fill in as much as you can:
- `automation.md` — What can AI do in this field? What can't it?
- `skills.md` — What skills are gaining/losing value?
- `career.md` — How are jobs and salaries changing?
- `voices.md` — Any quotes from practitioners?

**You don't need to complete everything.** A draft with overview + tools is a valid first PR. Others can help fill in the rest.

## Step 4: Submit Your PR

1. Create a branch: `add-field/{your-field-slug}`
2. Commit your files
3. Open a PR with:
   - Title: `Add field: {Field Name}`
   - Description: Your relationship to this field and any notes

## Step 5: Review

- Automated checks will validate your frontmatter and formatting
- A maintainer will review the content
- You may get feedback — this is collaborative, not adversarial
- Once approved, your field goes live and you're credited as the author

## Tips

- **Be honest about gaps.** "I don't know" is better than making something up.
- **Cite sources.** Even informal ones like "based on my 5 years in the field."
- **Start small.** A well-written overview with 5 tools is better than a rushed complete field.
- **Ask for help.** Open a Discussion if you're unsure about anything.
