---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

<!-- _class: lead -->

# Week 03：Claude Code 快速上手
## 从终端开始的 AI 协作

**课程 A：产品原型 + Claude Code 高级技能**

---

<!-- _class: lead -->

# 小林的进化

> 完成 Lab 02 本地项目后
> 她发现了新的问题：
> 只能在浏览器里用，无法操作本地项目

**她需要一个更专业的工具**
能在本地项目里长期协作

---

# 本周目标

- ⏱️ **学习时长**：约 2.5 小时
- 🎯 **产出物**：完成 Claude Code 安装配置，掌握核心操作
- 📚 **前置要求**：完成 Lab 02，能在本地启动一个小项目，熟悉基本终端操作
- 🏷️ **关键词**：Claude Code、AI 编程、终端工具、自然语言编程

---

# 学习路线

```
① 认识 Claude Code → ② 安装与配置 → ③ 核心技巧 → ④ 实战演练
```

**今天的核心**：
- 理解 Claude Code 的价值定位
- 完成安装和初始化配置
- 掌握 10+ 实用操作技巧
- 通过三个场景体验完整工作流

---

<!-- _class: lead -->

# Part 1
## 认识 Claude Code

---

# Bolt 的局限

小林把 Lab 02 的本地项目跑起来后发现的问题：

❌ 只能在浏览器里用，不能操作本地项目
❌ 生成的代码要手动复制粘贴
❌ 无法接入 Git、数据库等开发工具
❌ 每次都要重新描述项目背景

**她需要什么？**
一个能在本地项目里长期协作的 AI 伙伴

---

# 什么是 Claude Code？

**Claude Code** 是 Anthropic 官方推出的 AI 原生编程工具

**核心特点：**
1. **终端原生** - 直接在命令行里与 AI 对话
2. **项目记忆** - 通过 CLAUDE.md 记住项目信息
3. **完整工作流** - 从需求分析到代码实现到 Git 提交
4. **自然语言驱动** - 用人话描述需求，AI 自动编写代码

---

# 工具对比

| 工具 | 定位 | 适用场景 | 小林的评价 |
|------|------|----------|-----------|
| **Bolt** | 原型工具 | 快速验证想法 | 入门首选，但不适合长期维护 |
| **Claude Code** | 开发伙伴 | 本地项目开发 | 专业开发的核心工具 |
| **GitHub Copilot** | 代码补全 | 边写边提示 | 适合熟练开发者 |
| **Cursor** | AI IDE | 完整开发环境 | 功能强大但学习成本高 |

---

# 小林的选择逻辑

**三步走策略：**

1. 用 **Bolt** 快速做原型，验证想法
2. 用 **Claude Code** 在本地深度开发
3. 需要时配合 **Copilot** 提高编码速度

**为什么选择 Claude Code？**
- 低门槛：用自然语言就能工作
- 高天花板：支持完整的专业开发工作流

---

<!-- _class: lead -->

# Part 2
## 安装与配置

---

# 环境准备

**必需：**
- Node.js 18 或更高版本
- npm 或 yarn 包管理器
- 终端（Terminal / PowerShell / iTerm2）

**推荐：**
- Git（用于版本控制）
- 一个代码编辑器（VS Code / Sublime Text 等）

**检查 Node.js 版本：**
```bash
node --version
```

---

# 安装步骤

**方法一：手动安装（推荐）**

```bash
# 全局安装 Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version
```

**预期输出：**
```
claude-code/2.5.0
```

---

# 常见安装问题

**Q: 提示权限错误？**
```bash
# macOS/Linux
sudo npm install -g @anthropic-ai/claude-code

# Windows
# 以管理员身份运行 PowerShell
```

**Q: 安装很慢？**
```bash
# 使用国内镜像
npm install -g @anthropic-ai/claude-code \
  --registry=https://registry.npmmirror.com
```

---

# 首次启动

```bash
# 创建测试项目
mkdir ~/test-claude-code
cd ~/test-claude-code

# 启动 Claude Code
claude
```

**首次启动会引导你完成：**
1. 登录 Anthropic 账户（浏览器自动打开）
2. 选择使用计划（免费 / Pro）
3. 完成初始化配置

---

# 欢迎界面

```
欢迎使用 Claude Code！

我是 Claude，你的 AI 编程助手。我可以帮你：
- 编写和修改代码
- 解释复杂的技术概念
- 调试和优化程序
- 管理 Git 工作流
- 生成文档和测试

试试对我说：「你好，介绍一下你自己」
```

---

# 国内用户配置

