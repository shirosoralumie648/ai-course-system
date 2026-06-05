# Phase 1 Research: Course C Site Skeleton

**Phase:** 01 - Course C Site Skeleton
**Date:** 2026-06-05
**Status:** Complete

## Research Question

What does the planner need to know to create an executable plan for the Course C
public site skeleton without drifting into later course-content phases?

## Phase Boundary

Phase 1 is a static VitePress course-shell phase. It creates the public Course C
entry routes, exposes those routes in navigation and homepage surfaces, and
turns the approved Course C positioning into five usable first-pass pages.

In scope:

- Create `docs/course-c/index.md`.
- Create `docs/course-c/teaching-calendar.md`.
- Create `docs/course-c/reference-integration.md`.
- Create `docs/course-c/final-project.md`.
- Create `docs/course-c/rubric.md`.
- Modify `docs/.vitepress/config.mjs` to add top navigation and a Course C
  sidebar that only links existing Phase 1 pages.
- Modify `docs/index.md` to include Course C in the course-card area while
  keeping homepage hero actions unchanged.

Out of scope:

- Week pages, lab pages, templates, examples, sample data, and detailed
  professional source catalogs.
- New backend, database, auth, live API, CRM, ERP, finance, tax, OA, or MCP
  integrations.
- Large visual-system refactors or new dependencies.
- Build output, dependencies, local archives, or ignored `reference/repos/`
  content.

## Existing Site Patterns

### VitePress Configuration

`docs/.vitepress/config.mjs` is the routing source of truth for public nav and
sidebars. Current top-level nav is:

- `首页` -> `/`
- `课程 A` -> `/course-a/`
- `课程 B` -> `/course-b/`
- `共享资源` -> `/shared/`

Course C should become a parallel top-level item:

- `课程 C` -> `/course-c/`

The sidebar convention links only existing pages. Course C should start with:

- `课程介绍` -> `/course-c/`
- `教学日历` -> `/course-c/teaching-calendar`
- `Reference 融入方案` -> `/course-c/reference-integration`
- `期末项目` -> `/course-c/final-project`
- `评分标准` -> `/course-c/rubric`

Do not add Week/Lab sidebar entries in Phase 1 because those pages do not exist
yet and would create 404s.

### Homepage

`docs/index.md` currently has VitePress home frontmatter with three hero actions:
Course A, Course B, and shared resources. The locked Phase 1 decision says not
to add Course C to hero actions. Course C should be exposed in:

- The frontmatter `features` list.
- The `AnimatedFeatureCards` cards array.

The card layout becomes four cards: Course A, Course B, Course C, and shared
resources. This preserves the future Course D extension path.

### Course Landing Pages

`docs/course-a/index.md` and `docs/course-b/index.md` use a course-portal style:

- H1 title and a short blockquote.
- `ChapterIntroduction` with duration, output, and tags.
- Audience/requirements section.
- "学完能做什么" outcomes.
- 16-week route table.
- Reference integration section.
- Optional visual components such as `StepBar`, `WorkflowDiagram`, and
  `SummaryCard`.

Course C should reuse this course-portal pattern, but its copy must distinguish
it from:

- Course A: prototype literacy for non-CS learners.
- Course B: AI full-stack software product engineering.

Course C positioning must be business operations and role-agent workflow
training. Recommended first-screen language from context:

- Title: `课程 C：企业 AI 运营系统`
- Outcome: `岗位 AI 助理包 + 真实工作流改造报告`
- Audience: enterprise staff and managers first, business/management students
  second.

### Teaching Calendar

`docs/course-b/teaching-calendar.md` is a long per-week page. For Phase 1,
Course C should not create 16 long chapters inside the calendar. The plan should
ask for one 16-week overview table plus one concrete weekly task per week,
matching decision D-10.

## Content Requirements For Five Pages

### `index.md`

The landing page must satisfy `SHELL-01` and `SHELL-03`:

- Explain positioning, audience, outcomes, and 16-week route.
- State that Course C is a business operations and role-agent workflow course.
- State that Course C is not Course A prototype literacy and not Course B
  software engineering.
- Show the final deliverables: role AI assistant pack and workflow
  transformation report.
- Mention safe AI usage, human approval, and audit evidence without turning the
  page into a legal/compliance manual.

### `teaching-calendar.md`

The calendar must satisfy `SHELL-04` and support `SHELL-01`:

- Include all 16 weeks from the approved design spec.
- For every week, include topic, role scenario, core output, and one concrete
  weekly task.
