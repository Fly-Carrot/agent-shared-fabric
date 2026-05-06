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
  global-agent-fabric/              # fixed governance core
  agent-fabric-implementation/      # customizable tool body
```

The initializer writes:

- governance rules
- MCP/skills/workflow/project registries
- memory schema
- boot sequence
- runnable sync scripts
- runnable hook wrappers
- optional workspace `AGENTS.md`
- optional startup snippet

## Verify Boot With The Hook

```bash
WORKSPACE=/path/to/your/workspace \
AGENT_NAME=codex \
~/AgentSharedFabric/global-agent-fabric/hooks/before-task.sh
```

Only after this succeeds should an agent report `[BOOT_OK]`.

## Log A Six-Stage Task

```bash
WORKSPACE=/path/to/your/workspace \
AGENT_NAME=codex \
~/AgentSharedFabric/global-agent-fabric/hooks/log-phase.sh route "Classify task and choose workflow."
```

Use the exact phase keys:

```text
route -> plan -> review -> dispatch -> execute -> report
```

## Write Postflight

```bash
WORKSPACE=/path/to/your/workspace \
AGENT_NAME=codex \
SUMMARY="Completed the task." \
DECISION="Use Agent Shared Fabric as canonical governance." \
USER_QUESTION_PROFILE_JSON='{
  "focus_points": ["agent coordination"],
  "question_patterns": ["asks for concrete implementation"],
  "response_preferences": ["concise but operational"],
  "reasoning_preferences": ["verify real files"],
  "recurring_themes": ["shared fabric"],
  "frictions_or_anxieties": ["agents may skip discipline"]
}' \
~/AgentSharedFabric/global-agent-fabric/hooks/after-task.sh
```

Only after this succeeds should an agent report `[SYNC_OK]`.
