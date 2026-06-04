# 课程 A reference 融入方案：从资料到课堂

> 课程 A 的目标不是让非计算机专业学生啃大型源码，而是让 reference 进入他们的产品判断、原型质量和 AI 协作过程。每周只读一个小切面，只借一个明确做法，只交一个可验证产物。

## 使用原则

| 原则 | 具体做法 |
|---|---|
| 轻量阅读 | 不要求运行大型仓库，只看 README、目录结构、一个页面、一个示例或一段流程 |
| 课程化改写 | 教师把参考项目做法改成课堂小案例，不直接搬生产代码 |
| 证据优先 | 每次借鉴都要有截图、diff、走查记录、访谈记录或验证日志 |
| 保持 Course A 边界 | 学生做产品原型和 AI 协作流程，不做生产级全栈实现 |
| 为 Course B 铺垫 | 涉及数据库、支付、RAG、跨平台时，只讲概念和接口边界，深度留给课程 B |

## Week 01：小游戏热身与"能跑起来"标准

**参考来源**

- `reference/repos/courses/web-dev-for-beginners`
- `reference/repos/fullstack-ai/vercel-ai-chatbot`

**教师怎么借鉴**

教师不讲复杂框架，只抽取两个点：第一，入门项目应该有清楚的目标、运行方式和可观察结果；第二，一个应用即使很小，也应该让学生看见"文件 -> 运行 -> 页面 -> 修改 -> 再运行"的闭环。

**课堂活动**

1. 给学生展示一个小项目目录：`index.html`、`style.css`、`script.js`。
2. 让学生先说出每个文件可能负责什么。
3. 用 AI 生成一个小游戏后，不立刻评价代码，而是先问：它能不能运行？用户能不能玩一轮？失败时有没有错误信息？
4. 对比 reference 里的入门项目说明，让学生补一段自己的运行说明。

**学生任务**

```markdown
## Week 01 reference 借鉴记录

- 我看的参考材料：
- 它如何说明"项目怎么跑起来"：
- 我给自己小游戏补充的运行说明：
- 我实际运行的截图：
- 我遇到的第一个错误和处理方式：
```

**验收标准**

- 原型能运行，而不是只提交代码截图。
- README 或作业里写清楚打开方式。
- 至少记录一个真实错误或一次修改。

## Week 02：AI IDE 入门与第一个可控页面

**参考来源**

- `reference/repos/courses/web-dev-for-beginners`
- `reference/repos/fullstack-ai/shadcn-ui`

**教师怎么借鉴**

Web Dev for Beginners 用小任务帮助学生建立页面结构感；shadcn/ui 强调组件边界和一致性。课程 A 不讲组件库细节，只借"页面应该由可命名的区域组成"这个思想。

**课堂活动**

1. 拿一个 AI 生成的页面，让学生圈出标题区、输入区、结果区、按钮区。
2. 让 AI IDE 修改一个区域，而不是"把页面变好看"。
3. 讲清楚 prompt 里的三个约束：只改哪里、不改哪里、改完如何验证。

**学生任务**

- 用 AI IDE 做一个单页工具。
- 标注页面的 3-5 个区域。
- 让 AI 只修改其中一个区域。
- 截图对比修改前后。

**验收标准**

- 能说清楚 AI 改了哪个区域。
- 没有把整个页面反复重写。
- 修改前后有对比截图。

## Week 03：Claude Code 与 chatbot/coding agent 区分

**参考来源**

- `reference/repos/agentic-coding/anthropic-courses`
- `reference/repos/agentic-coding/aider`
- DeepLearning.AI Claude Code 短课

**教师怎么借鉴**

本周要纠正一个常见误解：Claude Code 不是更聪明的聊天框，而是能读取项目、提出计划、修改文件、展示 diff、运行命令的 coding agent。参考项目里最值得借鉴的是"任务必须落到文件和 diff"。

**课堂活动**

| 对比项 | 普通 chatbot | Claude Code / coding agent |
|---|---|---|
| 输入 | 一段问题 | 任务 + 项目上下文 |
| 输出 | 文字建议 | 计划、文件修改、diff、命令 |
| 风险 | 幻觉答案 | 错改文件、误删内容、测试缺失 |
| 人的责任 | 判断答案 | 审查 diff、运行验证、决定是否接受 |

让学生用同一个任务分别问 chatbot 和 Claude Code：给小游戏加一个重新开始按钮。比较两者输出。

**学生任务**

提交一张对比表：

