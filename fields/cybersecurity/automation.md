# What AI Can and Can't Do — Cybersecurity

## Fully Automated
*Tasks where AI does the work, humans review the output.*

- **Log analysis and event correlation** — AI-powered SIEM platforms (Splunk, IBM QRadar, Cortex XSIAM) ingest millions of events per day, correlate across sources, and surface prioritized alerts. Human involvement limited to reviewing escalated findings.
  Source: [Palo Alto Networks Cortex XSIAM](https://www.paloaltonetworks.com/cortex/cortex-xsiam), [Splunk](https://www.splunk.com)

- **Alert triage and classification** — AI SOC agents (Dropzone AI, SentinelOne) autonomously classify and prioritize security alerts, reducing Tier 1 analyst workload by filtering false positives. Gartner predicts 50% of Tier 1 SOC positions eliminated or transformed.
  Source: [Dropzone AI](https://www.dropzone.ai/), [Gartner](https://www.gartner.com/)

- **Malware classification** — Machine learning models classify known and polymorphic malware families based on behavioral signatures and code patterns. CrowdStrike Falcon and SentinelOne perform this at endpoint level without human intervention.
  Source: [CrowdStrike](https://www.crowdstrike.com/), [SentinelOne](https://www.sentinelone.com/)

- **Network anomaly detection** — Self-learning AI systems (Darktrace, Vectra AI) baseline normal network behavior and flag deviations in real time, replacing manual traffic analysis.
  Source: [Darktrace](https://darktrace.com/), [Vectra AI](https://www.vectra.ai/)

- **Phishing detection** — AI models analyze email content, sender reputation, URL patterns, and attachment behavior to identify phishing attempts with high accuracy.
  Source: [Palo Alto Networks](https://www.paloaltonetworks.com/)

- **Vulnerability scanning** — Automated tools (Tenable, Snyk, Checkmarx) continuously scan infrastructure and code for known vulnerabilities, generating prioritized remediation lists.
  Source: [Tenable](https://www.tenable.com/), [Snyk](https://snyk.io/)

## Partially Automated
*Tasks where humans direct the work, AI produces drafts or handles subtasks.*

- **Incident response** — AI handles initial triage, evidence collection, and playbook execution. Human analysts take over for root cause analysis, impact assessment, and cross-team coordination. The "agentic SOC" trend in 2026 pushes more of the initial response to AI agents.
  Source: [UnderDefense, Cybersecurity Trends 2026](https://underdefense.com/)

- **Threat hunting** — AI surfaces leads by correlating anomalous patterns and threat intelligence feeds. Human threat hunters investigate leads, form hypotheses, and pursue complex attack chains.
  Source: [CrowdStrike](https://www.crowdstrike.com/), [Vectra AI](https://www.vectra.ai/)

- **Compliance auditing** — AI automates evidence collection, control mapping, and continuous monitoring. Human auditors interpret regulatory requirements, handle edge cases, and make compliance determinations.
  Source: [SecurityScorecard](https://securityscorecard.com/)

- **Cloud security posture management** — AI tools (Wiz) continuously scan cloud configurations and flag misconfigurations. Humans prioritize remediation based on business context and risk tolerance.
  Source: [Wiz](https://www.wiz.io/)

- **Penetration testing (routine)** — Automated tools (Pentera) simulate common attack paths and identify exploitable vulnerabilities. Human testers handle novel attack vectors, social engineering, and chained exploits.
  Source: [Pentera](https://www.pentera.io/)

## AI-Assisted
*Tasks where humans do the core work, AI speeds it up.*

- **Threat intelligence analysis** — AI aggregates and correlates threat feeds, but human analysts provide geopolitical context, assess threat actor motivations, and produce strategic intelligence reports.
  Source: [RSAC 2026](https://www.rsaconference.com/)

- **Security code review** — AI tools (GitHub Copilot, Snyk, Checkmarx) flag potential vulnerabilities in code. Human reviewers assess business logic flaws, architectural weaknesses, and context-specific risks.
  Source: [GitHub Copilot](https://github.com/features/copilot), [Checkmarx](https://checkmarx.com/)

- **Third-party risk assessment** — AI scores vendor security postures continuously. Human analysts evaluate business criticality, contractual obligations, and risk appetite.
  Source: [SecurityScorecard](https://securityscorecard.com/)

## Still Fully Human
*Tasks AI cannot do in this field, and why.*

| Task | Why AI Can't Do This |
|------|---------------------|
| **Strategic security architecture** | Requires understanding business objectives, risk tolerance, regulatory landscape, and long-term technology roadmaps — all deeply contextual |
| **Threat intelligence requiring geopolitical context** | Assessing nation-state threat actors and geopolitical motivations requires human judgment about politics, history, and intent |
| **Security awareness training** | Effective training requires understanding organizational culture, tailoring messages to diverse audiences, and building human engagement |
| **Incident communication and crisis management** | Coordinating response across legal, PR, executive leadership, and regulators requires human diplomacy and judgment |
| **Creative ethical hacking** | Novel exploit chains, social engineering, and unconventional attack vectors require human creativity and lateral thinking |
| **Insider threat investigation** | Assessing employee behavior in context of HR situations, personal circumstances, and organizational dynamics requires human judgment and legal sensitivity |

## How The Role Is Changing

### What's shrinking
- Manual log review and alert triage → AI handles volume and initial classification
- Signature-based threat detection → ML-based behavioral detection replaces static rules
- Routine vulnerability scanning → Continuous automated scanning replaces periodic manual scans
- Basic incident classification → AI agents autonomously triage and categorize

### What's growing
- AI security operations management → Tuning, validating, and governing AI security tools
- Cloud and identity security → Expanding attack surface requires specialized expertise
- Complex incident investigation → As AI handles triage, humans focus on sophisticated attacks
- Security architecture and strategy → Designing defense-in-depth with AI-augmented tools
- AI/ML security → Protecting AI systems themselves from adversarial attacks

### New sub-roles emerging
- **AI SOC Engineer** — Configures, tunes, and validates AI-driven security automation platforms. Ensures AI agents follow appropriate playbooks and escalation paths.
- **AI Threat Analyst** — Specializes in AI-generated threats (deepfakes, AI-written malware, automated social engineering) and develops countermeasures.
- **Cloud Security Architect** — Designs security architecture for multi-cloud environments, integrating AI-powered posture management tools.
- **Security Automation Engineer** — Builds and maintains SOAR playbooks and agentic workflows that connect AI detection to automated response.

Source: [RSAC 2026](https://www.rsaconference.com/), [UnderDefense](https://underdefense.com/), [Sophos](https://www.sophos.com/)
