# Phase 2: Compliance, Templates, And Synthetic Examples - Patterns

**Mapped:** 2026-06-06
**Status:** Complete

## Reusable Assets

| Asset | Reuse In Phase 2 |
|---|---|
| `docs/.vitepress/config.mjs` | Add Course C `模板与样例` sidebar group after creating template/example pages. |
| `docs/course-c/reference-integration.md` | Extend existing implementation-vs-domain source rules with matrix and citation/use template. |
| `docs/course-c/final-project.md` | Align assistant-pack and transformation-report templates to final project evidence. |
| `docs/course-c/rubric.md` | Align checklist language to reuse, safety, evidence, and transformation quality. |
| `docs/course-b/templates/AGENTS.md` | Existing copyable template page precedent. |
| `docs/course-b/templates/SKILL.md` | Existing long-form template page precedent for fields and examples. |
| `docs/course-b/templates/CLAUDE.md` | Existing project-memory template precedent. |

## Established Patterns

- Course pages are static Markdown under `docs/`.
- Sidebar links omit the `.md` extension and should point only to existing
  files.
- Course B groups templates under a sidebar subsection. Course C should use the
  same subsection pattern, with business-operation template labels.
- Avoid complex Vue component prop blocks in newly-created Markdown; use H1/H2,
  tables, lists, and fenced code blocks.
- GitHub Pages verification uses `BASE=/ai-course-system/ npm run build` from
  the `docs/` directory.

## File Mapping

| New/Modified File | Closest Analog | Notes |
|---|---|---|
| `docs/course-c/templates/index.md` | `docs/course-b/templates/SKILL.md` | Overview plus links; keep shorter than Course B template pages. |
| `docs/course-c/templates/role-ai-assistant-pack.md` | `docs/course-c/final-project.md` | Must support final project assistant-pack structure. |
| `docs/course-c/templates/workflow-sop.md` | `docs/course-c/teaching-calendar.md` | Reuse weekly rhythm language: situation, role, inputs, workflow, compliance, update. |
| `docs/course-c/templates/prompt-library.md` | `docs/course-b/templates/SKILL.md` | Copyable artifact, but business-task prompt fields rather than coding-skill fields. |
| `docs/course-c/templates/compliance-checklist.md` | `docs/course-c/reference-integration.md` | Four gates become operational fields. |
| `docs/course-c/templates/audit-log.md` | `docs/course-c/final-project.md` | Supports evidence trail for inputs, AI outputs, edits, approvals, final version. |
| `docs/course-c/templates/roi-report.md` | `docs/course-c/rubric.md` | Supports workflow-transformation scoring evidence. |
| `docs/course-c/examples/*` | No direct Course C analog yet | Use small Markdown/CSV artifacts only. |
| `docs/.vitepress/config.mjs` | Existing Course C sidebar block | Add links only after files are created. |

## Integration Constraints

- Do not add Week/Lab links in Phase 2.
- Do not add `reference/repos/` requirements to public pages.
- Do not commit generated `docs/.vitepress/dist`, `docs/node_modules`, local
  archives, or reference clones.
- Use explicit fictional/sample labels in examples so later scans can verify
  `TEMP-04`.

---

*Phase: 02-compliance-templates-and-synthetic-examples*
