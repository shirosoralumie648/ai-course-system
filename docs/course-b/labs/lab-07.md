# Lab 07：Stripe 支付与 Zeabur 部署上线

<ChapterIntroduction duration="3-4 小时" output="Stripe Checkout + Webhook 测试证据 + Zeabur 公网部署链接 + 部署踩坑复盘" prerequisite="完成 Lab 06；本地能启动全栈应用；会用 Git 基础命令；了解环境变量" :tags="['Stripe', 'Checkout', 'Webhook', 'Zeabur', '部署上线', '环境变量']">

- 跑通一条测试支付链路，理解定价、确认、记账的边界
- 用 webhook 或后端确认更新订单状态
- 把全栈应用部署到 Zeabur 并完成线上走查

</ChapterIntroduction>

<StepBar :active="0" :items="[
  { title: '定义商品', description: '确定价格、权益和订单状态' },
  { title: '接 Checkout', description: '后端创建 Stripe Session' },
  { title: '配 Webhook', description: '验证支付成功并更新记录' },
  { title: '本地测试', description: '保存 Stripe 与数据库日志' },
  { title: '部署 Zeabur', description: '配置端口和环境变量' },
  { title: '线上验证', description: '提交公网链接和复盘' }
]" />

## 实验目标

让本地项目第一次具备“能收费”和“能被别人访问”的产品属性。实验结束时，你应有一条 Stripe test mode 或可信模拟支付链路，以及一个部署在 Zeabur 的公网应用。

## 实验任务

为你的产品加入一个最小商业化流程，并部署上线。优先使用 Stripe test mode。若账号条件暂时无法使用 Stripe，可以使用教师认可的模拟支付，但必须有后端确认、订单状态变化和日志。

必须完成：

- 一个付费项或订阅项
- 后端创建 Checkout Session 或模拟支付订单
- webhook 或后端确认接口
- 订单状态记录
- Zeabur 部署链接
- 本地和线上验证证据

## 操作步骤

### 1. 定义付费项和订单状态

写清楚：

- 用户为什么付费
- 测试价格
- 支付成功后解锁什么
- 订单表字段
- 状态流转：`pending`、`paid`、`failed`、`canceled`

至少在数据库或后端日志中记录一次状态变化。

### 2. 接入 Stripe Checkout

前端点击购买按钮后，请求你的后端接口。后端负责：

- 读取 Stripe secret key
- 创建 Checkout Session
- 设置 success URL 和 cancel URL
- 返回跳转 URL 或 session id

前端不得持有 Stripe secret key。

### 3. 配置 webhook 或确认接口

Stripe test mode 应保存：

- Stripe Dashboard 测试事件截图
- webhook endpoint 日志
- 订单状态从 `pending` 到 `paid` 的数据库截图

模拟支付应保存：

- 后端确认接口日志
- 订单状态变化截图
- 失败或取消路径截图

### 4. 本地完整走查

完成一次本地走查：

1. 登录或进入产品
2. 点击购买
3. 进入 Stripe test checkout 或模拟支付页
4. 完成支付或确认
5. webhook 或确认接口收到事件
6. 数据库订单状态更新
7. 前端显示权益或支付结果

保存截图和日志。

### 5. 部署到 Zeabur

把项目推送到 GitHub，并在 Zeabur 中创建服务。配置：

- 构建命令
- 启动命令
- 端口
- Supabase 环境变量
- Stripe 环境变量
- AI API 环境变量
- webhook secret

提交环境变量清单，只写变量名和用途，不写真实值。

### 6. 线上验证和复盘

打开 Zeabur 公网链接，至少验证：

- 页面可访问
- 登录或核心页面可用
- 数据库读取正常
- 支付入口可见
- webhook URL 或回调地址已改成线上地址

写 200-400 字部署踩坑复盘：端口、环境变量、回调地址、构建失败、日志定位中你遇到了什么。

## 提交要求

- Stripe test mode 或模拟支付入口截图
- Checkout Session 或订单创建日志
- webhook 或确认接口日志
- 订单状态数据库截图
- Zeabur 部署成功截图
- 公网部署链接
- 环境变量清单，禁止真实值
- 线上主路径截图
- `git diff` 或 PR diff
- 部署踩坑复盘

## 验收标准

- 支付入口不是纯前端假按钮，有后端创建或确认
- webhook 或确认接口有日志
- 订单状态能在数据库或后台记录中看到
- Zeabur 公网链接可以访问
- 线上环境变量没有暴露真实 secret
- 本地和线上差异有记录，尤其是端口、环境变量和回调地址

## 常见问题

**Stripe 账号无法使用怎么办？**
使用模拟支付方案，但必须保留后端确认、订单状态变化和失败路径。只展示一个“支付成功”页面不合格。

**为什么一定要 webhook？**
支付是否成功不能只相信前端跳转。真实支付系统必须由 Stripe 事件或可信后端确认来记账。

**部署失败怎么办？**
提交失败日志、定位过程和本地可运行证据可以获得部分分数，但公网链接是本实验核心验收项。

## 评分标准

| 维度 | 分值 | 说明 |
|---|---:|---|
| 支付链路 | 30 | Checkout、webhook/确认和状态变化是否完整 |
| 密钥与边界 | 15 | Stripe secret、price、webhook secret 是否放在后端 |
| Zeabur 部署 | 25 | 公网链接、构建日志和环境变量是否正确 |
| 线上走查 | 15 | 主路径是否在线可用 |
| 复盘证据 | 15 | 截图、日志、diff 和踩坑记录是否完整 |
