# Pitfalls Research: Course C Business AI Operations

**Domain:** Course C business AI operations curriculum
**Confidence:** High for repo/build pitfalls, medium-high for compliance

## Critical Pitfalls

| Pitfall | Warning signs | Prevention strategy | Phase |
| --- | --- | --- | --- |
| Course C becomes a prompt encyclopedia | Pages are mostly prompt lists; no company, role, inputs, outputs, or evidence | Require every week to include business problem, role boundary, input materials, AI workflow, compliance review, and assistant-pack update | 2, 3 |
| AI is framed as final decision-maker | Text says AI decides hiring, buy/sell, tax filing, legal conclusion, policy publication, or system write | Use "AI drafts/supports/summarizes"; require approval checkpoints | 2, 4 |
| Investment module becomes financial advice | Buy/sell calls, guaranteed returns, model portfolios, "AI stock picker" wording | Limit Week 8 to public-info research, assumption tables, risk disclosure, and source audit | 4 |
| HR module creates discrimination risk | Resume auto-ranking, rejection automation, salary decisions, protected-class proxies | Use job-related criteria, synthetic candidates, human review, and adverse-impact checklist | 4 |
| Legal/tax/finance modules imply professional authority | "Legal opinion", "tax strategy", "approved filing", "compliant contract" language | Frame outputs as checklists, drafts, risk memos, and sign-off packets | 4 |
| Sensitive data leaks | Sample CSVs contain real names, phone numbers, salaries, tax IDs, contracts, screenshots with secrets | Use synthetic data only; audit screenshots and samples; keep real data out of `docs/` and git | 2, 6 |
| Enterprise API/MCP path enables unsafe writes | CRM/ERP/finance write demos, broad tokens, production endpoints, credentials in pages | Make Week 15 read-only/mock-first with least privilege, secret hygiene, and audit log | 5 |
| Compliance artifacts are decorative | Generic disclaimer exists but weekly labs do not apply it | Each high-risk lab must produce audit-log, data-gate, source-gate, and human-gate evidence | 2, 4 |

## Moderate Pitfalls

| Pitfall | Warning signs | Prevention strategy | Phase |
| --- | --- | --- | --- |
| Pages exist but are unreachable | `docs/course-c/*.md` created but no nav/sidebar/homepage entry | Add Course C nav, sidebar, homepage card, and links in Phase 1 | 1 |
| GitHub Pages base-path breakage | Works locally but links/assets break under `/ai-course-system/` | Use `BASE=/ai-course-system/ npm run build`; avoid hard-coded root links | 1, 6 |
| Markdown/Vue component parse failures | Build fails near prop-heavy components, arrays, quotes, or multiline props | Keep first pass mostly Markdown and fenced code; build after batches | 1, 3 |
| Course C overlaps Course B | Lessons drift into coding/full-stack implementation | Course C owns business workflows, documents, SOPs, approvals, SaaS import/export | 1 |
| Reference dependency leaks into site | Pages require ignored `reference/repos/*` | Keep pages self-contained; use reference catalog as teacher guidance | 3, 6 |
| Final project rewards volume over transformation | Huge prompt library, no before/after, ROI, quality, or risk evidence | Rubric grades workflow reuse, compliance packet, before/after evidence, and measurable improvement | 6 |

