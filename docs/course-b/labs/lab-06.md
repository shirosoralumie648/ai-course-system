# Lab 06：用 AI 写后端接口与密钥安全

<ChapterIntroduction duration="2-3 小时" output="分层后端 API + 安全 AI 代理接口 + 接口文档 + 测试日志 + 密钥检查记录" prerequisite="完成 Lab 05；已有前端、Supabase 和基础后端骨架；会阅读 Express、Next.js Route Handler 或 Supabase Edge Function 代码" :tags="['API 接口', '后端代理', '密钥安全', 'AI 写代码', 'OpenAPI', '测试']">

- 用高质量 prompt 引导 AI 生成分层后端接口
- 把 AI API Key 锁在后端环境变量中
- 用文档、测试、日志和 Network 截图证明接口安全可用

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '定接口', description: '写清输入、输出和错误规则' },
  { title: '让 AI 写', description: '生成分层后端代码' },
  { title: '人工审查', description: '检查密钥、校验和错误脱敏' },
  { title: '接前端', description: '页面只调用自己的后端接口' },
  { title: '补文档测试', description: '生成 OpenAPI 或接口说明并跑测试' },
  { title: '安全自检', description: '提交日志、Network 和 diff 证据' }
]" />

## 实验目标

完成一个由 AI 辅助编写、但经过人工审查和验证的后端接口。实验重点是接口工程质量和密钥安全：前端不能直接持有 AI API Key，后端必须做输入校验、错误处理和日志记录。

## 实验任务

为你的产品实现一个后端接口。推荐选择：

- `/api/ai/chat`：把用户消息转发给大模型
- `/api/generate-plan`：根据用户输入生成学习计划
- `/api/summarize`：总结用户上传或保存的内容
- `/api/content-review`：审核用户输入
- `/api/items`：带 Supabase 读写的业务接口

必须使用后端 route、server action、Edge Function 或独立 API 服务。不要从浏览器直接请求模型供应商接口。

## 操作步骤

### 1. 写接口规格

在动手前写清楚：

- URL 和 HTTP method
- 请求 JSON
- 响应 JSON
- 参数校验规则
- 错误码和错误文案
- 是否需要登录
- 是否读写 Supabase
- 是否调用外部 AI API

示例：

```text
POST /api/ai/chat
输入：{ "message": string }
限制：message 必填，最长 1000 字
输出：{ "answer": string, "requestId": string }
错误：400 参数错误；500 服务暂不可用
安全：OPENAI_API_KEY 只从后端环境变量读取
```

### 2. 用 AI 生成后端代码

把接口规格、技术栈、目录结构、环境变量约束交给 AI。要求它按分层结构生成，例如：

- `routes`
- `controllers`
- `services`
- `middlewares`
- `tests`

如果使用 Next.js 或 Supabase Edge Function，也要保持路由逻辑、业务逻辑、外部调用逻辑尽量分离。

记录 prompt 和 AI 的计划。

### 3. 人工审查生成代码

重点检查：

- 是否硬编码 API Key
- 是否把上游原始错误直接返回给前端
- 是否校验输入为空、超长、类型错误
- 是否记录必要日志但不记录敏感信息
- 是否误用 service_role key
- 是否新增无关依赖

保存 `git diff` 和你的审查批注。

### 4. 接入前端调用

前端页面只能调用你自己的后端接口，例如 `/api/ai/chat`。页面至少包含：

- 输入区域
- 提交按钮
- loading 状态
- 成功结果
- 错误提示

保存浏览器 Network 截图，证明请求目标是自己的后端接口，而不是模型供应商接口。

### 5. 生成接口文档和测试

用 AI 辅助生成：

- OpenAPI/Swagger 片段，或一份接口文档
- 至少 2 个测试用例，覆盖成功和参数错误

运行测试或手动 curl：

```bash
curl -X POST http://localhost:3000/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"请用一句话介绍我的产品"}'
```

保存测试日志或 curl 输出。

### 6. 完成密钥安全检查

提交前检查：

- `.env` 未提交
- `.env.example` 只有占位值
- `git diff` 中没有真实 key
- 浏览器 Network 看不到模型供应商 key
- 后端日志没有打印完整 key

## 提交要求

- 接口规格文档
- AI prompt 或对话摘要
- 后端代码 diff
- 前端调用页面截图
- 接口文档或 OpenAPI 片段
- 测试日志、curl 输出或 API 日志
- 浏览器 Network 截图
- 密钥检查记录
- `.env.example`

## 验收标准

- 后端接口和产品场景相关
- AI API Key 或其他 secret 只在后端环境变量中使用
- 前端不直接调用模型供应商接口
- 有输入校验、错误处理和 loading/error UI
- 有接口文档和至少一种测试证据
- 日志、截图和 diff 能对应同一条调用链

## 常见问题

**可以让 AI 一次写完整后端吗？**
可以，但必须人工审查。AI 写出的代码没有测试和安全证据，不能直接视为完成。

**接口调用真实模型失败怎么办？**
保存错误日志和失败提示即可。若供应商不可用，可使用教师提供的测试接口，但仍要通过后端代理。

**为什么要生成接口文档？**
后端接口是前后端协作边界。文档能让你后续接 Dify、支付、部署时减少猜测。

## 评分标准

| 维度 | 分值 | 说明 |
|---|---:|---|
| 接口规格 | 15 | 输入、输出、错误和安全要求是否清楚 |
| 后端实现 | 25 | 分层、校验、错误处理是否合理 |
| 密钥安全 | 25 | key 是否只在后端，Network 和 diff 是否干净 |
| 文档测试 | 20 | 接口文档和测试日志是否可信 |
| AI 使用记录 | 15 | prompt、计划和人工审查是否完整 |
