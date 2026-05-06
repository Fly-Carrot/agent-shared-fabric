# Department Routing

Agent Shared Fabric treats the six stages as governance departments.

They do not have to be separate folders or separate agents. They are mandatory operating directions that every complex task must pass through.

This pattern is inspired by [cft0808/edict](https://github.com/cft0808/edict), which demonstrates a staged multi-agent governance flow. Agent Shared Fabric uses its own runtime-agnostic phase keys and is not affiliated with edict.

## Canonical Departments

| Phase | Department meaning | Required output |
| --- | --- | --- |
| `route` | Task classification and runtime selection | classify simple / medium / complex and choose direct, skill, MCP, or orchestration path |
| `plan` | Implementation plan and decomposition | state intended changes, ownership, order, and verification path |
| `review` | Feasibility and risk gate | check scope, safety, missing context, and likely failure modes |
| `dispatch` | Capability routing | choose MCP -> curated skills -> indexed skills -> Maestro/native subagent -> script |
| `execute` | Bounded execution | mutate only within planned scope and verify results |
| `report` | Postflight and handoff | write durable records, receipts, open loops, and user-question-profile distillation |

## Why This Matters

A folder tree alone cannot enforce discipline. The departments become reliable only when they are tied to:

- prompt instructions
- hook scripts
- phase receipts
- runtime bridge files
- postflight memory lanes

Future installations may map departments to Maestro agents or native runtime subagents, but the phase keys should remain stable.
