# 课程设计书：Agentic Development：AI 原生软件工程实践

## 1. 课程基本信息

| 项目 | 内容 |
| --- | --- |
| 课程名称 | Agentic Development：AI 原生软件工程实践 |
| 课程对象 | 计算机、软件工程、人工智能、数据科学等有编程基础的学生 |
| 建议学时 | 12 周，每周 2-3 学时 |
| 课程类型 | 项目制 / 实验驱动 / 软件工程实践课 |
| 先修要求 | Python 或 JavaScript 基础、Git 基础、终端基础、基本软件工程意识 |

本课程面向已经具备基本编程能力的学生。课程不以讲授某个工具的菜单功能为目标，而是训练学生把 Coding Agent 纳入可控、可验证、可审查的软件工程流程。

## 2. 课程背景

AI 编程工具已经从 Chatbot 和 Copilot 发展到 Coding Agent。早期 AI 工具主要回答问题、解释代码、生成片段或补全局部代码；现在的 Coding Agent 已经能够读取代码库、修改文件、运行命令、调用工具、生成计划、记录结果，并在一定程度上参与完整开发任务。

这种变化使软件工程教学面临新的问题。学生不能只学习“让 AI 写代码”，也不能把 Agent 当作不需要监督的自动程序员。真实软件工程中，Agent 的输出会影响代码库结构、测试结果、依赖、权限、文档、安全边界和团队协作。如果没有上下文、规则、权限、测试、Review、CI 和 Human Gate，Agent 可能误解需求、扩大修改范围、编造测试结果、泄漏敏感信息，甚至破坏项目结构。

因此，本课程要解决的核心问题是：如何设计、约束、验证和审查 Agent，使它成为工程流程中的受控协作者，而不是不可审计的代码生成器。

## 3. 课程定位

本课程不是普通 Prompt Engineering。学生不会只学习提示词模板，而是学习任务包、上下文工程、项目规则、可复用 Skill、MCP 工具接入、Agent Team 分工、测试验证和 Review 证据。

本课程不是工具演示课。Claude Code、Codex、Skill、MCP 和 Agent Team 都是教学对象，但课程重点不是展示工具有多强，而是让学生知道工具何时可用、何时不可靠、如何设置边界、如何验证结果。

本课程不是“AI 自动写代码”宣传课。课程强调人工判断、测试证据、权限边界和失败记录。工具输出“完成”不等于任务完成，测试通过也不等于工程风险消失。

本课程不是无测试无审查的 Demo 课。每个核心实验都要求保留任务输入、Agent 计划、实际 diff、测试日志、Review 记录和复盘。

本课程真正训练以下能力：

- Agentic Development 思维：把 AI 视为需要流程约束的工程协作者。
- Coding Agent 使用：能用 Claude Code / Codex 完成受控代码任务。
- 上下文工程：能组织任务背景、相关文件、错误日志、规则边界和验收标准。
- 项目规则文件：能编写 `CLAUDE.md` / `AGENTS.md` 等可执行规则。
- Skill：能把可复用流程固化为结构化能力单元。
- MCP：能理解和设计 Agent 的工具与资源接入边界。
- Agent Team：能设计 Planner、Coder、Tester、Reviewer 与 Human Gate 的协作流程。
- 测试、Review、CI：能用工程证据验证 Agent 输出。
- 工程交付和复盘：能说明过程、风险、失败和改进点。

## 4. 学情分析

学生进入本课程时通常有三类问题。

第一类是不会安装和配置工具。学生可能已经使用过网页端 AI 工具，但未必能在本地配置 Git、Python、Node.js、Claude Code、Codex、测试命令和仓库权限。若环境准备不足，课堂实验会变成安装排错课。

第二类是不知道哪些任务可以让 AI / Agent 代劳。学生容易把所有任务都交给 AI，也可能只把 AI 当作聊天工具。两种情况都会妨碍学生建立正确的任务分配意识。

