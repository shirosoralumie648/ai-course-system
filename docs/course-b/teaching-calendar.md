# 16 周教学日历：AI 全栈产品工程

> **给你的使用说明：** 每周按顺序完成"课堂内容 → 动手任务 → 配套实验 → 验收证据"。从第 4 周开始，每个阶段都要提交一段"参考借鉴说明"，写清楚读了哪个 reference、借鉴了什么、怎么改造到自己的项目、用什么证据验证。

---

## 第 1 周：从设计原型到项目代码

<ChapterIntroduction duration="1 课时" output="从设计稿还原出来的可运行页面 + 三种路径对比笔记" :tags="['Design to Code', 'Figma', 'MasterGo', '多模态 AI']">

- 理解多模态 AI、平台导出和 MCP 直连三种设计到代码路径
- 判断 AI 生成页面哪里可靠、哪里必须人工接管
- 建立从设计稿到本地运行页面的最小闭环

</ChapterIntroduction>

- **课堂内容**：设计稿拆解、截图生成页面、Figma/MasterGo 导出、MCP 路径对比
- **reference 借鉴**：`shadcn-ui` 的页面结构、`web-dev-for-beginners` 的小步运行习惯
- **动手任务**：选择一张设计稿或截图，生成一个能本地运行的页面
- **配套实验**：[Lab 01：设计到代码](/course-b/labs/lab-01)
- **验收证据**：页面能运行，报告包含三种路径取舍和至少一处人工修正

---

## 第 2 周：组件库与多产品 UI

<ChapterIntroduction duration="2-3 小时" output="一套可复用设计 token + 两个页面共享的组件清单" :tags="['组件库', '设计 token', 'shadcn/ui', '复用']">

- 使用组件库而不是复制粘贴页面
- 建立颜色、间距、圆角、按钮和表单的统一规则
- 让同一套视觉语言复用到多个产品页面

</ChapterIntroduction>

- **课堂内容**：组件库选择、设计 token、主题变量、组件复用和 UI before/after 评审
- **reference 借鉴**：`shadcn-ui` 的组件约定和 token 组织方式
- **动手任务**：为期末产品做 2 个风格一致的核心页面
- **配套实验**：[Lab 02：组件库与设计 token](/course-b/labs/lab-02)
- **验收证据**：至少一个组件或 token 被两个页面复用

---

## 第 3 周：Figma 与设计资产生成

<ChapterIntroduction duration="2-3 小时" output="结构清晰的页面原型 + 一套 AI 生成设计资产" :tags="['Figma', 'MasterGo', 'Auto Layout', 'AI 素材']">

- 掌握 Frame、Auto Layout、组件和设计资产的基本概念
- 用 AI 生成配图、图标或视觉素材，并保持风格一致
- 把设计稿当作结构化信息，而不是一张静态图片

</ChapterIntroduction>

- **课堂内容**：Figma/MasterGo 原型结构、素材生成、资产命名、设计到开发交接
- **reference 借鉴**：前端参考项目里的页面层级和素材使用方式
- **动手任务**：为产品准备一页原型和一组可复用素材
- **配套实验**：[Lab 03：设计资产生成](/course-b/labs/lab-03)
- **验收证据**：原型、素材、命名规则和至少一张落地截图齐全

---

## 第 4 周：现代 CLI 与 Git 版本管理

<ChapterIntroduction duration="2-3 小时" output="CLI AI 工具操作记录 + Git diff + 测试或运行日志" :tags="['CLI', 'Git', 'Claude Code', 'Codex', 'diff 审查']">

- 熟悉终端、Git、分支、commit、diff、push 的基本流程
- 对比 Claude Code、Codex 等 CLI AI 工具适合做什么
- 建立"先看 diff，再信结果"的工程习惯

</ChapterIntroduction>

