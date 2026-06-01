# Week 10：Skills

## 给 Claude Code 装上「技能包」

**课程 A：产品原型 + Claude Code 高级技能**

* * *

# 小林的困扰

> 用了几周 Claude Code 每次都要重复解释代码风格、提交规范 直到她听说有个叫 Skills 的东西 可以让 Claude Code 一次学会、永久记住

**那一刻她意识到：AI 编程不只是对话，更是知识沉淀**

* * *

# 本周目标

-   ⏱️ **学习时长**：约 2.5 小时
-   🎯 **产出物**：至少 3 个自定义 Skill，一份可提交到 Git 的 `.claude/skills/` 目录
-   📚 **前置要求**：学完前几章 Claude Code 基础
-   🏷️ **关键词**：Skills、知识管理、工作流自动化、团队协作

* * *

# 学习路线

```
① 认识 Skills → ② 安装与使用 → ③ 创建自定义 Skills
```

**今天的核心**：

-   理解 Skills 的本质与价值
-   体验社区 Skills 的强大功能
-   创建自己的技能包

* * *

# Part 1

## 什么是 Claude Code Skills？

* * *

# Skills 是什么？

**Claude Code Skills** 是一种将专业知识、工作流程和最佳实践打包成「可复用技能包」的功能。

**小林的理解方式**：

> 如果 Claude Code 是一个新员工 那 Skills 就是公司的「操作手册」 代码审查怎么做、Git 提交信息怎么写 全都写在手册里 新员工不用每次问，翻手册就行

* * *

# 为什么需要 Skills？

**没有 Skills 之前的问题**：

-   重复指令：每次都要解释代码风格、提交规范
-   知识无法沉淀：团队成员各自的经验无法共享
-   标准不统一：不同的人用 Claude，结果完全不同
-   效率低下：常见任务每次都要从头解释

**Skills 的价值**： 让 Claude 变成一个「有经验的团队成员」

* * *

# Skills 正在成为必备技能

**社区热度**：

-   GitHub 上 OpenSkills 项目已收获 7.2k stars
-   Vercel 推出 find-skills 工具
-   Anthropic 官方维护 Skills 仓库

**实用性强**：

-   从代码审查、Git 操作到视频制作、PPT 生成
-   覆盖多种场景
-   一次配置，反复使用

* * *

# Part 2

## 快速开始：安装第一个 Skill

* * *

# 第一步：安装 find-skills

**find-skills 是什么？** AI Agent 的「应用商店搜索器」

**安装命令**：

```bash
npx skills add vercel-labs/skills@find-skills -g -y
```

**使用方式**：

```
我需要做一个 React 组件的性能优化，
帮我找找有什么技能可以用
```

Claude 会自动搜索并推荐最合适的 Skill

* * *

# 为什么推荐先装 find-skills？

**没有 find-skills 之前**： 手动在 GitHub 搜索 → 逐个复制、安装、配置 → 反复调试

**有了 find-skills 之后**： 一句话描述需求 → AI 自动搜索 → 一键安装，立即可用

**核心价值**： 让 Skills 的发现和安装变得像对话一样简单

* * *

# 第二步：体验 Remotion 视频制作

**用 find-skills 搜索**：

```
帮我找找 Remotion 相关的技能，我想做视频
```

**安装 Remotion Skills**：

```bash
npx skills add remotion-dev/skills -g
```

**用它做个炫酷的文字动画视频**：

```
用 Remotion 做一个视频：
- 1920x1080，5 秒
- 一行文字 "Hello World" 从左边飞进来
- 同时带旋转和缩放效果
- 背景是渐变色
```

* * *

# 第三步：frontend-design 让界面变好看

**问题**： AI 生成的界面总是「看起来很土」

**解决方案**：

```bash
npx skills add anthropics/skills/frontend-design -g
```

**这个技能专门解决**：

-   独特的视觉风格（避开千篇一律的「AI 模板感」）
-   专业的配色和字体
-   流畅的动画效果
-   生产级别的代码质量

* * *

# 第四步：frontend-slides 快速制作 PPT

**核心特点**： 「展示而非讲述」——生成 3 个视觉预览让你选择

**安装**：

```bash
mkdir -p ~/.claude/skills/frontend-slides
# 从 GitHub 下载 SKILL.md 和 STYLE_PRESETS.md
```

**使用场景**：

```
/frontend-slides

我想创建一个 AI 创业项目的融资路演 PPT，大概 10 页
```

* * *

