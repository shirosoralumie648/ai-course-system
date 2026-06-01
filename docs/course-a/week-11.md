# Week 11：MCP——给 Claude Code 接上外部世界

> 小林做完前几章的练习后，一直以为 Claude Code 就是个「会写代码的终端」。直到有天她想让它顺手看一眼 GitHub 上的 Issue，结果发现它真能做到——前提是先接上一个叫 MCP 的东西。那一刻她意识到，Claude Code 远不只能读写本地文件，它可以连上整个外部世界。

🎯学习目标

MCPClaude Code工具集成配置管理自然语言运维

本章带你搞懂 MCP（Model Context Protocol）到底是什么、为什么它能让 Claude Code 脱胎换骨，以及怎么一步步把 GitHub、SQLite、文件系统、浏览器这些外部能力接进来。我们不只讲概念，而是把每一段配置、每一条命令、每一种传输方式都过一遍。学完这章，你的 Claude Code 就不再是孤岛，而是一个能访问真实数据和服务的超级助手。

⏱️

预计时长

约 2 小时

📦

核心产出

一份可提交到 Git 的 .claude/mcp.json 配置，以及用自然语言驱动 GitHub / 数据库 / 浏览器的实操流程

📋

前置条件

学完前几章 Claude Code 基础

0

① 认识 MCP

理解协议本质与价值

0

② 配置接入

配置文件、传输方式、自然语言管理

0

③ 实战与运维

实战示例、调试、最佳实践

* * *

## 什么是 Claude Code MCP？

小林的第一个问题很朴素：这个 MCP 到底是啥？

**Claude Code** 是 Anthropic 官方推出的 AI 命令行工具，而 **MCP（Model Context Protocol）** 则是让 Claude Code 能够连接外部工具和服务的协议。

简单来说，MCP 让 Claude Code 从一个「只能读写本地文件」的 AI 助手，变成一个「能访问 GitHub、数据库、API、云服务」的超级助手！

小林的理解方式：如果 Claude Code 是一台主机，那 MCP 就是 USB 接口——本身不做事，但你插上什么外设，它就多出什么能力。插上 GitHub，它会管 Issue；插上数据库，它会查数据；插上浏览器，它会截图。

## 为什么需要在 Claude Code 中使用 MCP？

要理解 MCP 的价值，最直观的办法就是对比「有」和「没有」两种状态。小林把这两份清单贴在了笔记本第一页。

### 没有 MCP 的 Claude Code

```
你能做的：
✓ 读取本地文件
✓ 编辑代码
✓ 运行命令
✓ 使用 Bash 工具

你不能做的：
✗ 查看你的 GitHub Issues
✗ 访问云数据库
✗ 调用外部 API
✗ 获取实时天气
```

### 有了 MCP 的 Claude Code

```
你能做的：
✓ 所有原来的功能
✓ 查看/创建 GitHub Issues 和 PR
✓ 查询 SQLite、PostgreSQL 数据库
✓ 访问 Notion、Slack 等外部服务
✓ 获取实时天气、地图数据
✓ 浏览器自动化
✓ ...以及更多！
```

对小林这种从产品原型起步的人来说，这个差别太关键了：她做产品时本来就要在 GitHub、数据库、Notion 之间来回切，现在这些都能在一个终端里用一句话搞定。

## 快速开始

小林决定边学边动手。她把上手流程拆成了四步。

### 步骤 1：了解配置文件位置

Claude Code 的 MCP 配置文件位于：

级别

配置文件路径

作用范围

**用户级**

`~/.claude.json`

所有项目

**项目级**

`.claude/mcp.json`

当前项目

推荐优先使用**项目级配置**，让不同项目使用不同的 MCP 服务。

### 步骤 2：用自然语言添加 MCP 服务器

在 Claude Code 中，你不需要手动编辑配置文件或记忆命令，直接用自然语言描述即可：

```
你：帮我添加 GitHub MCP 服务器，我的 token 是 ghp_xxx

Claude：我来帮你配置 GitHub MCP 服务器...

[自动更新 .claude/mcp.json]
```

```
你：添加一个 SQLite 数据库服务器，数据库文件在 ./data/app.db

Claude：好的，我来配置 SQLite MCP 服务器...
```

