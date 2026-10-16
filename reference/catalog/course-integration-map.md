# Course Integration Map

This map connects the current course system to the reference library. Course B
is the 16-week full-stack sidebar in `docs/.vitepress/config.mjs`. Agent
engineering is Week 15 of that same course, not a second calendar.

## Course A: Product Prototype + Claude Code

| Course area | Current weeks | References to inspect | Improvement ideas |
| --- | --- | --- | --- |
| No-code fear removal and first app | Week 01-02 | `courses/web-dev-for-beginners`, Vercel AI Chatbot | Add 2-3 small starter apps with screenshots and clear run commands. |
| Claude Code basics | Week 03 | `agentic-coding/anthropic-courses`, `agentic-coding/aider`, Anthropic Claude Code short course | Add a side-by-side "chatbot vs coding agent" exercise with diff review evidence. |
| Product discovery | Week 04-05 | The Mom Test, Continuous Discovery Habits, Sprint, Shape Up | Strengthen interview scripts, anti-pattern examples, and decision criteria. |
| Prototype to AI feature | Week 06-08 | `fullstack-ai/vercel-ai-chatbot`, `ai-engineering/openai-cookbook`, `fullstack-ai/supabase` | Add one real API-backed prototype path with mock mode and real-call verification. |
| Workflow and Skills | Week 09-10 | `agentic-coding/spec-kit`, `agentic-coding/anthropic-courses`, Agent Skills course | Convert current workflow advice into reusable checklists and one student-built skill. |
| MCP | Week 11 | `mcp/mcp-servers`, `mcp/mcp-typescript-sdk`, MCP docs/course | Add a minimal local MCP server design lab before any production integration. |
| Superpowers and verification | Week 12 | `agentic-coding/spec-kit`, Software Engineering at Google, Google SRE books | Add "completion proof" and "verification log" templates. |
| Spec coding and long-running tasks | Week 13-14 | `agentic-coding/spec-kit`, `agentic-coding/openhands`, `agentic-coding/swe-agent` | Add a spec-to-plan-to-diff exercise with a bounded task and explicit stop rule. |
| Agent SDK and Agent Teams | Week 15-16 | `ai-engineering/openai-agents-python`, `agentic-coding/browser-use`, `rag/langgraph` | Add role boundaries, handoff diagrams, and a small multi-agent trace example. |

## Course B: AI 全栈开发实战（16 周，与侧边栏一致）

公开页面上的周次以 `docs/.vitepress/config.mjs` 里 `/course-b/` 的「每周教程」为准。下面这张表取代以前把 Course B 拆成「全栈轨」和「Agent 轨」、并且都只排到 Week 12 的两张旧表。

