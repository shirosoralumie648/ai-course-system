# 第 5 讲：规则、Skills、MCP 与 Agent Team 总览

## 本讲目标

- 建立 `CLAUDE.md`、`AGENTS.md`、Skill、MCP、Agent Team 的整体关系。
- 理解这些机制都服务于工程化、复用、审查和边界控制。
- 为第 5-10 周的课程做概念预埋。

## 为什么要学

单次 Prompt 不能长期约束 Agent 行为。真实项目需要把背景、规则、流程、工具和角色设计固化下来。规则文件、Skill、MCP 和 Agent Team 分别解决不同层次的问题。

## 核心概念

| 机制 | 解决的问题 | 典型产出 |
| --- | --- | --- |
| `CLAUDE.md` | 给 Claude Code 提供项目背景、命令、风格和约束 | 项目级规则 |
| `AGENTS.md` | 给多种 Agent 提供工作原则、权限和角色边界 | Agent 工作协议 |
| Skill | 固化可复用流程，如 code review、debug、release check | `SKILL.md` |
| MCP | 给 Agent 接入受控工具、资源和 prompts | MCP Server 设计或配置 |
| Agent Team | 把任务拆给职责明确的角色 | Planner/Coder/Tester/Reviewer 工作流 |

## 课堂讲解提纲

1. Prompt 为什么不够。
2. 规则文件负责项目边界。
3. Skill 负责流程复用。
4. MCP 负责工具和资源接入。
5. Agent Team 负责角色拆分。
6. Human Gate 贯穿所有机制。

## 教师演示建议

用同一个“修改小功能”的任务展示：

1. 没有规则时 Agent 的输出。
2. 加入 `AGENTS.md` 后输出如何变化。
3. 使用 code-review Skill 后 Review 如何结构化。
4. 假设 MCP 提供课程 Rubric 后，审查报告如何引用评分标准。

## 学生实操任务

让学生为自己的期末项目方向草拟一张机制图：规则文件、Skill、MCP、Agent Team 分别承担什么职责。

## 常见误区

- 把 Skill 当作长 Prompt。
- 把 MCP 当作万能 API。
- 让多个 Agent 随便聊天而没有职责边界。
- 忽略 Human Gate。

## 课后思考题

1. 规则文件和 Skill 的区别是什么？
2. MCP 工具输出为什么不能默认可信？
3. Planner Agent 为什么不应该直接改代码？

## 与后续实验的关系

本讲连接 Lab 03 和 Lab 04，并为后续 MCP、Agent Team、期末项目设计打基础。
