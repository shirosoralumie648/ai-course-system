# Lab 04：Code Review Skill

> **完成比完美重要。** Skill 的第一版一定不完美，先让它能跑起来。

<ChapterIntroduction duration="2-3 小时" output="SKILL.md + Agent Review + 人工修订 Review + 复盘" prerequisite="已完成 Lab 01 或 Lab 02；已阅读 SKILL.md 模板" :tags="['Skill', '代码审查', '可复用流程', '人工修订']">

- Skill 和普通 Prompt 的本质区别
- 如何把代码审查流程封装成可复用的工程单元
- 如何对 Agent 生成的 Review 进行人工修订

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '① 阅读模板', description: '理解 SKILL.md 的 10 个必填部分' },
  { title: '② 编写 Skill', description: '写 code-review/SKILL.md' },
  { title: '③ Agent 执行', description: '用 Skill 让 Agent 生成 Review' },
  { title: '④ 人工修订', description: '修订 Agent 的 Review' },
  { title: '⑤ 对比', description: '有 Skill vs 无 Skill 的 Review 差异' },
  { title: '⑥ 复盘', description: '总结收获' }
]" />

## 实验步骤

### 第一步：阅读 SKILL.md 模板

SKILL.md 必须包含 10 个部分：
1. Skill 名称
2. 适用场景
3. 触发条件
4. 输入要求
5. 执行步骤
6. 输出格式
7. 检查清单
8. 禁止行为
9. 示例输出
10. 版本日志

### 第二步：编写 code-review/SKILL.md

设计一个代码审查 Skill，它应该能：
- 检查需求符合度
- 检查功能正确性
- 检查代码质量
- 检查测试覆盖
- 检查安全风险
- 输出结构化的 Review 报告

### 第三步：用 Skill 让 Agent 生成 Review

用 Lab 01 或 Lab 02 的 diff 作为审查目标，让 Agent 按照你的 Skill 执行审查。

### 第四步：人工修订 Agent 的 Review

检查 Agent 的 Review：
- 有没有遗漏重要问题？
- 有没有误报（指出不存在的问题）？
- 评价是否具体、可操作？
- 有没有伪造测试结果？

### 第五步：对比分析

对比"有 Skill 的 Review"和"无 Skill 让 Agent 随便 Review"的差异。

<InfoCard icon="⚠️" variant="warning">
**Skill 常见错误：**
- Skill 只是普通 Prompt — 没有触发条件、输入要求、输出格式
- Review 只有笼统评价 — "代码质量不错"不可操作
- 伪造测试结果 — Review 中引用了没有实际运行的测试
</InfoCard>

## 提交要求

1. code-review/SKILL.md 文件
2. Agent 生成的 Review 原文
3. 人工修订后的 Review
4. 修订说明：改了什么、为什么改
5. 有 Skill vs 无 Skill 对比
6. 复盘

## 评分标准

| 维度 | 分值 | 说明 |
|---|---|---|
| SKILL.md 结构完整性 | 25 分 | 10 个部分是否齐全 |
| Skill 可执行性 | 20 分 | Agent 能否按 Skill 执行 |
| Review 质量 | 20 分 | 是否具体、可操作 |
| 人工修订质量 | 20 分 | 是否识别了 Agent Review 的问题 |
| 复盘反思 | 15 分 | 是否有真实收获 |
