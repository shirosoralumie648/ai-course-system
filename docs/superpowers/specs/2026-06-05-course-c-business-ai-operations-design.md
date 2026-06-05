# Course C Business AI Operations Design

## Goal

Add Course C as a 16-week business and management course that teaches enterprise
operators, managers, and founders how to use AI tools as role-based business
assistants. The course should move beyond coding and show how Codex, Claude
Code, office tools, business SaaS, Skills, prompts, SOPs, APIs, and MCP can
support real workflows across market research, product positioning, brand,
sales, data analysis, investment analysis, finance, HR, legal, administration,
and business operations.

## Positioning

Course C is:

- A business operations and role-agent course, not a coding course.
- A virtual-company operating simulation, not a disconnected prompt library.
- A workflow and compliance course, not a promise that AI can replace licensed
  financial, tax, legal, HR, or management judgment.

Relationship to current courses:

| Course | Primary learner | Main outcome |
| --- | --- | --- |
| Course A | Non-CS students | First AI product prototype and Claude Code workflow literacy |
| Course B | Technical students | AI full-stack product delivery and engineering evidence |
| Course C | Enterprise staff, managers, founders | Role-based AI assistant pack and real business-process transformation |

## Target Learners

The primary audience is enterprise staff and managers:

- Sales, marketing, HR, finance, legal, administration, product, data analysis,
  and operations teams.
- Founders and managers who want to build a lightweight AI operating system for
  their company.
- Business users who can work with documents, spreadsheets, dashboards, and SaaS
  systems, but do not need full software engineering depth.

The course assumes basic business literacy and normal office-tool ability. It
does not assume programming ability, but it does expose students to structured
files, project folders, Skills, simple data tables, API/MCP concepts, and
reviewable AI workflows.

## Core Design Decision

Use a hybrid of three structures:

- Main structure: one virtual company operating story across 16 weeks.
- Weekly structure: one role or business scenario per week.
- Final structure: each learner creates a role-specific AI assistant pack and
  applies it to one real workflow, proving before/after improvement.

This avoids a scattered "prompt collection" course while still making each week
usable as a standalone enterprise workshop.

## Tool Integration Layers

Course C covers four levels of tool integration.

| Layer | Examples | Course use |
| --- | --- | --- |
| Office delivery | Word, Excel, PowerPoint, Feishu, DingTalk, Notion, Canva | Reports, dashboards, customer materials, meeting notes, presentations |
| Business SaaS | CRM, BI, survey tools, recruiting systems, finance tools, contract management, helpdesk | Field design, import/export, templates, workflow records |
| AI workflow | Codex, Claude Code, prompts, Skills, SOPs, folder conventions, reusable commands | Role assistant packs, review loops, repeatable workflows |
| Enterprise systems | API, MCP, database, ERP, OA, CRM, finance systems | Advanced demos and optional internal-training paths with permissions and audit |

The required course path should focus on the first three layers. Enterprise
system connection is included as a controlled advanced layer, never as an
unrestricted write path into production systems.

## Compliance Boundary

High-risk modules must treat AI as a standardized workflow assistant, draft
generator, analysis helper, and auditable system interface. AI must not be
positioned as the final decision maker.

Every high-risk workflow uses four gates:

1. Data gate: sensitive business, customer, employee, contract, financial, tax,
   and investment data must be redacted or handled under an explicit permission
   rule before being sent to AI tools.
2. Source gate: reports must distinguish facts, assumptions, analysis,
   inference, and recommendations. Sources must be recorded.
3. Human gate: external release, investment decisions, contracts, tax filings,
   hiring decisions, salary decisions, legal dispute handling, and policy
   publication require human approval.
4. Audit gate: key inputs, AI outputs, human edits, approval records, and final
   conclusions must be retained.

Required compliance artifacts:

- `disclaimer.md`: AI output boundaries and role responsibility.
- `human-approval.md`: who approves what and when.
- `data-redaction.md`: what data is removed or masked.
- `audit-log.md`: input, output, modification, and approval trail.

## High-Risk Scenario Rules

| Scenario | AI can support | AI must not directly do |
| --- | --- | --- |
| Public stock investment | Public-information summaries, research framework, risk list, valuation assumption table | Buy/sell instruction, return guarantee, final investment decision |
| Investment banking | Due-diligence checklist, business plan, financing materials, roadshow Q&A | Substitute professional due diligence, valuation approval, regulatory review |
| Finance | Cost analysis, budget draft, financial statement explanation, anomaly checklist | Replace finance owner sign-off |
| Tax | Filing material checklist, process SOP, policy summary, risk checklist | Submit filings or bypass tax professional confirmation |
| HR | Job descriptions, screening tables, interview questions, training and performance drafts | Automatically decide hiring, rejection, salary, discipline, or termination |
| Legal | Contract initial review, clause risk spotting, dispute material organization | Replace lawyer opinion, handle litigation directly |
| Administration | Meeting minutes, fixed-asset records, qualification checklists, policy drafts | Publish policy, purchase assets, or change credentials without approval |
| Enterprise systems | Read-only query, suggested updates, draft workflow records | Delete data, write to core systems, or override permissions without controls |

