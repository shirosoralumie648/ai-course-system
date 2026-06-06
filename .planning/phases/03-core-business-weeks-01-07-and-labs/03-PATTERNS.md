# Phase 3: Core Business Weeks 01-07 And Labs - Patterns

**Mapped:** 2026-06-06
**Status:** Complete

## Reusable Assets

| Asset | Reuse In Phase 3 |
|---|---|
| `docs/course-c/teaching-calendar.md` | Source of Week 01-07 topics, roles, outputs, and concrete tasks. |
| `docs/course-c/reference-integration.md` | Required source split and citation/use fields for every professional week. |
| `docs/course-c/templates/role-ai-assistant-pack.md` | Labs update this assistant-pack structure each week. |
| `docs/course-c/templates/workflow-sop.md` | Used by Week/Lab workflow outputs. |
| `docs/course-c/templates/prompt-library.md` | Used for reusable task/review prompts. |
| `docs/course-c/templates/compliance-checklist.md` | Four-gate compliance reference for all weeks/labs. |
| `docs/course-c/templates/audit-log.md` | Evidence record referenced by labs. |
| `docs/course-c/templates/roi-report.md` | Introduced lightly for Week 07 dashboard/management improvement evidence. |
| `docs/course-c/examples/virtual-company-profile.md` | Continuous fictional company story. |
| `docs/course-c/examples/sample-crm.csv` | Week 05-06 sales/CRM data source. |
| `docs/.vitepress/config.mjs` | Course C sidebar updates after pages exist. |

## Established Patterns

- Course pages are static Markdown under `docs/`.
- Sidebar routes omit `.md`; directory routes require `index.md`.
- Existing Course A/B weeks use H1 title, narrative scenario, optional
  `ChapterIntroduction`, `StepBar`, tables, prompts, and practical checks.
- Labs use operational steps, submission requirements, validation checks, and
  scoring tables.
- Course C must add business-specific sections: role boundary, reference use,
  compliance review, and assistant-pack update.

## File Mapping

| New/Modified File | Closest Analog | Notes |
|---|---|---|
| `docs/course-c/week-01.md` | `docs/course-c/index.md`, `docs/course-a/week-01.md` | Course C operating-system setup; use business scenario rather than coding/game frame. |
| `docs/course-c/week-02.md` | `docs/course-c/reference-integration.md` | Market research source audit; strongest source-gate page in this slice. |
| `docs/course-c/week-03.md` | `docs/course-b/week-01.md` | Prototype expression, but non-engineering and product-positioning focused. |
| `docs/course-c/week-04.md` | `docs/course-c/templates/prompt-library.md` | Brand voice/content assets tied to review workflow. |
| `docs/course-c/week-05.md` | `docs/course-c/examples/sample-crm.csv` | Lead segmentation and outreach workflow. |
| `docs/course-c/week-06.md` | `docs/course-c/templates/workflow-sop.md` | Meeting note to CRM fields and follow-up SOP. |
| `docs/course-c/week-07.md` | `docs/course-c/templates/roi-report.md` | KPI tree and dashboard spec. |
| `docs/course-c/labs/lab-01.md` through `lab-07.md` | `docs/course-a/labs/lab-01.md`, `docs/course-b/labs/lab-01.md` | Evidence-first lab pattern with scoring table. |
| `docs/.vitepress/config.mjs` | Existing Course C sidebar block | Add `每周教程` and `逐周实验` groups for existing Phase 3 files only. |

## Integration Constraints

- Do not add Week 08-16 or Lab 08-16 files or sidebar links in Phase 3.
- Do not commit `docs/.vitepress/dist`, `docs/node_modules`, `.local-archive`,
  or `reference/repos`.
- Do not require real SaaS accounts, private company data, production API
  access, or live enterprise system writes.
- Build verification must use `BASE=/ai-course-system/`.

---

*Phase: 03-core-business-weeks-01-07-and-labs*
