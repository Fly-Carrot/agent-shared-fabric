# Boot Sequence Template

1. Resolve the workspace.
2. Resolve the Agent Shared Fabric root.
3. Run preflight.
4. Run sync-all.
5. Load global shared context.
6. Load runtime bridge context.
7. Load project overlay.
8. Report `[BOOT_OK]` only after the real boot scripts succeed.
