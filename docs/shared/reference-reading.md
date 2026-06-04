# 参考项目读法：把 reference 变成课程内容

`reference/` 不是给学生直接照抄的大仓库，也不是教师备课时随手看的链接库。它在本课程里有一个明确作用：用真实项目和经典材料纠正课程边界，补足课堂 Demo、作业任务和验收标准。

## 四种进入课程的方式

| 进入方式 | 用在什么地方 | 产出是什么 |
|---|---|---|
| 纠正课程边界 | 课程首页、教学日历、每周目标 | 明确本周到底训练产品、工程、RAG、跨平台还是 Agent 能力 |
| 补课堂 Demo | 每周教程的演示环节 | 从参考项目抽一个小片段，改写成可讲、可跑、可截图的课堂示例 |
| 补作业任务 | 实验、课后作业、期末项目 | 让学生阅读一个局部文件或结构，提炼一个可复用做法 |
| 补验收证据 | rubric、最终报告、答辩 | 要求学生提交 diff、测试日志、调用截图、RAG 测评表或参考借鉴说明 |

## 教师怎么读 reference

每次备课只读一个小切面，不追求跑完整仓库。

1. 先看 `README`、目录结构、示例入口和测试命令。
2. 再选 1-3 个能支撑本周目标的文件或页面。
3. 把真实项目做法改写成本课程自己的小例子。
4. 写清楚学生要借鉴的是结构、流程、接口边界、验收方式还是错误处理。
5. 如果参考项目太复杂，只保留最小思想，不把复杂依赖带进课堂。

## 学生怎么读 reference

学生不需要克隆或运行大型生产项目。默认作业形式是"局部阅读 + 证据摘取 + 自己项目改造"。

| 必交内容 | 要求 |
|---|---|
| 阅读范围 | 写明读了哪个参考项目、哪个目录或哪个文件 |
| 可借鉴点 | 用自己的话说明一个结构、流程、接口或验收方法 |
| 本课改造 | 说明如何把它简化到自己的课程项目里 |
| 验证证据 | 提交截图、运行命令、测试日志、diff 或人工走查记录 |
| 边界说明 | 说明没有照抄什么，为什么不能直接搬生产代码 |

## 课程 A：产品原型 + Claude Code

课程 A 面向非计算机专业学生，所以 reference 的主要作用不是增加技术深度，而是把"产品原型"和"AI 协作流程"讲得更真实。

| 周次 | 参考来源 | 加进课程的方式 |
|---|---|---|
| Week 01-02 | `courses/web-dev-for-beginners`、`fullstack-ai/vercel-ai-chatbot` | 用小型 starter app 和截图帮助学生理解"能跑起来"是什么 |
| Week 03 | `agentic-coding/anthropic-courses`、`agentic-coding/aider` | 增加 chatbot、AI IDE、coding agent 的对比练习和 diff 审查 |
| Week 04-05 | The Mom Test、Continuous Discovery Habits、Sprint、Shape Up | 强化访谈脚本、坏问题示例、需求筛选标准 |
| Week 06-08 | `fullstack-ai/vercel-ai-chatbot`、`ai-engineering/openai-cookbook`、`fullstack-ai/supabase` | 给原型增加 mock mode、真实 API 调用和安全验证路径 |
| Week 09-10 | `agentic-coding/spec-kit`、Agent Skills 课程 | 把流程建议改成检查清单，并让学生做一个小 Skill |
| Week 11 | `mcp/mcp-servers`、`mcp/mcp-typescript-sdk` | 先设计最小 MCP 工具接口，再讨论真实接入 |
| Week 12-14 | `agentic-coding/spec-kit`、Software Engineering at Google、Google SRE | 增加完成证明、验证日志、spec-to-plan-to-diff 练习 |
| Week 15-16 | `ai-engineering/openai-agents-python`、`agentic-coding/browser-use`、`rag/langgraph` | 用角色边界、handoff 和 trace 解释 Agent Teams |

## 课程 B：AI 全栈产品工程

