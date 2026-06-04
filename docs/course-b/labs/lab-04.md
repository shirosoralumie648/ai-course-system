# Lab 04：现代 CLI 与 Git 版本管理

<ChapterIntroduction duration="2-3 小时" output="一套可复现的 CLI/Git 操作记录 + 一个小功能改动 + Git diff + 测试日志" prerequisite="完成 Lab 03；能使用终端、Git 和至少一种 AI 编程工具；项目可本地运行" :tags="['现代 CLI', 'Git', '版本管理', 'GitHub', 'diff 审查']">

- 用命令行和 Git 完成一次可审计的小改动
- 用 AI 辅助开发，但保留人工审查、测试和提交证据
- 建立“先看 diff，再相信结果”的工作习惯

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '建分支', description: '确认状态并创建实验分支' },
  { title: '定任务', description: '写清楚小功能和验收标准' },
  { title: 'AI 辅助', description: '记录 prompt、计划和执行过程' },
  { title: '审查 diff', description: '逐项检查改动范围' },
  { title: '运行验证', description: '保存测试或构建日志' },
  { title: '提交复盘', description: '形成 commit 和工作流记录' }
]" />

## 实验目标

完成一次小而完整的工程改动，并用 Git、diff、测试日志证明改动可审计。重点不是功能复杂度，而是过程是否专业、可复现、可回滚。

## 实验任务

在你的课程项目中完成一个小功能或小修复，例如：

- 给 Lab 03 的组件增加 loading 或 disabled 状态
- 修复移动端布局问题
- 增加一个空状态组件
- 给表单增加基础校验
- 增加一个最小单元测试或组件测试

改动应控制在 1-5 个文件内，避免大范围重构。

## 操作步骤

### 1. 检查工作区并创建分支

运行：

```bash
git status
git branch
git switch -c lab-04-ai-workflow
```

如果你在共享仓库中工作，先确认没有覆盖同学或老师的改动。保存 `git status` 输出。

### 2. 写任务说明和验收标准

在动手前写清楚：

- 要改什么
- 不改什么
- 涉及哪些文件
- 如何验证成功
- 哪些行为需要人工确认

示例：

```text
任务：给 AppButton 增加 loading 状态。
范围：只修改 AppButton 和使用示例页面。
验收：loading=true 时按钮不可重复点击，显示加载文本；现有按钮样式不变；npm run build 通过。
```

### 3. 使用 AI 工具辅助实现

可以使用 Claude Code、Codex、Cursor、Trae 或其他工具。记录：

- 你给 AI 的任务描述
- AI 的计划或关键回复
- AI 修改了哪些文件
- 你是否拒绝或调整了它的建议

不要让 AI 在没有说明的情况下大范围重写项目。

### 4. 审查 Git diff

运行：

```bash
git diff
```

检查：

- 改动是否在任务范围内
- 是否引入无关格式化
- 是否暴露密钥或本地路径
- 是否破坏组件 API
- 是否遗漏测试或验证

保存 diff 文本或截图。

### 5. 运行验证命令

根据项目实际情况至少运行一种：

```bash
npm run lint
npm run test
npm run build
npm run dev
```

如果项目没有测试命令，至少运行本地开发服务并截图验证页面。保存终端日志。

### 6. 提交并复盘

提交改动：

```bash
git add .
git commit -m "lab-04: add verified workflow change"
```

写 200-400 字复盘：AI 帮了什么、你人工发现了什么、diff 审查是否拦住了问题、下次会怎样缩小任务。

## 提交要求

- `git status` 初始输出
- 分支名和 commit hash
- 任务说明和验收标准
- AI prompt 或对话摘要
- `git diff` 文本或截图
- 测试、构建、lint 或运行日志
- 功能截图或本地 URL
- 复盘

## 验收标准

- 有独立分支或清晰 commit
- 改动范围与任务说明一致
- diff 无密钥、无无关大改、无删除他人内容
- 至少有一种验证日志
- 复盘中包含具体人工判断，而不是只写“AI 很好用”

## 常见问题

**没有测试怎么办？**
可以用 `npm run build`、`npm run lint` 或手动运行截图替代，但要说明项目当前缺少自动化测试。

**AI 改了很多文件怎么办？**
先不要提交。用 diff 找出无关改动，要求 AI 缩小范围，或手动只保留必要改动。

**必须 commit 吗？**
建议 commit。若课程平台不允许提交，也必须提供 diff 和改动文件清单。

## 评分标准

| 维度 | 分值 | 说明 |
|---|---:|---|
| 任务边界 | 15 | 改动是否小而清楚 |
| Git 证据 | 20 | 分支、diff、commit 是否完整 |
| AI 使用记录 | 20 | 是否记录计划、调整和人工判断 |
| 验证质量 | 25 | 测试、构建或运行证据是否可信 |
| 复盘质量 | 20 | 是否有具体工程收获 |
