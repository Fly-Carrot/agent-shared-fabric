# Implementation Body Templates

This folder represents user-owned extension capability.

Put real implementations in the generated `agent-fabric-implementation/` root, not in the governance core.

Suggested generated layout:

```text
agent-fabric-implementation/
  skills/       # curated/local/domain skill repositories
  mcp/          # user-owned MCP server implementations
  workflows/    # reusable workflow prompts
  agents/       # custom subagents or orchestration adapters
```

Register these capabilities from the governance core through:

- `global-agent-fabric/mcp/servers.yaml`
- `global-agent-fabric/skills/sources.yaml`
- `global-agent-fabric/workflows/sources.yaml`
- `global-agent-fabric/sync/runtime-map.yaml`
