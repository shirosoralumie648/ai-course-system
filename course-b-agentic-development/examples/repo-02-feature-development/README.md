# Repo 02：Feature Development 示例项目

## 项目背景

这是 Lab 02 使用的最小 Python 示例项目。项目当前有一个简单的任务标题提取函数，基础测试应全部通过。学生需要使用 Codex 增加一个小功能：按任务状态过滤标题。

## 目录结构

```text
repo-02-feature-development/
├── README.md
├── pyproject.toml
├── src/
│   └── todo_filter.py
├── tests/
│   └── test_todo_filter.py
├── teacher-guide.md
└── solution-notes.md
```

## 原始功能

`list_titles(tasks)` 接收任务列表，并按原始顺序返回所有任务标题。

任务数据结构：

```python
{"title": "Write report", "status": "pending"}
```

## 新增需求

新增函数：

```python
filter_titles_by_status(tasks, status)
```

验收标准：

- 当 `status="pending"` 时，只返回 pending 任务标题。
- 当 `status="done"` 时，只返回 done 任务标题。
- 返回顺序必须保持原任务列表顺序。
- 没有匹配任务时返回空列表。
- 不改变原有任务数据结构。
- 保留 `list_titles(tasks)` 的原有行为。

## 允许修改的文件

- `src/todo_filter.py`
- `tests/test_todo_filter.py`

## 禁止修改的文件

- 不要修改 `teacher-guide.md` 和 `solution-notes.md` 作为实验提交的一部分。
- 不要删除原有测试。
- 不要修改任务数据结构来绕过需求。
- 不要新增外部依赖。

## 运行测试

在本目录运行：

```bash
python -m unittest discover -s tests -v
```

初始状态应看到现有测试通过。新增功能完成后，学生应补充新测试并让全部测试通过。

## Codex 使用记录要求

实验记录必须包含：

- 你给 Codex 的任务 Prompt。
- Codex 的计划或输出摘要。
- 是否出现 sandbox / approval 请求。
- 修改文件列表。
- Git diff。
- 基线测试和最终测试日志。
- 与 Claude Code 的对比记录。
