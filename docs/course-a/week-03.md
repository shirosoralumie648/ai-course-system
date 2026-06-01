# Week 03：Claude Code 快速上手——从终端开始的 AI 协作

> 小林完成产品原型后，开始思考下一步：如何更高效地把想法变成代码？她听说过很多 AI 编程工具，但大多需要切换编辑器、学习新界面。直到她发现 Claude Code——一个直接在终端里工作的 AI 助手。不用离开命令行，不用改变工作流，只需要用自然语言说出需求，代码就写好了。

<ChapterIntroduction duration="约 2.5 小时" output="完成 Claude Code 安装配置，掌握核心操作技巧，能用自然语言驱动完整开发工作流" prerequisite="完成产品原型阶段，熟悉基本终端操作" :tags="['Claude Code', 'AI 编程', '终端工具', '自然语言编程', '开发效率']">

本章带你从零开始掌握 Claude Code 这个强大的 AI 编程助手。我们不只讲安装和命令，更重要的是教你如何用自然语言与 AI 协作，如何配置项目让 AI 更懂你的代码，如何把 Claude Code 融入日常开发工作流。学完这章，你将拥有一个 24 小时在线、永不疲倦的编程搭档。

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '① 认识 Claude Code', description: '理解它是什么、为什么要用' },
  { title: '② 安装与配置', description: '完成安装、初始化、环境配置' },
  { title: '③ 核心技巧', description: '掌握 10+ 实用操作技巧' },
  { title: '④ 实战演练', description: '三个完整的开发场景实操' }
]" />

---

## 小林的故事：从产品原型到工具精通

小林用 Bolt 做完产品原型后，心里有了底气——原来 AI 真能帮她把想法变成可运行的应用。但她也发现了问题：

**Bolt 的局限：**
- 只能在浏览器里用，不能操作本地项目
- 生成的代码要手动复制粘贴
- 无法接入 Git、数据库等开发工具
- 每次都要重新描述项目背景

她需要一个更专业的工具，能够：
- 直接在本地项目里工作
- 记住项目的技术栈和规范
- 与 Git、npm、测试工具无缝集成
- 支持长期的代码维护和迭代

这就是 **Claude Code** 的价值所在。

<InfoCard icon="💡" variant="tip">

小林的理解：如果说 Bolt 是「快速验证想法的原型工具」，那 Claude Code 就是「长期协作的开发伙伴」。Bolt 帮她证明了「这个想法能做」，Claude Code 帮她实现「把这个想法做好」。

</InfoCard>

---

## 什么是 Claude Code？

**Claude Code** 是 Anthropic 官方推出的 AI 原生编程工具，它将大型语言模型的能力直接集成到终端中。

### 核心特点

**1. 终端原生**
- 不需要切换到浏览器或 IDE
- 直接在命令行里与 AI 对话
- 无缝集成 Git、npm、测试等工具

**2. 项目记忆**
- 通过 `CLAUDE.md` 记住项目信息
- 理解你的技术栈和代码规范
- 不需要每次都重新解释背景

**3. 完整工作流**
- 从需求分析到代码实现
- 从测试调试到 Git 提交
- 从文档编写到代码审查

**4. 自然语言驱动**
- 用人话描述需求，AI 自动编写代码
- 支持多轮对话，逐步细化需求
- 能理解上下文，记住之前的讨论

### 与其他工具的对比

小林做了一张对比表，帮助自己理解 Claude Code 的定位：

| 工具 | 定位 | 适用场景 | 小林的评价 |
|------|------|----------|-----------|
| **Bolt** | 原型工具 | 快速验证想法 | 入门首选，但不适合长期维护 |
| **Claude Code** | 开发伙伴 | 本地项目开发 | 专业开发的核心工具 |
| **GitHub Copilot** | 代码补全 | 边写边提示 | 适合熟练开发者，新手容易迷失 |
| **Cursor** | AI IDE | 完整开发环境 | 功能强大但学习成本高 |

**小林的选择逻辑：**
1. 用 Bolt 快速做原型，验证想法
2. 用 Claude Code 在本地深度开发
3. 需要时配合 Copilot 提高编码速度

<InfoCard icon="🎯" variant="success">

**为什么小林选择 Claude Code？**

作为从产品经理转型的开发者，小林最看重两点：
1. **低门槛**：用自然语言就能工作，不需要记忆大量命令
2. **高天花板**：支持完整的专业开发工作流，能一直用下去

