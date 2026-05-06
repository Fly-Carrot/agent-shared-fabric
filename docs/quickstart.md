# Quickstart

## One-Command Local Bootstrap

Clone the repo, then run:

```bash
python3 scripts/init_agent_shared_fabric.py \
  --root ~/AgentSharedFabric/global-agent-fabric \
  --implementation-root ~/AgentSharedFabric/agent-fabric-implementation \
  --workspace /path/to/your/workspace
```

This creates two sibling roots:

```text
AgentSharedFabric/
  global-agent-fabric/              # governance brain
  agent-fabric-implementation/      # implementation body
```

The initializer writes:

- governance rules
- MCP/skills/workflow/project registries
- memory schema
- boot sequence
- runnable sync scripts
- optional workspace `AGENTS.md`
- optional startup snippet

## Verify Boot

```bash
python3 ~/AgentSharedFabric/global-agent-fabric/scripts/sync/preflight_check.py \
  --global-root ~/AgentSharedFabric/global-agent-fabric \
  --workspace /path/to/your/workspace \
  --agent codex

python3 ~/AgentSharedFabric/global-agent-fabric/scripts/sync/sync_all.py \
  --global-root ~/AgentSharedFabric/global-agent-fabric \
  --workspace /path/to/your/workspace \
  --agent codex
```

Only after both commands succeed should an agent report `[BOOT_OK]`.

## Log A Six-Stage Task

```bash
python3 ~/AgentSharedFabric/global-agent-fabric/scripts/sync/log_task_phase.py \
  --global-root ~/AgentSharedFabric/global-agent-fabric \
  --workspace /path/to/your/workspace \
  --agent codex \
  --phase route \
  --note "Classify task and choose workflow."
```

Use the exact phase keys:

```text
route -> plan -> review -> dispatch -> execute -> report
```

## Write Postflight

```bash
python3 ~/AgentSharedFabric/global-agent-fabric/scripts/sync/postflight_sync.py \
  --global-root ~/AgentSharedFabric/global-agent-fabric \
  --workspace /path/to/your/workspace \
  --agent codex \
  --summary "Completed the task." \
  --decision "Use Agent Shared Fabric as canonical governance." \
  --user-question-profile-json '{
    "focus_points": ["agent coordination"],
    "question_patterns": ["asks for concrete implementation"],
    "response_preferences": ["concise but operational"],
    "reasoning_preferences": ["verify real files"],
    "recurring_themes": ["shared fabric"],
    "frictions_or_anxieties": ["agents may skip discipline"]
  }'
```

Only after this succeeds should an agent report `[SYNC_OK]`.
