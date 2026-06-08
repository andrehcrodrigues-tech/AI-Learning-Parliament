# Technical Design

## Overview

AI Learning Parliament is implemented as a Microsoft Foundry multi-agent workflow.

The design follows a role-based specialisation pattern with a final synthesis layer and a Critic/Verifier pattern.

## Components

### 1. Input Layer
The user provides:
- role or job function;
- target certification;
- current skills;
- available study hours;
- workload signals;
- career goals;
- team objectives.

### 2. Orchestration Layer
Microsoft Foundry Workflow coordinates all agents.

The MVP uses sequential orchestration for reliability in Foundry Preview. A future version can move to parallel fan-out/fan-in execution.

### 3. Knowledge Layer
Foundry IQ is used as the grounding layer for:
- approved certification documents;
- Microsoft Learn references;
- internal synthetic learning guides;
- assessment criteria.

### 4. Work Context Layer
Synthetic Work IQ-style signals represent:
- meeting hours;
- focus hours;
- preferred learning windows;
- workload pressure.

### 5. Semantic Layer
A Fabric IQ-style semantic model represents:
- learner;
- role;
- certification;
- skill gap;
- readiness score;
- recommended hours;
- pass threshold.

### 6. Reasoning Layer
Agents reason independently from different perspectives.

### 7. Critic Layer
The Critic Agent validates contradictions, missing evidence and unrealistic recommendations.

### 8. Output Layer
The Speaker Agent generates the final Certification Readiness Report.

## Deployment Options

### Hackathon MVP
- Microsoft Foundry UI
- Foundry agents
- Foundry workflow
- GitHub repository

### Enhanced Demo
- Streamlit frontend
- Python wrapper
- Foundry workflow endpoint

### Production Story
- Hosted Agent in Foundry Agent Service
- Azure Container Registry
- Managed Identity
- Observability and evaluation