Claude Code 正好满足这两点——入门简单，但功能足够专业。

</InfoCard>

---

## 快速安装

### 环境准备

在安装 Claude Code 之前，确保你的系统满足以下要求：

**必需：**
- Node.js 18 或更高版本
- npm 或 yarn 包管理器
- 终端（Terminal / PowerShell / iTerm2）

**推荐：**
- Git（用于版本控制）
- 一个代码编辑器（VS Code / Sublime Text 等）

<InfoCard icon="⚠️" variant="warning">

**检查 Node.js 版本：**

```bash
node --version
```

如果版本低于 18，需要先升级 Node.js。推荐使用 [nvm](https://github.com/nvm-sh/nvm) 管理 Node.js 版本。

</InfoCard>

### 方法一：手动安装（推荐）

这是最直接的安装方式，适合想要掌控每个步骤的开发者。

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

如果看到版本号，说明安装成功！

**常见问题：**

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
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```

### 方法二：让 AI 帮你安装

如果你已经在使用其他 AI 工具（如 Cursor、Windsurf），可以直接让它们帮你安装：

```
帮我安装 Anthropic 的 Claude Code，
检查 Node.js 版本是否符合要求，
如果有问题请帮我解决。
```

AI 会自动：
1. 检查环境
2. 执行安装命令
3. 验证安装结果
4. 处理可能的错误

### 首次启动与登录

安装完成后，第一次启动 Claude Code：

```bash
# 进入任意目录（建议先创建一个测试项目）
mkdir ~/test-claude-code
cd ~/test-claude-code

# 启动 Claude Code
claude
```

**首次启动会引导你完成：**

1. **登录 Anthropic 账户**
   - 浏览器会自动打开登录页面
   - 使用 Google / GitHub / Email 登录
   - 授权 Claude Code 访问你的账户

2. **选择使用计划**
   - **免费计划**：适合学习和轻量使用
   - **Pro 计划**：更高配额，适合专业开发

3. **完成初始化**
   - Claude Code 会创建配置文件
   - 显示欢迎信息和快速入门提示

<AiChat :initial-messages="[
  { role: 'assistant', content: '欢迎使用 Claude Code！我是 Claude，你的 AI 编程助手。我可以帮你：编写和修改代码、解释复杂的技术概念、调试和优化程序、管理 Git 工作流、生成文档和测试。试试对我说：「你好，介绍一下你自己」' },
  { role: 'user', content: '你好，介绍一下你自己' },
  { role: 'assistant', content: '你好！我是 Claude，由 Anthropic 开发的 AI 助手。在 Claude Code 中，我可以：直接读写你的项目文件、执行终端命令、理解整个项目的上下文、记住我们的对话历史。我的工作方式是：你用自然语言告诉我需求，我会分析、规划、然后执行。如果有不确定的地方，我会先问清楚再动手。现在，你可以试着让我做点什么，比如：「创建一个 React 组件」「解释这段代码」「帮我写个测试」' }
]" :show-input="false" />

### 国内用户配置指南

由于网络原因，国内用户可能无法直接访问 Anthropic 服务。有两种解决方案：

**方案一：使用 API 代理服务**

购买兼容 Anthropic API 的第三方服务，然后配置环境变量：

```bash
# 在 ~/.bashrc 或 ~/.zshrc 中添加
export ANTHROPIC_API_KEY="your-api-key"
export ANTHROPIC_BASE_URL="https://api.your-provider.com/v1"

# 重新加载配置
source ~/.bashrc  # 或 source ~/.zshrc
```

**方案二：让 AI 帮你配置**

如果你已经购买了 API 服务，可以让其他 AI 工具帮你配置：

```
我购买了 XXX 服务商的 Anthropic API，
API 地址是 https://api.xxx.com，
密钥是 sk-xxx。

请帮我配置 Claude Code 的环境变量，
确保能正常使用。
```

<InfoCard icon="🔗" variant="info">

**更详细的配置指南：**

本课程在「Stage 2 - 后端开发 - Modern CLI」章节有完整的环境变量配置教程，包括：
- 如何选择 API 服务商
- 如何配置不同操作系统的环境变量
- 如何验证配置是否生效
- 常见问题排查

</InfoCard>

---

## 快速开始：三个小实验

安装完成后，不要急于在正式项目中使用。小林建议先做三个小实验，分别体验 Claude Code 的三种核心能力。

### 实验 1：对话——感受 AI 的理解能力

**目标：** 体验 Claude Code 的自然语言理解和多轮对话能力。

**操作步骤：**

```bash
# 启动 Claude Code
claude
```

**试试这些对话：**

<AiChat :initial-messages="[
  { role: 'user', content: '什么是闭包？太长不看版本' },
  { role: 'assistant', content: '闭包 = 函数 + 它能访问的外部变量。简单例子：inner 函数能「记住」count 变量，这就是闭包。' },
  { role: 'user', content: 'JavaScript 和 TypeScript 有什么区别？' },
  { role: 'assistant', content: '核心区别：TypeScript = JavaScript + 类型系统。TypeScript 在编写代码时就能发现类型错误，而不是等到运行时才发现。' }
]" :show-input="false" />

**观察要点：**
- Claude 的回答是否简洁准确？
- 它能否根据「太长不看」调整回答风格？
- 代码示例是否清晰易懂？

### 实验 2：生成文档——体验内容创作

**目标：** 体验 Claude Code 的内容生成能力。

**操作步骤：**

<AiChat :initial-messages="[
  { role: 'user', content: '帮我写一份 Git 常用命令的 Markdown 文档，要求：包含命令、说明、示例' },
  { role: 'assistant', content: '我来为你创建一份 Git 常用命令速查表。文档已创建！包含以下内容：初始化仓库、日常开发（add, commit, status）、分支管理（branch, checkout, merge）、远程协作（push, pull, fetch）、撤销操作（reset, revert）。每个命令都有说明和实际示例。' }
]" :show-input="false" />

**生成的文档示例：**

```markdown
# Git 常用命令速查表

## 初始化仓库

| 命令 | 说明 | 示例 |
|------|------|------|
| `git init` | 初始化新仓库 | `git init my-project` |
| `git clone` | 克隆远程仓库 | `git clone https://github.com/user/repo.git` |

## 日常开发

| 命令 | 说明 | 示例 |
|------|------|------|
| `git add` | 暂存文件 | `git add src/app.js` |
| `git commit` | 提交更改 | `git commit -m "feat: add login"` |
| `git status` | 查看状态 | `git status` |
```

**观察要点：**
- 文档结构是否清晰？
- 示例是否实用？
- 格式是否规范？

### 实验 3：编写游戏——完整的代码工作流

**目标：** 体验从需求到运行的完整开发流程。

**操作步骤：**

<AiChat :initial-messages="[
  { role: 'user', content: '用 Python 写一个猜数字游戏，要求：1. 随机生成 1-100 的数字 2. 用户输入猜测 3. 提示「太大」或「太小」4. 猜对后显示用了几次。写完后帮我运行它' },
  { role: 'assistant', content: '好的，我来创建这个猜数字游戏。游戏已启动！你可以开始猜数字了。' }
]" :show-input="false" />

**观察要点：**
- Claude 是否理解了所有需求？
- 代码是否可以直接运行？
- 如果有 bug，能否让 Claude 修复？

<InfoCard icon="💡" variant="tip">

**小林的实验心得：**

这三个实验让她明白了 Claude Code 的三个层次：
1. **理解层**：能听懂人话，给出准确回答
2. **创作层**：能生成结构化的内容
3. **执行层**：能写出可运行的代码

从对话到文档到代码，难度递增，但 Claude Code 都能胜任。这让她对后续的学习充满信心。

</InfoCard>

---

## 核心技巧：10 个必会操作

掌握这 10 个技巧，能让你的 Claude Code 使用效率提升数倍。

### 技巧 1：双击 Esc 回退对话

**快捷键：** 连续按两次 `Esc`

**作用：** 撤销上一轮对话，回到之前的状态。

**使用场景：**
- 不小心发了错误的指令
- 对 Claude 的回答不满意，想换个方式提问
- 对话进行太多轮，上下文混乱了

**按键说明：**

```
按 1 次 Esc  → 清除当前正在输入的内容
按 2 次 Esc  → 回退到上一次对话状态
按 3 次 Esc  → 清除所有对话历史
```

<InfoCard icon="⚠️" variant="warning">

**重要提醒：**

双击 Esc 只回退**对话状态**，不会撤销**文件修改**。

如果 Claude 已经修改了文件，需要用 Git 恢复：
```bash
git checkout -- filename.js
```

建议：在让 Claude 做大改动前，先提交当前工作。

</InfoCard>

### 技巧 2：@ 引用文件

**符号：** `@`

**作用：** 精准指定 Claude 要读取的文件或目录。

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

**Tab 补全：**

输入 `@` 后按 `Tab` 键，Claude 会显示当前目录的文件列表，可以用方向键选择。

<DiffViewer 
  title="使用 @ 引用 vs 不使用的区别"
  diff="@@ -1,1 +1,1 @@
-解释 src/utils.ts 这个文件
+@src/utils.ts 解释这个文件"
/>

**为什么要用 @？**

- **更精准**：Claude 知道你要的是哪个文件
- **省 Token**：避免 Claude 读取不相关的文件
- **更快速**：直接定位，不需要搜索

### 技巧 3：! 执行命令

**符号：** `!`

**作用：** 在 Claude Code 中直接执行终端命令。

**基本用法：**

```
!npm test           # 运行测试
!git status         # 查看 Git 状态
!ls -la             # 列出文件
```

**实际应用场景：**

<AiChat :initial-messages="[
  { role: 'user', content: '!npm test' },
  { role: 'assistant', content: '测试结果：✓ 15 passed ✗ 2 failed。失败的测试：auth.test.js: login with invalid password、user.test.js: update user profile' },
  { role: 'user', content: '分析一下测试失败的原因，并修复代码' },
  { role: 'assistant', content: '我来分析失败的测试...问题 1：auth.test.js 期望返回 401，但实际返回 500。问题 2：user.test.js 的 mock 数据格式不对。我来修复这两个问题...修复完成！再次运行测试：!npm test' }
]" :show-input="false" />

**安全提示：**

Claude Code 会询问是否执行敏感命令（如 `rm -rf`、`sudo` 等）。

### 技巧 4：/plan 先规划后编码

**命令：** `/plan`

**作用：** 对于复杂任务，先制定详细计划，再逐步执行。

**使用方式：**

<AiChat :initial-messages="[
  { role: 'user', content: '/plan 我想添加用户认证功能，请帮我制定实施计划' },
  { role: 'assistant', content: '📋 用户认证功能实施计划。阶段 1：数据库设计 - 创建 users 表（id, email, password_hash, created_at）、创建 sessions 表（id, user_id, token, expires_at）' }
]" :show-input="false" />

**阶段 2：后端 API**
- [ ] POST /api/auth/register - 用户注册
- [ ] POST /api/auth/login - 用户登录
- [ ] POST /api/auth/logout - 用户登出
- [ ] GET /api/auth/me - 获取当前用户

**阶段 3：前端集成**
- [ ] 创建登录页面
- [ ] 创建注册页面
- [ ] 添加路由守卫（未登录跳转到登录页）

**阶段 4：测试**
- [ ] 编写单元测试
- [ ] 编写集成测试

你想从哪个阶段开始？或者需要调整计划？
**最佳实践：**

- 超过 30 分钟的任务，先用 `/plan`
- 计划制定后，逐阶段执行
- 每完成一个阶段，检查一次

### 技巧 5：/init 自动生成配置

**命令：** `/init`

**作用：** 自动扫描项目，生成 `CLAUDE.md` 配置文件。

**使用方式：**

```
/init
```

**Claude 会做什么：**

1. 扫描项目结构
2. 识别技术栈（React / Vue / Next.js 等）
3. 分析配置文件（package.json、tsconfig.json）
4. 生成 CLAUDE.md

**生成的 CLAUDE.md 示例：**

```markdown
# My Project

## 技术栈
- 框架：Next.js 14 (App Router)
- 语言：TypeScript
- 样式：Tailwind CSS
- 状态管理：Zustand

## 常用命令
\`\`\`bash
npm run dev      # 启动开发服务器
npm run build    # 生产构建
npm run test     # 运行测试
\`\`\`

## 代码规范
- 使用函数组件 + Hooks
- 文件命名：PascalCase（组件）、camelCase（工具函数）
```

**为什么重要：**

`CLAUDE.md` 是 Claude Code 的「项目记忆」。每次启动时，Claude 会读取这个文件，了解项目背景。

<InfoCard icon="✨" variant="success">

**小林的使用心得：**

她每次开始新项目，第一件事就是运行 `/init`。这样 Claude 就知道：
- 这是个 React 项目，不是 Vue
- 用 TypeScript，不是 JavaScript
- 组件文件用 PascalCase 命名

不需要每次都解释，Claude 自己就知道。

</InfoCard>

### 技巧 6：/compact 压缩上下文

**命令：** `/compact`

**作用：** 压缩对话历史，节省 Token。

**使用时机：**

- 对话进行了 5-6 轮后
- 感觉 Claude 开始「遗忘」之前的内容
- 要切换到新任务，但想保留关键背景

**工作原理：**

`/compact` 会提取对话中的关键信息（决策、代码、需求），生成简洁摘要，后续对话基于摘要而非完整历史。

**使用示例：**

```
# 长对话后
/compact

# 继续工作
现在我们已经完成了用户模块，接下来做订单模块
```

### 技巧 7：/diff 查看改动

**命令：** `/diff`

**作用：** 打开交互式 diff 视图，查看当前未提交的改动。

**使用场景：**

- 提交代码前检查改动
- 让 Claude 生成 commit message
- 代码审查

**完整工作流：**

<AiChat :initial-messages="[
  { role: 'user', content: '/diff' },
  { role: 'assistant', content: '当前改动：src/components/LoginForm.tsx + 添加了表单验证 + 添加了错误提示。src/api/auth.ts + 新增 login 函数 + 新增 logout 函数。共修改 2 个文件，+45 行，-3 行' },
  { role: 'user', content: '请基于当前 diff 生成一个 Conventional Commit message' },
  { role: 'assistant', content: '根据改动内容，建议的 commit message：feat(auth): add login and logout functionality。你可以这样提交：git add -A，然后执行 git commit -m “feat(auth): add login and logout functionality”。' }
]" :show-input="false" />

