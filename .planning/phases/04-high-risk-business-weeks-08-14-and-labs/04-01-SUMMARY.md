---
phase: 04-high-risk-business-weeks-08-14-and-labs
plan: 01
subsystem: course-content
tags: [course-c, investment-research, investment-banking, labs, compliance]
requires:
  - phase: 02-compliance-templates-and-synthetic-examples
    provides: Four-gate compliance templates and synthetic examples
  - phase: 03-core-business-weeks-01-07-and-labs
    provides: Course C week/lab rhythm and navigation pattern
provides:
  - Week 08 public stock investment research boundary page
  - Week 09 investment banking and business planning boundary page
  - Lab 08 risk memo and no-recommendation evidence assignment
  - Lab 09 BP, due diligence, and roadshow Q&A review assignment
affects: [course-c, phase-5, phase-6]
tech-stack:
  added: []
  patterns:
    - Static Markdown high-risk pages with explicit AI support/prohibition tables
    - Evidence-first labs with source, human approval, and audit gates
key-files:
  created:
    - docs/course-c/week-08.md
    - docs/course-c/week-09.md
    - docs/course-c/labs/lab-08.md
    - docs/course-c/labs/lab-09.md
  modified: []
key-decisions:
  - "Week 08 teaches public investment research as source organization and risk memo work, not buy/sell/hold advice."
  - "Week 09 teaches BP, due diligence, and roadshow Q&A organization, not final valuation, deal terms, or solicitation."
  - "Both pages distinguish implementation sources from authoritative domain sources."
patterns-established:
  - "High-risk Course C pages state AI 可以支持, AI 不能直接做, and 必须由负责人或专业人员确认."
  - "Labs require redaction, source checking, human approval, audit logging, and assistant-pack updates."
requirements-completed: []
duration: 16 min
completed: 2026-06-06
---

# Phase 04 Plan 01 Summary

**Course C Week/Lab 08-09 covering public stock research and investment banking/business planning**

## Accomplishments

- Added Week 08 public stock investment research with SEC/EDGAR, FINRA, public filing, and investment-analysis source boundaries.
- Added Week 09 investment banking and business planning materials with BP, due diligence, roadshow Q&A, and material-review boundaries.
- Added Lab 08 no-recommendation risk memo assignment.
- Added Lab 09 BP evidence outline, due diligence checklist, and Q&A review assignment.

## Task Commits

1. **Investment and banking weeks** - `e5cc769` (feat)

## Verification

- Required week/lab section scans passed.
- High-risk support/prohibition and four-gate scans passed.
- `verify.artifacts` returned `all_passed: true`.
- `verify.key-links` returned `all_verified: true`.
- `BASE=/ai-course-system/ npm run build` exited 0 from `docs/`.

## Notes

Requirements are not marked globally complete here because `CURR-*`, `LAB-*`, and `RISK-*` still include later Week/Lab 15-16 scope.
