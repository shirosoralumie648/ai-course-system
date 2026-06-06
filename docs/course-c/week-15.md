# Week 15：企业系统连接与 AI 工作流治理

> 企业系统连接不是“把 AI 接上所有系统”。正确做法是先把业务流程、数据范围、权限、审批、审计和停止规则写清楚，再决定是否需要 API、MCP、Skill 或人工导入。星河咖啡设备本周设计一份 read-only、mock-first 的企业连接计划。

<ChapterIntroduction duration="2-3 课时" output="企业连接设计包 + 权限矩阵 + mock 数据集 + 审计与停止规则" prerequisite="完成 Week 14 行政治理支持" :tags="['企业系统连接', 'API', 'MCP', 'Skills', '权限治理']">

你会让 AI 帮你 draft 连接计划、organize 字段表、compare 权限、review 风险和 record workflow evidence，但不会让 AI 直接获得生产写权限、保存密钥、绕过审批或修改真实系统。

</ChapterIntroduction>

<StepBar :active="14" :items="[
  { title: '① 选流程', description: '先定义业务问题' },
  { title: '② 盘系统', description: '列来源系统和数据类型' },
  { title: '③ 做权限矩阵', description: '默认 read-only 和 least privilege' },
  { title: '④ mock-first', description: '先用合成数据验证' },
  { title: '⑤ 审计停止', description: '人类审批和回滚规则' }
]" />

## 业务情境

星河咖啡设备希望把“客户会议纪要 -> CRM 跟进任务 -> 管理仪表盘”做成半自动工作流。业务团队提出三个想法：

| 想法 | 听起来方便 | 真实风险 |
|---|---|---|
| 让 AI 直接读 CRM | 可以自动整理客户状态 | 可能读取客户隐私和商业机密 |
| 让 AI 写入跟进任务 | 减少销售运营手工录入 | 可能写错客户、误触发流程 |
| 让 AI 连接 BI 仪表盘 | 快速生成管理说明 | 可能扩大数据访问范围 |

本周的任务不是马上接入系统，而是先做企业连接设计包：工作流卡、系统清单、数据分类、字段映射、权限矩阵、mock 数据集、审批记录、audit log 和停止规则。

## 角色边界

| 角色 | AI 可以支持 | AI 不能直接做 |
|---|---|---|
| 企业连接助理 | draft 工作流卡、organize 字段表、prepare checklists | 创建生产写权限或修改真实系统 |
| 业务负责人 | 确认流程价值、输出边界和人工检查点 | 让 AI 绕过流程审批 |
| 系统负责人 | review API/MCP 权限、日志和回滚规则 | 把管理员权限交给 AI |
| 安全/合规负责人 | review secret hygiene、least privilege 和 audit log | 被 AI 草稿替代 |

必须由负责人或专业人员确认：数据范围、系统权限、API Key/OAuth 申请、MCP 工具能力、网络访问、生产变更、日志留存、回滚方案和上线审批。

## 输入资料

- [快速接入教程](/shared/quick-start)：用于理解 BaseURL、API Key、模型 ID 和工具配置。
- [Codex CLI 安装指南](/shared/codex-cli) 和 [Claude Code 安装指南](/shared/claude-code)。
- [合规检查清单](/course-c/templates/compliance-checklist)。
- [工作流 SOP 模板](/course-c/templates/workflow-sop)。
- [审计日志模板](/course-c/templates/audit-log)。
- fictional CRM 字段表、会议纪要样例、仪表盘字段和 mock 客户记录。

不要上传真实 API Key、OAuth token、`.env` 文件、客户资料、员工资料、财务数据、合同、税务记录、生产系统导出或管理员截图。

## AI 工作流

### 第一步：企业连接工作流卡

```text
请为“客户会议纪要 -> CRM 跟进任务 -> 管理仪表盘”生成企业连接工作流卡。
字段：
- 业务目标
- 触发条件
- 输入资料
- 输出资料
- 涉及系统
- 数据分类
- 人工审批点
- 不接入的范围
- 停止条件
要求默认 read-only、mock-first、no production writes。
```

### 第二步：系统与字段清单

```text
请把以下 fictional 系统整理成来源系统清单和字段映射表。
系统：CRM、文档、表格、BI 仪表盘。
字段：来源系统、字段名、业务含义、数据分类、字段负责人、是否进入 mock 数据集、是否允许 AI 读取、是否允许写入。
默认不允许写入。
```

### 第三步：权限矩阵

```text
请生成权限矩阵。
行：CRM、文档库、表格、BI、日志系统、API/MCP 工具。
列：无访问、read-only、search/list、draft output、write、admin。
要求：
1. 默认 least privilege。
2. production write/admin 设为禁止。
3. 每个权限写审批人、理由、到期时间和审计证据。
4. 标出需要 human approval 的动作。
```

