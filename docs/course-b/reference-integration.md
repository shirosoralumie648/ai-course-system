# 课程 B reference 融入方案：从全栈产品到工程证据

> 课程 B 的 reference 不能只做"推荐阅读"。它必须进入每周的技术决策、课堂 Demo、学生作业、项目验收和答辩证据。学生可以不运行大型 reference 仓库，但必须学会从真实项目中读结构、读边界、读验证方式。

## 使用原则

| 原则 | 具体做法 |
|---|---|
| 真实项目校准课程 | 用 reference 判断课程有没有漏掉后端、权限、部署、RAG 评测、跨平台约束 |
| 局部阅读 | 每周只要求阅读一个目录、一个示例、一个配置或一个接口，不要求跑完整仓库 |
| 改造成课堂 Demo | 教师把 reference 的复杂做法压缩成 20-30 分钟可讲的最小例子 |
| 证据化提交 | 每周作业都要附截图、diff、测试日志、调用日志、RAG eval 或部署链接 |
| 不照抄 | 学生必须说明哪些做法被简化、哪些生产能力暂时不做 |

## 课程 B 的 reference 主线

| 阶段 | 周次 | reference 作用 |
|---|---|---|
| 产品与前端基础 | Week 01-04 | 建立产品拆解、设计系统、CLI/Git 和 AI coding 证据意识 |
| 全栈产品闭环 | Week 05-07 | 补齐数据库、认证、AI 后端、支付、部署的真实边界 |
| RAG 与知识系统 | Week 08-10 | 从平台 RAG 走到代码 RAG、评测和知识治理 |
| 跨平台交付 | Week 11-14 | 判断 Web、PWA、小程序、移动端的真实取舍 |
| Agent 工程与答辩 | Week 15-16 | 用 rules、skills、MCP、human gate 和 trace 约束最终交付 |

## Week 01：AI 全栈产品导论

**参考来源**

- `reference/repos/fullstack-ai/vercel-ai-chatbot`
- `reference/repos/production-apps/dub`
- `reference/repos/production-apps/cal-com`

**教师怎么借鉴**

教师从真实产品中抽出"一个功能背后有几层"：页面、路由、数据、权限、AI/业务逻辑、部署、监控。不要让学生一上来写代码，先训练他们看产品结构。

**课堂 Demo**

用一个 AI chatbot 产品拆解：

| 层 | 学生看到的东西 | 背后需要的工程能力 |
|---|---|---|
| UI | 输入框、消息列表、按钮 | 组件、状态、响应式 |
| 数据 | 历史对话 | 数据库、用户关联 |
| AI | 流式回答 | 后端 API、模型调用、错误处理 |
| 权限 | 登录后看自己的记录 | auth、session、RLS |
| 部署 | 公开访问 | 环境变量、构建、回滚 |

**学生任务**

选择自己的期末产品方向，提交产品拆解表：

- 用户流程图
- 数据对象列表
- 需要的后端能力
- 需要的 AI 能力
- 需要的验证证据

**验收标准**

- 至少拆出 5 个工程层面。
- 每个层面都有"本课程哪一周完成"。
- 不允许只写"做一个 AI 应用"。

## Week 02：设计到代码

**参考来源**

- `reference/repos/fullstack-ai/shadcn-ui`
- Refactoring UI
- The Design of Everyday Things

**教师怎么借鉴**

shadcn/ui 的价值不是"好看组件"，而是组件命名、变体、组合和可复制的 UI 规范。课程要从 reference 中借"组件化页面生成"和"AI UI 不能只看第一眼"。

**课堂 Demo**

1. 用 AI 生成一个 dashboard。
2. 用设计检查表审查：层级、对齐、按钮状态、表单标签、空状态。
3. 从 shadcn/ui 抽一个 Button/Card/Form 的组件约定，改写当前页面。
4. 记录 before/after 截图。

**学生任务**

提交：

- AI 初稿页面截图
- 修改后页面截图
- 组件拆分说明
- 一个最小响应式检查记录

**验收标准**

- 页面能运行。
- 至少一个组件被命名并复用。
- 不能只用"更美观"作为改进理由。

## Week 03：组件库与设计系统

**参考来源**

- `reference/repos/fullstack-ai/shadcn-ui`
- `reference/repos/courses/web-dev-for-beginners`