## 16-Week Course Structure

The course follows one virtual company from market entry to operating-system
maturity. Each week solves one business problem and contributes to the learner's
role AI assistant pack.

| Week | Topic | Role scenario | Core output |
| --- | --- | --- | --- |
| 01 | AI enterprise operating system overview | Manager / founder | Company profile, AI assistant team map, project folder convention |
| 02 | Market research and industry analysis | Market research / strategy | Industry report, competitor table, survey, source audit sheet |
| 03 | Product positioning and prototype expression | Product / design | Positioning document, user personas, priority matrix, prototype prompts |
| 04 | Brand promotion and content assets | Brand / marketing | Brand guide, campaign theme, content calendar, poster or video script |
| 05 | Sales leads and channel development | Sales / BD | Target-account list, channel plan, email and outreach templates |
| 06 | Customer relationship maintenance and sales execution | Sales management | CRM field design, meeting notes, follow-up workflow, sales funnel dashboard |
| 07 | Data analysis and management dashboards | Data analysis / operations | KPI tree, data cleaning workflow, operating dashboard |
| 08 | Public stock and investment analysis | Investment research / management | Company research framework, valuation assumption table, investment memo, risk disclosure |
| 09 | Investment banking and business planning | Financing / strategy | Business plan, financing deck outline, due-diligence checklist, roadshow Q&A |
| 10 | Financial management and budget analysis | Finance | Budget table, cost analysis table, financial-statement analysis, budget explanation |
| 11 | Tax filing and compliance records | Finance / tax | Tax material checklist, filing SOP, risk checklist, compliance ledger |
| 12 | Human resources management | HR | Job description, resume screening table, interview bank, training and performance plan |
| 13 | Legal contracts and dispute handling | Legal / management | Contract review checklist, contract draft, dispute material packet, legal-risk memo draft |
| 14 | Administration and corporate governance | Administration / general management | Fixed-asset ledger, meeting minutes, policy draft, qualification-maintenance checklist |
| 15 | Enterprise system connection and AI workflow | Manager / digital operations | Skills, API/MCP connection plan, permission and audit process |
| 16 | Real workflow transformation defense | Learner-selected role | Role AI assistant pack, transformation report, ROI or quality-improvement evidence |

## Weekly Learning Rhythm

Each week should use the same operating rhythm:

1. Business situation: define the virtual-company problem.
2. Role boundary: explain what this role owns and what requires approval.
3. Inputs: provide sample data, documents, emails, tables, or public sources.
4. AI workflow: use prompts, Skills, templates, spreadsheet logic, and review
   loops to produce the weekly output.
5. Application integration: show the office tool, SaaS, or system connection
   relevant to that week.
6. Compliance review: run source, data, human, and audit checks.
7. Assistant-pack update: add a reusable workflow, prompt, template, or
   compliance artifact.

## Role AI Assistant Pack

Every learner builds a reusable role AI assistant pack:

```text
role-ai-assistant-pack/
├── README.md
├── role-profile.md
├── workflows/
│   ├── 01-research.md
│   ├── 02-analysis.md
│   ├── 03-draft.md
│   ├── 04-review.md
│   └── 05-approval.md
├── prompts/
│   ├── system-prompts.md
│   ├── task-prompts.md
│   └── review-prompts.md
├── skills/
│   ├── market-research-skill.md
│   ├── report-review-skill.md
│   └── compliance-check-skill.md
├── templates/
│   ├── report-template.md
│   ├── dashboard-schema.md
│   ├── email-template.md
│   └── meeting-minutes-template.md
├── data/
│   ├── sample-customers.csv
│   ├── sample-finance.csv
│   └── sample-hr.csv
├── tools/
│   ├── office-tools.md
│   ├── crm-bi-hr-finance-tools.md
│   └── mcp-api-plan.md
├── compliance/
│   ├── human-approval.md
│   ├── data-redaction.md
│   ├── audit-log.md
│   └── disclaimer.md
└── cases/
    ├── before.md
    ├── after.md
    ├── roi.md
    └── evidence/
```

The assistant pack is graded on reuse, clarity, safety, and evidence. A large
prompt collection alone is not sufficient.

## Final Project

The final project has two parts:

1. Role AI assistant pack: a complete package for one business role or
   management scenario.
2. Real workflow transformation: one real or realistic business process
   redesigned with AI support.

Required final evidence:

- Before-state description: current process, pain point, time cost, quality
  problems, or risk.
- After-state workflow: new AI-assisted process, required tools, human approval,
  and audit trail.
- Reusable assets: prompts, templates, SOPs, Skills, data schemas, or dashboard
  structures.
- Compliance packet: disclaimer, data redaction, approval rule, audit log.
- Impact proof: ROI estimate, time saving, quality improvement, risk reduction,
  consistency improvement, or stakeholder feedback.

## Grading Model

Suggested weighting:

