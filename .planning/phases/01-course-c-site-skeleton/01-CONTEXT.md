# Phase 1: Course C Site Skeleton - Context

**Gathered:** 2026-06-05
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 1 creates the public Course C entry points and stable route structure. It
adds the five Course C shell pages, exposes Course C in navigation/homepage, and
makes the course positioning clear. It does not create Week/Lab pages, templates,
sample data, or deep professional-source catalogs; those belong to later phases.

</domain>

<decisions>
## Implementation Decisions

### Homepage Positioning

- **D-01:** Course C homepage first screen uses **Enterprise AI operating
  system** as the primary positioning.
- **D-02:** The first screen addresses enterprise staff and managers first.
  Business/management students are a secondary audience.
- **D-03:** The outcome promise combines two concrete deliverables: a role AI
  assistant pack and a real workflow transformation report. These are framed as
  the smallest visible shape of an enterprise AI operating system.
- **D-04:** The homepage storyline is **from role tasks to enterprise AI
  operating system**. The virtual company story can appear after the first
  screen or in the course structure section.

### Navigation And Homepage Exposure

- **D-05:** Course A, Course B, and Course C should be parallel top-level nav
  items. Keep the pattern extensible for future Course D: research.
- **D-06:** Do not add a Course C button to the homepage hero actions in Phase 1.
  Keep hero actions from becoming crowded; expose Course C in the course card
  area instead.
- **D-07:** Homepage course cards use a four-card layout: Course A, Course B,
  Course C, and Shared Resources. This can later expand for Course D.
- **D-08:** Course C sidebar mirrors Course B's structure but only links existing
  Phase 1 shell pages to avoid 404s: course introduction, teaching calendar,
  reference integration, final project, and rubric.

### First-Pass Depth For Five Shell Pages

- **D-09:** All five shell pages must be complete usable first-pass pages, not
  placeholders.
- **D-10:** `teaching-calendar.md` uses a 16-week overview table plus one
  concrete weekly task per week. It should not become 16 long week chapters.
- **D-11:** `reference-integration.md` defines rules and source categories,
  especially implementation sources versus domain sources. Detailed
  book/paper/regulation lists are deferred to later phases.
- **D-12:** `final-project.md` describes required student deliverables.
  `rubric.md` defines scoring evidence and weights.

### Page Presentation Style

- **D-13:** Use a component-forward expression similar to Course A/B. Reuse
  existing components where useful, and add new components if they serve Phase 1.
- **D-14:** New components may be added as needed, but they must serve Phase 1
  and must not turn into unrelated visual-system refactoring.
- **D-15:** Course C homepage tone should feel like a course portal consistent
  with Course A/B, not a SaaS dashboard and not a strongly narrative virtual
  company page.
- **D-16:** `index.md` should be the strongest visual page. The other shell pages
  should stay clear and practical, using tables, sections, and limited
  components.

### the agent's Discretion

- Exact homepage wording, card copy, and component composition are up to the
  implementation agent as long as they follow the locked positioning.
- Exact component names are flexible. Any new component must be small,
  course-facing, stable under VitePress build, and useful for Phase 1.
- Exact table layouts for the calendar, final project, and rubric are flexible.

</decisions>

<specifics>
## Specific Ideas

- Suggested first-screen title: `课程 C：企业 AI 运营系统`.
- Suggested supporting sentence: `让 Codex / Claude Code 不只写代码，而是参与报告、仪表盘、客户材料、投资分析、合同草拟、财务、人力、法务与日常运营。`
- Suggested outcome line: `最终交付：一个岗位 AI 助理包 + 一份真实工作流改造报告。`
- Suggested sidebar first pass:

```text
课程 C：企业 AI 运营系统
- 课程介绍
- 教学日历
- Reference 融入方案
- 期末项目
- 评分标准
```

</specifics>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Planning

- `.planning/PROJECT.md` — Course C project context, core value, constraints,
  and key decisions.
- `.planning/REQUIREMENTS.md` — Phase 1 requirements `SHELL-01` through
  `SHELL-04` and cross-phase source-gate requirements.
- `.planning/ROADMAP.md` — Phase 1 goal, success criteria, and boundaries.
- `.planning/STATE.md` — Current focus and next action.
- `docs/superpowers/specs/2026-06-05-course-c-business-ai-operations-design.md`
  — Original approved Course C design spec.

### Existing Site Patterns

- `docs/.vitepress/config.mjs` — Current nav/sidebar structure and route
  conventions.
- `docs/index.md` — Current homepage hero actions and `AnimatedFeatureCards`
  pattern.
- `docs/course-a/index.md` — Course A landing page style and course-positioning
  pattern.
- `docs/course-b/index.md` — Course B landing page style and course-card route
  pattern.
- `docs/course-b/teaching-calendar.md` — Existing detailed calendar style to
  simplify for Course C Phase 1.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets

- `docs/.vitepress/config.mjs`: add Course C as a top-level nav entry and create
  a `'/course-c/'` sidebar section.
- `docs/index.md`: update frontmatter `features` and the `AnimatedFeatureCards`
  array to include Course C while keeping hero actions compact.
- Existing landing pages use `ChapterIntroduction`, `StepBar`,
  `WorkflowDiagram`, and `SummaryCard`; these are acceptable to reuse if their
  prop usage stays simple.

### Established Patterns

- Course A and Course B both use 16-week positioning and link from course index
  to teaching calendar, reference integration, final project, and rubric.
- Current homepage uses A/B/shared cards. Phase 1 should extend this instead of
  replacing the homepage information architecture.
- Current sidebar only links pages that exist. Follow that pattern to avoid 404s.

### Integration Points

- New route subtree: `docs/course-c/`.
- Navigation and sidebar: `docs/.vitepress/config.mjs`.
- Homepage exposure: `docs/index.md`.

### Build Risk

- This repo has a history of Markdown/Vue parse failures around complex
  component props. New components are allowed, but Phase 1 should avoid complex
  multiline prop values in Markdown. Verify with:

```bash
cd docs
BASE=/ai-course-system/ npm run build
```

</code_context>

<deferred>
## Deferred Ideas

- Future Course D: research should use the same scalable navigation and homepage
  pattern.
- Full Week/Lab sidebar entries are deferred until those pages exist in later
  phases.
- Detailed authoritative domain books, papers, regulations, and industry
  guidance lists are deferred to later phases; Phase 1 only defines the source
  categories and usage rule.

</deferred>

---

*Phase: 01-course-c-site-skeleton*
*Context gathered: 2026-06-05*
