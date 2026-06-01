# Lab 01：Claude Code Bugfix

> **完成比完美重要。** 这个实验不要求你一次做对，只要求你真实记录每一步。

| 项目 | 内容 |
|---|---|
| **适用周次** | 第 2 周 |
| **预计时长** | 2-3 小时 |
| **核心产出** | 实验记录 Markdown + 修复前后测试日志 + Git diff + 复盘 |
| **前置条件** | 已安装 Claude Code；能使用 Git 和命令行；已阅读示例项目 README |

**你将学到：**
- Claude Code 如何阅读项目、理解错误、提出修复计划
- 如何审查 Agent 的 diff，而不是盲目接受
- 如何运行测试并用证据证明修改正确

**实验步骤概览：**

```
① 运行失败测试，观察错误     ⏱️ ~15min
② 让 Claude Code 分析问题     ⏱️ ~20min
③ 审查修复计划，决定是否批准   ⏱️ ~15min
④ 审查 diff，运行测试         ⏱️ ~20min
⑤ 记录实验过程和复盘          ⏱️ ~30min
```

---

## 1. 实验名称

Claude Code Bugfix：用 Coding Agent 修复小型项目中的真实 bug。

## 5. 实验背景

本实验使用课程仓库内置示例项目：

```text
../examples/repo-01-small-bugfix/
```

项目测试初始状态应失败。学生使用 Claude Code 阅读项目、理解错误、提出修复方案、修改代码、运行测试并审查 diff。

重点不是“让 Claude Code 直接改完”，而是观察和记录 Agentic Development 的工程过程。

## 6. 使用工具

- Claude Code。
- Git。
- Python 3.10 或更高版本。
- Python 标准库 `unittest`。
- Markdown 实验记录。

## 7. 示例项目说明

示例项目路径：

```text
ai-course-system/course-b-agentic-development/examples/repo-01-small-bugfix/
```

关键文件：

- `src/grade_utils.py`：包含故意保留的业务 bug。
- `tests/test_grade_utils.py`：测试文件，学生不得删除或改写以绕过结果。
- `teacher-guide.md`：教师和助教说明。
- `solution-notes.md`：参考答案说明，实验开始前不直接发给学生。

固定测试命令：

```bash
python -m unittest discover -s tests -v
```

初始预期状态：

- `test_average_empty_list_returns_zero` 报 `ZeroDivisionError`。
- `test_pass_rate_counts_sixty_as_passing` 失败，因为 60 分没有被计入及格。

修复后预期状态：5 个测试全部通过。

## 8. 实验任务

1. 进入示例项目目录。
2. 运行初始测试，保存失败日志。
3. 让 Claude Code 分析失败原因。
4. 要求 Claude Code 先给计划，不要直接修改。
5. 审查计划后允许小步修改。
6. 查看 Git diff。
7. 运行测试。
8. 决定是否接受修改，并说明原因。

## 9. 操作步骤

1. 从课程仓库根目录进入示例项目：

   ```bash
   cd ai-course-system/course-b-agentic-development/examples/repo-01-small-bugfix
   ```

2. 创建实验分支，例如 `lab-01-bugfix`。
3. 运行初始测试并保存日志：

   ```bash
   python -m unittest discover -s tests -v
   ```

4. 向 Claude Code 提供任务：
   - 当前测试失败。
   - 请先分析失败原因。
   - 请列出计划和拟修改文件。
   - 未经确认不要大规模重构。
5. 审查 Claude Code 的分析，记录其判断。
6. 允许 Claude Code 小步修复。
7. 使用 `git diff` 查看修改。
8. 再次运行固定测试命令。
9. 如果测试仍失败，要求 Claude Code 基于日志继续分析。
10. 最终生成实验记录和复盘。

## 10. 推荐 Claude Code 任务描述模板

建议优先使用 Claude Code 交互模式，并先让 Claude 输出计划，等待你人工确认后再允许修改。可以复制下面模板作为起点：

```text
这是课程 B Lab 01：Claude Code Bugfix 的实验项目。

项目背景：
- 这是一个小型 Python 成绩统计函数库。
- 当前测试失败是课程故意保留的业务逻辑 bug。

当前测试命令：
python -m unittest discover -s tests -v

当前失败现象：
- average_score([]) 触发 ZeroDivisionError。
- pass_rate([59, 60, 80]) 没有把 60 分计入及格。

允许修改范围：
- src/grade_utils.py

禁止修改范围：
- tests/
- README.md
- teacher-guide.md
- solution-notes.md

修复目标：
- average_score([]) 返回 0.0。
- pass_rate 中 60 分算及格。

工作流程：
1. 先输出修改计划和拟修改文件。
2. 等待我人工确认。
3. 再修改代码。
4. 再运行测试命令。
5. 最后输出 diff 摘要和测试结果。

禁止行为：
- 不允许修改测试。
- 不允许删除测试。
- 不允许直接照抄 solution-notes。
- 不允许未运行测试就声称完成。
```

## 11. 交互模式建议

