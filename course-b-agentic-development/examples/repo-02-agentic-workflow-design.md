# 示例项目 02：Agentic Workflow Repo 设计

## 目的

用于期末项目展示参考，说明一个完整 Agentic Workflow 应包含哪些工程材料。

## 建议方向

构建一个小型代码审查助手，用于检查学生提交是否包含 README、规则文件、Skill、测试记录和 Review 报告。

## 必须包含

- `README.md`
- `AGENTS.md`
- `skills/code-review/SKILL.md`
- `mcp-design.md`
- `agent-team/workflow.md`
- `tests/` 或验证脚本
- `reports/review-example.md`

## 教学重点

本示例强调工作流，而不是复杂功能。学生应能看到 Planner、Coder、Tester、Reviewer 和 Human Gate 如何协作。

## 最小实现规格

本设计可实现为一个最小可运行项目：脚本读取一次学生提交目录，检查 README、规则文件、Skill、测试记录和 Review 报告是否存在，并生成结构化检查结果。实现时不需要接入真实在线模型，重点是让学生理解 Agentic Workflow 的工程材料边界。
