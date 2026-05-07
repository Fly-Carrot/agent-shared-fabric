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

`governance-core/STRUCTURE-CHECK.md` is copied to `global-agent-fabric/STRUCTURE-CHECK.md` so users can validate the fixed harness layout after install.

## implementation-body

The implementation body contains guidance for user-owned MCP implementations, skills, workflows, and custom agents.

These capabilities install into or live beside the generated `agent-fabric-implementation/` root and are referenced from the governance core through registries.

`implementation-body/STRUCTURE-CHECK.md` is copied to `agent-fabric-implementation/STRUCTURE-CHECK.md` so users can validate their extension slots separately from the governance brain.
