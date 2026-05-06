# Fabric App Boundary

Fabric App and Agent Shared Fabric should not be collapsed into one product concept.

## Agent Shared Fabric

Agent Shared Fabric answers:

> How do multiple agents share rules, memory, receipts, tools, workflows, and discipline?

It is the governance and coordination architecture.

## Fabric App

Fabric App answers:

> How does a human operate a knowledge-base workstation that consumes receipts, source artifacts, wiki pages, graphs, and terminal workflows?

It is the UI and knowledge management layer.

## Clean Boundary

Agent Shared Fabric produces:

- receipts
- phase logs
- memory lanes
- registries
- runtime mirrors
- project overlays

Fabric App consumes:

- receipts and logs for monitoring
- project registry for workspace selection
- source artifacts for processing
- wiki indexes for browsing
- graph JSON for visualization
- terminal access for maintenance

Fabric App should not own canonical agent governance.
