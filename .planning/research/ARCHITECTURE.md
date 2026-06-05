# Architecture Research: Course C Business AI Operations

**Domain:** VitePress course content architecture
**Confidence:** High for repo structure, medium for eventual content depth

## Recommended Architecture

Course C should be a self-contained VitePress course subtree parallel to
`docs/course-a/` and `docs/course-b/`. Keep the architecture content-first:
Markdown owns the curriculum, existing Vue components provide light presentation,
and sample artifacts live inside Course C so GitHub Pages does not depend on
local `reference/repos/`.

## Main Components

| Component | Responsibility | Boundary |
| --- | --- | --- |
| `index.md` | Course positioning, audience, outcomes, 16-week route, relation to A/B | Entry only, not long syllabus |
| `teaching-calendar.md` | Week-by-week instructor schedule | Mirrors Course A/B calendar pattern |
| `week-01.md` ... `week-16.md` | Lessons following the virtual-company story | One role scenario, workflow, output, compliance gate |
| `labs/lab-01.md` ... `labs/lab-16.md` | Assignments and evidence | Shorter task/checklist pages |
| `templates/*.md` | Assistant-pack, SOP, prompt, compliance, audit, ROI templates | Student-facing reusable artifacts |
| `examples/*` | Virtual company profile and sample CSV/docs | Synthetic data safe for Pages |
| `reference-integration.md` | How reference material informs Course C | No dependency on cloned repos |
| `final-project.md` | Assistant pack + transformation requirements | Drives Week 16 and rubric |
| `rubric.md` | Grading model and evidence criteria | Emphasize compliance and audit evidence |

## File Tree Boundary

```text
docs/course-c/
├── index.md
├── teaching-calendar.md
├── reference-integration.md
├── final-project.md
├── rubric.md
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

Do not add new theme components in the first pass. Reuse existing components
only where they already behave safely. Avoid prop-heavy multiline component
examples, especially patterns similar to `DiffViewer`, because this repo has had
Markdown/Vue parse failures around complex component props.

## Navigation And Sidebar

| File | Change |
| --- | --- |
| `docs/.vitepress/config.mjs` | Add top nav `{ text: '课程 C', link: '/course-c/' }` |
| `docs/.vitepress/config.mjs` | Add sidebar key `'/course-c/'` with intro, calendar, reference, weeks, labs, templates, final project, rubric |
| `docs/index.md` | Add Course C action/card |
| `docs/shared/index.md` | Link Course C templates only if shared page changes are useful |
| `reference/catalog/course-integration-map.md` | Add Course C mapping |

## Content Flow

```text
Course C spec
  -> course-c/index.md + teaching-calendar.md
  -> weekly pages define role scenarios and outputs
  -> labs turn weekly outputs into student submissions
  -> templates/examples provide reusable pack assets
  -> final-project.md assembles pack + transformation evidence
  -> rubric.md grades evidence, safety, reuse, and impact
```

## Build Order

1. Course shell pages.
2. Navigation/sidebar/homepage links.
3. Templates and examples.
4. Week 01-16 pages.
5. Lab 01-16 pages.
6. Reference map update.
7. Build and link verification.