**教师怎么借鉴**

参考项目用来解释：组件库不是素材库，而是一套约束。学生要学会用同一套按钮、表单、卡片、色彩和间距支撑多个页面。

**课堂 Demo**

把两个 AI 生成页面统一：

| 问题 | 改法 |
|---|---|
| 两个页面按钮颜色不同 | 抽出 button variant |
| 表单间距不一致 | 统一 form field spacing |
| 卡片标题层级混乱 | 统一 heading 和 description |
| 状态文案不一致 | 统一 loading/empty/error pattern |

**学生任务**

为期末项目做一个 mini design system：

- 颜色
- 字体层级
- 按钮状态
- 表单状态
- 卡片样式
- 空状态/错误状态

**验收标准**

- 至少 2 个页面使用同一套规则。
- 提交一次 "不一致 -> 统一" 的 diff 或截图。

## Week 04：CLI、Git 与 AI 工程流

**参考来源**

- `reference/repos/courses/missing-semester`
- `reference/repos/agentic-coding/aider`
- `reference/repos/agentic-coding/gemini-cli`
- `reference/repos/agentic-coding/anthropic-courses`

**教师怎么借鉴**

Missing Semester 提供 CLI/Git 基础，aider 和 Gemini CLI 提供 AI coding 工具对比。课程要把学生从"AI 帮我改了"拉回"我能看 diff、跑测试、知道改了什么"。

**课堂 Demo**

同一个小任务用两个工具执行：

```text
任务：给产品列表增加搜索框。
约束：不改数据结构，不重写页面，只加前端过滤。
验收：输入关键词后列表减少；清空后恢复。
```

比较：

- 工具是否先计划？
- 修改了哪些文件？
- diff 是否可读？
- 是否运行测试或本地验证？
- 人工该拒绝哪类改动？

**学生任务**

提交工具对比记录：

| 项 | Claude Code/Codex | 另一个工具 |
|---|---|---|
| 输入任务 | | |
| 输出计划 | | |
| 修改文件 | | |
| diff 风险 | | |
| 验证命令 | | |
| 适合场景 | | |

**验收标准**

- 必须有真实 diff。
- 必须有验证命令或人工走查。
- 不能只写主观体验。

## Week 05：Supabase 数据库、认证与 CRUD

**参考来源**

- `reference/repos/fullstack-ai/supabase`
- Designing Data-Intensive Applications
- Web Application Security

**教师怎么借鉴**

Supabase reference 用来补数据库、auth、storage、edge function 的真实边界。课程 B 本周先聚焦 schema、CRUD 和基础用户边界，不把所有 RLS 细节一次讲完，但必须让学生知道：用户数据要有 owner，权限不能只靠前端隐藏按钮。

**课堂 Demo**

以"任务管理产品"为例建表并接入登录：

| 表 | 字段 | 为什么需要 |
|---|---|---|
| projects | id, name, owner_id | 项目归属 |
| tasks | id, project_id, title, status | 核心业务数据 |
| task_events | id, task_id, action, created_at | 后续审计和历史 |

演示：

1. 建表。
2. 插入一条数据。
3. 页面读取列表。
4. 新增任务。
5. 用户 A 创建记录，用户 B 不能随意看到。
6. 刷新后数据仍在。

**学生任务**

为自己的产品提交：

- 数据对象清单
- schema 截图或 SQL
- CRUD 走查截图
- 登录/用户边界说明
- 一个失败案例：字段缺失、类型错误、越权或网络失败

**验收标准**

- 至少一张表和一条真实数据。
- 至少一个创建或更新操作。
- 刷新后数据仍存在。
- 不能把"页面没显示入口"当成权限。

## Week 06：AI API 后端集成

**参考来源**

- `reference/repos/fullstack-ai/vercel-ai`
- `reference/repos/fullstack-ai/vercel-ai-chatbot`
- `reference/repos/ai-engineering/openai-cookbook`

**教师怎么借鉴**

学生要看到一个真正 AI app 的关键边界：前端只收集输入和展示输出，模型调用在后端，密钥在环境变量，错误和成本要记录。

**课堂 Demo**

实现一个安全 AI endpoint：

```text
POST /api/ai/summarize
输入：用户文本
后端：读取环境变量 -> 调模型 -> 处理错误
输出：summary + usage/debug id
```

