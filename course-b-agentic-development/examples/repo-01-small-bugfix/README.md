# Repo 01：Small Bugfix 示例项目

## 项目背景

这是 Lab 01 使用的最小 Python 示例项目。项目提供几个成绩统计函数，当前代码中故意保留了两个真实 bug，用于训练学生让 Claude Code 分析失败测试、提出计划、修改业务代码、审查 diff 并重新运行测试。

## 目录结构

```text
repo-01-small-bugfix/
├── README.md
├── pyproject.toml
├── src/
│   └── grade_utils.py
├── tests/
│   └── test_grade_utils.py
├── teacher-guide.md
└── solution-notes.md
```

## 环境准备

本项目只使用 Python 标准库，不需要安装第三方依赖。建议使用 Python 3.10 或更高版本。

可选虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell 可使用：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 运行测试

在本目录运行：

```bash
python -m unittest discover -s tests -v
```

## 当前预期失败

初始代码应出现 2 个失败或错误：

- `test_average_empty_list_returns_zero`：空列表平均分没有被安全处理。
- `test_pass_rate_counts_sixty_as_passing`：60 分应视为及格，但当前代码把 60 分排除在外。

如果初始测试全部通过，说明你可能已经修改过业务代码，请重新检查 Git diff。

## 学生任务

你需要使用 Claude Code 完成以下目标：

1. 先运行测试并保存失败日志。
2. 让 Claude Code 分析失败原因，但不要直接大范围重构。
3. 修复 `src/grade_utils.py` 中的业务逻辑。
4. 重新运行测试，确认所有测试通过。
5. 使用 `git diff` 审查修改。
6. 写实验记录，说明你为什么接受或拒绝 Claude Code 的建议。

## 禁止事项

- 禁止直接删除测试。
- 禁止只修改测试来让结果通过。
- 禁止未运行测试就提交。
- 禁止新增外部依赖。
- 禁止提交虚假的测试结果。

## 提交实验结果

提交内容至少包括：

- `lab-01-report.md`
- 初始失败测试日志
- 修复后测试日志
- Git diff 或 Pull Request 链接
- Claude Code 关键交互记录
- 人工判断和复盘