### 技巧 8：Shift+Tab 自动接受

**快捷键：** `Shift+Tab`

**作用：** 开启/关闭自动接受模式。

**模式对比：**

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| 默认模式 | 每次修改都询问确认 | 学习阶段、重要代码 |
| 自动接受 | 直接应用修改 | 熟悉后、快速迭代 |

**注意事项：**

- 自动接受模式下，Claude 会直接修改文件
- 建议配合 Git 使用，出问题能回滚
- 敏感操作（删除文件等）仍会询问

### 技巧 9：Ctrl+C 取消操作

**快捷键：** `Ctrl+C`

**作用：** 取消当前正在执行的操作。

**使用场景：**

- Claude 正在运行耗时命令，想中断
- Claude 开始生成大量不相关代码
- 意识到给错了指令，立即停止

**按键说明：**

```
按 1 次 Ctrl+C  → 取消当前操作
按 2 次 Ctrl+C  → 完全退出 Claude Code
```

**与双击 Esc 的区别：**

- `Ctrl+C`：停止正在进行的**操作**
- `双击 Esc`：回退**对话状态**

### 技巧 10：/context 查看上下文

**命令：** `/context`

**作用：** 显示当前会话的上下文使用情况。

**输出示例：**

```
📊 上下文使用情况

Token 使用：45,230 / 200,000 (22.6%)
文件引用：12 个文件
对话轮数：8 轮

最消耗 Token 的文件：
1. src/api/users.ts (3,420 tokens)
2. node_modules/@types/react/index.d.ts (2,890 tokens)
3. src/components/Dashboard.tsx (1,560 tokens)

建议：
- 当前使用率健康，无需压缩
- 如需减少消耗，可在 .claudeignore 中添加 node_modules
```

