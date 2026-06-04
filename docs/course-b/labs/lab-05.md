# Lab 05：Supabase 数据库、认证、RLS 与存储总览

<ChapterIntroduction duration="3-4 小时" output="支持注册/登录和数据持久化的 Supabase 应用 + RLS 权限测试 + Storage 上传证据" prerequisite="完成 Lab 04；已有可运行前端项目；能创建 Supabase 项目；理解基础表格和字段" :tags="['Supabase', 'PostgreSQL', 'Auth', 'RLS', 'Storage', 'CRUD']">

- 用 Supabase 让应用真正记住数据
- 为应用加入基础用户系统和行级安全
- 体验 Storage 上传，理解 Supabase 后端模块的职责边界

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '建项目', description: '创建 Supabase 项目并熟悉控制台' },
  { title: '设计表', description: '创建核心业务表和字段' },
  { title: '做 CRUD', description: '从前端增删改查真实数据' },
  { title: '接 Auth', description: '实现注册、登录和退出' },
  { title: '开 RLS', description: '测试用户只能看自己的数据' },
  { title: '试 Storage', description: '上传头像或业务附件' }
]" />

## 实验目标

把前几周的前端项目升级为有后端地基的应用。实验结束时，你的应用应能注册/登录，能把核心业务数据写入 Supabase，能用 RLS 做基本隔离，并能完成一次文件上传。

## 实验任务

围绕你的产品主路径接入 Supabase。不要使用已经删除或不存在的课程根目录示例；可以在自己的学生项目中实现，也可以自建一个最小 Vite/Next.js 项目。

必须完成：

- 1 张核心业务表
- 创建、读取、更新、删除至少 3 类操作，其中创建和读取必须从前端触发
- Supabase Auth 登录或注册
- RLS 开启和至少 2 条策略
- Storage bucket 和一次上传
- 数据库、权限、上传的截图证据

## 操作步骤

### 1. 创建 Supabase 项目并熟悉控制台

创建 Supabase 项目后，浏览以下区域并截图：

- Table Editor
- SQL Editor
- Authentication
- Storage
- API settings

记录 anon key 和 service_role key 的区别。真实 key 不得提交到仓库。

### 2. 设计核心业务表

选择一个和产品主路径直接相关的数据对象，例如 `plans`、`resumes`、`orders`、`questions`、`assets`。

至少包含：

- `id`
- `user_id`
- `title` 或业务名称字段
- 1-3 个业务字段
- `created_at`
- `updated_at`

保存 schema 表或 SQL。

### 3. 从前端实现基础 CRUD

配置环境变量：

```bash
VITE_SUPABASE_URL=replace_me
VITE_SUPABASE_ANON_KEY=replace_me
```

根据项目技术栈调整前缀。实现：

- 新建记录
- 读取列表
- 更新状态或标题
- 删除记录

至少创建和读取必须由页面触发，不能只在 Dashboard 中操作。

### 4. 接入 Auth

选择邮箱密码、邮箱验证码或第三方登录。页面需要显示：

- 登录状态
- 当前用户邮箱或 ID
- 退出按钮
- 未登录时的提示或跳转

保存登录成功截图。

### 5. 开启 RLS 并验证隔离

为核心表开启 RLS。至少实现：

- 登录用户只能读取自己的记录
- 登录用户只能插入自己的记录

进阶可补充 update 和 delete 策略。

使用两个账号测试：

| 测试 | 预期 |
|---|---|
| A 创建记录 | 成功 |
| B 查看 A 的记录 | 看不到 |
| 未登录访问数据 | 被拒绝或跳转登录 |

保存测试截图或 API 日志。

### 6. 创建 Storage bucket 并上传文件

实现一个最小上传场景：

- 用户头像
- 简历 PDF
- 产品素材图
- 课程资料附件

记录 bucket 名称、文件路径、公开 URL 或 signed URL 选择理由。保存上传页面和 Storage 控制台截图。

## 提交要求

- Supabase 控制台关键区域截图
- schema 表或 SQL
- CRUD 页面截图和数据库记录截图
- 登录成功截图
- RLS 策略截图或 SQL
- 两个账号或未登录权限测试记录
- Storage bucket 和上传成功截图
- `.env.example`，不得包含真实密钥
- `git diff` 或 PR diff
- 运行日志或 API 日志

## 验收标准

- 数据对象和产品主路径相关
- 前端能触发真实数据写入和读取
- 用户可以登录和退出
- RLS 已开启，并有权限隔离证据
- Storage 上传成功，且说明了公开或签名访问的选择
- 仓库中没有真实 secret、service_role key 或私密连接串

## 常见问题

**本周要把 Supabase 所有功能都做完整吗？**
不需要。本周是数据库、Auth、RLS、Storage 的全链路总览，重点是每块都跑通最小证据。

**RLS 只写 select 和 insert 可以吗？**
可以达到基础要求。若你的页面已经支持更新和删除，建议补齐 update 和 delete 策略。

**Storage 可以用 public bucket 吗？**
可以，但必须说明为什么公开不会泄露隐私。头像可公开，私人文件通常不应公开。

## 评分标准

| 维度 | 分值 | 说明 |
|---|---:|---|
| 数据库与 CRUD | 25 | schema 是否合理，前端是否能读写真实数据 |
| Auth 集成 | 20 | 登录、退出和用户状态是否可用 |
| RLS 验证 | 25 | 是否开启策略并完成隔离测试 |
| Storage 实现 | 15 | 文件上传是否可用，权限说明是否合理 |
| 安全与证据 | 15 | 密钥、截图、日志、diff 是否完整 |