第三类是不知道如何让 Agent 按工程要求完成任务。学生常见做法是输入“帮我修一下 bug”，然后接受工具输出。这样的任务没有目标、上下文、允许范围、禁止范围、测试命令、验收标准和 Human Gate，难以保证质量。

对应教学策略如下：

- 环境检查：第 1-2 周完成基础工具检查，允许教师准备替代流程。
- AI / Agent 可代劳任务地图：帮助学生区分理解、规划、编码、测试、审查、文档、自动化和工作流任务。
- Task Packet 训练：要求学生用结构化任务包描述目标、上下文、边界、测试和验收标准。
- Lab 驱动：用小型 bugfix、功能修改、规则文件和 Review Skill 训练可操作能力。
- Rubric 约束：让学生知道评分看过程证据，而不是只看最终代码。
- Human Gate 意识：所有高风险操作必须人工确认，包括删除文件、修改依赖、访问外部服务、处理密钥和发布版本。

## 5. 教学目标

### 5.1 知识目标

学生应能够：

- 理解 Chatbot、Copilot、Coding Agent、Agentic Workflow 的区别。
- 理解 Context Engineering、Rules、Skill、MCP、Subagent、Human Gate 的含义和边界。
- 理解测试、Review、CI 和人工审批在 Agentic Development 中的作用。
- 理解权限、安全、密钥、外部工具和 prompt injection 的基本风险。

### 5.2 能力目标

学生应能够：

- 使用 Claude Code / Codex 完成受控代码任务。
- 编写具体、可执行、可审查的 `CLAUDE.md` / `AGENTS.md`。
- 设计包含触发条件、输入、步骤、输出和禁止行为的 Skill。
- 设计 MCP 使用方案，说明工具、资源、输入输出和安全边界。
- 设计 Agent Team 工作流，明确 Planner、Coder、Tester、Reviewer 和 Human Gate 的职责。
- 运行测试、审查 diff、记录测试日志、写 Review 和复盘。
- 在 Agent 输出不可靠时提出修正、拒绝或回滚方案。

### 5.3 素养目标

学生应形成以下工程素养：

- 不迷信 AI 输出，能区分 Agent 建议和人工判断。
- 有工程验证意识，知道没有测试证据就不能声称完成。
- 有权限和安全意识，不把密钥、隐私数据和高风险操作交给 Agent 默认处理。
- 有审计和复盘意识，能保留过程证据并分析失败模式。

## 6. 课程内容结构

| 周次 | 教学主题 | 核心问题 | 实验任务 | 交付物 |
| --- | --- | --- | --- | --- |
| 第 1 周 | AI 原生软件工程导论 | Coding Agent 与 Chatbot / Copilot 有什么区别？为什么 Agent 必须进入工程流程？ | 观察 Agent 分析任务，编写自己的 Task Packet | 概念对比表、Task Packet、课堂观察记录 |
| 第 2 周 | Claude Code 基础 | 如何让 Claude Code 阅读项目、提出计划、修复 bug 并留下证据？ | Lab 01：Claude Code Bugfix | 实验记录、失败和通过测试日志、Git diff、复盘 |
| 第 3 周 | Codex 基础 | 如何使用 Codex 完成小功能修改，并理解 sandbox 与 approval？ | Lab 02：Codex Code Change | 任务说明、Codex 输出摘要、diff、测试结果、工具对比记录 |
| 第 4 周 | Context Engineering | 什么上下文能提升 Agent 质量？上下文过多或过少会怎样？ | 为 Lab 01 或 Lab 02 编写 context-pack | `context-pack.md`、Agent 响应对比记录 |
| 第 5 周 | `CLAUDE.md` / `AGENTS.md` / Rules | 如何把工程规则写成 Agent 可执行的项目协议？ | Lab 03：Project Rules | `CLAUDE.md`、`AGENTS.md`、规则对比记录、复盘 |
| 第 6 周 | 权限、Hooks 与安全边界 | 哪些操作必须 Human Gate？如何处理命令、文件、网络和依赖边界？ | 设计危险操作审批清单 | 权限边界说明、审批清单、失败处理流程 |
| 第 7 周 | Skill 设计 | Skill 与普通 Prompt 有何区别？如何固化可复用流程？ | Lab 04：Code Review Skill | `code-review/SKILL.md`、原始 Review、人工修订 Review、复盘 |
| 第 8 周 | MCP 原理与使用 | MCP 如何为 Agent 提供工具和资源？工具输出为什么不能默认可信？ | 设计课程资料检索和作业查询场景 | MCP 学习记录、工具调用场景、风险清单 |
| 第 9 周 | 自定义 MCP Server | 如何设计 tools、resources、prompts 和权限边界？ | 补充课程 MCP Server 工具设计 | 工具设计、资源设计、Prompt 设计、安全说明 |
| 第 10 周 | Subagents 与 Agent Team | 多 Agent 协作如何分工？如何避免责任不清和越权？ | 设计期末项目 Agent Team 工作流 | 角色说明、流程图、Human Gate 清单、风险点 |
| 第 11 周 | 测试、Review 与 CI | 如何把 Agent 输出纳入质量门禁？ | 设计测试、Review 和 CI 证据链 | 测试计划、Review checklist、CI 方案、风险说明 |
| 第 12 周 | 期末项目答辩 | 如何展示一个可审计的 AI 原生软件工程工作流？ | 期末项目展示与答辩 | 项目仓库、规则文件、Skill、MCP 设计、Agent Team、报告和演示 |