**如何利用这个信息：**

1. **识别大文件**：某个文件消耗大量 Token，考虑是否真需要
2. **优化 .claudeignore**：将不相关文件加入忽略列表
3. **决定何时压缩**：使用率超过 70% 时，考虑 `/compact`

---

## 核心配置：让 Claude 更懂你的项目

合理的配置能让 Claude Code 更好地适应你的项目。

### CLAUDE.md - 项目记忆

`CLAUDE.md` 是 Claude Code 最重要的配置文件，相当于项目的「说明书」。

**最小可用模板：**

```markdown
# [项目名称]

## 技术栈
- 框架：React 18 + TypeScript
- 状态管理：Zustand
- 样式方案：Tailwind CSS
- 构建工具：Vite

## 常用命令

\`\`\`bash
npm run dev      # 启动开发服务器（端口 5173）
npm run test     # 运行单元测试
npm run build    # 生产构建
npm run lint     # 代码检查
\`\`\`

## 代码规范
- 组件使用函数组件 + Hooks
- 文件命名：PascalCase（组件）、camelCase（工具函数）
- Git 提交使用 Conventional Commits 规范
- 所有 API 调用必须经过统一的 request 封装
```

**快速生成：**

```
/init
```

Claude 会自动分析项目并生成配置文件。

