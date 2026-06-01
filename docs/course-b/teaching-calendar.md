# 12 周教学日历：Agentic Development

> **给你的使用说明：** 每周按顺序完成"课堂内容 → 实验任务 → 课后作业"。实验保留所有中间产物（prompt、计划、diff、测试日志、Review、复盘），不要只交最终结果。遇到工具问题如实记录，不要伪造。

---

## 第 1 周：AI 原生软件工程导论

<ChapterIntroduction duration="1 课时" output="概念对比表 + 800 字短文" :tags="['Chatbot', 'Copilot', 'Coding Agent', 'Agentic Workflow']">

- 区分 Chatbot、Copilot、Coding Agent、Agentic Workflow
- 理解为什么 Coding Agent 需要工程边界
- 建立"AI 输出必须验证"的课程规则

</ChapterIntroduction>

- **课堂内容**：四类工具形态的区别
- **实验任务**：课堂观察一个 Agent 分析小型仓库的过程，只记录不提交
- **课后作业**：写 800 字短文——为什么 Agentic Development 不是"让 AI 自动写代码"

**本周回顾：** 你能否用自己的话解释"Agentic Development 和让 AI 自动写代码有什么区别"？如果不能，重读课堂内容中关于规则、测试和 Human Gate 的部分。

---

## 第 2 周：Claude Code 基础

<ChapterIntroduction duration="1 课时 + 2-3 小时实验" output="实验记录 + 测试日志 + Git diff + 复盘" :tags="['Claude Code', 'diff 审查', '测试验证']">

- 让 Claude Code 阅读项目、理解失败测试、提出修复计划
- 审查修改 diff
- 运行测试并记录结果

</ChapterIntroduction>

- **课堂内容**：Claude Code 的项目上下文读取方式、任务描述、计划、文件修改
- **实验任务**：完成 [Lab 01：Claude Code Bugfix](/course-b/labs/lab-01)
- **课后作业**：提交实验记录和复盘

**本周回顾：** 你的实验记录中，是否有 Agent 的完整 diff？你是否逐行看过？如果跳过了 diff 审查，补上——这是 Agentic Development 最核心的技能。

---

## 第 3 周：Codex 基础

<ChapterIntroduction duration="1 课时 + 2-3 小时实验" output="任务说明 + Prompt + diff + 测试 + 工具对比记录" :tags="['Codex', 'sandbox', 'approval', '权限边界']">

- 使用 Codex 制定计划并小步修改代码
- 理解 sandbox、approval、权限边界的意义
- 对比 Claude Code 与 Codex 的交互差异

</ChapterIntroduction>

- **课堂内容**：Codex 任务输入、计划、执行和验证
- **实验任务**：完成 [Lab 02：Codex Code Change](/course-b/labs/lab-02)
- **课后作业**：提交 Codex 与 Claude Code 对比记录

**本周回顾：** 你的对比表中，Claude Code 和 Codex 的差异是否有具体证据？如果只是"感觉上不一样"，需要补充实际操作记录。

---

## 第 4 周：Context Engineering

<ChapterIntroduction duration="1 课时" output="上下文包 + Agent 响应对比记录" :tags="['上下文包', '完整性', '相关性', '时效性']">

- 识别任务需要哪些代码、文档、测试和约束
- 学会提供高质量上下文包
- 避免把无关信息塞给 Agent

</ChapterIntroduction>

- **课堂内容**：代码库地图、README、测试、错误日志、需求说明的作用
- **实验任务**：为 Lab 01 或 Lab 02 的示例项目补写上下文包
- **课后作业**：提交 `context-pack.md`

**本周回顾：** 你的上下文包中，是否明确写了"禁止修改哪些文件"？如果没有，Agent 可能会改你不希望它动的代码。

---

## 第 5 周：CLAUDE.md / AGENTS.md / Rules

<ChapterIntroduction duration="1 课时 + 2-3 小时实验" output="CLAUDE.md + AGENTS.md + 对比记录 + 复盘" :tags="['规则文件', '工程边界', '可执行规则']">

- 编写具体可执行的 CLAUDE.md 和 AGENTS.md
- 比较有规则和无规则时 Agent 行为差异
- 识别规则文件中的空话和不可执行要求

</ChapterIntroduction>

- **课堂内容**：项目目标、技术栈、目录结构、允许和禁止修改范围
- **实验任务**：完成 [Lab 03：Project Rules](/course-b/labs/lab-03)
- **课后作业**：提交规则设计说明

**本周回顾：** 把你的 CLAUDE.md 拿给同学看，问他"读完这条规则你知道该怎么做吗"。如果对方说不知道，说明规则还不够具体。

---

## 第 6 周：权限、Hooks 与安全边界

<ChapterIntroduction duration="1 课时" output="权限边界说明 + 审批清单 + 失败处理流程" :tags="['Human Gate', '权限边界', '审批流程']">

- 理解文件访问、命令执行、网络访问和依赖安装边界
- 设计 Hook 或审批规则
- 识别密钥、隐私和外部工具风险

</ChapterIntroduction>

- **课堂内容**：删除文件、大规模重构、修改依赖、访问外部服务、处理密钥时必须 Human Gate
- **实验任务**：设计一个危险操作审批清单
- **课后作业**：为示例项目补充权限边界和失败处理策略

**本周回顾：** 你的审批清单中，有没有"失败后怎么办"的条目？审批通过只是第一步，审批之后操作失败了如何回滚同样重要。

