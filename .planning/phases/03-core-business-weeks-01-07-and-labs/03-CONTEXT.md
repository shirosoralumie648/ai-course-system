# Phase 3: Core Business Weeks 01-07 And Labs - Context

**Gathered:** 2026-06-06
**Status:** Ready for planning
**Mode:** auto-selected recommended defaults

<domain>
## Phase Boundary

Phase 3 creates the Course C core business operating spine: Week 01 through Week
07 pages and Lab 01 through Lab 07 pages. It covers company setup, market
research, product positioning, brand promotion, sales leads, customer
relationship maintenance, and data dashboards.

Phase 3 must use the reusable templates, synthetic examples, four-gate
compliance fields, and professional-source rules created in Phase 2. It must not
create Week 08-16, Lab 08-16, high-risk investment/finance/tax/HR/legal/admin
scenario pages, or live enterprise API/MCP integrations. Those remain Phase 4,
Phase 5, and Phase 6 work.

The roadmap maps `CURR-01` and `LAB-01` broadly to all 16 weeks/labs, but Phase
3 is responsible only for the 01-07 slice. Requirements should not be marked
fully complete until later phases create the remaining weeks/labs, unless GSD
metadata explicitly records partial slice completion.

</domain>

<decisions>
## Implementation Decisions

### Page Set And Route Shape

- **D-01:** Create exactly these week pages in Phase 3:
  `docs/course-c/week-01.md` through `docs/course-c/week-07.md`.
- **D-02:** Create exactly these lab pages in Phase 3:
  `docs/course-c/labs/lab-01.md` through `docs/course-c/labs/lab-07.md`.
- **D-03:** Add Week 01-07 and Lab 01-07 to the Course C sidebar only after the
  files exist. Do not add sidebar links to Week 08-16 or Lab 08-16 in Phase 3.
- **D-04:** Keep every page static Markdown using the existing Course A/B style:
  H1 title, short scenario intro, `ChapterIntroduction` if useful, tables,
  fenced prompts/templates, and simple links. Do not introduce new Vue
  components or dependencies.

### Weekly Learning Rhythm

- **D-05:** Every Week 01-07 page must follow the Course C rhythm:
  business situation, role boundary, inputs, AI workflow, tool/application
  integration, compliance review, assistant-pack update, and acceptance
  criteria.
- **D-06:** Each week page should be a usable first-pass chapter, not a one-line
  placeholder. Target the same practical density as existing Course A/B first
  pass content, but keep Phase 3 focused enough to complete and build.
- **D-07:** Week pages should be role/workflow tutorials, not abstract prompt
  catalogs. Prompt examples must be tied to input data, output format, source
  rules, human review, and reusable artifacts.

### Continuous Virtual Company Story

- **D-08:** Use the Phase 2 synthetic company `星河咖啡设备有限公司（虚构）` as the
  continuous story for Week 01-07.
- **D-09:** Reuse Phase 2 sample artifacts where they fit:
  `virtual-company-profile.md`, `sample-crm.csv`, and relevant template pages.
  Week 07 may introduce a small inline KPI table if the current CSV files do not
  contain enough dashboard fields, but it should remain fictional/sample-only.
- **D-10:** The 01-07 storyline should advance from company/role setup to market
  research, product positioning, brand assets, sales channel planning, CRM
  follow-up, and management dashboard design.

### Lab Evidence Contract

- **D-11:** Each Lab 01-07 page must ask students for concrete evidence tied to
  the week: reports, tables, dashboards, SOPs, templates, approval records, or
  audit logs.
- **D-12:** Every lab must explicitly update the learner's role AI assistant
  pack with at least one reusable artifact, such as a workflow, prompt, SOP,
  source record, field table, checklist, or dashboard spec.
- **D-13:** Lab pages should include submission requirements, validation checks,
  and scoring criteria. They should be executable by a business learner without
  requiring code or production system access.

### Professional Sources And Research Gate

- **D-14:** Week 02-07 pages must include a `## Reference 使用` section with both
  implementation sources and authoritative domain sources. Week 01 can use
  management/operating-model sources plus the Phase 2 templates.
