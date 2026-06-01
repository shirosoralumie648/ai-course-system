# Week 15：Claude Agent SDK

## 让 AI 自主完成任务

**课程 A：产品原型 + Claude Code 高级技能**

* * *

# 小林的困惑

> 用了几个月 Claude Code 一直觉得它就是个「超级终端助手」 你说一句，它做一件事

**直到有一天...** 她想把「每次 PR 提交后自动跑代码审查」这个流程自动化 才发现背后有个叫 Agent SDK 的东西

* * *

# 本周目标

-   ⏱️ **学习时长**：约 3 小时
-   🎯 **产出物**：一个能自主修复 bug 的 Agent + 完整的 CI/CD 质量守护流水线
-   📚 **前置要求**：熟悉 Python 或 TypeScript 基础，学完前几章 Claude Code 使用
-   🏷️ **关键词**：Agent SDK、AI 自动化、工具编排、CI/CD

* * *

# 学习路线

```
① 认识 Agent SDK → ② 核心能力 → ③ 实战场景
```

**今天的核心**：

-   理解 Agent SDK 是什么、为什么需要它
-   掌握工具系统、执行模式、配置选项
-   从修 bug 到 CI/CD 流水线的完整实战

* * *

# Part 1

## 什么是 Claude Agent SDK？

* * *

# 一句话对比

工具

使用方式

适合场景

**Claude Code CLI**

终端交互，人工输入指令

日常开发、快速任务

**Claude Agent SDK**

代码调用，程序化执行

CI/CD、自动化、批量任务

**基础 anthropic SDK**

API 调用，你自己处理工具循环

聊天、生成、简单 tool use

* * *

# 代码量对比：修复 bug

**基础 SDK**：你得自己写循环处理工具调用

```python
# 你得自己定义工具、执行工具、喂回结果
response = client.messages.create(...)
while response.stop_reason == "tool_use":
    result = your_tool_executor(response.tool_use)
    response = client.messages.create(tool_result=result, ...)
```

**Agent SDK**：一行搞定

```python
async for message in query(
    prompt="修复 auth.py 的 bug",
    options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash"]),
):
    print(message)
```

* * *

# 为什么需要 Agent SDK？

**核心转变**：

> CLI 是「你和 AI 对话」 SDK 是「你的程序调用 AI」

**适合场景**：

-   每次 PR 提交后自动触发代码审查
-   定时让 AI 巡检系统日志找异常
-   批量处理多个项目的代码质量检查

* * *

# 三种工具的使用场景

你想做的事

该用什么

简单对话、文本生成、翻译

基础 `anthropic` SDK

日常写代码、改 bug、快速任务

Claude Code CLI

自主完成多步骤开发任务

**Agent SDK**

嵌入 CI/CD 流水线

**Agent SDK**

构建能操作文件系统的应用

**Agent SDK**

* * *

# Part 2

## 核心能力

* * *

# 安装和配置

**安装**：

```bash
# Python (需要 3.10+)
pip install claude-agent-sdk

# TypeScript (需要 Node.js 18+)
npm install @anthropic-ai/claude-agent-sdk
```

**认证**：

```bash
export ANTHROPIC_API_KEY=your-api-key
```

* * *

# 第一个 Agent：Hello World

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="这个目录下有哪些文件？",
        options=ClaudeAgentOptions(allowed_tools=["Bash", "Glob"]),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

**震撼时刻**：你没写任何「执行 ls 命令」的代码，Claude 自己决定用什么工具、怎么执行

* * *

# Agent Loop：工作原理

```
你：修复 auth.py 的 bug
  ↓
Claude 思考：需要先看代码
  ↓
调用 Read 工具读取 auth.py
  ↓
Claude 分析：发现空指针问题
  ↓
调用 Edit 工具修改代码
  ↓
调用 Bash 工具运行测试
  ↓
测试通过，任务完成
```

* * *

# 两种使用模式

模式

适合场景

是否保持上下文

**`query()` 函数**

单次任务，执行完就结束

✗ 无状态

**`resume` 参数**

多轮对话，需要记住之前的内容

✓ 有状态

**判断标准**：

-   绝大多数自动化场景用无状态的 `query()` 就够了
-   只有当任务真的需要「记住之前说了什么」时，才用 `resume` 参数

* * *

# 内置工具：开箱即用

工具

功能

典型用途

**Read**

读取文件

看代码、读配置

**Write**

创建文件

生成新文件

**Edit**

精确编辑文件

改 bug、重构

**Bash**

执行终端命令

跑测试、装依赖、git 操作

**Glob**

按模式找文件

`**/*.py`、`src/**/*.ts`

**Grep**