- chatbot 给了什么建议？
- Claude Code 改了哪些文件？
- diff 里哪一行最需要人工确认？
- 运行后是否真的出现重新开始按钮？

**验收标准**

- 必须包含 diff 或文件改动截图。
- 必须写一条人工审查意见。
- 不能只写"Claude Code 更方便"。

## Week 04：产品创意发现

**参考来源**

- The Mom Test
- Continuous Discovery Habits
- INSPIRED

**教师怎么借鉴**

参考材料的核心不是"问用户喜不喜欢"，而是通过过去行为判断真实需求。课程 A 要把它改成学生可执行的访谈脚本。

**课堂活动**

教师给出两组问题，让学生判断哪组更可靠：

| 坏问题 | 更好的问题 |
|---|---|
| 你会不会用我的 AI 简历工具？ | 你上次改简历是什么时候？卡在哪里？ |
| 这个功能是不是很有用？ | 你现在用什么方法解决这个问题？ |
| 如果免费你会用吗？ | 你最近一次为类似问题花了多少时间或钱？ |

**学生任务**

完成 3 次轻量访谈，每次只问 4 个问题：

1. 你上次遇到这个问题是什么时候？
2. 当时你怎么解决？
3. 哪一步最麻烦？
4. 你有没有尝试过别的工具？

**验收标准**

- 访谈记录必须是过去行为，不是想象意愿。
- 至少删掉一个"听起来很酷但没人真的需要"的创意。

## Week 05：验证创意与收敛 MVP

**参考来源**

- Sprint
- Shape Up
- Escaping the Build Trap

**教师怎么借鉴**

把"做很多功能"纠正为"先证明一个关键假设"。Shape Up 里的 appetite、scope、hill chart 可以改成非 CS 学生能理解的"时间盒 + 必做/不做清单"。

**课堂活动**

让学生把创意拆成三列：

| 必须验证 | 可以模拟 | 暂时不做 |
|---|---|---|
| 用户是否愿意输入信息 | AI 回答可以先用 mock | 登录、支付、复杂权限 |

**学生任务**

写一页 MVP 范围说明：

- 目标用户
- 核心场景
- 本周只验证的一个假设
- 原型必须有的 3 个功能
- 明确不做的 5 个功能

**验收标准**

- 不做清单必须具体。
- 每个保留功能都能对应一个用户痛点。

## Week 06：从需求到单页原型

**参考来源**

- `reference/repos/fullstack-ai/vercel-ai-chatbot`
- Refactoring UI
- Don't Make Me Think

**教师怎么借鉴**

参考 chatbot 产品的输入、输出、历史记录和状态反馈，但课程 A 只要求单页原型。Refactoring UI 和 Don't Make Me Think 用来改进视觉层级和可理解性。

**课堂活动**

教师展示一个 AI 生成的"平铺式页面"，带学生做 4 次改造：

1. 把最重要的输入框放到第一屏。
2. 把按钮文案从"提交"改成具体动作。
3. 给 AI 输出增加空状态和加载状态。
4. 删除和核心流程无关的装饰内容。

**学生任务**

提交原型前后对比：

- 初稿截图
- 修改后的截图
- 改动说明
- 用户从哪里开始、在哪里结束

**验收标准**

- 用户不看说明也能开始使用。
- 页面至少有一种状态反馈：加载、空状态、错误或完成。

## Week 07：接入 AI 能力与 mock/real-call 分离

**参考来源**

- `reference/repos/ai-engineering/openai-cookbook`
- `reference/repos/fullstack-ai/vercel-ai`
- `reference/repos/fullstack-ai/vercel-ai-chatbot`

**教师怎么借鉴**

课程 A 不要求学生掌握后端细节，但必须懂两个边界：API key 不能放前端；mock mode 和真实调用要分开记录。参考项目用来展示真实 AI app 为什么需要后端边界。

**课堂活动**

教师讲一个最小调用链：

```text
用户输入 -> 前端表单 -> 后端接口 -> AI 服务 -> 后端整理 -> 前端展示
```

再讲 mock mode：

```text
用户输入 -> 前端表单 -> 固定示例回答 -> 前端展示
```

学生要理解：mock 可以用于演示流程，但不能伪装成真实 AI 调用。

**学生任务**

- 标注自己的项目现在是 mock 还是真实调用。
- 如果是真实调用，提交调用截图和密钥保护说明。
- 如果是 mock，写清楚未来接入点在哪里。

**验收标准**

- 不把 API key 写进公开页面或仓库。
- 不把 mock 输出说成真实 AI 输出。

## Week 08：完整项目实践与异常处理

