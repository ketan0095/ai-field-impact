# What AI Can and Can't Do — UIUX Design

## Fully Automated

*Tasks where AI does the work, humans review the output.*

- **Responsive layout generation** — Given a desktop design, AI produces tablet and mobile variants. Human reviews for edge cases and interaction differences across breakpoints.
  Source: Figma AI Auto Layout features, [Figma Config 2024](https://config.figma.com/)

- **Design-to-code conversion** — Pixel-accurate frontend code generated from Figma frames. Works well for standard component-based layouts (card grids, forms, list views). Complex animations and custom interactions still require manual coding.
  Source: [Builder.io Visual Copilot](https://builder.io); [Locofy Lightning 2.0](https://locofy.ai)

- **Placeholder content filling** — Realistic fake names, addresses, product descriptions that fit the design context. No more "Lorem ipsum" in mockups.
  Source: [Figma AI Content Fill](https://figma.com)

- **Basic asset generation** — Icons, illustrations, and stock imagery generated from text prompts for mockup purposes. Not production-ready brand assets, but sufficient for concept exploration.
  Source: [Midjourney](https://midjourney.com); [Adobe Firefly](https://firefly.adobe.com)

- **AI-predicted attention heatmaps** — Predicts where users will look on a design without running an actual eye-tracking study. Both Google Stitch and UX Pilot include this natively.
  Source: [Attention Insight](https://attentioninsight.com); [Google Stitch](https://stitch.withgoogle.com)

**Honest caveat:** "Fully automated" is relative. Design-to-code works well for the standard 70-80% of layouts but breaks down on complex animation sequences, canvas-based interactions, or highly custom components.

## Partially Automated

*Tasks where humans direct the work, AI produces drafts or handles subtasks.*

- **Wireframing from prompts** — Describe a screen in text, get a wireframe. Fast for exploration during ideation, but human must evaluate and iterate for quality, feasibility, and edge cases (empty states, error states, loading states). AI-generated wireframes almost never account for all states.
  Source: [Galileo AI](https://usegalileo.ai); [Uizard](https://uizard.io); [Relume](https://relume.io)

- **Full UI generation** — Tools like Google Stitch and Moonchild AI generate high-fidelity UI screens from prompts. Human evaluates against design system constraints, accessibility, and user needs.
  Source: [Google Stitch](https://stitch.withgoogle.com); [Moonchild AI](https://moonchild.ai)

- **Component variation generation** — "Give me 5 versions of this card layout." AI generates options, human evaluates against design system constraints and user needs. AI produces "plausible" not "correct" variations.
  Source: [Figma AI](https://figma.com)

- **Usability heuristic checks** — AI flags obvious accessibility issues (contrast ratios, touch target sizes, missing alt text). WebAIM's 2024 Million report found automated tools catch roughly 30-57% of WCAG issues depending on the tool. The remaining issues require understanding user intent.
  Source: [WebAIM Million report 2024](https://webaim.org/projects/million/); [Stark](https://getstark.co); [axe DevTools](https://deque.com/axe/)

- **UX copy drafting** — AI generates microcopy (button labels, error messages, onboarding text). Human reviews for tone, edge cases, and ensures copy supports the actual UX flow rather than just sounding generic.
  Source: [Writer](https://writer.com)

- **Research synthesis** — AI clusters interview transcripts, auto-tags themes, generates session summaries. Human validates themes, adds nuance, and catches context that AI missed. AI often creates overlapping or misleading categories.
  Source: [Notably](https://notably.ai); [Maze AI](https://maze.co); [Dovetail](https://dovetail.com)

## AI-Assisted

*Tasks where humans do the core work, AI speeds it up.*

- **Competitive analysis** — AI summarizes competitor interfaces, extracts UI patterns, identifies feature gaps. ~2-3x faster for data-gathering. Strategic interpretation remains entirely human.

- **Design system documentation** — AI drafts component documentation from existing design files. ~2x faster for first drafts. Human must verify accuracy and add contextual usage guidance.
  Source: [Zeroheight](https://zeroheight.com); [Supernova](https://supernova.io)

- **User persona development** — AI synthesizes research data into draft personas. Faster initial drafts, but AI-generated personas tend to be stereotypical. Useful as starting structure, not finished artifact.

- **Rapid prototyping** — AI generates interactive prototypes from descriptions ~3-5x faster than manual construction. High-fidelity prototyping with realistic data and complex interactions still requires manual work.
  Source: [Google Stitch](https://stitch.withgoogle.com); [Figma AI](https://figma.com)

## Still Fully Human

*Tasks AI cannot do in this field, and why.*

| Task | Why AI Can't Do This |
|------|---------------------|
| **User interviews and contextual inquiry** | Requires empathy, follow-up instincts, reading body language, and building rapport. AI simulations are useful for hypothesis generation but not real research. NNGroup: "You need deep understanding of your users to build products they'll actually use." |
| **Problem framing** | Deciding WHAT to design requires understanding business context, user needs, technical constraints, and organizational politics simultaneously. AI can explore a defined space but cannot define the space. |
| **Design system governance** | Deciding when to add, deprecate, or modify components requires understanding team workflows, adoption patterns, and technical debt. This is judgment, not generation. |
| **Stakeholder alignment** | Presenting designs, handling feedback, navigating competing priorities, and building consensus is a human coordination problem. |
| **Ethical design decisions** | Dark patterns, addiction mechanics, inclusivity tradeoffs — these require moral reasoning and cultural understanding. As AI generates more output faster, ethical guardrails become more important, not less. |
| **Novel interaction paradigms** | AI remixes existing patterns. Inventing new interaction models (the way pinch-to-zoom or pull-to-refresh were invented) requires creative leaps AI does not make. |
| **Edge case judgment** | "What happens when the user has 0 items? 10,000 items? Is offline? Uses a screen reader?" — AI generates the happy path by default. |
| **Cross-journey coherence** | Ensuring experience makes sense across touchpoints (app, email, support call) requires understanding the full service ecosystem. NNGroup: "The experience isn't just the screen, and it never has been." |

Source: [NNGroup State of UX 2026](https://www.nngroup.com/articles/state-of-ux-2026/)

## How The Role Is Changing

### What's shrinking

- "Make this mockup pixel-perfect" — AI does this
- "Build 10 responsive variants" — AI does this
- "Create a wireframe for this flow" — AI does the first draft
- "Write placeholder microcopy" — AI does this
- Portfolio polish as differentiator — NNGroup: "Curated taste, research-informed contextual understanding, critical thinking, and careful judgment" are what matters now

### What's growing

- "Should we build this feature at all?" — Strategic problem solving more important than ever
- "What are users actually struggling with?" — Human research is irreplaceable; NNGroup notes research will inform how AI models are trained
- "How do all these AI-generated screens stay consistent?" — Design systems governance is critical
- "Is this AI output actually good UX or just pretty?" — Evaluation skills over production skills
- Designing AI experiences — Trust, transparency, control for AI-powered products

### New sub-roles emerging

- **AI Design Director** — Guides AI tools to produce on-brand output, curates and quality-checks AI-generated designs at scale
- **Design Systems Engineer** — Governs how AI-generated components fit into the system. Increasingly technical role bridging design and engineering.
- **UX Research Strategist** — As AI handles tactical analysis, the human focuses on research strategy, study design, and insight framing
- **Conversational UX Designer** — Designing for AI-first interfaces (chatbots, voice agents, copilots). Active job postings at Five9, Photon, and others.
- **Design QA Specialist** — Reviews AI-generated designs for usability, accessibility, and brand compliance before shipping
