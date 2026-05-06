# Concept Map

## Layer 1: Runtime Entry

Every task begins with an agent runtime:

- Codex
- Gemini CLI
- Antigravity
- future runtimes

The runtime receives user intent, but it does not invent governance from scratch. It enters through Agent Shared Fabric.

## Layer 2: Boot Discipline

The runtime must run:

```text
preflight_check -> sync_all -> context loading
```

This prevents stale local assumptions.

## Layer 3: Context Loading

Context is layered in order:

1. global shared context
2. runtime-specific bridge
3. project overlay

This keeps global governance stable while allowing projects to add local details.

## Layer 4: Fixed Core And Extension Discovery

Agent Shared Fabric has a stable core:

```text
rules + hooks + sync scripts + memory schema + phase discipline
```

It discovers customizable tools through registries:

```text
mcp/servers.yaml + skills/sources.yaml + workflows/sources.yaml + projects/registry.yaml + sync/runtime-map.yaml
```

Preflight and sync-all read these registries before substantial work, so the runtime sees the user's attached MCP servers, skills, workflows, projects, and runtime mirrors without hardcoding them into the framework.

## Layer 5: Routing And Dispatch

Complex work moves through:

```text
route -> plan -> review -> dispatch -> execute -> report
```

The dispatch stage chooses capabilities in this order:

1. MCP server
2. curated/local skill
3. indexed external skill library
4. Maestro or native subagent orchestration
5. manual script fallback

## Layer 6: Write-Back

The final state is not a chat summary. It is structured write-back:

```text
Agent Runtime -> Postflight Sync -> Memory Lanes
```

Memory lanes include:

- decisions
- handoffs
- open loops
- promoted learnings
- process memory
- user-question-profile distillation

## Layer 7: Receipts And Continuation

Memory lanes produce receipts and phase logs for downstream consumers:

```text
Memory Lanes -> Receipts + Phase Logs -> Fabric App
```

Memory lanes also flow back into runtimes:

```text
Memory Lanes -> Agent Runtime
```

This means Fabric App can monitor and visualize the fabric, but the next agent session can continue even without opening the app.
