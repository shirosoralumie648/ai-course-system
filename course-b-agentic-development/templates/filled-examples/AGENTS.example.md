# AGENTS.md 示例：Repo 01 Small Bugfix

> 示例性质：已填写教学示例。用于展示 Agent 工作协议如何约束 `repo-01-small-bugfix/`。

## 1. Agent 工作原则

- 先计划，再修改，再测试，再审查。
- 小步修改，保持 diff 可读。
- 不确定时说明假设，不编造结论。
- 测试失败不能声称完成。
- 涉及测试、依赖、删除文件或范围扩大时必须进入 Human Gate。

## 2. 项目背景

- 项目名称：Repo 01 Small Bugfix
- 项目目标：训练学生使用 Claude Code 修复小型 Python 项目 bug。
- 当前阶段：Lab 01 初始 bugfix 项目。
- 主要用户：课程 B 学生、教师、助教。
- 当前任务范围：修复 `src/grade_utils.py` 中导致测试失败的业务逻辑。

## 3. 允许做什么

- 阅读 `src/grade_utils.py`。
- 阅读 `tests/test_grade_utils.py` 来理解期望行为。
- 运行 `python -m unittest discover -s tests -v`。
- 修改 `src/grade_utils.py`。
- 输出计划、diff 摘要、测试结果和风险说明。

## 4. 禁止做什么

- 删除或弱化测试。
- 修改 `teacher-guide.md` 或 `solution-notes.md`。
- 新增第三方依赖。
- 大规模重构目录结构。
- 修改与当前测试失败无关的行为。
- 未运行测试就写“测试通过”。

## 5. 文件访问边界

允许访问：

- `src/grade_utils.py`
- `tests/test_grade_utils.py`
- `README.md`

默认不访问：

- 虚拟环境目录
- 缓存目录
- 与实验无关的父级课程材料

## 6. 命令执行边界

允许执行：

```bash
python -m unittest discover -s tests -v
git status
git diff
```

禁止执行：

- 删除文件命令。
- 重置仓库命令。
- 网络访问命令。
- 依赖安装命令。

## 7. 网络访问边界

本实验默认不访问外部网络。若需要查官方文档，必须先说明原因并等待人工确认。

## 8. 依赖安装边界

本项目不需要第三方依赖。任何新增依赖建议都必须拒绝或进入 Human Gate。

## 9. 角色划分

| 角色 | 职责 | 禁止行为 |
| --- | --- | --- |
| Planner | 分析失败测试，提出修复计划 | 不直接改代码 |
| Coder | 只修改 `src/grade_utils.py` | 不修改测试 |
| Tester | 运行固定测试命令并保存日志 | 不伪造测试通过 |
| Reviewer | 审查 diff 是否聚焦和正确 | 不直接合并 |
| Human Gate | 确认是否允许修改测试或扩大范围 | 不跳过高风险审批 |

## 10. 标准任务流程

1. 运行初始测试。
2. Planner 输出失败原因和计划。
3. Human Gate 确认只修改业务代码。
4. Coder 小步修复。
5. Tester 运行固定测试。
6. Reviewer 检查 diff 和测试日志。
7. Human Gate 决定接受或返工。

## 11. 测试要求

- 修复前必须保存失败日志。
- 修复后必须保存通过日志。
- 不能运行测试时必须说明环境原因和风险。

## 12. 人工审批点

以下情况必须 Human Gate：

- 修改测试前。
- 新增依赖前。
- 修改 README 或教师说明前。
- 发现第三个无关问题并想顺手修复前。
- 测试失败但想提交前。

## 13. 失败处理策略

- 停止继续扩大修改。
- 保留当前 diff 和失败日志。
- 说明失败原因和下一步选择。
- 由 Human Gate 决定继续修复、回退或重新规划。

## 14. 输出格式要求

每次任务结束输出：

- 修改摘要。
- 修改文件。
- diff 摘要。
- 测试命令和结果。
- 风险和不确定点。
- 是否需要 Human Gate。

## 15. 最小交付标准

- 有计划。
- 有初始失败日志。
- 有聚焦 diff。
- 有最终测试日志。
- 有人工接受或拒绝理由。
