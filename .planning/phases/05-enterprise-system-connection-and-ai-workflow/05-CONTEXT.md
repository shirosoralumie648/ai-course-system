# Phase 5: Enterprise System Connection And AI Workflow - Context

**Gathered:** 2026-06-06
**Status:** Ready for planning
**Mode:** auto-selected recommended defaults

<domain>
## Phase Boundary

Phase 5 creates Course C Week 15 and Lab 15. It teaches business learners how to
plan safe Skills, API/MCP, and enterprise-system connections for Codex/Claude
Code style agents without turning the course into a backend engineering module.

The deliverable is a connection design packet: workflow trigger, source system,
data classification, read-only/mock-first test plan, permission matrix, field
map, human approval path, audit log, rollback/stop rules, and implementation
source list.

Phase 5 does not create Week 16 or Lab 16, final project updates, full reference
catalog updates, production connectors, live API services, real credentials, or
write-enabled enterprise integrations.

</domain>

<decisions>
## Implementation Decisions

### Page Set And Navigation

- **D-01:** Create exactly `docs/course-c/week-15.md` and
  `docs/course-c/labs/lab-15.md`.
- **D-02:** Add Week/Lab 15 to the Course C sidebar only after files exist. Do
  not add Week/Lab 16 in Phase 5.
- **D-03:** Keep content as static Markdown using existing Course C components
  only. Do not add dependencies, Vue components, backend services, or live
  connectors.
- **D-04:** Keep Week 15 accessible to business learners. Code snippets may be
  illustrative, but the required output is a design and governance packet, not
  a working integration.

### Week 15 Learning Contract

- **D-05:** Week 15 must explain Skills, AGENTS/project instructions, API
  connection planning, MCP client/server/tool/resource concepts, permission
  boundaries, and audit process.
- **D-06:** Week 15 must distinguish implementation sources from authoritative
  governance/security sources.
- **D-07:** Week 15 must use the same Course C rhythm: business situation, role
  boundary, inputs, AI workflow, tool/application integration, Reference use,
  compliance review, assistant-pack update, and acceptance criteria.
- **D-08:** Week 15 must state AI can support drafting, organizing, comparing,
  reviewing, summarizing, generating questions, preparing checklists, and
  recording workflow evidence.
- **D-09:** Week 15 must state AI cannot directly create production write
  access, store secrets in prompts/repos, bypass approvals, change live CRM/ERP/
  finance/tax/OA systems, sync personal/sensitive data, or approve permissions.

### Lab 15 Evidence Contract

- **D-10:** Lab 15 asks students to produce a read-only/mock-first connection
  plan, not a live connector.
- **D-11:** Lab 15 must include a workflow card, source-system inventory, data
  classification, field map, permission matrix, mock dataset, approval record,
  audit log, and rollback/stop rules.
- **D-12:** Lab 15 must require redaction/source checking, human approval, and
  audit logging.
- **D-13:** Lab 15 must update the role AI assistant pack with a reusable
  enterprise-connection checklist, SOP, or permission-review prompt.

### Safety And Governance Rules

- **D-14:** Use read-only, mock-first, least-privilege, permissioned, auditable
  integration framing as hard constraints.
- **D-15:** No production writes, no real credentials, no personal data, no real
  customer/employee/financial/tax/legal records, no live OAuth tokens, and no
  autonomous business-system changes.
- **D-16:** Secret hygiene requires environment variables or secret managers,
  unique keys, no client-side exposure, no repository commits, and rotation/
  revocation planning.
- **D-17:** Any connector with side effects, external network access, private
  data access, or elevated permissions must require explicit human approval and
  audit evidence.
- **D-18:** MCP and agent tools are treated as capability surfaces with prompt
  injection, excessive agency, sensitive information disclosure, and confused
  deputy risks.

### Source Requirements

- **D-19:** Implementation sources should include the existing
  `/shared/quick-start` page, OpenAI/Codex official docs for Skills, AGENTS,
  MCP, approvals, sandboxing, permissions, and API key safety; Claude Code MCP
  docs; and the MCP specification/docs.
