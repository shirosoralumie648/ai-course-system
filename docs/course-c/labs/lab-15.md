# Lab 15：read-only / mock-first 企业连接计划

<ChapterIntroduction duration="约 2 小时" output="连接设计包 + 权限矩阵 + mock 数据集 + 审批与 audit log" prerequisite="完成 Week 15" :tags="['API', 'MCP', '权限矩阵', 'mock-first']">

本实验不要求你做真实连接。你要交付的是一份企业连接计划，证明这个 AI 工作流在进入真实系统之前已经完成数据、权限、审批和审计设计。

</ChapterIntroduction>

## 实验目标

- 定义一个业务 AI 工作流的连接边界。
- 设计 source-system inventory、data classification 和 field map。
- 建立 read-only / mock-first / least privilege 权限矩阵。
- 输出 human approval、secret hygiene、audit log 和 stop/rollback rules。

## 实验任务

围绕“客户会议纪要 -> CRM 跟进任务 -> 管理仪表盘”设计一份企业连接计划。

必须交付：

| 产物 | 要求 |
|---|---|
| 工作流卡 | 业务目标、触发条件、输入、输出、涉及系统、停止条件 |
| 系统清单 | CRM、文档、表格、BI、日志或其他来源系统 |
| 数据分类 | public、internal、sensitive、prohibited，并写处理规则 |
| 字段映射 | 来源字段、输出字段、负责人、敏感度、是否进入 mock |
| 权限矩阵 | 默认 read-only，写权限和 admin 权限禁止或需正式审批 |
| mock 数据集 | 至少 5 条 synthetic/mock 记录 |
| 审批与 audit log | 数据门、来源门、人类门、审计门都有证据 |
| 停止/回滚规则 | 什么时候撤销密钥、停止连接、回到人工流程 |

## 输入材料

- [快速接入教程](/shared/quick-start)。
- [合规检查清单](/course-c/templates/compliance-checklist)。
- [工作流 SOP 模板](/course-c/templates/workflow-sop)。
- [审计日志模板](/course-c/templates/audit-log)。
- fictional CRM 字段、会议纪要、BI 指标和 mock 客户记录。

不要提交真实 API Key、OAuth token、`.env`、客户资料、员工资料、财务数据、税务记录、合同、生产导出、管理员截图或公司内部系统地址。

## 操作步骤

1. 写出业务工作流卡，说明为什么需要 AI、谁负责、什么时候停止。
2. 建立 source-system inventory，列出每个系统的数据类型和系统负责人。
3. 做 data classification，把字段分成 public、internal、sensitive、prohibited。
4. 建立 field map，标注是否允许进入 mock 数据集。
5. 设计 permission matrix，默认 read-only 和 least privilege；write/admin 标为禁止或需正式审批。
6. 写 secret hygiene：环境变量或密钥管理、唯一密钥、过期、轮换、撤销、禁止提交仓库。
7. 准备至少 5 条 synthetic/mock 记录，证明可以先 mock-first 测试。
8. 用四门模型记录脱敏、来源、human approval 和 audit log。
9. 更新岗位 AI 助理包，加入企业连接 checklist、SOP 或权限-review prompt。

## 提交要求

- `enterprise-workflow-card.md`。
- `source-system-inventory.md`。
- `data-classification-and-field-map.md`。
- `permission-matrix.md`。
- `mock-dataset.csv` 或 `mock-dataset.md`。
- `secret-hygiene-checklist.md`。
- `approval-and-audit-log.md`。
- `stop-rollback-rules.md`。
- 岗位 AI 助理包更新说明。

## 验收标准

- 连接计划明确 read-only、mock-first、least privilege、secret hygiene、no production writes、human approval 和 audit log。
- 权限矩阵没有默认 write/admin 权限。
- mock 数据集不包含真实客户、员工、财务、税务、合同、凭证或生产系统数据。
- 数据门、来源门、人类门、审计门都有记录。
- 岗位 AI 助理包新增可复用的企业连接检查清单、SOP 或权限-review prompt。

## 评分标准

| 维度 | 分值 | 说明 |
|---|---:|---|
| 工作流与系统清单 | 20 | 业务目标、系统、负责人和停止条件清楚 |
| 数据与字段设计 | 20 | 分类、字段映射和 mock 范围完整 |
| 权限与密钥治理 | 25 | read-only、least privilege、secret hygiene 清楚 |
| 审批与审计 | 20 | human approval 和 audit log 可追溯 |
| 助理包更新 | 15 | 企业连接流程可复用 |
