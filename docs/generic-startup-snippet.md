# Generic Startup Snippet

Use this snippet when connecting a runtime such as Antigravity, Gemini CLI, Codex, or another coding agent to Agent Shared Fabric.

Replace:

- `{AGENT_SHARED_FABRIC_ROOT}` with the generated governance root, for example `~/AgentSharedFabric/global-agent-fabric`
- `{WORKSPACE}` with the project or workspace the agent is operating in
- `{AGENT_NAME}` with `antigravity`, `gemini`, `codex`, or another runtime id

```text
Use `{AGENT_SHARED_FABRIC_ROOT}` as the canonical Agent Shared Fabric root.
You are operating in workspace `{WORKSPACE}`.
Load the runtime bridge from `{WORKSPACE}/.agents/<runtime>/` if it exists.

Before substantial work, run the generated boot hook:
`WORKSPACE="{WORKSPACE}" AGENT_NAME={AGENT_NAME} "{AGENT_SHARED_FABRIC_ROOT}/hooks/before-task.sh"`

If hooks are not installed yet, run the canonical scripts directly:
`python3 "{AGENT_SHARED_FABRIC_ROOT}/scripts/sync/preflight_check.py" --global-root "{AGENT_SHARED_FABRIC_ROOT}" --workspace "{WORKSPACE}" --agent {AGENT_NAME}`
`python3 "{AGENT_SHARED_FABRIC_ROOT}/scripts/sync/sync_all.py" --global-root "{AGENT_SHARED_FABRIC_ROOT}" --workspace "{WORKSPACE}" --agent {AGENT_NAME}`

Report [BOOT_OK] only after the hook or both canonical scripts execute successfully.
If boot fails, say so explicitly and do not claim shared context was loaded.

Load order:
1. Global shared context from Agent Shared Fabric.
2. Runtime bridge from `.agents/<runtime>/` when present.
3. Current project overlay from `AGENTS.md` and `.agents/sync/`.

For complex tasks, emit phase events:
`WORKSPACE="{WORKSPACE}" AGENT_NAME={AGENT_NAME} "{AGENT_SHARED_FABRIC_ROOT}/hooks/log-phase.sh" <route|plan|review|dispatch|execute|report> "..."`

Dispatch order:
1. MCP first.
2. Curated/local shared skills second.
3. Indexed external skills through registry lookup only.
4. Maestro/native subagents when available and appropriate.
5. Manual script fallback.

For medium or complex tasks, prefer Maestro orchestration when installed and keep execution human-gated.

At the end of substantial work, write back through:
`WORKSPACE="{WORKSPACE}" AGENT_NAME={AGENT_NAME} SUMMARY="..." USER_QUESTION_PROFILE_JSON='{...}' "{AGENT_SHARED_FABRIC_ROOT}/hooks/after-task.sh"`

Report [SYNC_OK] only after postflight succeeds.
Do not write directly to memory/*.ndjson or sync/*.ndjson; use canonical scripts or hooks.
```
