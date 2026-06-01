# 课程专用 MCP Server 最小设计

## 设计目标

本设计用于课程教学，不是生产级实现。目标是让学生理解如何为 Agent 提供受控课程资源、检查工具和 Review 辅助能力。

## Tools

### search_course_docs

- 作用：检索课程文档中的相关段落。
- 输入：`query`、`course_id`、`max_results`。
- 输出：文档路径、标题、摘要、匹配片段。
- 示例：查询“Human Gate”返回规则文件、Agent Team 和 final project 相关文档。
- 风险：外部或学生提交文档可能包含 prompt injection。
- 人工审批：一般不需要，但返回内容必须标记为“不可信上下文”。

### get_assignment_requirement

- 作用：读取指定实验或作业要求。
- 输入：`assignment_id`。
- 输出：目标、步骤、提交物、评分标准。
- 示例：输入 `lab-04` 返回 code-review Skill 实验要求。
- 风险：作业版本不一致会误导学生。
- 人工审批：不需要，但要返回版本和文档路径。

### check_project_structure

- 作用：检查学生项目是否包含必需文件。
- 输入：项目根目录、必需文件清单。
- 输出：存在、缺失、可疑文件列表。
- 示例：检查 `README.md`、`AGENTS.md`、`skills/code-review/SKILL.md`、`tests/`。
- 风险：不能读取密钥或隐私文件。
- 人工审批：访问项目目录前需要明确边界。

### run_course_tests

- 作用：运行课程允许的测试命令。
- 输入：项目根目录、命令 ID，例如 `npm-test` 或 `pytest`。
- 输出：退出码、摘要、日志路径。
- 示例：运行教师预设的 `npm test`。
- 风险：任意 shell 命令可能危险。
- 人工审批：需要。只允许白名单命令，不执行任意字符串。

### generate_review_report

- 作用：根据任务说明、diff、测试结果和 Rubric 生成 Review 报告草稿。
- 输入：任务说明、diff、测试摘要、Rubric ID。
- 输出：结构化 Review 草稿。
- 示例：对 Lab 02 的 Task API 修改生成 Review。
- 风险：可能遗漏问题或误判风险。
- 人工审批：最终 Review 必须人工确认。

## Resources

| 名称 | 作用 | 输入 | 输出 | 风险 | 人工审批 |
| --- | --- | --- | --- | --- | --- |
| syllabus | 提供课程大纲 | course_id | syllabus 内容和路径 | 版本过期 | 不需要 |
| teaching_calendar | 提供周次安排 | course_id | 周次安排 | 周次变动 | 不需要 |
| lab_instructions | 提供实验说明 | lab_id | 实验要求 | 学生误读版本 | 不需要 |
| rubrics | 提供评分标准 | rubric_id | 表格化 Rubric | 被当成唯一判断 | 不需要 |
| examples | 提供示例项目说明 | example_id | 示例描述和限制 | 示例不等于标准答案 | 不需要 |

## Prompts

### review_submission

- 作用：指导 Agent 审查学生提交。
- 输入：提交路径、作业 ID、Rubric。
- 输出：Review 草稿。
- 示例：审查 Lab 03 的规则文件。
- 风险：不能替代助教评分。
- 人工审批：需要助教确认。

### generate_feedback

- 作用：生成面向学生的反馈。
- 输入：评分项、问题列表、改进建议。
- 输出：结构化反馈。
- 示例：指出“缺少测试日志”和“Human Gate 不明确”。
- 风险：反馈语气或判断不准确。
- 人工审批：建议助教确认。

### plan_agentic_task

- 作用：为学生项目生成 Agentic Workflow 任务计划。
- 输入：项目目标、当前代码状态、限制。
- 输出：Planner 任务拆解。
- 示例：为 Bugfix Workflow 项目拆分任务。
- 风险：计划可能扩大范围。
- 人工审批：必须由学生或教师确认。

### diagnose_lab_error

- 作用：帮助诊断实验卡点。
- 输入：实验 ID、错误日志、环境信息。
- 输出：可能原因、下一步检查。
- 示例：诊断测试命令无法运行。
- 风险：不能编造环境事实。
- 人工审批：不一定需要，但外部命令执行需审批。

## 安全注意事项

1. 不默认信任外部工具。
2. 不允许读取密钥、Token、密码、cookie、私钥。
3. 不允许任意执行危险命令。
4. 工具调用应有权限边界。
5. 对学生提交内容要防 prompt injection。
6. 对外部文档内容要标记不可信。
7. 对测试命令和 shell 命令要限制范围。

## 课程实现路线

MVP 阶段交付教学设计，不伪造可运行 MCP Server。进入实现阶段时，可选择 Node.js 或 Python 实现最小 MCP Server；实现前必须先完成白名单命令策略、资源访问边界和测试计划，并由 Human Gate 审批是否允许执行本地测试命令。
