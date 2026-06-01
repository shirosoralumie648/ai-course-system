# 第 6 周：用 AI 写后端接口，把密钥锁在自己人手里

> **接口是前端和数据之间的服务员，密钥是进后厨的门禁卡。** 这周小哲要学会一件全栈开发的核心功夫：让大模型帮他把后端接口、文档、测试一口气写出来——但他会先用一笔惨痛的盗刷账单明白，调用大模型 API 这件事，从第一行代码起就是个工程问题，不是「会不会写 fetch」的问题。

<ChapterIntroduction duration="2 课时（约 4 小时）" output="一套分层清晰、带密钥保护的后端 AI 代理接口 + 自动生成的接口文档与测试 + 流式聊天 Demo" prerequisite="已经能搭起前端 + Node.js 后端 + Supabase 的全栈骨架；会读 Express 路由代码" :tags="['API 接口', 'RESTful', 'Node.js', 'Express', '密钥安全', '后端代理', '错误处理', '流式响应', 'OpenAPI', '测试']">

你会先看小哲怎么把 API Key 暴露在浏览器里被盗刷，然后退一步搞清楚「API 接口到底是什么、为什么要前后端分离」，再学会用高质量的 Prompt 引导大模型写出分层清晰、健壮规范的后端接口，并把文档编写和测试用例这种苦活累活，转化成 AI 擅长的自动化任务。密钥管理、错误兜底、流式输出，一个都不能少。

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '① 小哲的盗刷账单', description: '前端直连 AI 是怎么翻车的' },
  { title: '② API 与前后端分离', description: '餐厅比喻：接口就是服务员' },
  { title: '③ 工程结构与安全封装', description: '分层架构 + 密钥进后端代理' },
  { title: '④ 用好 Prompt 写接口', description: '给足上下文，审查 AI 代码' },
  { title: '⑤ 错误处理与流式响应', description: '让接口扛得住，让用户不干等' },
  { title: '⑥ 文档、测试与上线清单', description: 'OpenAPI / Jest / 安全自检' }
]" />

---

## 1. 小哲的第一次 AI 集成翻车

前五周，小哲已经把全栈骨架搭起来了：前端页面、Node.js 后端、Supabase 数据库都跑通了。这周他想给应用加个亮点功能——一个「智能助手」，用户输入问题，AI 给出回答。

他打开文档，照着大模型 API 的示例，三分钟就在前端写出了第一版：

```javascript
// ❌ 危险写法：在前端 JS 里直接调用 AI API
async function askAI(userInput) {
  const res = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      // 致命错误：密钥被打包进前端代码
      Authorization: 'Bearer sk-proj-abc123真实密钥写在这里'
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini',
      messages: [{ role: 'user', content: userInput }]
    })
  })
  const data = await res.json()
  return data.choices[0].message.content
}
```

页面一刷新，AI 真的回答了。小哲很得意，当天就把项目部署上线发给同学体验。

三天后，他收到了 AI 服务商的一封邮件：**本月用量异常，账单 ￥4200。** 小哲一共就测试了几十次，怎么会有这么多调用？

他打开浏览器的开发者工具，点开 Network 面板，一眼就看见了那串 `sk-proj-...` 开头的密钥——**任何打开他网站的人，按 F12 都能直接抄走这把钥匙。** 有人把密钥扒下来，挂到自己的脚本上疯狂调用，账单全记在小哲头上。

::: warning 小哲的教训
**前端能看到的一切，用户都能看到。** 浏览器里的 JavaScript 是公开的，打包后的密钥不是「藏起来」了，只是「换了个地方明文写着」。任何写进前端的密钥，等于贴在公告栏上。小哲第一次意识到：调 AI 不是写一句 fetch 那么简单，**密钥放在哪、调用走哪条路，才是第一道工程题。**
:::

要把这道工程题做对，小哲得先退一步，把一个一直被他跳过的概念搞清楚：那个夹在「前端页面」和「数据」之间、本该由它来调 AI 的东西——**后端 API 接口**，到底是什么。

---

## 2. 退一步：API 接口到底是什么

前几周小哲一直有个模糊的疑问：前端那些动感十足的按钮，点一下数据就悄悄进了 Supabase；可当业务变复杂——要并发支付、要定时推送、要处理敏感数据——直接让前端连数据库，安全吗？

答案是不安全，而这正引出了现代 Web 开发架构里至关重要的一环：**后端 API 接口**。

### 2.1 餐厅比喻：接口就是那个服务员

如果把整个应用想象成一家餐厅：

- **前端（客户端）** 是餐厅的菜单和点餐桌，客人在这里浏览菜品、提出需求。
- **数据库（Supabase 等）** 是餐厅的后厨仓库，存放着所有食材和账本。
- **后端 API 接口** 就是餐厅的服务员。客人不能直接冲进后厨拿食材（既混乱又危险），而是把「点单诉求」（HTTP Request）告诉服务员；服务员核对一遍（参数校验、权限鉴权），去后厨取对应内容，再把「做好的菜」（HTTP Response，通常是 JSON 数据）端回给客人。

