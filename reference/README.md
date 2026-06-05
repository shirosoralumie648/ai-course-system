# Reference Library for AI Course System

This directory stores external reference material for improving the course content.
It is intentionally ignored by git because many entries are cloned third-party
repositories.

## Structure

- `repos/agentic-coding/`: coding agents, agent workflows, spec-driven coding.
- `repos/mcp/`: MCP servers and SDK references.
- `repos/ai-engineering/`: OpenAI, Anthropic, and general AI engineering examples.
- `repos/fullstack-ai/`: AI app templates, UI systems, Supabase, payments.
- `repos/rag/`: RAG, knowledge-base, search, and AI platform references.
- `repos/production-apps/`: production SaaS/domain products for architecture study.
- `repos/cross-platform/`: mobile, mini-program, and cross-platform app stacks.
- `repos/courses/`: open course repositories.
- `catalog/`: curated notes, course mapping, and non-cloned book/course links.

## Start Here

- [Cloned projects](catalog/cloned-projects.md)
- [Courses and books](catalog/courses-and-books.md)
- [Course integration map](catalog/course-integration-map.md)

## Maintenance

Update all cloned repositories:

```bash
for repo in reference/repos/*/*; do
  if [ -d "$repo/.git" ]; then
    git -C "$repo" pull --ff-only
  fi
done
```

For one repository:

```bash
git -C reference/repos/<category>/<repo> pull --ff-only
```

For sparse clones, keep the current sparse checkout unless you really need the
full project. Many production repositories are large.
