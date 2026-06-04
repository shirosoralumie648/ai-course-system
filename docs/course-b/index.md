# 课程 B：AI 全栈开发实战

> **AI 输出必须验证。** 这门课带你用 AI 做真正的全栈开发：从前端到后端、从数据库到部署、从接 AI 接口到企业级 RAG，最后跨平台交付一个完整产品。

<ChapterIntroduction duration="16 周，每周 2-3 课时" output="一个完整的 AI 全栈应用 + 期末答辩" :tags="['前端', '组件库', '数据库', 'Supabase', 'AI 接口', '支付部署', 'RAG', '跨平台', 'Agent 工程']">

面向有编程基础的学生。训练用 AI 完成真实软件工程：前端到代码、后端与数据库、接入 AI 与 RAG、支付部署、跨平台落地，以及用 Agent 工程方法把这一切高效安全地组织起来。

</ChapterIntroduction>

## 先修要求

- 能阅读并修改小型 Python 或 JavaScript 项目
- 掌握 Git 的 clone、branch、commit、diff、pull request 基础操作
- 能运行基本的命令行和测试命令
- 有基本安全意识：不提交 API Key、Token、密码

## 学完能做什么

1. 用 AI 把设计稿和想法转成可运行的前端代码
2. 用组件库和设计 token 搭出一致、可复用的多产品 UI
3. 用 Supabase 给应用加上数据库、认证和后端能力
4. 在后端安全地接入 AI 大模型接口
5. 给产品接上支付（Stripe）并部署上线（Zeabur）
6. 理解并实现 RAG，搭建企业级知识库应用
7. 把产品落地到小程序和移动端等多个平台
8. 用规格驱动、工作流编排和 Agent 团队的方法高效完成工程

## 16 周学习路线

每周教程把概念、动手和复盘串成一条递进路线。从「把设计变成代码」开始，到交付一个跨平台、带 AI 能力、带验证证据的完整全栈产品结束。Agent 工程放在后段作为交付纪律，而不是把课程 B 变成纯 Agent 课。

| 周次 | 主题 | 核心能力 | 配套 Lab |
|---|---|---|---|
| [Week 01](/course-b/week-01) | 从设计原型到项目代码 | Figma、MasterGo、截图、多模态 AI、MCP 路径选型 | [Lab 01](/course-b/labs/lab-01) |
| [Week 02](/course-b/week-02) | 组件库与多产品 UI | 组件库、设计 token、跨页面复用 | [Lab 02](/course-b/labs/lab-02) |
| [Week 03](/course-b/week-03) | Figma 与设计资产生成 | Frame、Auto Layout、AI 素材生成、资产库 | [Lab 03](/course-b/labs/lab-03) |
| [Week 04](/course-b/week-04) | 现代 CLI 与 Git 版本管理 | 终端、Claude Code、Codex、Git、diff 审查 | [Lab 04](/course-b/labs/lab-04) |
| [Week 05](/course-b/week-05) | 数据库与 Supabase | PostgreSQL、数据表、认证、RLS、Storage、Edge Functions | [Lab 05](/course-b/labs/lab-05) |
| [Week 06](/course-b/week-06) | AI 后端接口与密钥安全 | Express/API route、后端代理、OpenAPI、测试、流式响应 | [Lab 06](/course-b/labs/lab-06) |
| [Week 07](/course-b/week-07) | 支付与部署 | Stripe Checkout、Webhook、Zeabur、环境变量、线上验证 | [Lab 07](/course-b/labs/lab-07) |
| [Week 08](/course-b/week-08) | Dify 知识库 | 平台 RAG、文档导入、检索测试、API 对接 | [Lab 08](/course-b/labs/lab-08) |
| [Week 09](/course-b/week-09) | RAG 入门 | 切块、Embedding、向量检索、最小 RAG 脚本、效果评测 | [Lab 09](/course-b/labs/lab-09) |
| [Week 10](/course-b/week-10) | 高级 RAG 与企业知识库 | LlamaIndex、LangGraph、知识治理、证据化回答 | [Lab 10](/course-b/labs/lab-10) |
| [Week 11](/course-b/week-11) | 跨平台 PWA | 平台选择、manifest、service worker、离线与安装体验 | [Lab 11](/course-b/labs/lab-11) |
| [Week 12](/course-b/week-12) | 平台选择与小程序入门 | 小程序账号、开发者工具、页面结构、发布流程 | [Lab 12](/course-b/labs/lab-12) |
| [Week 13](/course-b/week-13) | 小程序后端 | 云开发、云函数、云数据库、云存储、登录态和权限 | [Lab 13](/course-b/labs/lab-13) |
| [Week 14](/course-b/week-14) | 小程序、移动端或 PWA 实现 | 选择一个平台补齐核心用户路径 | [Lab 14](/course-b/labs/lab-14) |
| [Week 15](/course-b/week-15) | Rules、Skills、MCP 与 Agent Team | 项目规则、Skill、MCP、Agent 分工与 Human Gate | [Lab 15](/course-b/labs/lab-15) |
| [Week 16](/course-b/week-16) | 期末答辩与技术评审 | Demo、代码走查、测试证据、技术复盘 | [Lab 16](/course-b/labs/lab-16) |

