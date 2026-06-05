# Roadmap: Course C Business AI Operations

**Created:** 2026-06-05
**Mode:** Vertical MVP
**Granularity:** Standard

## Overview

Course C will be delivered as a complete, navigable VitePress course in six
phases. The roadmap prioritizes a public course shell first, then reusable
compliance/template foundations, then weekly content in risk-aware groups, and
finally full verification.

## Phases

### Phase 1: Course C Site Skeleton
**Goal:** Create the public Course C entry points and stable route structure.
**Mode:** mvp

**Requirements:** SHELL-01, SHELL-02, SHELL-03, SHELL-04

**Success Criteria:**
1. `docs/course-c/index.md`, `teaching-calendar.md`, `reference-integration.md`,
   `final-project.md`, and `rubric.md` exist with first-pass content.
2. `docs/.vitepress/config.mjs` exposes Course C in top navigation and sidebar.
3. `docs/index.md` includes Course C in homepage actions/cards.
4. Course C positioning clearly says it is business operations and role-agent
   workflow training, not Course A prototype literacy or Course B engineering.

**UI hint:** yes

### Phase 2: Compliance, Templates, And Synthetic Examples
**Goal:** Establish the reusable assistant-pack and compliance foundation that
all weeks can reference.
**Mode:** mvp

**Requirements:** TEMP-01, TEMP-02, TEMP-03, TEMP-04, RISK-01, REF-01, REF-04,
REF-05

**Success Criteria:**
1. `docs/course-c/templates/` contains role assistant pack, workflow SOP, prompt
   library, compliance checklist, audit log, and ROI report templates.
2. `docs/course-c/examples/` contains synthetic virtual company, CRM, finance,
   HR, and contract/dispute examples.
3. Compliance templates define data, source, human, and audit gates.
4. Examples contain no real personal, customer, employee, credential, financial,
   tax, or legal data.
5. Course C source rules require professional business pages to consult
   authoritative domain books, papers, official standards/regulations, regulator
   guidance, or industry body materials in addition to code/tool docs.
6. `docs/course-c/reference-integration.md` explains the difference between
   implementation sources and professional domain sources.

**UI hint:** no

### Phase 3: Core Business Weeks 01-07 And Labs
**Goal:** Build the non-high-risk operating spine from company setup through
market, product, brand, sales, customer operations, and dashboards.
**Mode:** mvp

**Requirements:** CURR-01, CURR-02, CURR-03, LAB-01, LAB-02, LAB-03

**Success Criteria:**
1. Week 01-07 pages exist and follow the required weekly rhythm.
2. Lab 01-07 pages exist and produce concrete evidence tied to weekly outputs.
3. The virtual company story is visible across Weeks 01-07.
4. Each week/lab updates the role AI assistant pack with a reusable artifact.
5. Market research, product, brand, sales, and data-analysis pages include
   professional domain references beyond code/tool documentation.

**UI hint:** no

### Phase 4: High-Risk Business Weeks 08-14 And Labs
**Goal:** Add investment, investment banking, finance, tax, HR, legal, and admin
weeks with explicit compliance boundaries.
**Mode:** mvp

**Requirements:** CURR-04, RISK-02, RISK-03, RISK-04

**Success Criteria:**
1. Week 08-14 pages exist and cover all approved high-risk role scenarios.
2. Lab 08-14 pages require redaction/source checking, human approval, and audit
   evidence where applicable.
3. Course wording frames AI as draft, analysis, organization, review, and
   workflow support, not final professional judgment.
4. Investment, tax, HR, legal, finance, and admin pages state what AI must not
   directly do.
5. Investment, finance, tax, HR, legal, and administration pages cite
   authoritative domain sources, and distinguish those sources from AI/tool
   implementation docs.

**UI hint:** no

### Phase 5: Enterprise System Connection And AI Workflow
**Goal:** Add Week 15 and Lab 15 for safe API/MCP and enterprise-system planning.
**Mode:** mvp

**Requirements:** RISK-05

**Success Criteria:**
1. Week 15 explains Skills, API/MCP connection planning, permission boundaries,
   and audit process.
2. Lab 15 asks students to produce a read-only/mock-first connection plan.
3. Content uses least privilege, secret hygiene, no production writes, and human
   approval as hard constraints.
4. Week 15 remains accessible to business learners by keeping code optional and
   conceptual.
5. Week 15 uses both implementation references for API/MCP mechanics and
   authoritative governance/security references for enterprise permissions,
   audit, and operational risk.

**UI hint:** no

### Phase 6: Final Project, Reference Map, And Verification
**Goal:** Complete capstone framing, reference integration, and public-site
verification.
**Mode:** mvp

**Requirements:** FINAL-01, FINAL-02, FINAL-03, FINAL-04, REF-02, REF-03, VER-01,
VER-02, VER-03

**Success Criteria:**
1. Week 16, Lab 16, final project, and rubric align around assistant pack plus
   workflow transformation evidence.
2. Rubric uses the approved 15/25/20/20/20 weighting and rewards reuse, safety,
   evidence, and transformation quality.
3. `docs/course-c/reference-integration.md` and
   `reference/catalog/course-integration-map.md` include Course C mapping without
   requiring local `reference/repos/`.
4. `BASE=/ai-course-system/ npm run build` succeeds from `docs/`.
5. Course C links are reachable and no generated build output, dependencies,
   local archives, or ignored reference repos are committed.
6. Final QA checks that each professional scenario has both source types where
   relevant: implementation/tool references and authoritative domain references.

**UI hint:** yes

## Requirement Coverage

| Phase | Requirements |
| --- | --- |
| Phase 1 | SHELL-01, SHELL-02, SHELL-03, SHELL-04 |
| Phase 2 | TEMP-01, TEMP-02, TEMP-03, TEMP-04, RISK-01, REF-01, REF-04, REF-05 |
| Phase 3 | CURR-01, CURR-02, CURR-03, LAB-01, LAB-02, LAB-03 |
| Phase 4 | CURR-04, RISK-02, RISK-03, RISK-04 |
| Phase 5 | RISK-05 |
| Phase 6 | FINAL-01, FINAL-02, FINAL-03, FINAL-04, REF-02, REF-03, VER-01, VER-02, VER-03 |

**Coverage:** 32 of 32 v1 requirements mapped.

## Phase Dependencies

```text
Phase 1 -> Phase 2 -> Phase 3 -> Phase 4 -> Phase 5 -> Phase 6
```

Phase 1 creates stable routes. Phase 2 creates reusable templates and safety
rules. Phases 3-5 create weekly content using that foundation. Phase 6 verifies
the full site and final project contract.

## Risks To Monitor

- Prompt-library drift: every week must stay attached to a business scenario,
  input, output, and evidence.
- Compliance overclaiming: high-risk pages must not imply professional
  authority or AI final decision-making.
- VitePress parse failures: first pass should stay mostly Markdown and fenced
  code; avoid complex multiline component props.
- Reference leakage: public pages must not require ignored `reference/repos/`.
- Base-path breakage: verify with `BASE=/ai-course-system/`.
- Shallow professional research: phase work must not rely only on coding docs
  when teaching business, finance, legal, HR, tax, sales, product, brand, market
  research, governance, or management tasks.

---
*Roadmap updated: 2026-06-05 after adding authoritative domain-source gate*
