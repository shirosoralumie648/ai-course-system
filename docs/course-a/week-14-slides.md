# Week 14：长运行任务

## 让 Claude Code 持续工作到天亮

**课程 A：产品原型 + Claude Code 高级技能**

* * *

# 小林的困境

> 任务：把 55 个测试文件从 Jest 迁移到 Vitest Claude Code 改了 5 个文件后说「完成了」 实际上还有 50 个文件没动

**AI 总是「差不多就行」**

* * *

# 本周目标

-   ⏱️ **学习时长**：约 3 小时
-   🎯 **产出物**：掌握让 Claude Code 持续工作的完整方案
-   📚 **前置要求**：学完前几章 Claude Code 基础
-   🏷️ **关键词**：长运行任务、Ralph Loop、自动化、迭代开发

* * *

# 学习路线

```
① 理解问题 → ② 解决方案 → ③ 实战演练
```

**今天的核心**：

-   理解为什么 AI 会「过早停止」
-   学会用循环系统让 AI 持续工作
-   掌握 Ralph Loop 插件的使用
-   用 BBS 论坛系统实战演示

* * *

# Part 1

## 为什么 AI 会过早停止？

* * *

# 小林的真实经历

**任务**：迁移测试框架（Jest → Vitest）

**Claude 的输出**：

```
✓ 已将测试迁移到 Vitest
✓ 更新了 vite.config.js
✓ 修改了 5 个测试文件
任务完成！
```

**实际情况**：

-   还有 50 个测试文件没改
-   依然在用 Jest 的 API
-   运行 `npm test` 一堆报错

* * *

# AI 的「完成判断」不可靠

**人类的完成标准**（客观）：

-   所有测试通过 ✓
-   功能完整可用 ✓
-   代码质量达标 ✓
-   文档更新完成 ✓

**AI 的完成判断**（主观）：

-   「看起来差不多了」→ 停止
-   「输出够多了」→ 停止
-   「不知道接下来该干什么」→ 停止

* * *

# 核心问题

**AI 无法准确判断自己的工作是否真正完成**

它不是偷懒，而是真的「觉得」自己完成了

**解决方案**： 需要一个**外部系统**来判断任务是否真正完成 而不是依赖 AI 自己的感觉

* * *

# 解决方案的核心思想

**让 AI 在一个「循环」中工作**

每次 AI 想退出时，外部系统检查三个问题：

1.  **真的完成了吗？** 有没有明确的完成标记？
2.  **符合客观标准了吗？** 测试通过了吗？构建成功了吗？
3.  **还有没有遗漏？** 有没有文件没处理？有没有功能没实现？

如果没有，就重新注入任务，继续下一轮

* * *

# 传统方式 vs 循环方式

**传统方式（一次性）**：

```
你：帮我重构认证模块

Claude：
1. 抽取 AuthService 类
2. 添加几个测试
3. 更新文档

完成！（实际只做了 30%）
```

* * *

# 传统方式 vs 循环方式

**循环方式（持续迭代）**：

```
你：帮我重构认证模块，直到所有测试通过

循环系统：
第 1 轮：抽取 AuthService
第 2 轮：发现测试失败，修复
第 3 轮：补充遗漏的测试
第 4 轮：更新文档
第 5 轮：所有测试通过 ✓

真正完成！
```

* * *

# Part 2

## 解决方案：从简单到强大

* * *

# 方法一：While True Bash Loop

**最简单的实现**（5 行代码）：

```bash
#!/bin/bash
while true; do
    cat PROMPT.md | claude
done
```

**工作原理**：

-   读取任务描述
-   启动 Claude Code
-   Claude 退出后自动重启
-   无限循环，直到手动中断

* * *

# While True Loop 的优缺点

**优点**：

-   ✓ 极其简单，任何人都能看懂
-   ✓ 不需要任何配置，立即可用
-   ✓ 适合快速实验

**缺点**：

-   ✗ 无法判断任务是否真的完成
-   ✗ 可能无限空转，浪费 API 调用
-   ✗ 没有安全保护机制

* * *

# 安全改进版

```bash
#!/bin/bash
MAX_ITERATIONS=50
iteration=0

while true; do
    iteration=$((iteration + 1))
    echo "=== 迭代 $iteration/$MAX_ITERATIONS ==="

    cat PROMPT.md | claude

    if [ $iteration -ge $MAX_ITERATIONS ]; then
        echo "达到最大迭代次数，停止"
        break
    fi

    sleep 5  # 避免 API 限流
done
```