课程 B 面向有编程基础的学生，reference 要直接进入技术路线、课堂 Demo、项目验收和答辩证据。

| 模块 | 参考来源 | 加进课程的方式 |
|---|---|---|
| 前端与设计系统 | `fullstack-ai/shadcn-ui`、`courses/web-dev-for-beginners` | 组件规范、设计 token、UI before/after 评审 |
| CLI、Git 与 AI 编程 | `courses/missing-semester`、`agentic-coding/aider`、`agentic-coding/gemini-cli` | shell/git 训练、工具对比、diff 与测试日志 |
| AI 应用集成 | `fullstack-ai/vercel-ai`、`fullstack-ai/vercel-ai-chatbot`、`ai-engineering/openai-cookbook` | streaming、后端 AI route、tool calling、安全密钥边界 |
| Supabase 后端 | `fullstack-ai/supabase` | schema、RLS、storage、edge function 的课堂样例 |
| 支付与部署 | Stripe samples、`production-apps/dub` | checkout、subscription、webhook、后端持有 price ID |
| RAG 与知识库 | `rag/dify`、`rag/rag-from-scratch`、`rag/llama-index`、`rag/haystack`、`rag/graph-rag` | Dify 平台 RAG、最小代码 RAG、rerank、eval、graph retrieval |
| 跨平台 | `cross-platform/expo`、`cross-platform/taro`、`cross-platform/uni-app` | Web、PWA、小程序、移动端的决策矩阵和最小实现 |
| Agent 工程 | `agentic-coding/spec-kit`、`mcp/mcp-servers`、`mcp/mcp-typescript-sdk`、`ai-engineering/openai-agents-python` | rules、skills、MCP、Agent team、human gate、trace |

## 不能做什么

- 不把 reference 当成复制粘贴素材库。
- 不要求学生运行大型生产仓库。
- 不复制第三方长文本到课程页面。
- 不把 Course A 讲成 full-stack 课。
- 不把 Course B 退回纯 Agentic Development 课。
- 不接受"参考了某项目"这种空话，必须说明读了哪里、借鉴了什么、怎么改造、如何验证。

## 一次 reference 阅读课怎么上

这套流程适合 20-30 分钟课堂片段，也适合课后作业。

| 时间 | 教师动作 | 学生动作 | 产出 |
|---|---|---|---|
| 0-3 分钟 | 说明本周为什么看这个 reference | 记录本周目标 | 阅读目标 |
| 3-8 分钟 | 展示目录结构或关键页面 | 标出自己看懂的 3 个文件/模块 | 结构标注 |
| 8-15 分钟 | 拆一个具体做法 | 回答"它解决什么问题" | 借鉴点 |
| 15-22 分钟 | 改写成本课程小例子 | 写自己的简化方案 | 改造方案 |
| 22-30 分钟 | 给出验收证据要求 | 补截图、日志、diff 或表格 | 可审计提交 |

课堂不要把时间花在解释整个大型项目。只要学生能从一个真实项目里读出一个可迁移做法，并把它落到自己的作业里，这次 reference 阅读就有效。

## 教师备课四步

### 1. 选切面

不要说"本周参考 Supabase"这种大范围要求。要写成可执行切面：

| 太大 | 可执行 |
|---|---|
| 参考 Supabase | 看 Supabase auth/RLS 示例，提炼"用户只能看自己的数据"的验收方式 |
| 参考 Dify | 看知识库导入和检索测试流程，做 10 条 eval 表 |
| 参考 shadcn/ui | 看 Button/Form/Card 的组件命名和 variant 设计 |
| 参考 OpenAI Cookbook | 看 structured output 或 tool calling 的一个示例，改成课堂小 API |

### 2. 抽结构

教师要从 reference 中抽出结构，而不是抽长文本：

- 文件结构：哪些目录支撑这个能力？
- 数据结构：哪些字段是核心？
- 接口结构：输入、输出、错误是什么？
- 流程结构：先做什么，再做什么，哪里需要人工确认？
- 验证结构：它如何证明功能可用？

### 3. 改成课程例子