通过 API 接口，我们实现了明确的**前后端分离**：前端只关心页面怎么渲染，后端只专注业务逻辑、数据处理与安全防护。回到小哲的盗刷事故——他犯的错，本质就是让客人绕过服务员，直接拿着后厨的门禁卡（API Key）冲进了后厨。

### 2.2 这周你会学到什么

围绕「用大模型辅助编写后端接口」这条主线，小哲这周要走通五件事：

<AnimatedFeatureCards :cards="[
  { icon: '🔌', gradient: 'linear-gradient(135deg,#6366f1,#8b5cf6)', tag: '概念', title: 'API 与前后端分离', description: '理解前后端通信的桥梁，以及 RESTful 设计规范这套行业默认的接口语言。' },
  { icon: '🏗️', gradient: 'linear-gradient(135deg,#0ea5e9,#22d3ee)', tag: '工程', title: '大模型搭建工程骨架', description: '用结构化 Prompt 让 AI 帮你搭出分层清晰的 Node.js + Express 项目，而不是一坨面条。' },
  { icon: '🔐', gradient: 'linear-gradient(135deg,#f43f5e,#fb7185)', tag: '安全', title: '安全封装 AI 接口', description: '密钥进环境变量、后端做代理、输入强校验，从根上堵住盗刷的口子。' },
  { icon: '📄', gradient: 'linear-gradient(135deg,#10b981,#34d399)', tag: '协作', title: '自动生成接口文档', description: '让 AI 根据代码逆向生成跨团队协作标配的 OpenAPI / Swagger 文档。' },
  { icon: '✅', gradient: 'linear-gradient(135deg,#f59e0b,#fbbf24)', tag: '质量', title: '测试与联调闭环', description: '用 AI 生成 Postman 测试集合与 Jest 单元测试，给代码质量兜底。' }
]" />

::: tip 视角的转变
学完这一周，你不再是被困在语法和标点里的「打字员」，而是上升成了**系统设计师**：你想清楚要什么，把上下文喂给 AI，再用专业的眼光审查它的产出。**大模型不怕需求复杂，最怕需求模糊。**
:::

---

## 3. 为什么 AI 调用必须放在后端

小哲冷静下来想：盗刷的根源，是密钥跟着前端代码一起发给了浏览器。那正确的做法是什么？

答案是 **后端代理（Backend Proxy）**：前端不再直接连 AI 服务，而是先把请求发给小哲自己的后端，由后端带着密钥去调 AI，再把结果转发回前端。密钥从头到尾只待在服务器上，永远不下发到浏览器。

用前面餐厅那个比喻：前端是点餐的客人，AI 服务是后厨，**密钥是进后厨的门禁卡**。你不会把门禁卡复印一份发给每个客人，而是让服务员（后端）拿着卡进出，客人只管点单和取餐。

| 对比维度 | 前端直连 AI（错误） | 后端代理 AI（正确） |
|---|---|---|
| 密钥位置 | 打包进浏览器，人人可见 | 只在服务器环境变量里 |
| 被盗刷风险 | 极高，密钥一抄就废 | 低，密钥不暴露 |
| 输入校验 | 前端校验可被绕过 | 后端强制校验，无法绕过 |
| 限流与配额 | 无法控制，用户随便刷 | 后端可加速率限制 |
| 错误处理 | 上游报错直接暴露给用户 | 后端统一兜底、脱敏 |
| 更换模型/服务商 | 要改前端、重新发版 | 只改后端，前端无感 |

<InfoCard icon="💡" variant="tip">
**这就是 BFF（Backend For Frontend）的雏形**

你的后端在这里扮演的角色，不只是「传话筒」。它是一道闸门：校验输入、保管密钥、控制频率、统一错误、隐藏上游细节。前端只认识你自己的接口（比如 `/api/ai/chat`），完全不需要知道背后用的是哪家大模型。哪天你想从一个模型换到另一个，前端一行都不用改。
</InfoCard>

---

## 4. 项目架构设计与初始化

方向明确了，但在动手让 AI 写代码之前，小哲得先想清楚工程长什么样。**一个结构清晰的项目骨架，是大模型能写出好代码的先决条件。**

### 4.1 常见的 API 工程结构

即使是用大模型生成代码，也绝不能把所有逻辑都塞进一个 `server.js` 文件里——那样写出来的就是没人愿意维护的「面条式代码」。一个易于维护的 Node.js 后端架构通常长这样：

