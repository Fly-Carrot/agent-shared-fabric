# Customization Guide

Agent Shared Fabric keeps the governance core fixed and lets users attach their own tools.

## What Is Fixed

The fixed core is:

```text
preflight -> sync_all -> context loading -> phase logging -> postflight -> memory lanes -> receipts
```

Do not replace this with ad-hoc scripts if you want runtimes to share discipline.

## What Is Customizable

Users can customize:

- MCP servers
- skill repositories
- workflow prompt directories
- custom subagents
- domain project registries
- runtime-specific mirrors

These should be declared through registries and discovered during preflight/sync-all.

## Add An MCP Server

Edit `mcp/servers.yaml`:

```yaml
version: 1
servers:
  - id: my-server
    enabled: false
    command: /path/to/executable
    args: []
    env_refs:
      - MY_SERVER_TOKEN
    scope: my-capability
```

Keep examples disabled until the command path and environment variables are verified. Keep secrets in environment variables. Do not write API keys into YAML.

## Add A Skill Repository

Edit `skills/sources.yaml`:

```yaml
version: 1
sources:
  - id: my-local-skills
    type: skill_repo
    path: /path/to/agent-fabric-implementation/skills/local
```

Curated or local skills should be preferred before broad external skill indexes.

## Add Workflow Prompts

Edit `workflows/sources.yaml`:

```yaml
version: 1
sources:
  - id: global-workflows
    type: canonical_workflow_dir
    path: /path/to/agent-fabric-implementation/workflows/global
```

Workflows are reusable operating prompts. They are not memory and should not contain private raw task history.

## Add Maestro

Maestro is recommended for explicit subagent orchestration.

Declare it as an MCP server or runtime orchestration target, then route complex tasks through the dispatch phase. Keep execution human-gated when possible.

## Add MemPalace

MemPalace is recommended for process memory.

Use it for detailed trial-and-error, dense debugging history, and temporal context that is too rich for a compact decision log.

The core framework writes local process-memory receipts to `memory/mempalace-records.ndjson`. A MemPalace MCP server can consume or enrich that lane, but the governance core should still run when MemPalace is not installed.

## Security Rules

- Keep secrets in environment variables.
- Do not commit private runtime databases.
- Do not make Fabric App the source of governance truth.
- Prefer generated mirrors over hand-maintained runtime-specific copies.
