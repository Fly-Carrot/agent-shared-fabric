# Antigravity Startup Snippet Template

Use `{AGENT_SHARED_FABRIC_ROOT}` as the canonical Agent Shared Fabric root.
You are operating in workspace `{WORKSPACE}`.
Load the Antigravity bridge at `{WORKSPACE}/.agents/antigravity/ANTIGRAVITY.md`.

Run canonical boot before substantial work.
Report `[BOOT_OK]` only after success.

For complex or medium tasks, prefer Maestro orchestration when available and keep execution mode gated by human approval.

At the end, run postflight sync and report `[SYNC_OK]` only after success.
