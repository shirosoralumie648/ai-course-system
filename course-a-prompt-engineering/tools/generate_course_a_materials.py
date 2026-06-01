#!/usr/bin/env python3
"""Generate Course A teacher materials and PPTX decks.

Run from repository root:
  /usr/bin/python3 ai-course-system/course-a-prompt-engineering/tools/generate_course_a_materials.py
"""

from __future__ import annotations

import socket
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PPTX_DIR = BASE / "slides" / "pptx"


WEEKS = [
    {
        "n": 1,
        "title": "生成式 AI 基础",
        "subtitle": "能力、边界、幻觉与人工判断",
        "question": "生成式 AI 能做什么、不能做什么，为什么输出必须被人验证？",
        "objectives": ["理解生成式 AI 输出的概率性", "识别幻觉、偏见和过度自信", "建立人工判断和复核意识", "完成一次输出差异观察"],
        "concepts": ["概率性输出", "幻觉", "上下文", "人工判断", "风险记录"],
        "activity": "对同一专业问题连续提问 3 次，比较输出差异、事实冲突和表达变化。",
        "homework": "记录一次 AI 输出错误，说明错误类型、发现方式、修订方式和风险。",
        "deliverables": ["输出差异观察表", "AI 错误案例记录", "课堂复盘"],
        "risk": "学生把 AI 输出当成搜索结果或权威结论。",
    },
    {
        "n": 2,
        "title": "Prompt 基本结构",
        "subtitle": "角色、任务、背景、限制、格式与评价标准",
        "question": "怎样把模糊请求改写成可执行、可评价的 Prompt？",
        "objectives": ["掌握 Prompt 的基本组成", "能改写模糊 Prompt", "能设置输出格式和评价标准", "理解模板不能代替任务分析"],
        "concepts": ["角色", "任务", "背景", "限制", "输出格式", "评价标准"],
        "activity": "把一个模糊 Prompt 改写成面向专业任务的结构化 Prompt。",
        "homework": "提交 3 个专业任务 Prompt，并为每个 Prompt 写出使用场景和评价标准。",
        "deliverables": ["坏 Prompt 分析", "结构化 Prompt", "Prompt 设计说明"],
        "risk": "学生只背模板，不理解任务目标和评价标准。",
    },
    {
        "n": 3,
        "title": "任务拆解与上下文表达",
        "subtitle": "从复杂任务到上下文包",
        "question": "如何把复杂专业任务拆成 AI 可以辅助执行的步骤？",
        "objectives": ["能拆解复杂任务", "能组织材料、约束、样例和输出格式", "能判断上下文过多和过少的问题", "能提交任务拆解表"],
        "concepts": ["任务拆解", "上下文包", "材料选择", "约束条件", "样例", "输出格式"],
        "activity": "为一个专业任务写上下文包，包含目标、材料、限制、样例和输出格式。",
        "homework": "提交任务拆解表，说明每一步 AI 做什么、人做什么、如何验收。",
        "deliverables": ["任务拆解表", "上下文包", "人工验收标准"],
        "risk": "学生把大任务一次性交给 AI，缺少分步验收。",
    },
    {
        "n": 4,
        "title": "AI 辅助调研",
        "subtitle": "问题生成、资料整理与来源核查",
        "question": "如何用 AI 辅助调研，同时避免虚假来源和不可靠结论？",
        "objectives": ["能生成调研问题", "能整理关键词和资料框架", "能核查来源可信度", "能记录引用和不确定项"],
        "concepts": ["调研问题", "关键词", "来源核查", "引用风险", "证据等级"],
        "activity": "围绕专业主题生成调研问题、关键词和资料核查表。",
        "homework": "提交调研记录和来源核查说明，标明 AI 参与环节。",
        "deliverables": ["调研问题清单", "来源核查表", "引用风险说明"],
        "risk": "学生引用 AI 编造的来源或未核查的结论。",
    },
    {
        "n": 5,
        "title": "AI 辅助写作",
        "subtitle": "提纲、初稿、改写、润色与人工修订",
        "question": "如何让 AI 参与写作过程，而不是替代作者判断？",
        "objectives": ["能用 AI 辅助生成提纲和初稿", "能控制写作风格和受众", "能进行人工修订", "能说明学术诚信边界"],
        "concepts": ["写作目标", "受众", "风格控制", "人工修订", "引用", "学术诚信"],
        "activity": "对一段 AI 生成文本进行人工修订，标注事实、结构、风格和引用问题。",
        "homework": "提交写作前后版本、AI 使用记录和人工修订说明。",
        "deliverables": ["写作 Prompt", "AI 初稿", "人工修订稿", "修订说明"],
        "risk": "学生直接提交未经核查和修订的 AI 文本。",
    },
    {
        "n": 6,
        "title": "AI 辅助数据分析",
        "subtitle": "表格理解、指标解释、图表与错误检查",
        "question": "如何用 AI 辅助数据分析，同时避免错误计算和过度解读？",
        "objectives": ["能描述数据字段和指标", "能让 AI 辅助解释图表", "能检查计算和结论", "能写出分析风险说明"],
        "concepts": ["数据字段", "指标解释", "数据清洗", "图表解读", "错误检查", "过度解读"],
        "activity": "分析一个小型公开数据表，生成指标解释、图表建议和风险清单。",
        "homework": "提交分析报告、AI 交互记录、人工核查说明和风险说明。",
        "deliverables": ["数据说明", "分析报告", "核查记录", "风险说明"],
        "risk": "学生相信 AI 的错误计算或把相关性写成因果关系。",
    },
    {
        "n": 7,
        "title": "AI 辅助创意与展示、个人 AI 工作流",
        "subtitle": "从创意发散到可复用流程",
        "question": "如何把零散 AI 使用变成稳定的个人工作流？",
        "objectives": ["能用 AI 做创意发散和筛选", "能设计展示结构", "能画出个人 AI 工作流", "能准备期末项目选题"],
        "concepts": ["创意发散", "创意筛选", "展示结构", "流程复用", "个人工作流"],
        "activity": "绘制个人 AI 工作流图，标出 AI 执行、人类判断和风险检查点。",
        "homework": "提交期末项目选题和个人 AI 工作流草案。",
        "deliverables": ["创意清单", "展示结构", "个人工作流图", "期末选题"],
        "risk": "学生把工作流画成工具清单，没有任务、判断和复盘。",
    },
    {
        "n": 8,
        "title": "专业场景项目、风险、伦理、版权与学术诚信",
        "subtitle": "期末项目展示与课程复盘",
        "question": "如何展示一个可信、合规、可复盘的专业 AI 工作流？",
        "objectives": ["完成专业场景 AI 工作流展示", "说明风险、伦理、版权和学术诚信", "进行同伴互评", "完成课程复盘"],
        "concepts": ["专业场景", "隐私", "版权", "偏见", "学术诚信", "复盘"],
        "activity": "期末项目展示和互评，重点检查 AI 参与环节、人工修订和风险控制。",
        "homework": "提交最终项目、AI 使用记录、风险说明和课程复盘。",
        "deliverables": ["期末项目", "展示材料", "风险说明", "互评表", "课程复盘"],
        "risk": "学生只展示 AI 生成结果，不说明人工判断、来源核查和风险控制。",
    },
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def course_design() -> str:
    rows = "\n".join(
        f"| 第 {w['n']} 周 | {w['title']} | {w['question']} | {w['activity']} | {', '.join(w['deliverables'])} |"
        for w in WEEKS
    )
    return f"""
# 课程设计书：AI 思维与 Prompt Engineering 实践

## 1. 课程基本信息

| 项目 | 内容 |
| --- | --- |
| 课程名称 | AI 思维与 Prompt Engineering 实践 |
| 课程对象 | 文科、商科、管理、教育、新闻传播、设计、医学、法学、外语等非计算机专业学生 |
| 建议学时 | 8 周，每周 2-3 学时 |
| 课程类型 | 通识实践课 / 项目制 / 任务驱动 |
| 先修要求 | 基础信息检索能力、文字表达能力、常用文档或表格工具基础、基本学术诚信意识 |

## 2. 课程背景

生成式 AI 已经进入学习、调研、写作、分析、办公和创意工作。非计算机专业学生不一定需要训练 Coding Agent，但需要理解如何把 AI 放进自己的专业任务流程。只会复制 Prompt 模板无法形成稳定能力，学生必须学习任务定义、上下文组织、输出评估、人工修订、风险识别和工作流设计。

## 3. 课程定位

本课程不是“Prompt 模板背诵课”，不是 AI 工具测评课，也不是鼓励学生直接提交 AI 输出的捷径课。课程真正训练的是 AI 思维：能把模糊专业任务变成清晰任务包，能组织背景和材料，能判断输出是否可靠，能保留人工责任，能说明伦理、版权、隐私和学术诚信边界。

## 4. 学情分析

学生常见问题有三类：第一，把 AI 当成搜索引擎或权威答案；第二，只会写一句模糊请求，不会提供背景、限制和评价标准；第三，不知道如何核查 AI 输出、引用来源和记录人工修订。

教学策略包括：用坏 Prompt 与好 Prompt 对比建立结构意识；用专业任务练习替代抽象模板；用来源核查、修订记录和风险说明约束作业；用期末项目训练完整个人 AI 工作流。

## 5. 教学目标

### 知识目标

- 理解生成式 AI 的能力边界、概率性输出和幻觉风险。
- 理解 Prompt 的角色、任务、背景、限制、格式和评价标准。
- 理解调研、写作、数据分析、创意展示中 AI 使用的风险。
- 理解版权、隐私、偏见、引用和学术诚信基本要求。

### 能力目标

- 能把模糊任务转化为清晰 AI 任务。
- 能为专业任务组织上下文、材料、样例和输出格式。
- 能核查 AI 输出并进行人工修订。
- 能设计调研、写作、数据分析和展示场景的 AI 工作流。
- 能记录 AI 使用过程、人工判断和风险控制。

### 素养目标

- 不迷信 AI 输出。
- 不把 AI 生成内容直接当作个人成果。
- 有来源核查、版权意识、隐私意识和学术诚信意识。
- 能在专业场景中负责任地使用 AI。

## 6. 课程内容结构

| 周次 | 教学主题 | 核心问题 | 课堂任务 | 交付物 |
| --- | --- | --- | --- | --- |
{rows}

## 7. 教学方法

课程采用问题驱动、案例演示、工具实操、同伴互评、过程记录、Rubric 评价和复盘反思。每周都要求学生保留 Prompt、AI 输出、人工修订和风险说明，避免只提交最终文本。

## 8. 作业体系

- Prompt 设计记录：训练结构化任务表达。
- 调研记录：训练问题生成、资料整理和来源核查。
- 写作修订记录：训练人工修订和学术诚信说明。
- 数据分析记录：训练指标解释、错误检查和风险说明。
- 个人 AI 工作流草案：训练流程化、可复用的专业任务设计。

## 9. 考核方式

| 项目 | 比例 | 评价方式 |
| --- | --- | --- |
| 平时练习 | 35% | 每周课堂任务和短作业，重点看 Prompt 结构、过程记录和人工判断 |
| 阶段作业 | 25% | 调研、写作、数据分析和工作流草案，重点看来源核查、修订和风险意识 |
| 期末项目 | 30% | 面向本专业场景的 AI 工作流，重点看任务设计、过程证据、成果质量和风险说明 |
| 课堂参与与复盘 | 10% | 课堂讨论、同伴互评、失败记录和复盘质量 |

## 10. 期末项目

期末项目题目：设计一个面向本专业场景的 AI 工作流。

交付物包括：任务背景、工作流图、核心 Prompt、AI 输出样例、人工修订记录、来源核查或数据核查说明、风险与伦理说明、最终成果和复盘。评分重点不是输出是否华丽，而是任务是否真实、流程是否可复用、证据是否可审计、风险是否被识别和处理。

## 11. 教学资源

- `syllabus.md`：课程大纲。
- `teaching-calendar.md`：8 周教学日历。
- `assignments/README.md`：作业类型。
- `prompt-library/README.md`：Prompt Library 结构。
- `final-project/requirements.md`：期末项目要求。
- `rubric.md`：课程 A 评分建议。

## 12. 教学风险与对策

| 风险 | 对策 |
| --- | --- |
| 学生直接复制 AI 输出 | 要求提交 Prompt、AI 输出、人工修订和复盘，缺少人工判断不得高分 |
| 学生引用虚假来源 | 第 4 周专门训练来源核查，调研作业必须附来源核查说明 |
| 学生泄露隐私数据 | 教师强调不得上传个人隐私、学校敏感数据和未授权材料 |
| 学生把模板当能力 | 每周使用专业任务改写，要求说明任务目标和评价标准 |
| 学生不会评价输出 | 使用 Rubric 和同伴互评，训练事实、结构、风格和风险四类检查 |
| 学术诚信边界不清 | 明确 AI 可以辅助但必须声明参与环节和人工修改 |
| 工具不可用 | 允许使用学校批准的替代工具，重点评价任务设计和过程记录 |
| 课程被误解为工具演示 | 每周都围绕专业任务、人工修订、风险说明和工作流设计组织 |
"""


def teacher_guide() -> str:
    return """
# 教师授课指南：AI 思维与 Prompt Engineering 实践

## 1. 如何使用本课程仓库

教师先阅读 `README.md`、`syllabus.md` 和 `teaching-calendar.md`，确认 8 周教学节奏。备课时使用 `course-design/course-design.md` 把握课程定位，使用 `lesson-plans/` 安排课堂流程，使用 `teacher-scripts/` 准备讲解话术，使用 `slides/` 中 PPTX 开展授课。

## 2. 上课前教师要检查什么

- 本周主题、课堂活动和提交物。
- 学校允许使用的 AI 平台和账号可用性。
- 是否需要准备替代工具或离线案例。
- 是否有敏感数据、隐私数据或版权材料风险。
- 本周作业 Rubric 和互评要求。

## 3. 学生课前调查建议

建议调查学生专业背景、AI 使用经验、常用工具、是否用过 AI 写作或调研、是否理解引用和学术诚信、是否愿意提交 AI 使用记录供课堂讨论。

## 4. 第一节课前准备

第 1 节课不依赖特定工具。教师准备同一问题的多次 AI 输出、一个明显错误案例、一个来源不可靠案例，以及课程规则：AI 可以用，但必须记录、核查、修订和声明。

## 5. 每节课通用教学流程

| 环节 | 教师动作 | 学生产出 |
| --- | --- | --- |
| 课前检查 | 确认工具、案例、提交要求 | 准备材料 |
| 目标说明 | 说明本周专业任务能力 | 学习目标记录 |
| 概念讲解 | 讲清概念和风险 | 概念笔记 |
| 教师演示 | 展示坏例子和好例子 | 观察记录 |
| 学生实操 | 完成课堂任务 | Prompt、输出、修订 |
| 同伴互评 | 用检查表互评 | 修改建议 |
| 课堂复盘 | 总结失败和风险 | 复盘要点 |
| 课后作业 | 明确提交物和 Rubric | 作业文件 |

## 6. 如何组织课堂任务

课堂任务应来自真实专业场景，例如调研问题生成、文献摘要、新闻改写、商业分析、教学活动设计、法律案例摘要、外语表达修改。任务要小，能够在 15-30 分钟内完成一轮 AI 输出、人工修订和互评。

## 7. 如何批改作业

批改时不要只看最终文本。优先检查：任务目标是否清楚，Prompt 是否结构化，AI 输出是否保留，人工修订是否具体，来源或数据是否核查，风险说明是否真实，是否声明 AI 参与环节。

## 8. 如何处理工具不可用

若 AI 平台不可用，教师可使用预先准备的 AI 输出样例，让学生做评价、修订、来源核查和风险分析。不要要求学生伪造工具使用记录。

## 9. 如何防止学生只复制答案

要求每次作业提交四类证据：原始 Prompt、AI 输出、人工修订、复盘说明。课堂随机抽问学生解释修改原因。对高度相似文本要求补充过程记录或现场说明。

## 10. 如何解释本课程

教师可说明：本课程不是教大家背 Prompt 模板，而是训练“AI 思维”。AI 思维包括把任务说清楚、把上下文给准确、把输出查明白、把风险写出来、把人工判断保留下来。

## 11. 如何引导学生复盘

复盘至少回答：AI 做对了什么，AI 做错了什么，哪些信息影响输出，人工修改了哪些内容，来源或数据如何核查，下一次会怎样改进 Prompt 或流程。

## 12. 如何进入 Pilot

Alpha 阶段建议先让少量学生完成 Week 01-03 和一个调研或写作作业。收集工具可用性、学生误解、作业抄袭、来源核查困难和评分争议，再修订材料后进入 Pilot。
"""


def lesson_plan(w: dict[str, object]) -> str:
    n = int(w["n"])
    return f"""
# 第 {n} 周教案：{w['title']}

## 1. 本讲定位

本讲主题是“{w['title']}”。它服务于课程 A 的核心目标：让非计算机专业学生把 AI 放入真实专业任务，而不是背诵 Prompt 模板或直接复制 AI 输出。

## 2. 学习目标

{chr(10).join(f"- {item}" for item in w['objectives'])}

## 3. 教学重点

- 本周核心问题：{w['question']}
- 关键概念：{', '.join(w['concepts'])}。
- 过程证据：Prompt、AI 输出、人工修订、风险说明。

## 4. 教学难点

- {w['risk']}
- 学生容易只关注最终结果，忽略来源核查、人工修订和复盘。

## 5. 课前准备

教师准备本周案例、坏例子和好例子、课堂任务模板、互评检查表和作业 Rubric。学生准备一个与自己专业相关的小任务。

## 6. 教学流程

| 时间 | 环节 | 内容 | 产出 |
| --- | --- | --- | --- |
| 0-10 分钟 | 导入 | 引出本周核心问题 | 问题记录 |
| 10-30 分钟 | 概念讲解 | 讲解 {', '.join(w['concepts'][:3])} | 概念笔记 |
| 30-50 分钟 | 案例演示 | 对比坏例子和好例子 | 观察记录 |
| 50-80 分钟 | 学生实操 | {w['activity']} | 课堂任务初稿 |
| 80-100 分钟 | 同伴互评 | 按检查表互评 | 修改建议 |
| 100-115 分钟 | 课堂复盘 | 总结 AI 输出问题和人工修订 | 复盘要点 |
| 115-120 分钟 | 作业说明 | 布置课后作业 | 提交清单 |

## 7. 教师讲解内容

教师需要强调：AI 可以辅助完成本周任务，但学生必须保留任务目标、上下文、输出、人工判断和风险说明。任何未经核查的事实、来源、数据和结论都不能直接进入最终作业。

## 8. 演示内容

教师演示一个模糊输入如何导致不可靠输出，再演示结构化输入如何改善结果。演示时要刻意指出 AI 输出中的不确定项、缺少来源、表达过度或风险遗漏。

## 9. 课堂活动

{w['activity']}

活动要求：

- 写出任务目标。
- 给出必要背景。
- 明确输出格式。
- 保存 AI 输出。
- 做人工修订。
- 写出风险或不确定项。

## 10. 课堂提问

- 这个任务中 AI 适合做哪一步？
- 哪一步必须由人判断？
- 输出中哪些内容需要核查？
- 如果结果要提交给老师或真实用户，还需要补什么证据？

## 11. 课后作业

{w['homework']}

提交物：{', '.join(w['deliverables'])}。

## 12. 评价方式

评价重点包括：任务是否清楚、Prompt 是否结构化、AI 输出是否保留、人工修订是否具体、风险说明是否真实、是否遵守版权、隐私和学术诚信要求。
"""


def teacher_script(w: dict[str, object]) -> str:
    n = int(w["n"])
    return f"""
# 第 {n} 周教师讲稿：{w['title']}

## 0-10 分钟：开场与导入

各位同学，今天我们进入第 {n} 周，主题是“{w['title']}”。本节课要解决的问题是：{w['question']}

请大家注意，课程 A 不是让大家记住几个万能 Prompt，也不是鼓励大家把 AI 输出直接交上来。我们训练的是专业任务中的 AI 使用能力：把任务说清楚，把背景给准确，把输出查明白，把人工修订留下来，把风险写出来。

课堂提问：

- 你在自己的专业学习中，什么时候会想到使用 AI？
- 这个任务中，AI 最适合帮助你做哪一步？
- 哪一步不能交给 AI 直接决定？

教师过渡：接下来我们先建立本周的概念框架，再进入案例演示和课堂任务。

## 10-30 分钟：概念讲解

本周的关键概念包括：{', '.join(w['concepts'])}。

教师可以这样讲：

“我们使用 AI 时，第一步不是打开工具输入一句话，而是先判断任务。任务目标是什么？需要哪些材料？输出给谁看？结果怎样算合格？哪些内容必须核查？哪些信息不能上传？如果这些问题没有回答，AI 输出再流畅，也不能说明任务完成。”

围绕本周主题，教师重点解释：

- AI 可以辅助完成哪些子任务。
- AI 输出可能在哪些地方出错。
- 人工修订和核查应该发生在哪些节点。
- 最终作业需要留下哪些过程证据。

课堂提问：

- 如果 AI 输出看起来很专业，但没有来源，你能直接使用吗？
- 如果 AI 生成的文本与你的真实观点不一致，你应该怎样处理？
- 如果任务涉及他人隐私或未公开材料，你能否上传给 AI？

## 30-50 分钟：案例演示

现在我们看一个坏例子。坏例子的共同问题是任务不清、背景不足、评价标准缺失，或者让 AI 直接替代人的判断。

教师演示一个模糊请求：

```text
帮我做一下这个作业。
```

请大家观察，这句话缺少任务目标、专业背景、材料来源、输出格式、评价标准和诚信边界。AI 可能生成一段看似完整的内容，但学生无法证明内容可靠，也无法说明自己做了什么。

现在我们改成结构化请求：

```text
我是一名学生，正在完成一个与本专业相关的小任务。
任务目标：围绕主题形成初步分析。
背景材料：只使用我提供的材料，不编造来源。
输出要求：先列出思路，再给出草稿，最后列出需要人工核查的点。
限制：不要替我做最终结论，不要编造引用，不要使用未提供的数据。
评价标准：内容应准确、结构清楚、风险可见。
```

教师说明：

结构化 Prompt 的价值不是让文字变长，而是让任务边界、输出形式和人工责任更清楚。

## 50-80 分钟：学生实操

现在请大家完成课堂任务：{w['activity']}

请按以下步骤进行：

1. 写出你的专业任务目标。
2. 写出必要背景和材料。
3. 写出限制条件和输出格式。
4. 让 AI 生成第一版输出。
5. 标出你认为需要核查、修改或删除的内容。
6. 做人工修订。
7. 写 3-5 句话说明风险和下一步改进。

教师巡视时可以提醒：

- 不要输入真实隐私数据。
- 不要要求 AI 编造来源。
- 不要只保存最终答案。
- 如果 AI 输出错误，要把错误作为学习材料记录下来。

## 80-100 分钟：同伴互评

请和旁边同学交换任务记录。互评时不要评价“写得好不好看”，而是检查过程是否可靠。

互评问题：

- 任务目标是否清楚？
- 背景和材料是否足够？
- 输出格式是否明确？
- AI 输出中是否有未经核查的事实？
- 人工修订是否具体？
- 风险说明是否真实？

教师点评时可说：

“这个案例的优点是任务目标明确；不足是没有写清楚评价标准。下次可以补充：什么样的输出才算合格，哪些内容必须人工核查。”

## 100-115 分钟：课堂复盘

请大家回到自己的记录，回答三个问题：

第一，AI 在本次任务中最有帮助的是哪一步？

第二，AI 输出中最需要警惕的是什么？

第三，如果下次重做，你会如何修改 Prompt 或工作流？

教师总结：

“学习 Prompt Engineering，不是学习一句万能咒语，而是学习如何把任务、上下文、限制、评价和人工判断组织起来。AI 可以帮我们起草、整理、改写和分析，但最终责任在使用者。”

## 115-120 分钟：作业布置

本周作业是：{w['homework']}

提交时请保留：{', '.join(w['deliverables'])}。

请大家特别注意，作业必须说明 AI 参与了哪些环节，人工修改了哪些内容，哪些事实、来源或数据经过了核查，哪些风险仍然存在。

下节课我们会在本周基础上继续推进，把 AI 使用从单次输出扩展到更稳定的专业任务流程。
"""


def make_markdown_materials() -> None:
    write(BASE / "course-design" / "course-design.md", course_design())
    write(BASE / "teacher-guide" / "teacher-guide.md", teacher_guide())
    for week in WEEKS:
        n = int(week["n"])
        write(BASE / "lesson-plans" / f"week-{n:02d}-lesson-plan.md", lesson_plan(week))
        write(BASE / "teacher-scripts" / f"week-{n:02d}-teacher-script.md", teacher_script(week))


def make_slides_readme() -> None:
    write(
        BASE / "slides" / "README.md",
        """
# 课程 A 完整 PPT 文件

本目录存放课程 A 8 周授课版 PPTX 初版和生成脚本。

## 文件结构

- `pptx/`：生成后的 `.pptx` 文件，每周一个。
- `generate_course_a_pptx.py`：PPT 生成脚本。
- `../tools/generate_course_a_materials.py`：课程 A 教师材料和 PPTX 一键生成脚本。

## 生成方式

在仓库根目录运行：

```bash
/usr/bin/python3 ai-course-system/course-a-prompt-engineering/tools/generate_course_a_materials.py
```

PPTX 是授课初版，重点是完整教学结构、课堂活动、作业和风险提示。后续可以继续做视觉精修。
""",
    )


def prop(name: str, value):
    from com.sun.star.beans import PropertyValue

    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def wait_for_port(host: str, port: int, timeout: float = 15.0) -> None:
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return
        except OSError:
            time.sleep(0.2)
    raise RuntimeError("Timed out waiting for LibreOffice UNO listener")


def generate_pptx() -> None:
    import uno
    from com.sun.star.awt import Point, Size

    host = "127.0.0.1"
    port = 2003
    proc = subprocess.Popen(
        [
            "soffice",
            "--headless",
            "--norestore",
            "--nodefault",
            "--nofirststartwizard",
            f"--accept=socket,host={host},port={port};urp;StarOffice.ComponentContext",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    try:
        wait_for_port(host, port)
        local_ctx = uno.getComponentContext()
        resolver = local_ctx.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_ctx)
        ctx = resolver.resolve(f"uno:socket,host={host},port={port};urp;StarOffice.ComponentContext")
        desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        PPTX_DIR.mkdir(parents=True, exist_ok=True)

        def office_url(path: Path) -> str:
            return uno.systemPathToFileUrl(str(path))

        def clear(page) -> None:
            for index in range(page.getCount() - 1, -1, -1):
                page.remove(page.getByIndex(index))

        def text(page, doc, value: str, x: int, y: int, w: int, h: int, size: float, bold: bool = False) -> None:
            shape = doc.createInstance("com.sun.star.drawing.TextShape")
            shape.Position = Point(x, y)
            shape.Size = Size(w, h)
            page.add(shape)
            shape.Text.String = value
            cursor = shape.Text.createTextCursor()
            cursor.gotoStart(False)
            cursor.gotoEnd(True)
            cursor.CharHeight = size
            cursor.CharFontName = "Noto Sans CJK SC"
            cursor.CharWeight = 150 if bold else 100

        for week in WEEKS:
            n = int(week["n"])
            doc = desktop.loadComponentFromURL("private:factory/simpress", "_blank", 0, ())
            pages = doc.getDrawPages()
            while pages.getCount() > 1:
                pages.remove(pages.getByIndex(pages.getCount() - 1))
            first = pages.getByIndex(0)
            clear(first)
            text(first, doc, f"第 {n} 周：{week['title']}", 1100, 1500, 23000, 1000, 36, True)
            text(first, doc, str(week["subtitle"]), 1300, 2900, 22000, 800, 25)
            text(first, doc, "课程 A：AI 思维与 Prompt Engineering 实践", 1300, 4100, 22000, 700, 18)

            slides = [
                ("本讲目标", week["objectives"]),
                ("核心问题", [str(week["question"])]),
                ("关键概念", list(week["concepts"])),
                ("这节课不是做什么", ["不是背 Prompt 模板", "不是复制 AI 输出", "不是工具功能演示", "不是替代人工判断"]),
                ("教师演示", ["展示模糊输入的问题", "展示结构化输入的改善", "指出事实、来源、风格和风险问题"]),
                ("课堂任务", [str(week["activity"])]),
                ("过程证据", ["原始 Prompt", "AI 输出", "人工修订", "风险说明", "复盘"]),
                ("常见风险", [str(week["risk"])]),
                ("同伴互评", ["任务目标是否清楚", "背景是否足够", "输出是否可核查", "人工修订是否具体"]),
                ("课后作业", [str(week["homework"])]),
                ("提交物", list(week["deliverables"])),
            ]
            for idx, (title, bullets) in enumerate(slides, start=1):
                page = pages.insertNewByIndex(pages.getCount())
                clear(page)
                text(page, doc, title, 900, 500, 23600, 800, 30, True)
                body = "\n".join(f"• {item}" for item in bullets)
                text(page, doc, body, 1300, 1600, 22000, 4800, 24)
                text(page, doc, f"{idx}/{len(slides)}", 22500, 6500, 2000, 400, 12)

            out = PPTX_DIR / f"week-{n:02d}-course-a-{slug(str(week['title']))}.pptx"
            doc.storeAsURL(
                office_url(out),
                (prop("FilterName", "Impress MS PowerPoint 2007 XML"), prop("Overwrite", True)),
            )
            doc.close(True)
            print(f"generated {out.relative_to(BASE)}")
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


def slug(value: str) -> str:
    mapping = {
        "生成式 AI 基础": "generative-ai-basics",
        "Prompt 基本结构": "prompt-structure",
        "任务拆解与上下文表达": "task-context",
        "AI 辅助调研": "ai-research",
        "AI 辅助写作": "ai-writing",
        "AI 辅助数据分析": "ai-data-analysis",
        "AI 辅助创意与展示、个人 AI 工作流": "creative-presentation-workflow",
        "专业场景项目、风险、伦理、版权与学术诚信": "final-project-ethics",
    }
    return mapping.get(value, "deck")


def main() -> int:
    make_markdown_materials()
    make_slides_readme()
    generate_pptx()
    return 0


if __name__ == "__main__":
    sys.exit(main())

