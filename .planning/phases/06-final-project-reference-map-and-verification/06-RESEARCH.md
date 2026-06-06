# Phase 6 Research

## Question

How should Course C close a 16-week business AI operations course so students
submit a reusable assistant pack, a workflow transformation report, and
verifiable compliance/reference evidence?

## Existing Course Evidence

- Week/Lab 01-15 already establish business role workflows, high-risk
  professional boundaries, enterprise connection planning, templates, synthetic
  examples, and four-gate compliance.
- `final-project.md` already requires a role AI assistant pack, workflow
  transformation report, compliance evidence packet, Reference use, and defense.
- `rubric.md` already uses the approved 15/25/20/20/20 weighting.
- `reference-integration.md` already distinguishes implementation sources from
  authoritative domain sources and lists Course C scenario categories.

## Required Closure Pattern

Phase 6 should not introduce new concepts. It should force assembly,
traceability, and defense:

1. Manifest of assistant-pack assets.
2. Before/after workflow transformation report.
3. Evidence table for weekly outputs.
4. Compliance packet with data/source/human/audit gates.
5. Reference evidence map.
6. ROI/quality/risk proof.
7. Defense deck and rehearsal questions.

## Reference Map Need

The existing `reference/catalog/course-integration-map.md` covers Course A and
Course B. Add a Course C section that can be committed publicly without
requiring `reference/repos/`, using source categories and public docs/books
instead of local clone paths as hard dependencies.

## Verification Need

Final verification should prove that the complete course is navigable and
buildable:

- Week/Lab 01-16 files exist.
- Sidebar exposes Week/Lab 01-16.
- Final project and rubric include assistant-pack, transformation evidence,
  compliance evidence, source evidence, and approved scoring.
- `BASE=/ai-course-system/ npm run build` passes.
- Generated/ignored directories are not staged.

## Research Conclusion

Use Phase 6 as a completion and QA phase. Keep new content practical and
evidence-first; do not add live integrations or new component complexity.
