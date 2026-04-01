# Style Guide

## Tone

**Neutral, factual, non-alarmist.** We document what AI can and cannot do. We don't predict the future or make dramatic claims.

| Instead of | Write |
|-----------|-------|
| "AI will replace designers" | "AI automates layout generation; strategic design remains human-driven" |
| "AI can never do X" | "Currently, AI cannot do X because it requires Y" |
| "This tool is amazing" | "This tool automates X, reducing time from Y hours to Z minutes" |
| "Everyone is using X" | "X has widespread adoption, with 70% of surveyed teams reporting usage (Source)" |

## Sources

Every factual claim needs a source. Link inline or in the Sources section.

**Acceptable sources:**
- Official tool documentation
- Published industry reports and surveys
- Peer-reviewed papers
- Credible tech journalism (e.g., TechCrunch, The Verge, Wired)
- Official company announcements

**Not acceptable as sole source:**
- Individual tweets or social media posts
- Reddit comments
- Personal blogs without data
- YouTube videos without citations

## Formatting

- Use ATX-style headers (`#`, `##`, `###`)
- Tables: use markdown tables, align for readability
- Lists: use `-` for unordered, `1.` for ordered
- Bold for emphasis: `**important**`
- Links: `[text](url)` — use descriptive text, not "click here"
- Dates: ISO format `YYYY-MM-DD` everywhere

## tools.yml

- Sort entries alphabetically within each category
- Use the exact enum values for `adoption` and `pricing`
- Always include `added` and `last_verified` dates
- `what_it_does` should be one clear sentence
- `replaces` should describe the manual work, not just "manual work"

## Practitioner Quotes (voices.md)

- Use blockquote format: `> "Quote" > — Role, Context, Date`
- Keep quotes concise (2-4 sentences)
- Include enough context to understand the perspective
- Anonymous quotes are fine: `— Senior Designer, enterprise SaaS`
- Never attribute quotes without permission

## Updates

- File names: `YYYY-MM-DD-short-slug.md`
- Keep summaries to 2-3 paragraphs
- Always include "What This Means" for practitioners
- Link to the source in frontmatter AND in the body

## Language

- Use American English spelling
- Avoid jargon where possible; if necessary, explain on first use
- Write for a practitioner in the field, not for AI researchers
- "AI" not "A.I." — no periods
- "UIUX" not "UI/UX" in slugs and directory names; "UI/UX" is fine in prose