```
你：添加一个 HTTP 类型的 MCP 服务器，地址是 https://api.example.com/mcp

Claude：我来添加这个远程 MCP 服务器...
```

这正是小林作为非技术出身的人最喜欢的一点：她不用背 JSON 字段名，只要把需求说清楚，Claude Code 会替她把配置写对。但她也提醒自己——配置写完后还是要打开文件看一眼，知道它到底改了什么，这样出问题时心里有数。

### 步骤 3：验证配置

直接询问 Claude Code：

```
你：现在有哪些可用的 MCP 服务器？

Claude：当前已配置的 MCP 服务器：
• github - GitHub 集成
• sqlite - SQLite 数据库
• filesystem - 文件系统访问
```

或使用诊断命令：

```
/doctor
```

### 步骤 4：开始使用

配置成功后，直接用自然语言调用 MCP 功能：

```
你：帮我在 GitHub 上创建一个 Issue

Claude：我可以帮你创建 GitHub Issue。请告诉我：
- 仓库地址（如 owner/repo）
- Issue 标题
- Issue 描述
```

## Claude Code 的自然语言管理

小林发现，MCP 在 Claude Code 里几乎不需要「记命令」，从添加到删除、从诊断到更新 token，全都能用大白话完成。

### 查看和管理 MCP 服务器

你可以完全用自然语言与 Claude Code 交互：

```
你：列出所有已配置的 MCP 服务器

你：检查一下 MCP 服务器的连接状态

你：删除 notion 这个 MCP 服务器

你：更新 github 服务器的 token
```

### 诊断问题

当遇到问题时：

```
你：检查一下 MCP 连接有什么问题

Claude：[会自动运行诊断，分析配置文件，检查服务器状态]
```

## 配置方式详解

光会用自然语言还不够。小林想知道底层那份配置长什么样，这样团队协作时她才能读懂别人写的配置。

### 用户级配置（全局）

编辑 `~/.claude.json`：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yourname/Documents"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

### 项目级配置（推荐）

编辑项目根目录的 `.claude/mcp.json`：

```json
{
  "mcpServers": {
    "project-db": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "./data/app.db"]
    }
  }
}
```

**项目级配置优势：**

-   团队成员可以共享配置（提交到 Git）
-   不同项目使用不同的 MCP 服务
-   配置更灵活，不会污染全局设置

### 传输方式配置

Claude Code 支持三种传输方式：

#### STDIO（本地进程）

```json
{
  "mcpServers": {
    "local-tool": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    }
  }
}
```

#### HTTP（远程服务）

```json
{
  "mcpServers": {
    "remote-api": {
      "url": "https://api.example.com/mcp",
      "transport": "http",
      "headers": {
        "Authorization": "Bearer your-token"
      }
    }
  }
}
```

#### SSE（服务器推送）

```json
{
  "mcpServers": {
    "streaming": {
      "url": "https://api.example.com/sse",
      "transport": "sse"
    }
  }
}
```

小林的笔记

STDIO 适合本地工具（在你电脑上起一个进程），HTTP 和 SSE 适合远程服务（连别人的服务器）。绝大多数官方服务器都是 STDIO 方式，用 `npx` 临时拉起来就行，不用预装。

## 实战示例

配置打通后，小林挑了几个自己日常真会用到的场景试了一遍。

### 示例 1：GitHub 工作流自动化

```
你：帮我把当前的修改推送到 GitHub，然后创建一个 PR，标题是"添加新功能"

Claude：
1. 检查当前 git 状态...
2. 创建新分支 feature/new-feature...
3. 提交更改...
4. 推送到远程...
5. 调用 github_create_pull_request 创建 PR...
6. PR 已创建：https://github.com/owner/repo/pull/123
```

### 示例 2：数据库查询

```
你：查询数据库中最近注册的 10 个用户

Claude：
1. 连接到 SQLite 数据库...
2. 执行查询：SELECT * FROM users ORDER BY created_at DESC LIMIT 10
3. 返回结果：
   - 张三 (zhang@example.com) - 2025-02-28
   - 李四 (li@example.com) - 2025-02-27
   ...
```

