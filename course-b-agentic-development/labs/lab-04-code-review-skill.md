# Lab 04：Code Review Skill

> **完成比完美重要。** Skill 的第一版一定不完美，先让它能跑起来。

| 项目 | 内容 |
|---|---|
| **适用周次** | 第 7 周 |
| **预计时长** | 2-3 小时 |
| **核心产出** | code-review/SKILL.md + Agent 生成的 Review + 人工修订后的 Review + 复盘 |
| **前置条件** | 已完成 Lab 01 或 Lab 02，有一份可审查 diff；已阅读 SKILL.md 模板 |

**你将学到：**
- Skill 和普通 Prompt 的本质区别
- 如何把代码审查流程封装成可复用的工程单元
- 如何对 Agent 生成的 Review 进行人工修订

**实验步骤概览：**

```
① 阅读 SKILL.md 模板，理解 10 个必填部分   ⏱️ ~15min
② 编写 code-review/SKILL.md                 ⏱️ ~30min
③ 用 Skill 让 Agent 生成 Review              ⏱️ ~15min
④ 人工修订 Agent 的 Review                   ⏱️ ~25min
⑤ 对比 Skill Review 和无 Skill 的差异        ⏱️ ~15min
⑥ 复盘                                       ⏱️ ~20min
```

**工具不可用怎么办？**
- Skill 文件本身不依赖 Agent，手动编写即可
- 可以用 Lab 01 或 Lab 02 的历史 diff 手动写一份 Review 作为对照
- 在报告中说明"本次 Review 为手动完成，未经过 Agent 执行"

---

## 1. 实验名称

Code Review Skill：把代码审查流程封装成可复用 Skill。

## 5. 实验背景

真实软件工程中，代码修改不能只看“能运行”。Review 需要检查需求符合度、功能正确性、代码质量、架构一致性、测试覆盖、安全风险和文档完整性。Skill 可以把这个流程固化成 Agent 可重复执行的标准。

## 6. 使用工具

- Claude Code、Codex 或其他可读取 Skill 的 Agent。
- Markdown。
- Git diff。

## 7. 示例项目说明

优先使用 Lab 01 或 Lab 02 的修改作为审查对象：

- `../examples/repo-01-small-bugfix/`
- `../examples/repo-02-feature-development/`

也可以由教师提供一份包含明显问题的 Pull Request diff。

固定验证命令：

```bash
python -m unittest discover -s tests -v
```

Review 报告中引用的测试结果必须来自该命令或教师明确指定的等价命令。不能运行测试时，Review 必须标记“测试证据不足”。

## 8. 实验任务

创建 `code-review/SKILL.md`，必须包含：

1. Skill 名称。
2. 适用场景。
3. 触发条件。
4. 输入要求。
5. 执行步骤。
6. 输出格式。
7. 检查清单。
8. 禁止行为。
9. 示例 Review 输出。
10. 版本记录。

## 9. 操作步骤

1. 复制 `templates/SKILL.md` 作为基础。
2. 编写 code-review Skill。
3. 准备一份 diff 和任务说明。
4. 让 Agent 使用该 Skill 生成 Review。
5. 人工审查 Agent Review，标记错误、遗漏和不确定项。
6. 生成修订后的 Review。
7. 复盘 Skill 哪些规则有效，哪些需要改进。

## 10. 记录要求

必须记录：

- Skill 设计意图。
- 输入给 Agent 的任务说明和 diff。
- Agent 生成的原始 Review。
- 人工修订后的 Review。
- Agent 编造或不确定的地方。
- Skill 下一版改进点。

## 11. 预期结果

- Skill 结构完整。
- Review 输出结构化、可审计。
- Review 不编造测试结果。
- 学生能说明人工修订的原因。

## 12. 提交要求

- `code-review/SKILL.md`。
- 一份用该 Skill 生成的 Review 报告。
- 一份人工修订后的 Review 报告。
- 复盘。

## 13. 提交检查表

- 是否提交实验记录。
- 是否提交关键 Prompt / Agent 指令。
- 是否提交 `code-review/SKILL.md`。
- 是否提交待审查 Git diff。
- 是否提交测试结果或说明测试无法运行的原因。
- 是否提交 Agent 生成的原始 Review。
- 是否提交人工修订后的 Review。
- 是否提交失败记录，例如 Agent 编造测试结果或遗漏风险的案例。
- 是否说明人工判断。
- 是否说明没有完成的部分；如果全部完成，明确写“无未完成项”。
- 是否有复盘。

## 14. 助教验收标准

- 文件是否齐全：Skill、diff、原始 Review、人工修订 Review、测试证据、复盘。
- 任务是否完成：Skill 包含适用场景、触发条件、输入要求、执行步骤、输出格式、检查清单、禁止行为和版本记录。
- 测试是否真实：Review 中引用的测试结果必须来自学生提交的日志。
- 是否存在伪造测试结果：Skill 必须要求“信息不足时不做确定结论”。
- 是否符合规则边界：Skill 不应直接合并代码或绕过 Human Gate。
- 是否能解释 AI 修改结果：学生应能说明人工修订了哪些 Agent Review 内容。

## 15. 常见错误

- Skill 只是“请帮我审查代码”。
- Review 只有笼统评价。
- Agent 假设测试已经运行。
- 缺少安全检查。
- 没有人工确认建议。

## 16. 拓展任务

- 为不同项目类型添加专门检查项，例如 API、安全、前端、CLI。
- 让另一个同学使用你的 Skill 审查同一 diff。
- 把 Review 输出转成 Pull Request 评论格式。

## 17. 评分标准

| 评分项 | 分值 | 优秀标准 | 合格标准 | 常见扣分 |
| --- | --- | --- | --- | --- |
| Skill 结构 | 25 | 适用场景、触发、输入、步骤、输出、禁止行为完整 | 主要结构完整 | 缺关键栏目 |
| Checklist 质量 | 25 | 覆盖功能、架构、测试、安全、文档 | 覆盖主要维度 | 检查项笼统 |
| Review 可审计性 | 25 | 有风险等级、必须修改项、测试建议和 Gate | 有基本 Review | 只写总体评价 |
| 人工修订 | 25 | 能指出 Agent 错误和不确定点 | 有简单修订 | 不做人工判断 |

## 18. 复盘问题

1. Skill 与普通 Prompt 的差异是什么？
2. Agent Review 哪些地方不可靠？
3. 哪些检查项应成为必须修改项？
4. 什么时候 Reviewer 应建议 Human Gate？