- **课堂内容**：shell 基础、Git/GitHub、AI coding 工具边界、人工审批点
- **reference 借鉴**：`missing-semester` 的终端训练、`aider` 和 `gemini-cli` 的工具形态
- **动手任务**：用 AI 工具完成一个小改动，并人工审查 diff
- **配套实验**：[Lab 04：CLI、Git 与 AI 工程流](/course-b/labs/lab-04)
- **验收证据**：测试或运行命令可以复现，diff 审查有具体判断

---

## 第 5 周：数据库与 Supabase

<ChapterIntroduction duration="2-3 小时" output="带真实数据、认证和基础权限意识的应用" :tags="['Supabase', 'PostgreSQL', 'Auth', 'RLS', 'Storage']">

- 设计核心业务表和字段
- 实现数据创建、读取和刷新后持久化
- 理解认证、RLS、Storage、Edge Functions 在后端中的位置

</ChapterIntroduction>

- **课堂内容**：数据库、schema、CRUD、认证、RLS、Storage、Edge Functions 总览
- **reference 借鉴**：`supabase` 的 auth、database、storage 示例
- **动手任务**：为期末产品接入一张核心业务表和一条数据流程
- **配套实验**：[Lab 05：Supabase 数据库](/course-b/labs/lab-05)
- **验收证据**：刷新页面后数据仍存在，报告说明至少一个权限风险

---

## 第 6 周：AI 后端接口与密钥安全

<ChapterIntroduction duration="2-3 小时" output="安全 AI endpoint + 接口文档 + 调用验证日志" :tags="['AI API', '后端代理', '密钥安全', 'OpenAPI', '测试']">

- 在后端封装 AI 调用，不把密钥放到浏览器
- 用结构化 Prompt 让 AI 辅助生成分层接口、文档和测试
- 区分 mock mode、real-call mode、错误处理和流式响应

</ChapterIntroduction>

- **课堂内容**：REST/API route、后端代理、环境变量、错误脱敏、接口测试
- **reference 借鉴**：`vercel-ai`、`vercel-ai-chatbot`、`openai-cookbook`
- **动手任务**：给产品接入一个安全的 AI 后端接口
- **配套实验**：[Lab 06：AI 后端接口](/course-b/labs/lab-06)
- **验收证据**：有一次真实或模拟调用日志，密钥没有进入前端或仓库

---

## 第 7 周：支付与部署

<ChapterIntroduction duration="2-3 小时" output="支付或模拟支付闭环 + 公网部署版本 + 踩坑复盘" :tags="['Stripe', 'Webhook', 'Zeabur', '环境变量', '上线验证']">

- 理解 Checkout、Webhook、订单状态和后端确认的职责边界
- 把应用部署到公开地址，并处理端口、环境变量和域名问题
- 上线后亲自走查支付或模拟支付流程

</ChapterIntroduction>

- **课堂内容**：Stripe/支付模拟、Webhook、Zeabur 部署、环境变量和成本控制
- **reference 借鉴**：Stripe samples、`production-apps/dub`
- **动手任务**：上线一个可访问版本，并跑通支付或模拟支付证据
- **配套实验**：[Lab 07：支付与部署](/course-b/labs/lab-07)
- **验收证据**：公开地址能访问，敏感配置不暴露，支付状态有记录

---

## 第 8 周：Dify 知识库

<ChapterIntroduction duration="2-3 小时" output="Dify 知识库应用 + 检索测试日志 + API 对接记录" :tags="['Dify', '知识库', '平台 RAG', '检索测试']">

- 用平台方式快速搭建知识库应用
- 理解文档导入、切块、检索设置和回答质量的关系
- 记录检索测试，而不是只看一次回答

</ChapterIntroduction>

- **课堂内容**：Dify 应用、知识库导入、检索设置、workflow 和 API Key 安全
- **reference 借鉴**：`rag/dify`
- **动手任务**：为期末产品做一个知识库问答版本
- **配套实验**：[Lab 08：Dify 知识库](/course-b/labs/lab-08)
- **验收证据**：至少 10 条检索测试日志，包含 2 条失败样本和改进建议

---

## 第 9 周：RAG 入门