### 示例 3：网页截图分析

```
你：打开 https://example.com 并截图，分析一下页面设计

Claude：
1. 启动浏览器...
2. 导航到 https://example.com...
3. 截取屏幕...
4. [返回截图]
5. 页面设计分析：
   - 布局采用居中设计，最大宽度 1200px
   - 主色调为蓝色 (#3b82f6)
   - 导航栏固定在顶部
   ...
```

### 示例 4：与 Notion 集成

```
你：把我刚才的笔记保存到 Notion

Claude：
1. 使用 Notion MCP 服务器...
2. 创建新页面...
3. 已保存：https://notion.so/page/xxx
```

小林的体会：MCP 真正的威力在于「组合」。示例 1 里它一口气做完了 git 提交 + 推送 + 建 PR 三件事——这本来要她切到终端敲好几条命令。现在一句话，Claude Code 自己编排好步骤。

## 调试技巧

接外部服务难免出岔子。小林第一次配 SQLite 就因为路径写错连不上，于是她总结了一套排查方法。

### 使用自然语言诊断

遇到问题时，直接告诉 Claude Code：

```
你：我的 MCP 服务器连接不上了，帮我检查一下

你：GitHub MCP 工具调用失败，是什么原因？

你：为什么 sqlite 服务器一直显示连接中？
```

Claude Code 会自动：

1.  检查配置文件格式
2.  验证环境变量
3.  测试服务器连接
4.  提供具体的修复建议

### 常见问题排查

问题

可能原因

解决方案

服务器未连接

配置文件格式错误

检查 JSON 语法

工具无法调用

权限不足

检查环境变量

连接超时

网络问题

检查 URL 或网络

进程崩溃

服务器代码错误

查看服务器日志

### 手动诊断命令

```
/doctor
```

输出示例：

```
系统诊断报告：
===============

Claude Code: v2.5.0 ✓
Node.js: v20.0.0 ✓

MCP 服务器状态：
• github: ✓ 已连接 (12 tools)
• sqlite: ✗ 连接失败 - Database file not found
• puppeteer: ✓ 已连接 (8 tools)

建议：
1. 检查 sqlite 数据库路径是否正确
2. 确保 .claude/mcp.json 格式正确
```

小林踩过的坑

她那次的报错正是 `Database file not found`。原因是她写的是相对路径 `./data/app.db`，但运行 Claude Code 时的工作目录并不在项目根目录。排查时先看 `/doctor` 输出最快——它会直接告诉你哪个服务器挂了、为什么挂。

## 最佳实践

跑通之后，小林又回头整理了几条「让配置不出乱子」的规矩。这部分她觉得比怎么连还重要，因为团队协作里配置一乱就全乱。

### 1\. 项目级配置优先

**为什么推荐项目级配置？**

不同的项目往往需要不同的 MCP 服务。例如，前端项目可能需要浏览器测试工具，而后端项目则需要数据库连接。使用项目级配置可以让每个项目拥有自己专属的 MCP 服务器集合，避免全局配置的混乱。

更重要的是，项目级配置可以提交到 Git 仓库，团队成员克隆项目后就能直接使用相同的 MCP 服务，无需重复配置。

```
项目 A（前端项目）→ .claude/mcp.json 包含浏览器测试 MCP
项目 B（后端项目）→ .claude/mcp.json 包含数据库 MCP
```

### 2\. 敏感信息环境变量化

**永远不要在配置文件中硬编码密钥！**

配置文件可能会被意外提交到 Git 仓库，导致密钥泄露。正确的做法是将敏感信息存储在环境变量中，配置文件只引用变量名。这样即使配置文件被公开，也不会暴露实际的密钥。

```json
{
  "env": {
    "GITHUB_TOKEN": "$GITHUB_TOKEN",  // ✓ 好 - 从环境变量读取
    "GITHUB_TOKEN": "ghp_abc123"       // ✗ 不好 - 硬编码密钥
  }
}
```

这条小林记得最牢。她见过有人把带 token 的 `.claude/mcp.json` 直接提交上 GitHub，几分钟后 token 就被滥用了。永远用 `$环境变量` 引用，把真实密钥放在你本机的环境变量里，绝不写进会进 Git 的文件。

