# Phase 2: Compliance, Templates, And Synthetic Examples - Research

**Researched:** 2026-06-06
**Status:** Complete

## Planning Question

What does the planner need to know to implement the Course C reusable
assistant-pack templates, synthetic examples, four-gate compliance model, and
professional-source rules without creating later week/lab content prematurely?

## Key Findings

### Documentation Shape

- The existing Course C route is a VitePress Markdown subtree. Phase 2 should
  stay in Markdown and small CSV files to avoid the repo's known Markdown/Vue
  component parsing risk.
- VitePress routes are file-based and sidebar entries should point only at files
  that exist. Plan execution must create files before adding matching sidebar
  links in `docs/.vitepress/config.mjs`.
- Existing Course B templates are useful analogs for copyable Markdown
  artifacts, but Course C templates need business workflow, approval, source,
  and audit fields instead of coding-project fields.

### Template Strategy

- Use one overview plus six separate template pages so later week/lab pages can
  deep-link to a precise reusable artifact.
- Every template page should include purpose, suitable use cases, required
  fields, copyable template, short synthetic example, and a usage/submission
  checklist.
- Template pages should remain short enough for repeated reference. Full
  teaching narratives belong in Phase 3-5 week pages.

### Synthetic Data Strategy

- Use one fictional company across all example artifacts to support the Course C
  continuous virtual-company story.
- Keep data small and field-complete: enough columns to power later CRM,
  finance, HR, and contract/dispute exercises without becoming a separate data
  product.
- CSV examples are acceptable for CRM, finance, and HR; Markdown is better for
  company profile and contract/dispute materials.
- All example values must be obviously synthetic. Avoid real companies, real
  emails, real customer names, real contract parties, credentials, IDs that look
  operational, and production-system URLs.

### Compliance Baseline

- Phase 2's four-gate model maps cleanly to public AI governance baselines:
  NIST AI RMF's govern/map/measure/manage framing, ISO/IEC 42001's management
  system controls, and OECD AI Principles around transparency, accountability,
  human oversight, privacy, and safety.
- The course should translate those ideas into student-facing fields: risk
  level, data sensitivity, source type, source confidence, human approver,
  approval timing, audit evidence, final release boundary, and "AI must not"
  language.
- High-risk scenario specifics should not all be solved in Phase 2. Phase 2
  should create reusable fields that Phase 4 and Phase 5 can specialize.

### Source Rules

- `docs/course-c/reference-integration.md` already separates implementation
  sources from authoritative domain sources. Phase 2 should extend it with a
  matrix and a copyable citation/use block.
- Professional-source categories should be explicit enough that future page
  writers cannot use tool docs as the only evidence source for finance, legal,
  HR, tax, investment, product, brand, sales, market research, or management
  content.
- Detailed weekly bibliographies should remain deferred, but Phase 2 should
  define the expected categories per scenario.

## Recommended Plan Shape

1. Build the template and synthetic example files first.
2. Extend reference/compliance rules and Course C navigation after the files
   exist.
3. Verify with file-existence checks, source-content checks, no-real-data scans,
   sidebar link checks, and `BASE=/ai-course-system/ npm run build` from
   `docs/`.

## Validation Architecture

The phase is static content, so validation is source and build verification:

- **Artifact checks:** required template and example files exist.
- **Content checks:** each template has purpose/use cases/required fields/
  copyable template/example/checklist sections.
- **Synthetic-data checks:** examples contain fictional/sample markers and do
  not contain obvious real-data patterns such as `@gmail.com`, `@qq.com`,
  `password`, `secret`, `api_key`, `token`, `身份证`, or `真实客户`.
- **Compliance checks:** checklist content contains data gate, source gate,
  human gate, audit gate, risk level, approver, audit evidence, and release
  boundary.
- **Source checks:** reference integration contains implementation source,
  authoritative domain source, professional-source matrix, and citation/use
  template.
- **Routing checks:** Course C sidebar links every created Phase 2 page and no
  nonexistent Course C week/lab pages.
- **Build check:** `cd docs && BASE=/ai-course-system/ npm run build` exits 0.

## Risks

- Overbuilding: too many sample records or scenario-specific bibliographies
  would pull Phase 3-5 work into Phase 2.
- Underbuilding: empty templates without short examples would not be useful to
  business learners.
- Link risk: adding sidebar links before files exist recreates 404 problems.
- Safety risk: examples that look like real customer, employee, financial, tax,
  legal, or credential data would violate `TEMP-04`.

---

*Phase: 02-compliance-templates-and-synthetic-examples*
