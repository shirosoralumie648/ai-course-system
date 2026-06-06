# Phase 5 Patterns

## Reused Course C Patterns

- Week pages use the 9-section Course C rhythm:
  business situation, role boundary, inputs, AI workflow, tool/application
  integration, Reference use, compliance review, assistant-pack update, and
  acceptance criteria.
- Lab pages use the 7-section evidence rhythm:
  goal, task, input, steps, submission, acceptance, and scoring.
- High-risk pages must include AI support/prohibition language and four-gate
  compliance checks.
- Sources are split into implementation sources and authoritative domain sources.

## Phase 5 Additions

- Enterprise connection pages use a governance packet rather than production
  connector code as the primary artifact.
- Permission matrix defaults to read-only and escalates only with explicit owner
  approval.
- Mock dataset is required before any real data is considered.
- Secret hygiene is a first-class acceptance criterion.
- MCP/API/tool surfaces are described as capability boundaries, not magic
  productivity features.

## Anti-Patterns To Avoid

- Asking students to paste real API keys, OAuth tokens, credentials, customer
  data, HR data, finance data, tax records, contracts, or production exports.
- Creating a live MCP server or backend service in Phase 5.
- Presenting `danger-full-access`, wildcard OAuth scopes, broad network access,
  or write/admin permissions as normal defaults.
- Treating AI tool output as sufficient approval evidence.
- Adding Week/Lab 16 links before Phase 6 creates those pages.
