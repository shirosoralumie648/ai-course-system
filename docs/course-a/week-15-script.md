# Week 15 讲稿：Claude Agent SDK - 让 AI 自主完成任务

**课程时长**：90 分钟
**授课对象**：熟悉 Python 或 TypeScript 基础的学生
**教学目标**：让学生理解 Agent SDK 的核心概念，能够构建自动化 Agent

* * *

## 课前准备（5 分钟）

### 开场白

大家好！欢迎来到 Week 14 的课程。

在开始之前，我想问大家一个问题：**你们用 Claude Code 这么久了，有没有想过让它「自己干活」，而不是每次都要你盯着？**

（举手互动，观察学生反应）

很好。今天我们要学的 Claude Agent SDK，就是让 AI 真正「自主完成任务」的工具。

想象一下：每次 PR 提交后，AI 自动审查代码、扫描安全漏洞、修复问题、跑测试，全程不需要你盯着。这就是 Agent SDK 的魅力。

### 课程目标

今天结束后，你们每个人都会：

1.  理解 Agent SDK 和 CLI 的区别
2.  掌握 Agent 的核心概念和工作原理
3.  能够构建自动修 bug 的 Agent
4.  了解如何构建企业级 CI/CD 流水线

准备好了吗？让我们开始吧！

* * *

## Part 1：认识 Agent SDK（20 分钟）

### 1.1 小林的困惑（5 分钟）

**\[展示 PPT：小林的故事\]**

让我先给大家讲一个故事。小林用了几个月 Claude Code，一直觉得它就是个「超级终端助手」——你说一句，它做一件事。

直到有一天，她想把「每次 PR 提交后自动跑代码审查」这个流程自动化，才发现 Claude Code 背后有个叫 Agent SDK 的东西。

**\[互动提问\]**
大家有没有类似的需求？想让 AI 自动完成某些重复性任务？

（等待学生回应）

### 1.2 什么是 Agent SDK（5 分钟）

**\[展示 PPT：一句话对比\]**

让我们先搞清楚三个工具的区别：

**Claude Code CLI**：终端交互，人工输入指令，适合日常开发 **Claude Agent SDK**：代码调用，程序化执行，适合 CI/CD、自动化 **基础 anthropic SDK**：API 调用，你自己处理工具循环，适合聊天、生成

**\[停顿，让学生理解\]**

简单来说：CLI 是「你和 AI 对话」，SDK 是「你的程序调用 AI」。

### 1.3 代码量对比（5 分钟）

**\[展示 PPT：代码对比\]**

让我给大家看看，如果用基础 SDK 实现「修复 bug」，需要多少代码：

```python
# 基础 SDK：你得自己写循环处理工具调用
response = client.messages.create(...)
while response.stop_reason == "tool_use":
    result = your_tool_executor(response.tool_use)
    response = client.messages.create(tool_result=result, ...)
```

而用 Agent SDK，只需要：

```python
async for message in query(
    prompt="修复 auth.py 的 bug",
    options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash"]),
):
    print(message)
```

**\[停顿\]**

区别很明显：基础 SDK 需要你自己实现工具循环、工具执行、上下文管理，而 Agent SDK 把这些全部内置了。

### 1.4 使用场景（5 分钟）

**\[展示 PPT：三种工具的使用场景\]**

什么时候该用什么工具？我给大家一个判断标准：

-   **翻译文本、写文案、回答问题** → 基础 anthropic SDK
-   **日常写代码、改 bug、快速任务** → Claude Code CLI
-   **CI/CD 流水线、定时巡检、批量处理** → Agent SDK

**\[互动提问\]**
如果你想每天早上自动检查系统日志有没有异常，该用什么工具？

（等待学生回答：Agent SDK）

对！因为这个任务能「自己跑」，不需要人盯着。

* * *

## Part 2：核心能力（30 分钟）

### 2.1 安装和配置（5 分钟）

**\[展示 PPT：安装和配置\]**

好，理论讲完了。现在让我们动手搭环境。

请大家打开终端，跟着我一起做：

```bash
# Python (需要 3.10+)
pip install claude-agent-sdk

# 设置 API Key
export ANTHROPIC_API_KEY=your-api-key
```

**\[等待学生操作，巡视确认\]**

### 2.2 第一个 Agent（10 分钟）

**\[展示 PPT：Hello World\]**

现在，让我们写第一个 Agent。请大家创建一个文件 `hello_agent.py`：

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

**\[演示运行\]**

```bash
python hello_agent.py
```

**\[等待 Agent 执行\]**

大家看到了吗？我们没有写任何「执行 ls 命令」的代码，只是说了「有哪些文件」，Claude 自己决定用什么工具、怎么执行。

**\[互动\]**
有同学看到结果了吗？分享一下你的目录里有什么文件。

（让 1-2 个学生分享）

### 2.3 Agent Loop 工作原理（5 分钟）

**\[展示 PPT：Agent Loop\]**

