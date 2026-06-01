# 期末项目 Rubric

总分 100 分。题目是“构建一个 AI 原生软件工程工作流”。评分重点不是代码量，而是 Agentic Workflow 是否可解释、可约束、可验证、可审查。

| 评分项 | 分值 | 优秀标准 | 合格标准 | 不合格表现 | 常见扣分项 |
| --- | --- | --- | --- | --- | --- |
| 工程完整度 | 20 | GitHub 仓库结构清楚，README、规则文件、Skill、MCP 设计、Agent 角色、测试、Review、报告和复盘齐全 | 主要交付物齐全，少量说明不够细 | 缺多个核心交付物，无法理解项目 | README 不清楚；文件散乱；缺演示说明；交付物无法对应要求 |
| Claude Code / Codex 使用质量 | 15 | 有清晰任务 Prompt、计划、权限记录、diff、测试、审查和人工接受/拒绝记录 | 有基本 AI 使用记录和结果说明 | 只写“用了 AI”，没有过程证据 | 缺 Prompt；缺 diff；无 sandbox / approval 观察；无法说明工具边界 |
| 规则文件与上下文工程 | 15 | `CLAUDE.md` / `AGENTS.md` 具体可执行，包含项目背景、允许范围、禁止范围、测试命令、安全规则和 Human Gate | 有基本规则文件，覆盖主要边界 | 规则空泛或不可执行 | 无测试命令；无禁止范围；没有不确定事项处理；Human Gate 不明确 |
| Skill 设计 | 15 | 至少 1 个 Skill 结构完整，含适用场景、触发条件、输入要求、步骤、输出格式、检查清单、禁止行为和示例输出 | 有可用 Skill，但部分细节较弱 | 只是普通 Prompt，不可复用 | 缺禁止行为；缺输入要求；输出格式不可审计；无版本记录 |
| MCP 设计或接入 | 15 | MCP tools/resources/prompts 清楚，输入输出、风险、审批和安全边界明确；如有接入，能说明验证方式 | 有基本 MCP 设计或配置说明 | 没有 MCP 内容或只写概念 | 未说明输入输出；未说明 prompt injection 风险；无权限边界 |
| Agent Workflow | 10 | 至少 3 个 Agent / Subagent 角色职责清楚，流程有输入、输出、允许操作、禁止操作、失败处理和 Human Gate | 有基本角色和流程 | 多 Agent 职责混乱或只是聊天分工 | 无 Human Gate；Planner/Coder/Tester/Reviewer 边界不清 |
| 测试、Review、文档与复盘 | 10 | 测试真实可复查，Review 具体，文档能指导复现，复盘能分析失败和改进 | 有基本验证、Review 和复盘 | 无测试或伪造结果，Review 笼统 | 测试日志缺命令；Review 只写好坏；复盘没有人工判断 |

## 红线

- 伪造测试结果、Review 结果或工具输出。
- 提交真实 API Key、Token、密码、cookie、私钥或学生隐私。
- 无法解释项目中的 Agentic Workflow。
- 测试失败但报告中声称通过。

## 批改建议

助教应先检查交付物是否齐全，再检查过程证据是否真实。代码功能可以较小，但规则、Skill、MCP、Agent Workflow、测试和 Review 必须形成闭环。
