# Contributing to AI Field Impact

Thank you for contributing! This project is built by practitioners — people who actually work in the fields we document. Whether you're a designer, nurse, lawyer, or engineer, your perspective is valuable.

**You don't need to be a programmer to contribute.**

## Ways to Contribute

### No GitHub experience needed

| What | How | Time |
|------|-----|------|
| Report outdated info | [Open an issue](../../issues/new?template=outdated-info.yml) | 1 min |
| Suggest a new AI tool | [Submit via form](../../issues/new?template=tool-submission.yml) | 2 min |
| Suggest a new field | [Request via form](../../issues/new?template=new-field.yml) | 2 min |
| Share how AI changed your work | [Open a general issue](../../issues/new?template=general.yml) | 2 min |

### With basic GitHub skills (edit files in browser)

| What | How | Time |
|------|-----|------|
| [Add a tool](#add-a-tool) | Edit `tools.yml` | 2 min |
| [Add a voice](#add-a-voice) | Edit `voices.md` | 1 min |
| [Add an update](#add-an-update) | Create a file in `updates/` | 3 min |
| [Add a paper](#add-a-paper) | Create a file in `papers/` | 3 min |
| [Fix content](#fix-content) | Edit any `.md` file | 2 min |

### For experienced contributors

| What | How | Time |
|------|-----|------|
| [Write a new field](#write-a-new-field) | Copy `_template/`, fill it in | 1-2 hrs |
| Review a field for accuracy | Read and suggest corrections | 30 min |
| Improve the website | Work on `site/` | Varies |
| Improve automation | Work on `scripts/` or `.github/workflows/` | Varies |

---

## How To: Step by Step

### Add a Tool

1. Navigate to `fields/{field-name}/tools.yml`
2. Click the pencil icon (edit) on GitHub
3. Add a new entry at the end, following this format:

```yaml
- name: "Tool Name"
  url: "https://tool-url.com"
  category: "relevant-category"
  what_it_does: "One line — what does this tool do?"
  replaces: "What manual work does it replace?"
  adoption: "emerging"        # experimental | emerging | growing | widespread
  pricing: "freemium"         # free | freemium | paid | enterprise
  added: "2026-04-01"         # today's date
  last_verified: "2026-04-01" # today's date
```

4. Click "Propose changes" → "Create pull request"

### Add a Voice

1. Navigate to `fields/{field-name}/voices.md`
2. Click edit
3. Add your quote:

```markdown
> "Your quote about how AI is changing your work."
> — Your Role, Your Context (e.g., "Series B startup"), 2026-04
```

4. Submit as a PR

### Add an Update

When something notable happens in a field (new tool launch, industry shift, regulation):

1. Navigate to `fields/{field-name}/updates/`
2. Create a new file named `YYYY-MM-DD-short-description.md`
3. Use this template:

```markdown
---
date: 2026-04-01
type: tool-launch
source: https://link-to-announcement.com
impact: medium
affects:
  - tools
  - automation
---

## What Happened

2-3 sentences describing the event.

## What This Means

2-3 sentences on impact for practitioners.
```

### Add a Paper

When you find a relevant research paper or industry report:

1. Navigate to `fields/{field-name}/papers/`
2. Create a new file named `YYYY-MM-org-or-author-topic.md`
3. Use this template:

```markdown
---
date: 2026-04-01
title: "Full Paper Title"
authors: ["Organization or Author Names"]
url: https://link-to-paper.com
type: industry-report
key_findings:
  - "Finding 1"
  - "Finding 2"
  - "Finding 3"
affects:
  - automation
  - career
---

## Summary

2-3 paragraphs summarizing the paper's key findings relevant to this field.

## Key Data Points

- Specific numbers, percentages, or statistics worth noting
```

### Fix Content

If you spot incorrect or outdated information:

1. Navigate to the file
2. Click edit
3. Make the correction
4. In your PR description, explain what was wrong and cite a source for the correction

### Write a New Field

This is the biggest contribution you can make. See [ADDING_A_FIELD.md](ADDING_A_FIELD.md) for a detailed walkthrough.

Short version:
1. Copy the entire `fields/_template/` directory
2. Rename it to your field's kebab-case slug (e.g., `graphic-design`)
3. Fill in each file, starting with `overview.md` and `tools.yml`
4. You don't have to fill everything — a draft with overview + tools is a valid first PR

---

## Content Guidelines

### Tone
- **Neutral and factual.** Not alarmist, not dismissive.
- Bad: "AI will replace all designers within 2 years"
- Bad: "AI can never do what a real designer does"
- Good: "AI handles layout generation; strategic design decisions still require human judgment"

### Sources
- Every factual claim needs a source. Link to it inline or in the Sources section.
- Acceptable: official docs, industry reports, published surveys, credible news
- Not acceptable: tweets, Reddit posts, personal blogs without data

### Tools
- Only list tools that are publicly available (not internal/proprietary)
- Verify the tool still exists and is maintained before adding
- Be honest about adoption level — "experimental" is fine, don't inflate

### "Still Human" Section
- This is the most important section. Be specific about WHY.
- Bad: "Creativity is human"
- Good: "Designing novel interaction paradigms requires understanding user behavior patterns that current AI cannot observe or reason about"

---

## Review Process

1. You submit a PR
2. Automated checks run (markdown lint, spell check, schema validation)
3. A domain expert reviews the content (if available for that field)
4. A maintainer does final review and merges
5. You get credited in the field's contributor list and the project README

**Expected timeline:** Most PRs are reviewed within 1 week. Simple additions (tool, voice, update) are usually merged within 1-2 days.

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold it.

## Questions?

Open a [Discussion](../../discussions) — we're happy to help.
