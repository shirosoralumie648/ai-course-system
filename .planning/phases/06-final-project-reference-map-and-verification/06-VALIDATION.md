# Phase 6 Validation

## Validation Strategy

- Verify Week/Lab 16 artifacts and required sections.
- Verify final project and rubric requirement phrases.
- Verify Course C reference map presence in docs and reference catalog.
- Verify Week/Lab 01-16 files and sidebar links.
- Verify professional/high-risk pages contain source sections.
- Run VitePress production build with repo base.
- Verify staged files exclude generated or local-only directories.

## Commands

```bash
for n in $(seq -w 1 16); do test -f "docs/course-c/week-$n.md"; test -f "docs/course-c/labs/lab-$n.md"; done
for n in $(seq -w 1 16); do rg "/course-c/week-$n" docs/.vitepress/config.mjs; rg "/course-c/labs/lab-$n" docs/.vitepress/config.mjs; done
rg "15%|25%|20%" docs/course-c/rubric.md
rg "before-state|after-state|合规证据|Reference|岗位 AI 助理包" docs/course-c/final-project.md docs/course-c/rubric.md
rg "Course C|课程 C|企业 AI 运营系统" reference/catalog/course-integration-map.md
git diff --check
cd docs && BASE=/ai-course-system/ npm run build
```