让我给大家解释一下 Agent 是怎么工作的。

假设你说「修复 auth.py 的 bug」，Agent 会这样做：

1.  Claude 思考：需要先看代码
2.  调用 Read 工具读取 auth.py
3.  Claude 分析：发现空指针问题
4.  调用 Edit 工具修改代码
5.  调用 Bash 工具运行测试
6.  测试通过，任务完成

**\[停顿\]**

这和人类开发者的工作方式一模一样——先看代码，再改代码，然后跑测试看结果。Agent SDK 把这个循环自动化了。

### 2.4 内置工具（5 分钟）

**\[展示 PPT：内置工具\]**

Agent SDK 最爽的地方是：你不需要自己实现任何工具，Claude 直接就能用。

常用工具有：

-   **Read**：读取文件
-   **Edit**：精确编辑文件
-   **Bash**：执行终端命令
-   **Grep**：正则搜索文件内容
-   **WebSearch**：搜索网页

通过 `allowed_tools` 参数控制 Agent 能用哪些工具。

### 2.5 权限模式（5 分钟）

**\[展示 PPT：权限模式\]**

这是一个非常重要的概念。Agent SDK 提供了三种权限模式：

-   **`bypassPermissions`**：所有操作都不需要确认（只读任务）
-   **`acceptEdits`**：文件修改自动通过，危险操作需确认（代码审查、自动修复）
-   **`requirePermissions`**：所有操作都需要人工确认（生产环境）

**\[强调\]**

记住一个安全原则：第一次跑新 Agent 时，永远先用 `requirePermissions` 模式，看它到底会做什么操作。确认没问题后，再改成其他模式。

* * *

## Part 3：实战场景（30 分钟）

### 3.1 自动修 Bug Agent（10 分钟）

**\[展示 PPT：实战场景一\]**

现在我们来写第一个真正有用的 Agent——自动修 bug。

**需求**：用户反馈登录时偶尔报 500 错误，需要排查 `src/auth/` 目录下的代码并修复。

**\[展示代码\]**

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

**\[演示运行或展示运行效果\]**

大家看到了吗？Agent 自己编排了步骤：

1.  搜索错误日志 → 找到 auth.py 第 45 行
2.  读取代码 → 发现数据库连接失败时没有正确处理异常
3.  修改代码 → 添加异常处理
4.  运行测试 → 所有测试通过

**核心价值**：你只描述了任务，Agent 自己决定了执行顺序。

### 3.2 代码审查 Agent（10 分钟）

**\[展示 PPT：实战场景二\]**

第二个场景：每次 PR 提交后，自动审查代码质量，但不做任何修改——只输出报告。

**关键设计**：

-   只读权限：`allowed_tools=["Read", "Glob", "Grep"]`
-   跳过确认：`permission_mode="bypassPermissions"`（只读操作无风险）
-   结构化输出：要求输出 JSON 格式

**\[展示代码并讲解\]**

这个 Agent 的特点是：它只看不改，所以可以放心用 `bypassPermissions` 模式。

### 3.3 企业级 CI/CD 流水线（10 分钟）

**\[展示 PPT：实战场景三\]**

前面的场景都是单个 Agent 做单件事。但在真实的企业环境中，我们需要的是一条完整的流水线。

**需求**：每次 PR 提交后，自动触发： **代码审查 → 安全扫描 → 自动修复 → 测试验证 → 生成报告**

**\[展示 PPT：架构图\]**

核心思想：每个 Agent 只做一件事，权限最小化，结果串联传递。

**\[展示代码框架\]**

```python
async def run_pipeline():
    print("🔍 阶段 1/3：代码审查...")
    review_result = await run_code_review(pr_diff)

    print("🛡️ 阶段 2/3：安全扫描...")
    security_result = await run_security_scan()

    print("🔧 阶段 3/3：自动修复...")
    fix_result = await run_auto_fix(review_result, security_result)

    print("✅ 流水线完成")
```

**\[展示 PPT：企业级设计原则\]**

这个流水线体现了几个关键的企业级设计原则：

1.  **权限最小化**：代码审查和安全扫描 Agent 只有只读权限
2.  **可审计**：每个 Agent 的每一步操作都通过 Hook 记录到审计日志
3.  **结果串联**：上一个 Agent 的输出是下一个 Agent 的输入
4.  **成本可控**：每个 Agent 都设置了 `max_turns` 限制

* * *

## Part 4：高级功能（10 分钟）

### 4.1 Hooks（5 分钟）

**\[展示 PPT：Hooks\]**

Hooks 让你在 Agent 执行的关键时刻插入自定义代码。

支持的 Hook 类型：

-   **`PreToolUse`**：工具执行前
-   **`PostToolUse`**：工具执行后
-   **`Stop`**：Agent 停止时

**实际用途**：

-   审计日志：记录 Agent 的每一步操作
-   安全拦截：阻止 Agent 修改某些关键文件
-   通知推送：Agent 完成任务时发送消息

