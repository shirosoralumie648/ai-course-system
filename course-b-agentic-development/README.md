# Agentic Development：AI 原生软件工程实践

## 课程一句话定义

这是一门面向计算机专业学生的 AI 原生软件工程实践课，训练学生使用、约束、扩展和评估 Coding Agent，使其参与真实软件工程流程。

## 这门课不是做什么

- 不是普通 Prompt Engineering 课。
- 不是“让 AI 自动写代码”的工具课。
- 不是 Claude Code / Codex 的功能介绍课。
- 不是脱离测试和审查的 Demo 课。
- 不是鼓励学生把判断责任交给 Agent 的课。

## 这门课真正做什么

- 用 Claude Code / Codex 处理真实代码任务。
- 用 `AGENTS.md` / `CLAUDE.md` 建立项目规则。
- 用 Skill 固化可复用流程。
- 用 MCP 扩展工具和上下文。
- 用 Agent Team 拆分 Planner、Coder、Tester、Reviewer 等角色。
- 用测试、Review、CI 和 Human Gate 保证质量。
- 用复盘训练学生识别 Agent 的能力边界和失败模式。

## 面向对象

- 计算机科学、软件工程、人工智能、数据科学、网络工程、信息安全、电子信息等专业学生。
- 已有基础编程能力、Git 使用经验，并愿意记录工程过程的学习者。
- 希望把 AI 工具纳入团队工程流程的助教、开发者和课程设计者。

## 先修要求

- 能阅读并修改小型 Python 或 JavaScript 项目。
- 掌握 Git 的 clone、branch、commit、diff、pull request 基础操作。
- 能运行基本测试命令。
- 理解命令行、依赖安装、项目目录结构和 README。
- 有基本安全意识：不提交 API Key、Token、密码和隐私数据。

## 学完能做什么

学生完成课程后，应能：

1. 让 Coding Agent 理解代码库和任务边界。
2. 编写可执行的 `CLAUDE.md` / `AGENTS.md` 项目规则。
3. 使用 Claude Code 和 Codex 完成小步代码任务。
4. 设计 Skill，把审查、调试、测试等流程固化为可复用单元。
5. 解释 MCP 的作用，并设计课程级 MCP Server。
6. 设计职责清晰、权限有限的 Agent Team。
7. 审查 Agent 生成的 diff，并用测试、Review 和 CI 验证结果。
8. 在危险操作前设置 Human Gate。
9. 形成可审计的实验记录和工程复盘。

## 课程结构

| 模块 | 内容 |
| --- | --- |
| 基础认知 | AI 原生软件工程、Claude Code、Codex |
| 上下文工程 | 代码库理解、任务上下文、证据和约束 |
| 规则文件 | `CLAUDE.md`、`AGENTS.md`、权限和禁止行为 |
| 流程复用 | Skill 设计、Review Skill、模板库 |
| 工具扩展 | MCP 原理、课程 MCP Server 设计 |
| 多 Agent 协作 | Subagents、Agent Team、Planner/Coder/Tester/Reviewer |
| 质量保障 | 测试、Review、CI、安全边界、Human Gate |
| 综合项目 | 构建一个 AI 原生软件工程工作流 |

## MVP 实验列表

4 个实验形成一条进阶路线，从"让 Agent 改代码"到"用规则约束 Agent"到"把流程固化成 Skill"：

```
Lab 01: 让 Claude Code 修一个 bug        → 学会审查 diff、跑测试
    ↓
Lab 02: 让 Codex 加一个小功能             → 学会对比不同 Agent 的交互方式
    ↓
Lab 03: 给项目写规则文件                  → 学会用 CLAUDE.md/AGENTS.md 约束 Agent
    ↓
Lab 04: 把代码审查封装成 Skill            → 学会把流程固化成可复用单元
```

每个 Lab 都使用同一个示例代码库（`repo-01-small-bugfix` 或 `repo-02-feature-development`），所以你能看到同一个项目在不同工程手段下的变化：从"裸奔让 Agent 改代码"到"有规则、有审查、有 Skill 的工程流程"。

| Lab | 文件 | 周次 | 核心技能 |
|---|---|---|---|
| 01 | [lab-01-claude-code-bugfix.md](labs/lab-01-claude-code-bugfix.md) | 第 2 周 | diff 审查 + 测试验证 |
| 02 | [lab-02-codex-code-change.md](labs/lab-02-codex-code-change.md) | 第 3 周 | 工具对比 + 权限边界 |
| 03 | [lab-03-project-rules.md](labs/lab-03-project-rules.md) | 第 5 周 | 规则编写 + 行为对比 |
| 04 | [lab-04-code-review-skill.md](labs/lab-04-code-review-skill.md) | 第 7 周 | Skill 设计 + Review 修订 |

## 教师授课材料

- [课程设计书](course-design/course-design.md)
- [教师授课指南](teacher-guide/teacher-guide.md)
- [前 4 周教案](lesson-plans/)
- [12 周教师逐字讲稿](teacher-scripts/)
- [PPT 大纲](slides-outline/)
- [12 周 PPT 文件](slides/)

## 期末项目

题目：构建一个 AI 原生软件工程工作流。

学生最终交付的不只是代码，而是一套 Agentic Workflow，包括 GitHub 仓库、规则文件、至少 1 个 Skill、至少 1 个 MCP 配置或 MCP Server 设计、至少 3 个 Agent / Subagent 角色设计、测试或验证脚本、Review 报告、演示和技术复盘。

## 评分方式

| 项目 | 比例 |
| --- | --- |
| 平时实验 | 35% |
| 阶段作业 | 20% |
| 期末项目 | 35% |
| 课堂参与与复盘 | 10% |

## 当前 MVP 范围

MVP 只保证最小可教学闭环，不承诺完整教材、完整网站或完整 MCP Server 生产代码。当前已经补充 12 周教师逐字讲稿和 12 套课程 B PPTX 初版，重点仍是支持教师授课、学生完成 4 个核心实验，并明确期末项目标准。