- 如果使用 Claude Code 交互模式，先要求 Claude 输出修改计划，再由学生人工确认是否允许修改。
- 如果使用 `claude -p` 非交互模式，可能不会留下清晰的“先计划、再确认”过程。
- 如果使用非交互模式，必须保存完整 stdout、最终 diff 和测试结果。
- 实验评分更推荐有“计划 -> 确认 -> 修改 -> 测试 -> 审查”的过程记录，而不是只提交最终结果。

## 12. Claude Code 不可用时的替代流程

如果学生本机 Claude Code 不可用，不要伪造调用记录。应提交：

- Claude Code 不可用的原因。
- 版本检查或报错截图，例如 `claude --version` 的输出或失败信息。
- 手动修复过程。
- 手动 diff。
- 测试结果。
- 对比说明：如果 Claude Code 可用，自己会如何给它下任务。

该情况可作为 Alpha 反馈，不直接判零。助教应重点检查学生是否如实记录环境问题、是否完成了测试和人工审查。

## 13. 测试通过后的人工审查提醒

测试通过不等于任务完全完成。学生必须检查：

- 是否只改了允许修改的文件。
- 是否没有修改 `tests/`。
- 是否没有引入无关重构。
- diff 是否与失败测试一一对应。
- 是否能用自己的话解释修改原因。

如果 diff 超出 `src/grade_utils.py`，即使测试通过，也必须说明原因并等待助教或教师确认。

## 14. solution-notes 风险提醒

- `solution-notes.md` 是教师 / 助教参考材料。
- Alpha 阶段如果学生能看到该文件，不得提前查看。
- 如果查看过，必须在实验记录中如实说明查看时间和原因。
- Pilot 阶段建议制作 student-only 包，隐藏 `solution-notes.md` 和 `teacher-guide.md`。

## 15. 记录要求

实验记录必须包含：

1. 原始问题是什么。
2. 初始测试命令和失败日志。
3. Claude Code 如何理解问题。
4. 它建议改哪些文件。
5. 实际 diff 是什么。
6. 测试结果是什么。
7. 学生是否接受修改，为什么。
8. 有哪些风险或不确定点。

## 16. 预期结果

- 预置 bug 被修复。
- 测试从失败变为通过，最终输出应显示 5 个测试通过。
- 学生能解释修改原因，而不是只引用 Agent 结论。
- Git diff 应主要集中在 `src/grade_utils.py`。

## 17. 提交要求

- `lab-01-report.md`：实验记录。
- 修复前后测试截图或终端日志。
- Git diff 或 Pull Request 链接。
- 简短复盘，至少 300 字。

## 18. 禁止事项

- 禁止直接删除测试。
- 禁止只改测试不改业务代码。
- 禁止未运行测试就提交。
- 禁止新增外部依赖解决简单逻辑问题。
- 禁止把 Claude Code 输出原样当作人工判断。

## 19. 提交检查表

- 是否提交 `lab-01-report.md`。
- 是否提交关键 Prompt / Claude Code 指令。
- 是否提交初始失败测试日志。
- 是否提交修复后测试结果。
- 是否提交 Git diff。
- 是否说明人工接受或拒绝 Claude Code 建议的理由。
- 是否说明没有完成的部分；如果全部完成，明确写“无未完成项”。
- 是否有复盘。

## 20. 助教验收标准

- 文件是否齐全：报告、Prompt、初始失败日志、最终测试日志、diff、复盘。
- 任务是否完成：`python -m unittest discover -s tests -v` 最终通过 5 个测试。
- 测试是否真实：日志应包含命令、测试名和通过/失败状态。
- 是否存在伪造测试结果：报告中的测试结果必须与 diff 和日志一致。
- 是否符合规则边界：主要修改应在 `src/grade_utils.py`，不得删除测试。
- 是否能解释 AI 修改结果：学生应能说明空列表和 60 分边界的修复原因。

## 21. 常见错误

- 没有保存初始失败日志。
- 让 Claude Code 直接“修复所有问题”。
- 不审查 diff。
- 测试没跑却写“测试通过”。
- 修改范围扩大到无关文件。
- 使用非交互模式但没有保存 stdout。
- 提前查看 `solution-notes.md` 却没有在记录中说明。

## 22. 拓展任务

- 故意拒绝 Claude Code 的一个不合理建议，并记录原因。
- 为修复补充一个回归测试。
- 将本实验中的经验写入一条 `CLAUDE.md` 规则。

## 23. 评分标准

| 评分项 | 分值 | 优秀标准 | 合格标准 | 常见扣分 |
| --- | --- | --- | --- | --- |
| bug 理解 | 25 | 能解释根因和触发条件 | 能描述表层问题 | 只写“AI 修好了” |
| diff 审查 | 25 | 能逐项解释修改 | 能列出修改文件 | 没有 diff 或不看 diff |
| 测试证据 | 25 | 有修复前后测试日志 | 有最终测试结果 | 伪造或省略测试 |
| 复盘质量 | 25 | 能分析 Agent 优缺点和风险 | 有基本复盘 | 无人工判断 |

## 24. 复盘问题

1. Claude Code 哪一步最有帮助？
2. Claude Code 哪一步需要人工纠正？
3. 如果没有测试，你还能相信这个修改吗？
4. 哪些规则应该写进项目规则文件？
