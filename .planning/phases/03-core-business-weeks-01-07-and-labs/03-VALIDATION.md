---
phase: 03
slug: core-business-weeks-01-07-and-labs
status: draft
nyquist_compliant: true
wave_0_complete: true
created: 2026-06-06
---

# Phase 03 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

## Test Infrastructure

| Property | Value |
|---|---|
| **Framework** | VitePress build plus shell/source assertions |
| **Config file** | `docs/package.json`, `docs/.vitepress/config.mjs` |
| **Quick run command** | `git diff --check && gsd-sdk query verify.plan-structure .planning/phases/03-core-business-weeks-01-07-and-labs/03-01-PLAN.md` |
| **Full suite command** | `cd docs && BASE=/ai-course-system/ npm run build` |
| **Estimated runtime** | ~20 seconds |

## Sampling Rate

- **After every task commit:** Run the task's `<verify>` command and `git diff --check`.
- **After every plan wave:** Run `BASE=/ai-course-system/ npm run build` from `docs/`.
- **Before closeout:** Run all plan artifact/link checks, decision coverage, and full build.
- **Max feedback latency:** 30 seconds.

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Secure Behavior | Test Type | Automated Command | Status |
|---|---|---|---|---|---|---|---|
| 03-01-01 | 01 | 1 | CURR-01, CURR-02, CURR-03 | Week 01-03 use sample/public inputs and source/compliance gates. | source/build | `test -f docs/course-c/week-01.md && test -f docs/course-c/week-02.md && test -f docs/course-c/week-03.md` | pending |
| 03-01-02 | 01 | 1 | LAB-01, LAB-02, LAB-03 | Lab 01-03 require evidence and assistant-pack updates. | source/build | `test -f docs/course-c/labs/lab-01.md && test -f docs/course-c/labs/lab-02.md && test -f docs/course-c/labs/lab-03.md` | pending |
| 03-02-01 | 02 | 2 | CURR-01, CURR-02, CURR-03 | Week 04-05 use brand/sales sources and review gates. | source/build | `test -f docs/course-c/week-04.md && test -f docs/course-c/week-05.md` | pending |
| 03-02-02 | 02 | 2 | LAB-01, LAB-02, LAB-03 | Lab 04-05 require concrete assets and review evidence. | source/build | `test -f docs/course-c/labs/lab-04.md && test -f docs/course-c/labs/lab-05.md` | pending |
| 03-03-01 | 03 | 3 | CURR-01, CURR-02, CURR-03 | Week 06-07 use CRM/dashboard sources and human review boundaries. | source/build | `test -f docs/course-c/week-06.md && test -f docs/course-c/week-07.md` | pending |
| 03-03-02 | 03 | 3 | LAB-01, LAB-02, LAB-03 | Lab 06-07 require CRM/dashboard artifacts and audit logs. | source/build | `test -f docs/course-c/labs/lab-06.md && test -f docs/course-c/labs/lab-07.md` | pending |
| 03-04-01 | 04 | 4 | CURR-01, LAB-01 | Sidebar links only created Week/Lab 01-07 pages. | source/build | `rg -n "/course-c/week-01|/course-c/labs/lab-01" docs/.vitepress/config.mjs && cd docs && BASE=/ai-course-system/ npm run build` | pending |

## Wave 0 Requirements

Existing infrastructure covers all phase requirements:

- `docs/package.json` contains the VitePress build command.
- `docs/.vitepress/config.mjs` controls nav/sidebar routing.
- Phase 2 templates/examples exist and are already build-verified.
- `gsd-sdk query verify.plan-structure` validates plan structure.

## Manual-Only Verifications

All Phase 3 acceptance criteria are source/build verifiable. Human review is
useful for teaching quality, but not required for completion proof.

## Validation Sign-Off

- [x] All tasks have automated verify commands
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all missing references
- [x] No watch-mode flags
- [x] Feedback latency < 30s
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** pending execution