也可以查看 [16 周教学日历](/course-b/teaching-calendar) 了解每周的课堂内容、动手任务和课后作业安排。

## reference 怎么进入课程 B

课程 B 的 reference 要直接变成工程判断、Demo、作业和验收证据。具体读法见 [参考项目读法](/shared/reference-reading)，逐周课堂方案见 [课程 B reference 融入方案](/course-b/reference-integration)。

| 模块 | 参考来源 | 加进课程的内容 |
|---|---|---|
| 前端与设计系统 | `fullstack-ai/shadcn-ui`、`courses/web-dev-for-beginners` | 组件规范、设计 token、UI before/after 评审 |
| CLI、Git 与 AI 编程 | `courses/missing-semester`、`agentic-coding/aider`、`agentic-coding/gemini-cli` | shell/git drill、AI 工具对比、diff 和测试日志 |
| AI 应用集成 | `fullstack-ai/vercel-ai`、`fullstack-ai/vercel-ai-chatbot`、`ai-engineering/openai-cookbook` | streaming、backend AI route、tool calling、密钥安全 |
| Supabase 后端 | `fullstack-ai/supabase` | schema、RLS、storage、edge function 样例 |
| 支付与部署 | Stripe samples、`production-apps/dub` | checkout、subscription、webhook、后端持有 price ID |
| RAG 与知识库 | `rag/dify`、`rag/rag-from-scratch`、`rag/llama-index`、`rag/haystack`、`rag/graph-rag` | 从平台 RAG 到代码 RAG、rerank、eval、graph retrieval |
| 跨平台 | `cross-platform/expo`、`cross-platform/taro`、`cross-platform/uni-app` | Web、PWA、小程序、移动端决策矩阵和最小实现 |
| Agent 工程 | `agentic-coding/spec-kit`、`mcp/mcp-servers`、`mcp/mcp-typescript-sdk`、`ai-engineering/openai-agents-python` | rules、skills、MCP、Agent team、human gate、trace |

从 Week 04 开始，每个阶段都要求提交"参考借鉴说明"：读了哪里、借鉴了什么、怎么改造到自己的产品、用什么证据证明有效。

## 课程主线

<SummaryCard title="课程 B 三条主线" :sections="[
  { number: '1', title: '做出真正能用的产品', items: ['前端到代码、组件库、设计资产落地', '数据库、认证、支付、部署，全栈打通'] },
  { number: '2', title: '把 AI 能力接进产品', items: ['后端安全封装 AI 接口', '从 Dify 知识库到自己实现 RAG 和企业级检索'] },
  { number: '3', title: '用工程方法高效交付', items: ['现代 CLI 与 Git 协作工作流', '规格驱动开发、工作流编排、Agent 团队，跨平台落地'] }
]" :outputs="[
  '一个全栈 + AI 的完整应用',
  '可部署上线、能跨平台访问的产品',
  '1 个期末答辩项目'
]" />
