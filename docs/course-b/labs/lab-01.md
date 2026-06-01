# Lab 01：Claude Code Bugfix

> **完成比完美重要。** 这个实验不要求你一次做对，只要求你真实记录每一步。

<ChapterIntroduction duration="2-3 小时" output="实验记录 + 修复前后测试日志 + Git diff + 复盘" prerequisite="已安装 Claude Code；能使用 Git 和命令行" :tags="['Claude Code', 'diff 审查', '测试验证', '人工判断']">

- Claude Code 如何阅读项目、理解错误、提出修复计划
- 如何审查 Agent 的 diff，而不是盲目接受
- 如何运行测试并用证据证明修改正确

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '① 运行失败测试', description: '观察错误，保存日志' },
  { title: '② 让 Claude Code 分析', description: '观察它如何理解问题' },
  { title: '③ 审查修复计划', description: '决定是否批准' },
  { title: '④ 审查 diff + 测试', description: '逐行看改动，运行测试' },
  { title: '⑤ 记录复盘', description: '总结收获和教训' }
]" />

## 实验背景

本实验使用课程仓库内置示例项目 `repo-01-small-bugfix`，一个小型 Python 成绩工具库，包含故意保留的 bug。测试初始状态应失败。

重点不是"让 Claude Code 直接改完"，而是观察和记录 Agentic Development 的工程过程。

## 实验步骤

### 第一步：进入项目，运行失败测试

```bash
cd ai-course-system/course-b-agentic-development/examples/repo-01-small-bugfix
python -m unittest discover -s tests -v
```

保存失败日志，记录你观察到的错误信息。

### 第二步：让 Claude Code 分析问题

启动 Claude Code，让它阅读项目并分析测试失败原因。

**关键**：要求它先给计划，不要直接修改。

### 第三步：审查修复计划

Claude Code 给出计划后，你决定：
- 批准：计划合理，继续执行
- 修改：计划有部分问题，要求调整
- 拒绝：计划方向错误，重新描述任务

### 第四步：审查 diff，运行测试

Claude Code 修改代码后：
1. 用 `git diff` 查看所有改动
2. 逐行审查：改了什么？为什么改？有没有改错？
3. 运行测试：`python -m unittest discover -s tests -v`
4. 记录测试结果

**审查 diff 示例：**

<DiffViewer title="示例：修复 calculate_average 函数" diff="@@ -10,7 +10,7 @@
 def calculate_average(scores):
     if not scores:
-        return 0
+        return None
     total = 0
     for score in scores:
-        total += score
-    return total / len(scores)
+        if isinstance(score, (int, float)):
+            total += score
+    count = len([s for s in scores if isinstance(s, (int, float))])
+    return total / count if count > 0 else None" />

<InfoCard icon="🔍" variant="tip">
**审查要点：**
- 改动是否符合修复计划？
- 是否引入了新的 bug？
- 边界情况是否处理了？
- 代码风格是否一致？
</InfoCard>

### 第五步：写实验记录和复盘

<InfoCard icon="⚠️" variant="warning">
**不要做的事：**
- 不要跳过 diff 审查直接看测试结果
- 不要测试没跑就声称通过
- 不要在实验开始前看 `solution-notes.md`
</InfoCard>

## 提交要求

1. 初始测试失败日志
2. Claude Code 的分析和修复计划记录
3. 你的审批决定和理由
4. Git diff 输出
5. 修复后测试通过日志
6. 复盘：这次实验让你对 Agentic Development 有什么新理解？

## 工具不可用怎么办？

- 记录错误截图或日志（如 `claude --version` 输出）
- 手动完成修复，保留完整 diff 和测试结果
- 在报告中写明"Claude Code 不可用，以下为手动流程"
- 这会被视为 Alpha 反馈，不会直接判零分

<InfoCard icon="💡" variant="tip">
**关键教训：** Agentic Development 的核心不是"让 AI 做完"，而是"让 AI 做，你审查"。如果你跳过了 diff 审查，你就不知道 AI 到底改了什么——这比不用 AI 更危险。
</InfoCard>

## 评分标准

| 维度 | 分值 | 说明 |
|---|---|---|
| Bug 理解 | 20 分 | 是否准确描述了问题和原因 |
| Diff 审查 | 25 分 | 是否逐行审查，是否有审批判断 |
| 测试证据 | 25 分 | 是否有修复前后完整测试日志 |
| 复盘质量 | 20 分 | 是否有真实收获 |
| 提交完整性 | 10 分 | 6 项是否齐全 |
