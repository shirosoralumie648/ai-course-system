# Course B Weeks 14-16 Long Chapters Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand Course B weeks 14, 15, and 16 from short summary pages into long-form teaching chapters comparable to the existing Week 10 and Week 13 chapters.

**Architecture:** This is a content-only update. Keep the VitePress navigation and component contracts unchanged, and replace only the three week markdown files with deeper classroom narrative, reference analysis, implementation workflows, failure diagnosis, evidence requirements, and assessment material.

**Tech Stack:** VitePress, Markdown, existing `ChapterIntroduction` component.

---

### Task 1: Expand Week 14

**Files:**
- Modify: `docs/course-b/week-14.md`

- [ ] Replace the short cross-platform page with a long chapter covering platform selection, product-path migration, PWA implementation, mini-program implementation, mobile-app implementation, evidence capture, failure diagnosis, and student deliverables.
- [ ] Preserve the existing title, `ChapterIntroduction`, and course framing.
- [ ] Avoid changing sidebar routes or build configuration.

### Task 2: Expand Week 15

**Files:**
- Modify: `docs/course-b/week-15.md`

- [ ] Replace the short Agent engineering page with a long chapter covering rules, skills, MCP permissions, agent teams, human gates, trace records, security boundaries, testing evidence, and final-project integration.
- [ ] Preserve the existing title, `ChapterIntroduction`, and course framing.
- [ ] Avoid introducing new dependencies or runtime components.

### Task 3: Expand Week 16

**Files:**
- Modify: `docs/course-b/week-16.md`

- [ ] Replace the short final defense page with a long chapter covering release review, demo scripts, evidence packages, technical review, AI/RAG evaluation, production-gap analysis, scoring rubrics, and defense preparation.
- [ ] Preserve the existing title, `ChapterIntroduction`, and course framing.
- [ ] Keep final-project expectations specific and auditable.

### Task 4: Verify

**Commands:**

- [ ] Run `wc -l docs/course-b/week-14.md docs/course-b/week-15.md docs/course-b/week-16.md` and confirm each page has been expanded materially.
- [ ] Run `BASE=/ai-course-system/ npm run build` from `docs`.
- [ ] Confirm `docs/.vitepress/dist/course-b/week-14.html`, `week-15.html`, and `week-16.html` exist.
