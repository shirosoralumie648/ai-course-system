#!/usr/bin/env python3
"""Generate Course B PPTX decks with LibreOffice UNO.

Run with system Python because python3-uno is installed for /usr/bin/python3:
  /usr/bin/python3 ai-course-system/course-b-agentic-development/slides/generate_course_b_pptx.py
"""

from __future__ import annotations

import os
import socket
import subprocess
import sys
import time
from pathlib import Path

import uno
from com.sun.star.awt import Point, Size
from com.sun.star.beans import PropertyValue


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "pptx"
HOST = "127.0.0.1"
PORT = 2002


def slide(title: str, bullets: list[str], note: str = "") -> dict[str, object]:
    return {"title": title, "bullets": bullets, "note": note}


DECKS: list[dict[str, object]] = [
    {
        "filename": "week-01-ai-native-software-engineering.pptx",
        "title": "第 1 周：AI 原生软件工程导论",
        "subtitle": "从 Chatbot 到 Coding Agent",
        "slides": [
            slide("本讲目标", ["区分 Chatbot、Copilot、Coding Agent、Agentic Workflow", "理解 Coding Agent 的工程风险", "掌握 Task Packet 的基本结构", "认识测试、Review、权限、安全和 Human Gate"]),
            slide("这门课不是 Prompt 技巧课", ["不是普通 Prompt Engineering", "不是工具演示课", "不是 AI 自动写代码宣传课", "不是无测试无审查 Demo 课"]),
            slide("这门课真正训练什么", ["提出任务", "组织上下文", "约束工具", "验证结果", "审查风险", "复盘失败"]),
            slide("为什么要学 Agentic Development", ["软件工程正在进入人与 Agent 协作阶段", "重要能力从背语法转向设计任务和验证交付", "Agent 能加速工程，也能放大错误"]),
            slide("四个概念", ["Chatbot：对话、解释、总结", "Copilot：代码补全和局部建议", "Coding Agent：读代码、改文件、跑命令", "Agentic Workflow：规则、测试、Review、Human Gate"]),
            slide("Coding Agent 能做什么", ["理解项目结构", "提出修改计划", "修 bug 或新增小功能", "运行测试并分析失败", "生成 diff 摘要和报告"]),
            slide("Coding Agent 不能默认做什么", ["删除大量文件", "修改依赖", "处理密钥", "修改登录、权限、支付", "合并 PR 或发布线上版本"]),
            slide("AI / Agent 可代劳任务地图", ["理解类", "规划类", "编码类", "测试类", "审查类", "文档类", "自动化类", "工作流类"]),
            slide("工程风险", ["误解需求", "扩大修改范围", "修改测试骗过结果", "编造测试通过", "泄漏密钥或隐私", "破坏项目结构"]),
            slide("Human Gate", ["范围确认", "危险操作审批", "最终接受或拒绝", "保留人工责任边界"]),
            slide("Task Packet 是什么", ["给 Coding Agent 的结构化任务包", "把模糊请求变成可执行任务", "把工程边界和验收标准写清楚"]),
            slide("Task Packet 组成", ["目标", "上下文", "允许修改范围", "禁止修改范围", "测试命令", "验收标准", "输出格式", "Human Gate"]),
            slide("坏任务描述", ["“帮我修一下这个 bug。”", "缺少项目路径", "缺少修改边界", "缺少测试命令", "缺少验收标准"]),
            slide("好任务描述", ["说明目标和失败现象", "列出相关文件", "限定允许和禁止范围", "要求先计划再修改", "指定测试命令和输出格式"]),
            slide("课堂活动", ["从最近遇到的代码问题出发", "写一个自己的 Task Packet", "同桌互评缺失项", "教师抽样点评"]),
            slide("本课程学习路径", ["Claude Code Bugfix", "Codex Code Change", "Project Rules", "Code Review Skill", "MCP 与 Agent Team", "测试、Review 与 CI"]),
            slide("作业", ["完成环境检查", "提交 week-01-task-packet.md", "阅读 Lab 01", "准备运行示例项目"]),
        ],
    },
    {
        "filename": "week-02-claude-code-basics.pptx",
        "title": "第 2 周：Claude Code 基础",
        "subtitle": "Lab 01：可审计 Bugfix",
        "slides": [
            slide("本讲目标", ["理解 Claude Code 的代码库任务方式", "给出受控 bugfix 任务", "审查计划、diff 和测试结果", "完成 Lab 01 流程"]),
            slide("从 Task Packet 开始", ["目标", "上下文", "允许和禁止范围", "测试命令", "验收标准", "Human Gate"]),
            slide("Claude Code 是什么", ["面向代码库任务的 Coding Agent", "能读项目、改文件、跑命令", "必须受规则和验证约束"]),
            slide("Lab 01 工作流", ["运行基线测试", "输入 Task Packet", "要求先计划", "人工确认", "小步修改", "看 diff", "跑测试", "复盘"]),
            slide("示例项目", ["repo-01-small-bugfix", "src/grade_utils.py", "tests/test_grade_utils.py", "固定测试命令"]),
            slide("初始测试", ["先运行失败测试", "保存失败日志", "记录失败测试名和错误类型"]),
            slide("任务描述重点", ["当前失败现象", "只允许修改 src/grade_utils.py", "禁止修改 tests/ 和教师材料", "先输出计划再修改"]),
            slide("计划审查", ["是否理解失败原因", "是否只改允许文件", "是否说明测试命令", "是否存在无关重构"]),
            slide("diff 审查", ["看实际修改文件", "检查是否修改测试", "确认修改对应失败现象", "避免无关重构"]),
            slide("测试证据", ["初始失败日志", "修复后测试日志", "失败时的下一轮分析", "不能伪造测试通过"]),
            slide("接受或拒绝", ["diff 是否在范围内", "测试是否真实", "学生能否解释修改", "是否仍有风险"]),
            slide("工具不可用替代流程", ["记录不可用原因", "手动修复", "保存 diff 和测试", "补写如果工具可用会如何下任务"]),
            slide("Lab 01 提交物", ["实验记录", "Claude Code 计划和输出摘要", "Git diff", "测试日志", "复盘"]),
            slide("常见扣分", ["不运行测试", "不看 diff", "修改测试骗过结果", "只复制 Agent 输出", "伪造工具记录"]),
        ],
    },
    {
        "filename": "week-03-codex-basics.pptx",
        "title": "第 3 周：Codex 基础",
        "subtitle": "Lab 02：小功能开发",
        "slides": [
            slide("本讲目标", ["理解 Codex 本地任务流程", "对比 Codex 与 Claude Code", "完成小功能开发", "新增测试并保护原有行为"]),
            slide("从 Bugfix 到 Feature", ["Bugfix 从失败测试开始", "Feature 需要主动写验收标准", "新增功能必须有新增测试"]),
            slide("Codex 是什么", ["面向本地代码任务的 Coding Agent", "计划、执行、验证", "关注 sandbox 和 approval"]),
            slide("Codex 工作流", ["Task Packet", "Plan", "Approval / Human Gate", "Edit", "Test", "Diff", "Summary"]),
            slide("Codex 与 Claude Code 对比", ["任务输入", "上下文读取", "权限请求", "diff 呈现", "测试执行", "总结质量"]),
            slide("Lab 02 项目", ["repo-02-feature-development", "src/todo_filter.py", "tests/test_todo_filter.py", "初始测试应通过"]),
            slide("新增需求", ["filter_titles_by_status(tasks, status)", "按状态过滤标题", "保持顺序", "无匹配返回空列表", "不破坏 list_titles"]),
            slide("验收标准", ["新增功能测试通过", "原有测试仍通过", "不新增依赖", "diff 在允许范围内"]),
            slide("新增测试设计", ["有匹配状态", "无匹配状态", "保持原始顺序", "原有 list_titles 行为"]),
            slide("权限请求判断", ["记录请求原因", "判断是否与任务相关", "依赖、网络、删除文件需 Human Gate"]),
            slide("diff 审查", ["是否新增函数", "是否新增测试", "是否保留旧测试", "是否无关修改"]),
            slide("工具对比记录", ["只基于本次证据", "不写泛化宣传", "说明任务、权限、测试、diff 差异"]),
            slide("Lab 02 提交物", ["任务说明", "Codex 输出摘要", "权限记录", "Git diff", "测试结果", "工具对比"]),
        ],
    },
    {
        "filename": "week-04-context-engineering.pptx",
        "title": "第 4 周：Context Engineering",
        "subtitle": "让 Agent 获得足够但不过量的上下文",
        "slides": [
            slide("本讲目标", ["理解上下文质量对 Agent 的影响", "整理代码库地图", "编写 context-pack", "为 Lab 03 规则文件准备材料"]),
            slide("为什么上下文决定质量", ["上下文不足导致猜测", "上下文过多稀释重点", "过期信息会误导 Agent"]),
            slide("高质量上下文公式", ["目标", "代码库地图", "相关文件", "错误或需求证据", "测试命令", "验收标准", "边界", "风险"]),
            slide("代码库地图", ["项目目标", "主要目录", "关键源文件", "关键测试文件", "入口命令", "当前任务相关路径"]),
            slide("任务上下文", ["当前目标", "当前行为", "期望行为", "相关文件", "不应改变的旧行为"]),
            slide("错误日志", ["失败测试名", "错误类型", "关键栈信息", "完整日志留存", "摘要交给 Agent"]),
            slide("测试命令", ["明确可执行命令", "无法测试需说明原因", "不把未运行测试写成通过"]),
            slide("验收标准", ["可判断", "可验证", "可审查", "包含文件范围和行为保护"]),
            slide("上下文过少", ["只有一句需求", "没有路径", "没有日志", "没有测试", "没有边界"]),
            slide("上下文过多", ["整仓无差别粘贴", "旧聊天混入", "过期需求污染", "当前目标不突出"]),
            slide("context-pack 模板", ["项目说明", "当前任务", "代码库地图", "相关文件", "证据", "边界", "测试", "验收", "Human Gate"]),
            slide("连接 Lab 03", ["规则文件是长期上下文", "Task Packet 是单次任务上下文", "context-pack 可转化为 CLAUDE.md / AGENTS.md"]),
        ],
    },
    {
        "filename": "week-05-rules.pptx",
        "title": "第 5 周：CLAUDE.md / AGENTS.md / Rules",
        "subtitle": "用规则文件建立工程边界",
        "slides": [
            slide("本讲目标", ["理解项目规则文件", "编写具体可执行规则", "比较有规则和无规则时 Agent 行为", "完成 Lab 03 准备"]),
            slide("从 context-pack 到 Rules", ["context-pack 面向单次任务", "Rules 面向长期项目约束", "规则减少重复说明"]),
            slide("规则文件解决什么问题", ["项目背景", "技术栈", "目录结构", "测试命令", "允许和禁止范围", "Human Gate"]),
            slide("不是空泛口号", ["不要只写高质量代码", "要写实际命令", "要写具体路径", "要写可检查边界"]),
            slide("CLAUDE.md", ["项目说明", "开发流程", "测试命令", "禁止行为", "输出要求"]),
            slide("AGENTS.md", ["通用 Agent 工作协议", "权限边界", "角色职责", "Review checklist", "失败处理"]),
            slide("无规则 vs 有规则", ["任务计划是否更具体", "是否主动提到测试", "是否识别禁止范围", "是否触发 Human Gate"]),
            slide("Human Gate 写法", ["删除文件", "大规模重构", "修改依赖", "访问外部服务", "处理密钥", "测试失败仍想提交"]),
            slide("Lab 03 流程", ["无规则分析", "编写规则", "有规则分析", "对比输出", "修订规则"]),
            slide("提交物", ["CLAUDE.md", "AGENTS.md", "对比记录", "规则设计说明", "复盘"]),
            slide("常见错误", ["只有口号", "没有测试命令", "没有禁止范围", "没有 Human Gate", "规则太长但不可执行"]),
        ],
    },
    {
        "filename": "week-06-permissions-hooks-security.pptx",
        "title": "第 6 周：权限、Hooks 与安全边界",
        "subtitle": "把危险操作从默认执行改为人工审批",
        "slides": [
            slide("本讲目标", ["理解文件、命令、网络、依赖边界", "设计危险操作审批清单", "理解 Hook 的教学定位", "形成失败处理流程"]),
            slide("规则与权限的区别", ["规则是文字协议", "权限是执行边界", "Hook 是流程检查点", "Human Gate 是责任边界"]),
            slide("文件访问边界", ["允许读写任务相关文件", "禁止输出密钥和隐私", "限制 .env、*.key、credentials.*"]),
            slide("命令执行边界", ["允许测试和只读检查", "谨慎格式化和构建", "禁止删除、重置、上传、不明脚本"]),
            slide("网络和依赖边界", ["默认不访问外部网络", "查询官方文档需确认", "新增依赖需说明影响和替代方案"]),
            slide("危险操作清单", ["删除文件", "修改依赖", "访问网络", "处理密钥", "修改登录/支付/权限", "发布版本"]),
            slide("Hook 示例", ["执行命令前检查白名单", "修改文件前检查路径", "输出结果前检查测试证据", "危险操作前请求确认"]),
            slide("失败处理", ["停止继续执行", "保存日志和 diff", "判断影响范围", "回到可解释状态", "重新给任务"]),
            slide("课堂任务", ["设计危险操作审批清单", "写明风险", "写明谁审批", "写明证据和失败处理"]),
            slide("连接后续", ["Skill 需要禁止行为", "MCP 需要工具权限", "Agent Team 需要角色边界"]),
        ],
    },
    {
        "filename": "week-07-skill-design.pptx",
        "title": "第 7 周：Skill 设计",
        "subtitle": "Lab 04：Code Review Skill",
        "slides": [
            slide("本讲目标", ["区分 Skill 和 Prompt", "设计 code-review Skill", "生成结构化 Review", "人工修订 Agent Review"]),
            slide("Skill 不是长 Prompt", ["有适用场景", "有触发条件", "有输入要求", "有执行步骤", "有输出格式", "有禁止行为"]),
            slide("为什么做 Review Skill", ["Review 可复用", "输出需要统一", "测试证据必须真实", "风险需要结构化"]),
            slide("Review 维度", ["需求符合度", "功能正确性", "代码质量", "架构一致性", "测试覆盖", "安全风险", "文档完整性"]),
            slide("Skill 输入", ["任务说明", "Git diff", "测试日志", "相关文件", "Rubric 或检查清单"]),
            slide("Skill 输出", ["总体结论", "主要问题", "测试证据", "安全风险", "建议修改", "Human Gate", "不确定项"]),
            slide("禁止行为", ["不得编造测试结果", "不得直接合并代码", "不得忽略 diff", "证据不足必须标记"]),
            slide("Lab 04 流程", ["编写 Skill", "准备 diff", "Agent 生成 Review", "人工修订 Review", "复盘 Skill 改进"]),
            slide("人工修订", ["标出遗漏", "标出夸大", "补充证据", "修订结论", "记录下一版改进"]),
            slide("提交物", ["code-review/SKILL.md", "原始 Review", "人工修订 Review", "测试证据", "复盘"]),
        ],
    },
    {
        "filename": "week-08-mcp-basics.pptx",
        "title": "第 8 周：MCP 原理与使用",
        "subtitle": "为 Agent 提供工具和资源",
        "slides": [
            slide("本讲目标", ["解释 MCP 解决什么问题", "区分 tools、resources、prompts", "识别工具调用安全边界", "设计工具调用场景"]),
            slide("MCP 解决什么", ["标准化工具接入", "标准化资源访问", "减少临时复制粘贴", "让 Agent 使用受控接口"]),
            slide("MCP 不解决什么", ["不保证工具输出正确", "不替代人工判断", "不自动解决权限问题", "不让任意命令变安全"]),
            slide("Tools", ["可调用动作", "可能有副作用", "需要输入输出约束", "最需要权限控制"]),
            slide("Resources", ["只读课程资料", "实验要求", "Rubric", "模板和示例", "仍需处理不可信内容"]),
            slide("Prompts", ["预定义任务模板", "Review 报告", "Task Packet 生成", "实验反馈草稿"]),
            slide("课程 MCP 场景", ["search_course_docs", "get_assignment_requirement", "check_project_structure", "run_course_tests", "generate_review_report"]),
            slide("安全风险", ["工具越权", "资源 prompt injection", "输入污染", "输出误信"]),
            slide("课堂任务", ["设计 2 个工具调用场景", "写输入输出", "写权限边界", "写 Human Gate"]),
            slide("期末项目连接", ["至少 1 个 MCP 配置或设计", "说明 tools/resources/prompts", "说明安全边界"]),
        ],
    },
    {
        "filename": "week-09-custom-mcp-server.pptx",
        "title": "第 9 周：自定义 MCP Server",
        "subtitle": "课程专用工具与资源接口设计",
        "slides": [
            slide("本讲目标", ["设计 tools、resources、prompts", "说明输入输出", "说明失败情况", "说明权限和 Human Gate"]),
            slide("设计原则", ["小而清楚", "只服务课程任务", "默认最小权限", "输出可审计", "失败可解释"]),
            slide("目标 1：课程资料", ["搜索文档", "获取实验要求", "返回来源路径", "避免过期或无来源信息"]),
            slide("目标 2：受限检查", ["检查项目结构", "运行预设测试", "禁止任意 shell", "返回退出码和日志"]),
            slide("目标 3：反馈草稿", ["根据 diff 和 Rubric 生成 Review", "区分证据和推测", "不得自动评分或合并"]),
            slide("核心工具", ["search_course_docs", "get_assignment_requirement", "check_project_structure", "run_course_tests", "generate_review_report"]),
            slide("输入规范", ["避免 command 字符串", "使用 project_id 和 test_profile", "路径白名单", "参数可验证"]),
            slide("输出规范", ["实际命令", "退出码", "摘要", "日志路径", "未验证项", "风险提示"]),
            slide("信任边界", ["课程材料可能过期", "学生提交不可信", "外部文档不可信", "工具输出需核对"]),
            slide("课堂任务", ["设计一个 MCP 工具", "写使用场景", "输入输出", "失败情况", "安全风险", "Human Gate"]),
        ],
    },
    {
        "filename": "week-10-agent-team.pptx",
        "title": "第 10 周：Subagents 与 Agent Team",
        "subtitle": "职责明确、权限有限的多 Agent 协作",
        "slides": [
            slide("本讲目标", ["设计 Planner、Coder、Tester、Reviewer", "明确输入输出和权限", "避免责任不清", "准备期末项目 Agent Team"]),
            slide("Agent Team 不是随便聊天", ["必须有职责", "必须有边界", "必须有交接", "必须有 Human Gate"]),
            slide("Planner", ["澄清需求", "拆解任务", "识别风险", "输出计划", "不直接改代码"]),
            slide("Coder", ["根据确认计划实现", "小步修改", "保持 diff 可审查", "不无计划重构"]),
            slide("Tester", ["生成测试", "运行测试", "分析失败", "不伪造测试通过", "不弱化测试"]),
            slide("Reviewer", ["审查 diff", "检查测试和安全", "提出修改建议", "不直接合并"]),
            slide("Human Gate", ["确认范围", "审批危险操作", "最终接受或拒绝", "承担责任边界"]),
            slide("标准工作流", ["需求输入", "Planner 计划", "Human Gate", "Coder 实现", "Tester 验证", "Reviewer 审查", "Human Gate 决策"]),
            slide("权限分离", ["提出方案的人不批准自己", "写代码的人不证明自己正确", "测试失败不能绕过", "合并必须人工决策"]),
            slide("期末项目任务", ["设计至少 3 个角色", "写输入输出", "写允许和禁止操作", "画 workflow"]),
        ],
    },
    {
        "filename": "week-11-testing-review-ci.pptx",
        "title": "第 11 周：测试、Review 与 CI",
        "subtitle": "把 Agent 输出纳入质量门禁",
        "slides": [
            slide("本讲目标", ["设计测试和 Review 流程", "理解 CI 作用和局限", "形成期末项目验证证据"]),
            slide("为什么需要质量门禁", ["Agent 输出不是完成", "测试验证行为", "Review 审查风险", "CI 自动化部分验证", "Human Gate 最终决策"]),
            slide("测试类型", ["单元测试", "集成测试", "构建检查", "静态检查", "手动验证"]),
            slide("测试证据", ["命令", "退出码", "通过和失败数量", "关键日志", "无法运行原因"]),
            slide("Review 维度", ["需求符合度", "功能正确性", "代码质量", "架构一致性", "测试覆盖", "安全风险", "文档完整性"]),
            slide("CI 的作用", ["自动运行测试", "统一门禁", "减少人为遗漏", "形成可复查记录"]),
            slide("CI 的局限", ["只覆盖已配置检查", "通过不等于需求正确", "通过不等于安全", "不能自动替代合并决策"]),
            slide("期末验证计划", ["测试命令", "测试范围", "Review checklist", "CI 或替代验证", "失败处理", "Human Gate"]),
            slide("Review 演练", ["读任务目标", "读 diff", "核对测试", "查安全风险", "给出接受/返工/拒绝/证据不足"]),
            slide("答辩证据链", ["Task Packet", "规则文件", "Skill", "MCP 设计", "Agent Team", "测试日志", "Review 报告", "Human Gate"]),
        ],
    },
    {
        "filename": "week-12-final-project-defense.pptx",
        "title": "第 12 周：期末项目答辩",
        "subtitle": "展示一个 AI 原生软件工程工作流",
        "slides": [
            slide("答辩目标", ["展示 Agentic Workflow", "解释规则、Skill、MCP、Agent Team", "提供测试和 Review 证据", "完成技术复盘"]),
            slide("不是普通 Demo", ["不只展示最终功能", "不只展示工具使用", "必须展示工程流程和证据链"]),
            slide("必须展示的材料", ["项目仓库", "规则文件", "Skill", "MCP 配置或设计", "Agent Team", "测试日志", "Review 报告", "Human Gate"]),
            slide("评分维度", ["工作流完整性", "规则可执行性", "Skill 质量", "MCP 设计", "Agent Team 分工", "验证证据", "安全边界", "复盘质量"]),
            slide("展示顺序建议", ["项目目标", "Workflow 图", "规则文件", "Task Packet", "Agent 计划", "diff", "测试", "Review", "Human Gate", "复盘"]),
            slide("答辩提问", ["Agent 为什么这样分工", "哪个规则最关键", "Skill 与 Prompt 有何区别", "MCP 为什么受限", "测试失败如何处理"]),
            slide("常见问题", ["只有最终功能", "规则空泛", "Skill 只是 Prompt", "MCP 权限过宽", "缺测试日志", "Human Gate 形同虚设"]),
            slide("课程回顾", ["从工具使用到工程流程", "从 Task Packet 到 Rules", "从 Skill 到 MCP", "从单 Agent 到 Agent Team", "从输出到质量门禁"]),
            slide("最终提交", ["仓库或代码包", "规则文件", "Skill", "MCP 设计", "Agent Team", "验证脚本", "Review", "演示材料", "技术报告", "复盘"]),
            slide("结束语", ["Agent 可以加速工程", "工程责任仍然在人", "证据、边界、审查和复盘是核心能力"]),
        ],
    },
]