```text
my-api-project/
├── .env                  # 敏感环境变量（如 API Keys、数据库连接串）
├── server.js             # 项目入口（服务器启动、全局中间件注册）
├── package.json          # 依赖管理文件
├── src/
│   ├── routes/           # 路由层：定义 URL 路径与请求方法
│   ├── controllers/      # 控制器层：处理请求参数，调用服务并返回响应
│   ├── services/         # 服务层：封装数据库交互和核心业务逻辑
│   └── middlewares/      # 中间件：登录鉴权、错误全局捕获
└── docs/                 # API 文档存放目录
```

这套分层不是炫技，而是「关注点分离」：路由只管「哪个 URL 对应哪个动作」，控制器只管「收参数、调服务、回响应」，服务层只管「真正干活（读写数据库、调外部 API）」。哪一层出问题，你立刻知道该去翻哪个文件夹。

### 4.2 借助 AI 完成工程初始化

与其手动 `npm init` 再一个个装依赖，不如直接把上面这套规范以 Prompt 的形式喂给大模型：

> 🗣️ **给大模型的提示词（Prompt 示例）：**
> 「帮我搭建一个 Node.js + Express 后端项目，要能连接 Supabase 数据库，结构按 routes / controllers / services / middlewares 分层，方便以后维护。密钥统一从环境变量读取，不要硬编码。」

运行 AI 返回的代码后，你就能在 `localhost:3000` 获得一个具备企业级雏形的后端应用了。

### 4.3 用 AI 写后端接口的完整工作流

小哲很快发现，「让 AI 写接口」不是甩一句话就完事，而是一条有节奏的流水线——有些环节 AI 能独立干，有些必须你亲自把关：

<WorkflowDiagram title="AI 辅助后端接口开发流程" :steps="[
  { name: '想清楚需求与数据结构', description: '先把要哪些表、每张表有哪些字段、有什么约束想透', type: 'human' },
  { name: '写结构化 Prompt', description: '把 Schema、约束、错误处理要求一并喂给 AI', type: 'human' },
  { name: 'AI 生成分层接口代码', description: '路由、控制器、服务层各司其职', type: 'ai' },
  { name: '人工审查代码', description: '密钥是否硬编码、校验是否到位、错误是否脱敏', type: 'human' },
  { name: 'AI 逆向生成接口文档', description: '根据代码产出 OpenAPI / Swagger', type: 'assist' },
  { name: 'AI 生成测试用例', description: 'Postman 集合 + Jest 单元测试', type: 'assist' },
  { name: '跑通联调', description: '本地测试 + 对照数据库验证', type: 'human' }
]" />

记住这条流水线的精髓和第 5 周接 Supabase 的 SOP 一脉相承：**先把数据结构想清楚，再让 AI 动代码。** 地基稳了，上面的代码改起来才顺。

---

## 5. 在后端安全封装 AI 接口

工程结构有了底，小哲开始把调用搬到后端。这一节有三件事：把密钥放进环境变量、写一个代理接口、对输入做校验。

### 5.1 密钥进环境变量，绝不进代码库

第一步，把密钥从代码里挪到 `.env` 文件，再通过环境变量读取。

```bash
# .env —— 这个文件绝对不能提交到 Git
OPENAI_API_KEY=sk-proj-你的真实密钥
AI_API_BASE=https://api.openai.com/v1
```

```bash
# .gitignore —— 务必把 .env 排除掉
.env
node_modules/
```

::: warning 密钥最容易栽在 Git 上
小哲差点犯第二个错：把 `.env` 一起 commit 了。**一旦密钥进过 Git 历史，即使后来删掉，历史记录里依然能翻出来。** 正确顺序永远是：先在 `.gitignore` 里写上 `.env`，再创建 `.env`。如果不小心已经提交过密钥，光删文件没用——必须立刻去服务商后台**吊销并重新生成**这把密钥。这正是上周配置版本控制时反复强调的纪律。
:::

### 5.2 写一个后端代理接口

接下来在 Express 里写一个 `/api/ai/chat` 接口。密钥从 `process.env` 读取，前端永远碰不到它。

```javascript
// src/routes/ai.js
const express = require('express')
const router = express.Router()

router.post('/api/ai/chat', async (req, res) => {
  const { message } = req.body

  // 永远不信任前端传来的数据，先做输入校验
  if (!message || typeof message !== 'string') {
    return res.status(400).json({ error: '消息不能为空' })
  }
  if (message.length > 2000) {
    return res.status(400).json({ error: '消息过长，请控制在 2000 字以内' })
  }

  try {
    const response = await fetch(`${process.env.AI_API_BASE}/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // 密钥只存在于服务器，不会随响应下发到浏览器
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages: [
          { role: 'system', content: '你是一个友善的中文助手，回答简洁准确。' },
          { role: 'user', content: message }
        ]
      })
    })

    if (!response.ok) {
      const detail = await response.text()
      console.error('AI 上游报错:', response.status, detail)
      // 关键：不要把上游的原始报错直接丢给前端
      return res.status(502).json({ error: 'AI 服务暂时不可用，请稍后再试' })
    }

    const data = await response.json()
    res.json({ reply: data.choices[0].message.content })
  } catch (err) {
    console.error('调用 AI 失败:', err)
    res.status(500).json({ error: '服务器内部错误' })
  }
})

