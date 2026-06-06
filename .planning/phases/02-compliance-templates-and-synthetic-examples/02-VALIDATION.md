---
phase: 02
slug: compliance-templates-and-synthetic-examples
status: draft
nyquist_compliant: true
wave_0_complete: true
created: 2026-06-06
---

# Phase 02 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | VitePress build plus shell/source assertions |
| **Config file** | `docs/package.json`, `docs/.vitepress/config.mjs` |
| **Quick run command** | `git diff --check && gsd-sdk query verify.plan-structure .planning/phases/02-compliance-templates-and-synthetic-examples/02-01-PLAN.md` |
| **Full suite command** | `cd docs && BASE=/ai-course-system/ npm run build` |
| **Estimated runtime** | ~20 seconds |

---

## Sampling Rate

- **After every task commit:** Run the task's `<verify>` command and `git diff --check`.
- **After every plan wave:** Run `BASE=/ai-course-system/ npm run build` from `docs/`.
- **Before `$gsd-verify-work`:** Full build and all plan `must_haves` checks must be green.
- **Max feedback latency:** 30 seconds.

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 02-01-01 | 01 | 1 | TEMP-01, TEMP-02 | T-02 | Templates use synthetic examples and no real sensitive data. | source | `find docs/course-c/templates -maxdepth 1 -type f` | W0 | pending |
| 02-01-02 | 01 | 1 | TEMP-03, TEMP-04 | T-02 | Examples are fictional/sample-only. | source | `rg -n "示例|虚构|fictional|sample" docs/course-c/examples` | W0 | pending |
| 02-02-01 | 02 | 2 | RISK-01 | T-01 | Four gates include risk, approver, audit, and release boundary fields. | source | `rg -n "数据门|来源门|人类门|审计门|风险等级|审批人|审计证据|发布边界" docs/course-c/templates/compliance-checklist.md` | W0 | pending |
| 02-02-02 | 02 | 2 | REF-01, REF-04, REF-05 | T-01 | Source matrix distinguishes implementation and domain authority. | source | `rg -n "实现来源|权威领域来源|来源矩阵|不能推出什么结论" docs/course-c/reference-integration.md` | W0 | pending |
| 02-02-03 | 02 | 2 | TEMP-01, TEMP-02, TEMP-03 | T-03 | Sidebar links only created Phase 2 files. | source/build | `rg -n "/course-c/templates/|/course-c/examples/" docs/.vitepress/config.mjs && cd docs && BASE=/ai-course-system/ npm run build` | W0 | pending |

---

## Wave 0 Requirements

Existing infrastructure covers all phase requirements:

- `docs/package.json` contains the VitePress build command.
- `docs/.vitepress/config.mjs` controls nav/sidebar routing.
- `gsd-sdk query verify.plan-structure` validates plan structure.

---

## Manual-Only Verifications

All Phase 2 behaviors have automated source/build verification. Human review is
still useful for educational quality, but not required to prove phase completion.

---

## Validation Sign-Off

- [x] All tasks have automated verify commands
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all missing references
- [x] No watch-mode flags
- [x] Feedback latency < 30s
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** pending execution
