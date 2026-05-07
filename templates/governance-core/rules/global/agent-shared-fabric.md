# Agent Shared Fabric Global Rule Template

Use the configured Agent Shared Fabric root as canonical.

## Fixed Core

The fixed operating flow is:

```text
preflight -> sync_all -> context loading -> phase logging -> postflight -> memory lanes -> receipts
```

Do not replace this with ad-hoc summaries or direct writes.

Before substantial work:

1. run `hooks/before-task.sh` when available
2. otherwise run preflight and sync-all directly
3. load global context
4. load runtime bridge
5. load project overlay
6. report `[BOOT_OK]` only after success

For complex work, emit these exact phase keys:

```text
route
plan
review
dispatch
execute
report
```

These keys are the recommended governance sequence. The base hook validates the vocabulary; stricter runtimes may enforce ordering, but the portable core keeps ordering advisory so agents can recover from retries or late reporting.

## Dispatch Order

When a task needs external capability, choose in this order:

1. MCP server
2. curated/local skill
3. indexed external skill library
4. Maestro or native subagent orchestration
5. manual script fallback

## Custom Extensions

MCP servers, skills, workflows, custom subagents, and domain registries are customizable extension bodies. Register them through YAML registries. Do not hardcode private tools into the governance core.

MemPalace is strongly recommended for process memory. Maestro is strongly recommended for explicit subagent orchestration. Neither is required for the core contract to run.

At the end of substantial work, run `hooks/after-task.sh` when available, include user-question-profile distillation, and report `[SYNC_OK]` only after success. Lightweight receipt-only postflight is allowed for trivial work, but it is not a full synchronization record.
