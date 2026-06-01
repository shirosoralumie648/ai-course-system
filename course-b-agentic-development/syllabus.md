# 课程大纲：Agentic Development：AI 原生软件工程实践

## 1. 课程基本信息

| 项目 | 内容 |
| --- | --- |
| 课程名称 | Agentic Development：AI 原生软件工程实践 |
| 适用对象 | 计算机、软件工程、人工智能、数据科学、网络工程、信息安全、电子信息等有编程基础的学生 |
| 建议周期 | 12 周 |
| 课程形态 | 讲授 + 工具演示 + 实验 + 复盘 + 期末项目 |
| 当前版本 | MVP |

## 2. 课程简介

本课程训练学生把 Coding Agent 纳入真实软件工程流程。课程不把 Agent 当作神奇代码生成器，而是把它视为一个需要上下文、规则、权限、测试、Review 和 Human Gate 的工程协作者。

学生将使用 Claude Code、OpenAI Codex、`CLAUDE.md`、`AGENTS.md`、Skill、MCP、Subagents、Agent Team、测试和 Review 流程，完成从小型 bugfix 到综合 Agentic Workflow 的训练。

## 3. 教学目标

学生完成课程后应能：

1. 区分 Chatbot、Copilot、Coding Agent 和 Agentic Workflow。
2. 使用 Claude Code 和 Codex 完成小步代码任务。
3. 为项目编写具体、可执行、可审查的 Agent 规则文件。
4. 设计 Skill，把可复用工程流程固化下来。
5. 解释 MCP 如何扩展 Agent 的工具和上下文。
6. 设计职责清晰、权限有限的 Agent Team。
7. 用测试、Review、CI 和人工审批控制 Agent 交付质量。
8. 识别 Agent 误改、越权、幻觉、安全风险和测试伪通过等问题。

## 4. 先修要求

- 基础编程能力，建议熟悉 Python 或 JavaScript。
- 基础 Git 能力，包括 clone、branch、commit、diff、pull request。
- 能阅读 README、运行项目测试、理解简单错误日志。
- 能使用命令行。
- 理解不要提交密钥、Token、密码和隐私数据。

## 5. 教学方式

- 课堂讲授：概念、流程、风险和案例。
- 教师演示：展示 Agent 如何读取代码库、提出计划、修改文件、运行测试和生成 diff。
- 实验训练：每个实验要求保留可审计记录。
- 课堂复盘：对比 Agent 输出和人工判断。
- 期末项目：构建一套完整 Agentic Workflow。

## 6. 使用工具

| 工具 | 课程用途 |
| --- | --- |
| Claude Code | 代码库理解、bugfix、规则文件训练、Skill 使用 |
| OpenAI Codex | 本地代码任务、计划、审批、测试和 diff 记录 |
| Git / GitHub | 实验提交、diff 审查、Pull Request |
| 测试框架 | 验证代码修改，具体框架由示例项目决定 |
| MCP | 工具和课程资源接入设计 |
| CI | 后续版本用于自动化验证 |

如果某个工具的安装命令发生变化，以官方文档为准。本课程不伪造未经确认的安装命令。

## 7. 学习成果

课程结束时，学生应提交：

- 4 个 MVP 实验记录。
- 至少 1 个规则文件设计。
- 至少 1 个 Skill。
- 至少 1 个 MCP 配置或 MCP Server 设计。
- 至少 1 个 Agent Team 工作流。
- 期末 Agentic Workflow 项目。

## 8. 周次安排概览

| 周次 | 主题 |
| --- | --- |
| 第 1 周 | AI 原生软件工程导论 |
| 第 2 周 | Claude Code 基础 |
| 第 3 周 | Codex 基础 |
| 第 4 周 | Context Engineering |
| 第 5 周 | `CLAUDE.md` / `AGENTS.md` / Rules |
| 第 6 周 | 权限、Hooks 与安全边界 |
| 第 7 周 | Skill 设计 |
| 第 8 周 | MCP 原理与使用 |
| 第 9 周 | 自定义 MCP Server |
| 第 10 周 | Subagents 与 Agent Team |
| 第 11 周 | 测试、Review 与 CI |
| 第 12 周 | 期末项目答辩 |

## 9. 实验安排

| 实验 | 对应周次 | 核心能力 |
| --- | --- | --- |
| Lab 01 Claude Code Bugfix | 第 2 周 | 代码库理解、修复、测试、diff 审查 |
| Lab 02 Codex Code Change | 第 3 周 | 计划、权限、审批、测试、工具对比 |
| Lab 03 Project Rules | 第 5 周 | `CLAUDE.md` / `AGENTS.md` 规则设计 |
| Lab 04 Code Review Skill | 第 7 周 | Skill 设计、结构化 Review、人工修订 |

## 10. 作业安排

阶段作业建议围绕以下主题：

1. Agent 交互记录分析。
2. 规则文件设计说明。
3. Skill 设计说明。
4. MCP Server 设计说明。
5. Agent Team 工作流说明。

每份作业都必须保留可审计证据，不接受只有结论没有过程的提交。

## 11. 期末项目

题目：构建一个 AI 原生软件工程工作流。

学生必须交付仓库、规则文件、Skill、MCP 设计、Agent 角色设计、测试或验证脚本、Review 或测试报告、演示材料、技术报告和复盘文档。

## 12. 评分构成

| 项目 | 比例 | 说明 |
| --- | --- | --- |
| 平时实验 | 35% | 4 个核心实验，重点看过程记录、测试和审查 |
| 阶段作业 | 20% | 规则、Skill、MCP、Agent Team 等设计作业 |
| 期末项目 | 35% | 完整 Agentic Workflow |
| 课堂参与与复盘 | 10% | 课堂讨论、复盘质量、风险意识 |

## 13. 学术诚信和 AI 使用规范

- 可以使用 AI，但必须记录 AI 做了什么、学生审查了什么、最终接受了什么。
- 不得把 AI 输出直接当作个人理解。
- 不得伪造测试结果、Review 结果或工具输出。
- 不得提交他人代码、密钥、隐私数据或未经授权的材料。
- 必须明确区分 Agent 输出和人工判断。

## 14. 安全和隐私要求

- 不提交 API Key、Token、密码、cookie、私钥、学生隐私和真实业务数据。
- 涉及外部服务、网络访问、依赖安装、删除文件、大规模重构时必须进入 Human Gate。
- 任何工具调用和 MCP 资源都不默认可信。
- 对学生提交内容和外部文档要防 prompt injection。
