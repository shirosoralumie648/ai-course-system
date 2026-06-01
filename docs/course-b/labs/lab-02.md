# Lab 02：Codex Code Change

> **完成比完美重要。** 工具不可用时如实记录，不要伪造结果。

<ChapterIntroduction duration="2-3 小时" output="任务说明 + Prompt + diff + 测试 + 工具对比记录" prerequisite="已安装 Codex；已完成 Lab 01" :tags="['Codex', 'sandbox', 'approval', '权限边界', '工具对比']">

- Codex 如何制定计划、执行修改、请求审批
- sandbox、approval 和权限边界的实际含义
- Claude Code 与 Codex 的交互方式差异（基于证据）

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '① 阅读项目', description: '理解要做什么功能' },
  { title: '② 写任务描述', description: '写好验收标准' },
  { title: '③ 给 Codex 下达任务', description: '记录它的计划' },
  { title: '④ 审批 + 审查', description: '审批操作，审查 diff，运行测试' },
  { title: '⑤ 对比表', description: '填写 Claude Code vs Codex 对比' },
  { title: '⑥ 复盘', description: '总结收获' }
]" />

## 实验背景

本实验使用 `repo-02-feature-development`，一个 todo-filter Python 项目。你需要用 Codex 给任务列表工具新增"按状态过滤标题"的功能。

## 实验步骤

### 第一步：阅读示例项目

```bash
cd ai-course-system/course-b-agentic-development/examples/repo-02-feature-development
python -m unittest discover -s tests -v
```

确认现有测试全部通过。

### 第二步：写任务描述和验收标准

在给 Codex 下达任务前，先写清楚：
- 要做什么：新增 `filter_titles_by_status()` 函数
- 验收标准：按状态过滤标题，返回匹配的标题列表
- 约束：不破坏现有功能，必须补充测试

### 第三步：给 Codex 下达任务

记录 Codex 的计划、它请求的权限、它的执行步骤。

### 第四步：审批、审查、测试

- 审批 Codex 请求的操作
- 用 `git diff` 审查所有改动
- 运行测试验证

### 第五步：填写对比表

| 维度 | Claude Code（Lab 01） | Codex（本次） |
|---|---|---|
| 任务描述方式 | | |
| 计划生成方式 | | |
| 执行模式 | | |
| 审批机制 | | |
| diff 审查体验 | | |
| 测试验证方式 | | |

## 工具不可用怎么办？

- 记录错误截图或日志
- 手动完成功能修改，保留完整 diff 和测试结果
- 在对比表中写明"Codex 不可用，以下为手动流程"
- 这会被视为 Alpha 反馈，不会直接判零分

## 提交要求

1. 任务描述和验收标准
2. Codex 的计划记录
3. 审批决定和理由
4. Git diff
5. 测试结果
6. Claude Code vs Codex 对比表
7. 复盘

## 评分标准

| 维度 | 分值 | 说明 |
|---|---|---|
| 任务描述质量 | 15 分 | 验收标准是否清晰 |
| 可审计过程 | 25 分 | 计划、审批、diff 是否完整记录 |
| 测试证据 | 25 分 | 是否有修复前后完整测试日志 |
| 对比分析 | 20 分 | 是否有具体证据支持对比结论 |
| 提交完整性 | 15 分 | 7 项是否齐全 |