正则搜索文件内容

找函数定义、找 TODO

**WebSearch**

搜索网页

查文档、找方案

**WebFetch**

抓取网页内容

读在线文档

* * *

# 权限模式：控制 Agent 的行为边界

权限模式

行为

适合场景

**`bypassPermissions`**

所有操作都不需要确认

只读任务、可信环境

**`acceptEdits`**

文件修改自动通过，危险操作需确认

代码审查、自动修复

**`requirePermissions`**

所有操作都需要人工确认

生产环境、高风险操作

**安全原则**：第一次跑新 Agent 时，永远先用 `requirePermissions` 模式

* * *

# Part 3

## 实战场景

* * *

# 实战场景一：自动修 Bug Agent

**需求**： 用户反馈登录时偶尔报 500 错误，需要排查 `src/auth/` 目录下的代码并修复

**步骤**：

1.  用 Grep 搜索错误日志和异常处理
2.  读取相关代码文件
3.  定位问题根因
4.  修改代码
5.  运行测试确认修复

* * *

# 自动修 Bug Agent：代码实现

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def auto_fix_bug():
    """自动修复 bug 的 Agent"""
    async for message in query(
        prompt="""
用户反馈登录时偶尔报 500 错误，请排查 src/auth/ 目录下的代码并修复。

步骤：
1. 先用 Grep 搜索错误日志和异常处理
2. 读取相关代码文件
3. 定位问题根因
4. 修改代码
5. 运行测试确认修复
        """,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Bash", "Glob", "Grep"],
            permission_mode="acceptEdits",
            max_turns=20,
        ),
    ):
        if hasattr(message, "type"):
            print(f"[{message.type}] {message}")

asyncio.run(auto_fix_bug())
```

* * *

# 运行效果

**Agent 自己编排步骤**：

1.  搜索错误日志 → 找到 auth.py 第 45 行
2.  读取代码 → 发现数据库连接失败时没有正确处理异常
3.  修改代码 → 添加异常处理，返回 503 状态码
4.  运行测试 → 所有测试通过

**核心价值**： 你只描述了任务，Agent 自己决定了执行顺序

* * *

# 实战场景二：代码审查 Agent

**需求**： 每次 PR 提交后，自动审查代码质量，但不做任何修改——只输出报告

**关键设计**：

-   **只读权限**：`allowed_tools=["Read", "Glob", "Grep"]`
-   **跳过确认**：`permission_mode="bypassPermissions"`（只读操作无风险）
-   **结构化输出**：要求输出 JSON 格式，方便后续处理

* * *

# 代码审查 Agent：代码实现

```python
async def code_review():
    """只读代码审查 Agent"""
    result_text = ""
    async for message in query(
        prompt="""
审查 src/ 目录下的代码，从这几个维度分析：
1. 代码规范：命名、格式、注释
2. 逻辑问题：边界条件、空指针、竞态
3. 性能隐患：N+1 查询、内存泄漏、不必要的循环
4. 可维护性：函数过长、职责不清、魔法数字

输出 JSON 格式：
{
  "issues": [
    {"severity": "high/medium/low", "file": "...", "line": ..., "description": "..."}
  ],
  "summary": "..."
}
        """,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep"],
            permission_mode="bypassPermissions",
            max_turns=15,
        ),
    ):
        if hasattr(message, "result"):
            result_text = message.result
    print(result_text)
```

* * *

# 实战场景三：企业级 CI/CD 流水线

**需求**： 每次 PR 提交后，自动触发： **代码审查 → 安全扫描 → 自动修复 → 测试验证 → 生成报告**

**核心思想**： 每个 Agent 只做一件事，权限最小化，结果串联传递

* * *

# CI/CD 流水线架构

```
PR 提交
  │
  ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  代码审查     │───▶│  安全扫描     │───▶│  自动修复     │
│  Agent       │    │  Agent       │    │  Agent       │
│ (只读)       │    │ (只读)       │    │ (可写)       │
└─────────────┘    └─────────────┘    └─────────────┘
                                            │
                                            ▼
                                     ┌─────────────┐
                                     │  测试验证     │
                                     │  Agent       │
                                     │ (Bash)       │
                                     └──────┬──────┘
                                            │
                                            ▼
                                     生成报告 + 通知
```

* * *

# 企业级设计原则

**权限最小化**

-   代码审查和安全扫描 Agent 只有只读权限
-   只有自动修复 Agent 才有写权限

**可审计**

-   每个 Agent 的每一步操作都通过 Hook 记录到审计日志
-   出了问题可以回溯是哪个 Agent 在什么时间做了什么操作

**结果串联**

-   上一个 Agent 的输出是下一个 Agent 的输入
-   每个环节都有明确的输入输出契约

**成本可控**

-   每个 Agent 都设置了 `max_turns` 限制，防止某个环节失控空转

* * *

# 完整流水线代码（1/2）

```python
import asyncio
import json
from datetime import datetime
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