| Sidebar week | Topic | References to inspect | What the chapter now asks students to hand in |
| --- | --- | --- | --- |
| Week 01 | 从设计到代码 | `fullstack-ai/shadcn-ui`, Refactoring UI | 三种路径对比，加上一处人工修订 diff |
| Week 02 | 组件库与多产品 UI | `fullstack-ai/shadcn-ui` | 同一套 token 被两个页面复用 |
| Week 03 | Figma 与设计资产 | [WCAG 2.2 对比度 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum), [Figma Auto Layout](https://help.figma.com/hc/en-us/articles/360040451373-Create-dynamic-designs-with-auto-layout) | 层级、对齐、间距、对比，以及绝对定位导出和 flex 导出的对照 |
| Week 04 | 现代 CLI 与 Git | [Pro Git：Git 对象](https://git-scm.com/book/zh/v2/Git-%E5%86%85%E9%83%A8%E5%8E%9F%E7%90%86-Git-%E5%AF%B9%E8%B1%A1), [git-restore](https://git-scm.com/docs/git-restore) | blob / tree / commit、分支合并，以及 AI 改坏文件后的 diff 与 revert |
| Week 05 | 数据库与 Supabase | [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security), [PostgreSQL 事务](https://www.postgresql.org/docs/current/tutorial-transactions.html) | 三道 `orders` 查询、RLS 关闭时 anon key 的读法、订单事务回滚 |
| Week 06 | 接入 AI 接口 | `fullstack-ai/vercel-ai`, `ai-engineering/openai-cookbook` | 后端持有密钥、流式响应和错误处理 |
| Week 07 | 支付与部署 | [Stripe Webhooks](https://docs.stripe.com/webhooks), [重复事件](https://docs.stripe.com/webhooks#handle-duplicate-events) | 支付状态图、签名校验、`event.id` 幂等、金额只来自服务端 price |
| Week 08 | Dify 知识库 | Dify 文档, `rag/dify` | 切分、top-k、拒答阈值三参数记录表，交给 Week 09 |
| Week 09 | RAG 入门 | [RAGAS](https://arxiv.org/abs/2309.15217), [RGB](https://arxiv.org/abs/2309.01431) | 五题手算 Recall@3 与 MRR，以及最小 RAG 改阈值前后的六行记录 |
| Week 10 | 高级 RAG 与企业知识库 | `rag/llama-index`, `rag/langgraph` | 一条客服对话走完切分、重排、拒答和转人工 |
| Week 11 | 跨平台 PWA | `cross-platform/expo` 仅作对照；本周正文是 PWA | manifest、service worker、离线与安装 |
| Week 12 | 小程序入门 | `cross-platform/taro`, `cross-platform/uni-app` | 页面结构、开发者工具、发布边界 |
| Week 13 | 小程序后端 | 微信云开发文档 | 云函数、云数据库、登录态；模型密钥留在后端 |
| Week 14 | 跨平台整合 | 同上，加一条迁移记录 | 请求 `req_act_20261016_0142` 的平台、数据库和失败日志 |
| Week 15 | Agent 工程 | `docs/course-b/templates`, `agentic-coding/spec-kit` | 只允许修改 `activity_trace.py` 的规则、人工门和 trace |
| Week 16 | 期末评审 | `production-apps/cal-com`, `production-apps/dub` | 证据索引逐列指回同一条请求，而不是另起一个项目 |

## Course C: Enterprise AI Operations System

Course C maps reference material to business-role AI workflows. Public course
pages should not require local `reference/repos/`; local clones are optional
teacher preparation material. Student-facing pages should cite source categories
and accessible public documentation, books, papers, standards, regulator
guidance, or company policy.

| Course area | Current weeks | Implementation references | Authoritative domain references | Improvement ideas |
| --- | --- | --- | --- | --- |
| AI operating-system setup | Week 01 | Course C templates, AGENTS/Codex/Claude Code docs, shared setup pages | Workflow management, organizational design, AI governance | Add a filled assistant-pack example for one nontechnical role. |
| Market research | Week 02 | Survey tools, spreadsheet tools, public-source collection workflows | Market research textbooks, consumer research papers, industry-report methods | Add a source-quality rubric for public reports and AI summaries. |
| Product positioning | Week 03 | Prototype tools, document templates, prompt-library template | Product management books, user research methods, Stage-Gate, design research | Add one before/after positioning critique with source evidence. |
| Brand promotion | Week 04 | Content calendars, design tools, publishing checklists | Brand management, integrated marketing communication, advertising ethics, platform rules | Add review examples for risky marketing claims. |
| Sales and CRM | Week 05-06 | CRM docs, meeting-note templates, sales email templates | Sales management, customer relationship management, customer-experience research | Add a CRM-field governance checklist shared by sales and operations. |
| Data analysis and dashboards | Week 07 | Spreadsheet/BI docs, metric dictionaries, dashboard specs | Statistics, data quality, business analytics, Balanced Scorecard | Add dashboard anti-pattern examples around misleading metrics. |
| Investment and IB materials | Week 08-09 | EDGAR/public filing workflows, BP templates, due-diligence checklists | SEC/FINRA investor education, company finance, valuation, investment banking texts | Add jurisdiction notes so examples are not mistaken for advice. |
| Finance and tax | Week 10-11 | Sample finance data, budget tables, tax-record checklists | Accounting standards, management accounting, internal control, tax authority guidance | Add separate local-tax-authority lookup instructions for teachers. |
| HR and legal | Week 12-13 | HR sample data, JD templates, contract/dispute sample, evidence packet templates | DOL/EEOC examples, HR management, labor law, contract law, court-record guidance | Add privacy-preserving submission examples. |
| Administration and governance | Week 14 | Asset registers, meeting minutes, qualification calendars, policy SOPs | Corporate governance, records management, procurement controls, asset management | Add an approval-matrix example for small teams. |
| Enterprise system connection | Week 15 | OpenAI/Codex Skills, AGENTS, MCP, permissions docs; Claude Code MCP docs; MCP docs | NIST SP 800-53, OWASP LLM Top 10, ISO/CIS/SOC2, privacy/security policy | Add a sample read-only/mock-first connection packet. |
| Final defense | Week 16 | Course C final project, rubric, templates, audit log, ROI report | The selected role's professional sources and organization-specific approval rules | Add exemplar defense decks after the first cohort. |

## Gaps To Consider Next

- Course B now follows one 16-week sidebar. Week 15 is the Agent engineering
  week inside that calendar. Do not revive a second 12-week Agent track with
  different week numbers.
- Add small local sample projects for each major reference category so students
  do not need to learn from huge production repositories first.
- Add "reference reading" assignments: students inspect one cloned project and
  extract directory structure, run command, test command, and one reusable idea.
- For Course C, add public exemplar submissions for one low-risk role and one
  high-risk role so students can see the expected evidence depth.
