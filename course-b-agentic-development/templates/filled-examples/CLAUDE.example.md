# CLAUDE.md 示例：Repo 01 Small Bugfix

> 示例性质：已填写教学示例。适用于 `examples/repo-01-small-bugfix/`，学生复制到其他项目时必须按真实项目修改。

## 1. 项目概述

- 项目名称：Repo 01 Small Bugfix
- 项目目标：提供一个小型 Python 成绩统计函数库，用于训练 Claude Code 修复测试暴露的 bug。
- 当前版本：Lab 01 初始版本
- 当前最重要的交付：修复 `average_score` 和 `pass_rate` 的边界行为，并让测试通过。

## 2. 当前目标

- 当前任务：分析并修复 `python -m unittest discover -s tests -v` 暴露的失败。
- 验收标准：5 个 `unittest` 测试全部通过。
- 不属于本轮范围：重写项目结构、修改测试期望、新增依赖、增加未要求的新功能。

## 3. 技术栈

- 语言：Python 3.10+
- 框架：无
- 包管理器：无第三方依赖
- 测试框架：Python 标准库 `unittest`
- 构建工具：无
- 部署方式：无

## 4. 目录结构

```text
repo-01-small-bugfix/
├── src/grade_utils.py
├── tests/test_grade_utils.py
├── README.md
├── teacher-guide.md
└── solution-notes.md
```

## 5. 关键架构决策

- 保持项目极小，方便学生聚焦 Agent 工作流。
- 使用 Python 标准库测试，降低安装复杂度。
- 测试表达课程策略：空成绩列表平均分为 `0.0`，60 分计入及格。

## 6. 代码风格

- 函数保持短小。
- 不引入类或复杂抽象。
- 边界条件用显式 `if` 处理。
- 不添加与实验目标无关的日志或打印。

## 7. 测试命令

```bash
python -m unittest discover -s tests -v
```

Claude Code 必须展示修复前失败和修复后通过的测试结果。不能运行测试时必须说明原因。

## 8. 构建命令

本项目没有构建步骤。

## 9. 运行命令

本项目不提供独立应用入口，只通过测试验证。

## 10. 禁止修改区域

未经人工确认，不允许修改：

- `tests/test_grade_utils.py`
- `teacher-guide.md`
- `solution-notes.md`
- `pyproject.toml`
- 与当前 bugfix 无关的文件

## 11. 安全注意事项

- 不读取或输出密钥、Token、密码。
- 不新增网络访问。
- 不新增第三方依赖。
- 不把测试失败伪装成测试通过。

## 12. 常见任务流程

1. 复述当前失败测试和假设。
2. 阅读 `src/grade_utils.py` 与 `tests/test_grade_utils.py`。
3. 先给出修复计划和拟修改文件。
4. 等待人工确认后只修改 `src/grade_utils.py`。
5. 展示 diff 摘要。
6. 运行 `python -m unittest discover -s tests -v`。
7. 输出测试结果、风险和是否需要人工复核。

## 13. 提交规范

- Commit 信息建议：`fix: correct grade boundary handling`
- 一次提交只包含本次 bugfix。
- 不提交缓存、虚拟环境或无关文件。

## 14. Review checklist

- 是否只修改了 `src/grade_utils.py`。
- 是否处理了空列表平均分。
- 是否把 60 分计入及格。
- 是否保留原有 letter grade 行为。
- 是否运行了固定测试命令。
- 是否需要 Human Gate。

## 15. 不确定事项处理规则

- 如果测试输出和 README 不一致，先停止并报告。
- 如果需要修改测试，必须进入 Human Gate。
- 如果发现需求之外的问题，只记录风险，不顺手重构。
