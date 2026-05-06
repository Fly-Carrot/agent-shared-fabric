# Templates

Templates are intentionally split into two top-level folders.

```text
templates/
  governance-core/       # fixed Agent Shared Fabric control plane
  implementation-body/   # user-owned extension capability
```

## governance-core

The governance core contains rules, hooks, sync scripts, registry examples, memory schema, bridge snippets, and boot/runtime maps.

These templates install into the generated `global-agent-fabric/` root.

## implementation-body

The implementation body contains guidance for user-owned MCP implementations, skills, workflows, and custom agents.

These capabilities install into or live beside the generated `agent-fabric-implementation/` root and are referenced from the governance core through registries.
