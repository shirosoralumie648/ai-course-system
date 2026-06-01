# Lab 02：Codex Code Change

> **完成比完美重要。** 工具不可用时如实记录，不要伪造结果。

| 项目 | 内容 |
|---|---|
| **适用周次** | 第 3 周 |
| **预计时长** | 2-3 小时 |
| **核心产出** | 任务说明 + Prompt + Codex 输出摘要 + diff + 测试结果 + 工具对比记录 |
| **前置条件** | 已安装 Codex；已完成 Lab 01 或理解 Claude Code 基本工作方式 |

**你将学到：**
- Codex 如何制定计划、执行修改、请求审批
- sandbox、approval 和权限边界的实际含义
- Claude Code 与 Codex 的交互方式差异（基于证据，不是基于感觉）

**实验步骤概览：**

```
① 阅读示例项目，理解要做什么功能    ⏱️ ~15min
② 写好任务描述和验收标准            ⏱️ ~15min
③ 给 Codex 下达任务，记录它的计划   ⏱️ ~20min
④ 审批操作，审查 diff，运行测试     ⏱️ ~30min
⑤ 填写 Claude Code vs Codex 对比表  ⏱️ ~20min
⑥ 复盘                             ⏱️ ~20min
```

**工具不可用怎么办？**
- 记录错误截图或日志（如 `codex --version` 输出或报错信息）
- 手动完成功能修改，保留完整 diff 和测试结果
- 在对比表中写明"Codex 不可用，以下为手动流程"
- 这会被视为 Alpha 反馈，不会直接判零分

---

## 1. 实验名称

Codex Code Change：用 Codex 完成一个小型功能修改。

## 5. 实验背景

本实验使用课程仓库内置示例项目：

```text
../examples/repo-02-feature-development/
```

项目当前有基础测试并应全部通过。学生需要使用 Codex 给任务列表工具新增“按状态过滤标题”的小功能，同时保留原有行为。

学生使用 Codex 完成修改，但必须保留计划、prompt、diff 和测试记录。

## 6. 使用工具

- OpenAI Codex。
- Git。
- Python 3.10 或更高版本。
- Python 标准库 `unittest`。
- Markdown 实验记录。

## 7. 示例项目说明

示例项目路径：

```text
ai-course-system/course-b-agentic-development/examples/repo-02-feature-development/
```

关键文件：

- `src/todo_filter.py`：业务代码。
- `tests/test_todo_filter.py`：现有测试，学生需要在此补充新增功能测试。
- `teacher-guide.md`：教师和助教说明。
- `solution-notes.md`：参考答案说明，实验开始前不直接发给学生。

固定初始测试命令：

```bash
python -m unittest discover -s tests -v
```

初始预期状态：2 个现有测试通过。

新增功能需求：

- 新增 `filter_titles_by_status(tasks, status)`。
- 支持 `pending` / `done` 等状态过滤。
- 没有匹配任务时返回空列表。
- 保留原始任务顺序。
- 不改变原有数据结构。
- 不破坏 `list_titles(tasks)` 的行为。

## 8. 实验任务

1. 阅读需求并写出自己的验收标准。
2. 给 Codex 输入任务和边界。
3. 记录 Codex 的计划。
4. 审批或拒绝高风险操作。
5. 记录 Codex 修改了哪些文件。
6. 运行测试。
7. 对比 Claude Code 与 Codex 的交互差异。

## 9. 操作步骤

1. 从课程仓库根目录进入示例项目：

   ```bash
   cd ai-course-system/course-b-agentic-development/examples/repo-02-feature-development
   ```

2. 创建实验分支，例如 `lab-02-codex-change`。
3. 运行基线测试，确认项目初始状态：

   ```bash
   python -m unittest discover -s tests -v
   ```

4. 编写任务 Prompt，包含需求、允许修改范围、测试命令和禁止行为。
5. 启动 Codex 执行任务。
6. 如果 Codex 请求权限，记录请求原因和你的审批决定。
7. Codex 修改完成后，使用 `git diff` 审查。
8. 运行测试。
9. 如果测试失败，要求 Codex 基于失败日志提出修复计划。
10. 写对比记录。

### Codex 任务描述模板

```text
请在当前 Python 项目中新增 filter_titles_by_status(tasks, status)。

需求：
- 返回指定 status 的任务标题列表。
- 保持原始顺序。
- 没有匹配任务时返回空列表。
- 不改变 list_titles(tasks) 的原有行为。

允许修改：
- src/todo_filter.py
- tests/test_todo_filter.py

禁止修改：
- teacher-guide.md
- solution-notes.md
- 删除或弱化已有测试
- 新增外部依赖

请先给出计划和拟修改文件，确认后再小步修改。修改后运行：
python -m unittest discover -s tests -v
```

