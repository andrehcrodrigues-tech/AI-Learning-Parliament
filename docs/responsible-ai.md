# Responsible AI

## Data Policy

This project uses synthetic data only.

Do not include:
- real employee names;
- real emails;
- customer data;
- personally identifiable information;
- confidential documents;
- API keys;
- credentials;
- proprietary internal material.

## Responsible AI Controls

### 1. Grounding
Learning and assessment recommendations should be grounded in approved sources through Foundry IQ whenever available.

### 2. Transparency
The output clearly states that recommendations are AI-generated and should be reviewed by humans.

### 3. Human Oversight
The system does not automatically enrol learners, schedule exams or make HR decisions.

### 4. Privacy
Workload signals are synthetic and should be aggregated in production. Manager outputs should avoid exposing sensitive individual-level information.

### 5. Safety
The Critic Agent checks for:
- unrealistic schedules;
- unsupported claims;
- missing evidence;
- overconfident readiness decisions;
- privacy concerns.

### 6. Bias Mitigation
The system should be tested across different roles, workloads and career goals to avoid uneven recommendations.

## Limitations

- The MVP uses synthetic inputs.
- Foundry IQ grounding depends on quality of uploaded knowledge sources.
- Readiness scores are advisory, not official exam predictions.
- Human review is required before applying recommendations in real learning programmes.
