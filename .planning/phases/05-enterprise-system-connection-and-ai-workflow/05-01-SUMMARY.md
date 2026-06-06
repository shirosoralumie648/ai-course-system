---
phase: 05-enterprise-system-connection-and-ai-workflow
plan: 01
subsystem: course-content
tags: [course-c, enterprise-systems, api, mcp, skills, governance]
requires:
  - phase: 04-high-risk-business-weeks-08-14-and-labs
    provides: High-risk Course C wording pattern and four-gate compliance
provides:
  - Week 15 enterprise system connection and AI workflow governance page
  - Lab 15 read-only/mock-first connection plan assignment
affects: [course-c, phase-6]
tech-stack:
  added: []
  patterns:
    - Enterprise connection content grades governance packets rather than live connectors
    - API/MCP/Skills are framed as capability surfaces with permission and audit boundaries
key-files:
  created:
    - docs/course-c/week-15.md
    - docs/course-c/labs/lab-15.md
  modified: []
key-decisions:
  - "Week 15 keeps code optional and accessible to business learners."
  - "Lab 15 requires read-only, mock-first, least-privilege, human approval, audit log, secret hygiene, and no production writes."
  - "Implementation sources are separated from governance/security sources."
patterns-established:
  - "Enterprise connection plans require workflow card, system inventory, data classification, field map, permission matrix, mock dataset, approval record, audit log, and stop rules."
requirements-completed:
  - RISK-05
duration: 12 min
completed: 2026-06-06
---

# Phase 05 Plan 01 Summary

**Course C Week/Lab 15 covering safe enterprise system connection planning**

## Accomplishments

- Added Week 15 enterprise system connection and AI workflow governance content.
- Explained Skills, AGENTS/project instructions, API/MCP concepts, permission boundaries, secret hygiene, audit logs, and mock-first testing.
- Added Lab 15 read-only/mock-first enterprise connection plan assignment.
- Required workflow card, system inventory, data classification, field map, permission matrix, mock dataset, approval record, audit log, and stop/rollback rules.

## Task Commits

1. **Enterprise connection week** - `f98a75a` (feat)

## Verification

- Required Week/Lab 15 section scans passed.
- Enterprise safety scans passed for `read-only`, `mock-first`, `least privilege`, `secret hygiene`, `no production writes`, `human approval`, and `audit log`.
- `verify.artifacts` returned `all_passed: true`.
- `verify.key-links` returned `all_verified: true`.
- `BASE=/ai-course-system/ npm run build` exited 0 from `docs/`.

## Notes

Week 15 intentionally does not implement a live connector. The deliverable is a governance-ready connection plan.
