# Requirements: Course C Business AI Operations

**Defined:** 2026-06-05
**Core Value:** Course C must show non-engineering business roles how to use AI
agents safely and repeatably for real enterprise workflows, with useful outputs
and explicit human approval gates.

## v1 Requirements

### Course Shell

- [ ] **SHELL-01**: Visitor can open a Course C landing page that explains the
  course positioning, audience, outcomes, and 16-week route.
- [ ] **SHELL-02**: Visitor can reach Course C from the VitePress top navigation,
  homepage course cards/actions, and Course C sidebar.
- [ ] **SHELL-03**: Course C landing copy clearly distinguishes Course C from
  Course A prototype literacy and Course B software product engineering.
- [ ] **SHELL-04**: Course C includes `teaching-calendar.md`,
  `reference-integration.md`, `final-project.md`, and `rubric.md`.

### Curriculum Structure

- [ ] **CURR-01**: Course C includes Week 01 through Week 16 pages under
  `docs/course-c/`.
- [ ] **CURR-02**: Every week page follows the same learning rhythm: business
  situation, role boundary, inputs, AI workflow, tool/application integration,
  compliance review, assistant-pack update, and acceptance criteria.
- [ ] **CURR-03**: The 16-week structure advances one continuous virtual company
  from market entry to AI operating-system maturity.
- [ ] **CURR-04**: Weekly topics cover the approved roles and scenarios from the
  design spec, including market research, product, brand, sales, data,
  investment, finance, tax, HR, legal, administration, enterprise systems, and
  final defense.

### Labs And Assignments

- [ ] **LAB-01**: Course C includes Lab 01 through Lab 16 pages under
  `docs/course-c/labs/`.
- [ ] **LAB-02**: Every lab asks students to produce concrete evidence for the
  corresponding week, such as reports, tables, dashboards, SOPs, templates,
  approval records, or audit logs.
- [ ] **LAB-03**: Every lab contributes at least one reusable artifact to the
  learner's role AI assistant pack.

### Templates And Examples

- [ ] **TEMP-01**: Course C includes a role AI assistant pack template with role
  profile, workflows, prompts, Skills, templates, data, tools, compliance, and
  cases sections.
- [ ] **TEMP-02**: Course C includes reusable templates for workflow SOP, prompt
  library, compliance checklist, audit log, and ROI or quality-improvement
  report.
- [ ] **TEMP-03**: Course C includes synthetic sample artifacts for the virtual
  company, CRM, finance, HR, and contract/dispute examples.
- [ ] **TEMP-04**: Template and example pages do not contain real personal,
  customer, employee, financial, tax, legal, credential, or production system
  data.

### Compliance And Risk

- [ ] **RISK-01**: Course C defines a four-gate compliance model: data gate,
  source gate, human gate, and audit gate.
- [ ] **RISK-02**: High-risk weeks covering investment, finance, tax, HR, legal,
  administration, and enterprise systems state what AI can support and what it
  must not directly do.
- [ ] **RISK-03**: High-risk labs require evidence of redaction/source checking,
  human approval, and audit logging.
- [ ] **RISK-04**: Course wording avoids presenting AI as a licensed legal, tax,
  investment, HR, accounting, or management decision maker.
- [ ] **RISK-05**: Week 15 enterprise system/API/MCP content uses read-only,
  mock-first, least-privilege, permissioned, and auditable integration framing.

### Final Project And Rubric

- [ ] **FINAL-01**: Final project requires both a role AI assistant pack and a
  real or realistic workflow transformation report.
- [ ] **FINAL-02**: Final project evidence includes before-state, after-state,
  reusable assets, compliance packet, and ROI/quality/risk improvement proof.
- [ ] **FINAL-03**: Rubric uses the approved weighting: business framing 15%,
  assistant-pack completeness 25%, weekly outputs 20%, compliance/risk 20%, and
  workflow transformation 20%.
- [ ] **FINAL-04**: Rubric rewards reuse, clarity, safety, evidence, and
  transformation quality rather than prompt-library volume.

### Reference Integration

- [ ] **REF-01**: `docs/course-c/reference-integration.md` explains how business,
  operations, AI workflow, SaaS, compliance, and API/MCP references inform Course
  C.
- [ ] **REF-02**: `reference/catalog/course-integration-map.md` includes a Course
  C section.
- [ ] **REF-03**: Published Course C pages remain self-contained and do not
  require local ignored `reference/repos/` content.

### Verification

- [ ] **VER-01**: `BASE=/ai-course-system/ npm run build` succeeds from `docs/`
  after Course C implementation.
- [ ] **VER-02**: Course C navigation links, week links, lab links, template
  links, final project, rubric, and reference integration pages are reachable.
- [ ] **VER-03**: Course C implementation does not commit `docs/.vitepress/dist`,
  `docs/node_modules`, local archives, or `reference/repos/`.

## v2 Requirements

### Content Depth

- **DEPTH-01**: Expand every Course C week into a full long-form chapter after
  the first navigable pass has been verified.
- **DEPTH-02**: Add instructor scripts and slide outlines for Course C weeks.
- **DEPTH-03**: Add richer visual diagrams or interactive examples after
  Markdown build stability is proven.

### Integrations

- **INT-01**: Add optional safe read-only MCP/API demos using mock systems.
- **INT-02**: Add optional private-enterprise deployment guidance for internal
  training environments.

## Out of Scope

| Feature | Reason |
| --- | --- |
| Production CRM/ERP/finance/tax/OA writes | Unsafe and outside first course-content pass |
| Professional legal/tax/investment/HR/accounting advice | AI is a workflow assistant, not a licensed professional or final decision maker |
| New large reference clones | `reference/repos/` is local-only and ignored by git |
| Rewriting Course A/B | Course C should be additive except necessary navigation/homepage links |
| New frontend app or backend service | Existing VitePress site is sufficient for v1 |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| SHELL-01 | Phase 1 | Pending |
| SHELL-02 | Phase 1 | Pending |
| SHELL-03 | Phase 1 | Pending |
| SHELL-04 | Phase 1 | Pending |
| CURR-01 | Phase 3 | Pending |
| CURR-02 | Phase 3 | Pending |
| CURR-03 | Phase 3 | Pending |
| CURR-04 | Phase 4 | Pending |
| LAB-01 | Phase 3 | Pending |
| LAB-02 | Phase 3 | Pending |
| LAB-03 | Phase 3 | Pending |
| TEMP-01 | Phase 2 | Pending |
| TEMP-02 | Phase 2 | Pending |
| TEMP-03 | Phase 2 | Pending |
| TEMP-04 | Phase 2 | Pending |
| RISK-01 | Phase 2 | Pending |
| RISK-02 | Phase 4 | Pending |
| RISK-03 | Phase 4 | Pending |
| RISK-04 | Phase 4 | Pending |
| RISK-05 | Phase 5 | Pending |
| FINAL-01 | Phase 6 | Pending |
| FINAL-02 | Phase 6 | Pending |
| FINAL-03 | Phase 6 | Pending |
| FINAL-04 | Phase 6 | Pending |
| REF-01 | Phase 6 | Pending |
| REF-02 | Phase 6 | Pending |
| REF-03 | Phase 6 | Pending |
| VER-01 | Phase 6 | Pending |
| VER-02 | Phase 6 | Pending |
| VER-03 | Phase 6 | Pending |

**Coverage:**
- v1 requirements: 30 total
- Mapped to phases: 30
- Unmapped: 0

---
*Requirements defined: 2026-06-05*
*Last updated: 2026-06-05 after initial definition*

