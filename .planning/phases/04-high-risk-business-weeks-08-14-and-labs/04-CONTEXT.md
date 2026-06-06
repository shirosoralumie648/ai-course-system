# Phase 4: High-Risk Business Weeks 08-14 And Labs - Context

**Gathered:** 2026-06-06
**Status:** Ready for planning
**Mode:** auto-selected recommended defaults

<domain>
## Phase Boundary

Phase 4 creates Course C Week 08 through Week 14 and Lab 08 through Lab 14. It
covers public stock/investment research, investment banking/business planning,
financial management, tax filing records, HR, legal contracts/disputes, and
administration/corporate governance.

This is the high-risk business slice. Pages must teach AI-supported drafting,
analysis, organization, comparison, review, checklists, and workflow records.
They must not teach AI as final legal, tax, investment, HR, accounting,
compliance, or management decision authority.

Phase 4 does not create Week 15 enterprise API/MCP content, Week 16 final
defense, full reference catalog consolidation, or live production integrations.

</domain>

<decisions>
## Implementation Decisions

### Page Set And Navigation

- **D-01:** Create exactly Week 08-14 pages:
  `docs/course-c/week-08.md` through `docs/course-c/week-14.md`.
- **D-02:** Create exactly Lab 08-14 pages:
  `docs/course-c/labs/lab-08.md` through `docs/course-c/labs/lab-14.md`.
- **D-03:** Add Week/Lab 08-14 to Course C sidebar only after files exist. Do
  not add Week 15-16 or Lab 15-16 links in Phase 4.
- **D-04:** Continue the static Markdown Course C style from Phase 3. Do not add
  new Vue components, dependencies, or live systems.

### High-Risk Wording Contract

- **D-05:** Every Week 08-14 page must include explicit `AI 可以支持` and
  `AI 不能直接做` sections or tables.
- **D-06:** The allowed AI verbs are draft, analyze, organize, compare, review,
  summarize, classify, generate questions, prepare checklists, and record
  workflow evidence.
- **D-07:** The prohibited AI actions include final buy/sell investment advice,
  final valuation or financing terms, final accounting/tax treatment, tax filing
  submission, hiring/firing/pay/performance decisions, final legal opinion,
  contract signing, dispute strategy, official corporate governance decisions,
  and any production-system write.
- **D-08:** Every page must state that responsible professionals or managers
  approve final output: investment/finance/tax/legal/HR/admin/governance owners
  as appropriate.

### Weekly Rhythm And Evidence

- **D-09:** Every Week 08-14 page must follow the same Course C rhythm used in
  Phase 3: business situation, role boundary, inputs, AI workflow, tool/application
  integration, Reference use, compliance review, assistant-pack update, and
  acceptance criteria.
- **D-10:** Every Lab 08-14 page must require redaction/source checking, human
  approval, and audit logging where applicable.
- **D-11:** Every lab must update the role AI assistant pack with at least one
  reusable artifact: checklist, SOP, source record, review prompt, risk memo,
  approval record, or audit log.

### Scenario Scope

- **D-12:** Week/Lab 08 covers public stock and investment research only as a
  research framework and risk memo without buy/sell/hold recommendations.
- **D-13:** Week/Lab 09 covers investment banking/business planning as BP
  structure, due diligence checklist, roadshow Q&A, and financing material
  organization without final deal terms or solicitation claims.
- **D-14:** Week/Lab 10 covers financial management and budget analysis as
  sample-data budget explanation, cost categorization, variance analysis, and
  financial statement interpretation support without final accounting judgment.
- **D-15:** Week/Lab 11 covers tax filing and compliance records as document
  checklist, recordkeeping SOP, risk questions, and review packet without tax
  filing submission or final tax advice.
- **D-16:** Week/Lab 12 covers HR as job description, screening rubric, interview
  questions, training/performance workflow, bias/privacy review without hiring,
  firing, compensation, or performance decisions.
- **D-17:** Week/Lab 13 covers legal contracts and dispute handling as clause
  checklist, issue spotting, timeline, evidence packet, and lawyer questions
  without final legal advice or dispute strategy.
- **D-18:** Week/Lab 14 covers administration and corporate governance as fixed
  asset register, meeting agenda/minutes, qualification-maintenance checklist,
  and policy rollout SOP without official governance decisions.

### Source Requirements

- **D-19:** Every Week 08-14 page must include `## Reference 使用` with
  implementation sources and authoritative domain sources.
- **D-20:** Implementation sources may include spreadsheet/BI docs, filing
  database help, HR/ATS help, contract-review tool docs, office SaaS docs, and
  Phase 2 templates. They only explain workflow mechanics.
- **D-21:** Authoritative domain sources must be official, regulatory,
  standards-based, recognized textbook/book, peer-reviewed paper/review, public
  filing, court/government, or recognized professional/industry-body materials.
- **D-22:** Source anchors for Phase 4 should include examples such as SEC
  Investor.gov/EDGAR for public filings and investment education, FINRA investor
  education for investment risk and due diligence framing, IRS official
  recordkeeping/business expense guidance for tax records, DOL and EEOC official
  materials for HR/labor and hiring discrimination boundaries, court/government
  records guidance such as PACER/U.S. Courts for litigation-material boundaries,
  accounting/finance textbooks and standards categories, and corporate
  governance/records management references.
