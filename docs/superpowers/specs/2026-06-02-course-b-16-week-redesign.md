# Course B 16-Week Redesign

## Goal

Expand Course B from a compressed 12-week outline into a 16-week AI full-stack
product engineering course that covers frontend, database, AI API integration,
payments, deployment, RAG, cross-platform delivery, and Agent engineering without
turning Agentic Development into a separate competing course.

## Current Problem

The current Course B entry page positions the course as "AI full-stack
development" with frontend, Supabase, AI APIs, payment, deployment, RAG,
cross-platform work, and Agent engineering. The current teaching calendar is
mostly a 12-week Agentic Development syllabus around Claude Code, Codex, rules,
skills, MCP, subagents, tests, and review. The directory also contains
`week-13.md`, while the entry page describes a 12-week course.

This creates three problems:

- The course identity is split between full-stack product delivery and Agentic
  Development process training.
- Full-stack topics are too compressed to become a real product loop.
- Agent engineering has no product context if taught as an isolated block.

## Design Decision

Course B becomes a 16-week course:

- Course A remains the non-CS "AI product prototype + Claude Code workflow"
  course.
- Course B becomes the technical "AI full-stack product engineering" course.
- Agent engineering becomes a late-course delivery method for Course B projects,
  not a separate primary track.
- Shared resources hold cross-course tools, templates, safety rules, reference
  reading guides, and verification logs.

## 16-Week Structure

| Phase | Week | Topic | Student output |
| --- | --- | --- | --- |
| Product and frontend foundation | 01 | AI full-stack product orientation | Product decomposition table and technical route map |
| Product and frontend foundation | 02 | Design to code with Figma, MasterGo, screenshots, and AI | Runnable landing or dashboard page |
| Product and frontend foundation | 03 | Component libraries and design systems | Reusable UI screen built with component conventions |
| Product and frontend foundation | 04 | CLI, Git, Claude Code, Codex, and engineering workflow | Diff, test log, and tool comparison record |
| Full-stack product loop | 05 | Supabase database, schema design, and CRUD | App with persistent data |
| Full-stack product loop | 06 | Auth, permissions, RLS, and file storage | Login, protected data, and upload flow |
| Full-stack product loop | 07 | AI API backend integration | Secure backend AI endpoint with real-call verification |
| Full-stack product loop | 08 | Payment and deployment | Public deployed product with payment or payment simulation |
| RAG and knowledge systems | 09 | Dify knowledge base and platform RAG | Dify knowledge-base app and retrieval test log |
| RAG and knowledge systems | 10 | Minimal code RAG | Document chunking, embeddings, vector search, answer generation |
| RAG and knowledge systems | 11 | Advanced RAG debugging and evaluation | RAG eval sheet covering recall, answer quality, and failure cases |
| RAG and knowledge systems | 12 | Enterprise knowledge base design | Permission, update, evaluation, and operations plan |
| Cross-platform delivery | 13 | Cross-platform decision making | Web, PWA, mini-program, and mobile decision matrix |
| Cross-platform delivery | 14 | Mini-program, mobile, or PWA implementation | Minimal cross-platform version of the product |
| Agent engineering | 15 | Rules, Skills, MCP, Agent Team, and Human Gate | Project-specific Agent workflow and safety rules |
| Final delivery | 16 | Final defense and technical review | Product demo, code walkthrough, test evidence, and reflection |

## Reference Material Mapping

Use reference projects as teacher preparation and focused student reading, not
as copy-paste source material.

| Course area | Local references | Use |
| --- | --- | --- |
| Frontend and UI | `reference/repos/fullstack-ai/shadcn-ui`, `reference/repos/courses/web-dev-for-beginners` | UI quality standards, small frontend exercises, component conventions |
| CLI and Git | `reference/repos/courses/missing-semester`, `reference/repos/agentic-coding/aider`, `reference/repos/agentic-coding/gemini-cli` | Terminal habits, diff review, coding agent comparison |
| AI app integration | `reference/repos/fullstack-ai/vercel-ai`, `reference/repos/fullstack-ai/vercel-ai-chatbot`, `reference/repos/ai-engineering/openai-cookbook` | Streaming, backend AI routes, tool calling, verification |
| Supabase | `reference/repos/fullstack-ai/supabase` | Auth, RLS, storage, edge function examples |
| Payment | `reference/repos/fullstack-ai/stripe-checkout-one-time`, `reference/repos/fullstack-ai/stripe-subscription-use-cases` | Checkout, subscription, webhook, backend-owned price IDs |
| RAG | `reference/repos/rag/dify`, `reference/repos/rag/rag-from-scratch`, `reference/repos/rag/llama-index`, `reference/repos/rag/haystack`, `reference/repos/rag/graph-rag` | Dify platform RAG, minimal RAG, advanced retrieval, evaluation |
| Cross-platform | `reference/repos/cross-platform/expo`, `reference/repos/cross-platform/taro`, `reference/repos/cross-platform/uni-app` | Mobile, mini-program, and cross-platform decision guidance |
| Agent engineering | `reference/repos/agentic-coding/spec-kit`, `reference/repos/mcp/mcp-servers`, `reference/repos/mcp/mcp-typescript-sdk`, `reference/repos/ai-engineering/openai-agents-python` | Rules, specs, MCP tool design, Agent team boundaries |

