# 第 3 周教师讲稿框架：Codex 基础与 Lab 02

## 0-10 分钟：从 Lab 01 过渡到 Lab 02

教师话术要点：

- “上周我们处理的是 bugfix，本周处理小功能开发。”
- “bugfix 的重点是从失败测试定位问题；小功能开发还要新增测试并保护原有行为。”
- “今天我们使用 Codex，同时比较它和 Claude Code 的工程交互差异。”

课堂提问：

- Lab 01 中最容易漏掉的证据是什么？
- bugfix 和新增功能在验证方式上有什么不同？

## 10-25 分钟：Codex 是什么

讲解要点：

- Codex 是面向本地代码任务的 Coding Agent。
- 课程关注它如何计划、执行、运行命令、请求权限和报告结果。
- sandbox 和 approval 是安全边界，不是单纯的操作阻碍。

建议板书：

```text
Codex 任务流程：
Task Packet -> Plan -> Approval / Human Gate -> Edit -> Test -> Diff -> Summary
```

强调：

- 任何工具都不能跳过测试和 Review。
- 权限请求要记录原因和人工决定。

## 25-40 分钟：Codex 与 Claude Code 对比

对比维度：

- 任务输入方式。
- 上下文读取方式。
- 计划呈现方式。
- 权限请求方式。
- diff 和测试记录方式。
- 适合任务类型。

教师提醒：

- 不要让学生写“Codex 比 Claude Code 好”或相反。
- 工具对比必须写“在本次任务中观察到什么证据”。

课堂提问：

- 哪些任务更适合交互式分析？
- 哪些任务更适合本地计划和小步执行？
- 如果两个工具给出不同方案，你如何判断？

## 40-55 分钟：小功能开发流程

本周需求：

```text
新增 filter_titles_by_status(tasks, status)
```

验收标准：

- 返回指定状态的任务标题列表。
- 保持原始顺序。
- 没有匹配任务时返回空列表。
- 不改变任务数据结构。
- 不破坏 `list_titles(tasks)`。
- 新增测试和原有测试全部通过。

讲解要点：

- 新功能必须有新增测试。
- 原有测试必须继续通过。
- 不能为了实现新函数破坏已有 API。
- 不新增外部依赖。

## 55-75 分钟：教师演示 Codex 执行

演示路径：

```text
ai-course-system/course-b-agentic-development/examples/repo-02-feature-development/
```

演示基线测试：

```bash
python -m unittest discover -s tests -v
```

演示 Task Packet 要点：

- 需求和验收标准。
- 允许修改 `src/todo_filter.py` 和 `tests/test_todo_filter.py`。
- 禁止修改教师材料、参考答案和依赖。
- 先给计划。
- 修改后运行测试。

演示暂停点：

- Codex 输出计划后暂停，让学生判断是否批准。
- Codex 请求权限时暂停，让学生判断是否允许。
- 修改后先看 diff，再看测试结果。

课堂提问：

- 计划是否包含新增测试？
- 是否说明保留原有行为？
- 是否出现不必要依赖或大改？

## 75-110 分钟：学生实操 Lab 02

学生任务：

1. 运行基线测试。
2. 写 Codex Task Packet。
3. 记录 Codex 计划。
4. 执行小步修改。
5. 检查 diff。
6. 运行测试。
7. 写工具对比观察。

教师巡视重点：

- 是否先确认基线测试通过。
- 是否新增测试。
- 是否保护原有测试。
- 是否记录 approval。
- 是否把工具对比写成证据而非主观偏好。

## 110-120 分钟：总结与作业

教师总结：

- “Lab 02 的核心是小功能开发的完整证据链。”
- “新增功能不只看实现，还看新增测试和回归测试。”
- “Codex 和 Claude Code 可以比较，但比较必须基于实际任务记录。”

课后提交：

- Lab 02 实验记录。
- Codex Task Packet。
- Codex 计划和输出摘要。
- 权限请求和人工决定记录。
- Git diff。
- 测试日志。
- Claude Code 与 Codex 对比记录。

常见扣分提醒：

- 无基线测试。
- 无新增测试。
- 破坏原有行为。
- 未记录权限请求。
- 工具对比空泛。

