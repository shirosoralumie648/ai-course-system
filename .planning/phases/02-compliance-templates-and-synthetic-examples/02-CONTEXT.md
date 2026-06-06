# Phase 2: Compliance, Templates, And Synthetic Examples - Context

**Gathered:** 2026-06-06
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 2 creates the reusable Course C foundation that later week and lab pages
will reference: template pages, synthetic example artifacts, the four-gate
compliance model, and the professional-source rules. It does not create the 16
weekly chapters, lab pages, final reference catalog update, or live enterprise
system integrations. Those belong to later phases.

</domain>

<decisions>
## Implementation Decisions

### Template Structure

- **D-01:** Create `docs/course-c/templates/` with a template overview page plus
  six separate template pages:
  `role-ai-assistant-pack.md`, `workflow-sop.md`, `prompt-library.md`,
  `compliance-checklist.md`, `audit-log.md`, and `roi-report.md`.
- **D-02:** Each template page should use the same content shape: purpose,
  suitable use cases, required fields, a copyable Markdown template, a short
  synthetic filled example, and a usage/submission checklist.
- **D-03:** Keep template pages practical and reusable, not long conceptual
  lectures. Deeper teaching belongs in later week pages.
- **D-04:** Add the template overview and six template pages to the Course C
  sidebar under a `模板与样例` group once the files exist. Do not add sidebar
  links for files that are not created in the phase.

### Synthetic Example Pack

- **D-05:** Create `docs/course-c/examples/` with small but realistic synthetic
  artifacts for a single virtual company. The examples should be field-complete
  enough for later weeks to reuse, but intentionally small enough to avoid a
  separate sample-data project.
- **D-06:** Include at least these example artifacts: virtual company profile,
  synthetic CRM data, synthetic finance data, synthetic HR data, and a synthetic
  contract/dispute example.
- **D-07:** Synthetic examples must not include real personal, customer,
  employee, financial, tax, legal, credential, or production-system data.
  Names, companies, emails, account numbers, contract text, and amounts must be
  clearly fictional or sample-only.
- **D-08:** Prefer Markdown and small CSV files over complex generated assets.
  If CSV files are added, include a short Markdown guide so students know how
  each dataset should be used in later Course C weeks.

### Four-Gate Compliance Model

- **D-09:** The Phase 2 compliance checklist should operationalize four gates:
  data gate, source gate, human gate, and audit gate.
- **D-10:** The checklist should include risk level, data sensitivity,
  source type, human approver role, approval timing, audit evidence, and release
  boundary fields. This makes the model reusable for investment, finance, tax,
  HR, legal, admin, and enterprise-system weeks.
- **D-11:** The model should frame AI as draft, analysis, organization,
  comparison, review, and workflow support. It must not frame AI as final legal,
  tax, investment, HR, accounting, compliance, or management decision authority.
- **D-12:** High-risk scenarios should be supported by template fields now, but
  their detailed scenario-specific prohibitions are deferred to Phase 4 and
  Phase 5 week/lab pages.

### Authoritative Domain Sources

- **D-13:** Phase 2 should add a professional-source matrix that separates
  implementation sources from authoritative domain sources across market
  research, product, brand, sales, data analysis, investment, investment banking,
  finance, tax, HR, legal, administration, governance, and enterprise systems.
- **D-14:** The source matrix should specify acceptable source categories:
  recognized books or textbooks, peer-reviewed papers or reviews, official laws
  and regulations, official standards, regulator guidance, public filings, and
  recognized industry-body materials.
- **D-15:** The source matrix should also include a copyable citation/use
  template with fields for source, scope, supported judgment, limitation, and
  evidence used in the AI workflow.
- **D-16:** Phase 2 should not try to finish detailed weekly bibliographies.
  It should create the matrix and citation rules so Phase 3, 4, and 5 can fill
  week-specific books, papers, regulations, standards, and official guidance.

### the agent's Discretion

- The exact wording of template headings and checklist labels is flexible as
  long as the six-template structure and required fields are preserved.
- The exact synthetic company name, fictional customer names, and sample values
  are up to the implementation agent, provided they are clearly synthetic and
  pedagogically useful.
- The source matrix can live in `reference-integration.md`, a dedicated
  template/source page, or both, as long as Course C pages have a stable route
  to cite and the sidebar exposes created pages only.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Planning

- `.planning/PROJECT.md` — Course C value, constraints, high-risk boundaries,
  and authoritative-domain-source requirement.
- `.planning/REQUIREMENTS.md` — Phase 2 requirements `TEMP-01` through
  `TEMP-04`, `RISK-01`, `REF-01`, `REF-04`, and `REF-05`.
