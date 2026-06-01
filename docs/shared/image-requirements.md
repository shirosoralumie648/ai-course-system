# 图片需求清单

> 目标：把现有课程从“长文档 + 代码块”补成更容易讲授、阅读和复盘的图文材料。若某页暂时没有可用截图或实拍图，按本清单补采或补生成。

## 统一规范

| 项目 | 要求 |
| --- | --- |
| 截图尺寸 | 优先 16:9，宽度不低于 1600px；移动端或小程序截图可用 9:16 |
| 文件位置 | 放在对应周次目录，例如 `course-a/week-11-images/` |
| 文件命名 | 使用语义化英文，例如 `spec-workflow-overview.png`，避免继续新增 `image99.png` |
| 标注方式 | 关键按钮、路径、状态变化用红色箭头或编号标注 |
| 页面插入 | 每个长篇教程至少补 1 张总览图，核心操作步骤每 3-5 个步骤补 1 张截图 |

## 优先补图

| 优先级 | 页面 | 建议插入位置 | 图片内容 | 建议文件名 |
| --- | --- | --- | --- | --- |
| P0 | `course-b/week-03.md` | `4.1 认识 NanoBanana` 的介绍段落后 | 真实的 NanoBanana / 图像生成工具首次出图界面，包含输入提示词、生成结果、下载或保存按钮 | `week-03-images/nanobanana-first-result.png` |
| P0 | `course-b/week-12.md` | `11.5 用 HBuilderX 创建项目骨架` 后 | HBuilderX 新建 uni-app 项目的四步截图：选择模板、填写项目名、创建完成、项目结构 | `week-12-images/hbuilderx-create-project.png` |
| P0 | `course-b/week-12.md` | `12.3 在 HBuilderX 和微信开发者工具中查看效果` 后 | HBuilderX 运行到微信开发者工具后的模拟器界面，能看到贪吃蛇首页或游戏页 | `week-12-images/wechat-devtools-preview.png` |
| P0 | `course-b/week-13.md` | `2. 云开发的核心概念` 后 | 小程序端、云函数、云数据库、微信支付之间的数据流示意图 | `week-13-images/cloud-dev-architecture.png` |
| P0 | `course-a/week-13.md` | `什么是 Spec Coding？` 后 | Vibe Coding 与 Spec Coding 的流程对比图：即兴 prompt → 返工，对比 规范 → 计划 → 实现 → 验收 | `week-13-images/spec-vs-vibe-flow.png` |

## Course A 缺图页

| 页面 | 建议图片内容 | 放置位置 |
| --- | --- | --- |
| `course-a/week-03.md` | Claude Code 终端界面截图，标注输入区、计划、文件改动、执行结果 | 第一次介绍 Claude Code 时 |
| `course-a/week-08.md` | 完整项目从需求、原型、代码到部署的端到端路线图 | 章节导语后 |
| `course-a/week-09.md` | Workflow 节点图：输入、路由、执行、验证、输出 | Workflow 概念介绍后 |
| `course-a/week-10.md` | Skill 的目录结构示意图：`SKILL.md`、`scripts/`、`templates/`、`examples/` | 讲 Skill 结构前 |
| `course-a/week-11.md` | MCP 架构图：Claude Code、MCP Server、本地工具、远程 API 的关系 | MCP 概念介绍后 |
| `course-a/week-12.md` | Superpowers 工作流图：brainstorming、planning、TDD、debugging、verification | 技能体系介绍后 |
| `course-a/week-14.md` | 长运行任务监控图：任务队列、日志、检查点、恢复流程 | 任务生命周期介绍后 |
| `course-a/week-15.md` | Agent SDK 调用链路图：主 Agent、工具、子任务、结果汇总 | SDK 概念介绍后 |
| `course-a/week-16.md` | 多 Agent 团队协作图：规划、实现、测试、审查、整合 | 章节导语后 |

## Course B 缺图页

| 页面 | 建议图片内容 | 放置位置 |
| --- | --- | --- |
| `course-b/week-02.md` | 组件库对比截图：同一按钮/卡片在 shadcn、Ant Design、Material UI 中的样式差异 | 组件库对比段落后 |
| `course-b/week-06.md` | 前端调用 AI 接口的数据流：用户输入、前端、后端代理、模型 API、结果回传 | 第一次讲 API 调用前 |
| `course-b/week-10.md` | 企业 RAG 治理图：知识域路由、版本过滤、权限边界、证据化回答 | 章节导语后 |
| `course-b/week-11.md` | PWA 安装与离线流程图：manifest、service worker、缓存、安装入口 | PWA 配置介绍后 |
| `course-b/week-12.md` | 小程序发布流程图：注册账号、配置 AppID、开发者工具上传、审核、发布 | 发布章节开头 |
| `course-b/week-13.md` | 支付安全流程图：后端下单、签名、微信支付、回调验签、更新订单 | 支付章节开头 |

## 首页与课程索引

| 页面 | 建议图片内容 | 放置位置 |
| --- | --- | --- |
| `index.md` | 两条课程路线总览图：Course A 偏 AI 编程方法，Course B 偏全栈产品实战 | 首页第一屏后 |
| `course-a/index.md` | Course A 学习路径图，按周展示从原型到 Agent Teams 的能力递进 | 课程介绍后 |
| `course-b/index.md` | Course B 产品构建路线图，按周展示设计、前端、后端、RAG、小程序、部署 | 课程介绍后 |
| `course-a/final-project.md` | 期末项目交付物看板示例 | 评分说明前 |
| `course-b/final-project.md` | 全栈项目架构模板图：前端、数据库、AI、支付、部署 | 项目要求前 |

## 已发现的临时替代

| 页面 | 当前处理 | 后续动作 |
| --- | --- | --- |
| `course-b/week-03.md` | 原 `nanobanana-example.png` 缺失，临时改为已有 AI 生成界面截图 `image38.png` | 补采真实 NanoBanana 首次生成结果图后替换 |
| `course-b/week-08.md` | 5 个语义化图片名缺失，已改为实际存在的 Dify 截图编号 | 后续整理时可把 `image15.png` 等重命名为语义文件名 |