- **D-15:** Phase 3 professional-source examples should use stable, recognized
  books, papers, and management frameworks rather than only current tool docs.
  Recommended source anchors:
  - Market research and measurement: Churchill (1979) on marketing construct
    measurement, Kotler/Keller marketing management textbooks, and public
    industry-report methodology notes.
  - Product positioning and new product process: Cooper Stage-Gate research,
    user research/design thinking texts, and product management textbooks.
  - Brand promotion: Keller (1993) customer-based brand equity and integrated
    marketing communications references.
  - Sales/CRM/customer journey: Payne & Frow (2005) CRM framework and Lemon &
    Verhoef (2016) customer journey/customer experience research.
  - Data dashboard and management metrics: Kaplan & Norton (1992) balanced
    scorecard, Davenport/Harris analytics management writing, statistics/data
    quality basics.
- **D-16:** Do not overclaim bibliography completeness in Phase 3. The pages must
  show students what kind of source to use, why it supports the task, and what it
  cannot prove. Detailed reference catalog consolidation remains Phase 6.

### Compliance And Risk

- **D-17:** Weeks 01-07 are lower or medium risk compared with Phase 4/5, but
  every page still applies the four gates: data gate, source gate, human gate,
  and audit gate.
- **D-18:** Pages must not ask students to use real customer, employee, finance,
  tax, legal, credential, or production-system data. Use fictional/sample,
  public, or redacted inputs.
- **D-19:** AI wording must stay within draft, analysis, organization,
  comparison, review, and workflow support. Human review is required for customer
  promises, pricing commitments, external brand publication, KPI interpretation,
  and management conclusions.

### Planning Shape

- **D-20:** Split Phase 3 execution into four plans:
  1. Week/Lab 01-03: operating system setup, market research, product
     positioning.
  2. Week/Lab 04-05: brand promotion and sales/channel development.
  3. Week/Lab 06-07: CRM/customer maintenance and dashboard/KPI design.
  4. Sidebar/navigation integration and full verification.
- **D-21:** Each content plan should commit its pages separately from navigation
  and closeout metadata where possible, keeping verification failures easy to
  isolate.

### the agent's Discretion

- Exact section titles within each week/lab can vary if the required rhythm is
  present and machine-verifiable.
- Exact prompt wording, tables, sample values, and fictional sub-scenarios are up
  to the implementation agent as long as they remain consistent with 星河咖啡设备
  and Phase 2 safety rules.
- The planner may choose whether `ChapterIntroduction` appears on every page or
  only on week pages, based on consistency with existing Course A/B style.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Planning

- `.planning/PROJECT.md` — Course C product identity, source-gate requirement,
  safety boundaries, and repo constraints.
- `.planning/REQUIREMENTS.md` — Phase 3 requirements `CURR-01`, `CURR-02`,
  `CURR-03`, `LAB-01`, `LAB-02`, and `LAB-03`.
- `.planning/ROADMAP.md` — Phase 3 goal and success criteria.
- `.planning/STATE.md` — Current workflow status and next route.
- `.planning/phases/01-course-c-site-skeleton/01-CONTEXT.md` — Course C public
  shell and route-stability decisions.
- `.planning/phases/02-compliance-templates-and-synthetic-examples/02-CONTEXT.md`
  — Template, synthetic example, compliance, and professional-source decisions.
- `.planning/phases/02-compliance-templates-and-synthetic-examples/02-01-SUMMARY.md`
  and `02-02-SUMMARY.md` — Implemented Phase 2 assets and route/build notes.

### Course C Assets

- `docs/course-c/index.md` — Course C positioning and 16-week route.
- `docs/course-c/teaching-calendar.md` — Week 01-07 topics and concrete tasks.
- `docs/course-c/reference-integration.md` — Source split, professional-source
  matrix, and citation/use template.
- `docs/course-c/templates/role-ai-assistant-pack.md` — Assistant-pack template
  that every lab should update.
- `docs/course-c/templates/workflow-sop.md` — SOP template for workflow outputs.
- `docs/course-c/templates/prompt-library.md` — Prompt/source/review template.
- `docs/course-c/templates/compliance-checklist.md` — Four-gate checklist.
- `docs/course-c/templates/audit-log.md` — Evidence and audit template.
- `docs/course-c/templates/roi-report.md` — Improvement proof template.
- `docs/course-c/examples/virtual-company-profile.md` — Continuous fictional
  company context.
- `docs/course-c/examples/sample-crm.csv` — Sales/CRM sample table.

### Existing Site Patterns

- `docs/course-a/week-01.md` and `docs/course-a/labs/lab-01.md` — Long-form
  tutorial/lab shape with `ChapterIntroduction`, `StepBar`, tables, and
  practical evidence.
