# Teacher Guide：Repo 02 Feature Development

## 教学目的

本项目用于 Lab 02，让学生体验 Codex 在小型功能开发中的作用。重点不是让 Codex “自动写完”，而是让学生记录任务 Prompt、计划、权限边界、diff、测试和人工判断。

## 教师演示建议

1. 进入 `repo-02-feature-development/`。
2. 运行 `python -m unittest discover -s tests -v`，确认初始测试通过。
3. 展示 README 中的新增需求。
4. 让学生先写自己的验收标准。
5. 使用 Codex 前，要求学生在 Prompt 中写明允许修改范围、禁止修改范围和测试命令。
6. Codex 修改后，要求学生运行测试、审查 diff，再决定是否接受。

## 学生容易犯的错

- 只实现函数，不新增测试。
- 改动 `list_titles` 导致原有行为破坏。
- 为了过滤功能改变任务数据结构。
- 忽略无匹配任务应返回空列表。
- 没有记录 Codex 的权限请求或失败输出。

## 期望 diff 范围

合理 diff 通常只包含：

- `src/todo_filter.py`：新增 `filter_titles_by_status`。
- `tests/test_todo_filter.py`：新增 2-3 个状态过滤测试。

如果学生修改 README、教师说明、依赖配置或删除原有测试，需要重点审查原因。

## 建议验收测试

学生应新增类似测试：

```python
from todo_filter import filter_titles_by_status


def test_filter_titles_by_pending_status(self):
    tasks = [
        {"title": "Write report", "status": "pending"},
        {"title": "Submit homework", "status": "done"},
        {"title": "Review diff", "status": "pending"},
    ]
    self.assertEqual(
        filter_titles_by_status(tasks, "pending"),
        ["Write report", "Review diff"],
    )
```

还应覆盖 `done` 和无匹配任务。

## 如何判断学生是否真正完成

- 基线测试日志存在。
- 新增测试能覆盖 pending、done、无匹配。
- 最终测试全部通过。
- diff 没有删除原有测试。
- 学生能说明 Codex 的修改是否符合验收标准。
