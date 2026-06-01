# Agent Team 设计

## 核心观点

Agent Team 不是让多个 AI 随便聊天，而是把软件工程任务拆成多个职责明确、权限有限、输入输出清楚的角色。

## 角色

- Planner Agent：需求澄清、任务拆解、风险识别、生成 task plan，不直接改代码。
- Coder Agent：根据 task plan 小步实现，必须遵守修改范围。
- Tester Agent：生成测试、运行测试、分析失败，不伪造测试通过。
- Reviewer Agent：审查 diff、架构一致性、测试覆盖、安全风险、文档完整性，不直接合并代码。
- Human Gate：范围确认、危险操作审批、最终合并决策。

## 共同规则

- 每个角色只做自己职责内的事。
- 每一步都要有输入、输出和通过条件。
- 失败时停止扩大修改，返回上一阶段。
- 最终交付必须有报告。

## 文件说明

- `planner-agent.md`
- `coder-agent.md`
- `tester-agent.md`
- `reviewer-agent.md`
- `workflow.md`