module.exports = router
```

### 5.3 让大模型帮你写，但你要会审查

小哲发现，上面这段代码其实可以让 Coding Agent 替他生成——但前提是他得给足上下文，并且看得懂生成结果。一个好的提示词长这样：

> 🗣️ **给大模型的提示词：**
> 「帮我用 Express 写一个后端代理接口 `/api/ai/chat`，转发用户消息到大模型的 chat completions 接口。密钥从环境变量 `OPENAI_API_KEY` 读取，不要硬编码。要做输入校验（非空、长度上限），上游报错时不要把原始错误暴露给前端，统一返回友好提示。」

拿到代码后，小哲会逐项检查这几点（这正是这门课第 1 周立下的规矩——**AI 输出必须验证**）：

- 密钥是不是从 `process.env` 读的，有没有被写死在代码里？
- 有没有对 `message` 做非空和长度校验？
- 上游 4xx/5xx 报错时，会不会把原始错误泄漏给前端？
- `try/catch` 有没有兜住网络异常？

第一条尤其要命——审查时小哲发现 AI 偶尔会图省事把密钥写进代码，他必须一眼揪出来改掉：

<DiffViewer title="审查 AI 代码：把硬编码密钥改成环境变量" diff="@@ -1,5 +1,5 @@
   const response = await fetch(url, {
     headers: {
-      Authorization: 'Bearer sk-proj-abc123真实密钥'
+      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`
     }
   })" />

---

## 6. 核心实战：用高质量 Prompt 引导 AI 写接口代码

封装好 AI 代理只是开胃菜。这周的核心，是让大模型帮小哲写**业务接口**——比如他汉堡店应用里「新增菜单项」这样的 CRUD 接口。大模型写出的代码常常存在「逻辑漏洞」或「表面敷衍」，根因几乎都是开发者给的上下文不足。

### 6.1 赋予大模型完整上下文

在请求 AI 写接口之前，一定要提供**数据库字段定义（Schema）**和**具体的约束条件**。同样一句「写个新增菜单接口」，给不给上下文，产出天差地别：

<PromptPlayground
  title="模糊 Prompt vs 结构化 Prompt"
  leftLabel="模糊 Prompt"
  rightLabel="结构化 Prompt（带 Schema 与约束）"
  leftPrompt="帮我写一个新增菜单的接口。"
  rightPrompt="帮我写一个新增菜单的接口。菜单字段：商品名 name（必填，文本）、价格 price_cents（必填，整数存分，不能为负）、分类 category（汉堡 / 小食 / 饮料）、是否上架 available（布尔）。用 Express + Supabase，按 routes / controllers / services 分层。校验不通过返回 400 并给出错误原因，数据库出错时不要把原始错误透传给前端。"
  leftOutput="一个把校验、数据库操作、响应全堆在一个函数里的面条式接口，价格能传负数，错误直接 500 抛栈。"
  rightOutput="分层清晰：路由 → 控制器（校验参数）→ 服务层（调 Supabase）。价格负数被拦截，数据库错误被捕获并脱敏。"
  :analysis="[
    { dimension: '结构清晰度', left: 25, right: 90 },
    { dimension: '校验完整度', left: 20, right: 88 },
    { dimension: '可直接上线', left: 15, right: 85 }
  ]" />

> 🗣️ **高质量提示词（Prompt）模板：**
> 「帮我写一个新增菜单的接口，菜单有商品名、价格、分类（汉堡、小食、饮料）、是否上架这几个信息。商品名和价格必须填，价格不能是负数。用户输入不对的时候要提示错误。」

### 6.2 审查大模型生成的代码

给足上下文后，大模型生成的代码通常会像下面这样清晰地拆分职责，把数据库交互收敛在服务层里：

```javascript
// src/services/menuService.js
const { createClient } = require('@supabase/supabase-js')
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY)

exports.createMenuItem = async (menuData) => {
  // 调用 Supabase SDK 将数据推入表内
  const { data, error } = await supabase
    .from('menu_items')
    .insert([menuData])
    .select()

  if (error) throw new Error(`数据库插入失败: ${error.message}`)
  return data[0]
}
```

控制器层则负责把守「参数校验」这道关，校验通过才调服务层：

