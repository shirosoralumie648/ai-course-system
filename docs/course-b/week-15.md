# 第 15 周：Rules、Skills、MCP 与 Agent Team

> 到了最后交付阶段，AI 不是"多叫几个 Agent 一起写"就会更可靠。真正重要的是把任务边界、审批点、工具权限和验证证据写清楚，让 Agent 帮你执行，但不能替你负责。

<ChapterIntroduction duration="2-3 小时" output="项目 Agent 工作流 + 安全规则 + 一次执行 trace" prerequisite="期末项目已有可运行版本" :tags="['Rules', 'Skills', 'MCP', 'Agent Team', 'Human Gate']">

- 给最终项目写清楚 AI 工程规则
- 设计 Agent 能做什么、不能做什么、何时必须人工审批
- 把 Skills、MCP 和 Agent Team 用在真实项目交付上

</ChapterIntroduction>

## 本周目标

1. 为期末项目写一份可执行的规则文件。
2. 设计一个小型 Agent Team，不超过 4 个角色。
3. 标注 Human Gate：哪些操作必须人工审批。
4. 记录一次真实执行 trace，能看出计划、改动、验证和人工判断。

## 为什么最后一周前要写规则

前 14 周我们一直在训练"用 AI 做产品"，但期末交付时最容易出问题的不是 AI 不会写代码，而是团队没有边界：

- AI 修改了认证、支付、RLS，却没有人工复核。
- Agent 跑完后说"测试通过"，但没有日志和命令。
- MCP 工具能读写过多目录，学生不知道它碰了哪些文件。
- 多个 Agent 同时改同一批文件，最后靠手工猜测合并。
- 为了赶进度，把失败测试删掉或把错误状态藏起来。

Rules、Skills、MCP 和 Agent Team 的共同目标，是把这些隐性风险变成显性协议。它们不是"高级玩法"，而是期末项目的交付纪律。

## reference 拆解

| 参考项目 | 读什么 | 借鉴到课堂 |
|---|---|---|
| `reference/repos/agentic-coding/spec-kit/README.md` | constitution、spec、plan、tasks、implement、analyze/checklist 的链路 | 把期末项目从聊天式开发改成规格驱动交付 |
| `reference/repos/mcp/mcp-servers/README.md` 与 `src/*/README.md` | filesystem、git、fetch、memory、time 等 server 如何定义工具边界 | 设计"工具能做什么，不能做什么" |
| `reference/repos/mcp/mcp-typescript-sdk/README.md` | tools、resources、prompts、stdio/HTTP、server/client 的接口形态；注意本地 README 标注 v2 仍是 pre-alpha | 给自己的 MCP 设计写输入、输出、错误处理和版本边界 |
| `reference/repos/ai-engineering/openai-agents-python/docs/guardrails.md`、`handoffs.md`、`tracing.md` | guardrail、handoff、trace 的教学概念 | 设计角色边界、交接记录、人工介入和可审计轨迹 |

### Reference 借鉴卡

- 来源：`spec-kit`、`mcp-servers`、`mcp-typescript-sdk`、`openai-agents-python`
- 它解决的问题：让 AI 工程从"聊天请求"变成可检查、可审批、可追踪的流程。
- 可借鉴做法：规格先行、工具最小权限、角色交接、guardrail、trace。
- 我们课程中的用法：为自己的期末项目写 `AGENTS.md`、Human Gate、MCP 工具卡和执行 trace。
- 学生任务：用自己的项目复现这些思路，提交规则文件和一次真实执行记录。
- 不要照搬：不要要求实现完整 SDK 或生产级 Agent 框架；MCP TypeScript SDK 本地 README 提醒 v2 仍在开发中，课堂只借鉴接口思维。

本卡不是让你复制源码，而是训练你从成熟项目中提取可迁移的工程判断。

## AGENTS.md 最小规则文件

一份合格的规则文件不需要很长，但必须能约束行为。下面是期末项目可直接改写的结构：

```markdown
# AGENTS.md

## 项目目标
- 本项目是：一句话说明产品、用户、核心路径。
- 本周交付边界：只允许围绕期末验收修复和补证据，不做新大功能。

## 允许 AI 做的事
- 修改指定目录内的前端页面、API route、测试和文档。
- 生成小步计划，列出将修改的文件。
- 运行本地测试、构建、lint，并保存命令输出。

## 必须人工审批的事
- 删除文件、大规模重构、安装依赖、修改 lockfile。
- 修改认证、支付、RLS、webhook、生产环境变量。
- 读取或处理 API Key、Token、密码、真实用户数据。
- 跳过测试、删除失败用例、把失败测试标记为通过。

## 验证要求
- 每次实现后记录：命令、结果、失败原因或通过证据。
- 最终答辩前必须有：运行截图、测试日志、AI 调用/RAG eval 证据、人工 review 记录。
```

不合格的规则文件通常只写"保证质量、注意安全、认真测试"。这些话不能执行，也不能审计。

## Agent Team 最小设计

