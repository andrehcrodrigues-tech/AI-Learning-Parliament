# AI Learning Parliament

AI Learning Parliament is a multi-agent reasoning system for certification readiness and enterprise learning decisions.

The solution uses Microsoft Foundry Agents, Foundry Workflows and a curated Knowledge Base to produce transparent, evidence-based certification recommendations.

## Purpose

Enterprise learning decisions are often too generic. They usually ignore:

- learner career goals
- certification readiness
- available study capacity
- manager and team priorities
- future skill relevance
- operational delivery risk

AI Learning Parliament solves this through a structured multi-agent decision process.

## Final Architecture

The current architecture uses five stakeholder agents, followed by a Critic Agent and a Speaker Agent.

```text
Manager-Agent
Career-Growth-Agent
Readiness-Agent
Capacity-Agent
Future-Skills-Agent
        ↓
Critic-Agent
        ↓
Speaker-Agent
```

## Agents

### Manager-Agent
Evaluates manager goals, team capability, delivery impact, operational risk and short-term execution feasibility.

### Career-Growth-Agent
Evaluates career progression, target role alignment and whether the certification supports the learner's professional growth.

### Readiness-Agent
Evaluates certification readiness, practice score thresholds, weak areas and exam preparedness.

### Capacity-Agent
Evaluates study hours, meeting load, workload risk and whether a realistic study effort is feasible.

### Future-Skills-Agent
Evaluates whether the certification develops skills that remain strategically relevant over the next 3 to 5 years.

### Critic-Agent
Validates stakeholder consistency, evidence quality, contradictions, risks and whether the recommendation should proceed, be revised or blocked.

### Speaker-Agent
Synthesizes stakeholder outputs and Critic validation into the final AI Learning Parliament Decision.

## Key Differentiators

- Multi-perspective evaluation
- Evidence-based decisions
- Agent-specific knowledge grounding
- Explainable final recommendation
- Critic validation before final decision
- Scalable to additional certifications and career paths

## Repository Structure

```text
agents/             Final prompt instructions for each agent
workflow/           Microsoft Foundry workflow YAML
knowledge-base/     Agent-specific KB source documents
architecture/       Architecture diagram and explanation
demo/               Demo prompts and expected outcomes
docs/               Supporting documentation
data/synthetic/     Synthetic datasets used for demo only
.github/workflows/  Basic CI validation
```

## Demo Scenarios

The demo includes three validation scenarios:

1. Favourable candidate → expected decision: Start Now
2. Unfavourable candidate → expected decision: Delay
3. Misaligned career path → expected decision: Delay or Alternative Certification

## Responsible AI

This project uses synthetic examples and synthetic learning/workload data only. Do not upload real employee data, confidential information, credentials or personal identifiable information.

## Technologies

- Microsoft Foundry
- Foundry Agents
- Foundry Workflows
- Foundry IQ / Knowledge Base
- Azure Blob Storage
- Azure AI Search
- Azure OpenAI / GPT models
