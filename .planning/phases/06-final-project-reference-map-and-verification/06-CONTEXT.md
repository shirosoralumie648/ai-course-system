# Phase 6: Final Project, Reference Map, And Verification - Context

**Gathered:** 2026-06-06
**Status:** Ready for planning
**Mode:** auto-selected recommended defaults

<domain>
## Phase Boundary

Phase 6 completes Course C v1. It creates Week 16 and Lab 16, aligns the final
project and rubric around the role AI assistant pack plus workflow
transformation evidence, updates the Course C reference map, exposes Week/Lab 16
in navigation, and performs final public-site verification.

Phase 6 should close the remaining Course C requirements without creating new
front-end components, backend services, live integrations, or new reference
clones. The public site must not require ignored local `reference/repos/`.

</domain>

<decisions>
## Implementation Decisions

### Page Set And Navigation

- **D-01:** Create exactly `docs/course-c/week-16.md` and
  `docs/course-c/labs/lab-16.md`.
- **D-02:** Add Week/Lab 16 to the Course C sidebar after files exist.
- **D-03:** Keep all changes static Markdown / existing VitePress config only.
  Do not add Vue components, dependencies, generated build output, or live
  services.

### Week/Lab 16 Contract

- **D-04:** Week 16 must teach final defense: role AI assistant pack, workflow
  transformation report, compliance evidence packet, reference evidence, ROI/
  quality/risk proof, and oral defense.
- **D-05:** Lab 16 must require students to assemble the final assistant pack,
  transformation evidence, compliance packet, reference map, and defense deck.
- **D-06:** Week/Lab 16 must preserve high-risk boundaries: AI supports draft,
  organization, review, evidence preparation, and rehearsal; AI does not make
  final professional decisions or fabricate proof.
- **D-07:** Week 16 must include Reference 使用 with implementation sources and
  authoritative domain sources.
- **D-08:** Lab 16 must require data/source/human/audit gate evidence and
  assistant-pack reuse evidence.

### Final Project And Rubric

- **D-09:** `docs/course-c/final-project.md` must explicitly require both a role
  AI assistant pack and a real or realistic workflow transformation report.
- **D-10:** Final project evidence must include before-state, after-state,
  reusable assets, compliance packet, and ROI/quality/risk improvement proof.
- **D-11:** `docs/course-c/rubric.md` must preserve the approved 15/25/20/20/20
  weighting: business framing 15%, assistant-pack completeness 25%, weekly
  outputs 20%, compliance/risk 20%, workflow transformation 20%.
- **D-12:** Rubric must reward reuse, clarity, safety, evidence, and
  transformation quality rather than prompt-library volume.
- **D-13:** Final project and rubric must reference Week/Lab 16 and the 16-week
  assistant-pack progression.

### Reference Map

- **D-14:** `docs/course-c/reference-integration.md` must state Course C is fully
  mapped across Week 01-16 and preserve the implementation-vs-domain source
  distinction.
- **D-15:** `reference/catalog/course-integration-map.md` must include Course C
  mapping without requiring local `reference/repos/`.
- **D-16:** Reference map must include implementation sources and authoritative
  domain-source categories for Course C: market, product, brand, sales, data,
  investment, finance, tax, HR, legal, admin/governance, enterprise systems, and
  final defense.

### Final Verification

- **D-17:** Final QA must verify Week/Lab 01-16 files exist and sidebar links
  Week/Lab 01-16.
- **D-18:** Final QA must verify professional/high-risk pages include both source
  types where relevant.
- **D-19:** Final QA must run `cd docs && BASE=/ai-course-system/ npm run build`.
- **D-20:** Final QA must ensure generated build output, `node_modules`,
  `.local-archive`, and `reference/repos` are not staged/committed.
- **D-21:** Final verification should update `.planning/STATE.md` to complete
  only after checks pass.

### the agent's Discretion

- Exact defense prompts, sample scoring language, and reference-map phrasing are
  up to the implementation agent if the requirement evidence is preserved.
- If final project/rubric already satisfy a requirement, keep edits minimal and
  additive.

</decisions>

<canonical_refs>
## Canonical References

- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/phases/05-enterprise-system-connection-and-ai-workflow/05-VERIFICATION.md`
- `docs/course-c/index.md`
- `docs/course-c/teaching-calendar.md`
- `docs/course-c/final-project.md`
- `docs/course-c/rubric.md`
- `docs/course-c/reference-integration.md`
- `reference/catalog/course-integration-map.md`
- `docs/course-c/templates/role-ai-assistant-pack.md`
- `docs/course-c/templates/compliance-checklist.md`
- `docs/course-c/templates/audit-log.md`
- `docs/course-c/templates/roi-report.md`

</canonical_refs>

<code_context>
## Existing Code Insights

- Week/Lab 01-15 exist and are linked in `docs/.vitepress/config.mjs`.
- `final-project.md` and `rubric.md` already contain the approved core framing
  and weighting, so Phase 6 should refine rather than rewrite.
- `reference/catalog/course-integration-map.md` currently covers Course A/B but
  does not yet map Course C.
- `reference/repos/` is intentionally ignored/local-only and must not be needed
  by public pages.

</code_context>

<specifics>
## Specific Ideas

Recommended Week/Lab 16 outputs:

| Artifact | Purpose |
|---|---|
| Assistant-pack manifest | Proves the reusable role AI assistant pack is complete |
| Workflow transformation report | Shows before/after process and human approvals |
| Compliance evidence packet | Contains data/source/human/audit gate proof |
| Reference evidence map | Shows implementation and authoritative domain sources |
| ROI/quality/risk proof | Shows measurable or inspectable improvement |
| Defense deck/script | Supports 5-8 minute final presentation |

Final QA checks:

- Week 01-16 and Lab 01-16 files exist.
- Sidebar links Week 01-16 and Lab 01-16.
- Build succeeds with GitHub Pages base.
- Final project/rubric/reference map include Course C final closure.
- No ignored/generated directories are staged.

</specifics>

<deferred>
## Deferred Ideas

- Live final showcase platform.
- Automated link crawler beyond VitePress build.
- Real organization-specific legal/security review.
- Course D research course content.

</deferred>

---

*Phase: 06-final-project-reference-map-and-verification*
*Context gathered: 2026-06-06*