# 审计日志：记录每个 Agent 的每一步操作
audit_log = []

async def audit_hook(input_data, tool_use_id, context):
    """审计 Hook：记录所有工具调用"""
    audit_log.append({
        "time": datetime.now().isoformat(),
        "tool": input_data.get("tool_name"),
        "input": input_data.get("tool_input", {}),
    })
    return {}

# 通用 Hook 配置：所有 Agent 共享审计能力
audit_hooks = {
    "PostToolUse": [HookMatcher(matcher=".*", hooks=[audit_hook])]
}
```

* * *

# 完整流水线代码（2/2）

```python
async def run_pipeline():
    """完整的 PR 质量守护流水线"""
    print("🔍 阶段 1/3：代码审查...")
    pr_diff = subprocess.run(
        ["git", "diff", "main...HEAD"],
        capture_output=True, text=True
    ).stdout
    review_result = await run_code_review(pr_diff)

    print("🛡️ 阶段 2/3：安全扫描...")
    security_result = await run_security_scan()

    print("🔧 阶段 3/3：自动修复...")
    fix_result = await run_auto_fix(review_result, security_result)

    # 保存审计日志
    with open("audit-log.json", "w") as f:
        json.dump(audit_log, f, indent=2, ensure_ascii=False)

    print(f"✅ 流水线完成，审计日志已保存（共 {len(audit_log)} 条操作记录）")
```

* * *

# 高级功能：Hooks

**Hooks 让你在 Agent 执行的关键时刻插入自定义代码**

支持的 Hook 类型：

-   **`PreToolUse`**：工具执行前
-   **`PostToolUse`**：工具执行后
-   **`Stop`**：Agent 停止时
-   **`SessionStart`**、**`SessionEnd`**：会话开始/结束

**实际用途**：

-   审计日志：记录 Agent 的每一步操作
-   安全拦截：阻止 Agent 修改某些关键文件
-   通知推送：Agent 完成任务时发送消息
-   成本监控：统计工具调用次数和 token 消耗

* * *

# 高级功能：子 Agent

**当任务足够复杂时，定义多个专门的子 Agent**

```python
async for message in query(
    prompt="用 code-reviewer agent 审查这个项目的代码质量",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep", "Task"],
        agents={
            "code-reviewer": AgentDefinition(
                description="专业代码审查员，负责质量和安全审查",
                prompt="分析代码质量，找出潜在问题并给出改进建议。",
                tools=["Read", "Glob", "Grep"],
            ),
            "test-writer": AgentDefinition(
                description="测试专家，负责编写单元测试",
                prompt="为缺少测试的函数编写单元测试。",
                tools=["Read", "Write", "Bash"],
            ),
        },
    ),
):
    if hasattr(message, "result"):
        print(message.result)
```

* * *

# MCP 集成：接入外部世界

**让 Agent 不仅能操作本地文件，还能连接数据库、浏览器、第三方 API**

**接入 Playwright：让 Agent 操作浏览器**

```python
async for message in query(
    prompt="打开 example.com 并描述你看到了什么",
    options=ClaudeAgentOptions(
        mcp_servers={
            "playwright": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"]
            }
        }
    ),
):
    print(message.result)
```

* * *

# 常见的 MCP 集成场景

MCP 服务器

用途

典型场景

**Playwright**

浏览器自动化

E2E 测试、截图、爬虫

**PostgreSQL/MySQL**

数据库操作

数据查询、迁移、备份

**Slack/Email**

通知推送

Agent 完成任务后发送通知

**GitHub**

代码仓库操作

自动创建 PR、管理 Issue

* * *

# 错误处理和调试

**常见问题排查**

问题

可能原因

解决方案

`CLINotFoundError`

Claude Code CLI 未安装

`npm install -g @anthropic-ai/claude-code`

`ProcessError`

Agent 执行失败

检查 `exit_code` 和日志

Agent 一直不停止

`max_turns` 设置过大

降低 `max_turns` 或优化 prompt

工具调用失败

权限不足

检查 `allowed_tools` 和 `permission_mode`

* * *

# 调试技巧

**1\. 打印所有消息**

```python
async for message in query(prompt="...", options=options):
    print(f"[{message.type}] {message}")
```

**2\. 使用 Hooks 记录日志**

```python
async def debug_hook(input_data, tool_use_id, context):
    print(f"Tool: {input_data.get('tool_name')}")
    print(f"Input: {input_data.get('tool_input')}")
    return {}
