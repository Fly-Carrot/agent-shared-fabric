#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
GLOBAL_ROOT="${AGENT_SHARED_FABRIC_ROOT:-$DEFAULT_ROOT}"
WORKSPACE="${WORKSPACE:?Set WORKSPACE=/path/to/workspace before running log-phase.sh}"
AGENT_NAME="${AGENT_NAME:-${AGENT:-agent}}"
TASK_ID="${TASK_ID:-session}"
PHASE="${1:-${PHASE:-}}"
NOTE="${2:-${NOTE:-}}"

case "$PHASE" in
  route|plan|review|dispatch|execute|report) ;;
  *) echo "Invalid phase: $PHASE" >&2; echo "Use: route | plan | review | dispatch | execute | report" >&2; exit 2 ;;
esac

python3 "$GLOBAL_ROOT/scripts/sync/log_task_phase.py" \
  --global-root "$GLOBAL_ROOT" \
  --workspace "$WORKSPACE" \
  --agent "$AGENT_NAME" \
  --task-id "$TASK_ID" \
  --phase "$PHASE" \
  --note "$NOTE"
