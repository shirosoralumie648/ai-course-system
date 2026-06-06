# Phase 4: High-Risk Business Weeks 08-14 And Labs - Research

**Researched:** 2026-06-06
**Status:** Complete

## Planning Question

How should Course C add high-risk investment, finance, tax, HR, legal, and
administration weeks while teaching useful AI workflows without creating
professional advice or unsafe data handling?

## Key Findings

### Common High-Risk Pattern

Every high-risk page needs the same safety contract:

- AI can draft, analyze, organize, compare, review, summarize, classify, create
  checklists, generate questions, and record workflow evidence.
- AI cannot make final professional decisions, submit filings, sign contracts,
  give buy/sell recommendations, determine hiring/pay/performance outcomes, or
  act on production systems.
- The page must name the human approver role and the approval timing.
- Labs must require redaction/source checking, human approval, and audit logs.

### Official Source Anchors

The phase should cite official or authoritative categories without locking the
course to one jurisdiction:

| Scenario | Source anchors |
|---|---|
| Public investment | SEC Investor.gov, EDGAR filings, FINRA investor education, corporate finance/valuation textbooks |
| Investment banking/BP | Public company filings, due diligence checklists, corporate finance textbooks, regulator/industry materials |
| Finance/budget | Accounting/finance textbooks, accounting standards categories, internal-control/audit references |
| Tax records | IRS official small-business recordkeeping/business expense guidance as example; local tax authority guidance for actual jurisdiction |
| HR | DOL official employer/labor materials, EEOC prohibited employment practices, HR management textbooks |
| Legal contracts/disputes | Official laws/regulations, court/government records guidance, contract law textbooks, lawyer review |
| Administration/governance | Corporate governance, records management, fixed-asset policy, official qualification requirements |

### Existing Course Assets

- `sample-finance.csv` supports Week 10 budget/variance.
- `sample-hr.csv` supports Week 12 HR/recruiting.
- `sample-contract-dispute.md` supports Week 13 legal/dispute issue spotting.
- The compliance checklist, audit log, workflow SOP, prompt library, and ROI
  report templates should be deep-linked throughout Phase 4.

### Validation Architecture

Static source/build verification is enough:

- Files exist for Week/Lab 08-14.
- Week pages contain required Course C sections plus high-risk boundary terms.
- Lab pages contain evidence sections plus redaction/source/human/audit terms.
- Each page includes implementation and authoritative domain source sections.
- Sidebar links Week/Lab 08-14 and omits Week/Lab 15-16.
- Full VitePress build succeeds.

## Risks

- Professional overclaiming: pages must avoid advice language.
- Jurisdiction drift: official source examples must be framed as source types,
  not globally applicable rules.
- Data leakage: labs must not ask students to upload real sensitive records.
- Placeholder pressure: Phase 4 should create complete first-pass pages, not
  shallow stubs.

---

*Phase: 04-high-risk-business-weeks-08-14-and-labs*