教师重点讲：

- 为什么不能在前端放 key。
- streaming 和普通 JSON response 的区别。
- tool calling 何时需要，何时过度。
- mock mode 怎么和 real-call mode 分开。

**学生任务**

提交 AI 接入记录：

- API route 文件位置
- 环境变量清单
- 真实调用截图或日志
- 一条失败处理记录
- 成本或调用次数记录

**验收标准**

- key 不进入前端和仓库。
- 至少一次真实调用。
- 有错误处理，不是空白页面。

## Week 07：支付与部署

**参考来源**

- `reference/repos/fullstack-ai/stripe-checkout-one-time`
- `reference/repos/fullstack-ai/stripe-subscription-use-cases`
- `reference/repos/production-apps/dub`
- Release It!

**教师怎么借鉴**

支付 reference 用来强调：价格、订单状态、webhook 验证必须在后端；部署不是上传完成，而是环境变量、构建命令、回滚和日志。

**课堂 Demo**

支付流程拆解：

| 步骤 | 前端 | 后端 |
|---|---|---|
| 选择商品 | 展示套餐 | 不信任前端价格 |
| 创建 checkout | 请求下单 | 使用后端 price id |
| 支付完成 | 展示结果页 | webhook 更新订单 |
| 查询状态 | 调接口 | 从数据库读订单状态 |

**学生任务**

根据条件二选一：

- 有支付条件：做 Stripe checkout 或 sandbox 支付。
- 无支付条件：做支付模拟，但必须写清楚真实支付要放到后端的部分。

同时提交部署链接。

**验收标准**

- 公开链接可访问。
- 环境变量不泄露。
- 支付/支付模拟流程有状态记录。

## Week 08：Dify 知识库与平台 RAG

**参考来源**

- `reference/repos/rag/dify`
- Dify docs
- Evaluating and Debugging Generative AI

**教师怎么借鉴**

Dify 用来让学生先体验完整知识库链路：导入文档、切块、检索、生成、工作流、测试。重点不是会点界面，而是会记录 RAG 是否答对。

**课堂 Demo**

教师准备 5 份课程文档，演示：

1. 上传文档。
2. 调整切块。
3. 提 10 个问题。
4. 记录命中文档、答案、是否正确、失败原因。
5. 调整设置后对比。

**学生任务**

提交 Dify 检索测试表：

| 问题 | 期望依据 | 检索片段 | 回答 | 是否通过 | 失败原因 |
|---|---|---|---|---|---|

**验收标准**

- 至少 10 条样本。
- 至少 2 条失败样本。
- 有一次设置调整前后对比。

## Week 09：RAG 入门

**参考来源**

- `reference/repos/rag/rag-from-scratch`
- Evaluating and Debugging Generative AI

**教师怎么借鉴**

本周把 Dify 背后的机制拆开：chunking、embedding、retriever、answer generation、eval。学生要从"会用平台"走到"知道每一步为什么会错、怎么验证"。

**课堂 Demo**

用一个最小 RAG 脚本演示完整流程：

1. 把 5 段文档切块。
2. 生成 embedding。
3. 根据问题检索 top-k 片段。
4. 把片段拼进 prompt。
5. 记录答对、答错和无答案场景。

**学生任务**

提交最小 RAG 走查表：

- 文档来源
- chunk 示例
- 检索结果截图或日志
- 5-10 条问题样本
- 至少 1 条失败原因分析

**验收标准**

- 能解释 RAG 的四步：切分、向量化、检索、增强生成。
- 有检索片段证据，不只交最终回答。
- 失败原因能对应到切分、检索或生成某一步。

## Week 10：高级 RAG 与企业知识库

**参考来源**

- `reference/repos/rag/llama-index`
- `reference/repos/rag/haystack`
- `reference/repos/rag/graph-rag`
- `reference/repos/rag/langgraph`

**教师怎么借鉴**

本周把 Dify 背后的机制拆开：chunking、embedding、retriever、rerank、answer generation、eval。再进一步讨论企业知识库的权限、版本、更新、追溯。

**课堂 Demo**

用同一批文档演示三种失败：