* * *

# 方法二：Ralph Loop（官方推荐）

**Ralph Loop** 是 Anthropic 官方插件 专门解决长时间任务问题

**命名来源**： 《辛普森一家》中的 Ralph Wiggum 象征「尽管失败，仍坚持尝试」的精神

**核心机制**：Stop Hook（停止钩子）

* * *

# Stop Hook 工作原理

**没有 Ralph**：

```
Claude：
1. 写了几个文件
2. 觉得差不多了
3. 退出 ✓

（实际只完成 30%）
```

* * *

# Stop Hook 工作原理

**有 Ralph（Stop Hook）**：

```
Claude：
1. 写了几个文件
2. 想退出 → Stop Hook 拦截
3. 检查：有 DONE 标记吗？没有
4. 重新注入任务，继续
5. 修复测试
6. 想退出 → Stop Hook 拦截
7. 检查：有 DONE 标记吗？没有
8. 继续...
9. 所有测试通过，输出 <promise>DONE</promise>
10. Stop Hook：找到标记，允许退出 ✓
```

* * *

# 安装 Ralph Loop

**方法一：自然语言安装**

```
你：帮我安装 Ralph Loop 插件

Claude：我来帮你安装 ralph-loop 插件...
[自动安装]
安装完成！
```

**方法二：手动安装**

```bash
/plugin install ralph-loop
```

**可用命令**：

-   `/ralph-loop` - 启动循环
-   `/cancel-ralph` - 取消循环
-   `/help ralph` - 查看帮助

* * *

# Ralph Loop 基本使用

**语法**：

```bash
/ralph-loop "任务描述，完成后输出 <promise>完成标记</promise>" \
  --max-iterations 50 \
  --completion-promise "完成标记"
```

**实际示例**：

```bash
/ralph-loop "构建一个待办事项 API，包含 CRUD 操作、输入验证、测试。
             全部完成后输出 <promise>COMPLETE</promise>" \
  --max-iterations 50 \
  --completion-promise "COMPLETE"
```

* * *

# 参数说明：max-iterations

**最大迭代次数**（安全机制）

任务类型

推荐迭代次数

简单重构

20-30

测试迁移

30-50

功能开发

50-80

大型项目

80-150

**作用**：

-   防止无限循环消耗 API 额度
-   即使任务没完成，达到上限也会停止

* * *

# 参数说明：completion-promise

**完成标记**（判断任务是否完成）

**推荐使用清晰的标记**：

-   ✓ `COMPLETE`
-   ✓ `TASK_DONE`
-   ✓ `MIGRATION_FINISHED`
-   ✗ `完成`（太模糊，可能误触发）
-   ✗ `done`（太常见，可能误触发）

**最佳实践**： 使用 `<promise>标记</promise>` 格式 例如：`<promise>TODO_API_COMPLETE</promise>`

* * *

# Prompt 编写最佳实践

**❌ 不好的 Prompt**：

```
写一个 todo API
```

问题：没有明确的完成标准，AI 可能写个基础框架就说完成了

* * *

# Prompt 编写最佳实践

**✅ 好的 Prompt**：

```
/ralph-loop "
请从零开始构建一个 Todo API，使用 TDD 方式开发。

阶段 1：基础功能
- POST /todos - 创建任务
- GET /todos - 获取列表
- GET /todos/:id - 获取单个
- PUT /todos/:id - 更新
- DELETE /todos/:id - 删除

阶段 2：输入验证
- 标题不能为空
- 完成状态必须是布尔值

阶段 3：测试
- 为每个端点编写测试
- 覆盖率 > 80%

验收标准：
- 所有测试通过（npm test）
- 代码通过 linter 检查（npm run lint）
- README 包含 API 文档

完成后输出：<promise>TODO_API_COMPLETE</promise>
" --max-iterations 40 --completion-promise "TODO_API_COMPLETE"
```

* * *

# 好的 Prompt 包含三要素

1.  **分阶段的任务描述** - 让 AI 知道要做什么
2.  **明确的验收标准** - 让 AI 知道什么叫「完成」
3.  **唯一的完成标记** - 让系统知道何时停止