# frontend-slides 内置视觉风格

风格名称

特点

适用场景

**Neon Cyber**

未来科技感、粒子效果

技术分享、AI 产品

**Midnight Executive**

高端商务、值得信赖

商务汇报、融资路演

**Paper & Ink**

编辑风格、文学气息

内容创作、教育分享

**Swiss Modern**

简洁几何、包豪斯风格

设计作品、极简主义

**Brutalist**

原始大胆、抓人眼球

艺术展示、个性表达

生成的演示文稿是**单文件 HTML**，零依赖，10 年后还能打开

* * *

# 查看已安装的 Skills

**查看命令**：

```bash
npx skills list
```

**自动调用**： 当你向 Claude 提出相关任务时，它会自动调用对应的 Skill

**小林的体会**：

> 这些 Skills 让她意识到，AI 编程不只是「写代码」 还能做视频、做设计、做 PPT Claude Code 就像一个可以无限扩展的工具箱

* * *

# Part 3

## Skills 的核心概念

* * *

# Skills 是什么？

**Skills 是存储在文件系统中的「技能包」**：

```
my-skill/
├── SKILL.md          # 必需：技能定义文件
├── scripts/          # 可选：辅助脚本
├── templates/        # 可选：输出模板
├── references/       # 可选：参考文档
└── examples/         # 可选：示例文件
```

* * *

# Skills vs 提示词

传统提示词方式

使用 Skills

每次对话都要重复说

创建一次反复用

存在对话历史中，占用 Token

按需加载，节省 Token

无法在会话间共享

可以在团队中共享

难以版本控制

可以用 Git 管理

**核心区别**： 提示词是临时的，Skills 是持久化的

* * *

# Skills 的两种类型

**全局 Skills（个人）**：

-   存放位置：`~/.claude/skills/`
-   作用范围：所有项目
-   适用场景：个人通用技能（代码风格、Git 习惯）

**项目 Skills（团队）**：

-   存放位置：`项目目录/.claude/skills/`
-   作用范围：当前项目
-   适用场景：团队共享、项目特定规范

* * *

# Skills 如何工作

```
用户："帮我审查这个 PR"
         ↓
Claude 识别关键词 "审查" "PR"
         ↓
匹配到 review-pr skill 的 description
         ↓
加载 SKILL.md 完整内容
         ↓
按照技能定义的流程执行
```

**关键机制**： 基于 description 字段的自动匹配

* * *

# SKILL.md 文件结构

**第一部分：YAML Frontmatter（元数据）**

```yaml
---
name: skill-name              # 技能名称
description: 简短描述         # 用于 Claude 自动匹配
category: development         # 分类
tags:                         # 标签
  - code
  - automation
---
```

**第二部分：Markdown 内容（指令）**

-   使用场景
-   执行步骤
-   注意事项

* * *

# 关键字段说明

字段

必填

说明

`name`

是

技能名称，只能用小写字母、数字、连字符

`description`

是

技能描述，越具体越容易被 Claude 自动匹配

`category`

否

分类标签

`tags`

否

更多分类标签

`allowed-tools`

否

允许使用的工具，无需权限即可用

**最关键的是 description**： 包含 2-3 个核心关键词 + 一句使用场景描述

* * *

# Skills vs MCP：有什么区别？

维度

Skills

MCP

**本质**

知识和流程

工具和接口

**提供什么**

告诉 AI「怎么做」

给 AI「能用什么」

**存储位置**

`skills/` 目录

MCP 服务器

**配置方式**

Markdown 文件

JSON 配置文件

**触发方式**

`/skill-name` 或自动识别

通过配置自动加载

**形象比喻**：

-   MCP 是「工具」（扳手、电脑、访问权限）
-   Skills 是「操作手册」（怎么做代码审查、怎么提交代码）

* * *

# Part 4

## 如何创建自己的 Skills

* * *

# 方法一：直接让 Claude 帮你创建

**示例**：

```
请帮我创建一个名为「format-code」的 skill，
功能是自动格式化代码。

要求：
1. 自动检测编程语言类型
2. 应用对应的格式化规则
3. 返回格式化前后的 diff
```

**Claude 会自动**：

1.  创建目录结构
2.  生成 SKILL.md 文件
3.  填写 YAML frontmatter
4.  编写技能内容

* * *

# 方法二：使用 skill-creator

**安装**：

```bash
npx skills add anthropics/skills@skill-creator -g
```

**使用**：

```
/skill-creator
```

