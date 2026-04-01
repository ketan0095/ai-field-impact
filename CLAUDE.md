# AI Field Impact

A community-maintained knowledge base tracking how AI is transforming every professional field.

## How It Works

This repo uses a **directory-per-field** structure. Each professional field (e.g., UIUX Design, Cybersecurity) is a directory containing structured files that capture tools, automation status, skills impact, career trends, and incoming updates.

## Skills (Slash Commands)

| Command | What it does |
|---------|-------------|
| `/add-field "field name"` | Scaffold a new field directory from template |
| `/add-tool` | Add a new AI tool to a field's tools.yml |
| `/add-update` | Log a timestamped update (new tool launch, industry shift, etc.) |
| `/add-paper` | Add a research paper or report to a field |
| `/field-report "field"` | Generate a summary report of a field's current state |
| `/freshness-check` | Scan all fields for stale data (not verified in 6+ months) |
| `/site-preview` | Build and preview the Jekyll site locally |

## Project Structure

```
ai-field-impact/
├── CLAUDE.md                    <- You are here
├── .claude/commands/            <- Skills for maintaining the repo
├── fields/                      <- One directory per professional field
│   ├── _template/               <- Copy this for new fields
│   │   ├── overview.md          <- Curated summary (stable, quarterly updates)
│   │   ├── tools.yml            <- AI tools list (structured, easy to add)
│   │   ├── automation.md        <- What AI can/can't do
│   │   ├── skills.md            <- Skills gaining/losing value
│   │   ├── career.md            <- Jobs, salaries, new roles
│   │   ├── voices.md            <- Practitioner quotes
│   │   ├── updates/             <- Timestamped news feed
│   │   └── papers/              <- Research papers & reports
│   ├── uiux-design/
│   ├── software-engineering/
│   ├── cybersecurity/
│   └── ...
├── docs/                        <- Contributor docs
├── site/                        <- Jekyll website (GitHub Pages)
├── scripts/                     <- Validation & generation scripts
└── .github/                     <- CI, issue templates, workflows
```

## Content Rules

### File Responsibilities

| File | Changes | Who |
|------|---------|-----|
| `overview.md` | Quarterly | Maintainers — curated, stable summary |
| `tools.yml` | Anytime | Anyone — add a row, submit a PR |
| `automation.md` | Monthly | Practitioners who use the tools |
| `skills.md` | Quarterly | Senior practitioners, career coaches |
| `career.md` | Quarterly | Recruiters, salary survey data |
| `voices.md` | Anytime | Anyone — submit a quote |
| `updates/*.md` | Anytime | Anyone — timestamped news entries |
| `papers/*.md` | Anytime | Anyone — research papers with summaries |

### Information Flow

```
New tool / paper / event drops
    ↓
Contributor adds to: tools.yml | updates/ | papers/
    ↓
Monthly maintainer review
    ↓
Curated files updated: overview.md | automation.md | skills.md | career.md
```

### Conventions

- Field directories: lowercase kebab-case (e.g., `uiux-design/`)
- Dates: ISO format YYYY-MM-DD throughout
- Update files: `YYYY-MM-DD-slug.md` format
- Paper files: `YYYY-MM-author-or-org-slug.md` format
- Every factual claim needs a source citation
- Tone: neutral, factual, non-alarmist. No "AI will replace all jobs" fearmongering
- No speculation — only document what AI can demonstrably do today
- tools.yml entries must have `last_verified` dates

### YAML Frontmatter

Every overview.md must have:
```yaml
---
title: "Field Name"
slug: "field-name"
category: "category-name"
status: "draft | review | published"
last_verified: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
confidence: "high | medium | low"
contributors:
  - github: "username"
    role: "author | reviewer | domain-expert"
tags: ["tag1", "tag2"]
---
```

Every tools.yml entry must have:
```yaml
- name: Tool Name
  url: https://...
  category: category-slug
  what_it_does: One line description
  replaces: What manual work it replaces
  adoption: experimental | emerging | growing | widespread
  pricing: free | freemium | paid | enterprise
  added: YYYY-MM-DD
  last_verified: YYYY-MM-DD
```

Every update file must have:
```yaml
---
date: YYYY-MM-DD
type: tool-launch | tool-update | industry-shift | company-news | regulation | acquisition
source: https://...
impact: low | medium | high | critical
affects:
  - tools | automation | skills | career
---
```