真实项目通常有大量生产复杂度，课堂必须降维：

| 生产项目能力 | Course A 改写 | Course B 改写 |
|---|---|---|
| 完整账号体系 | 解释为什么要登录，先用 mock 用户 | 接 Supabase auth/RLS |
| 支付和 webhook | 讲清楚金额不能信前端 | 做 Stripe sandbox 或支付模拟 |
| 大规模 RAG pipeline | 看检索和引用是什么 | 做 eval sheet 和最小 RAG |
| 多 Agent orchestration | 画角色边界和 handoff | 写 rules、trace、human gate |

### 4. 定证据

每次 reference 作业都必须落到证据，不然学生会写空话。

| 借鉴类型 | 证据 |
|---|---|
| UI/组件 | before/after 截图、组件复用说明 |
| CLI/Git | 命令记录、diff、commit |
| 数据库 | schema 截图、CRUD 走查 |
| 权限 | 登录/未登录/越权测试 |
| AI API | real-call 日志、错误处理截图 |
| RAG | eval 表、失败样本、改进前后对比 |
| 跨平台 | 平台决策矩阵、运行截图 |
| Agent 工程 | 计划、diff、测试日志、human gate |

## 学生阅读四问

学生每次看 reference，只回答四个问题：

1. **它解决什么问题？** 不要先讲技术名词，先说场景。
2. **它怎么组织？** 看目录、文件、页面、接口或流程。
3. **我能借哪一点？** 只能选一个点，不要贪多。
4. **我怎么证明借鉴有效？** 交截图、diff、日志、表格或走查记录。

## reference 读法示例

### 示例 1：从 shadcn/ui 借组件约束

**阅读范围**

- 组件文档或组件目录
- Button、Card、Form 中任选一个

**可借鉴点**

组件不是复制一段代码，而是统一命名、状态、尺寸和变体。

**课堂改写**

让学生把两个 AI 生成页面里样式不一致的按钮统一成三种状态：

| 状态 | 用法 |
|---|---|
| primary | 页面主动作 |
| secondary | 次要动作 |
| destructive | 删除、清空、取消危险操作 |

**学生提交**

- 修改前截图
- 修改后截图
- 哪些按钮被统一
- 统一后是否影响核心流程

### 示例 2：从 Supabase 借权限验收

**阅读范围**

- auth/RLS 示例
- storage 权限示例

**可借鉴点**

权限不是"前端不显示按钮"，而是后端或数据库层拒绝非法访问。

**课堂改写**

让学生为自己的产品写一张权限表：

| 用户状态 | 能做什么 | 不能做什么 | 怎么验证 |
|---|---|---|---|
| 未登录 | 看公开页 | 看个人数据 | 访问受保护页面 |
| 已登录用户 A | 看自己的记录 | 看用户 B 的记录 | 换账号测试 |
| 管理员 | 管理内容 | 直接改支付状态 | 审批流程 |

**学生提交**

- 权限表
- 至少一次拒绝访问截图
- 说明哪些权限暂时用 mock 表示

### 示例 3：从 Vercel AI Chatbot 借 AI 产品结构

**阅读范围**

- 对话页面结构
- API route 或 server action
- 消息数据结构

**可借鉴点**

AI 产品不是一个输入框，而是输入、上下文、生成、历史、错误和反馈的组合。

**课堂改写**

Course A：只保留输入、输出、历史记录和错误提示。

Course B：补后端 AI endpoint、数据库历史、真实调用日志和失败处理。

**学生提交**

- 对话流程图
- mock/real-call 状态说明
- 真实调用或 mock 边界证据

### 示例 4：从 Dify 借 RAG 评测

**阅读范围**

- 知识库导入流程
- 检索设置
- workflow 测试方式

**可借鉴点**

RAG 不能靠"问一次觉得还行"验收，必须有问题集、预期依据、检索片段和失败分析。

**课堂改写**

学生用 10 个问题测自己的知识库：

| 问题 | 期望依据 | 检索片段 | 回答 | 通过 | 失败原因 |
|---|---|---|---|---|---|

