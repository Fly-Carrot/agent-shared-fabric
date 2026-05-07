# Structure Validation

Agent Shared Fabric has two roots that should be checked separately.

```text
AgentSharedFabric/
  global-agent-fabric/              # fixed governance harness
  agent-fabric-implementation/      # user-owned extension body
```

## Governance Brain Checklist

`global-agent-fabric/` is the fixed control plane. A usable install should contain:

- `rules/global/` for global runtime instructions
- `hooks/before-task.sh`, `hooks/log-phase.sh`, and `hooks/after-task.sh`
- `scripts/sync/preflight_check.py`, `sync_all.py`, `log_task_phase.py`, and `postflight_sync.py`
- `sync/boot-sequence.md`, receipts, phase logs, and runtime maps
- `memory/schema.yaml` plus memory lane files
- `mcp/servers.yaml`, `skills/sources.yaml`, and `workflows/sources.yaml`
- `projects/registry.yaml`
- `LAYOUT.tree` and `STRUCTURE-CHECK.md`

This root should stay small, inspectable, and portable. It stores governance, not heavy tool implementations.

## Implementation Body Checklist

`agent-fabric-implementation/` is the user-owned capability area. A healthy body usually contains:

- `skills/` for curated, local, or domain skill repositories
- `mcp/` for user-owned MCP server implementations
- `workflows/` for reusable prompt workflows
- `agents/` for custom subagents or orchestration adapters
- `README.md` and `STRUCTURE-CHECK.md`

This root is intentionally customizable. Empty folders are valid on first install; registries in the governance brain decide what is enabled.

## How To Validate

Run the initializer in a temporary location or against an existing install:

```bash
python3 scripts/init_agent_shared_fabric.py \
  --root ~/AgentSharedFabric/global-agent-fabric \
  --implementation-root ~/AgentSharedFabric/agent-fabric-implementation \
  --workspace /path/to/workspace
```

Then inspect:

```bash
cat ~/AgentSharedFabric/global-agent-fabric/STRUCTURE-CHECK.md
cat ~/AgentSharedFabric/agent-fabric-implementation/STRUCTURE-CHECK.md
```

The Fabric App can also surface this boundary through its Preflight Harness page: governance files are the harness; MCP, skills, workflows, and subagents are extension capability.