| 角色 | 输入 | 输出 | 不能做什么 | Human Gate |
|---|---|---|---|---|
| Planner | 需求、当前代码状态、限制 | 小步计划和验收标准 | 不能直接改代码 | 计划超过 6 个文件时需审批 |
| Coder | 已审批计划、允许修改范围 | diff 和实现说明 | 不能改密钥、账单、生产配置 | 碰认证/支付/权限立即停止 |
| Tester | 测试命令、验收标准 | 测试日志和失败分析 | 不能把失败测试改成通过 | 测试失败但仍想交付时需审批 |
| Reviewer | diff、测试日志、需求 | 风险清单和是否通过建议 | 不能代替人类最终批准 | 高风险问题必须人工判定 |

如果团队只有一个人，也可以用这四个角色管理自己的工作：先计划，再实现，再验证，再复核。角色是思考边界，不一定是四个真实 Agent。

## MCP 工具权限表

MCP 的教学重点不是"连上越多工具越好"，而是每个工具都要有输入、输出、权限和失败处理。

| 工具 | 可以做什么 | 禁止做什么 | 失败模式 | 人工审批 |
|---|---|---|---|---|
| filesystem | 读取/修改指定项目目录 | 读取家目录、系统目录、`.env`、密钥文件 | 改错文件、覆盖用户修改 | 写入前列文件清单 |
| git | 查看 diff、status、log | 强制 reset、删除历史、覆盖分支 | 混入无关改动 | revert/reset 必须审批 |
| fetch | 访问公开文档或测试接口 | 请求内部系统、带密钥请求第三方 | 网络失败、返回不稳定 | 涉及真实用户或账单需审批 |
| database | 读取测试库、执行迁移草案 | 操作生产库、导出隐私数据 | RLS 绕过、误删数据 | 写操作必须审批 |
| payment | 读取测试模式状态 | 触发真实扣费、改生产 webhook | 金额错误、状态不同步 | 必须使用测试模式并保留日志 |

课堂可以要求学生不实现 MCP server，只提交"MCP 工具卡"。如果已经实现工具，必须提交一次调用 trace 和权限说明。

## 一次合格的执行 trace

trace 不是聊天截图，而是能审计的工作记录。

```markdown
## Week 15 Agent Trace

### 1. 任务
- 目标：修复 RAG 问答页空状态，并补充一条失败样本测试。
- 允许文件：`app/rag/page.tsx`、`tests/rag-empty-state.spec.ts`
- 禁止事项：不改数据库 schema，不改生产 env，不安装依赖。

### 2. Agent 计划
- Step 1：阅读页面和现有测试。
- Step 2：添加空状态 UI。
- Step 3：添加失败样本测试。
- Step 4：运行 `npm test -- rag-empty-state`。

### 3. 人工审批
- 审批人：
- 审批结论：允许修改上述两个文件。
- 补充限制：不要改 RAG 检索逻辑。

### 4. 执行结果
- 修改文件：
- 关键 diff：
- 测试命令：
- 测试结果：

### 5. Review
- 风险：
- 是否需要二次修复：
- 最终结论：
```

合格 trace 能回答三个问题：AI 被允许做什么，AI 实际做了什么，人类在哪里做了判断。

## 课堂练习：把一个模糊请求改成可执行任务

原始请求：

> 帮我把项目优化一下，顺便让 AI 功能更稳定。

课堂改写：

```markdown
目标：修复 AI 问答页在接口失败时没有错误提示的问题。
允许范围：`app/api/chat/route.ts`、`app/chat/page.tsx`、`tests/chat-error.spec.ts`
验收标准：
1. API 返回 500 时，前端显示可理解的错误消息。
2. 用户可以重新提交。
3. 测试覆盖失败返回。
4. 不修改模型供应商、数据库 schema、支付或认证。
Human Gate：如果需要新增依赖或修改 env，先停止并询问。
```

这就是 Rules 的价值：把"优化一下"变成可验证的小步任务。

## 实验任务

为你的期末项目提交：

1. `AGENTS.md` 或等价规则文件。
2. Agent Team 角色表。
3. Human Gate 清单。
4. MCP 工具卡：至少 2 个工具，写清输入、输出、权限、失败模式。
5. 一次执行 trace：计划、diff、测试日志、人工审批记录。

## 验收标准

- 规则具体到可执行，不写"保证质量"这种空话。
- Agent 角色少而清晰。
- Human Gate 覆盖危险操作。
- MCP 工具卡体现最小权限。
- trace 能说明 AI 做了什么、人做了什么、验证了什么。
- 没有要求 AI 接触真实密钥、真实账单或生产数据。

## 参考借鉴说明模板

```markdown
## Week 15 参考借鉴说明

- 参考项目：
- 阅读范围：
- 我借鉴的 Agent 工程做法：
- 我在项目中的规则/角色/工具设计：
- Human Gate：
- MCP 工具卡：
- 执行 trace：
```

## 本周回顾

本周的核心不是让 Agent 变多，而是让责任边界变清楚。一个可信的 AI 工程工作流应该能被复盘：谁提出任务，谁批准边界，工具有什么权限，AI 产生了哪些改动，验证证据在哪里，人类最终判断了什么。