**学生提交**

- 10 条 eval
- 2 条失败样本
- 一次改进前后对比

### 示例 5：从 spec-kit 借规格驱动

**阅读范围**

- spec、plan、task 的组织方式
- 验收标准写法

**可借鉴点**

AI 编程任务不能只写"帮我优化"，要写清楚目标、范围、不做什么、验收标准。

**课堂改写**

```markdown
## 小任务 spec

- 目标：
- 允许修改：
- 禁止修改：
- 验收标准：
- 验证命令：
- 人工审查点：
```

**学生提交**

- spec
- AI 计划
- diff
- 验证记录

### 示例 6：从 MCP servers 借工具边界

**阅读范围**

- 一个 MCP server 的 tool 定义
- 输入输出 schema
- 错误处理方式

**可借鉴点**

工具必须有明确输入、输出、权限和失败处理，不能只写"让 AI 查数据库"。

**课堂改写**

```markdown
## MCP 工具设计

- 工具名：
- 使用场景：
- 输入：
- 输出：
- 可能错误：
- 是否需要人工审批：
- 不允许做什么：
```

**学生提交**

- 2 个工具设计
- 每个工具一个风险说明

## 教师不要直接照搬的内容

| reference 中常见内容 | 为什么不直接搬 | 课程化处理 |
|---|---|---|
| 大量源码 | 学生会迷失在框架细节 | 只抽目录结构和一个局部示例 |
| 完整生产配置 | 环境复杂，课堂不可控 | 改成伪配置或教师演示 |
| 第三方长文档 | 版权和可读性问题 | 用自己的话总结，不长引用 |
| benchmark 结果 | 可能过时，且学生无法复现 | 改成本课程小样本评测 |
| 企业级架构图 | 太抽象 | 改成学生项目的一页架构 |

## 分层要求：Course A 与 Course B 不同

| 能力 | Course A 要求 | Course B 要求 |
|---|---|---|
| 前端 | 能演示核心流程 | 组件复用、响应式、状态完整 |
| 数据 | 可用 mock 说明未来数据 | 真实数据库、CRUD、权限 |
| AI API | 可用 mock 或教师演示真实调用 | 后端封装、真实调用、错误处理 |
| RAG | 理解知识库/检索概念 | Dify、最小 RAG、eval、失败分析 |
| 跨平台 | 说明用户在哪个平台 | 决策矩阵和最小实现 |
| Agent | 角色边界和人工接管 | rules、skills、MCP、trace、human gate |

## 教师课前准备模板

```markdown
## 本周 reference 备课卡

- 本周课程：
- 本周能力目标：
- 选择的 reference：
- 阅读范围：
- 我抽取的真实项目做法：
- 我改写成的课堂 Demo：
- 学生需要完成的最小任务：
- 学生提交的证据：
- 不要求学生做的生产级复杂度：
```

## 学生课后提交模板

```markdown
## 本周 reference 借鉴说明

- 本周主题：
- 参考项目/材料：
- 阅读范围：
- 我看到的真实项目做法：
- 我借鉴的一个点：
- 我如何改造到自己的项目：
- 我没有照抄的部分：
- 验证证据：
- 下一步还需要补的能力：
```

## 评分用快速检查表

教师批改时只看四件事：

| 检查项 | 不合格 | 合格 | 优秀 |
|---|---|---|---|
| 阅读范围 | 只写项目名 | 写到目录/文件/页面 | 能解释为什么选这个范围 |
| 借鉴点 | 空泛描述 | 有一个具体做法 | 能说明解决了什么课程问题 |
| 改造方式 | 直接照抄或没改 | 简化到自己项目 | 能说明取舍和边界 |
| 验证证据 | 无证据 | 有截图/日志/diff | 有失败样本或前后对比 |

## 统一提交模板

```markdown
## 参考借鉴说明

- 参考项目：
- 阅读范围：
- 我借鉴的做法：
- 我在自己项目中的简化/改造：
- 验证证据：
- 没有直接照抄的部分：
```
