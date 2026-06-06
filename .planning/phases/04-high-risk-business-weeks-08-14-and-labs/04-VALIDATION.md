---
phase: 04
slug: high-risk-business-weeks-08-14-and-labs
status: draft
nyquist_compliant: true
wave_0_complete: true
created: 2026-06-06
---

# Phase 04 — Validation Strategy

## Test Infrastructure

| Property | Value |
|---|---|
| Framework | VitePress build plus shell/source assertions |
| Quick run command | `git diff --check && gsd-sdk query verify.plan-structure .planning/phases/04-high-risk-business-weeks-08-14-and-labs/04-01-PLAN.md` |
| Full suite command | `cd docs && BASE=/ai-course-system/ npm run build` |
| Estimated runtime | ~20 seconds |

## Per-Task Verification Map

| Task ID | Plan | Requirement | Test Type | Automated Command |
|---|---|---|---|---|
| 04-01-01 | 01 | CURR-04, RISK-02, RISK-04 | source | `test -f docs/course-c/week-08.md && test -f docs/course-c/week-09.md` |
| 04-01-02 | 01 | RISK-03, LAB-02, LAB-03 | source | `test -f docs/course-c/labs/lab-08.md && test -f docs/course-c/labs/lab-09.md` |
| 04-02-01 | 02 | CURR-04, RISK-02, RISK-04 | source | `test -f docs/course-c/week-10.md && test -f docs/course-c/week-11.md` |
| 04-02-02 | 02 | RISK-03, LAB-02, LAB-03 | source | `test -f docs/course-c/labs/lab-10.md && test -f docs/course-c/labs/lab-11.md` |
| 04-03-01 | 03 | CURR-04, RISK-02, RISK-04 | source | `test -f docs/course-c/week-12.md && test -f docs/course-c/week-13.md` |
| 04-03-02 | 03 | RISK-03, LAB-02, LAB-03 | source | `test -f docs/course-c/labs/lab-12.md && test -f docs/course-c/labs/lab-13.md` |
| 04-04-01 | 04 | CURR-04, RISK-02, RISK-04 | source | `test -f docs/course-c/week-14.md && test -f docs/course-c/labs/lab-14.md` |
| 04-04-02 | 04 | CURR-04, LAB-01 | source/build | `rg -n "/course-c/week-14|/course-c/labs/lab-14" docs/.vitepress/config.mjs && cd docs && BASE=/ai-course-system/ npm run build` |

## Required Source Checks

- Week pages contain `AI 可以支持`, `AI 不能直接做`, `Reference 使用`, `实现来源`, `权威领域来源`, `数据门`, `来源门`, `人类门`, `审计门`.
- Lab pages contain `脱敏`, `来源`, `审批`, `审计`, and `岗位 AI 助理包`.
- Sidebar omits Week/Lab 15-16 until Phase 5/6.

---

*Phase: 04-high-risk-business-weeks-08-14-and-labs*