## 7. 教学方法

本课程采用问题驱动、案例演示、工具实操、Lab 训练、过程记录、Peer Review、Rubric 评价和复盘反思相结合的方式。

- 问题驱动：每周以一个工程问题开场，例如“为什么 Agent 不能直接合并代码”。
- 案例演示：教师用小型项目展示 Agent 如何计划、修改、测试和失败。
- 工具实操：学生在真实仓库中使用 Claude Code、Codex、Git 和测试命令。
- Lab 训练：用 Lab 01-04 形成最小教学闭环。
- 过程记录：所有实验保留 prompt、计划、diff、测试、Review 和复盘。
- Peer Review：学生互相检查 Task Packet、规则文件和 Review 报告。
- Rubric 评价：助教按统一评分表检查可审计证据。
- 复盘反思：每个实验都要求说明 Agent 做对了什么、错了什么、人工如何判断。

## 8. 实验体系

Lab 01-04 是课程第一阶段的核心实验，作用如下：

- Lab 01：Claude Code Bugfix。训练学生让 Claude Code 分析失败测试、提出计划、修复小型 bug、运行测试并审查 diff。
- Lab 02：Codex Code Change。训练学生用 Codex 完成小功能开发，理解 sandbox、approval、测试新增和原有行为保护。
- Lab 03：Project Rules。训练学生编写 `CLAUDE.md` / `AGENTS.md`，把项目目标、目录、测试命令、允许范围、禁止范围和 Human Gate 固化为规则。
- Lab 04：Code Review Skill。训练学生把代码审查流程封装成 Skill，并对 Agent 生成的 Review 做人工修订。

后续 Lab 05-08 可规划为：权限与 Hook 设计、MCP 使用与风险分析、自定义 MCP Server 设计、Agent Team 工作流演练。当前阶段只保留规划，不展开完整实验，避免在第 1 阶段材料中扩大范围。

## 9. 考核方式

| 项目 | 比例 | 评价方式 |
| --- | --- | --- |
| 平时实验 | 35% | 依据 Lab Rubric 评价 Lab 01-04，重点看任务描述、过程记录、diff 审查、测试证据、Human Gate 和复盘 |
| 阶段作业 | 20% | 评价规则文件、context-pack、Skill 设计、MCP 设计草案和 Agent Team 草案，重点看结构完整性和工程边界 |
| 期末项目 | 35% | 评价完整 Agentic Workflow，包含仓库、规则文件、Skill、MCP 设计、Agent Team、测试/Review/CI 证据和答辩 |
| 课堂参与与复盘 | 10% | 评价课堂讨论、同伴互评、风险识别、失败记录和复盘质量 |

