# Course Integration Map

This map connects the current course system to the reference library. It covers
both visible Course B directions in the current repo: full-stack AI product
development and agentic development.

## Course A: Product Prototype + Claude Code

| Course area | Current weeks | References to inspect | Improvement ideas |
| --- | --- | --- | --- |
| No-code fear removal and first app | Week 01-02 | `courses/web-dev-for-beginners`, Vercel AI Chatbot | Add 2-3 small starter apps with screenshots and clear run commands. |
| Claude Code basics | Week 03 | `agentic-coding/anthropic-courses`, `agentic-coding/aider`, Anthropic Claude Code short course | Add a side-by-side "chatbot vs coding agent" exercise with diff review evidence. |
| Product discovery | Week 04-05 | The Mom Test, Continuous Discovery Habits, Sprint, Shape Up | Strengthen interview scripts, anti-pattern examples, and decision criteria. |
| Prototype to AI feature | Week 06-08 | `fullstack-ai/vercel-ai-chatbot`, `ai-engineering/openai-cookbook`, `fullstack-ai/supabase` | Add one real API-backed prototype path with mock mode and real-call verification. |
| Workflow and Skills | Week 09-10 | `agentic-coding/spec-kit`, `agentic-coding/anthropic-courses`, Agent Skills course | Convert current workflow advice into reusable checklists and one student-built skill. |
| MCP | Week 11 | `mcp/mcp-servers`, `mcp/mcp-typescript-sdk`, MCP docs/course | Add a minimal local MCP server design lab before any production integration. |
| Superpowers and verification | Week 12 | `agentic-coding/spec-kit`, Software Engineering at Google, Google SRE books | Add "completion proof" and "verification log" templates. |
| Spec coding and long-running tasks | Week 13-14 | `agentic-coding/spec-kit`, `agentic-coding/openhands`, `agentic-coding/swe-agent` | Add a spec-to-plan-to-diff exercise with a bounded task and explicit stop rule. |
| Agent SDK and Agent Teams | Week 15-16 | `ai-engineering/openai-agents-python`, `agentic-coding/browser-use`, `rag/langgraph` | Add role boundaries, handoff diagrams, and a small multi-agent trace example. |

## Course B: Full-Stack AI Product Track

| Course area | Current weeks | References to inspect | Improvement ideas |
| --- | --- | --- | --- |
| Design to code | Week 01-03 | `fullstack-ai/shadcn-ui`, Refactoring UI, Design of Everyday Things | Add design critique rubrics and "before/after AI UI refinement" examples. |
| CLI and Git | Week 04 | `courses/missing-semester`, Software Engineering at Google | Add shell/git drills that directly support later agent workflows. |
| Database and backend | Week 05 | `fullstack-ai/supabase`, Designing Data-Intensive Applications | Add schema migration, auth/RLS, storage, and edge function reference examples. |
| AI API integration | Week 06 | `fullstack-ai/vercel-ai`, `ai-engineering/openai-cookbook`, `ai-engineering/openai-agents-python` | Separate frontend streaming, backend key safety, and tool-calling examples. |
| Payments and deployment | Week 07 | `fullstack-ai/stripe-checkout-one-time`, `fullstack-ai/stripe-subscription-use-cases`, `production-apps/dub` | Add webhook verification and "backend owns price IDs" as a hard rule. |
| Dify and knowledge base | Week 08 | `rag/dify`, Dify docs | Add retrieval testing logs, chunking experiments, and workflow export review. |
| RAG | Week 09-10 | `rag/rag-from-scratch`, `rag/llama-index`, `rag/haystack`, `rag/graph-rag`, Firecrawl | Add a ladder from naive RAG to chunking, reranking, evals, and graph retrieval. |
| Cross-platform | Week 11 | `cross-platform/expo`, `cross-platform/taro`, `cross-platform/uni-app` | Add a decision matrix: web app, mobile app, mini-program, or PWA. |
| Final product | Week 12 | `production-apps/cal-com`, `production-apps/dub`, `production-apps/twenty`, `production-apps/medplum` | Use production apps to teach architecture reading, domain modeling, and tradeoffs. |

## Course B: Agentic Development Track

| Course area | Current calendar weeks | References to inspect | Improvement ideas |
| --- | --- | --- | --- |
| Agentic development intro | Week 01 | `agentic-coding/openhands`, `agentic-coding/swe-agent`, `agentic-coding/aider` | Use real agent repos to contrast chatbot, copilot, coding agent, and workflow. |
| Claude Code and Codex basics | Week 02-03 | `agentic-coding/anthropic-courses`, `ai-engineering/openai-cookbook`, `agentic-coding/gemini-cli` | Add comparable logs across multiple coding agents and CLI permission models. |
| Context engineering | Week 04 | `agentic-coding/continue`, OpenAI Cookbook selected examples | Add examples of good/bad context packs and retrieval-backed context selection. |
| Rules files | Week 05 | `agentic-coding/spec-kit`, current `docs/course-b/templates` | Add rule linting: concrete, enforceable, scoped, testable. |
| Permissions, hooks, safety | Week 06 | `mcp/mcp-servers`, Claude Code docs, Web Application Security | Add threat cases for tools, file writes, dependency changes, API keys. |
| Skill design | Week 07 | `agentic-coding/anthropic-courses`, Agent Skills course | Add one exemplar skill and one deliberately bad skill for review. |
| MCP | Week 08-09 | `mcp/mcp-servers`, `mcp/mcp-typescript-sdk` | Add minimal MCP server interface design plus risk annotation per tool. |
| Agent team | Week 10 | `rag/langgraph`, `ai-engineering/openai-agents-python` | Add role handoffs, state diagrams, and failure loops. |
| Tests, review, CI | Week 11 | Software Engineering at Google, Google SRE, `agentic-coding/spec-kit` | Add explicit evidence artifacts: test command, review checklist, CI gate, human gate. |
| Final defense | Week 12 | `production-apps/*`, `agentic-coding/*` | Require process trace, diff review, test proof, and a short architecture walk-through. |

## Gaps To Consider Next

- Current Course B has two overlapping identities: full-stack AI product and
  agentic development. Decide whether to split them into two courses or make one
  an advanced module.
- Add small local sample projects for each major reference category so students
  do not need to learn from huge production repositories first.
- Add "reference reading" assignments: students inspect one cloned project and
  extract directory structure, run command, test command, and one reusable idea.
