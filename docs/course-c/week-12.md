# Week 12：人力资源招聘、培训与绩效流程

> HR 场景里，AI 可以帮助起草 JD、整理筛选标准、生成面试问题和检查偏见风险，但不能决定录用、解雇、薪酬或绩效结果。星河咖啡设备本周建立一个公平、可审计的人力资源助理。

<ChapterIntroduction duration="2-3 课时" output="JD 草稿 + 筛选量表 + 面试题库 + 偏见/隐私审查" prerequisite="完成 Week 11 税务合规留档" :tags="['人力资源', '招聘', '培训', '绩效考核']">

你会让 AI 支持 draft、review、classify 和 prepare checklists，但 HR 负责人必须确认岗位要求、候选人筛选、录用决定、薪酬福利和绩效结论。

</ChapterIntroduction>

<StepBar :active="11" :items="[
  { title: '① 岗位定义', description: '职责和必要条件' },
  { title: '② 筛选量表', description: '标准公开可解释' },
  { title: '③ 面试题库', description: '问题与岗位相关' },
  { title: '④ 偏见隐私审查', description: '不收集无关敏感信息' },
  { title: '⑤ 人工决策', description: 'HR 和用人经理确认' }
]" />

## 业务情境

星河咖啡设备准备招聘“区域渠道运营经理”，负责渠道开拓、客户维护、销售协同和运营数据复盘。HR 助理要把岗位说明、筛选量表、面试题库和入职培训计划整理成可复用包。

本周要处理的不是“让 AI 招人”，而是“让 HR 流程更清楚”：

| 模块 | AI 支持 | AI 不能直接做 |
|---|---|---|
| JD 草稿 | draft 职责、要求和工作场景 | 决定岗位最终等级和薪酬 |
| 筛选量表 | organize 标准和证据 | 录用或淘汰候选人 |
| 面试题库 | generate questions | 询问歧视性或隐私问题 |
| 培训计划 | summarize 入职学习路径 | 认定员工是否胜任 |
| 绩效材料 | prepare checklists | 做最终绩效、奖惩或解雇决定 |

## 角色边界

| 角色 | AI 可以支持 | AI 不能直接做 |
|---|---|---|
| HR 助理 | draft JD、classify 能力项、review 偏见词 | 决定录用、解雇、薪酬和绩效 |
| 用人经理 | 确认岗位能力和面试评价 | 让 AI 排名候选人并直接录用 |
| HR 负责人 | 确认流程、公平性和隐私边界 | 省略人工审批 |
| 法务/合规 | review 劳动合规和反歧视风险 | 被 AI 草稿替代 |

必须由负责人或专业人员确认：岗位等级、薪酬福利、录用/淘汰、绩效结果、纪律处分、解雇、培训认证和劳动合规判断。

## 输入资料

- [sample-hr.csv](/course-c/examples/sample-hr.csv)。
- fictional 岗位需求、用人部门访谈纪要和培训资源清单。
- 公司招聘制度、面试流程、薪酬福利政策或教师提供的 sample 规则。
- DOL official employer/labor materials 和 EEOC prohibited employment practices 作为公平招聘边界示例。
- [合规检查清单](/course-c/templates/compliance-checklist)。

不要上传真实简历、身份证、联系方式、薪资、绩效、健康、家庭、宗教、政治观点或其他敏感个人信息。

## AI 工作流

### 第一步：JD 草稿

```text
请为“区域渠道运营经理”生成 JD 草稿。
字段：岗位目标、主要职责、必要条件、加分条件、协作对象、工作成果、不能承诺的内容。
要求条件必须与岗位相关，不得包含年龄、性别、婚育、户籍、健康等无关限制。
```

### 第二步：筛选量表

```text
请把岗位要求转成筛选量表。
字段：能力项、证据、评分说明、面试验证方式、偏见风险、需要人工确认的问题。
不要对候选人做最终录用或淘汰决定。
```

### 第三步：面试题库

```text
请生成结构化面试题库。
分类：渠道开拓、客户维护、数据分析、跨部门协作、合规意识。
每题写评价要点和禁止追问。
避免询问隐私、受保护特征或与岗位无关的信息。
```

### 第四步：培训与绩效流程

```text
请起草 30-60-90 天培训和绩效跟踪流程。
输出：学习任务、辅导人、证据、复盘问题、需要用人经理确认的节点。
不要给出最终绩效评级或奖惩建议。
```

## 工具与应用整合

| 工具 | 用途 | 证据 |
|---|---|---|
| 文档工具 | JD、面试题库和培训计划 | 版本记录 |
| 表格工具 | 筛选量表和培训跟踪 | 字段表 |
| ATS 或 HR 系统 | 流程字段参考 | read-only 截图或字段清单 |
| AI 工具 | draft、review、classify、prepare checklists | Prompt 和人工修改 |
| 审计日志 | 记录偏见审查和审批 | [审计日志模板](/course-c/templates/audit-log) |

课堂练习不连接真实 ATS，不处理真实候选人资料，不让 AI 自动筛人或排序。

## Reference 使用

### 实现来源

- HRIS、ATS、文档和表格工具说明：用于理解字段、流程和导出方式。
- [sample-hr.csv](/course-c/examples/sample-hr.csv)：作为 fictional / sample HR 数据。
- [提示词库模板](/course-c/templates/prompt-library)：用于保存 JD、筛选和面试提示词。
- [合规检查清单](/course-c/templates/compliance-checklist)：用于执行四门审查。

### 权威领域来源

- U.S. Department of Labor official employer/labor materials 可作为劳动流程边界示例。
- EEOC prohibited employment practices materials 可作为公平招聘和反歧视边界示例。
- HR management 教材、结构化面试研究和工业组织心理学资料可支持胜任力模型、结构化面试和培训设计。
- 实际地区劳动法、公司制度和法务/HR 专业意见必须优先于示例来源。

## 合规审查

| 门 | 检查问题 |
|---|---|
| 数据门 | 是否只使用 sample、虚构、公开或脱敏 HR 数据？是否排除敏感个人信息？ |
| 来源门 | 岗位条件、筛选标准和面试题是否有岗位依据、政策或权威来源？ |
| 人类门 | 录用、薪酬、绩效、解雇和劳动合规是否由 HR/用人经理/法务确认？ |
| 审计门 | 是否保存 Prompt、AI 输出、偏见审查、人工修改和审批记录？ |

AI 可以支持 draft、analyze、organize、compare、review、summarize、classify、generate questions、prepare checklists、record workflow evidence。AI 不能直接做录用、淘汰、解雇、薪酬福利、绩效评级、纪律处分或劳动合规最终判断。

## 助理包更新

更新人力资源助理：

- 新增工作流：岗位需求 -> JD 草稿 -> 筛选量表 -> 面试题库 -> 偏见/隐私审查 -> 人工审批。
- 新增提示词：JD 草稿、结构化筛选、面试题库、培训计划、偏见词审查。
- 新增模板：筛选量表、面试评价表、培训跟踪表、HR 审批记录。
- 新增审计规则：凡涉及录用、解雇、薪酬、绩效和敏感个人信息，必须停止并转人工。

## 验收标准

- JD 草稿只包含与岗位相关的职责和条件。
- 筛选量表写清能力项、证据、评分说明和偏见风险。
- 面试题库包含禁止追问和隐私边界。
- 至少引用 1 个 HR、劳动、公平招聘、结构化面试或培训发展权威领域来源。
- 没有让 AI 直接做录用、薪酬、绩效或解雇决定。
