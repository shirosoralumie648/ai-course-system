# Phase 5 Validation

## Validation Strategy

Phase 5 is static course content with navigation. Validation is file-based:

- Verify Week/Lab 15 artifacts exist.
- Verify Week 15 has the required 9 Course C sections.
- Verify Lab 15 has the required 7 lab sections.
- Verify read-only/mock-first/least-privilege/secret-hygiene/no-production-write
  language is present.
- Verify implementation and governance/security source sections are present.
- Verify sidebar links Week/Lab 15 and omits Week/Lab 16.
- Verify VitePress builds with `BASE=/ai-course-system/`.

## Required Safety Checks

- No real credentials or production-system instructions.
- No production write setup.
- No live enterprise connector implementation.
- No claim that official examples replace organization-specific security,
  legal, data-owner, or system-owner approval.

## Build Check

```bash
cd docs && BASE=/ai-course-system/ npm run build
```