### .claudeignore - 节省 Token

`.claudeignore` 告诉 Claude Code 哪些文件不应该被读取。

**推荐配置：**

```
# 依赖目录
node_modules/
.pnp/

# 构建产物
dist/
build/
.next/
out/

# 日志文件
*.log

# 测试覆盖率
coverage/

# 编辑器配置
.vscode/*
.idea/

# 环境变量
.env
.env.local

# 大型资源文件
*.png
*.jpg
*.jpeg
*.gif
*.svg
*.mp4
```

**配置技巧：**

1. 先忽略 node_modules 和构建产物
2. 使用 `/context` 查看哪些文件消耗最多 Token
3. 根据项目类型调整（图片项目忽略图片，文档项目保留 Markdown）

### 权限配置

通过 `.claude/settings.json` 控制 Claude 的操作权限。

**配置示例：**

```json
{
  "permissions": {
    "allow": [
      "Bash(git status)",
      "Bash(git log:*)",
      "Bash(git diff:*)",
      "Bash(npm test:*)",
      "Edit(src/**/*.{ts,tsx})",
      "Read(src/**/*.ts)"
    ],
    "ask": [
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(npm install:*)",
      "Edit(package.json)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)",
      "Edit(.git/*)"
    ]
  }
}
```

**权限级别：**