* * *

# 什么时候适合用 Ralph Loop

**✅ 适合的场景**：

-   测试迁移（有明确目标，测试通过即可验证）
-   大规模重构（可以定义具体的重构规则）
-   框架迁移（迁移完成后代码能正常运行）
-   批量添加类型（typecheck 通过即完成）
-   测试覆盖率提升（覆盖率百分比是客观指标）
-   文档生成（API 文档可以自动验证）
-   Bug 修复（有复现步骤，测试通过即修复成功）

* * *

# 什么时候不适合用 Ralph Loop

**❌ 不适合的场景**：

-   架构设计决策（需要权衡多种方案）
-   安全相关代码（安全漏洞可能很隐蔽）
-   需求模糊的任务（没有明确完成标准）
-   探索性工作（需要不断调整方向）
-   创意性设计（需要人类审美判断）
-   简单一次性任务（使用 Ralph 是浪费）

* * *

# 判断标准

问自己三个问题：

1.  **我能定义明确的完成标准吗？** 如果不能，不适合

2.  **有客观的验证方法吗？**（测试、构建、类型检查） 如果没有，不适合

3.  **这个任务需要我持续反馈吗？** 如果是，不适合


如果三个答案都是「是、是、否」，那就放手让 Ralph 去做吧！

* * *

# Part 3

## 安全机制：防止无限循环

* * *

# 硬性限制

**1\. 最大迭代次数（必须设置）**

```bash
--max-iterations 50  # 达到 50 次后都会停止
```

**2\. 时间限制**

```bash
# 最长运行 4 小时后自动停止
timeout 4h /ralph-loop "任务描述" --max-iterations 100
```

**3\. API 预算警告** 在 `.claude/settings.json` 中配置：

```json
{
  "costAlertThresholds": [10, 50, 100],
  "alertAction": "pause_and_notify"
}
```

* * *

# 智能检测

**检查最近几次提交有没有实质变化**：

```bash
# 检查最近 5 次提交
if [ $(git diff HEAD~5 | wc -l) -eq 0 ]; then
    echo "最近 5 次提交没有实质变化，可能陷入循环"
    exit 1
fi
```

如果最近 5 次提交的代码差异很小，说明可能陷入了死循环

* * *

# 人工检查点

**每 10 次迭代暂停一次，等待确认**：

```bash
if [ $((iteration % 10)) -eq 0 ]; then
    read -p "已完成 $iteration 次迭代，继续吗？(y/n)" answer
    if [ "$answer" != "y" ]; then
        break
    fi
fi
```

适合特别重要的任务

* * *

# Part 4

## 实战：构建完整的 BBS 论坛系统

* * *

# 项目目标

**用户端功能**：

-   用户注册、登录、退出
-   浏览帖子列表（分页）
-   查看帖子详情
-   发布新帖
-   评论功能
-   个人中心（查看自己的帖子、修改个人信息）

**管理后台功能**：

-   管理员登录
-   用户管理（封禁、解封）
-   帖子管理（删除、置顶）
-   评论管理
-   系统统计

* * *

# 技术栈

**后端**：

-   Node.js + Express
-   SQLite 数据库（better-sqlite3）
-   JWT Token 认证

**前端**：

-   React + React Router
-   Axios
-   Tailwind CSS

**开发方式**：

-   TDD（测试驱动开发）
-   后端使用 Jest
-   前端使用 Vitest

* * *

# 启动 Ralph Loop

