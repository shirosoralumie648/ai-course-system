---
phase: 01
slug: course-c-site-skeleton
status: approved
shadcn_initialized: false
preset: existing-vitepress-course-portal
created: 2026-06-05
---

# Phase 01 - UI Design Contract

> Visual and interaction contract for the Course C public site skeleton.

## Design System

| Property | Value |
|----------|-------|
| Tool | none |
| Preset | existing VitePress course portal |
| Component library | existing VitePress theme components + Element Plus already in project |
| Icon library | none for Phase 1; emoji icons are acceptable only where existing homepage features/cards already use them |
| Font | inherit VitePress default |

No new UI dependency is allowed for Phase 1. Reuse the current VitePress theme
and existing custom components under `docs/.vitepress/theme/components/`.

## Page Experience Contract

| Surface | Contract |
| --- | --- |
| `docs/course-c/index.md` | Strongest Course C visual page. It should read as a course portal for `企业 AI 运营系统`, not a SaaS dashboard, marketing landing page, or virtual-company story page. |
| `docs/course-c/teaching-calendar.md` | Practical schedule page. Use tables and short weekly task descriptions; do not create long week chapters inside this page. |
| `docs/course-c/reference-integration.md` | Practical rules page. Make implementation sources and authoritative domain sources visibly distinct. |
| `docs/course-c/final-project.md` | Deliverable contract page. Emphasize required evidence and human approval. |
| `docs/course-c/rubric.md` | Scoring page. Use weighted tables and evidence language. |
| `docs/index.md` | Add Course C in homepage cards/features only. Do not add a Course C hero action in Phase 1. |
| `docs/.vitepress/config.mjs` | Add Course C as a top-level nav item and a sidebar containing only existing Phase 1 shell pages. |

## Spacing Scale

Use existing VitePress and component spacing. New inline HTML/CSS should be
minimal and should use multiples of 4px.

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Inline icon/text gaps only |
| sm | 8px | Compact table/caption spacing |
| md | 16px | Default paragraph/list spacing |
| lg | 24px | Section intro spacing |
| xl | 32px | Major content block gaps |
| 2xl | 48px | Top-level page section breaks |
| 3xl | 64px | Only for course landing-page visual rhythm |

Exceptions: VitePress default theme spacing is allowed.

## Typography

Use VitePress defaults. Do not set viewport-based font sizing.

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Body | inherit VitePress | regular | inherit VitePress |
| Label | inherit VitePress small text | medium where needed | inherit VitePress |
| Heading | inherit VitePress h2/h3 | semibold/bold | inherit VitePress |
| Display | inherit VitePress h1 | bold | inherit VitePress |

Course C landing copy must keep the H1 literal and clear: `课程 C：企业 AI 运营系统`.

## Color

Use existing theme variables and the homepage card pattern. Course C may use a
distinct accent, but the page must not become a one-note purple/blue gradient
theme.

| Role | Value | Usage |
|------|-------|-------|
| Dominant (60%) | VitePress default background | Page background and text surfaces |
| Secondary (30%) | VitePress default surface/border colors | Tables, blockquotes, standard docs sections |
| Accent (10%) | Course C card accent distinct from Course A/B/shared | Homepage feature/card and limited landing-page emphasis |
| Destructive | not applicable | No destructive action in static course shell |

Accent reserved for: Course C homepage card, tags, and limited course-landing
emphasis. Do not restyle the whole site.

## Copywriting Contract

| Element | Copy |
|---------|------|
| Course C title | `课程 C：企业 AI 运营系统` |
| Primary outcome | `岗位 AI 助理包 + 真实工作流改造报告` |
| Audience | Enterprise staff and managers first; business/management students second |
| Differentiation | Course C is business operations and role-agent workflow training, not Course A prototype literacy or Course B software engineering |
| Safety boundary | AI supports draft, analysis, organization, review, and workflow execution evidence; humans approve high-risk decisions |
| Source rule | Professional business pages need authoritative domain sources as well as implementation/tool sources |

No empty state, error state, or destructive confirmation copy is needed for
Phase 1 static content.

## Navigation Contract

Top nav target:

- Keep `首页`, `课程 A`, `课程 B`, and `共享资源`.
- Add `课程 C` as a parallel nav item linking to `/course-c/`.
- Keep this structure extensible for future Course D.

Course C sidebar target:

- `课程介绍` -> `/course-c/`
- `教学日历` -> `/course-c/teaching-calendar`
- `Reference 融入方案` -> `/course-c/reference-integration`
- `期末项目` -> `/course-c/final-project`
- `评分标准` -> `/course-c/rubric`

Do not add week, lab, template, or example links until those pages exist.

## Component Safety

Allowed:

- `ChapterIntroduction` with simple string props and short tag arrays.
- `StepBar` with short items if useful on the Course C landing page.
- `WorkflowDiagram` only if the prop values remain short and simple.
- `SummaryCard` only if values remain concise.
- `AnimatedFeatureCards` only in the existing homepage usage.

Avoid:

- `DiffViewer` in Phase 1.
- `AiChat` in Phase 1.
- Complex multiline Vue props inside Markdown.
- Nested cards or section-as-card page layouts.
- New components unless implementation proves an existing component cannot serve
  the Phase 1 shell.

## Accessibility And Responsive Constraints

- Keep link text descriptive: `查看课程 C`, `教学日历`, `期末项目`, etc.
- Tables should have short column labels and avoid very long unbroken text.
- Do not add fixed-width content that overflows mobile viewports.
- Do not add in-app instructional text about keyboard shortcuts or visual
  styling.
- Do not put cards inside other cards.

## Registry Safety

| Registry | Blocks Used | Safety Gate |
|----------|-------------|-------------|
| shadcn official | none | not required |
| third-party UI registries | none | not allowed in Phase 1 |

## Checker Sign-Off

- [x] Dimension 1 Copywriting: PASS
- [x] Dimension 2 Visuals: PASS
- [x] Dimension 3 Color: PASS
- [x] Dimension 4 Typography: PASS
- [x] Dimension 5 Spacing: PASS
- [x] Dimension 6 Registry Safety: PASS

**Approval:** approved 2026-06-05
