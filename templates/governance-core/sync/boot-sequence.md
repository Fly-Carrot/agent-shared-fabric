# Boot Sequence Template

The recommended boot path is hybrid: executable hook first, model-visible prompt second.

1. Resolve the workspace.
2. Resolve the Agent Shared Fabric root.
3. Run `hooks/before-task.sh`.
4. The hook runs `preflight_check.py`.
5. The hook runs `sync_all.py`.
6. Load global shared context.
7. Load runtime bridge context.
8. Load project overlay.
9. Paste or load the startup prompt so the model understands the contract.
10. Report `[BOOT_OK]` only after the real hook and boot scripts succeed.

During complex work, log phase transitions with `hooks/log-phase.sh`.

At the end of substantial work, run `hooks/after-task.sh` and report `[SYNC_OK]` only after postflight succeeds.
