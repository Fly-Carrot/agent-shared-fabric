# Antigravity Startup Snippet Template

Use `{AGENT_SHARED_FABRIC_ROOT}` as the canonical Agent Shared Fabric root.
You are operating in workspace `{WORKSPACE}`.
Load the Antigravity bridge at `{WORKSPACE}/.agents/antigravity/ANTIGRAVITY.md` if it exists.

## Boot

Before substantial work, run the generated boot hook:

```bash
WORKSPACE="{WORKSPACE}" AGENT_NAME=antigravity "{AGENT_SHARED_FABRIC_ROOT}/hooks/before-task.sh"
```

If hooks are not installed yet, run the canonical scripts directly:

```bash
python3 "{AGENT_SHARED_FABRIC_ROOT}/scripts/sync/preflight_check.py" --global-root "{AGENT_SHARED_FABRIC_ROOT}" --workspace "{WORKSPACE}" --agent antigravity
python3 "{AGENT_SHARED_FABRIC_ROOT}/scripts/sync/sync_all.py" --global-root "{AGENT_SHARED_FABRIC_ROOT}" --workspace "{WORKSPACE}" --agent antigravity
```

Report `[BOOT_OK]` only after the hook or both canonical scripts execute successfully. If boot fails, say so explicitly and do not claim shared context was loaded.

## Load Order

1. Global shared context from Agent Shared Fabric.
2. Antigravity runtime bridge from `.agents/antigravity/ANTIGRAVITY.md`.
3. Current project overlay from `AGENTS.md` and `.agents/sync/`.

## Phase Logging

For complex tasks, emit phase events with the generated phase hook:

```bash
WORKSPACE="{WORKSPACE}" AGENT_NAME=antigravity "{AGENT_SHARED_FABRIC_ROOT}/hooks/log-phase.sh" <route|plan|review|dispatch|execute|report> "..."
```

Fallback direct script:

```bash
python3 "{AGENT_SHARED_FABRIC_ROOT}/scripts/sync/log_task_phase.py" --global-root "{AGENT_SHARED_FABRIC_ROOT}" --workspace "{WORKSPACE}" --agent antigravity --phase <route|plan|review|dispatch|execute|report> --note "..."
```

## Maestro Orchestration

- Default to `/maestro:orchestrate <task>` for complex or medium tasks unless explicit point-to-point delegation is requested.
- Always maintain `MAESTRO_EXECUTION_MODE=ask` as an execution gate.
- Dispatch should use registered expert subagents; do not fallback to generic/generalist delegation when specific agents exist.

## Skill And Workflow Routing

- MCP first.
- Curated/local shared skills second.
- Indexed external skills only through registry lookup, not bulk copying.
- Native subagents only when the runtime exposes a real mechanism or the task explicitly supports parallel work.

## Postflight

At the end of substantial work, write back through the generated postflight hook:

```bash
WORKSPACE="{WORKSPACE}" AGENT_NAME=antigravity SUMMARY="..." USER_QUESTION_PROFILE_JSON='{...}' "{AGENT_SHARED_FABRIC_ROOT}/hooks/after-task.sh"
```

Fallback direct script:

```bash
python3 "{AGENT_SHARED_FABRIC_ROOT}/scripts/sync/postflight_sync.py" --global-root "{AGENT_SHARED_FABRIC_ROOT}" --workspace "{WORKSPACE}" --agent antigravity --summary "..." --user-question-profile-json '{...}'
```

Report `[SYNC_OK]` only after postflight succeeds. Do not write directly to `memory/*.ndjson` or `sync/*.ndjson`; use canonical scripts or hooks.
