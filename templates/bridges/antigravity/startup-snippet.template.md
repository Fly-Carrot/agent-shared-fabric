# Antigravity Startup Snippet Template

Use `{AGENT_SHARED_FABRIC_ROOT}` as the canonical Agent Shared Fabric root.
You are operating in workspace `{WORKSPACE}`.
Load the Antigravity bridge at `{WORKSPACE}/.agents/antigravity/ANTIGRAVITY.md`.

Before substantial work, run the generated boot hook:

```bash
WORKSPACE="{WORKSPACE}" AGENT_NAME=antigravity "{AGENT_SHARED_FABRIC_ROOT}/hooks/before-task.sh"
```

Report `[BOOT_OK]` only after the hook succeeds.

For complex or medium tasks, prefer Maestro orchestration when available and keep execution mode gated by human approval. Log phase transitions with:

```bash
WORKSPACE="{WORKSPACE}" AGENT_NAME=antigravity "{AGENT_SHARED_FABRIC_ROOT}/hooks/log-phase.sh" <route|plan|review|dispatch|execute|report> "..."
```

At the end, run postflight through:

```bash
WORKSPACE="{WORKSPACE}" AGENT_NAME=antigravity SUMMARY="..." USER_QUESTION_PROFILE_JSON='{...}' "{AGENT_SHARED_FABRIC_ROOT}/hooks/after-task.sh"
```

Report `[SYNC_OK]` only after success.
