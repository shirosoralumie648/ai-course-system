# Feature Research: Course C Business AI Operations

**Domain:** 16-week role-based business AI operations curriculum
**Source of truth:** `docs/superpowers/specs/2026-06-05-course-c-business-ai-operations-design.md`
**Confidence:** High

## Table Stakes For v1

| Feature / Deliverable | Why Expected | Notes |
| --- | --- | --- |
| Course C landing page | Establishes positioning, audience, outcomes, and 16-week route | Must distinguish from Course A/B |
| 16-week teaching calendar | Core course structure | One virtual company story, one role scenario per week |
| Week 01-16 pages | Makes the course navigable and teachable | Each week needs business context, workflow, output, and compliance boundary |
| Lab 01-16 pages | Converts lessons into assignments | Each lab contributes to the assistant pack |
| Final project page | Defines capstone expectations | Role AI assistant pack + workflow transformation |
| Rubric page | Makes grading explicit | Use spec weights |
| Reference integration page | Keeps continuity with Course A/B reference practice | No new cloned repos required |
| Role AI assistant pack template | Central learner deliverable | Workflows, prompts, Skills, templates, data, tools, compliance, cases |
| Compliance templates | Mandatory for high-risk workflows | Disclaimer, approval, redaction, audit log |
| Sample business data | Makes the course usable immediately | CRM, finance, HR, contract, virtual company profile |
| Navigation integration | Required for public VitePress access | Nav/sidebar/homepage/reference map |

## Differentiators To Preserve

- Continuous virtual-company operating simulation.
- Role-based assistant pack as a reusable workplace artifact.
- Real workflow transformation with before/after, ROI, quality, or risk
  evidence.
- Four-gate compliance model: data, source, human, audit.
- Office/SaaS-first path for non-programmer enterprise learners.
- Controlled API/MCP exposure in the advanced layer.
- Clear Course A/B/C identity separation.

## Anti-Features

| Anti-feature | Why avoid | Alternative |
| --- | --- | --- |
| Prompt encyclopedia | Spec explicitly rejects scattered prompt collections | Anchor each week to business scenario and output |
| Coding-course depth | Target learners are business roles | Teach structured files, workflows, Skills, tables, API/MCP concepts |
| Production enterprise integrations | Too risky for first pass | Use plans, mocks, read-only examples, permissions, and audit |
| Live CRM/ERP/finance/tax/OA writes | Operational and compliance risk | Use sample data, import/export, templates, and mock workflows |
| Professional legal/tax/investment/HR/accounting advice | Liability and authority risk | AI drafts, checks, organizes, and reviews under human approval |
| New cloned reference repositories | Spec excludes this from v1 | Keep pages self-contained and update catalog mapping |
| Replacing human approval | Violates compliance boundary | Require human gate for high-risk decisions |

## Suggested Requirement Categories

- Course Shell
- Curriculum Structure
- Labs and Assignments
- Final Project
- Templates and Examples
- Compliance and Risk
- Reference Integration
- Learner Positioning
- Verification

## Feature Dependencies

```text
Course positioning -> Course C index -> nav/sidebar/homepage entry

16-week structure -> teaching calendar -> week pages -> lab pages

Compliance model -> weekly compliance sections -> final compliance packet -> rubric

Role AI assistant pack structure -> weekly assistant-pack updates -> final project

Virtual company profile + sample data -> weekly scenarios -> labs -> final transformation

Reference mapping -> reference integration page -> course-integration-map update

Office/SaaS-first path -> API/MCP advanced layer -> Week 15 enterprise connection plan
```