- **D-23:** Pages must avoid implying U.S.-only rules apply globally. Use official
  sources as examples and instruct learners to use the relevant jurisdiction,
  regulator, standard, or company policy for their context.

### Data And Privacy

- **D-24:** Use Phase 2 fictional/sample data and small inline fictional records.
  Do not ask students to upload real account numbers, tax IDs, employee records,
  payroll data, legal filings, confidential contracts, credentials, production
  exports, or private customer data.
- **D-25:** Labs may ask students to practice redaction on fictional/sample
  documents and to document redaction rules, but not to process real sensitive
  material in public course submissions.

### Planning Shape

- **D-26:** Split Phase 4 into five plans:
  1. Week/Lab 08-09: investment research and investment banking/business
     planning.
  2. Week/Lab 10-11: financial management and tax records.
  3. Week/Lab 12-13: HR and legal contracts/disputes.
  4. Week/Lab 14 plus navigation.
  5. Full verification and closeout metadata if needed.
- **D-27:** Keep content slices independently verifiable with plan-specific
  artifact, source, prohibited-action, and build checks.

### the agent's Discretion

- Exact sample values, fictional records, and prompt wording are up to the
  implementation agent if the safety boundary is preserved.
- Exact authority-source examples can vary by page, but every page must include
  both source types and limitations.
- The planner may combine navigation with Week/Lab 14 if the plan remains
  manageable.

</decisions>

<canonical_refs>
## Canonical References

### Project And Prior Phase Context

- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/phases/02-compliance-templates-and-synthetic-examples/02-CONTEXT.md`
- `.planning/phases/03-core-business-weeks-01-07-and-labs/03-CONTEXT.md`
- `.planning/phases/03-core-business-weeks-01-07-and-labs/03-VERIFICATION.md`

### Course Assets

- `docs/course-c/teaching-calendar.md`
- `docs/course-c/reference-integration.md`
- `docs/course-c/templates/compliance-checklist.md`
- `docs/course-c/templates/audit-log.md`
- `docs/course-c/templates/workflow-sop.md`
- `docs/course-c/templates/prompt-library.md`
- `docs/course-c/templates/roi-report.md`
- `docs/course-c/examples/virtual-company-profile.md`
- `docs/course-c/examples/sample-finance.csv`
- `docs/course-c/examples/sample-hr.csv`
- `docs/course-c/examples/sample-contract-dispute.md`

### Official/Authoritative Source Anchors

- SEC Investor.gov and EDGAR for public company filings and investment education.
- FINRA investor education for investment risk and due diligence concepts.
- IRS official small-business recordkeeping and business-expense guidance for
  tax-record workflow examples.
- U.S. Department of Labor official employer/labor materials for wage/hour and
  employment process boundaries.
- EEOC official prohibited employment practices and hiring-discrimination
  materials for HR fairness boundaries.
- U.S. Courts/PACER official materials for litigation-record boundaries.
- Accounting, corporate finance, HR management, contract law, tax, corporate
  governance, and records-management textbooks/standards as domain source
  categories.

</canonical_refs>

<code_context>
## Existing Code Insights

- `docs/course-c/week-01.md` through `week-07.md` and `docs/course-c/labs/lab-01.md`
  through `lab-07.md` already exist and are linked in the sidebar.
- Phase 4 should add only Week/Lab 08-14 files and links.
- Course C sidebar currently has shell links, Week/Lab 01-07 groups, and
  template/example groups. Extend existing groups rather than creating duplicate
  navigation groups.
- All pages should remain static Markdown and build with
  `cd docs && BASE=/ai-course-system/ npm run build`.

</code_context>

<specifics>
## Specific Ideas

Recommended Week/Lab pairing:

| Week | Topic | Safe artifact |
|---|---|---|
| 08 | Public stock and investment research | Company research framework, filing/source table, risk memo without recommendations |
| 09 | Investment banking and business planning | BP outline, due diligence checklist, roadshow Q&A, no final terms |
| 10 | Financial management and budget analysis | Sample budget explanation, variance table, finance review questions |
| 11 | Tax filing and compliance records | Tax document checklist, recordkeeping SOP, reviewer questions |
| 12 | Human resources management | JD, screening rubric, interview question bank, bias/privacy review |
| 13 | Legal contracts and dispute handling | Clause checklist, issue-spotting memo, timeline, lawyer questions |
| 14 | Administration and corporate governance | Fixed asset register, meeting minutes, qualification calendar, policy rollout SOP |

Required high-risk page phrases:

- `AI 可以支持`
- `AI 不能直接做`
- `必须由负责人或专业人员确认`
- `数据门`
- `来源门`
- `人类门`
- `审计门`

</specifics>

<deferred>
## Deferred Ideas

- Week 15 / Lab 15 enterprise system connection and API/MCP planning.
- Week 16 / Lab 16 final defense and project package.
- Full reference catalog consolidation.
- Jurisdiction-specific legal/tax/investment advice.
- Live enterprise integrations or production data handling.

</deferred>

---

*Phase: 04-high-risk-business-weeks-08-14-and-labs*
*Context gathered: 2026-06-06*