## File-Level Implementation Scope

Implementation should update these course-facing files:

- `docs/course-b/index.md`: change course duration, positioning, learning
  outcomes, and week table from 12 to 16 weeks.
- `docs/course-b/teaching-calendar.md`: replace the current 12-week Agentic
  Development calendar with the 16-week full-stack product engineering calendar.
- `docs/course-b/week-01.md` through `docs/course-b/week-13.md`: keep useful
  content, but align titles, transitions, outputs, references, and assignments
  with the new 16-week sequence.
- `docs/course-b/week-14.md`, `docs/course-b/week-15.md`,
  `docs/course-b/week-16.md`: add new pages for cross-platform implementation,
  Agent engineering, and final defense.
- `docs/course-b/final-project.md`: update final deliverables to require a
  deployed AI full-stack product, RAG component or justified omission, validation
  evidence, and Agent workflow evidence.
- `docs/course-b/rubric.md`: update grading to match product, full-stack, AI,
  RAG, cross-platform, Agent workflow, and verification evidence.
- `docs/shared/index.md`: add links to shared templates and verification
  resources when those pages are created.

Implementation may add shared-resource pages in a separate follow-up plan:

- `docs/shared/reference-reading.md`
- `docs/shared/templates.md`
- `docs/shared/security-checklist.md`
- `docs/shared/verification-log.md`
- `docs/shared/fallback-plan.md`

## Course Boundary Rules

- Do not move Course A into full-stack depth. Course A remains prototype-first
  and non-CS friendly.
- Do not make Course B a pure Agentic Development course. Agent engineering is a
  product delivery discipline taught after students have a real project.
- Do not require students to run large reference repositories. Teachers use them
  for preparation; students inspect selected files or simplified excerpts.
- Do not copy long third-party text into course pages. Summarize ideas, cite
  sources, and use local examples.

## Weekly Page Template

Each Course B week should converge on this structure:

```markdown
# 第 N 周：主题

## 本周目标
## 小哲的项目进展
## 核心概念
## 参考项目拆解
## 课堂 Demo
## 实验任务
## 常见错误
## 验收标准
## 参考资料
```

The template is a content target, not a requirement to erase existing useful
material. Existing sections can be retained if they still support the week goal.

## Acceptance Criteria

The redesign is complete when:

- Course B entry page, teaching calendar, week pages, final project, and rubric
  all describe a 16-week course consistently.
- The week list includes Week 01 through Week 16 and no dangling 12-week wording.
- The former Agentic Development content is either integrated into Week 04,
  Week 15, Week 16, labs, or shared resources.
- Each week has a concrete student output and an evidence-based acceptance
  requirement.
- Course A remains scoped to AI product prototypes and Claude Code workflow.
- Shared resources are referenced as common infrastructure rather than copied
  into every week.
- `npm run build` from `docs/` succeeds after content changes.

## Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Course B becomes too broad | Keep one final product thread across all weeks; each topic must improve that product. |
| Students drown in production repositories | Use reference projects for teacher prep and short reading tasks only. |
| Agent engineering feels disconnected | Teach it after the product loop and apply it to the final project. |
| Course A and B overlap | Course A stops at prototype and workflow literacy; Course B owns full-stack production depth. |
| Build breaks due Markdown/Vue component syntax | Run `npm run build` from `docs/` and fix component prop issues before completion. |

## Out of Scope

- Rewriting Course A pages as part of this Course B redesign.
- Fully implementing every shared-resource page in the same pass.
- Cloning additional reference repositories.
- Adding runnable sample projects before the 16-week structure is consistent.