## 10. 记录要求

必须记录：

- 任务说明。
- 使用的 Prompt。
- Codex 输出摘要。
- 修改文件列表。
- diff。
- 测试命令和结果。
- sandbox / approval 观察。
- 与 Claude Code 的差异。
- 对未完成部分的说明；如果全部完成，明确写“无未完成项”。

## 11. 预期结果

- 小功能完成并通过测试。
- 学生能说明 Codex 的行为边界。
- 学生能基于证据比较两个工具，而不是写主观口号。
- Git diff 通常只涉及 `src/todo_filter.py` 和 `tests/test_todo_filter.py`。

## 12. 提交要求

- `lab-02-report.md`。
- Prompt 原文。
- Codex 输出摘要。
- Git diff 或 Pull Request 链接。
- 测试日志。
- 工具对比记录。

## 13. 允许修改范围

- `src/todo_filter.py`
- `tests/test_todo_filter.py`
- 学生自己的实验记录文件

## 14. 禁止修改范围

- 禁止修改 `teacher-guide.md` 和 `solution-notes.md` 作为实验结果。
- 禁止删除原有测试。
- 禁止改变任务数据结构来绕过过滤逻辑。
- 禁止新增外部依赖。
- 禁止未运行测试就提交。

## 15. 新增测试要求

学生至少补充以下测试：

- `pending` 状态过滤。
- `done` 状态过滤。
- 无匹配状态返回空列表。
- 原有 `list_titles(tasks)` 测试仍然通过。

## 16. 提交检查表

- 是否提交 `lab-02-report.md`。
- 是否提交关键 Prompt / Codex 指令。
- 是否提交基线测试结果。
- 是否提交最终测试结果。
- 是否提交 Git diff。
- 是否提交 sandbox / approval 观察记录。
- 是否说明人工判断。
- 是否说明没有完成的部分；如果全部完成，明确写“无未完成项”。
- 是否提交 Claude Code 与 Codex 对比记录。
- 是否有复盘。

## 17. 助教验收标准

- 文件是否齐全：报告、Prompt、基线测试、最终测试、diff、对比记录、复盘。
- 任务是否完成：新增函数满足状态过滤需求。
- 测试是否真实：最终测试包含原有测试和新增过滤测试。
- 是否存在伪造测试结果：测试日志必须能对应提交 diff。
- 是否符合规则边界：修改范围应集中在 `src/todo_filter.py` 和 `tests/test_todo_filter.py`。
- 是否能解释 AI 修改结果：学生应能说明 Codex 为什么这样实现，以及是否接受。

## 18. Claude Code 与 Codex 对比记录模板

| 维度 | Claude Code 观察 | Codex 观察 | 证据 |
| --- | --- | --- | --- |
| 计划方式 |  |  |  |
| 权限请求 |  |  |  |
| 修改范围 |  |  |  |
| 测试执行 |  |  |  |
| diff 可读性 |  |  |  |
| 人工审查压力 |  |  |  |

## 19. 常见错误

- 功能完成但无测试。
- 忽略 Codex 的权限请求。
- 让 Codex 修改无关文件。
- 对比工具时写“更强”“更智能”等未经验证结论。

## 20. 拓展任务

- 为新增功能补充测试。
- 用 Claude Code 重做同一任务，比较 diff。
- 将任务流程整理成 `AGENTS.md` 的标准任务流程。

## 21. 评分标准

| 评分项 | 分值 | 优秀标准 | 合格标准 | 常见扣分 |
| --- | --- | --- | --- | --- |
| 功能完成度 | 25 | 功能符合验收标准且边界清楚 | 基本完成需求 | 功能跑偏或无验收 |
| 审计记录 | 25 | Prompt、计划、diff、审批、测试完整 | 记录主要过程 | 只提交最终代码 |
| 测试验证 | 25 | 有基线和最终测试 | 有最终测试 | 无测试或伪造结果 |
| 工具对比 | 25 | 基于证据说明差异 | 有基本比较 | 夸张或无证据 |

## 22. 复盘问题

1. Codex 的 sandbox 和 approval 对你的操作有什么影响？
2. 哪些修改你必须人工确认？
3. Claude Code 与 Codex 哪个更适合这个任务，为什么？
4. 如果测试不可用，你会如何降低风险？