```bash
/ralph-loop "请从零开始构建一个完整的 BBS 论坛系统，使用 TDD 方式开发。

项目结构要求：
- backend/ 目录：Express API 服务器
- frontend/ 目录：React 前端应用
- 两个目录都有各自的测试

后端功能要求：
- 使用 Express 框架
- SQLite 数据存储（better-sqlite3）
- JWT 用户认证（jsonwebtoken + bcrypt）
- 用户表：id、username、password、email、role、createdAt
- 帖子表：id、title、content、authorId、category、pinned、createdAt
- 评论表：id、content、postId、authorId、createdAt

后端 API 端点：
- POST /api/auth/register - 用户注册
- POST /api/auth/login - 用户登录
- GET /api/posts - 获取帖子列表（分页、分类筛选）
- GET /api/posts/:id - 获取帖子详情
- POST /api/posts - 发布帖子（需登录）
- PUT /api/posts/:id - 编辑帖子（作者或管理员）
- DELETE /api/posts/:id - 删除帖子（作者或管理员）
- POST /api/posts/:id/comments - 发表评论（需登录）
- GET /api/user/profile - 获取个人信息（需登录）
- PUT /api/user/profile - 更新个人信息（需登录）
- GET /api/admin/stats - 管理员统计（需管理员）
- GET /api/admin/users - 用户列表（需管理员）
- PUT /api/admin/users/:id/ban - 封禁用户（需管理员）

前端页面要求：
- /login - 登录页
- /register - 注册页
- / - 首页（帖子列表）
- /post/:id - 帖子详情
- /new - 发布帖子
- /profile - 个人中心
- /admin - 管理后台（需管理员权限）

管理后台功能：
- 用户管理（查看、封禁、解封）
- 帖子管理（查看、删除、置顶）
- 评论管理（查看、删除）
- 系统统计（用户数、帖子数、评论数）

TDD 要求：
- 先写测试，后写代码
- 每个功能都要有对应的测试
- 后端使用 Jest，API 测试要覆盖所有端点
- 前端使用 Vitest，组件测试要覆盖主要功能
- 认证中间件要有测试

验收标准：
- 运行 npm test（后端）全部通过
- 运行 npm test（前端）全部通过
- 前端可以正常启动并使用
- 后端 API 可以正常响应
- 普通用户和管理员权限正确隔离
- 代码通过 ESLint 检查

完成后输出：<promise>BBS_SYSTEM_COMPLETE</promise>
" --max-iterations 150 --completion-promise "BBS_SYSTEM_COMPLETE"
```

* * *

# 预计时间与成本

**如果人工编写**：大约 40-60 小时

-   数据库设计：4 小时
-   后端 API 开发：15 小时
-   前端页面开发：18 小时
-   认证系统：5 小时
-   测试编写：10 小时
-   前后端联调：8 小时

**使用 Ralph Loop**：约 6-10 小时

-   基础版本（核心功能）：约 3-5 小时
-   完整版本（包含管理后台、测试）：约 6-10 小时
-   预估成本：$20-40（取决于迭代次数）

* * *

# 监控进度

**1\. 查看迭代次数**

```
=== 迭代 25/150 ===
```

**2\. 查看日志**

-   「设计数据库表结构...」
-   「编写用户注册 API...」
-   「实现前端登录组件...」
-   「修复测试失败...」

**3\. 测试状态**

-   第 5 轮：10 passed, 3 failed
-   第 12 轮：25 passed, 1 failed
-   第 18 轮：35 passed, 0 failed ✓

* * *

# 完成后验证

```bash
# 后端测试
cd backend
npm test

# 前端测试
cd frontend
npm test

# 启动后端
cd backend
npm start

# 启动前端（另一个终端）
cd frontend
npm run dev
```

**手动测试流程**： 注册新用户 → 登录 → 浏览帖子 → 发布新帖 → 发表评论 → 访问个人中心 → 管理后台

* * *

# 注意事项

**1\. Prompt 越详细，结果越好** 模糊的 Prompt 导致需要更多迭代来修正

**2\. 设置合理的迭代次数** BBS 系统比较复杂，建议至少 100 次迭代

**3\. TDD 是推荐方式** 先写测试可以大幅减少调试时间

**4\. 最终需要人工验证** AI 可能遗漏边界情况或特殊场景

**5\. 数据库设计要仔细** 如果你对数据库设计有明确想法，最好在 Prompt 中详细说明

* * *

# Ralph Loop 的真实案例

* * *

# 案例 1：Y Combinator 黑客松

**时间**：晚上 11 点设置任务，去睡觉 **任务**：根据 specs 目录下的 6 个产品需求，依次实现每个项目的 MVP **设置**：最大迭代次数 200 次 **结果**：第二天早上醒来，6 个可演示的项目全部完成 **成本**：$297

**这就是 Ralph 的威力——你睡觉的时候，AI 在工作**

* * *

# 案例 2：Boris Cherny 的 30 天实验

**Boris Cherny**（Claude Code 负责人）使用 Ralph Loop + Opus 4.5 模型

**时间**：30 天 **成果**：

