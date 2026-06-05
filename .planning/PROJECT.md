# Course C Business AI Operations

## What This Is

Course C is a 16-week business and management course inside the AI Course System
VitePress site. It teaches enterprise staff, managers, and founders to use
Codex, Claude Code, office tools, business SaaS, prompts, Skills, SOPs, API/MCP
concepts, and controlled system connections as role-based business assistants.

The course is a virtual-company operating simulation, not a disconnected prompt
library and not a coding course. Learners produce a reusable role AI assistant
pack and transform one real or realistic business workflow with before/after
evidence.

## Core Value

Course C must show non-engineering business roles how to use AI agents safely and
repeatably for real enterprise workflows, with useful outputs and explicit human
approval gates.

## Requirements

### Validated

- ✓ Existing VitePress course website publishes from `docs/` — existing
- ✓ Course A is a 16-week non-CS AI product prototype course — existing
- ✓ Course B is a 16-week AI full-stack product engineering course — existing
- ✓ Shared resources and reference catalog pages exist for cross-course tools
  and reading routes — existing
- ✓ GitHub Pages deployment uses `BASE=/ai-course-system/` and publishes
  `docs/.vitepress/dist` through Actions — existing

### Active

- [ ] Add Course C as a complete navigable 16-week course under `docs/course-c/`.
- [ ] Keep Course C distinct from Course A and Course B: business workflows and
  documents belong to Course C; software product engineering belongs to Course B.
- [ ] Build Course C around one continuous virtual company operating story and
  one role/business scenario per week.
- [ ] Include week pages, lab pages, teaching calendar, final project, rubric,
  reference integration, templates, and examples needed for first-pass use.
- [ ] Provide a reusable role AI assistant pack structure with workflows,
  prompts, Skills, templates, data examples, tool notes, compliance artifacts,
  and before/after cases.
- [ ] Cover office delivery, business SaaS import/export, AI workflow assets,
  and controlled API/MCP enterprise-system planning.
- [ ] Put compliance boundaries into every high-risk scenario: data redaction,
  source tracking, human approval, audit trail, and disclaimer.
- [ ] Update VitePress nav/sidebar and homepage entry points so Course C is
  discoverable.
- [ ] Update `reference/catalog/course-integration-map.md` with Course C mapping
  without requiring local `reference/repos/` to exist on GitHub Pages.
- [ ] Require each professional business scenario to cite authoritative domain
  sources, not only code or tool documentation.
- [ ] Verify Markdown/VitePress build with `BASE=/ai-course-system/ npm run build`
  from `docs/`.

### Out of Scope

- Production-grade live CRM, ERP, OA, finance, tax, or legal-system writes —
  first pass must stay course-content and template oriented.
- Legal, tax, investment, HR, or accounting advice that claims professional
  authority — the course teaches draft, analysis, review, and approval workflows.
- New large cloned reference repositories — local `reference/repos/` remains
  teacher prep only and is ignored by git.
- Rewriting Course A or Course B beyond navigation/homepage links needed for
  Course C discoverability — Course C should not destabilize existing courses.
- Building runnable enterprise integrations before the course content spine is
  complete — API/MCP belongs to a controlled advanced layer first.

## Context

- Repository: `/media/shirosora/4A183E5C183E46EB/codestorage/ai-course-system`
- Published site: `https://shirosoralumie648.github.io/ai-course-system/`
- Site root: `docs/`
- VitePress config: `docs/.vitepress/config.mjs`
- Build command: `cd docs && BASE=/ai-course-system/ npm run build`
- Course C source spec:
  `docs/superpowers/specs/2026-06-05-course-c-business-ai-operations-design.md`
- Existing Course B redesign spec:
  `docs/superpowers/specs/2026-06-02-course-b-16-week-redesign.md`
- Local reference clones are intentionally ignored by `.gitignore` under
  `reference/repos/`; public course pages must be self-contained.

Course C topics from the approved spec:

- AI enterprise operating system overview
- Market research and industry analysis
- Product positioning and prototype expression
- Brand promotion and content assets
- Sales leads and channel development
- Customer relationship maintenance and sales execution
- Data analysis and management dashboards
- Public stock and investment analysis
- Investment banking and business planning
- Financial management and budget analysis
- Tax filing and compliance records
- Human resources management
- Legal contracts and dispute handling
- Administration and corporate governance
- Enterprise system connection and AI workflow
- Real workflow transformation defense

## Constraints

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
- **Domain research**: Professional business tasks must consult authoritative
  domain books, peer-reviewed papers, official standards/regulations, or
  recognized industry guidance in addition to implementation/code references.
- **Scope**: First implementation pass should be complete and navigable but does
  not need every week to be a long chapter.
- **Repository hygiene**: Keep planning and course changes scoped; do not restore
  removed legacy material or commit build outputs.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Course C is a business operations and role-agent course | User wants Codex/Claude Code beyond coding for reports, dashboards, customer materials, investment analysis, prototypes, contracts, legal/compliance, finance, HR, brand, sales, and admin workflows | -- Pending |
| Use one virtual company across 16 weeks | Prevents the course from becoming a scattered prompt library while keeping weekly role scenarios concrete | -- Pending |
| Required path focuses on office tools, SaaS import/export, and AI workflow assets | Keeps the course accessible to non-engineering business users | -- Pending |
| API/MCP and enterprise systems are advanced controlled layers | Allows realistic integration coverage without unsafe production writes | -- Pending |
| Every high-risk workflow uses data, source, human, and audit gates | Protects against overclaiming AI authority in investment, finance, tax, HR, legal, and compliance contexts | -- Pending |
| Course C pages must be self-contained on GitHub Pages | `reference/repos/` is local-only and ignored by git | -- Pending |
| Professional tasks require authoritative domain sources | Code docs explain implementation mechanics but cannot validate finance, legal, HR, tax, sales, product, or management content quality | -- Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `$gsd-transition`):
1. Requirements invalidated? Move to Out of Scope with reason.
2. Requirements validated? Move to Validated with phase reference.
3. New requirements emerged? Add to Active.
4. Decisions to log? Add to Key Decisions.
5. "What This Is" still accurate? Update if drifted.

**After each milestone** (via `$gsd-complete-milestone`):
1. Full review of all sections.
2. Core Value check: still the right priority?
3. Audit Out of Scope: reasons still valid?
4. Update Context with current state.

---
*Last updated: 2026-06-05 after initialization from Course C design spec*