**方案一：使用 API 代理服务**

```bash
# 在 ~/.bashrc 或 ~/.zshrc 中添加
export ANTHROPIC_API_KEY="your-api-key"
export ANTHROPIC_BASE_URL="https://api.your-provider.com/v1"

# 重新加载配置
source ~/.bashrc
```

**方案二：让 AI 帮你配置**
```
我购买了 XXX 服务商的 Anthropic API，
API 地址是 https://api.xxx.com，
密钥已经保存在本机环境变量 ANTHROPIC_API_KEY 中。
不要在对话、截图或 Git 里写出真实密钥。
请帮我配置 Claude Code 的环境变量。
```

---

<!-- _class: lead -->

# Part 3
## 快速开始：三个小实验

---

# 实验 1：对话

**目标：** 体验自然语言理解和多轮对话能力

**试试这些对话：**
```
什么是闭包？太长不看版本
```

```
JavaScript 和 TypeScript 有什么区别？
```

**观察要点：**
- Claude 的回答是否简洁准确？
- 它能否根据「太长不看」调整回答风格？
- 代码示例是否清晰易懂？

---

# 实验 2：生成文档

**目标：** 体验内容生成能力

```
帮我写一份 Git 常用命令的 Markdown 文档
要求：包含命令、说明、示例
```

**观察要点：**
- 文档结构是否清晰？
- 示例是否实用？
- 格式是否规范？

---

# 实验 3：编写游戏

**目标：** 体验从需求到运行的完整开发流程

```
用 Python 写一个猜数字游戏
要求：
1. 随机生成 1-100 的数字
2. 用户输入猜测
3. 提示「太大」或「太小」
4. 猜对后显示用了几次

写完后帮我运行它
```

---

# 三个实验的意义

**小林的理解：**

这三个实验展示了 Claude Code 的三个层次：

1. **理解层**：能听懂人话，给出准确回答
2. **创作层**：能生成结构化的内容
3. **执行层**：能写出可运行的代码

从对话到文档到代码，难度递增，但 Claude Code 都能胜任。

---

<!-- _class: lead -->

# Part 4
## 核心技巧：10 个必会操作

---

# 技巧 1：双击 Esc 回退对话

**快捷键：** 连续按两次 `Esc`

**作用：** 撤销上一轮对话，回到之前的状态

**按键说明：**
```
按 1 次 Esc  → 清除当前正在输入的内容
按 2 次 Esc  → 回退到上一次对话状态
按 3 次 Esc  → 清除所有对话历史
```

**重要提醒：**
双击 Esc 只回退对话状态，不会撤销文件修改
如需撤销文件修改，使用 Git

---

# 技巧 2：@ 引用文件

**符号：** `@`

**作用：** 精准指定 Claude 要读取的文件或目录

**基本用法：**
```
@src/utils.ts 解释这个文件
```

**高级用法：**
```
# 对比两个文件
@src/components/OldButton.tsx @src/components/NewButton.tsx 
对比这两个组件的差异

# 引用整个目录
@src/components/ 总结一下这个目录下的所有组件

# 引用特定行
@src/utils.ts:45-60 解释这段代码
```

---

# 为什么要用 @？

**对比：**

❌ **模糊描述**
```
解释 src/utils.ts 这个文件
```

✅ **精准引用**
```
@src/utils.ts 解释这个文件
```

**优势：**
- 更精准：Claude 知道你要的是哪个文件
- 省 Token：避免 Claude 读取不相关的文件
- 更快速：直接定位，不需要搜索

---

# 技巧 3：! 执行命令

**符号：** `!`

**作用：** 在 Claude Code 中直接执行终端命令

**基本用法：**
```
!npm test           # 运行测试
!git status         # 查看 Git 状态
!ls -la             # 列出文件
```

**实际应用：**
```
!npm test
# Claude 会执行测试，分析失败原因，并提供修复建议
```

---

# 技巧 4：/plan 先规划后编码

**命令：** `/plan`

**作用：** 对于复杂任务，先制定详细计划，再逐步执行

**使用方式：**
```
/plan
我想添加用户认证功能，请帮我制定实施计划
```

**Claude 会生成：**
- 阶段 1：数据库设计
- 阶段 2：后端 API
- 阶段 3：前端集成
- 阶段 4：测试

然后逐阶段执行

---

# 技巧 5：/init 自动生成配置

**命令：** `/init`

**作用：** 自动扫描项目，生成 `CLAUDE.md` 配置文件