- **allow**：自动允许，不询问
- **ask**：执行前询问确认
- **deny**：完全禁止

---

## 实战演练：三个完整场景

理论学完了，现在通过三个真实场景，体验 Claude Code 的完整工作流。

### 场景 1：Bug 修复工作流

**背景：** 测试失败，需要定位并修复问题。

**完整流程：**

<AiChat :initial-messages="[
  { role: 'user', content: '!npm test' },
  { role: 'assistant', content: '测试失败：isEmail 函数无法正确处理包含 + 的邮箱地址。错误详情：Expected: true, Received: false, Input: user+tag@example.com' },
  { role: 'user', content: '@src/utils/validation.ts 问题出在这个文件吗？' },
  { role: 'assistant', content: '是的，问题在 validation.ts 的第 15 行。正则表达式中缺少 + 字符，导致无法匹配包含加号的邮箱。' },
  { role: 'user', content: '修复这个问题' },
  { role: 'assistant', content: '已修复 validation.ts，在邮箱正则表达式中添加了 + 字符。现在重新运行测试：!npm test。✓ 所有测试通过！修复完成。你可以提交这个改动了。' },
  { role: 'user', content: '/diff 请生成 commit message' },
  { role: 'assistant', content: '当前改动：src/utils/validation.ts + 在邮箱正则表达式中添加 + 字符支持。建议的 commit message：fix(validation): support plus sign in email addresses' }
]" :show-input="false" />

**小林的收获：**

这个流程展示了 Claude Code 的完整调试能力：
1. 运行测试发现问题
2. 定位问题文件和代码行
3. 理解问题原因
4. 修复代码
5. 验证修复
6. 生成规范的提交信息

### 场景 2：新功能开发工作流

**背景：** 需要添加一个用户资料编辑功能。

**完整流程：**

<AiChat>
<AiChatMessage role="user">
/plan
我要添加用户资料编辑功能
</AiChatMessage>
<AiChatMessage role="assistant">
📋 用户资料编辑功能实施计划

**阶段 1：创建 API**
- [ ] 添加 PUT /api/users/:id 接口
- [ ] 实现数据验证
- [ ] 添加权限检查（只能编辑自己的资料）

**阶段 2：前端表单**
- [ ] 创建 EditProfileForm 组件
- [ ] 添加表单验证
- [ ] 实现提交逻辑

**阶段 3：测试**
- [ ] API 单元测试
- [ ] 组件测试

从哪个阶段开始？
</AiChatMessage>
<AiChatMessage role="user">
从阶段 1 开始
</AiChatMessage>
<AiChatMessage role="assistant">
好的，开始实现 API。

[创建 src/api/users.ts]