def prop(name: str, value: str) -> PropertyValue:
    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def office_url(path: Path) -> str:
    return uno.systemPathToFileUrl(str(path))


def wait_for_port(timeout: float = 15.0) -> None:
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((HOST, PORT), timeout=0.5):
                return
        except OSError:
            time.sleep(0.2)
    raise RuntimeError("Timed out waiting for LibreOffice UNO listener")


def start_office() -> subprocess.Popen[str]:
    proc = subprocess.Popen(
        [
            "soffice",
            "--headless",
            "--norestore",
            "--nodefault",
            "--nofirststartwizard",
            f"--accept=socket,host={HOST},port={PORT};urp;StarOffice.ComponentContext",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    wait_for_port()
    return proc


def connect_desktop():
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    ctx = resolver.resolve(
        f"uno:socket,host={HOST},port={PORT};urp;StarOffice.ComponentContext"
    )
    smgr = ctx.ServiceManager
    return smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)


def add_text(page, doc, text: str, x: int, y: int, w: int, h: int, size: float, bold: bool = False):
    shape = doc.createInstance("com.sun.star.drawing.TextShape")
    shape.Position = Point(x, y)
    shape.Size = Size(w, h)
    page.add(shape)
    shape.Text.String = text
    cursor = shape.Text.createTextCursor()
    cursor.gotoStart(False)
    cursor.gotoEnd(True)
    cursor.CharHeight = size
    cursor.CharFontName = "Noto Sans CJK SC"
    cursor.CharWeight = 150 if bold else 100
    return shape


def add_bullets(page, doc, bullets: list[str], x: int, y: int, w: int, h: int):
    text = "\n".join(f"• {item}" for item in bullets)
    shape = add_text(page, doc, text, x, y, w, h, 24, False)
    return shape


def clear_page(page):
    for index in range(page.getCount() - 1, -1, -1):
        page.remove(page.getByIndex(index))


def build_deck(desktop, deck: dict[str, object]) -> None:
    doc = desktop.loadComponentFromURL("private:factory/simpress", "_blank", 0, ())
    pages = doc.getDrawPages()
    while pages.getCount() > 1:
        pages.remove(pages.getByIndex(pages.getCount() - 1))

    title = str(deck["title"])
    subtitle = str(deck["subtitle"])
    slides: list[dict[str, object]] = deck["slides"]  # type: ignore[assignment]

    first = pages.getByIndex(0)
    clear_page(first)
    add_text(first, doc, title, 1100, 1600, 23000, 1300, 38, True)
    add_text(first, doc, subtitle, 1300, 3100, 22000, 1000, 26, False)
    add_text(first, doc, "Agentic Development：AI 原生软件工程实践", 1300, 4300, 22000, 700, 18, False)

    for index, item in enumerate(slides, start=2):
        page = pages.insertNewByIndex(pages.getCount())
        clear_page(page)
        add_text(page, doc, str(item["title"]), 900, 500, 23600, 800, 30, True)
        add_bullets(page, doc, list(item["bullets"]), 1300, 1600, 22000, 4800)
        add_text(page, doc, f"{index - 1}/{len(slides)}", 22500, 6500, 2000, 400, 12, False)

    out_path = OUT_DIR / str(deck["filename"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.storeAsURL(
        office_url(out_path),
        (prop("FilterName", "Impress MS PowerPoint 2007 XML"), prop("Overwrite", True)),
    )
    doc.close(True)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    proc = start_office()
    try:
        desktop = connect_desktop()
        for deck in DECKS:
            build_deck(desktop, deck)
            print(f"generated {deck['filename']}")
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
    return 0


if __name__ == "__main__":
    sys.exit(main())
