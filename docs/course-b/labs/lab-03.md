# Lab 03：Project Rules

> **完成比完美重要。** 规则文件不需要一步到位，先写能用的，再迭代。

<ChapterIntroduction duration="2-3 小时" output="CLAUDE.md + AGENTS.md + 有无规则对比记录 + 复盘" prerequisite="已完成 Lab 01 或 Lab 02" :tags="['CLAUDE.md', 'AGENTS.md', '规则文件', '工程边界']">

- 规则文件为什么是 Agentic Development 的工程边界
- 如何编写具体、可执行、可审查的项目规则
- 有规则和无规则时 Agent 输出的实际差异

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '① 无规则分析', description: '让 Agent 分析任务，记录输出' },
  { title: '② 编写 CLAUDE.md', description: '写项目级规则' },
  { title: '③ 编写 AGENTS.md', description: '写 Agent 行为规范' },
  { title: '④ 有规则分析', description: '同一任务再让 Agent 分析' },
  { title: '⑤ 对比复盘', description: '对比两次输出差异' }
]" />

## 实验步骤

### 第一步：无规则让 Agent 分析任务

选 Lab 01 或 Lab 02 的示例项目，在**没有** CLAUDE.md 和 AGENTS.md 的情况下，让 Agent 分析一个任务。记录：
- Agent 的理解是否准确
- 是否遗漏了重要约束
- 是否提出了不合理的修改方案

### 第二步：编写 CLAUDE.md

CLAUDE.md 必须包含：
- 项目目标（一句话说清楚）
- 技术栈
- 目录结构
- 测试命令
- 允许修改的范围
- 禁止修改的范围
- 代码风格要求

### 第三步：编写 AGENTS.md

AGENTS.md 必须包含：
- Agent 的角色定位
- 允许的操作
- 禁止的操作
- 危险操作的人工审批要求
- 输出格式要求

### 第四步：有规则让 Agent 分析同一任务

用同样的任务，让 Agent 在有规则文件的情况下重新分析。记录：
- Agent 的理解是否更准确
- 是否遵守了规则中的约束
- 是否主动提出需要人工审批的操作

### 第五步：对比分析

| 维度 | 无规则 | 有规则 |
|---|---|---|
| 任务理解准确性 | | |
| 约束遵守程度 | | |
| 安全边界意识 | | |
| 输出可审计性 | | |

<InfoCard icon="⚠️" variant="warning">
**规则文件常见错误：**
- "写高质量代码" — 不可执行，Agent 不知道什么是"高质量"
- 没有测试命令 — Agent 无法验证修改是否正确
- 没有 Human Gate — 所有操作都自动执行，没有人工审核
</InfoCard>

## 提交要求

1. 无规则时 Agent 的输出记录
2. CLAUDE.md 文件
3. AGENTS.md 文件
4. 有规则时 Agent 的输出记录
5. 对比分析表
6. 规则设计说明：为什么写这些规则？
7. 复盘

## 评分标准

| 维度 | 分值 | 说明 |
|---|---|---|
| CLAUDE.md 质量 | 25 分 | 是否具体、可执行、无空话 |
| AGENTS.md 质量 | 25 分 | 角色边界是否清晰 |
| 对比分析深度 | 25 分 | 是否有具体证据支持差异 |
| 复盘反思 | 15 分 | 是否有真实收获 |
| 提交完整性 | 10 分 | 7 项是否齐全 |