<ChapterIntroduction duration="2-3 小时" output="RAG 全链路拆解笔记 + 最小 RAG 脚本 + 测试日志" :tags="['RAG', 'Embedding', '向量检索', '最小实现']">

- 拆开 Dify 背后的 RAG 原理
- 实现或模拟文档切块、embedding、Top-K 检索和增强生成
- 用测试样本判断检索和回答是否正确

</ChapterIntroduction>

- **课堂内容**：Naive RAG、切块、向量相似度、上下文拼接、模型选型和评测
- **reference 借鉴**：`rag/rag-from-scratch`
- **动手任务**：实现一个最小 RAG 问答脚本
- **配套实验**：[Lab 09：最小 RAG](/course-b/labs/lab-09)
- **验收证据**：测试日志包含命中文档、回答结果、失败样本和分析

---

## 第 10 周：高级 RAG 与企业知识库

<ChapterIntroduction duration="2-3 小时" output="企业知识库架构 + RAG eval sheet + 改进对比记录" :tags="['高级 RAG', 'LlamaIndex', 'LangGraph', '知识治理', 'Eval']">

- 从最小 RAG 走向可治理、可评测、可追溯的企业知识库
- 理解知识域拆分、检索编排、证据化回答和版本治理
- 用评测样本证明一次 RAG 改进是否有效

</ChapterIntroduction>

- **课堂内容**：LlamaIndex、LangGraph、知识域、版本冲突、引用和拒答策略
- **reference 借鉴**：`rag/llama-index`、`rag/haystack`、`rag/graph-rag`
- **动手任务**：为自己的 RAG 做一次评测和一次改进
- **配套实验**：[Lab 10：企业知识库评测](/course-b/labs/lab-10)
- **验收证据**：改进结论必须由 eval sheet 支持

---

## 第 11 周：跨平台 PWA

<ChapterIntroduction duration="2-3 小时" output="可安装 PWA 原型 + 离线验证截图 + 平台决策矩阵" :tags="['PWA', '跨平台', 'Service Worker', 'Manifest']">

- 判断产品应该优先做 Web、PWA、小程序还是移动端
- 把普通网页改造成可安装、可离线打开的 PWA
- 识别平台能力、发布成本和维护成本

</ChapterIntroduction>

- **课堂内容**：PWA、manifest、service worker、平台选择矩阵、移动端体验检查
- **reference 借鉴**：`cross-platform/expo`、`cross-platform/taro`、`cross-platform/uni-app`
- **动手任务**：填写平台选择表，并做一个 PWA 最小版本
- **配套实验**：[Lab 11：PWA 跨平台](/course-b/labs/lab-11)
- **验收证据**：安装和离线证据齐全，平台选择和用户场景匹配

---

## 第 12 周：平台选择与小程序入门

<ChapterIntroduction duration="2-3 小时" output="可运行小程序前端 + 平台限制说明 + 开发者工具截图" :tags="['微信小程序', '开发者工具', 'Taro', 'uni-app']">

- 认识小程序适合什么场景
- 从账号、工具、页面结构到预览流程跑通一次
- 用 AI 辅助完成一个最小小程序前端

</ChapterIntroduction>

- **课堂内容**：小程序页面结构、开发者工具、Taro/uni-app 选择、平台限制
- **reference 借鉴**：`cross-platform/taro`、`cross-platform/uni-app`
- **动手任务**：完成一个可运行小程序前端页面
- **配套实验**：[Lab 12：小程序前端](/course-b/labs/lab-12)
- **验收证据**：至少一个页面能在开发者工具或替代环境运行

---

## 第 13 周：小程序后端

<ChapterIntroduction duration="2-3 小时" output="带云端数据流程的小程序版本 + 安全检查表" :tags="['微信云开发', 'CloudBase', '云函数', '云数据库', '云存储']">

- 理解哪些逻辑必须放在后端
- 用云函数、云数据库或替代后端支撑小程序核心流程
- 识别登录态、权限、支付签名和内容审核风险