### 4.2 MCP 集成（5 分钟）

**\[展示 PPT：MCP 集成\]**

Agent SDK 还能无缝接入 MCP 服务器——让 Agent 不仅能操作本地文件，还能连接数据库、浏览器、第三方 API。

**常见场景**：

-   **Playwright**：浏览器自动化（E2E 测试、截图）
-   **PostgreSQL/MySQL**：数据库操作
-   **Slack/Email**：通知推送
-   **GitHub**：代码仓库操作

* * *

## Part 5：最佳实践和调试（10 分钟）

### 5.1 最佳实践（5 分钟）

**\[展示 PPT：最佳实践\]**

让我给大家总结几条「让 Agent 不出乱子」的规矩：

**1\. Prompt 要具体**

-   ❌ 不好：`prompt="优化代码"`
-   ✅ 好：`prompt="重构 src/utils.py 的 parse_config 函数：提取重复的 JSON 解析逻辑，添加错误处理"`

**2\. 限制执行轮数**

```python
options = ClaudeAgentOptions(max_turns=15)  # 防止死循环
```

**3\. 权限最小化**

-   只读任务：不给写权限
-   写任务：限定工具范围

**4\. 使用 Hooks 做审计**

-   记录每个 Agent 的每一步操作

**5\. 结构化输出**

-   要求输出 JSON 格式，方便后续处理

### 5.2 错误处理和调试（5 分钟）

**\[展示 PPT：常见问题排查\]**

当 Agent 跑不通时，怎么办？

**常见问题**：

-   `CLINotFoundError`：Claude Code CLI 未安装
-   `ProcessError`：Agent 执行失败
-   Agent 一直不停止：`max_turns` 设置过大或 prompt 太模糊

**调试技巧**：

1.  打印所有消息：`print(f"[{message.type}] {message}")`
2.  使用 Hooks 记录日志
3.  限制执行轮数：`max_turns=5`

**\[互动\]**
如果你的 Agent 跑了 50 轮还在改代码，可能是什么原因？

（引导学生回答：Prompt 太模糊、没有设置 max\_turns）

* * *

## 本周回顾（5 分钟）

### 6.1 学习进度检查

**\[展示 PPT：学习进度检查\]**

让我们回顾一下今天学到了什么：

✅ 理解了 Agent SDK 是什么（和 CLI、基础 SDK 的区别） ✅ 掌握了核心概念（Agent Loop、工具系统、权限模式） ✅ 会写单个 Agent（自动修 bug、代码审查） ✅ 会构建流水线（审查 → 扫描 → 修复 → 测试） ✅ 掌握了高级功能（Hooks、子 Agent、MCP 集成） ✅ 记住了最佳实践（Prompt 具体化、限制轮数、权限最小化）

### 6.2 本周作业

**\[展示 PPT：作业要求\]**

**必做**：

-   实现一个自动修 Bug Agent，能够自己找代码、定位问题、修复、跑测试
-   记录 Agent 的执行过程和遇到的问题
-   总结你对 Agent SDK 的理解

**选做**：

-   构建一个完整的 CI/CD 流水线（代码审查 → 安全扫描 → 自动修复）
-   尝试接入 MCP 服务器（Playwright、数据库等）
-   分享你的 Agent 到课程讨论区

**截止时间**：下周上课前

* * *

## 下周预告（3 分钟）

**\[展示 PPT：下周预告\]**

下周我们要学什么？

**Week 15：AI Agent 进阶——记忆系统与决策树**

-   从「执行任务」到「理解业务」
-   从「单次调用」到「持续学习」
-   从「工具编排」到「自主决策」

我们会学习如何让 Agent 真正变成「会思考的助手」。

* * *

## Q&A（5 分钟）

**\[展示 PPT：Q&A\]**

现在是提问时间。大家有什么问题吗？

（回答学生问题）

* * *

## 结束语（2 分钟）

**\[展示 PPT：结束语\]**

今天我们学习了 Claude Agent SDK，从单个 Agent 到企业级流水线。

我希望大家记住三句话：

> Prompt 要具体 权限要最小化 审计要完整

不要担心做得不够好，不要害怕犯错。每个人都是从第一个 Agent 开始的。

期待下周看到你们的作品！

谢谢大家！

* * *

## 课后反思（教师用）

### 观察要点

-   学生是否都成功运行了第一个 Agent？
-   哪些学生遇到了困难？是什么类型的困难？
-   学生对 Agent SDK 的接受程度如何？
-   课堂互动是否充分？

### 改进建议

-   如果学生普遍卡在环境配置，下次课可以提前准备安装脚本
-   如果时间不够，可以压缩「高级功能」部分
-   如果学生反应热烈，可以增加更多实战演示

### 下周准备

-   提醒学生完成本周作业
-   准备 Week 15 的演示项目
-   收集本周作业，选出优秀作品在下周展示