- Avoid links to nonexistent week/lab pages in Phase 1, unless phrased as future
  pages without clickable route links.

### `reference-integration.md`

The reference page must satisfy the Phase 1 part of the source-gate decision:

- Define the difference between implementation sources and domain sources.
- Require professional business pages to use authoritative domain sources
  where relevant.
- Establish source categories: recognized books/textbooks, peer-reviewed
  papers, official laws/regulations/standards, regulator guidance, and industry
  body materials.
- Explain that detailed per-week books, papers, regulations, and standards are
  deferred to later phases.
- Keep public pages self-contained; do not require local ignored
  `reference/repos/`.

### `final-project.md`

The final project page should describe required student deliverables:

- Role AI assistant pack.
- Workflow transformation report.
- Before-state, after-state, reusable assets, compliance packet, and impact
  proof.
- Human approval and audit expectations for high-risk scenarios.

### `rubric.md`

The rubric should use the approved weights:

- Business framing: 15%.
- Assistant-pack completeness: 25%.
- Weekly outputs: 20%.
- Compliance/risk: 20%.
- Workflow transformation: 20%.

Acceptance language should focus on evidence, reuse, safety, and transformation
quality rather than prompt-library volume.

## Build And Markdown Risk

This repo has a known failure mode: Markdown pages that pass complex multiline
strings into Vue component props can break VitePress/Vue parsing. The safest
Phase 1 plan is:

- Prefer Markdown sections and tables for the shell pages.
- Reuse existing components only with simple props.
- Avoid complex multiline `diff`, `messages`, or deeply nested prop values.
- Do not introduce a new dependency for a course shell.

Verification command:

```bash
cd docs
BASE=/ai-course-system/ npm run build
```

Relevant local memory and prior repo notes confirm that `docs/` is the actual
site root and that GitHub Pages requires the `/ai-course-system/` base path.

## UI And Interaction Considerations

Phase 1 changes user-facing pages and navigation, so a lightweight UI design
contract is useful even though this is not a new frontend app.

The plan should require:

- Course C landing page remains a course portal, not a SaaS dashboard.
- `index.md` is the strongest visual page.
- Other shell pages stay practical, with clear tables and sections.
- Cards should not become nested cards.
- Text should remain scannable on mobile and desktop.
- Homepage hero actions should remain unchanged.
- Course C card should use a distinct palette from A/B/shared while avoiding a
  one-note purple/blue theme.

## Security And Compliance Considerations

Phase 1 is static curriculum content, so there are no database, auth, API, or
secret-handling threats. The relevant risks are content-safety and navigation
risks:

- Do not imply AI can make final legal, tax, investment, HR, accounting, or
  management decisions.
- Do not include real customer, employee, finance, tax, legal, credential, or
  production-system data.
- Do not link to nonexistent Course C week/lab/template pages in Phase 1.
- Do not require private local reference repositories for published pages.
- Keep high-risk areas framed as draft, analysis, organization, review, and
  workflow support with human approval.

## Suggested Plan Shape

A single execution plan is sufficient because the deliverable is one coherent
site skeleton with tightly coupled nav and page content. The plan should contain
serial tasks:

1. Create the `docs/course-c/` shell pages with first-pass content.
2. Update VitePress top nav/sidebar and homepage Course C exposure.
3. Run build and route/link checks.

The plan must list all Phase 1 requirement IDs in frontmatter:

- `SHELL-01`
- `SHELL-02`
- `SHELL-03`
- `SHELL-04`

## Verification Strategy

Minimum verification for execution:

- `test -f` confirms all five Course C shell pages exist.
- `rg` confirms `docs/.vitepress/config.mjs` contains `/course-c/`,
  `/course-c/teaching-calendar`, `/course-c/reference-integration`,
  `/course-c/final-project`, and `/course-c/rubric`.
- `rg` confirms `docs/index.md` contains a Course C feature/card but the hero
  actions remain limited to Course A, Course B, and shared resources.
- `BASE=/ai-course-system/ npm run build` succeeds from `docs/`.
- `find docs/course-c` confirms no Week/Lab pages were created in Phase 1.

## Research Complete

Phase 1 can be planned as a narrow VitePress content/navigation slice. The main
planner risk is not technical complexity; it is scope creep into week/lab
content or shallow treatment of the professional source gate. Keep the plan
focused on shell pages, nav/homepage exposure, and explicit reference rules.
