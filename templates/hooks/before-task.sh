#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
GLOBAL_ROOT="${AGENT_SHARED_FABRIC_ROOT:-$DEFAULT_ROOT}"
WORKSPACE="${WORKSPACE:?Set WORKSPACE=/path/to/workspace before running before-task.sh}"
AGENT_NAME="${AGENT_NAME:-${AGENT:-agent}}"
TASK_ID="${TASK_ID:-session}"

python3 "$GLOBAL_ROOT/scripts/sync/preflight_check.py" \
  --global-root "$GLOBAL_ROOT" \
  --workspace "$WORKSPACE" \
  --agent "$AGENT_NAME" \
  --task-id "$TASK_ID"

python3 "$GLOBAL_ROOT/scripts/sync/sync_all.py" \
  --global-root "$GLOBAL_ROOT" \
  --workspace "$WORKSPACE" \
  --agent "$AGENT_NAME" \
  --task-id "$TASK_ID"
