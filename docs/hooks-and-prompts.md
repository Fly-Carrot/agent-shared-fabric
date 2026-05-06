# Hooks And Prompts

Agent Shared Fabric can be activated in two ways.

## Prompt-First Mode

This is the most portable mode.

Paste the generated startup snippet at the beginning of a runtime session. The snippet tells the agent:

1. where the canonical fabric root is
2. which workspace it is operating in
3. which boot scripts must run
4. what phase keys are valid
5. how to write postflight
6. when it may report `[BOOT_OK]` and `[SYNC_OK]`

Prompt-first mode is useful when a runtime does not expose reliable hooks.

## Hook Mode

Hook mode wraps runtime entry and exit with scripts.

A minimal hook flow is:

```text
before_task:
  preflight_check.py
  sync_all.py
  load global/runtimes/project context

during_task:
  log_task_phase.py route|plan|review|dispatch|execute|report

after_task:
  postflight_sync.py
```

Hooks are stronger than prompts because they reduce agent forgetfulness. Prompts are still useful because they make the contract visible to the model.

## Recommended Hybrid

Use both:

- hook scripts enforce the minimum state transition
- startup prompts teach the runtime the discipline
- receipts prove what happened
- apps consume receipts, not hidden runtime assumptions
