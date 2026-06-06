---
phase: 04-high-risk-business-weeks-08-14-and-labs
plan: 03
subsystem: course-content
tags: [course-c, hr, legal, contracts, labs, compliance]
requires:
  - phase: 04-high-risk-business-weeks-08-14-and-labs
    plan: 02
    provides: High-risk Course C wording pattern
provides:
  - Week 12 HR recruiting, training, and performance-process page
  - Week 13 legal contract and dispute-material organization page
  - Lab 12 screening rubric and bias/privacy review assignment
  - Lab 13 contract dispute timeline and lawyer-question assignment
affects: [course-c, phase-5, phase-6]
tech-stack:
  added: []
  patterns:
    - HR pages separate process drafting from employment decisions
    - Legal pages separate issue spotting and evidence organization from legal opinion and dispute strategy
key-files:
  created:
    - docs/course-c/week-12.md
    - docs/course-c/week-13.md
    - docs/course-c/labs/lab-12.md
    - docs/course-c/labs/lab-13.md
  modified: []
key-decisions:
  - "Week 12 prohibits AI-driven hiring, firing, pay, and performance decisions."
  - "Week 13 prohibits final legal opinion, contract signing, and dispute strategy."
  - "Both pages cite implementation sources and authoritative HR/labor/legal source categories."
patterns-established:
  - "Legal and HR labs require boundary review artifacts, not only task outputs."
requirements-completed: []
duration: 15 min
completed: 2026-06-06
---

# Phase 04 Plan 03 Summary

**Course C Week/Lab 12-13 covering HR and legal/dispute workflows**

## Accomplishments

- Added Week 12 HR recruiting, structured screening, interview, training, and bias/privacy review workflow.
- Added Week 13 contract clause checklist, dispute timeline, evidence packet, and lawyer-question workflow.
- Added Lab 12 JD, screening rubric, interview question bank, and bias/privacy review assignment.
- Added Lab 13 contract clause checklist, evidence packet, and lawyer-question assignment.

## Task Commits

1. **HR and legal weeks** - `29affb0` (feat)

## Verification

- Required week/lab section scans passed.
- HR/legal prohibited-action scans passed for hiring/pay/performance decisions, legal opinions, contract signing, and dispute strategy.
- `verify.artifacts` returned `all_passed: true`.
- `verify.key-links` returned `all_verified: true`.
- `BASE=/ai-course-system/ npm run build` exited 0 from `docs/`.

## Notes

The pages use sample HR and contract/dispute materials and require privacy, source, approval, and audit evidence before any learner submission.