| 失败类型 | 表现 | 可能原因 | 改进方向 |
|---|---|---|---|
| 召回失败 | 找不到相关片段 | chunk 太大/太小、关键词不匹配 | 调 chunk、hybrid search |
| 答案幻觉 | 检索到了但乱答 | prompt 没要求引用、模型过度发挥 | 强制证据化回答 |
| 版本冲突 | 新旧制度混用 | 文档没有版本字段 | 元数据过滤 |

**学生任务**

提交 RAG eval sheet 和企业知识库方案：

- 文档来源
- chunk 策略
- 检索策略
- 10 条 eval 样本
- 失败样本分析
- 权限和更新流程

**验收标准**

- 有失败样本，不接受全是通过。
- 改进结论必须对应数据。
- 能说明企业知识库如何更新和下线旧文档。

## Week 11：跨平台 PWA

**参考来源**

- `reference/repos/cross-platform/expo`
- `reference/repos/cross-platform/taro`
- `reference/repos/cross-platform/uni-app`

**教师怎么借鉴**

跨平台 reference 用来防止学生把"我想做 App"当成技术决策。先用 PWA 做低成本验证，再判断是否需要小程序或移动端。

**课堂 Demo**

平台决策矩阵：

| 维度 | Web/PWA | 小程序 | 移动 App |
|---|---|---|---|
| 触达 | 链接即用 | 微信生态强 | 安装后留存强 |
| 能力 | 浏览器能力 | 微信 API | 原生能力多 |
| 成本 | 最低 | 中等 | 最高 |
| 审核 | 无或少 | 平台审核 | 应用商店审核 |
| 适合 | 工具、内容、后台 | 本地服务、社交传播 | 高频、硬件能力 |

**学生任务**

- 给自己的产品填矩阵。
- 把一个页面改成 PWA 或写清楚为什么暂不做。

**验收标准**

- 决策必须基于用户场景，不基于个人喜好。
- PWA 有 manifest 或离线/安装证据。

## Week 12：平台选择与小程序入门

**参考来源**

- `reference/repos/cross-platform/taro`
- `reference/repos/cross-platform/uni-app`
- Taro docs
- uni-app docs

**教师怎么借鉴**

本周进入小程序，不是为了放弃 Web，而是让学生理解平台约束：页面结构、路由、请求限制、发布审核、微信生态能力。

**课堂 Demo**

把 Web 页面迁移成小程序页面时，标注变化：

| Web 思维 | 小程序约束 |
|---|---|
| 浏览器路由 | 小程序页面栈 |
| DOM 操作 | WXML/WXSS/组件模型 |
| 任意网络请求 | 域名白名单 |
| 浏览器存储 | 小程序 storage |
| 网页部署 | 体验版、审核、发布 |

**学生任务**

完成一个小程序前端：

- 1 个首页
- 1 个列表或表单页
- 1 次页面跳转
- 1 次 mock 数据展示

**验收标准**

- 能在开发者工具运行。
- 有平台限制说明。

## Week 13：小程序后端

**参考来源**

- `reference/repos/fullstack-ai/supabase`
- `reference/repos/cross-platform/taro`
- `reference/repos/cross-platform/uni-app`

**教师怎么借鉴**

小程序后端和 Web 后端本质一样：身份、权限、数据库、文件、支付都不能只放前端。Supabase 的权限思想可以迁移到 CloudBase/云开发讲解。

**课堂 Demo**

小程序订单流程：

```text
前端选择商品 -> 云函数校验价格 -> 云数据库创建订单 -> 返回订单状态 -> 前端展示
```

教师强调：

- 价格不信任前端。
- openid/session 是身份基础。
- 支付签名必须后端生成。
- 文件上传要有大小和类型限制。

**学生任务**

为小程序补一个云端流程：

- 登录态或用户标识
- 数据库读写
- 云函数封装
- 错误提示

**验收标准**

- 至少一次云端读写。
- 说明哪些逻辑不能放前端。

## Week 14：小程序、移动端或 PWA 整合

**参考来源**

- `reference/repos/cross-platform/expo`
- `reference/repos/cross-platform/taro`
- `reference/repos/cross-platform/uni-app`

**教师怎么借鉴**

本周不再新增概念，而是要求学生选择一条最小跨平台路径，把期末产品的一条核心流程迁移过去。

**课堂 Demo**

三种整合路线：