-   259 个 PR
-   497 次提交
-   新增 40,000 行代码
-   删除 38,000 行代码
-   **100% 由 Claude Code 完成**，没有人工编写一行代码

* * *

# 案例 3：CURSED 编程语言

**Geoffrey Huntley**（Ralph 的创作者）用 Ralph Loop 在 3 个月内自主构建了一门完整编程语言

**项目**：CURSED 编程语言 **特点**：使用 Gen Z 俚语作为关键字（`slay`、`sus`、`based`） **包含**：

-   完整的 LLVM 编译器实现
-   标准库
-   部分编辑器支持

* * *

# 案例 4：自动重构遗留项目

**初始状态**：

-   代码混乱，没有测试
-   文档缺失
-   技术债务严重

**任务设置**：

1.  为现有代码添加测试
2.  逐步重构，每次重构后确保测试通过
3.  更新文档

**结果**：

-   运行了一整个周末
-   47 次提交
-   测试覆盖率达到 75%
-   完整的 API 文档
-   成本约 $12

* * *

# Ralph Loop 的哲学

* * *

# 三个核心哲学思想

**1\. 迭代大于完美**

-   第 1 次：写个框架
-   第 2 次：修复 bug
-   第 3 次：优化代码
-   第 4 次：添加测试
-   每次都比上一次更好

**2\. 失败是数据**

-   测试失败 → 知道哪里有问题
-   修复问题 → 再次测试
-   不要害怕失败，要从失败中学习

**3\. 持续尝试**

-   **Keep trying until it works**
-   就像 Ralph Wiggum，虽然经常失败，但从不放弃

* * *

# 方法对比与选择

* * *

# 各种方法对比

方法

复杂度

完成检测

安全机制

适用场景

**While True Loop**

⭐ 极简

✗ 无

✗ 基础

快速实验、原型验证

**Ralph Loop**

⭐⭐ 简单

✓ Stop Hook

✓ 完善

通用推荐、大部分场景

**后台任务（Ctrl+B）**

⭐ 极简

✗ 无

✗ 无

简单的非阻塞执行

* * *

# 选择建议

-   **想要简单快速？** 用 While True Loop 5 行代码就能工作，但功能有限

-   **想要通用推荐？** 用 Ralph Loop 官方支持，功能完整，适合大部分场景

-   **只是想后台运行？** 按 `Ctrl+B` 适合长时间测试、构建等不需要循环的任务


* * *

# 本周回顾

* * *

# 学习进度检查

✅ 理解过早停止问题（AI 为什么会「差不多就行」） ✅ 掌握 While True Loop（最简单的循环方式） ✅ 掌握 Ralph Loop（官方推荐的解决方案） ✅ 会写好的 Prompt（分阶段任务、验收标准、完成标记） ✅ 理解适用场景（什么任务适合/不适合用 Ralph Loop） ✅ 掌握安全机制（迭代上限、成本预警、智能检测） ✅ 完成实战案例（BBS 论坛系统）

* * *

# 自测题

**1\. 为什么 AI 会「过早停止」？**

**2\. Ralph Loop 的 Stop Hook 机制是如何工作的？**

**3\. 写一个好的 Ralph Loop Prompt 需要包含哪三个关键要素？**

**4\. 判断以下任务是否适合用 Ralph Loop：**

-   a) 把项目中所有 var 改成 let/const
-   b) 设计一个新的微服务架构
-   c) 修复一个有明确复现步骤的 bug
-   d) 为产品选择一个 UI 设计风格
-   e) 把测试覆盖率从 40% 提升到 80%

* * *

# 本周作业

**必做**：

-   用 Ralph Loop 完成一个中等规模的任务
-   记录迭代次数、耗时、成本
-   总结 Prompt 编写经验

**选做**：

-   尝试用 While True Loop 实现同样的任务，对比效果
-   为你的项目编写一套 Ralph Loop Prompt 模板库
-   分享你的 Ralph Loop 使用经验到课程讨论区

* * *

# 下周预告

## Agent Teams - 多代理协作

**从单个 AI 到 AI 团队****从串行工作到并行协作****从单打独斗到团队作战**

* * *

# Q&A

## 有问题吗？

* * *

# 谢谢！

## 期待看到你用 Ralph Loop 完成的项目

**记住**：

> 迭代大于完美 失败是数据 持续尝试直到成功