```javascript
// src/controllers/menuController.js
const menuService = require('../services/menuService')

exports.createMenuItem = async (req, res) => {
  const { name, price_cents, category, available } = req.body

  // 永远不信任用户输入：必填项、类型、取值范围都要查
  if (!name || typeof name !== 'string') {
    return res.status(400).json({ error: '商品名必填且必须是文本' })
  }
  if (!Number.isInteger(price_cents) || price_cents < 0) {
    return res.status(400).json({ error: '价格必须是非负整数（以分为单位）' })
  }

  try {
    const item = await menuService.createMenuItem({ name, price_cents, category, available })
    res.status(201).json(item) // 201 Created：资源创建成功
  } catch (err) {
    console.error('新增菜单失败:', err)
    res.status(500).json({ error: '服务器内部错误' }) // 不透传原始错误
  }
}
```

你可以发现，这样生成的代码不仅结构合理，还把 Supabase 初始化、错误捕获、异常处理都考虑在内——这和简单要求「写个新增接口」得到的**面条式代码（Spaghetti Code）**有着天壤之别。

<InfoCard icon="🧭" variant="tip">
**为什么分层这么重要？**

面条式代码把校验、业务、数据库、响应全揉在一个函数里，短期看「能跑」，但只要需求一变（比如要加缓存、换数据库、加权限），你就得在一团乱麻里动刀，改一处崩三处。分层之后，每一层职责单一、可独立测试、可独立替换。让 AI 写代码时**主动要求分层**，是把「能跑的代码」变成「能维护的代码」的关键一步。
</InfoCard>

---

## 7. 错误处理：AI 接口比你想的更容易出错

普通的数据库接口，参数对了基本就能成功。但调用大模型 API 完全不同：它走外网、依赖第三方、有配额和限流、响应还可能很慢。**把「成功」当默认情况来写，是新手最常踩的坑。**

小哲整理了一张表，把 AI 接口最常见的失败情形和应对方式列清楚：

| 错误情形 | 典型状态码 | 原因 | 后端该怎么处理 |
|---|---|---|---|
| 触发限流 | 429 | 请求太频繁或超出额度 | 提示稍后重试，可做指数退避重试 |
| 账户欠费 | 401 / 429 | 余额不足、密钥失效 | 记录告警，前端只提示「服务不可用」 |
| 内容被拒 | 400 | 命中内容安全策略 | 提示用户换个说法 |
| 响应超时 | 无 | 模型生成太慢、网络抖动 | 设超时时间，超时给兜底提示 |
| 上游故障 | 500 / 503 | AI 服务方自己挂了 | 降级或重试，不要把栈信息透出 |

下面给代理接口加上超时控制和针对限流的退避重试，让它扛得住真实流量：

```javascript
// 给请求加超时：避免模型卡住时把后端连接一直占着
async function callAIWithTimeout(body, timeoutMs = 30000) {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), timeoutMs)
  try {
    const response = await fetch(`${process.env.AI_API_BASE}/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`
      },
      body: JSON.stringify(body),
      signal: controller.signal
    })
    return response
  } finally {
    clearTimeout(timer)
  }
}

router.post('/api/ai/chat', async (req, res) => {
  const { message } = req.body
  if (!message?.trim()) {
    return res.status(400).json({ error: '消息不能为空' })
  }

  const body = {
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: message }]
  }

  try {
    let response = await callAIWithTimeout(body)

    // 遇到 429 限流，等待后重试一次
    if (response.status === 429) {
      await new Promise((r) => setTimeout(r, 1500))
      response = await callAIWithTimeout(body)
    }

    if (!response.ok) {
      console.error('AI 上游报错:', response.status)
      return res.status(502).json({ error: 'AI 服务繁忙，请稍后再试' })
    }

    const data = await response.json()
    res.json({ reply: data.choices[0].message.content })
  } catch (err) {
    // AbortError 就是超时
    if (err.name === 'AbortError') {
      return res.status(504).json({ error: 'AI 响应超时，请重试' })
    }
    console.error('调用 AI 失败:', err)
    res.status(500).json({ error: '服务器内部错误' })
  }
})
```

::: tip 错误信息要分两层
后端的日志里可以记详细的原始错误（状态码、上游返回体），方便你排查；但返回给前端的，永远是一句脱敏后的友好提示。**把上游的报错原样透传给用户，既不友好，也可能泄漏接口结构和密钥相关信息。**
:::

---

## 8. 流式响应：让用户不用干等

接口能跑通、扛得住了，小哲又发现一个体验问题：AI 生成一段长回答要好几秒，这期间页面一片空白，用户以为卡死了。

你肯定见过 ChatGPT 那种「一个字一个字蹦出来」的效果——这就是 **流式响应（Streaming）**。模型边生成边返回，前端边收边显示，用户几乎立刻看到第一个字。

<AiChat botName="汉堡店智能助手" status="流式响应中" :showInput="false" :initialMessages="[
  { role: 'user', content: '招牌牛肉汉堡里有什么？' },
  { role: 'assistant', content: '我们的招牌牛肉汉堡用的是 100% 现煎牛肉饼，配生菜、番茄、芝士和秘制酱料……', meta: '流式输出：文字一段段蹦出来，无需干等' }
]" />

