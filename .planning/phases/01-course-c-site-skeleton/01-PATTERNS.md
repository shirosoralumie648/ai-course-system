# Phase 1 Pattern Map: Course C Site Skeleton

**Phase:** 01 - Course C Site Skeleton
**Date:** 2026-06-05
**Status:** Complete

## Purpose

Map Phase 1 files to the closest existing repo analogs so the execution plan can
reuse local VitePress patterns instead of inventing a new site structure.

## Files To Create

| New file | Role | Closest analog | Pattern to reuse |
| --- | --- | --- | --- |
| `docs/course-c/index.md` | Course landing page | `docs/course-a/index.md`, `docs/course-b/index.md` | H1, blockquote, `ChapterIntroduction`, outcome sections, 16-week route table, reference section, optional simple components |
| `docs/course-c/teaching-calendar.md` | 16-week schedule overview | `docs/course-b/teaching-calendar.md` | Calendar framing and weekly evidence language, simplified into a 16-row table plus one concrete task per week |
| `docs/course-c/reference-integration.md` | Reference/source rules | `docs/course-a/reference-integration.md`, `docs/course-b/reference-integration.md` | Explain how references enter course work; adapt to Course C's implementation-vs-domain source distinction |
| `docs/course-c/final-project.md` | Capstone contract | `docs/course-a/final-project.md`, `docs/course-b/final-project.md` | Deliverables, evidence requirements, review expectations |
| `docs/course-c/rubric.md` | Scoring criteria | `docs/course-a/rubric.md`, `docs/course-b/rubric.md` | Weighted scoring table and evidence-based grading |

## Files To Modify

| Existing file | Role | Existing pattern | Phase 1 change |
| --- | --- | --- | --- |
| `docs/.vitepress/config.mjs` | Site nav/sidebar source of truth | `nav` array and course-specific `sidebar` sections | Add `{ text: '课程 C', link: '/course-c/' }`; add `'/course-c/'` sidebar with only five shell pages |
| `docs/index.md` | Public homepage | VitePress home frontmatter + `AnimatedFeatureCards` cards array | Add Course C to `features` and card array; do not add Course C to hero actions |

## Component Use Guidance

Existing safe components for Phase 1:

- `ChapterIntroduction`: used by Course A/B landing pages and week pages.
- `StepBar`: useful for course structure phases.
- `WorkflowDiagram`: useful for a simple role-to-operating-system flow if props
  stay short.
- `SummaryCard`: useful for outputs and assessment summary.
- `AnimatedFeatureCards`: already used on `docs/index.md`.

Avoid in Phase 1 unless there is a strong reason:

- `DiffViewer`: prior malformed multiline prop failures occurred around complex
  diff strings.
- `AiChat`: prior component-contract mismatches occurred around message props.
- New visual components: allowed by context, but not needed for a shell plan
  unless implementation finds a real gap.

## Navigation Pattern

Course C should mirror Course B's top-level shape but omit pages that do not
exist yet.

Target nav addition:

```js
{ text: '课程 C', link: '/course-c/' }
```

Target sidebar section:

```js
'/course-c/': [
  {
    text: '课程 C：企业 AI 运营系统',
    items: [
      { text: '课程介绍', link: '/course-c/' },
      { text: '教学日历', link: '/course-c/teaching-calendar' },
      { text: 'Reference 融入方案', link: '/course-c/reference-integration' },
      { text: '期末项目', link: '/course-c/final-project' },
      { text: '评分标准', link: '/course-c/rubric' }
    ]
  }
]
```

The implementation must preserve existing Course A, Course B, and shared
resource sidebars.

## Homepage Pattern

`docs/index.md` currently exposes course cards in two places:

- Frontmatter `features`.
- `AnimatedFeatureCards :cards`.

Phase 1 should update both places so Course C is visible in the static
VitePress home features and the custom animated card UI.

Hero action rule:

- Preserve Course A, Course B, and shared-resource hero actions.
- Do not add Course C to hero actions in Phase 1.

## Link Stability Pattern

Use route links without `.md`, matching existing VitePress usage:

- `/course-c/`
- `/course-c/teaching-calendar`
- `/course-c/reference-integration`
- `/course-c/final-project`
- `/course-c/rubric`

Do not link to:

- `/course-c/week-01`
- `/course-c/labs/lab-01`
- `/course-c/templates/...`

until those pages exist in later phases.

## Acceptance Check Patterns

Use source and build checks:

```bash
test -f docs/course-c/index.md
test -f docs/course-c/teaching-calendar.md
test -f docs/course-c/reference-integration.md
test -f docs/course-c/final-project.md
test -f docs/course-c/rubric.md
rg "/course-c/" docs/.vitepress/config.mjs docs/index.md
cd docs && BASE=/ai-course-system/ npm run build
```

## Pattern Mapping Complete
