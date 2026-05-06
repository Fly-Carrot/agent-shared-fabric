# Preflight And Postflight

## Preflight

Preflight answers one question:

> Is this runtime allowed to start substantial work from this context?

A preflight check validates:

- the governance root exists
- required rules and registries exist
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

## Postflight

Postflight answers another question:

> What durable state should survive this session?

Postflight writes structured records into lanes:

- decision
- handoff
- open loop
- promoted learning
- process memory
- user-question profile
- receipt

A task is not fully synced until postflight succeeds.