实现方式是 **SSE（Server-Sent Events）**：调用上游时带上 `stream: true`，后端再把这股数据流一段段转发给前端。

```javascript
// src/routes/ai.js —— 流式版本
router.post('/api/ai/chat/stream', async (req, res) => {
  const { message } = req.body
  if (!message?.trim()) {
    return res.status(400).json({ error: '消息不能为空' })
  }

  // 设置 SSE 响应头
  res.setHeader('Content-Type', 'text/event-stream')
  res.setHeader('Cache-Control', 'no-cache')
  res.setHeader('Connection', 'keep-alive')

  try {
    const upstream = await fetch(`${process.env.AI_API_BASE}/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages: [{ role: 'user', content: message }],
        stream: true // 开启流式输出
      })
    })

    // 把上游返回的数据流一段段转发给前端
    for await (const chunk of upstream.body) {
      res.write(chunk)
    }
    res.end()
  } catch (err) {
    console.error('流式调用失败:', err)
    // 流已经开始就不能再改状态码，用事件告知前端出错
    res.write(`data: ${JSON.stringify({ error: 'AI 服务中断' })}\n\n`)
    res.end()
  }
})
```

前端用浏览器原生的 `fetch` + 读取流就能消费它，逐段把文字追加到界面上：

```javascript
// 前端：逐段读取并显示
const res = await fetch('/api/ai/chat/stream', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: userInput })
})

const reader = res.body.getReader()
const decoder = new TextDecoder()

while (true) {
  const { done, value } = await reader.read()
  if (done) break
  // 解析 SSE 数据块，把增量文字追加到聊天框
  const text = decoder.decode(value)
  appendToChat(text)
}
```

<InfoCard icon="⚡" variant="tip">
**流式不是炫技，是省钱又省心**

除了体验更好，流式还有两个实在的好处：用户能随时点「停止」，避免为不想要的长回答白白付费；服务器也不必把整段回答攒在内存里等生成完，而是来一段转一段，内存占用更低。对要上线的真实产品来说，流式几乎是聊天类功能的标配。

顺带一提，第 5 周讲的 Supabase Edge Function，本质上也能扮演这个「把密钥藏好的流式代理」角色——如果你不想自建 Node 后端，那条路同样走得通。
</InfoCard>

---

## 9. 解放双手：自动生成接口文档

接口写完了，但对开发团队而言，**没有文档的 API 就是一个盲盒**：前端工程师无法猜测你要传什么参数，也不能预测会返回什么结构。业界最通用的 API 描述规范是 **OpenAPI（此前也称 Swagger）**。

过去，手写 YAML 或 JSON 格式的 Swagger 文档极其痛苦且容易出错。现在，这恰恰是大模型最擅长的领域。你可以直接选中刚写好的 `routes` 和 `controllers` 代码，丢给大模型：

> 🗣️ **生成文档的提示词：**
> 「帮我根据上面的代码生成一份 OpenAPI 接口文档，要写清楚每个参数是什么意思、返回什么数据，方便前端同事对接。」

你甚至可以要求 AI 补全字段说明（Description）和 Mock 数据（如 `price_cents: 1200` 代表 12 美元），极大降低沟通成本。AI 产出的文档片段大致长这样：

```yaml
# docs/openapi.yaml（节选）
paths:
  /api/menu:
    post:
      summary: 新增一个菜单项
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [name, price_cents]
              properties:
                name:
                  type: string
                  description: 商品名
                  example: 招牌牛肉汉堡
                price_cents:
                  type: integer
                  description: 价格，以分为单位，避免浮点误差
                  example: 1200
                category:
                  type: string
                  enum: [burger, side, drink]
                available:
                  type: boolean
                  example: true
      responses:
        '201':
          description: 创建成功，返回新建的菜单项
        '400':
          description: 参数校验失败
```

把这份 YAML 接入 Swagger UI，团队就能得到一个可在线点击调试的接口面板，前端再也不用追着你问「这个字段到底传啥」。

---

## 10. 保驾护航：生成测试代码与 Postman 集合

代码写好、文档出炉，还差最后一步：验证代码到底能不能跑通。

### 10.1 生成 Postman / Apifox 测试配置

接口开发中，我们通常用 Postman 这类可视化工具模拟前端发 HTTP 请求。不借助 AI 的话，你得手动填 URL、逐个加 Header、拼 JSON 请求体。现在只需一句指令：

> 🗣️ **给大模型的提示词：**
> 「帮我把这份接口文档转成 Postman 可以导入的格式，要包含正常请求和错误请求的例子。」

拿到 JSON 文本后，保存为 `menu_api.json` 拖进 Postman，你瞬间就获得一套开箱即用的测试点击面板，正常请求和异常请求（比如价格传负数）都备好了。

### 10.2 编写自动化单元测试

如果你追求更严谨的工程质量，可以让大模型用 `Jest` 等测试框架编写单元测试，对核心业务逻辑做边界测试——比如传入负数价格时，校验是否真的拦得住：

```javascript
// tests/menuController.test.js
const request = require('supertest')
const app = require('../src/app')

