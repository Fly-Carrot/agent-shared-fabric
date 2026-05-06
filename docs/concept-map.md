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

## Layer 4: Routing And Dispatch

Complex work moves through:

```text
route -> plan -> review -> dispatch -> execute -> report
```

The dispatch stage chooses tools in this order:

1. MCP server
2. curated/local skill
3. indexed external skill library
4. native subagent or Maestro orchestration
5. manual script fallback

## Layer 5: Write-Back

The final state is not a chat summary. It is structured write-back:

- decisions
- handoffs
- open loops
- promoted learnings
- process memory
- receipts
- user-question-profile distillation

## Layer 6: Downstream Consumers

Downstream apps can read the fabric outputs.

Fabric App is one such downstream consumer. It can visualize receipts, monitor operations, and connect fabric outputs to an Obsidian knowledge-base pipeline.