### 3\. 版本锁定

**为什么需要锁定版本？**

默认情况下，`npx -y` 会总是使用最新版本的 MCP 服务器。这可能导致问题：新版本可能引入不兼容的更改，或者某个服务器突然被下架/改名。

通过在包名后添加 `@版本号`，可以确保始终使用经过验证的特定版本，避免因自动更新导致的意外问题。

```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github@1.2.3"]  // 固定版本
}
```

### 4\. 文档化你的 MCP 配置

**让团队成员快速理解 MCP 配置**

当项目中有多个 MCP 服务器时，新成员可能不清楚每个服务器的用途和配置要求。在 `.claude/` 目录下创建一个 `README.md` 文件，说明每个服务器的用途、所需的配置项以及获取方式，可以大大降低团队的沟通成本。

在项目中创建 `.claude/README.md`：

在项目中创建 `.claude/README.md`：

```markdown
# MCP 配置说明

本项目使用的 MCP 服务器：

## github
用于自动化 GitHub 操作，需要配置 GITHUB_TOKEN。

## sqlite
连接到 ./data/app.db，用于查询和修改数据。

## puppeteer
用于 E2E 测试。
```

## Claude Code vs Claude Desktop

小林还用过 Claude Desktop，于是好奇两者在 MCP 上有啥区别。她整理成了一张对照表。

特性

Claude Code

Claude Desktop

**配置文件**

`~/.claude.json` 或 `.claude/mcp.json`

`claude_desktop_config.json`

**项目级配置**

✓ 支持

✗ 不支持

**自然语言管理**

✓ 支持

✗ 需手动编辑

**诊断工具**

✓ `/doctor`

✗ 无

**热重载**

✓ 自动重载

✗ 需重启应用

**适用场景**

开发工作流、CI/CD

日常使用、办公

结论很清楚：做开发、走工作流，Claude Code 在 MCP 上的体验全方位更顺手——尤其是项目级配置 + 自然语言管理 + 热重载这三点。

## 常用 MCP 服务器

> 💡 完整的 MCP 服务器列表可在本课程附录的「MCP 服务器大全」中查阅（站内附录章节，本页不外链）。

小林把自己最常用的几个服务器配置整理在一起，方便随时复制。

### GitHub 服务器

**功能：** Issues、PR、仓库管理

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

**获取 Token：** [https://github.com/settings/tokens](https://github.com/settings/tokens)

### SQLite 服务器

**功能：** 查询和管理 SQLite 数据库

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "./data/database.db"]
    }
  }
}
```

### 文件系统服务器

**功能：** 访问指定目录的文件

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yourname/Documents"]
    }
  }
}
```

### Puppeteer 浏览器自动化

**功能：** 浏览器控制、截图、自动化测试

```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

### Brave 搜索服务器

**功能：** 网络搜索

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-brave-api-key"
      }
    }
  }
}
```

## 参考资源

小林把学习路上收藏的链接都留在这里，方便日后深挖。

### 官方文档

