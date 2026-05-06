# Agent Shared Fabric Global Rule Template

Use the configured Agent Shared Fabric root as canonical.

Before substantial work:

1. run preflight
2. run sync-all
3. load global context
4. load runtime bridge
5. load project overlay
6. report `[BOOT_OK]` only after success

For complex work, emit these exact phase keys:

```text
route
plan
review
dispatch
execute
report
```

Do not write directly to memory or sync logs. Use canonical scripts.

At the end of substantial work, run postflight sync and report `[SYNC_OK]` only after success.