- `.planning/ROADMAP.md` — Phase 2 goal, success criteria, phase boundaries, and
  dependency on Phase 1.
- `.planning/STATE.md` — Current workflow state and next action.
- `.planning/phases/01-course-c-site-skeleton/01-CONTEXT.md` — Prior decisions
  about Course C positioning, navigation, page style, source rules, and avoiding
  404 links.
- `docs/superpowers/specs/2026-06-05-course-c-business-ai-operations-design.md`
  — Approved Course C design spec, role assistant pack shape, compliance
  boundary, high-risk scenario rules, and initial file-level scope.

### Existing Course C Pages

- `docs/course-c/index.md` — Current Course C positioning, four-gate overview,
  weekly route, and final outcome framing.
- `docs/course-c/reference-integration.md` — Existing implementation-source vs
  authoritative-domain-source distinction and the source-use workflow to extend.
- `docs/course-c/final-project.md` — Assistant pack and transformation report
  requirements that templates should support.
- `docs/course-c/rubric.md` — Scoring weights and evidence expectations that
  templates should reinforce.

### Existing Site Patterns

- `docs/.vitepress/config.mjs` — Course C sidebar and VitePress route
  conventions. Add links only for files created in Phase 2.
- `docs/course-b/templates/AGENTS.md` — Existing template-page style for
  reusable agent instructions.
- `docs/course-b/templates/SKILL.md` — Existing long-form template style for
  copyable skill artifacts.
- `docs/course-b/templates/CLAUDE.md` — Existing reusable project-memory
  template style.

### External Source-Gate Baselines

- `https://www.nist.gov/itl/ai-risk-management-framework` — AI risk management
  framing: govern, map, measure, and manage.
- `https://www.iso.org/standard/81230.html` — ISO/IEC 42001 AI management system
  baseline for policies, objectives, and organizational process control.
- `https://www.oecd.org/en/topics/ai-principles.html` — OECD AI principles:
  transparency, accountability, human oversight, privacy, and safety.
- `https://vitepress.dev/guide/routing` — VitePress file-based routing behavior.
- `https://vitepress.dev/reference/default-theme-sidebar` — VitePress sidebar
  structure and route exposure.
- `https://diataxis.fr/reference/` — Documentation separation between reference
  material and task-oriented how-to content.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets

- `docs/.vitepress/config.mjs`: Course C currently has a five-link sidebar.
  Phase 2 should add a `模板与样例` group after creating the referenced files.
- `docs/course-c/reference-integration.md`: already separates implementation
  sources from authoritative domain sources; Phase 2 should extend rather than
  replace this page.
- `docs/course-b/templates/*.md`: useful precedent for reusable Markdown
  templates, but Course C templates should be business-workflow and compliance
  oriented rather than coding-project oriented.

### Established Patterns

- Public course pages are self-contained Markdown under `docs/`; they cannot
  depend on ignored `reference/repos/` content.
- Sidebar entries should only point at files that exist to avoid 404s.
- This repo has had Markdown/Vue parse failures around complex multiline
  component props. Phase 2 should stay mostly Markdown tables, fenced code, and
  simple links.
- GitHub Pages uses the `/ai-course-system/` base path. Final verification after
  implementation should use `cd docs && BASE=/ai-course-system/ npm run build`.

### Integration Points

- New template subtree: `docs/course-c/templates/`.
- New synthetic examples subtree: `docs/course-c/examples/`.
- Course C sidebar update: `docs/.vitepress/config.mjs`.
- Source-rule extension point: `docs/course-c/reference-integration.md`.

</code_context>

<specifics>
## Specific Ideas

- Template overview route: `/course-c/templates/`.
- Recommended sidebar group title: `模板与样例`.
- Recommended template page format:

```markdown
## 用途
## 适用场景
## 必填字段
## 可复制模板
## 示例片段
## 使用检查
```

- Recommended synthetic examples:
  - `examples/virtual-company-profile.md`
  - `examples/sample-crm.csv`
  - `examples/sample-finance.csv`
  - `examples/sample-hr.csv`
  - `examples/sample-contract-dispute.md`
  - optional `examples/README.md` if needed to explain how the sample set fits
    the course.

</specifics>

<deferred>
## Deferred Ideas

- Full Week 01-16 pages and Lab 01-16 pages remain Phase 3, Phase 4, and Phase 5
  scope.
- Scenario-specific detailed bibliographies for each professional week are
  deferred to the relevant week phases. Phase 2 only creates the source matrix
  and citation/use template.
- Live CRM, ERP, finance, tax, OA, legal, or HR system connections are out of
  scope for Phase 2 and remain controlled later-phase material.

</deferred>

---

*Phase: 02-compliance-templates-and-synthetic-examples*
*Context gathered: 2026-06-06*
