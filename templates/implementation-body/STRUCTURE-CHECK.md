# Implementation Body Structure Check

This root is the user-owned extension body. It may be empty on first install, but it gives users a predictable place to attach real capability.

Suggested directories:

- `skills/` for curated, local, generated, or domain skill repositories
- `mcp/` for user-owned MCP server implementations
- `workflows/` for reusable prompt workflows
- `agents/` for custom subagents or orchestration adapters

Expected behavior:

- Register MCP servers from `global-agent-fabric/mcp/servers.yaml`.
- Register skills from `global-agent-fabric/skills/sources.yaml`.
- Register workflows from `global-agent-fabric/workflows/sources.yaml`.
- Route subagents through Maestro or runtime-specific bridges.
- Keep secrets in environment variables or local ignored files, never in public registries.

The governance brain is fixed. This body is intentionally customizable.
