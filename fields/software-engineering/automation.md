# What AI Can and Can't Do — Software Engineering

The defining shift in 2025-2026 is the transition from the "copilot" era (AI suggests inline code completions) to the "agent" era (AI autonomously plans and executes multi-step coding tasks). 55% of engineers regularly use AI agents, with staff+ engineers leading adoption at 63.5%. Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

## Fully Automated
*Tasks where AI does the work, humans review the output.*

- **Code completion and boilerplate generation** — AI generates function implementations, repetitive patterns, and standard scaffolding. Engineers review and accept/reject. This is the most mature AI capability in software engineering.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Documentation generation** — AI produces docstrings, API documentation, README files, and inline comments from code context. Quality is high enough that human review is light-touch.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Test generation** — AI writes unit tests, generates test cases for edge conditions, and creates test scaffolding. Human review focuses on ensuring meaningful coverage rather than writing tests from scratch.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Commit message and PR description generation** — AI produces accurate summaries of code changes. Widely adopted and largely uncontroversial.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Code translation** — AI converts code between languages (e.g., Python to TypeScript) with high accuracy for straightforward translations. Human review needed for idiomatic patterns.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Simple bug fixes** — AI identifies and patches straightforward bugs (off-by-one errors, null checks, typos). Agents can autonomously fix, test, and submit PRs for routine issues.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

## Partially Automated
*Tasks where humans direct the work, AI produces drafts or handles subtasks.*

- **Code review** — AI tools like CodeRabbit flag common issues (style violations, potential bugs, security patterns), but humans judge architectural fit, team conventions, and contextual appropriateness. AI catches the obvious; humans evaluate the subtle.
  Source: [CodeRabbit, Copilot-to-Agent Era, 2026](https://coderabbit.ai/)

- **Debugging** — AI suggests potential fixes and explains error traces, but humans validate root causes and understand system-wide implications. AI handles "what might be wrong"; humans determine "what is actually wrong and why."
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Refactoring** — AI proposes refactoring patterns and executes mechanical transformations, but humans approve architectural decisions. AI can safely rename, extract methods, and restructure within clear boundaries; humans decide when and why to refactor.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Feature implementation** — AI agents can implement well-specified features across multiple files, but humans must define requirements, review output quality, and validate that the implementation matches intent. The "70% of work" that AI handles (per survey data) is largely in this category.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

## AI-Assisted
*Tasks where humans do the core work, AI speeds it up.*

- **System design and architecture** — Engineers design systems; AI helps generate diagrams, evaluate trade-offs in documentation, and draft design documents. The decisions remain entirely human.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

- **Production incident debugging** — AI can analyze logs and suggest hypotheses, but resolving production incidents requires system-wide context, understanding of deployment history, and coordination across teams. AI is a research assistant here, not a lead.
  Source: [Pragmatic Engineer AI Tooling Survey, Mar 2026](https://newsletter.pragmaticengineer.com/)

## Still Fully Human
*Tasks AI cannot do in this field, and why.*

| Task | Why AI Can't Do This |
|------|---------------------|
| **System architecture decisions** | Requires understanding business context, scalability needs, team capabilities, operational constraints, and long-term maintainability trade-offs simultaneously |
| **Understanding business requirements** | Translating vague stakeholder needs into technical specifications requires empathy, negotiation, and domain knowledge that AI lacks |
| **Navigating organizational trade-offs** | Technical decisions are shaped by team politics, budget, timelines, and strategic priorities that exist outside the codebase |
| **Security-critical judgment** | Threat modeling, security architecture, and risk assessment require adversarial thinking and understanding of real-world attack patterns in context |
| **Novel algorithm design** | Creating new algorithms for unprecedented problems requires creative leaps that current AI cannot make |
| **Production incidents requiring system-wide context** | Debugging across distributed systems requires understanding deployment topology, recent changes across teams, and failure mode interactions |
| **Code review for team conventions and history** | Understanding why code is written a certain way — due to past incidents, team agreements, or legacy constraints — requires institutional knowledge |

## How The Role Is Changing

### What's shrinking
- Writing boilerplate code → AI generates this faster and more consistently
- Manual test writing → AI generates tests from implementation code
- Searching documentation → AI answers questions with codebase context
- Writing commit messages and PR descriptions → AI auto-generates these
- Simple bug triage → AI agents autonomously fix routine issues

### What's growing
- Defining specifications clearly → AI executes well-specified tasks better; vague specs produce poor output
- Reviewing and validating AI output → Every AI-generated line needs human judgment
- System design and architecture → More important as AI handles implementation
- AI tool orchestration → Selecting and configuring the right AI tools for each task
- Security and reliability oversight → AI-generated code needs careful security review

### New sub-roles emerging
- **AI Engineering Lead** — Defines team AI tool strategy, evaluates new agents, measures productivity impact
- **AI-Assisted Code Reviewer** — Specializes in reviewing AI-generated code for quality, security, and architectural fit
- **Prompt Engineer (SWE context)** — Crafts specifications and prompts that produce high-quality AI output for complex tasks