describe('POST /api/menu', () => {
  it('合法数据应返回 201 并带上新建项', async () => {
    const res = await request(app).post('/api/menu').send({
      name: '招牌牛肉汉堡',
      price_cents: 1200,
      category: 'burger'
    })
    expect(res.status).toBe(201)
    expect(res.body.name).toBe('招牌牛肉汉堡')
  })

  it('价格为负数应被拦截，返回 400', async () => {
    const res = await request(app).post('/api/menu').send({
      name: '问题汉堡',
      price_cents: -500
    })
    expect(res.status).toBe(400)
  })

  it('缺少必填的 name 应返回 400', async () => {
    const res = await request(app).post('/api/menu').send({ price_cents: 1200 })
    expect(res.status).toBe(400)
  })
})
```

> 🗣️ **给大模型的提示词：**
> 「用 Jest + supertest 给这个新增菜单接口写单元测试，覆盖：合法数据成功、价格为负被拒、缺必填项被拒这三种情况。」

::: tip 测试是 AI 代码的「第二双眼睛」
AI 写的接口看起来对，不代表真的对。让 AI 顺手把测试也写了，再亲自跑一遍 `npm test`——这一步能在上线前抓出大量「看起来没问题」的边界 bug。把测试当成你审查 AI 代码的自动化助手。
:::

---

## 11. 后端接口必知的最佳实践

即使有 AI 协助，作为整个系统的「把关人」，你依然得了解并审核这些核心准则——AI 不一定每次都遵守，你得看得出它哪里没做到位：

1. **RESTful 规范的路径命名**
   - 好的设计：`GET /api/users`（获取用户列表）、`POST /api/users`（创建用户）。URL 应该代表「资源」的名词。
   - 错误的设计：`POST /api/getUser` 或 `POST /api/createUser`。动作（增删改查）应该交给 HTTP Method（GET / POST / PUT / DELETE）来表达，而不是塞进 URL 里。
2. **规范的 HTTP 状态码**
   - `200 / 201`：请求成功 / 资源创建成功。
   - `400`：Bad Request，前端传参格式错误、少传了必填项。
   - `401 / 403`：Unauthorized / Forbidden，用户未登录或无权操作。
   - `404`：Not Found，资源不存在。
   - `500`：Server Error，后端代码报错或数据库挂了。**绝对要避免把报错调用栈直接暴露给前端**（会有安全隐患）。
3. **永远不信任用户的输入**：前端的输入可能是伪造的，所有核心参数校验**必须在后端接口中再做一次**。前端校验只是为了体验（提前提示），后端校验才是真正的防线。

小哲把这三条钉在了脑子里。下面这张卡片是他给自己写的「接口验收三连问」：

<AnimatedFeatureCards :cards="[
  { icon: '🔤', gradient: 'linear-gradient(135deg,#6366f1,#818cf8)', tag: 'RESTful', title: 'URL 是名词，动作交给 Method', description: '看到 /api/getUser 这种动词路径就该警觉，改成 GET /api/users 才规范。' },
  { icon: '🚦', gradient: 'linear-gradient(135deg,#0ea5e9,#38bdf8)', tag: '状态码', title: '用对状态码说话', description: '成功 200/201，参数错 400，没权限 401/403，资源不存在 404，服务端崩 500。' },
  { icon: '🛡️', gradient: 'linear-gradient(135deg,#f43f5e,#fb7185)', tag: '校验', title: '永远不信任用户输入', description: '前端能绕过，后端校验才是防线。必填、类型、取值范围一个都不能少。' },
  { icon: '🧱', gradient: 'linear-gradient(135deg,#10b981,#34d399)', tag: '分层', title: '拒绝面条式代码', description: '路由 / 控制器 / 服务层各司其职，让接口可维护、可测试、可替换。' }
]" />

---

## 12. 上线前的安全清单

接口写完了，但小哲学乖了——上线前他要先把「密钥和调用」这条线上的风险盘一遍。下面这张风险矩阵，就是他这周用真金白银（4200 块账单）换来的清单：

<RiskMatrix title="接入 AI 接口的典型风险" :risks="[
  { name: '密钥泄漏', description: '密钥写进前端或提交进 Git，被人扒走', icon: '🔑', color: '#ef4444', probability: 3, impact: 3 },
  { name: 'API 被盗刷', description: '密钥暴露后被脚本疯狂调用，账单爆炸', icon: '💸', color: '#ef4444', probability: 2, impact: 3 },
  { name: '没有限流', description: '单个用户无限制调用，成本和负载失控', icon: '🚦', color: '#f59e0b', probability: 3, impact: 2 },
  { name: '错误信息暴露', description: '上游原始报错透传给前端，泄漏接口细节', icon: '🪟', color: '#f59e0b', probability: 2, impact: 2 },
  { name: '提示词注入', description: '用户输入未校验，试图操纵模型行为', icon: '🧨', color: '#8b5cf6', probability: 2, impact: 2 },
  { name: '调用超时未处理', description: '模型卡住拖垮后端，连接被一直占用', icon: '⏳', color: '#f59e0b', probability: 2, impact: 2 }
]" />

针对这些风险，小哲给项目立了一份上线前必查的清单：

<SummaryCard title="AI 接口上线前自检" :sections="[
  { number: '1', title: '密钥安全', items: ['密钥只在后端环境变量里，前端代码搜不到 sk-', '.env 已写进 .gitignore，没进过 Git 历史', '一旦怀疑泄漏，立刻去后台吊销重置'] },
  { number: '2', title: '调用防护', items: ['对每个用户或 IP 做速率限制', '输入做非空、长度、类型校验', '关注用量看板，设好预算告警'] },
  { number: '3', title: '规范与质量', items: ['路径遵循 RESTful，状态码用对', '接口文档（OpenAPI）与测试用例齐全', '核心逻辑跑过 Jest，边界情况覆盖到'] },
  { number: '4', title: '稳定与体验', items: ['请求设超时，限流做退避重试', '上游报错统一脱敏，只回友好提示', '长回答用流式输出，别让用户干等'] }
]" />

::: warning 速率限制不能省
小哲补的最后一块拼图是**速率限制**：哪怕密钥藏好了，如果不限制单个用户的调用频率，一个人写个脚本照样能把你的额度刷光。给 `/api/ai/chat` 加上「每用户每分钟 N 次」的限制（比如用 `express-rate-limit`），是上线前的硬性要求，不是可选项。
:::

---

## 13. 小哲这周的转变

> 小哲回看这一周：他从「在前端硬塞一句 fetch、三天被刷掉 4200 块」起步，最后做出了一套分层清晰、密钥锁在后端、带文档和测试、还能流式输出的 AI 接口。
>
> 他在笔记里写下一句话：**「我不再是那个被困在语法里的打字员。把数据结构想清楚、把上下文喂给 AI、再用专业的眼光审查它的产出——这才是这周真正学到的东西。代码可以让 AI 写，但‘把关人’这个角色，永远是我自己。」**

而真正让他安心的，是那条贯穿全周的安全主线：密钥只能待在后端环境变量里，永不下发浏览器；所有用户输入都当成不可信，后端再校验一遍；上游报错统一脱敏，绝不透传。这套「先完成，再完美」的节奏，加上对密钥和输入的敬畏，就是这周最值钱的收获。

---

## 本周回顾

<ProgressTracker title="第 6 周学习进度" :items="[
  { title: '看懂了密钥泄漏的代价', description: '前端能看到的一切，用户都能看到', done: false },
  { title: '理解了 API 与前后端分离', description: '接口是服务员，密钥是后厨门禁卡', done: false },
  { title: '会用分层结构搭后端', description: 'routes / controllers / services / middlewares', done: false },
  { title: '会用 Prompt 引导 AI 写接口', description: '给足上下文与 Schema，再逐项审查产出', done: false },
  { title: '掌握了错误处理与流式响应', description: '超时、退避重试、SSE 流式输出', done: false },
  { title: '会让 AI 出文档与测试', description: 'OpenAPI 文档 + Postman 集合 + Jest 单测', done: false },
  { title: '建立了上线前的安全意识', description: '密钥、限流、校验、用量告警一个不落', done: false }
]" />

**自测问题：**

1. 为什么 AI API 的调用绝对不能放在前端？密钥即使做了混淆打包，问题解决了吗？
2. 用餐厅比喻解释一下「前后端分离」：前端、后端接口、数据库分别对应餐厅里的什么角色？
3. 同样是「写个新增菜单接口」，给 AI 一句模糊指令和一段带 Schema、约束的结构化 Prompt，产出会有什么区别？为什么分层的代码比面条式代码值钱？
4. 后端代理接口至少要处理哪几类错误？为什么不能把上游的原始报错直接返回给前端？
5. RESTful 规范里，为什么 `POST /api/getUser` 是错误设计？正确该怎么写？
6. 流式响应（SSE）相比一次性返回，除了体验更好，还带来了哪些工程上的好处？

---

## 下周预告

AI 功能接进来了，应用越来越像个真产品。下周小哲要解决两个真实世界的问题：**怎么收钱，怎么让全世界访问到它。** 第 7 周我们讲 **支付与部署**——用 Stripe 给应用接上付费功能（又一次和密钥、Webhook 安全打交道），再用 Zeabur 把整套全栈应用部署到公网。从「本地能跑」到「用户能付费使用」，就差这一周。
