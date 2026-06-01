# Teacher Guide：Repo 01 Small Bugfix

## 教学目的

本项目用于 Lab 01，让学生第一次体验 Coding Agent 参与真实 bugfix 的完整过程：运行失败测试、让 Agent 分析、审查计划、限制修改范围、运行测试、审查 diff、做人工判断。

## Bug 设计

项目中保留两个故意 bug：

1. `average_score([])` 会触发除零错误，但课程策略要求空列表返回 `0.0`。
2. `pass_rate([59, 60, 80])` 把 60 分排除在及格之外，但课程策略要求 60 分及格。

这两个 bug 都集中在 `src/grade_utils.py`，学生不需要修改测试。

## 预期学生操作路径

1. 进入 `repo-01-small-bugfix/`。
2. 运行 `python -m unittest discover -s tests -v`。
3. 保存初始失败日志。
4. 让 Claude Code 分析失败原因，并要求它先输出计划。
5. 审查计划是否只修改 `src/grade_utils.py`。
6. 允许小步修复。
7. 查看 `git diff`。
8. 重新运行测试。
9. 提交实验记录、测试日志和复盘。

## 预期测试失败输出

初始测试应包含：

```text
ERROR: test_average_empty_list_returns_zero
ZeroDivisionError: division by zero

FAIL: test_pass_rate_counts_sixty_as_passing
AssertionError: 0.3333333333333333 != 0.6666666666666666
```

具体行号可能因 Python 版本不同而变化。

## 参考修复思路

- 在 `average_score` 中先判断空列表，返回 `0.0`。
- 在 `pass_rate` 中把判断条件从 `score > 60` 改为 `score >= 60`。

参考答案见 `solution-notes.md`。教师讲评前不要把参考答案直接发给学生。

## 批改重点

- 学生是否保存初始失败日志。
- 学生是否让 Agent 先计划再修改。
- 学生是否审查了 diff。
- 学生是否只修改业务代码。
- 学生是否运行了修复后测试。
- 学生是否能解释为什么接受最终修改。
