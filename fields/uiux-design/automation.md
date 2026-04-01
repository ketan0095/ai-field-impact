# What AI Can and Can't Do — UIUX Design

## Fully Automated

*Tasks where AI does the work, humans review the output.*

- **Responsive layout generation** — Given a desktop design, AI produces tablet and mobile variants. Human reviews for edge cases and interaction differences across breakpoints.
- **Design-to-code conversion** — Pixel-accurate frontend code generated from Figma frames. Replaces the "handoff" step almost entirely for standard layouts.
- **Placeholder content filling** — Realistic fake names, addresses, product descriptions that fit the design context. No more "Lorem ipsum" in mockups.
- **Basic asset generation** — Icons, illustrations, and stock imagery generated from text prompts for mockup purposes.

## Partially Automated

*Tasks where humans direct the work, AI produces drafts or handles subtasks.*

- **Wireframing from prompts** — Describe a screen in text, get a wireframe. Fast for exploration during ideation, but human must evaluate and iterate on the output for quality and feasibility.
- **Component variations** — "Give me 5 versions of this card layout." AI generates options, human evaluates against design system constraints and user needs.
- **Usability heuristic checks** — AI flags obvious accessibility issues (contrast ratios, touch target sizes, missing alt text). Catches roughly 60% of what a thorough manual audit would find.
- **UX copy drafting** — AI generates microcopy (button labels, error messages, onboarding text). Human reviews for tone, clarity, and edge cases.

## AI-Assisted

*Tasks where humans do the core work, AI speeds it up.*

- **Research synthesis** — AI clusters interview transcripts and identifies themes. Human validates themes, adds nuance, and catches context that AI missed.
- **Design system documentation** — AI drafts component documentation from existing design files. Human reviews for accuracy and adds usage guidelines.
- **Competitive analysis** — AI summarizes competitor interfaces and patterns. Human evaluates strategic implications and differentiation opportunities.

## Still Fully Human

*Tasks AI cannot do in this field, and why.*

| Task | Why AI Can't Do This |
|------|---------------------|
| **User interviews and contextual inquiry** | Requires empathy, follow-up instincts, reading body language, and building rapport. AI simulations are useful for hypothesis generation but are not real research. |
| **Problem framing** | Deciding WHAT to design requires understanding business context, user needs, technical constraints, and organizational politics simultaneously. AI can explore a defined space but cannot define the space. |
| **Design system governance** | Deciding when to add, deprecate, or modify components requires understanding team workflows, adoption patterns, and technical debt. This is judgment, not generation. |
| **Stakeholder alignment** | Presenting designs, handling feedback, navigating competing priorities, and building consensus is a human coordination problem. |
| **Ethical design decisions** | Dark patterns, addiction mechanics, inclusivity tradeoffs — these require moral reasoning and cultural understanding that AI does not possess. |
| **Novel interaction paradigms** | AI remixes existing patterns. Inventing new interaction models (the way pinch-to-zoom or pull-to-refresh were invented) requires creative leaps AI does not make. |
| **Edge case judgment** | "What happens when the user has 0 items? 10,000 items? Is offline? Uses a screen reader?" — comprehensive state thinking across scenarios. |

## How The Role Is Changing

### What's shrinking

- "Make this mockup pixel-perfect" — AI does this
- "Build 10 responsive variants" — AI does this
- "Create a wireframe for this flow" — AI does the first draft
- "Write placeholder microcopy" — AI does this

### What's growing

- "Should we build this feature at all?" — More important than ever
- "What are users actually struggling with?" — Human research is irreplaceable
- "How do all these AI-generated screens stay consistent?" — Design systems thinking is critical
- "Is this AI output actually good UX or just pretty?" — Evaluation skills over production skills

### New sub-roles emerging

- **AI Design Director** — Guides AI tools to produce on-brand output, curates and quality-checks AI-generated designs at scale
- **Design Systems Engineer** — Governs how AI-generated components fit into the system. Increasingly technical role bridging design and engineering.
- **UX Research Strategist** — As AI handles tactical analysis, the human focuses on research strategy, study design, and insight framing
- **Conversational UX Designer** — Designing for AI-first interfaces (chatbots, voice agents, copilots) is a growing specialization
