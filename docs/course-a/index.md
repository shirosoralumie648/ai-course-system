# 课程 A：用 AI 做出你的第一个产品原型

> **完成比完美重要。** 这门课不要求你会写代码，而是带你用 AI 把一个想法，一步步变成能演示、能用的产品原型。

<ChapterIntroduction duration="16 周，每周 2 课时" output="一个完整的 AI 产品原型 + 一套可复用的 Claude Code 工程工作流" :tags="['产品思维', 'AI IDE', 'Claude Code', '需求发现', '原型搭建', 'Agent 协作']">

面向非计算机专业学生。核心不是学语法，而是训练用 AI 做产品与协作开发的完整能力：先消除编程畏惧，掌握 AI IDE 与 Claude Code，再发现真需求、搭出原型、接入真实 AI 能力，最后学习 Workflow、Skills、MCP、Spec Coding、长运行任务与 Agent Teams。

</ChapterIntroduction>

## 你是谁？

这门课面向文科、商科、管理、教育、新闻传播、设计、医学、法学、外语等专业学生。你不需要编程基础，只需要：

- 能用电脑完成日常学习任务
- 愿意尝试新工具
- 愿意把一个想法认真打磨成产品

## 学完能做什么

- 用 AI IDE 把一句话需求变成能跑的程序
- 用 Claude Code 在终端里完成文件理解、修改、调试和协作
- 用产品方法发现并验证一个真实的痛点
- 从需求出发搭出可交互的多页原型
- 给原型接入真正的 AI 能力（调 API、管理密钥安全）
- 用 Workflow、Skills、MCP、Spec Coding 和 Agent Teams 把 AI 协作沉淀成可复用流程

## 小林的故事

> 小林是新闻传播专业大三学生，不会写代码，但一直想做一个属于自己的小工具。这学期她选了这门课，从做小游戏消除畏惧开始，先学会 AI IDE 和 Claude Code，再找到「文科生求职测评」这个创意，亲手搭出原型、接上 AI。后半程她继续把 Claude Code 用到真实项目里：整理工作流、沉淀 Skills、接入 MCP、写 Spec、处理长运行任务，最后尝试 Agent Teams。她说："我不只是做出了一个原型，我还知道怎么让 AI 按流程持续帮我做事。"

跟着小林的故事学完 16 周，你也会做出属于自己的第一个产品原型，并掌握一套可继续复用的 AI 协作开发方法。

## 课程结构

<StepBar :active="0" :items="[
  { title: '第 1-3 周', description: '游戏热身 + AI IDE + Claude Code 快速上手' },
  { title: '第 4-8 周', description: '发现需求、验证创意、搭建并迭代产品原型' },
  { title: '第 9-13 周', description: 'Workflow、Skills、MCP、Superpowers 与 Spec Coding' },
  { title: '第 14-16 周', description: '长运行任务、Agent SDK 与 Agent Teams' }
]" />

## 你会学到什么

<WorkflowDiagram title="小林的产品原型之路（最终成果预览）" :steps="[
  { name: '找创意', description: '发现真实痛点并验证值不值得做', type: 'human' },
  { name: '写需求', description: '把模糊想法收敛成具体功能', type: 'human' },
  { name: '搭原型', description: 'AI IDE 生成可交互的多页应用', type: 'assist' },
  { name: '接 AI', description: '调用真实 AI 能力，注意密钥安全', type: 'assist' },
  { name: '走查', description: '亲手点一遍，确认流程跑通', type: 'human' },
  { name: '展示', description: '完整演示作品并答辩', type: 'human' }
]" />

| 周次 | 主题 | 核心任务 |
|---|---|---|
| [Week 01](/course-a/week-01) | 做出第一个小游戏 | 消除编程畏惧，跑出能玩的小游戏 |
| [Week 02](/course-a/week-02) | AI IDE 入门 | 装好工具，跑出第一个程序 |
| [Week 03](/course-a/week-03) | Claude Code 快速上手 | 在终端中完成对话、文件引用、修改和基本调试 |
| [Week 04](/course-a/week-04) | 找到一个好创意 | 发现真实痛点，完成需求发现 |
| [Week 05](/course-a/week-05) | 验证你的创意 | Mom Test、JTBD 与双钻模型 |
| [Week 06](/course-a/week-06) | 从需求到单页原型 | 把需求变成可演示原型 |
| [Week 07](/course-a/week-07) | 接入真正的 AI 能力 | 调 API、管理密钥安全、验证真实调用 |
| [Week 08](/course-a/week-08) | 完整项目实践 | 补齐异常、数据、反馈与迭代 |
| [Week 09](/course-a/week-09) | Workflow | 建立 AI 辅助开发的标准工作流 |
| [Week 10](/course-a/week-10) | Skills 指南 | 把经验沉淀成可复用技能 |
| [Week 11](/course-a/week-11) | MCP 服务器 | 让 Claude Code 连接外部工具与数据 |
| [Week 12](/course-a/week-12) | Superpowers | 用流程纪律提升 AI 协作质量 |
| [Week 13](/course-a/week-13) | Spec Coding | 从即兴对话转向规格驱动实现 |
| [Week 14](/course-a/week-14) | 长运行任务 | 让 Claude Code 持续执行复杂任务 |
| [Week 15](/course-a/week-15) | Claude Agent SDK | 用 SDK 构建可控 Agent 自动化 |
| [Week 16](/course-a/week-16) | Agent Teams | 多智能体协作与课程总结 |

<SummaryCard title="课程 A 学习路径" :sections="[
  { number: '1', title: '学会发现真需求', items: ['痛点、爽点、痒点的区别', '用 Mom Test 问对问题，不被假需求骗'] },
  { number: '2', title: '学会指挥 AI 做产品', items: ['把模糊创意收敛成具体需求', '用 AI IDE 和 Claude Code 跑出原型，遇到报错会定位和转述'] },
  { number: '3', title: '学会工程化协作', items: ['用 Workflow 和 Spec 管住复杂任务', '用 Skills、MCP、Agent SDK 与 Agent Teams 扩展 AI 能力'] }
]" :outputs="[
  '3 个实验报告',
  '1 个可演示的 AI 产品原型',
  '1 套 Claude Code 协作工作流',
  '1 个期末展示项目'
]" />