| Area | Weight | Evidence |
| --- | --- | --- |
| Business problem framing | 15% | Clear process, role boundary, inputs, and success criteria |
| Assistant-pack completeness | 25% | Workflows, prompts, templates, tools, data examples, compliance artifacts |
| Weekly role outputs | 20% | Completed outputs across market, sales, data, finance, HR, legal, admin, and management |
| Compliance and risk controls | 20% | Redaction, source tracking, approval, audit, disclaimers |
| Real workflow transformation | 20% | Before/after comparison, ROI or quality evidence, reusable workflow |

## Reference Material Mapping

Course C should extend the current reference system with business and operations
sources. Initial mapping:

| Course area | Useful reference categories | Use |
| --- | --- | --- |
| AI workflow and Skills | `reference/repos/agentic-coding/spec-kit`, `reference/repos/mcp/*`, Claude Code and Codex guides | Role assistant pack structure, workflow rules, review loops |
| Data and dashboards | public BI examples, spreadsheet templates, company KPI frameworks | KPI tree, dashboard schema, data cleaning workflow |
| Product and brand | product discovery books, positioning frameworks, marketing playbooks | Product positioning, brand guide, content calendar |
| Sales and CRM | CRM playbooks, sales funnel frameworks | Lead list, CRM fields, customer follow-up process |
| Finance and investment | public company filings, valuation primers, accounting templates | Investment memo, financial analysis, budget and cost templates |
| HR and administration | HR playbooks, interview frameworks, policy templates | Recruiting, training, performance, policy, asset and meeting workflows |
| Legal and compliance | contract checklists, privacy and compliance frameworks | Contract review, dispute materials, approval and audit rules |

When implementation begins, add Course C entries to
`reference/catalog/course-integration-map.md`. Do not clone large new reference
repositories as part of the first Course C implementation pass.

## File-Level Implementation Scope

Course C should follow the existing VitePress structure:

```text
docs/course-c/
├── index.md
├── teaching-calendar.md
├── final-project.md
├── rubric.md
├── reference-integration.md
├── week-01.md ... week-16.md
├── labs/
│   ├── lab-01.md ... lab-16.md
├── templates/
│   ├── role-ai-assistant-pack.md
│   ├── workflow-sop.md
│   ├── prompt-library.md
│   ├── compliance-checklist.md
│   ├── audit-log.md
│   └── roi-report.md
└── examples/
    ├── virtual-company-profile.md
    ├── sample-crm.csv
    ├── sample-finance.csv
    ├── sample-hr.csv
    └── sample-contract.md
```

Update these shared/navigation files:

- `docs/.vitepress/config.mjs`: add Course C nav and sidebar.
- `docs/index.md`: add a Course C action and feature card.
- `docs/shared/index.md`: optionally link Course C templates and compliance
  materials if shared pages are added.
- `reference/catalog/course-integration-map.md`: add Course C mapping.

## Initial Content Scope

The first implementation pass should create a complete navigable Course C, but
does not need to write every week as a long chapter.

Required first pass:

- Course C index with positioning, audience, outcomes, and 16-week route.
- Teaching calendar.
- Final project requirements.
- Rubric.
- Reference integration page.
- Week 01 through Week 16 pages with business context, workflow, output, and
  compliance boundary.
- Lab 01 through Lab 16 pages with weekly assignments.
- Templates and sample data needed to make the course immediately usable.

Out of first pass:

- Production-grade enterprise system integrations.
- Live CRM, ERP, finance, tax, or OA writes.
- New cloned reference repositories.
- Legal, tax, investment, HR, or accounting advice that claims professional
  authority.

## Weekly Page Template

Each Course C week should use this target structure:

```markdown
# 第 N 周：主题

## 本周经营问题
## 角色职责与边界
## 输入材料
## AI 工作流
## 工具与应用接入
## 交付物模板
## 合规与风险检查
## 加入岗位 AI 助理包
## 验收标准
```

## Acceptance Criteria

The design is ready for implementation when:

- Course C is clearly distinct from Course A and Course B.
- The 16-week structure covers virtual-company operations and weekly role
  scenarios.
- The role AI assistant pack structure is explicit and reusable.
- High-risk scenarios have compliance boundaries and required artifacts.
- File-level implementation scope matches the current VitePress repo.
- No requirement depends on untracked local `reference/repos/` content being
  available on GitHub Pages.

## Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Course C becomes a prompt encyclopedia | Anchor every week to the virtual company and a concrete business output. |
| Business scope becomes too broad | Keep one 16-week operating story and let final projects specialize by role. |
| High-risk topics create liability | Require source tracking, disclaimers, human approval, redaction, and audit logs. |
| Non-technical learners get blocked by API/MCP | Make API/MCP an advanced layer; required path uses office tools, SaaS import/export, prompts, and Skills. |
| Course C overlaps Course B | Course C focuses on business workflows and documents; Course B owns software product engineering. |
| Reference repositories are unavailable online | Treat `reference/repos/` as local teacher prep only and keep course pages self-contained. |