- **D-20:** Authoritative domain sources should include NIST SP 800-53 access
  control/audit/control-family framing, OWASP Top 10 for LLM Applications,
  ISO/IEC 27001/27002 or CIS Controls categories, SOC 2 trust-services style
  controls, privacy/security laws or company policies where relevant, and
  internal-control/audit references.
- **D-21:** Official sources are examples and categories, not legal compliance
  advice. Learners must use their organization, jurisdiction, security team,
  data-owner, and system-owner rules for real work.

### Planning Shape

- **D-22:** Split Phase 5 into two plans:
  1. Week/Lab 15 enterprise connection content.
  2. Sidebar exposure and phase verification.
- **D-23:** Keep each slice independently verifiable with artifact, source,
  prohibited-action, navigation, and build checks.

### the agent's Discretion

- Exact fictional source systems and sample fields are up to the implementation
  agent if the mock/read-only boundary is preserved.
- Exact source examples can vary by page, but both implementation and
  governance/security sources must appear.

</decisions>

<canonical_refs>
## Canonical References

### Project And Prior Phase Context

- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/phases/02-compliance-templates-and-synthetic-examples/02-VERIFICATION.md`
- `.planning/phases/04-high-risk-business-weeks-08-14-and-labs/04-VERIFICATION.md`

### Course Assets

- `docs/shared/quick-start.md`
- `docs/shared/claude-code.md`
- `docs/shared/codex-cli.md`
- `docs/course-c/reference-integration.md`
- `docs/course-c/templates/compliance-checklist.md`
- `docs/course-c/templates/audit-log.md`
- `docs/course-c/templates/workflow-sop.md`
- `docs/course-c/templates/prompt-library.md`

### Official/Authoritative Source Anchors

- OpenAI Codex official manual sections for Agent Skills, AGENTS.md, MCP,
  approvals/security, sandboxing, permissions, and plugins.
- OpenAI API key safety and production best-practices docs.
- Claude Code official MCP documentation.
- Model Context Protocol official docs and security best practices.
- NIST SP 800-53 Rev. 5 for access control, audit/accountability, risk, and
  control-family framing.
- OWASP Top 10 for LLM Applications for prompt injection, sensitive information
  disclosure, excessive agency, insecure plugin/tool design, and overreliance
  risk categories.

</canonical_refs>

<code_context>
## Existing Code Insights

- `docs/course-c/week-01.md` through `week-14.md` and
  `docs/course-c/labs/lab-01.md` through `lab-14.md` already exist.
- Course C sidebar currently exposes Week/Lab 01-14. Phase 5 should add only
  Week/Lab 15.
- Shared quick-start pages already explain API key, BaseURL, model ID, and
  common tool connection basics.
- All content should remain static Markdown and build with
  `cd docs && BASE=/ai-course-system/ npm run build`.

</code_context>

<specifics>
## Specific Ideas

Recommended Week/Lab 15 output:

| Artifact | Purpose |
|---|---|
| Workflow card | Describe the business workflow and why AI is involved |
| Source-system inventory | CRM, spreadsheet, OA, finance, HR, docs, or ticket system |
| Data classification | Public, internal, sensitive, prohibited |
| Field map | Source field, destination/output field, owner, sensitivity |
| Permission matrix | Read/list/search/write/admin; default to read-only |
| Mock dataset | Synthetic records used before any real system access |
| Approval record | Data owner, system owner, security/admin, business owner |
| Audit log | Prompt, input, output, tool calls, human edits, final approval |
| Rollback/stop rules | When to stop, revoke access, rotate keys, or return to manual work |

Required phrases:

- `read-only`
- `mock-first`
- `least privilege`
- `secret hygiene`
- `no production writes`
- `human approval`
- `audit log`
- `数据门`
- `来源门`
- `人类门`
- `审计门`

</specifics>

<deferred>
## Deferred Ideas

- Week 16 / Lab 16 final defense and project package.
- Full reference catalog consolidation.
- Live CRM/ERP/finance/tax/OA integrations.
- Production MCP server implementation.
- Real OAuth app registration or real enterprise credentials.
- Organization-specific legal/security/compliance approval.

</deferred>

---

*Phase: 05-enterprise-system-connection-and-ai-workflow*
*Context gathered: 2026-06-06*