```typescript
export async function updateUser(userId: string, data: UpdateUserData) {
  // 验证权限
  const currentUser = await getCurrentUser();
  if (currentUser.id !== userId) {
    throw new Error('Unauthorized');
  }
  
  // 验证数据
  const validated = validateUserData(data);
  
  // 更新数据库
  return await db.users.update({
    where: { id: userId },
    data: validated
  });
}
```

阶段 1 完成。继续阶段 2？
</AiChatMessage>
<AiChatMessage role="user">
继续
</AiChatMessage>
<AiChatMessage role="assistant">
创建前端表单组件...

[创建 src/components/EditProfileForm.tsx]

```tsx
export function EditProfileForm({ user }: Props) {
  const [formData, setFormData] = useState({
    name: user.name,
    email: user.email,
    bio: user.bio
  });
  
  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    await updateUser(user.id, formData);
    toast.success('资料更新成功');
  };
  
  return (
    <form onSubmit={handleSubmit}>
      {/* 表单字段 */}
    </form>
  );
}
```

阶段 2 完成。现在添加测试？
</AiChatMessage>
<AiChatMessage role="user">
是的，添加测试
</AiChatMessage>
<AiChatMessage role="assistant">
创建测试文件...

[创建 src/api/users.test.ts]
[创建 src/components/EditProfileForm.test.tsx]

测试已创建。运行测试：
!npm test
</AiChatMessage>
<AiChatMessage role="assistant">
✓ 所有测试通过！

功能开发完成。现在可以提交代码了。
</AiChatMessage>
</AiChat>

**小林的收获：**

`/plan` 命令让复杂任务变得有条理：
1. 先规划整体步骤
2. 逐阶段实现
3. 每个阶段都有明确的产出
4. 不会遗漏重要环节（如测试）

### 场景 3：代码审查工作流

**背景：** 完成开发后，需要审查代码质量。

**完整流程：**

<AiChat>
<AiChatMessage role="user">
/diff
</AiChatMessage>
<AiChatMessage role="assistant">
当前改动：

src/api/users.ts (+45 行)
src/components/EditProfileForm.tsx (+120 行)
src/api/users.test.ts (+35 行)
src/components/EditProfileForm.test.tsx (+50 行)

共 4 个文件，+250 行
</AiChatMessage>
<AiChatMessage role="user">
请审查这些改动，指出潜在问题和改进建议
</AiChatMessage>
<AiChatMessage role="assistant">
代码审查报告：

**✓ 做得好的地方：**
1. 添加了完整的测试覆盖
2. 实现了权限检查
3. 表单有数据验证

**⚠️ 需要改进的地方：**

1. **安全问题**：
   - users.ts 第 12 行：密码字段应该从返回数据中排除
   - 建议添加：`delete result.password`

2. **性能问题**：
   - EditProfileForm.tsx 第 25 行：每次输入都触发验证
   - 建议使用 debounce 优化

3. **用户体验**：
   - 表单提交时缺少 loading 状态
   - 建议添加 isSubmitting 状态

需要我帮你修复这些问题吗？
</AiChatMessage>
<AiChatMessage role="user">
是的，请修复
</AiChatMessage>
<AiChatMessage role="assistant">
已修复所有问题：

1. ✓ 从返回数据中排除密码字段
2. ✓ 添加 debounce 优化表单验证
3. ✓ 添加 loading 状态和禁用按钮

再次运行测试确保没有破坏现有功能：
!npm test
</AiChatMessage>
<AiChatMessage role="assistant">
✓ 所有测试通过！

代码已优化，可以提交了。
</AiChatMessage>
</AiChat>

**小林的收获：**

Claude Code 不只能写代码，还能审查代码：
1. 发现安全漏洞
2. 指出性能问题
3. 提升用户体验
4. 给出具体的改进建议

<InfoCard icon="🎯" variant="success">

**三个场景的共同点：**

小林发现，无论是修 bug、开发新功能还是代码审查，Claude Code 的工作流都很相似：
1. 用自然语言描述需求
2. Claude 分析并给出方案
3. 逐步执行，随时调整
4. 验证结果，确保质量

这种「对话式开发」让她感觉不是在「使用工具」，而是在「与伙伴协作」。

</InfoCard>

---

## 常见问题与解决方案

### Q1: Token 消耗太快怎么办？

**诊断：**

```
/context
```

查看哪些文件消耗了最多 Token。

**解决方案：**

1. **完善 .claudeignore**
   ```
   node_modules/
   dist/
   *.log
   coverage/
   ```