**引导流程**：

1.  技能名称
2.  功能描述
3.  使用场景
4.  执行步骤
5.  生成草稿
6.  创建测试用例
7.  运行评估并优化

* * *

# 两种方法对比

方法一：直接创建

方法二：skill-creator

快速简单

步骤引导

适合简单技能

适合复杂技能

直接对话完成

规范流程

灵活修改

有测试验证

可能遗漏关键字段

需要额外安装

**选择建议**：

-   简单技能 → 方法一
-   复杂技能 → 方法二

* * *

# 如何写好需求

**好的需求描述**：

```
创建一个「git-commit」skill，功能是自动提交代码。

执行步骤：
1. 检查有哪些文件被修改
2. 生成符合 Conventional Commits 规范的提交信息
3. 执行 git commit
4. 询问是否需要 push

注意事项：
- 提交前先检查是否有敏感信息
- 不要提交 dist/node_modules/ 等目录
```

**不好的需求描述**：

```
帮我写一个提交代码的 skill
```

* * *

# Part 5

## 实战：创建三个常用 Skills

* * *

# 实战 1：代码审查 Skill

**需求分析**： 每次审查代码都要检查：代码风格、安全性、测试覆盖率

**创建步骤**：

```bash
mkdir -p ~/.claude/skills/review-pr
```

**核心内容**：

1.  代码风格检查
2.  安全性检查
3.  测试检查
4.  总体评价

**使用方式**：

```
/review-pr
请审查当前分支的 PR
```

* * *

# 实战 2：Git 自动提交 Skill

**需求分析**： 检查修改 → 写提交信息 → 确认没有敏感信息 → 提交

**创建步骤**：

```bash
mkdir -p ~/.claude/skills/git-commit
```

**核心内容**：

1.  检查修改（git status、git diff）
2.  生成提交信息（Conventional Commits 格式）
3.  安全检查（敏感信息、不该提交的目录）
4.  确认后执行（git add、git commit）

**使用方式**：

```
/git-commit
```

* * *

# 实战 3：测试生成 Skill

**需求分析**： 写完功能后总是忘记写测试，或者不知道该测什么

**创建步骤**：

```bash
mkdir -p ~/.claude/skills/gen-test
```

**核心内容**：

1.  分析代码（理解功能、识别输入输出、找出边界情况）
2.  生成测试（使用合适的测试框架）
3.  验证测试（确保测试可以运行）

**使用方式**：

```
/gen-test
为 src/utils.ts 生成单元测试
```

* * *

# 小林的实战总结

**效率提升**： 创建这三个 Skills 后，工作效率提升了至少 30%

**标准化**： 以前每次代码审查要花 10 分钟解释要求 现在一句「/review-pr」就搞定

**团队协作**： 这些 Skills 可以提交到项目的 `.claude/skills/` 目录 团队其他成员也能用上同样的标准

* * *

# Part 6

## 进阶技巧

* * *

# 技巧 1：Skills 与 Hooks 配合

**例如：代码保存后自动格式化**

```json
// .claude/hooks.json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": {
        "tool_name": "Edit"
      },
      "hook": {
        "type": "command",
        "command": "/format-code"
      }
    }]
  }
}
```

每次编辑文件后，Claude Code 会自动调用 format-code skill

* * *

# 技巧 2：团队协作

**共享项目 Skills**：

1.  将 Skills 放在 `.claude/skills/` 目录
2.  提交到 Git 仓库
3.  团队成员克隆项目后即可使用

**版本控制**：

-   Skills 可以像代码一样进行版本控制
-   每个 commit 都可以记录 Skills 的变更
-   可以回滚到旧版本

**示例项目结构**：

```
my-project/
├── .claude/
│   └── skills/
│       ├── review-pr/
│       ├── git-commit/
│       └── gen-test/
```

* * *

# 技巧 3：调试 Skill

**常见问题排查**：

问题

可能原因

解决方案

Skill 没有被触发

description 不够具体

改进 description，包含具体的使用场景

YAML 解析错误

frontmatter 格式错误

检查 YAML 语法，确保缩进正确

技能不生效

Claude Code 没有重启

重启 Claude Code

找不到技能

目录位置错误

确认在 `~/.claude/skills/` 或 `.claude/skills/`

**调试步骤**：

1.  使用 `npx skills list` 查看技能是否被识别
2.  直接输入技能名称手动触发（如 `/review-pr`）
3.  检查 SKILL.md 文件内容是否正确