-   [Claude Code 官方文档 - MCP](https://docs.anthropic.com/zh-CN/docs/claude-code/mcp)
-   [MCP 官方网站](https://modelcontextprotocol.io/)
-   [MCP 规范文档](https://modelcontextprotocol.io/specification/)
-   [MCP GitHub 仓库](https://github.com/modelcontextprotocol)

### 官方服务器

-   [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) - GitHub 集成
-   [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) - SQLite 数据库
-   [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - PostgreSQL 数据库
-   [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - 文件系统访问
-   [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) - 浏览器自动化
-   [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) - 网页抓取
-   [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Brave 搜索
-   [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) - Git 操作

### 教程文章

-   [一文讲透 MCP 的原理及实践](https://view.inews.qq.com/a/20250414A023WV00)
-   [MCP（Model Context Protocol）架构与工作原理](https://m.toutiao.com/w/1826385835060307/)
-   [2025 大模型最新教程：MCP 协议从入门到精通](https://m.blog.csdn.net/weixin_45653328/article/details/150916706)
-   [从零开始学 MCP（八）- 构建一个 MCP server](https://juejin.cn/post/7582510291667419187)

### 配置指南

-   [Claude Code 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices)
-   [Claude Code 完全配置指南](https://juejin.cn/post/7576838552472043563)

### 开发教程

-   [零基础构建 MCP 服务器 TypeScript/Python 双语言实战指南](https://m.blog.csdn.net/ztt123654/article/details/150844207)
-   [终极 MCP 服务器构建指南：TypeScript 与 Python 双版本完整教程](https://m.blog.csdn.net/gitblog_00703/article/details/154862128)
-   [使用 TypeScript 构建一个最简单的 MCP 服务器](https://m.blog.csdn.net/weixin_45653525/article/details/148433757)
-   [使用 Azure 容器应用生成 TypeScript MCP 服务器](https://learn.microsoft.com/zh-cn/azure/developer/ai/build-mcp-server-ts)

### MCP 服务器资源

-   [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - 最全面的 MCP 服务器列表
-   [Official MCP Registry](https://registry.modelcontextprotocol.io) - Anthropic 官方「应用商店」
-   [MCP.so](https://mcp.so) - 社区 MCP 服务器中心
-   [Glama.ai MCP](https://glama.ai/mcp/servers) - 带评分评论的 MCP 目录
-   [Smithery](https://smithery.ai) - MCP 服务器市场
-   [MCPHub](https://mcphub.io/registry) - 界面简洁的目录
-   [LobeHub MCP](https://lobehub.com/zh/mcp) - 中文 MCP 目录

### 地图和天气服务

-   [高德地图 MCP Server](https://lobehub.com/zh/mcp/luozengchang-mcp-amap)
-   [腾讯位置服务 MCP 文档](https://lbs.qq.com/service/MCPServer/MCPServerGuide/overview)
-   [彩云天气 MCP Server](https://github.com/caiyunapp/mcp-caiyun-weather)
-   [OpenWeatherMap MCP Server](https://github.com/CodeByWaqas/weather-mcp-server)

### 社区资源

-   [Everything Claude Code Config](https://github.com/affaan-m/everything-claude-code) - 生产级 Claude Code 配置集合
-   [AI Coding Guide](https://github.com/hacket/AICodingGuide) - Claude Code 中文学习路径

### 实际应用案例

-   [BlenderMCP - AI 驱动的 3D 建模](https://github.com/Belthur/blender-mcp) - 4,100+ ⭐
-   [MCP 生产环境 15 条最佳实践](https://learn.microsoft.com/zh-cn/azure/azure-functions/scenario-mcp-apps)

* * *

## 本周回顾

小林这一章从「Claude Code 不就是写代码的吗」走到了「它能连 GitHub、数据库、浏览器」。下面对照检查你掌握得怎么样。

Week 11 学习进度

1

理解 MCP 是什么

能说清 MCP 是让 Claude Code 连接外部工具的协议，以及它带来的能力跃迁

2

掌握配置文件

分得清用户级 ~/.claude.json 与项目级 .claude/mcp.json，知道为何优先项目级

3

会用三种传输方式

能根据本地/远程场景选择 STDIO、HTTP、SSE

4

能用自然语言管理

会用大白话添加、查看、删除、诊断 MCP 服务器

5

跑通实战与调试

能配 GitHub/SQLite/Puppeteer，并用 /doctor 排查连接问题

6

记住安全最佳实践

密钥环境变量化、版本锁定、项目级配置、文档化

**自测问题：**

1.  用户级配置（`~/.claude.json`）和项目级配置（`.claude/mcp.json`）各自的作用范围是什么？为什么团队协作时推荐项目级？
2.  STDIO、HTTP、SSE 三种传输方式分别适合什么场景？远程 MCP 服务一般用哪种？
3.  为什么绝不能在配置文件里硬编码密钥？正确写法长什么样？当 `/doctor` 报告某个服务器连接失败时，你的排查顺序是怎样的？

## 下周预告

接上外部世界之后，小林开始想：能不能让 AI 写代码这件事本身也变得更可控、更有章法？下一章我们进入 spec-coding——规格驱动开发，先把需求和设计写成规格，再让 Claude Code 照着规格落地，让 AI 编程从「碰运气」变成「按图施工」。