---

## 第 7 周：Skill 设计

<ChapterIntroduction duration="1 课时 + 2-3 小时实验" output="SKILL.md + Agent Review + 人工修订 Review + 复盘" :tags="['Skill', '可复用流程', '可审计输出']">

- 区分普通 Prompt 和 Skill
- 编写包含触发条件、输入、步骤、输出、禁止行为的 Skill
- 让 Skill 输出可审计结果

</ChapterIntroduction>

- **课堂内容**：Skill 的适用场景、code-review Skill 的结构
- **实验任务**：完成 [Lab 04：Code Review Skill](/course-b/labs/lab-04)
- **课后作业**：用自己的 Skill 审查一次代码修改

**本周回顾：** 你的 SKILL.md 中，"禁止行为"部分写了什么？如果为空，说明你还没想清楚 Skill 的边界在哪里。

---

## 第 8 周：MCP 原理与使用

<ChapterIntroduction duration="1 课时" output="MCP 学习记录 + 工具调用场景 + 风险清单" :tags="['MCP', 'tools', 'resources', '安全边界']">

- 解释 MCP 解决什么问题，不解决什么问题
- 区分 MCP 与普通 API 调用
- 识别 MCP 工具调用安全边界

</ChapterIntroduction>

- **课堂内容**：tools、resources、prompts 的基本概念
- **实验任务**：为课程资料检索设计 2 个工具调用场景
- **课后作业**：提交 MCP 工具使用风险清单

**本周回顾：** 你设计的工具调用场景中，有没有考虑"工具返回错误数据怎么办"？MCP 工具的输出不能默认信任。

---

## 第 9 周：自定义 MCP Server

<ChapterIntroduction duration="1 课时" output="MCP Server 设计草案" :tags="['接口设计', '输入输出', '安全说明']">

- 设计 tools、resources、prompts
- 为每个接口说明输入、输出、风险和人工审批
- 理解 MVP 可以先做设计，不伪造生产级实现

</ChapterIntroduction>

- **课堂内容**：课程 MCP Server 的工具设计
- **实验任务**：补充 `mcp-course-server-design.md` 的一个工具设计
- **课后作业**：提交一个最小 MCP Server 设计草案

**本周回顾：** 你的 MCP Server 设计中，每个工具是否都有"人工审批"标注？

---

## 第 10 周：Subagents 与 Agent Team

<ChapterIntroduction duration="1 课时" output="角色设计 + 任务流程图 + Human Gate 清单" :tags="['Planner', 'Coder', 'Tester', 'Reviewer', 'Human Gate']">

- 设计 Planner、Coder、Tester、Reviewer 和 Human Gate
- 明确每个角色的输入、输出、允许操作和禁止操作
- 防止多个 Agent 随意聊天导致责任不清

</ChapterIntroduction>

- **课堂内容**：Agent Team 的角色边界和职责
- **实验任务**：为期末项目画出 Agent Team 工作流
- **课后作业**：提交 Agent 角色说明和 workflow 草案

**本周回顾：** 你的 Agent Team 工作流中，如果 Tester 报告测试失败，流程会怎么走？是否有明确的"回退到 Coder"路径？

---

## 第 11 周：测试、Review 与 CI

<ChapterIntroduction duration="1 课时" output="测试命令 + Review checklist + CI 设计 + Human Gate 规则" :tags="['单元测试', 'Review 维度', 'CI', '质量门禁']">

- 设计自动化测试和人工 Review 流程
- 理解 CI 的作用和局限
- 形成最终项目的验证证据

</ChapterIntroduction>

- **课堂内容**：测试、Review 维度、CI 的作用
- **实验任务**：为期末项目补充测试和 Review 计划
- **课后作业**：提交期末项目验证计划

**本周回顾：** 你的验证计划中，测试命令是否可以直接复制粘贴运行？

---

## 第 12 周：期末项目答辩

<ChapterIntroduction duration="答辩课" output="完整 Agentic Workflow 项目" :tags="['演示', '代码走查', '技术复盘']">

- 展示 Agentic Workflow 而不仅是最终代码
- 解释规则文件、Skill、MCP、Agent Team、测试、Review 和 Human Gate 的设计
- 进行技术复盘

</ChapterIntroduction>

- **课堂内容**：3-5 分钟演示 + 代码走查 + 现场问答
- **课后作业**：提交最终技术报告和课程复盘文档

**本周回顾：** 答辩前自查：你的演示是否涵盖了"规则文件 → Agent 执行 → 测试验证 → Review → Human Gate → 最终合并"完整链路？

<SummaryCard title="12 周学习路径回顾" :sections="[
  { number: '1', title: '学会用 Agent', items: ['Claude Code 和 Codex 的基本操作', 'diff 审查和测试验证'] },
  { number: '2', title: '学会约束 Agent', items: ['规则文件（CLAUDE.md / AGENTS.md）', '权限边界和 Human Gate'] },
  { number: '3', title: '学会扩展 Agent', items: ['Skill 设计、MCP 工具扩展', 'Agent Team 多角色协作'] },
  { number: '4', title: '学会保障质量', items: ['测试、Review、CI', '可审计的工程过程'] }
]" :outputs="[
  '4 个核心实验报告',
  'CLAUDE.md + AGENTS.md 规则文件',
  '1 个 code-review Skill',
  '1 个期末项目 Agentic Workflow'
]" />
