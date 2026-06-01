# 第 10 周教师讲稿：Subagents 与 Agent Team

## 0-10 分钟：从单 Agent 到 Agent Team

各位同学，到目前为止，我们已经学习了 Task Packet、规则文件、Skill 和 MCP。今天我们讨论一个更接近真实工程协作的问题：多个 Agent 或 Subagent 如何组成 Agent Team。

首先请大家明确一点：Agent Team 不是让几个 AI 随便聊天。真正的 Agent Team 必须有职责划分、输入输出、权限边界、失败处理和 Human Gate。

课堂提问：

- 如果 Planner、Coder、Tester、Reviewer 都能直接改代码，会发生什么？
- 如果多个 Agent 给出相互冲突的建议，谁负责决策？
- Human Gate 在团队流程中应该放在哪里？

教师总结：

Agent Team 的价值不是“人更多”，而是分工更清楚。每个角色做自己该做的事，不越权，不伪造证据，不绕过人工审批。

## 10-25 分钟：Agent Team 的基本角色

课程中建议使用五类角色。

第一，Planner。Planner 负责澄清需求、拆解任务、识别风险、生成计划。Planner 不直接改代码。

第二，Coder。Coder 根据已确认计划小步实现。Coder 不无计划重构，不修改禁止文件。

第三，Tester。Tester 负责生成测试、运行测试、分析失败。Tester 不伪造测试通过，不弱化测试。

第四，Reviewer。Reviewer 负责审查 diff、架构、测试、安全和文档。Reviewer 不直接合并代码。

第五，Human Gate。Human Gate 由学生、教师、助教或团队负责人承担，负责确认范围、审批危险操作和最终接受或拒绝。

教师说明：

这五个角色可以由不同 Agent 执行，也可以由同一个工具在不同阶段扮演。关键不是工具数量，而是职责边界。

课堂提问：

- 为什么 Planner 不应该直接改代码？
- 为什么 Reviewer 不应该直接合并代码？
- Tester 如果测试失败，应输出什么？

## 25-45 分钟：Agent Team 工作流

一个基本 Agent Team 工作流可以这样设计：

```text
需求输入
-> Planner 分析任务、风险和计划
-> Human Gate 确认范围
-> Coder 小步实现
-> Tester 运行测试并分析失败
-> Reviewer 审查 diff 和风险
-> Human Gate 决定接受、返工或拒绝
-> 生成交付报告和复盘
```

教师强调：

每一步都要有输入和输出。例如 Planner 的输出是计划和风险，不是代码。Tester 的输出是测试命令、结果和失败分析，不是“我觉得可以”。Reviewer 的输出是问题列表、证据和建议，不是“LGTM”。

课堂提问：

- 哪一步最容易被学生跳过？
- 哪一步最容易出现伪造证据？
- 如果测试失败，流程应该回到哪里？

## 45-65 分钟：权限分离

Agent Team 的一个重要原则是权限分离。

Planner 可以读需求和代码，但不改代码。Coder 可以改允许文件，但不能批准自己的修改。Tester 可以运行测试，但不能为了通过而弱化测试。Reviewer 可以指出问题，但不能直接合并。Human Gate 才能做最终接受和高风险审批。

教师说明：

权限分离不是形式主义。它防止同一个角色同时提出方案、执行方案、证明方案正确并批准方案。这在真实工程中会导致风险失控。

示例：

如果 Coder 修改了测试让功能通过，Tester 和 Reviewer 应该发现并标记。如果 Reviewer 自己合并，就失去了 Human Gate。

课堂活动：

请学生判断以下行为是否越权：

- Planner 直接修改 `src/`。
- Coder 在没有计划确认时重构项目。
- Tester 删除失败测试。
- Reviewer 合并 PR。
- Human Gate 未看测试日志直接接受。

## 65-85 分钟：失败处理和冲突处理

Agent Team 会产生冲突。例如 Coder 认为修改完成，Tester 发现测试失败；Reviewer 认为 diff 过大，Planner 认为任务需要重构；安全检查认为依赖变更风险过高。

处理冲突的原则是：证据优先，Human Gate 决策。

教师话术：

当 Agent 之间意见冲突时，不要让它们无限对话。要把冲突转化为可检查问题：

- 具体失败测试是什么？
- 具体 diff 风险是什么？
- 依赖变更影响什么？
- 哪个验收标准未满足？
- 是否需要缩小任务范围？

课堂提问：

- 如果 Coder 说完成但 Tester 说失败，你相信谁？
- 如果 Reviewer 提出安全风险但测试通过，是否可以忽略？
- 如果 Planner 建议大重构但当前任务很小，你如何决策？

## 85-105 分钟：期末项目 Agent Team 设计

期末项目要求学生提交至少 3 个 Agent / Subagent 角色设计。今天我们开始准备。

每个角色设计至少包含：

- 角色名称。
- 角色职责。
- 输入。
- 输出。
- 允许操作。
- 禁止操作。
- 需要交给 Human Gate 的情况。
- 与其他角色的交接方式。

示例：

```text
角色：Tester Agent
职责：运行测试、分析失败、报告验证证据
输入：任务目标、diff、测试命令
输出：测试命令、退出码、失败摘要、风险
允许：运行指定测试命令
禁止：修改测试以绕过失败；声称未运行测试已通过
Human Gate：测试失败但团队仍想提交时
```

课堂任务：

请学生为期末项目草拟 Planner、Coder、Tester、Reviewer 中至少 3 个角色。

教师巡视重点：

- 是否职责重叠。
- 是否有禁止行为。
- 是否写清输入输出。
- 是否保留 Human Gate。

## 105-115 分钟：流程图与交付证据

Agent Team 不能只写角色，还要画出流程。流程图可以简单，但必须显示任务如何流转，哪里测试，哪里 Review，哪里 Human Gate。

交付证据包括：

- 任务包。
- Planner 计划。
- Coder diff。
- Tester 日志。
- Reviewer 报告。
- Human Gate 决策。
- 复盘。

教师说明：

期末答辩时，老师不只看你做了什么功能，还要看你的 Agent Team 如何保证功能可信。

## 115-120 分钟：总结与作业

今天我们学习了 Subagents 与 Agent Team。请记住：多 Agent 协作的核心是职责清楚、权限有限、证据可审计、最终由人决策。

课后作业：

- 为期末项目提交 Agent 角色说明。
- 画出 Agent Team workflow 草案。
- 标注 Human Gate 和失败处理路径。

下周我们会讲测试、Review 与 CI，把 Agent 输出纳入质量门禁。

