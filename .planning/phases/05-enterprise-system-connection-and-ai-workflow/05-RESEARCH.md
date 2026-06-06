# Phase 5 Research

## Question

How should Course C teach business learners to plan safe Skills, API/MCP, and
enterprise-system connections for Codex/Claude Code style agents without
creating unsafe production integrations?

## Implementation Sources

### Existing Course Sources

- `docs/shared/quick-start.md` already explains API Key, BaseURL, model ID,
  OpenAI-compatible and Anthropic-compatible calling patterns, and tool
  configuration basics.
- `docs/shared/codex-cli.md` and `docs/shared/claude-code.md` provide local
  installation/verification placeholders.
- Course C templates already provide compliance checklist, audit log, workflow
  SOP, and prompt-library structures.

### OpenAI/Codex Official Docs

- Codex Agent Skills docs explain that skills package instructions, resources,
  and optional scripts for reusable workflows, with progressive disclosure and
  local/repo/user/admin/system skill locations.
- Codex AGENTS.md docs explain durable instruction discovery, root-to-current
  directory precedence, and repo/team guidance layering.
- Codex MCP docs explain MCP server configuration through `config.toml` or
  `codex mcp`, stdio and streamable HTTP transports, OAuth/bearer-token auth,
  tool allow/deny lists, and per-tool approval modes.
- Codex approvals/security docs frame sandbox mode and approval policy as two
  layers: what actions are technically allowed, and when Codex must ask before
  acting.
- Codex permissions docs show profiles that can deny `.env` files and allow
  network access only to selected domains.
- OpenAI API key safety and production docs emphasize unique keys, no client-side
  exposure, no repository commits, environment variables/secret management,
  usage monitoring, staging/production isolation, and spend/rate limits.

### Claude Code / MCP Official Docs

- Claude Code MCP docs explain connecting remote HTTP, SSE, stdio, and WebSocket
  MCP servers; using `/mcp` to inspect/authenticate; configuring scopes; and
  approving project-scoped servers.
- MCP docs describe MCP as an open standard for connecting AI applications to
  external data sources, tools, and workflows.
- MCP security best practices emphasize consent, redirect URI validation, OAuth
  state validation, SSRF protection, sandboxing local servers, token audience
  validation, and scope minimization.

## Authoritative Governance/Security Sources

- NIST SP 800-53 Rev. 5 provides access control, audit/accountability, risk, and
  security/privacy control-family framing for system permissions and evidence.
- OWASP Top 10 for LLM Applications provides LLM-specific risk categories such
  as prompt injection, sensitive information disclosure, excessive agency,
  insecure plugin/tool design, and overreliance.
- ISO/IEC 27001/27002, CIS Controls, SOC 2 trust-services criteria, privacy law,
  internal-control, and organization-specific security policies are appropriate
  categories for real enterprise permission and audit review.

## Course Pattern

Phase 5 should not teach live integration as the default. It should teach an
enterprise connection readiness packet:

1. Workflow card.
2. Source-system inventory.
3. Data classification.
4. Field map.
5. Permission matrix.
6. Mock dataset.
7. Approval record.
8. Audit log.
9. Stop/rollback rules.

## Risks

- Learners may mistake API/MCP setup for permission to connect real systems.
- Learners may paste secrets or production data into prompts.
- MCP tools may introduce side effects, prompt injection, confused-deputy risk,
  or excess agency.
- Course pages may become too technical for business learners if they focus on
  implementation code rather than planning artifacts.

## Research Conclusion

Use implementation docs to explain the concepts and vocabulary, but grade the
student on the governance packet. The required lab output should be read-only,
mock-first, least-privilege, permissioned, auditable, and approved by human
owners before any real connection work.