**Claude 会做什么：**
1. 扫描项目结构
2. 识别技术栈（React / Vue / Next.js 等）
3. 分析配置文件（package.json、tsconfig.json）
4. 生成 CLAUDE.md

**为什么重要：**
`CLAUDE.md` 是 Claude Code 的「项目记忆」

---

# 技巧 6：/compact 压缩上下文

**命令：** `/compact`

**作用：** 压缩对话历史，节省 Token

**使用时机：**
- 对话进行了 5-6 轮后
- 感觉 Claude 开始「遗忘」之前的内容
- 要切换到新任务，但想保留关键背景

**工作原理：**
提取对话中的关键信息（决策、代码、需求），生成简洁摘要

---

# 技巧 7：/diff 查看改动

**命令：** `/diff`

**作用：** 打开交互式 diff 视图，查看当前未提交的改动

**使用场景：**
- 提交代码前检查改动
- 让 Claude 生成 commit message
- 代码审查

**完整工作流：**
```
/diff
# 查看改动

请基于当前 diff 生成一个 Conventional Commit message
# Claude 生成规范的提交信息
```

---

# 技巧 8：Shift+Tab 自动接受

**快捷键：** `Shift+Tab`

**作用：** 开启/关闭自动接受模式

**模式对比：**

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| 默认模式 | 每次修改都询问确认 | 学习阶段、重要代码 |
| 自动接受 | 直接应用修改 | 熟悉后、快速迭代 |

**注意事项：**
建议配合 Git 使用，出问题能回滚

---

# 技巧 9：Ctrl+C 取消操作

**快捷键：** `Ctrl+C`

**作用：** 取消当前正在执行的操作

**使用场景：**
- Claude 正在运行耗时命令，想中断
- Claude 开始生成大量不相关代码
- 意识到给错了指令，立即停止

**按键说明：**
```
按 1 次 Ctrl+C  → 取消当前操作
按 2 次 Ctrl+C  → 完全退出 Claude Code
```

---

# 技巧 10：/context 查看上下文

**命令：** `/context`

**作用：** 显示当前会话的上下文使用情况

**输出示例：**
```
📊 上下文使用情况

Token 使用：45,230 / 200,000 (22.6%)
文件引用：12 个文件
对话轮数：8 轮

最消耗 Token 的文件：
1. src/api/users.ts (3,420 tokens)
2. node_modules/@types/react/index.d.ts (2,890 tokens)
```

---

# 10 个技巧总结

| 技巧 | 快捷键/命令 | 作用 |
|------|------------|------|
| 回退对话 | `Esc Esc` | 撤销上一轮对话 |
| 引用文件 | `@` | 精准指定文件 |
| 执行命令 | `!` | 运行终端命令 |
| 规划任务 | `/plan` | 制定详细计划 |
| 生成配置 | `/init` | 自动生成 CLAUDE.md |
| 压缩上下文 | `/compact` | 节省 Token |
| 查看改动 | `/diff` | 查看未提交改动 |
| 自动接受 | `Shift+Tab` | 开启/关闭自动接受 |
| 取消操作 | `Ctrl+C` | 中断当前操作 |
| 查看上下文 | `/context` | 显示 Token 使用情况 |

---

<!-- _class: lead -->

# Part 5
## 核心配置

---

# CLAUDE.md - 项目记忆

`CLAUDE.md` 是 Claude Code 最重要的配置文件

**最小可用模板：**
```markdown
# [项目名称]

## 技术栈
- 框架：React 18 + TypeScript
- 状态管理：Zustand
- 样式方案：Tailwind CSS

## 常用命令
npm run dev      # 启动开发服务器
npm run test     # 运行单元测试

## 代码规范
- 组件使用函数组件 + Hooks
- 文件命名：PascalCase（组件）、camelCase（工具函数）
```

---

# .claudeignore - 节省 Token

`.claudeignore` 告诉 Claude Code 哪些文件不应该被读取

**推荐配置：**
```
# 依赖目录
node_modules/

# 构建产物
dist/
build/
.next/

# 日志文件
*.log

# 环境变量
.env
.env.local

# 大型资源文件
*.png
*.jpg
*.mp4
```

---

# 权限配置

通过 `.claude/settings.json` 控制 Claude 的操作权限

**配置示例：**
```json
{
  "permissions": {
    "allow": [
      "Bash(git status)",
      "Bash(npm test:*)",
      "Edit(src/**/*.ts)"
    ],
    "ask": [
      "Bash(git commit:*)",
      "Bash(npm install:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ]
  }
}
```

---