**参考来源**

- `reference/repos/fullstack-ai/vercel-ai-chatbot`
- `reference/repos/fullstack-ai/supabase`

**教师怎么借鉴**

让学生看到真实产品不仅有成功路径，还必须处理输入为空、网络失败、回答太长、用户误操作等情况。Supabase 只用来解释"数据以后会存在哪里"，不要求深度实现。

**课堂活动**

给每个项目补一张异常表：

| 异常 | 用户看到什么 | 现在怎么处理 | 以后怎么改 |
|---|---|---|---|
| 输入为空 | 提示请输入内容 | 前端判断 | 保留 |
| AI 调用失败 | 显示重试按钮 | mock 错误 | 后端错误码 |
| 结果不满意 | 允许重新生成 | 暂无 | 加反馈按钮 |

**学生任务**

为原型补 3 个异常或反馈状态。

**验收标准**

- 至少一个错误状态能实际触发。
- 答辩时能演示一次失败处理。

## Week 09：Workflow

**参考来源**

- `reference/repos/agentic-coding/spec-kit`
- Claude Code best practices

**教师怎么借鉴**

Spec Kit 的价值是把"聊天"变成"需求 -> 计划 -> 任务 -> 验证"。课程 A 只借工作流骨架，不要求工具链完整复刻。

**课堂活动**

把一次 AI 修改拆成 6 步：

1. 写清楚任务。
2. 给出当前项目状态。
3. 让 AI 先计划。
4. 人工批准小步计划。
5. 执行修改。
6. 看 diff 并运行验证。

**学生任务**

提交一份个人 AI 开发流程卡片，贴到自己项目 README。

**验收标准**

- 流程里必须有"人工审查 diff"。
- 流程里必须有"失败后怎么办"。

## Week 10：Skills 指南

**参考来源**

- DeepLearning.AI Agent Skills with Anthropic
- `reference/repos/agentic-coding/anthropic-courses`

**教师怎么借鉴**

Skill 的本质是把重复经验包装成可触发、可执行、可验证的流程。课程 A 的 Skill 不需要复杂，只要能让 AI 稳定完成一个小任务。

**课堂活动**

对比一个坏 Skill 和好 Skill：

```markdown
坏：帮我优化页面。

好：当我说"检查原型可用性"时，按顺序检查：
1. 用户入口是否清楚；
2. 按钮文案是否具体；
3. 空状态/错误状态是否存在；
4. 输出一张问题表，不直接改代码。
```

**学生任务**

写一个自己的小 Skill：

- 触发条件
- 输入材料
- 执行步骤
- 输出格式
- 禁止行为

**验收标准**

- Skill 不能只是一段 prompt。
- 必须包含"禁止行为"。

## Week 11：MCP 服务器

**参考来源**

- `reference/repos/mcp/mcp-servers`
- `reference/repos/mcp/mcp-typescript-sdk`
- MCP 官方文档

**教师怎么借鉴**

课程 A 只讲 MCP 的设计思想：让 AI 通过标准接口访问工具和资源。学生先设计工具，不要求生产实现。

**课堂活动**

给校园采访助手设计 3 个 MCP 工具：

| 工具 | 输入 | 输出 | 风险 |
|---|---|---|---|
| search_school_news | 关键词 | 新闻列表 | 来源不可靠 |
| save_interview_note | 采访记录 | 保存结果 | 隐私泄露 |
| list_style_examples | 类型 | 示例文本 | 版权和照抄 |

**学生任务**

为自己的项目设计 2 个 MCP 工具或资源接口。

**验收标准**

- 每个工具必须写输入、输出、错误和人工审批。
- 不能只写"连接数据库"这种泛描述。

## Week 12：Superpowers 与验证纪律

**参考来源**

- Software Engineering at Google
- Google SRE
- `reference/repos/agentic-coding/spec-kit`

**教师怎么借鉴**

把工程文化改写成非 CS 可执行的"完成证明"：没有证据不能说完成。验证不是测试工程师的事，而是每个 AI 使用者的责任。

**课堂活动**

让学生把一句话"我的功能做好了"改成证据链：

```markdown
我完成了重新生成按钮。
证据：
- 修改文件：src/App.vue
- 验证命令：npm run dev
- 走查步骤：输入问题 -> 点击生成 -> 点击重新生成
- 结果截图：...
- 已知问题：第二次生成仍然使用 mock 输出
```

**学生任务**

提交一份 completion proof。

**验收标准**

- 必须包含命令、截图或走查步骤。
- 必须写已知问题。