```

**3\. 限制执行轮数**

```python
options = ClaudeAgentOptions(max_turns=5)  # 防止死循环
```

* * *

# Agent SDK vs 其他 Agent 框架

框架

最适合的场景

核心优势

学习曲线

**Claude Agent SDK**

代码开发、文件操作、命令执行

开箱即用的开发工具，无需自己实现

低

**LangChain**

构建复杂的通用 AI 应用

高度自定义，生态丰富

高

**CrewAI**

模拟多角色协作场景

角色扮演、任务分配

中

**LlamaIndex**

知识库问答系统

连接企业数据与 LLM

中

* * *

# 最佳实践

**1\. Prompt 要具体**

-   ❌ 不好：`prompt="优化代码"`
-   ✅ 好：`prompt="重构 src/utils.py 的 parse_config 函数：提取重复的 JSON 解析逻辑，添加错误处理，补充单元测试"`

**2\. 限制执行轮数**

```python
options = ClaudeAgentOptions(max_turns=15)  # 防止死循环
```

**3\. 权限最小化**

```python
# 只读任务：不给写权限
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Grep"],
    permission_mode="bypassPermissions"
)
```

* * *

# 最佳实践（续）

**4\. 使用 Hooks 做审计**

```python
audit_log = []

async def audit_hook(input_data, tool_use_id, context):
    audit_log.append({
        "time": datetime.now().isoformat(),
        "tool": input_data.get("tool_name"),
        "input": input_data.get("tool_input"),
    })
    return {}

options = ClaudeAgentOptions(
    hooks={"PostToolUse": [HookMatcher(matcher=".*", hooks=[audit_hook])]}
)
```

**5\. 结构化输出**

-   要求输出 JSON 格式，方便后续处理和解析

* * *

# 场景速查表

场景

核心工具

权限模式

难度

**自动修 Bug**

Read, Edit, Bash, Grep

acceptEdits

入门

**代码审查**

Read, Glob, Grep

bypassPermissions

入门

**CI/CD 自动修复**

Read, Edit, Bash

acceptEdits

中级

**技术调研报告**

WebSearch, WebFetch, Write

acceptEdits

入门

**浏览器自动化**

MCP (Playwright)

acceptEdits

中级

**多 Agent 协作**

Task + AgentDefinition

混合

高级

**数据库操作**

MCP (PostgreSQL/MySQL)

bypassPermissions

中级

* * *

# 本周回顾

* * *

# 学习进度检查

✅ 理解了 Agent SDK 是什么（和 CLI、基础 SDK 的区别） ✅ 掌握了核心概念（Agent Loop、工具系统、权限模式） ✅ 会写单个 Agent（自动修 bug、代码审查） ✅ 会构建流水线（审查 → 扫描 → 修复 → 测试） ✅ 掌握了高级功能（Hooks、子 Agent、MCP 集成） ✅ 记住了最佳实践（Prompt 具体化、限制轮数、权限最小化）

* * *

# 自测题

**1\. 场景判断题**：以下场景分别该用什么工具？

-   翻译一段文本 → ？
-   日常写代码、改 bug → ？
-   每次 PR 提交后自动跑代码审查 → ？

**2\. 权限模式题**：以下任务分别该用什么权限模式？

-   只读代码审查 → ？
-   自动修复 bug → ？
-   生产环境操作 → ？

* * *

# 自测题（续）

**3\. 设计题**： 如果要构建一个「每天早上自动检查系统日志，发现异常就发 Slack 通知」的 Agent，你会怎么设计？需要哪些工具？需要接入哪些 MCP 服务器？

**4\. 调试题**： 你的 Agent 一直不停止，跑了 50 轮还在改代码，可能是什么原因？怎么解决？

* * *

# 本周作业

**必做**：

-   实现一个自动修 Bug Agent，能够自己找代码、定位问题、修复、跑测试
-   记录 Agent 的执行过程和遇到的问题
-   总结你对 Agent SDK 的理解

**选做**：

-   构建一个完整的 CI/CD 流水线（代码审查 → 安全扫描 → 自动修复）
-   尝试接入 MCP 服务器（Playwright、数据库等）
-   分享你的 Agent 到课程讨论区

* * *

# 下周预告

## AI Agent 进阶——记忆系统与决策树

**从「执行任务」到「理解业务」****从「单次调用」到「持续学习」****从「工具编排」到「自主决策」**

* * *

# Q&A

## 有问题吗？

* * *

# 谢谢！

## 期待下周看到你的 Agent

**记住**：

> Prompt 要具体 权限要最小化 审计要完整
