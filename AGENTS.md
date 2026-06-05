## Ruflo Integration

When working on multi-file tasks or complex features, use ToolSearch to find and
invoke Ruflo MCP tools.

Key tools: `memory_store`, `memory_search`, `hooks_route`, `swarm_init`,
`agent_spawn`.

Check system-reminder tags for `[INTELLIGENCE]` pattern suggestions before
starting work.

<!-- GSD:project-start source:PROJECT.md -->
## Project

**Course C Business AI Operations**

Course C is a 16-week business and management course inside the AI Course System
VitePress site. It teaches enterprise staff, managers, and founders to use
Codex, Claude Code, office tools, business SaaS, prompts, Skills, SOPs, API/MCP
concepts, and controlled system connections as role-based business assistants.

The course is a virtual-company operating simulation, not a disconnected prompt
library and not a coding course. Learners produce a reusable role AI assistant
pack and transform one real or realistic business workflow with before/after
evidence.

**Core Value:** Course C must show non-engineering business roles how to use AI agents safely and
repeatably for real enterprise workflows, with useful outputs and explicit human
approval gates.

### Constraints

- **Tech stack**: Use the existing VitePress 2 + Vue 3 + Element Plus docs site
  under `docs/`; do not introduce a new app framework.
- **Deployment**: Preserve GitHub Pages subpath behavior with
  `BASE=/ai-course-system/`.
- **Content structure**: Match Course A/B conventions: course index, teaching
  calendar, week pages, labs, final project, rubric, and reference integration.
- **Safety**: High-risk business areas require disclaimer, redaction, approval,
  source tracking, and audit artifacts.
- **Reference material**: Course pages cannot depend on untracked
  `reference/repos/` content being available online.
- **Scope**: First implementation pass should be complete and navigable but does
  not need every week to be a long chapter.
- **Repository hygiene**: Keep planning and course changes scoped; do not restore
  removed legacy material or commit build outputs.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->
## Technology Stack

## Current Stack
| Layer | Current choice | Notes |
| --- | --- | --- |
| Site generator | VitePress | Markdown pages under `docs/` |
| UI runtime | Vue 3 | Existing VitePress theme/components only |
| Component library | Element Plus | Already installed; avoid adding new dependencies for Course C v1 |
| Package manager | npm | `docs/package-lock.json` is committed |
| Deployment | GitHub Pages Actions | Builds `docs/.vitepress/dist` |
| Base path | `/ai-course-system/` | Required for repository Pages deployment |
- `vitepress`: `^2.0.0-alpha.16`
- `vue`: `^3.5.0`
- `element-plus`: `^2.13.1`
## Files To Use
- `docs/course-c/`: Course C source subtree.
- `docs/.vitepress/config.mjs`: nav and sidebar.
- `docs/index.md`: homepage action/card.
- `docs/shared/index.md`: optional shared resource links.
- `reference/catalog/course-integration-map.md`: Course C reference mapping.
- `.github/workflows/deploy-pages.yml`: deployment behavior to preserve.
## Commands

```bash
cd docs
npm ci
BASE=/ai-course-system/ npm run build
npm run dev -- --host 0.0.0.0
```

## What Not To Use
- Do not add a backend, database, auth layer, CRM/ERP integration, or live API
  write path for Course C v1.
- Do not clone new large `reference/repos/` dependencies.
- Do not commit generated `docs/.vitepress/dist`.
- Do not move the site root out of `docs/`.
- Do not treat Course C as a web-app feature; it is static curriculum content,
  examples, templates, and VitePress navigation.
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