## Week 13：Spec Coding

**参考来源**

- `reference/repos/agentic-coding/spec-kit`
- `reference/repos/agentic-coding/openhands`
- `reference/repos/agentic-coding/swe-agent`

**教师怎么借鉴**

真实 coding agent 项目告诉学生：复杂任务不能靠一轮 prompt，要靠规格、计划、执行和验证。课程 A 只做一个小任务的 spec-to-plan-to-diff。

**课堂活动**

教师给出一个 bounded task：

```markdown
任务：给原型增加"清空历史记录"按钮。
范围：只改历史记录组件。
不做：登录、多用户同步、数据库保存。
验收：点击按钮后历史记录为空；刷新后不要求保留状态。
```

**学生任务**

为自己的项目写一个 bounded spec，并让 Claude Code 执行。

**验收标准**

- spec 必须写不做什么。
- diff 必须和 spec 范围一致。

## Week 14：长运行任务

**参考来源**

- `reference/repos/agentic-coding/openhands`
- `reference/repos/agentic-coding/swe-agent`
- `reference/repos/agentic-coding/spec-kit`

**教师怎么借鉴**

长运行任务的关键不是放任 AI 跑很久，而是设置检查点、停止条件和恢复记录。参考项目用来展示自动化循环为什么需要状态和日志。

**课堂活动**

把"帮我完善项目"改写成有检查点的任务：

1. 先扫描项目并列问题。
2. 只选 1 个问题修。
3. 修改前输出计划。
4. 修改后输出 diff。
5. 验证失败就停止，不继续乱改。

**学生任务**

设计一个 30 分钟内可完成的长任务计划。

**验收标准**

- 必须有 stop rule。
- 必须有 checkpoint。
- 失败时不能让 AI 自动扩大范围。

## Week 15：Claude Agent SDK

**参考来源**

- `reference/repos/ai-engineering/openai-agents-python`
- `reference/repos/agentic-coding/browser-use`

**教师怎么借鉴**

课程 A 不要求写 SDK 项目，只让学生理解 agent 的输入、工具、handoff、trace 和 guardrail。参考项目用来提供角色和工具边界的真实例子。

**课堂活动**

用产品原型解释一个最小 agent：

| 组成 | 在学生项目里的例子 |
|---|---|
| instruction | 你是采访提纲助手 |
| tool | 搜索过往校园新闻 |
| guardrail | 不编造采访对象说过的话 |
| handoff | 需要事实核查时交给人工 |
| trace | 记录每一步用了什么信息 |

**学生任务**

为自己的项目画一个 agent 结构图。

**验收标准**

- 必须包含人工接管点。
- 必须说明 agent 不能做什么。

## Week 16：Agent Teams 与课程总结

**参考来源**

- `reference/repos/rag/langgraph`
- `reference/repos/ai-engineering/openai-agents-python`
- `reference/repos/agentic-coding/browser-use`

**教师怎么借鉴**

多 agent 不是角色越多越好，而是责任边界清晰。课程 A 只设计 2-3 个角色，并用一次 trace 解释协作。

**课堂活动**

把期末项目拆成三个角色：

| 角色 | 做什么 | 不能做什么 |
|---|---|---|
| Product Agent | 根据访谈整理需求 | 不能替用户决定真实需求 |
| Prototype Agent | 修改页面和交互 | 不能提交未经验证的代码 |
| Review Agent | 检查风险和证据 | 不能代替人类最终批准 |

**学生任务**

在答辩中展示一段 multi-agent trace 或角色协作图。

**验收标准**

- 能说清楚每个角色的输入和输出。
- 有 human gate。
- 不把 agent 输出当成最终事实。

## 教师备课检查表

每周上课前，教师用这张表检查 reference 是否真的进入课程：

| 检查项 | 是/否 |
|---|---|
| 本周是否只选了 1-2 个 reference 切面？ | |
| 是否把参考内容改写成课堂案例？ | |
| 是否有学生能完成的最小任务？ | |
| 是否有明确验收证据？ | |
| 是否避免了生产级复杂度？ | |
| 是否保留 Course A 的非 CS 友好边界？ | |

## 学生最终提交中的 reference 证据

期末项目至少包含这一段：

```markdown
## 我如何使用 reference

### 参考 1
- 来源：
- 我读了哪里：
- 我学到的做法：
- 我如何简化到自己的原型：
- 证据：

### 参考 2（可选）
- 来源：
- 我读了哪里：
- 我学到的做法：
- 我如何简化到自己的原型：
- 证据：
```