* * *

# Part 7

## Skills 的内部机制

* * *

# 基于提示词的动态上下文注入

**核心事实**： Skills 不是可执行代码，而是高级指令（Prompt）

**工作流程**：

```
用户请求 → LLM 匹配 Skill 描述 → 触发 Skill
                                    ↓
                            注入完整指令内容
                                    ↓
                                执行任务
```

**本质**： 在需要时被「植入」到 Claude 的上下文中

* * *

# 三层渐进式加载架构

层级

内容

加载时机

Token 消耗

**Layer 1: 元数据**

YAML frontmatter

Claude 启动时

~30-50 tokens/skill

**Layer 2: 指令**

完整 SKILL.md 内容

Skill 被触发时

~5,000 tokens

**Layer 3: 资源**

脚本、模板、参考文档

按需通过文件系统访问

不占上下文

**优势**：

-   假设你有 100 个 Skills，启动时只消耗约 3,000-5,000 tokens
-   只有被触发的 Skill 才会加载完整内容
-   参考文档等资源文件永远不会被完整加载到上下文

* * *

# 纯 LLM 推理的路由机制

**核心设计**： Claude Skills 没有硬编码路由

传统方法

Claude Skills

❌ 嵌入向量匹配

✅ 纯 LLM 推理

❌ 分类器

✅ Transformer 前向传播

❌ 正则/关键词匹配

✅ 自然语言理解

❌ 单独的路由算法

✅ 统一的模型决策

**为什么这样设计？**

-   利用 Claude 本身的语言理解能力
-   自动处理多语言、同义词、模糊描述
-   无需额外维护
-   路由决策更智能

* * *

# Part 8

## 常用 Skills 资源

* * *

# 官方资源

**Anthropic 官方**：

-   [Anthropic 官方 Skills 仓库](https://github.com/anthropics/skills)
-   [Claude Code 官方文档 - Skills](https://docs.anthropic.com/en/docs/claude-code/configuration/skills)
-   [Agent Skills 标准](https://agentskills.io/)

**Vercel**：

-   [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) - 60K+ 订阅

**社区资源**：

-   [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
-   [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)
-   [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills) - 66 个专业技能

* * *

# Skills 市场

**skills.sh**：

-   Vercel 出品的 Agent Skills 应用商店
-   48000+ 技能库
-   网址：[skills.sh](https://skills.sh/)

**Skills 市场（中文界面）**：

-   发现和安装社区 Skills
-   网址：[skillsmp.com/zh](https://skillsmp.com/zh)

**搜索技巧**：

-   使用具体关键词：「react testing」优于「testing」
-   组合「领域 + 动作」：「nextjs deploy」「typescript lint」
-   优先选择高安装量的技能（10K+ 说明经过实战检验）

* * *

# 本周回顾

* * *

# 学习进度检查

✅ 理解 Skills 是什么（知识和流程的打包） ✅ 会安装和使用 Skills（find-skills 搜索、安装社区 Skills） ✅ 掌握 SKILL.md 结构（YAML frontmatter 和 Markdown 内容） ✅ 能创建自定义 Skills（两种方法创建 Skills） ✅ 跑通实战案例（代码审查、Git 提交、测试生成） ✅ 理解内部机制（三层加载架构、纯 LLM 路由）

* * *

# 自测题

**1\. Skills 和提示词的核心区别是什么？****2\. SKILL.md 的 description 字段为什么这么重要？****3\. Skills 和 MCP 的关系是什么？****4\. 三层渐进式加载架构是如何节省 Token 的？****5\. 如何调试一个不触发的 Skill？**

* * *

# 本周作业

**必做**：

-   创建至少 3 个自定义 Skills
-   将 Skills 提交到项目的 `.claude/skills/` 目录
-   记录创建过程和遇到的问题

**选做**：

-   尝试将 Skills 与 Hooks 配合使用
-   探索社区 Skills，安装并体验至少 5 个
-   分享你的 Skills 到课程讨论区

**截止时间**：下周上课前

* * *

# 下周预告

## MCP——连接外部世界

**从本地到云端****从文件到服务****从单机到全栈**

下周我们进入 MCP（Model Context Protocol） 给 Claude Code 接上 GitHub、数据库、浏览器等外部服务

* * *

# Q&A

## 有问题吗？

* * *

# 谢谢！

## 期待下周看到你的 Skills

**记住**：

> Skills 是知识沉淀 一次创建，反复使用 团队共享，持续优化