<!-- _class: lead -->

# Part 6
## 实战演练：三个完整场景

---

# 场景 1：Bug 修复工作流

**背景：** 测试失败，需要定位并修复问题

**完整流程：**
1. `!npm test` - 运行测试，发现失败
2. `@src/utils/validation.ts` - 定位问题文件
3. Claude 分析问题原因
4. Claude 修复代码
5. `!npm test` - 验证修复
6. `/diff` - 查看改动
7. Claude 生成 commit message

---

# 场景 2：新功能开发工作流

**背景：** 需要添加用户资料编辑功能

**完整流程：**
1. `/plan` - 制定实施计划
2. 阶段 1：创建 API
3. 阶段 2：前端表单
4. 阶段 3：测试
5. `!npm test` - 验证功能
6. `/diff` - 查看改动并提交

**关键点：** `/plan` 让复杂任务变得有条理

---

# 场景 3：代码审查工作流

**背景：** 完成开发后，需要审查代码质量

**完整流程：**
1. `/diff` - 查看所有改动
2. 请 Claude 审查代码
3. Claude 指出潜在问题：
   - 安全问题（密码字段未排除）
   - 性能问题（频繁验证）
   - 用户体验（缺少 loading 状态）
4. Claude 修复所有问题
5. `!npm test` - 验证修复

---

# 三个场景的共同点

**对话式开发流程：**

1. 用自然语言描述需求
2. Claude 分析并给出方案
3. 逐步执行，随时调整
4. 验证结果，确保质量

**小林的感受：**
> 不是在「使用工具」，而是在「与伙伴协作」

---

<!-- _class: lead -->

# 常见问题与解决方案

---

# Q1: Token 消耗太快怎么办？

**诊断：**
```
/context
```

**解决方案：**
1. 完善 `.claudeignore`
2. 定期压缩上下文 `/compact`
3. 精准引用文件 `@src/utils/auth.ts`

---

# Q2: Claude 不理解我的项目怎么办？

**解决方案：**
1. 生成 CLAUDE.md：`/init`
2. 手动补充项目信息
3. 即时补充上下文

---

# Q3: 如何回退 Claude 的操作？

**回退对话：**
```
双击 Esc
```

**回退文件修改：**
```bash
git diff              # 查看改动
git checkout -- .     # 撤销所有改动
```

**预防措施：**
```bash
git add .
git commit -m "WIP: before claude session"
```

---

# Q4: 权限提示太多怎么办？

**编辑 `.claude/settings.json`：**

将常用的安全操作加入 `allow` 列表

```json
{
  "permissions": {
    "allow": [
      "Bash(git status)",
      "Bash(npm test:*)",
      "Edit(src/**/*.ts)"
    ]
  }
}
```

---

<!-- _class: lead -->

# 本周回顾

---

# 学习进度检查

✅ 理解 Claude Code 的价值（与 Bolt、Copilot、Cursor 的区别）
✅ 完成安装与配置（成功安装，能正常使用）
✅ 掌握 10 个核心技巧（Esc、@、!、/plan、/init 等）
✅ 理解配置文件（CLAUDE.md、.claudeignore、settings.json）
✅ 完成三个实战场景（Bug 修复、新功能开发、代码审查）
✅ 能独立解决常见问题（优化 Token、回退操作、配置权限）

---

# 自测题

**1. Claude Code 与 Bolt 的核心区别是什么？**
**2. 双击 Esc 和 Ctrl+C 有什么区别？**
**3. 为什么要用 @ 引用文件？**
**4. /plan 命令适合什么样的任务？**
**5. CLAUDE.md 文件的作用是什么？**

---

# 本周作业

**必做**：
- 在自己的项目中安装 Claude Code
- 完成三个小实验（对话、生成文档、编写游戏）
- 尝试使用 10 个核心技巧中的至少 5 个
- 生成项目的 CLAUDE.md 配置文件

**选做**：
- 用 Claude Code 完成一个完整的功能开发
- 分享你的使用心得到课程讨论区

---

<!-- _class: lead -->

# 下周预告
## CLAUDE.md 深度配置

**从基础配置到高级定制**
**让 Claude 真正理解你的项目**
**成为团队的一员**

---

<!-- _class: lead -->

# Q&A
## 有问题吗？

---

<!-- _class: lead -->

# 谢谢！
## 期待下周见到你的 Claude Code 配置

**记住**：
> Claude Code 不是工具，是伙伴
> 用自然语言说出需求
> 与 AI 对话细化方案
> 验证结果并迭代优化
