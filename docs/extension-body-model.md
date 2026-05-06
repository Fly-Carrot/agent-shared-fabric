# Extension Body Model

Agent Shared Fabric uses a parallel-folder model.

## Governance Brain

The governance root contains light, inspectable state:

```text
global-agent-fabric/
  rules/
  mcp/servers.yaml
  skills/sources.yaml
  workflows/sources.yaml
  memory/schema.yaml
  projects/registry.yaml
  sync/
  scripts/sync/
```

It describes what should happen.

## Implementation Body

The implementation root contains heavy executable capability:

```text
agent-fabric-implementation/
  skills/
  mcp/
  workflows/
  agents/
```

It does the work.

## Why Separate Them

This gives the system two useful properties:

- the governance layer stays portable and reviewable
- implementations can grow, change, or be swapped without rewriting the control plane

## Registry References

The governance brain points to the body through registries:

- `skills/sources.yaml` points to skill folders
- `mcp/servers.yaml` points to MCP server entrypoints
- `workflows/sources.yaml` points to reusable workflow prompts
- `runtime-map.yaml` points to generated runtime mirrors

This is the "plugin" model: structure and function are separated, but connected by explicit routes.