| 路线 | 最小产出 | 适合谁 |
|---|---|---|
| PWA | 可安装、可离线打开核心页 | Web 产品已有雏形 |
| 小程序 | 开发者工具可运行核心流程 | 用户在微信生态 |
| 移动端 | Expo/React Native 原型 | 需要相机、定位、推送 |

**学生任务**

提交跨平台整合包：

- 选择理由
- 最小版本截图
- 运行方式
- 未迁移功能清单
- 下一步计划

**验收标准**

- 至少一条核心流程跑通。
- 不要求完整重写。
- 明确写出平台限制。

## Week 15：Rules、Skills、MCP 与 Agent Team

**参考来源**

- `reference/repos/agentic-coding/spec-kit`
- `reference/repos/mcp/mcp-servers`
- `reference/repos/mcp/mcp-typescript-sdk`
- `reference/repos/ai-engineering/openai-agents-python`
- `reference/repos/rag/langgraph`

**教师怎么借鉴**

Agent 工程不是新开一门课，而是最终项目的交付纪律。reference 用来提供 rules、skills、MCP tool、agent handoff、trace 的真实形态。

**课堂 Demo**

把期末项目的最后一轮修改交给 Agent，但设置边界：

```markdown
任务：为 RAG eval 页面增加失败样本筛选。
允许：修改 eval 页面和本地状态。
禁止：修改数据库 schema、删除测试、改环境变量。
Human Gate：任何依赖安装、权限改动、支付相关改动。
验收：筛选按钮可用；原有 10 条样本仍显示；截图和 diff 提交。
```

**学生任务**

提交 Agent 工程包：

- `AGENTS.md` 或等价规则文件
- 角色表
- Human Gate 清单
- 一次执行 trace
- diff 和验证日志

**验收标准**

- 规则具体可执行。
- trace 能区分 Agent 行为和人工决策。
- 不接受"AI 自动完成"的笼统描述。

## Week 16：期末答辩与技术评审

**参考来源**

- `reference/repos/production-apps/cal-com`
- `reference/repos/production-apps/dub`
- `reference/repos/production-apps/twenty`
- `reference/repos/production-apps/medplum`
- `reference/repos/agentic-coding/spec-kit`

**教师怎么借鉴**

生产应用 reference 用来帮助学生答辩时讲清楚取舍：自己做的是课程 MVP，不是生产 SaaS；哪些能力已经验证，哪些能力只是下一步。

**答辩必须覆盖**

| 模块 | 必讲问题 | 证据 |
|---|---|---|
| 产品 | 用户是谁，核心流程是什么 | Demo 或录屏 |
| 前端 | 组件如何复用 | 页面截图和代码 |
| 数据 | schema 为什么这样设计 | 表结构和 CRUD 走查 |
| AI | key 在哪里，失败怎么办 | 调用日志和错误处理 |
| RAG | 如何评测，不准在哪里 | eval sheet |
| 跨平台 | 为什么选这个平台 | 决策矩阵和运行截图 |
| Agent | AI 做了什么，人审了什么 | trace、diff、Human Gate |
| reference | 借鉴了哪里，如何简化 | 阅读范围和改造说明 |

**验收标准**

- 产品能演示核心流程。
- 证据能支撑技术说法。
- 能说清楚没有做什么，以及为什么没有做。

## 教师备课检查表

| 检查项 | 是/否 |
|---|---|
| 本周 reference 是否进入了 Demo，而不是只放在参考资料？ | |
| 学生是否只需读一个可控切面？ | |
| 作业是否要求提交证据？ | |
| 是否明确了不能照抄的部分？ | |
| 是否保留了全栈主线，不被 Agent 或 RAG 单点带偏？ | |

## 学生每周 reference 提交模板

```markdown
## 本周 reference 借鉴说明

- 本周主题：
- 参考项目/材料：
- 阅读范围：
- 我看到的真实项目做法：
- 我借鉴的一个点：
- 我如何改造到自己的项目：
- 我没有照抄的部分：
- 验证证据：
- 下一步还需要补的能力：
```

## 期末 reference 总结模板

```markdown
## 期末 reference 总结

| 模块 | 参考来源 | 借鉴点 | 我的改造 | 证据 |
|---|---|---|---|---|
| 前端 | | | | |
| 数据库/权限 | | | | |
| AI API | | | | |
| RAG | | | | |
| 跨平台 | | | | |
| Agent 工程 | | | | |
```
