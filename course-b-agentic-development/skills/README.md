# Course B Skills

## 用途

本目录保存课程 B 中用于教学的 Skill 示例。Skill 是可复用流程单元，不是普通 Prompt。它应当明确适用场景、输入要求、执行步骤、输出格式、检查清单和禁止行为。

## 当前 Skill

- `code-review/SKILL.md`：结构化代码审查 Skill，用于审查一次代码修改。

## 使用原则

- 使用 Skill 前要提供任务说明、diff、测试结果和项目规则。
- Skill 输出不能替代人工判断。
- Skill 必须标记不确定项和 Human Gate。
- 不允许编造测试结果。

## 可扩展 Skill 类型

课程可在当前 code-review Skill 之外继续扩展 debug、test-generation、release-check、security-review 等 Skill。每个新增 Skill 都必须绑定真实教学场景、输入材料、输出格式、禁止行为和评分标准，不能只写成一段通用 Prompt。
