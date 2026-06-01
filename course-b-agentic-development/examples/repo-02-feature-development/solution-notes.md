# Solution Notes：Repo 02 Feature Development

## 参考答案用途

本文件供教师和助教批改使用。不要在实验开始前直接发给学生。

## 预期修改文件

合理答案通常只修改：

- `src/todo_filter.py`
- `tests/test_todo_filter.py`

## 参考实现

```python
def filter_titles_by_status(tasks, status):
    return [task["title"] for task in tasks if task["status"] == status]
```

## 参考测试

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


def test_filter_titles_by_done_status(self):
    tasks = [
        {"title": "Write report", "status": "pending"},
        {"title": "Submit homework", "status": "done"},
    ]
    self.assertEqual(filter_titles_by_status(tasks, "done"), ["Submit homework"])


def test_filter_titles_by_status_with_no_matches(self):
    tasks = [{"title": "Write report", "status": "pending"}]
    self.assertEqual(filter_titles_by_status(tasks, "blocked"), [])
```

## 验证命令

```bash
python -m unittest discover -s tests -v
```

完成后，原有测试和新增测试都应通过。

## 不可接受做法

- 删除 `list_titles` 或改变其原有行为。
- 删除原有测试。
- 修改任务数据结构，例如把任务列表预先转换成其他格式。
- 新增外部依赖处理简单过滤。
- 未运行测试却声称完成。
