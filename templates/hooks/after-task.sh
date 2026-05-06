#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
GLOBAL_ROOT="${AGENT_SHARED_FABRIC_ROOT:-$DEFAULT_ROOT}"
WORKSPACE="${WORKSPACE:?Set WORKSPACE=/path/to/workspace before running after-task.sh}"
AGENT_NAME="${AGENT_NAME:-${AGENT:-agent}}"
TASK_ID="${TASK_ID:-session}"
SUMMARY="${SUMMARY:?Set SUMMARY before running after-task.sh}"
USER_QUESTION_PROFILE_JSON="${USER_QUESTION_PROFILE_JSON:?Set USER_QUESTION_PROFILE_JSON before running after-task.sh}"

args=(
  --global-root "$GLOBAL_ROOT"
  --workspace "$WORKSPACE"
  --agent "$AGENT_NAME"
  --task-id "$TASK_ID"
  --summary "$SUMMARY"
  --user-question-profile-json "$USER_QUESTION_PROFILE_JSON"
)

[[ -n "${DECISION:-}" ]] && args+=(--decision "$DECISION")
[[ -n "${HANDOFF:-}" ]] && args+=(--handoff "$HANDOFF")
[[ -n "${OPEN_LOOP:-}" ]] && args+=(--open-loop "$OPEN_LOOP")
[[ -n "${PROMOTED_LEARNING:-}" ]] && args+=(--promoted-learning "$PROMOTED_LEARNING")
[[ -n "${MEMPALACE_RECORD:-}" ]] && args+=(--mempalace-record "$MEMPALACE_RECORD")

python3 "$GLOBAL_ROOT/scripts/sync/postflight_sync.py" "${args[@]}"