2. **定期压缩上下文**
   ```
   /compact
   ```

3. **精准引用文件**
   ```
   # 不推荐
   @src/ 解释这些代码
   
   # 推荐
   @src/utils/auth.ts 解释这个文件
   ```

### Q2: Claude 不理解我的项目怎么办？

**解决方案：**

1. **生成 CLAUDE.md**
   ```
   /init
   ```

2. **手动补充项目信息**
   ```markdown
   ## 项目特点
   - 使用自定义的 useAuth Hook 处理认证
   - API 调用统一通过 request.ts 封装
   - 组件库使用 Ant Design
   ```

3. **即时补充上下文**
   ```
   我们使用 Zustand 管理状态，
   store 定义在 src/store/ 目录下。
   请基于这个结构添加用户状态管理。
   ```

### Q3: 如何回退 Claude 的操作？

**回退对话：**
```
双击 Esc
```

**回退文件修改：**
```bash
# 查看改动
git diff

# 撤销特定文件
git checkout -- src/utils.ts

# 撤销所有改动
git checkout -- .
```

**预防措施：**
```bash
# 使用 Claude 前先提交
git add .
git commit -m "WIP: before claude session"

# 出问题后回退
git reset --hard HEAD~1
```

### Q4: 权限提示太多怎么办？

**编辑 `.claude/settings.json`：**

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

将常用的安全操作加入 `allow` 列表。

### Q5: 国内网络问题怎么解决？

**方案一：配置 API 代理**

```bash
export ANTHROPIC_API_KEY="your-key"
export ANTHROPIC_BASE_URL="https://api.your-provider.com/v1"
```

**方案二：让 AI 帮你配置**

```
我购买了 XXX 的 API 服务，
地址是 https://api.xxx.com，
密钥是 sk-xxx。
请帮我配置环境变量。
```

---

## 本周回顾

小林从「Claude Code 是什么」开始，一路学到了安装、配置、核心技巧和实战应用。现在检查一下你掌握得怎么样。

<ProgressTracker title="Week 03 学习进度" :items="[
  { title: '理解 Claude Code 的价值', description: '能说清它与 Bolt、Copilot、Cursor 的区别，知道为什么要用它', done: false },
  { title: '完成安装与配置', description: '成功安装 Claude Code，完成首次登录，能正常使用', done: false },
  { title: '掌握 10 个核心技巧', description: '会用 Esc、@、!、/plan、/init、/compact、/diff 等操作', done: false },
  { title: '理解配置文件', description: '知道 CLAUDE.md、.claudeignore、settings.json 的作用', done: false },
  { title: '完成三个实战场景', description: '跑通 Bug 修复、新功能开发、代码审查的完整流程', done: false },
  { title: '能独立解决常见问题', description: '知道如何优化 Token、回退操作、配置权限', done: false }
]" />

**自测问题：**

1. Claude Code 与 Bolt 的核心区别是什么？各自适合什么场景？
2. 双击 Esc 和 Ctrl+C 有什么区别？分别在什么情况下使用？
3. 为什么要用 `@` 引用文件，而不是直接描述文件路径？
4. `/plan` 命令适合什么样的任务？什么时候应该使用它？
5. `CLAUDE.md` 文件的作用是什么？为什么说它是「项目记忆」？

<InfoCard icon="🎓" variant="info">

**小林的学习总结：**

完成这一章后，小林最大的感受是：Claude Code 不是一个「工具」，而是一个「伙伴」。

她不再需要：
- 记忆复杂的命令
- 在编辑器和终端之间切换
- 手动查找文档和示例

她只需要：
- 用自然语言说出需求
- 与 Claude 对话细化方案
- 验证结果并迭代优化

从产品原型到专业开发，Claude Code 成为了她最重要的协作伙伴。

</InfoCard>

---

## 下周预告

掌握了 Claude Code 的基础操作后，小林终于可以更稳定地做东西了。但她很快发现：工具会用了，真正困难的问题变成了**到底做什么**。

下一章，我们将学习 **找到一个好创意**——如何从真实人群、真实场景和真实痛点里找到值得做的产品方向。

**下周内容预告：**
- 真需求和假需求的区别
- 痛点、爽点、痒点
- 横向切分人群
- 纵向深挖用户场景

我们下周见！


**作用：** 撤销上一轮对话，回到之前的状态。

**使用场景：**
