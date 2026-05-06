# Hooks And Prompts

Agent Shared Fabric is strongest when prompts and hooks work together.

## Prompt Contract

Prompt-first mode is the most portable mode.

Paste the generated startup snippet at the beginning of a runtime session. The snippet tells the agent:

1. where the canonical fabric root is
2. which workspace it is operating in
3. which hook scripts and canonical scripts must run
4. what phase keys are valid
5. how to write postflight
6. when it may report `[BOOT_OK]` and `[SYNC_OK]`

Prompts make the contract visible to the model.

## Hook Contract

Hook mode wraps runtime entry, phase transitions, and exit with executable scripts.

Generated hooks:

```text
hooks/before-task.sh
hooks/log-phase.sh
hooks/after-task.sh
```

Minimal flow:

```text
before-task:
  preflight_check.py
  sync_all.py
  emit [BOOT_OK] only if both succeed

during-task:
  log_task_phase.py route|plan|review|dispatch|execute|report

after-task:
  postflight_sync.py
  require user-question-profile payload
  emit [SYNC_OK] only if write-back succeeds
```

Hooks reduce agent forgetfulness. Prompts are still needed because the model must understand why the hooks exist and how to interpret receipts.

## Recommended Hybrid

Use both:

```text
before-task hook -> startup prompt -> phase hook(s) -> after-task hook
```

The prompt is the model-visible rulebook. The hook is the executable guardrail. Receipts are the audit trail.
