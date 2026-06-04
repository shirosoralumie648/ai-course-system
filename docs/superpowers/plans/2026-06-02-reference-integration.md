# Reference Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the local `reference/` library visibly correct and enrich Course A, Course B, and shared resources instead of leaving it as a catalog.

**Architecture:** Keep reference material in shared resources as the common reading method, then connect Course A and Course B to that method through week-level maps and evidence requirements. Do not copy large third-party text or require students to run large repositories.

**Tech Stack:** VitePress Markdown, existing course pages, local `reference/catalog/course-integration-map.md`, VitePress sidebar config.

---

### Task 1: Shared Reference Reading Page

**Files:**
- Create: `docs/shared/reference-reading.md`
- Modify: `docs/shared/index.md`
- Modify: `docs/.vitepress/config.mjs`

- [ ] **Step 1: Create a shared reading guide**

Add a page that explains how references enter teaching: concept structure, classroom demo, assignment, and acceptance criteria. Include Course A and Course B mapping tables.

- [ ] **Step 2: Add shared-resource entry points**

Add the new page to `docs/shared/index.md` and the shared sidebar.

- [ ] **Step 3: Verify the shared page is reachable**

Run `rg -n "reference-reading|参考项目读法" docs/shared docs/.vitepress/config.mjs`.

### Task 2: Course Entry Pages

**Files:**
- Modify: `docs/course-a/index.md`
- Modify: `docs/course-b/index.md`

- [ ] **Step 1: Add Course A reference mapping**

Add a "reference 怎么进入课程 A" section that maps reference categories to the existing 16-week Course A flow.

- [ ] **Step 2: Convert Course B entry page to 16 weeks**

Update duration, route description, week table, calendar link, and add a "reference 怎么进入课程 B" section.

- [ ] **Step 3: Verify no stale 12-week entry wording remains**

Run `rg -n "12 周|12周|12 次|第 12 周：高级 Agent" docs/course-b/index.md`.

### Task 3: Course B Delivery Requirements

**Files:**
- Modify: `docs/course-b/teaching-calendar.md`
- Modify: `docs/course-b/final-project.md`
- Modify: `docs/course-b/rubric.md`
- Create: `docs/course-b/week-14.md`
- Create: `docs/course-b/week-15.md`
- Create: `docs/course-b/week-16.md`

- [ ] **Step 1: Replace the Course B calendar with the 16-week structure**

Use the accepted full-stack, RAG, cross-platform, Agent engineering sequence.

- [ ] **Step 2: Add week 14-16 pages**

Add focused pages for cross-platform implementation, Agent engineering, and final defense so sidebar links resolve.

- [ ] **Step 3: Update final project requirements**

Require a deployed AI full-stack product, reference-borrowing note, RAG/cross-platform decision evidence, Agent workflow evidence, and test logs.

- [ ] **Step 4: Update rubric**

Grade product, full-stack, AI/RAG, cross-platform decision, Agent workflow, reference evidence, and verification evidence.

### Task 4: Course A Assessment Requirements

**Files:**
- Modify: `docs/course-a/final-project.md`
- Modify: `docs/course-a/rubric.md`

- [ ] **Step 1: Add reference borrowing to Course A final project**

Require students to explain one borrowed idea from the reference library and how they simplified it for a non-CS prototype.

- [ ] **Step 2: Add reference evidence to Course A rubric**

Reserve rubric weight for reference borrowing and verification without turning Course A into a full-stack course.

### Task 5: Build Verification

**Files:**
- All modified docs files

- [ ] **Step 1: Search for stale Course B language**

Run `rg -n "12 周|12周|12 次|Agentic Workflow 设计与实现|高级 Agent 技能" docs/course-b docs/.vitepress/config.mjs`.

- [ ] **Step 2: Build VitePress**

Run `cd docs && npm run build`.

- [ ] **Step 3: If build fails**

Inspect the reported file and line. Fix Markdown or Vue component syntax, then rerun the build.
