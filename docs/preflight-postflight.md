# Preflight And Postflight

## Preflight

Preflight answers one question:

> Is this runtime allowed to start substantial work from this context?

A preflight check validates:

- the governance root exists
- required rules and registries exist
- registry files have the expected top-level shape, such as `version`, `servers`, or `sources`
- hook templates are present in generated installs
- the workspace exists
- the runtime knows its agent name
- the task has an id

It should fail loudly. A failed boot must not be described as conceptually loaded.

## Sync-All

`sync_all.py` is the import/export bridge.

In a full installation it can:

- import runtime-native records
- export generated mirrors
- refresh workspace context
- read MCP/skills/workflow/project registries
- write a session-start receipt

The public template implementation writes a minimal receipt so the contract is runnable.

## Phase Logging

`log_task_phase.py` appends exact phase events.

The valid keys are:

```text
route
plan
review
dispatch
execute
report
```

Do not invent synonyms if downstream tools expect these keys.

The keys are a governance sequence, not a hard scheduler by default. The public hook validates the exact phase names. A stricter harness may enforce ordering, but the base framework keeps ordering advisory so runtimes can recover, retry, or log late phases without corrupting the receipt stream.

## Postflight

Postflight answers another question:

> What durable state should survive this session?

The flow is:

```text
Agent Runtime -> Postflight Sync -> Memory Lanes -> Receipts + Phase Logs -> Fabric App
                                   -> Memory Lanes -> Next Agent Runtime
```

Postflight writes structured records into lanes:

- decision
- handoff
- open loop
- promoted learning
- process memory
- user-question profile
- receipt

The public script supports lightweight receipt-only postflight for simple tasks. For substantial or full-sync tasks, use `hooks/after-task.sh`; it requires `USER_QUESTION_PROFILE_JSON` and only then should the runtime claim a complete synchronization.