评分不只看最终结果。若学生代码能运行但没有测试日志、diff 审查和人工判断，不能获得高分。若工具不可用但学生如实记录环境问题、完成替代流程并保留证据，可按替代流程评分。

## 10. 期末项目

期末项目题目：构建一个 AI 原生软件工程工作流。

学生需要选择一个小型软件项目或课程提供的示例项目，构建一套可审计的 Agentic Workflow。项目不要求规模大，但必须体现真实工程流程。

期末项目交付物包括：

- 项目仓库或可复查代码目录。
- 项目级 `CLAUDE.md` / `AGENTS.md`。
- 至少 1 个 Skill。
- 至少 1 个 MCP 配置或 MCP Server 设计文档。
- 至少 3 个 Agent / Subagent 角色设计。
- 测试命令、测试日志或 CI 结果。
- Review 报告和风险清单。
- Human Gate 清单。
- 演示材料和技术复盘。

评分维度包括：

- 工作流完整性：是否覆盖计划、实现、测试、Review、审批和复盘。
- 规则可执行性：规则是否具体，是否能限制 Agent 行为。
- 验证证据：是否有真实测试、diff、Review 和 CI 或替代验证。
- 安全边界：是否处理权限、密钥、外部服务、依赖和高风险操作。
- 复盘质量：是否能说明失败、权衡、改进和人工判断。

## 11. 教学资源

本课程可使用以下资源：

- 示例项目：`examples/repo-01-small-bugfix/`、`examples/repo-02-feature-development/`。
- Lab 文档：`labs/lab-01-claude-code-bugfix.md` 至 `labs/lab-04-code-review-skill.md`。
- 模板：`templates/` 中的 README、规则文件、Skill 和最终报告模板。
- filled examples：`templates/filled-examples/` 中的 `CLAUDE.example.md`、`AGENTS.example.md`、`SKILL.example.md`。
- Skill 示例：`skills/code-review/SKILL.md`。
- MCP 设计文档：`mcp/README.md`、`mcp/mcp-course-server-design.md`。
- Agent Team 文档：`agent-team/README.md`、`agent-team/workflow.md` 及角色说明。
- Rubric：`rubric.md`、`assessment/lab-rubric.md`、`assessment/homework-rubric.md`、`assessment/final-project-rubric.md`。
- Alpha 测试材料：若当前仓库中存在 Alpha 测试材料，可作为小范围验证参考；若不存在，不得虚构测试结果。

## 12. 教学风险与对策

| 风险 | 对策 |
| --- | --- |
| 工具安装失败 | 第 1 周发放环境检查表，第 2 周前完成版本检查；准备手动替代流程和失败记录模板 |
| Claude Code / Codex 不可用 | 不要求伪造调用记录；学生提交不可用原因、手动操作、diff、测试结果和如果工具可用会如何下任务的说明 |
| 学生只复制 AI 输出 | Rubric 要求提交 prompt、计划、diff、测试日志、人工判断和复盘；缺少人工解释不得高分 |
| 学生看 solution-notes | Alpha 阶段明确诚信要求；Pilot 阶段制作 student-only 包隐藏 `solution-notes.md` 和教师说明 |
| 学生不会看 diff | 第 1-2 周安排 diff 阅读活动，要求学生逐项说明文件、函数、行为和风险 |
| 学生不会运行测试 | 每个 Lab 固定测试命令；课堂演示失败测试和通过测试；助教检查日志真实性 |
| 学生修改测试骗过结果 | 明确禁止弱化或删除测试；助教检查 Git diff；对测试修改要求解释，必要时运行教师基准测试 |
| 助教评分不一致 | 使用统一 Rubric 和样例批改记录；首次批改前做助教标定，抽查边界案例 |
| 课程被误解为 Prompt 技巧课 | 第一讲明确课程定位，后续每个 Lab 都要求测试、Review、权限、安全和 Human Gate 证据 |

