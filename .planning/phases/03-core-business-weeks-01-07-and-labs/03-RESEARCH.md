# Phase 3: Core Business Weeks 01-07 And Labs - Research

**Researched:** 2026-06-06
**Status:** Complete

## Planning Question

What does the planner need to know to create Course C Week 01-07 and Lab 01-07
as a coherent business-operations spine without pulling later high-risk weeks
or enterprise-system integration into Phase 3?

## Key Findings

### Existing Site Shape

- The site is a VitePress Markdown course portal under `docs/`. Phase 3 should
  continue with static Markdown, tables, fenced prompts, and existing components
  such as `ChapterIntroduction` and `StepBar`.
- Course A/B week and lab pages use long-form tutorials plus evidence-based lab
  requirements. Course C should follow that instructional style while adding
  business-source and compliance sections.
- `docs/.vitepress/config.mjs` is the only navigation integration point needed
  in Phase 3. Sidebar links should be added after the target pages exist.

### Course C Foundation From Phase 2

- Phase 2 created reusable template pages for role assistant packs, workflow
  SOPs, prompt libraries, compliance checklists, audit logs, and ROI reports.
  Week/lab pages should reference these assets instead of duplicating full
  templates.
- Phase 2 created a fictional company, `星河咖啡设备有限公司（虚构）`, and small
  CRM/finance/HR/legal sample artifacts. Phase 3 should reuse the company and
  CRM data; Week 07 can introduce inline KPI examples if needed.
- The four-gate model is now operational: data gate, source gate, human gate,
  and audit gate. Every Phase 3 page should include a short version of the
  checks, even when the task is not high risk.

### Domain Source Strategy

Phase 3 is business curriculum content, so implementation sources alone are not
enough. Each week should distinguish:

- **Implementation sources:** AI tool docs, spreadsheet/BI docs, CRM help
  centers, prompt examples, template routes.
- **Authoritative domain sources:** recognized business books, peer-reviewed
  papers, official standards, or accepted management frameworks.

Useful anchors for the first seven weeks:

| Week | Domain source anchors | Use in course |
|---|---|---|
| 01 | Porter strategy framing, operating-model/management-system ideas, Phase 2 templates | Define role boundaries and assistant teams without overclaiming AI authority. |
| 02 | Porter (1979), Churchill (1979), market research textbooks | Separate facts, assumptions, measures, and source quality in industry research. |
| 03 | Cooper Stage-Gate, product management and user research texts | Turn product ideas into target users, value proposition, risks, and decision gates. |
| 04 | Keller (1993), integrated marketing communications references | Connect brand assets to brand knowledge, audience, channels, and publication review. |
| 05 | Sales management and CRM textbooks, customer segmentation practice | Build target-account segmentation and outreach sequences with review gates. |
| 06 | Payne & Frow (2005), Lemon & Verhoef (2016) | Treat CRM as a cross-functional process and customer journey evidence, not just a table. |
| 07 | Kaplan & Norton (1992), analytics management writing, data-quality basics | Build dashboard metrics with definitions, data sources, owners, and limitations. |

The pages should cite these as source categories and examples. They should not
claim to provide a complete bibliography; Phase 6 will consolidate references.

### Content Depth

- Phase 3 pages should be complete enough for first-pass teaching and
  assignment use: concrete scenario, inputs, AI workflow, source rules,
  compliance, assistant-pack update, and acceptance criteria.
- Avoid turning each page into a long textbook chapter. A practical business
  learner should be able to complete the task with the page, Phase 2 templates,
  and sample data.
- Labs should be more operational than reflective. Every lab should require
  evidence: source records, tables, prompts, screenshots/exported files,
  approval notes, audit logs, and assistant-pack updates.

### Validation Architecture

Phase 3 remains static content, so verification is source/build oriented:

- Week file existence: `docs/course-c/week-01.md` through `week-07.md`.
- Lab file existence: `docs/course-c/labs/lab-01.md` through `lab-07.md`.
- Required section scans: week pages contain `业务情境`, `角色边界`,
  `输入资料`, `AI 工作流`, `Reference 使用`, `合规审查`, `助理包更新`,
  and `验收标准`; lab pages contain `实验目标`, `实验任务`, `提交要求`,
  `验收标准`, and `评分标准`.
- Source scans: Week 02-07 contain `实现来源` and `权威领域来源`; all weeks
  contain at least one professional source anchor or source category.
- Compliance scans: each week/lab mentions data/source/human/audit gate or the
  four-gate model.
- Route scans: Course C sidebar links only created Week/Lab 01-07 pages.
- Build check: `cd docs && BASE=/ai-course-system/ npm run build`.

## Recommended Plan Shape

1. Create Week/Lab 01-03: operating system setup, market research, product
   positioning.
2. Create Week/Lab 04-05: brand promotion and sales/channel development.
3. Create Week/Lab 06-07: CRM/customer maintenance and dashboard/KPI design.
4. Add Course C sidebar groups for Week 01-07 and Lab 01-07, then run full
   verification.

## Risks

- Requirement ambiguity: `CURR-01` and `LAB-01` mention all 16 pages, but Phase
  3 only owns 01-07. Avoid claiming full 16-week completion in Phase 3.
- Source shallowness: pages that only list tool docs would violate the user's
  requirement for authoritative books and papers.
- Placeholder risk: creating Week 08-16 or Lab 08-16 empty pages would recreate
  404/low-quality content problems.
- Link risk: adding sidebar links before files exist will fail VitePress build.
- Safety risk: using real customer or private operational data in examples would
  violate Phase 2 boundaries.

---

*Phase: 03-core-business-weeks-01-07-and-labs*