### 第四步：secret hygiene 和 audit log

```text
请生成企业连接 secret hygiene 和 audit log 检查清单。
包含：环境变量或密钥管理、唯一密钥、最小权限、过期时间、轮换、撤销、日志字段、异常停止、负责人审批。
不要要求学生粘贴真实密钥。
```

## 工具与应用整合

| 工具/概念 | 用途 | 证据 |
|---|---|---|
| Skills | 把可复用工作流写成角色助理能力 | SKILL 草案或助理包条目 |
| AGENTS / 项目指令 | 记录仓库或项目级工作规则 | 指令片段和适用范围 |
| API | 规划模型或系统调用边界 | BaseURL、endpoint、权限和测试记录 |
| MCP | 规划工具、资源、提示词和外部系统能力 | server/client/tool/resource 清单 |
| 权限矩阵 | 限制 read-only、write、admin 范围 | 审批记录 |
| audit log | 追溯输入、输出、工具调用和人工修改 | [审计日志模板](/course-c/templates/audit-log) |

Week 15 只要求设计和 mock 验证。任何真实 API/MCP、CRM、ERP、财务、税务、HR、OA 或 BI 系统接入，都必须由系统负责人和安全/合规负责人批准。

## Reference 使用

### 实现来源

- [快速接入教程](/shared/quick-start)：用于理解 API Key、BaseURL、模型 ID 和常见工具配置字段。
- OpenAI Codex official docs：Skills、AGENTS.md、MCP、approvals/security、sandboxing、permissions 和 plugin/MCP 配置，用来理解 agent 能力边界和本地配置方式。
- OpenAI API key safety / production best-practices docs：用于 secret hygiene、环境变量、唯一密钥、监控、限额、测试/生产隔离和密钥轮换。
- Claude Code official MCP docs：用于理解 Claude Code 如何连接、查看和认证 MCP server。
- Model Context Protocol official docs：用于理解 MCP client/server/tool/resource、transport、authorization 和 security best practices。

### 权威领域来源

- NIST SP 800-53 Rev. 5 的 access control、audit/accountability 和 risk/control family 可支持权限矩阵、日志和控制点设计。
- OWASP Top 10 for LLM Applications 可支持 prompt injection、sensitive information disclosure、excessive agency、insecure tool/plugin design 和 overreliance 风险检查。
- ISO/IEC 27001/27002、CIS Controls、SOC 2 trust-services criteria、隐私法规、公司安全政策和内控审计资料可支持真实企业审批和证据要求。
- 组织所在地法规、系统所有者规则、数据所有者规则和安全团队要求必须优先于课堂示例。

## 合规审查

| 门 | 检查问题 |
|---|---|
| 数据门 | 是否只使用 mock、fictional、公开或脱敏数据？是否排除真实密钥、客户、员工、财务、税务和合同资料？ |
| 来源门 | API/MCP/Skill 做法是否来自官方实现来源？权限和审计是否有治理/安全来源支撑？ |
| 人类门 | 数据范围、系统权限、生产接入、网络访问和上线审批是否由业务/系统/安全负责人确认？ |
| 审计门 | 是否保存工作流卡、字段表、权限矩阵、mock 数据、Prompt、AI 输出、人工修改和审批记录？ |

AI 可以支持 draft、analyze、organize、compare、review、summarize、classify、generate questions、prepare checklists、record workflow evidence。AI 不能直接创建生产写权限、保存真实密钥、绕过审批、连接真实敏感数据、修改 CRM/ERP/财务/税务/HR/OA 系统、提交系统变更或扩大权限。

## 助理包更新

更新企业连接助理：

- 新增工作流：业务流程 -> 系统清单 -> 数据分类 -> 字段映射 -> 权限矩阵 -> mock-first 测试 -> 审批审计。
- 新增提示词：企业连接工作流卡、字段映射表、权限矩阵、secret hygiene、audit log、停止规则。
- 新增模板：连接设计包、MCP/API 能力清单、权限申请记录、回滚/停止规则。
- 新增审计规则：凡涉及真实凭据、生产数据、写权限、管理员权限、网络放通和系统变更，必须停止并转系统/安全负责人。

## 验收标准

- 企业连接设计包包含工作流卡、系统清单、数据分类、字段映射、权限矩阵、mock 数据集、审批记录、audit log 和停止规则。
- 权限矩阵默认 read-only、mock-first、least privilege，并明确 no production writes。
- secret hygiene 写清环境变量或密钥管理、唯一密钥、过期、轮换、撤销和禁止提交仓库。
- 至少引用 1 个官方实现来源和 1 个安全/治理权威领域来源。
- 没有要求学生连接真实系统、提交真实密钥、使用真实敏感数据或给 AI 生产写权限。
