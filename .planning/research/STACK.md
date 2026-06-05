# Stack Research: Course C Business AI Operations

**Domain:** VitePress static course site
**Confidence:** High

## Current Stack

Course C should use the existing docs stack. It is curriculum content, not a new
application surface.

| Layer | Current choice | Notes |
| --- | --- | --- |
| Site generator | VitePress | Markdown pages under `docs/` |
| UI runtime | Vue 3 | Existing VitePress theme/components only |
| Component library | Element Plus | Already installed; avoid adding new dependencies for Course C v1 |
| Package manager | npm | `docs/package-lock.json` is committed |
| Deployment | GitHub Pages Actions | Builds `docs/.vitepress/dist` |
| Base path | `/ai-course-system/` | Required for repository Pages deployment |

Observed package ranges from `docs/package.json`:

- `vitepress`: `^2.0.0-alpha.16`
- `vue`: `^3.5.0`
- `element-plus`: `^2.13.1`

## Files To Use

- `docs/course-c/`: Course C source subtree.
- `docs/.vitepress/config.mjs`: nav and sidebar.
- `docs/index.md`: homepage action/card.
- `docs/shared/index.md`: optional shared resource links.
- `reference/catalog/course-integration-map.md`: Course C reference mapping.
- `.github/workflows/deploy-pages.yml`: deployment behavior to preserve.

## Commands

```bash
cd docs
npm ci
npm run dev -- --host 0.0.0.0
npm run build
BASE=/ai-course-system/ npm run build
npm run preview -- --host 0.0.0.0
```

Use `BASE=/ai-course-system/ npm run build` before deploy-sensitive completion
claims.

## What Not To Use

- Do not add a backend, database, auth layer, CRM/ERP integration, or live API
  write path for Course C v1.
- Do not clone new large `reference/repos/` dependencies.
- Do not commit generated `docs/.vitepress/dist`.
- Do not move the site root out of `docs/`.
- Do not treat Course C as a web-app feature; it is static curriculum content,
  examples, templates, and VitePress navigation.