</ChapterIntroduction>

- **课堂内容**：云开发、云函数、云数据库、文件上传、后端代理和安全规则
- **reference 借鉴**：Supabase 权限思想、Taro/uni-app 的跨端约束
- **动手任务**：给小程序补一条云端数据流程
- **配套实验**：[Lab 13：小程序后端](/course-b/labs/lab-13)
- **验收证据**：至少一条数据写入或读取流程在云端或替代后端跑通

---

## 第 14 周：小程序、移动端或 PWA 实现

<ChapterIntroduction duration="2-3 小时" output="跨平台最小产品版本 + 核心路径录屏 + 限制报告" :tags="['PWA', '小程序', '移动端', '核心路径']">

- 选择一个平台做最小实现
- 保留核心用户路径，不追求完整重写
- 验证跨平台版本和原 Web 产品的数据或功能关系

</ChapterIntroduction>

- **课堂内容**：最小迁移、平台 API、登录限制、接口适配和发布路径
- **reference 借鉴**：`expo`、`taro`、`uni-app`
- **动手任务**：做一个可演示的跨平台版本
- **配套实验**：[Lab 14：跨平台最小实现](/course-b/labs/lab-14)
- **验收证据**：至少一条核心流程能在目标平台跑通

---

## 第 15 周：Rules、Skills、MCP 与 Agent Team

<ChapterIntroduction duration="2-3 小时" output="项目 Agent 工作流 + 安全规则 + 一次执行 trace" :tags="['Rules', 'Skills', 'MCP', 'Agent Team', 'Human Gate']">

- 给最终项目写清楚 AI 工程规则
- 设计 Agent 能做什么、不能做什么、何时必须人工审批
- 把 Skills、MCP 和 Agent Team 用在真实项目交付上

</ChapterIntroduction>

- **课堂内容**：AGENTS.md、Skills、MCP 权限、Agent Team 分工、Human Gate、trace
- **reference 借鉴**：`spec-kit`、`mcp-servers`、`mcp-typescript-sdk`、`openai-agents-python`
- **动手任务**：为期末项目设计并验证一套 Agent 工作流
- **配套实验**：[Lab 15：Agent 工程规则](/course-b/labs/lab-15)
- **验收证据**：危险操作必须有 Human Gate，执行记录包含 diff、日志和复盘

---

## 第 16 周：期末答辩与技术评审

<ChapterIntroduction duration="答辩课" output="最终演示 + 技术报告 + 验证证据包 + 课程复盘" :tags="['Demo', '代码走查', '测试证据', '技术评审']">

- 展示完整 AI 全栈产品，而不仅是页面截图
- 解释 reference 借鉴、关键技术决策和验证证据
- 接受技术问答和同伴评审

</ChapterIntroduction>

- **课堂内容**：产品 demo、代码走查、AI/RAG 证据、跨平台证据、Agent 流程证据
- **配套实验**：[Lab 16：期末技术评审](/course-b/labs/lab-16)
- **验收证据**：答辩材料必须包含运行链接、测试日志、参考借鉴说明、风险边界和复盘

<SummaryCard title="16 周学习路径回顾" :sections="[
  { number: '1', title: '前端与工程基础', items: ['设计到代码、组件库、设计资产', 'CLI、Git 和 AI 工程流'] },
  { number: '2', title: '全栈产品闭环', items: ['Supabase、认证、权限、文件存储', 'AI API、支付、部署'] },
  { number: '3', title: 'RAG 与知识系统', items: ['Dify 平台 RAG、最小代码 RAG', '高级 RAG 评测与企业知识库设计'] },
  { number: '4', title: '跨平台与 Agent 交付', items: ['平台决策和最小跨平台版本', 'Rules、Skills、MCP、Agent Team 和最终答辩'] }
]" :outputs="[
  '一个完整 AI 全栈产品',
  '一套 RAG 或知识库验证证据',
  '一个跨平台最小版本或决策证明',
  '一套 Agent 工程交付记录'
]" />
