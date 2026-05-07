# Governance Brain Structure Check

This root is the fixed Agent Shared Fabric harness. It should contain governance, sync contracts, memory lanes, and registries, not heavy implementation code.

Required directories and files:

- `rules/global/`
- `hooks/before-task.sh`
- `hooks/log-phase.sh`
- `hooks/after-task.sh`
- `scripts/sync/preflight_check.py`
- `scripts/sync/sync_all.py`
- `scripts/sync/log_task_phase.py`
- `scripts/sync/postflight_sync.py`
- `sync/boot-sequence.md`
- `memory/schema.yaml`
- `mcp/servers.yaml`
- `skills/sources.yaml`
- `workflows/sources.yaml`
- `projects/registry.yaml`
- `LAYOUT.tree`

Expected behavior:

- Preflight reads this root before substantial work.
- Sync-all refreshes runtime/project context.
- Phase logging writes only the six accepted phase keys.
- Postflight writes memory lanes and receipts.
- External MCP, skills, workflows, and subagents are referenced by registry, not copied wholesale into this brain.