- `docs/course-b/week-01.md` and `docs/course-b/labs/lab-01.md` — Engineering
  week/lab structure and scoring format.
- `docs/.vitepress/config.mjs` — Sidebar conventions and route exposure.

### Domain Source Anchors

- Porter, M. E. (1979). "How Competitive Forces Shape Strategy." Harvard
  Business Review.
- Churchill, G. A. (1979). "A Paradigm for Developing Better Measures of
  Marketing Constructs." Journal of Marketing Research.
- Cooper, R. G. (1990). "Stage-Gate Systems: A New Tool for Managing New
  Products." Business Horizons.
- Keller, K. L. (1993). "Conceptualizing, Measuring, and Managing Customer-Based
  Brand Equity." Journal of Marketing.
- Payne, A., & Frow, P. (2005). "A Strategic Framework for Customer Relationship
  Management." Journal of Marketing.
- Lemon, K. N., & Verhoef, P. C. (2016). "Understanding Customer Experience
  Throughout the Customer Journey." Journal of Marketing.
- Kaplan, R. S., & Norton, D. P. (1992). "The Balanced Scorecard: Measures That
  Drive Performance." Harvard Business Review.

</canonical_refs>

<code_context>
## Existing Code Insights

### Current Course C State

- Course C has shell pages, templates, examples, final project, rubric, and
  reference rules. It does not yet have week or lab pages.
- `docs/.vitepress/config.mjs` currently exposes Course C shell pages and
  Phase 2 template/example pages. Phase 3 should add week/lab groups only for
  pages created in Phase 3.
- Phase 2 created both `docs/course-c/examples/README.md` and
  `docs/course-c/examples/index.md`; use `/course-c/examples/` for public
  route links.

### Established Patterns

- Public pages are static Markdown under `docs/`; avoid new build dependencies.
- Linked directory routes need `index.md`, not only `README.md`.
- VitePress build must be verified with `cd docs && BASE=/ai-course-system/ npm
  run build`.
- Avoid exact sensitive-pattern strings in sample disclaimers where they cause
  automated false positives; use neutral wording such as "课堂外部业务对象" and
  "上线环境凭据".

### Integration Points

- New week pages: `docs/course-c/week-01.md` through `week-07.md`.
- New lab pages: `docs/course-c/labs/lab-01.md` through `lab-07.md`.
- Sidebar update: `docs/.vitepress/config.mjs`.
- Course C pages should deep-link to templates and examples that already exist.

</code_context>

<specifics>
## Specific Ideas

Recommended Week/Lab pairing:

| Week | Topic | Main reusable artifact | Lab evidence |
|---|---|---|---|
| 01 | Enterprise AI operating system setup | Role AI assistant map and folder/SOP convention | Assistant-pack skeleton and four-gate role boundary |
| 02 | Market research and industry analysis | Source audit table and industry brief | 10-source research packet with fact/assumption/inference labels |
| 03 | Product positioning and prototype expression | Positioning memo, persona, feature priority matrix | Product one-pager and prototype prompt pack |
| 04 | Brand promotion and content assets | Brand voice guide and content calendar | Campaign asset pack plus publication review checklist |
| 05 | Sales leads and channel development | Target account segmentation and outreach templates | Customer tier table, channel plan, outreach sequence |
| 06 | Customer relationship maintenance and sales execution | CRM field design and follow-up SOP | Meeting note to CRM update and sales funnel evidence |
| 07 | Data analysis and management dashboard | KPI tree, metric dictionary, dashboard spec | Management dashboard field table and audit notes |

Recommended common week sections:

```markdown
## 业务情境
## 角色边界
## 输入资料
## AI 工作流
## 工具与应用整合
## Reference 使用
## 合规审查
## 助理包更新
## 验收标准
```

Recommended common lab sections:

```markdown
## 实验目标
## 实验任务
## 输入材料
## 操作步骤
## 提交要求
## 验收标准
## 评分标准
```

</specifics>

<deferred>
## Deferred Ideas

- Week 08-14 and Lab 08-14 high-risk investment, finance, tax, HR, legal, and
  administration pages.
- Week 15 and Lab 15 enterprise API/MCP/system-connection content.
- Week 16 final defense page and Lab 16.
- Full reference catalog consolidation in `reference/catalog/course-integration-map.md`.
- Long-form instructor scripts, slide outlines, and richer visual/interactive
  examples.

</deferred>

---

*Phase: 03-core-business-weeks-01-07-and-labs*
*Context gathered: 2026-06-06*
