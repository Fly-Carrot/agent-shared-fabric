#!/usr/bin/env python3
"""Initialize a local Agent Shared Fabric skeleton.

This intentionally creates two sibling roots:
- governance root: rules, registries, sync scripts, memory schemas, receipts
- implementation root: skills, MCP implementations, workflows, subagents

The goal is not to copy a personal setup. The goal is to make the contract
runnable so a runtime can boot, log phases, and write postflight receipts.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

PRE_FLIGHT = r'''#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED = [
    "rules/global/agent-shared-fabric.md",
    "hooks/before-task.sh",
    "hooks/log-phase.sh",
    "hooks/after-task.sh",
    "sync/runtime-map.yaml",
    "sync/boot-sequence.md",
    "mcp/servers.yaml",
    "skills/sources.yaml",
    "workflows/sources.yaml",
    "memory/schema.yaml",
    "projects/registry.yaml",
]

REGISTRY_EXPECTATIONS = {
    "mcp/servers.yaml": ["version", "servers"],
    "skills/sources.yaml": ["version", "sources"],
    "workflows/sources.yaml": ["version", "sources"],
    "memory/schema.yaml": ["version"],
    "projects/registry.yaml": ["version"],
    "sync/runtime-map.yaml": ["version"],
}


def has_top_level_key(text: str, key: str) -> bool:
    return re.search(rf"^{re.escape(key)}\s*:", text, flags=re.MULTILINE) is not None


def validate_registry_shape(root: Path) -> list[dict]:
    errors = []
    try:
        import yaml  # type: ignore
    except Exception:
        yaml = None

    for rel, required_keys in REGISTRY_EXPECTATIONS.items():
        path = root / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "\t" in text:
            errors.append({"path": rel, "error": "YAML files must not contain tab indentation"})
        missing = [key for key in required_keys if not has_top_level_key(text, key)]
        if missing:
            errors.append({"path": rel, "error": f"missing top-level keys: {', '.join(missing)}"})
        if yaml is not None:
            try:
                parsed = yaml.safe_load(text)
            except Exception as exc:
                errors.append({"path": rel, "error": f"YAML parse failed: {exc}"})
                continue
            if not isinstance(parsed, dict):
                errors.append({"path": rel, "error": "YAML root must be a mapping"})
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Agent Shared Fabric before substantial work.")
    parser.add_argument("--global-root", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--task-id", default="session")
    args = parser.parse_args()

    root = args.global_root.expanduser().resolve()
    workspace = args.workspace.expanduser().resolve()
    missing = [item for item in REQUIRED if not (root / item).exists()]
    registry_errors = validate_registry_shape(root)
    ok = not missing and not registry_errors and workspace.exists()
    payload = {
        "status": "ok" if ok else "failed",
        "status_marker": "[BOOT_OK]" if ok else "[BOOT_FAILED]",
        "global_root": str(root),
        "workspace": str(workspace),
        "agent": args.agent,
        "task_id": args.task_id,
        "missing_global_files": missing,
        "registry_errors": registry_errors,
        "workspace_exists": workspace.exists(),
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

SYNC_ALL = r'''#!/usr/bin/env python3
from __future__ import annotations

import argparse
try:
    import fcntl
except Exception:  # pragma: no cover - Windows fallback
    fcntl = None
import json
from datetime import UTC, datetime
from pathlib import Path


def append_ndjson(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    with lock_path.open("w", encoding="utf-8") as lock:
        if fcntl is not None:
            fcntl.flock(lock, fcntl.LOCK_EX)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        if fcntl is not None:
            fcntl.flock(lock, fcntl.LOCK_UN)


def main() -> int:
    parser = argparse.ArgumentParser(description="Synchronize runtime mirrors and write a session-start receipt.")
    parser.add_argument("--global-root", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--task-id", default="session")
    args = parser.parse_args()

    root = args.global_root.expanduser().resolve()
    workspace = args.workspace.expanduser().resolve()
    now = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    receipt = {
        "type": "session_start",
        "timestamp": now,
        "agent": args.agent,
        "task_id": args.task_id,
        "workspace": str(workspace),
        "status_marker": "[BOOT_OK]",
    }
    append_ndjson(root / "sync" / "receipts.ndjson", receipt)
    print(json.dumps({"status": "ok", "status_marker": "[BOOT_OK]", "receipt": receipt}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

LOG_PHASE = r'''#!/usr/bin/env python3
from __future__ import annotations

import argparse
try:
    import fcntl
except Exception:  # pragma: no cover - Windows fallback
    fcntl = None
import json
from datetime import UTC, datetime
from pathlib import Path

PHASES = {"route", "plan", "review", "dispatch", "execute", "report"}


def append_ndjson(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    with lock_path.open("w", encoding="utf-8") as lock:
        if fcntl is not None:
            fcntl.flock(lock, fcntl.LOCK_EX)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        if fcntl is not None:
            fcntl.flock(lock, fcntl.LOCK_UN)


def main() -> int:
    parser = argparse.ArgumentParser(description="Append an exact six-stage phase event.")
    parser.add_argument("--global-root", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--phase", required=True, choices=sorted(PHASES))
    parser.add_argument("--task-id", default="session")
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    record = {
        "timestamp": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "agent": args.agent,
        "workspace": str(args.workspace.expanduser().resolve()),
        "task_id": args.task_id,
        "phase": args.phase,
        "note": args.note,
    }
    target = args.global_root.expanduser().resolve() / "sync" / "task_phases.ndjson"
    append_ndjson(target, record)
    print(json.dumps({"status": "written", "phase_key": args.phase, "target": str(target)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

POSTFLIGHT = r'''#!/usr/bin/env python3
from __future__ import annotations

import argparse
try:
    import fcntl
except Exception:  # pragma: no cover - Windows fallback
    fcntl = None
import json
from datetime import UTC, datetime
from pathlib import Path

LANE_FILES = {
    "decision": "memory/decision-log.ndjson",
    "handoff": "memory/handoffs.ndjson",
    "open_loop": "memory/open-loops.ndjson",
    "promoted_learning": "memory/promoted-learnings.ndjson",
    "mempalace_record": "memory/mempalace-records.ndjson",
}

REQUIRED_PROFILE_FIELDS = [
    "focus_points",
    "question_patterns",
    "response_preferences",
    "reasoning_preferences",
    "recurring_themes",
    "frictions_or_anxieties",
]


def append_ndjson(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    with lock_path.open("w", encoding="utf-8") as lock:
        if fcntl is not None:
            fcntl.flock(lock, fcntl.LOCK_EX)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        if fcntl is not None:
            fcntl.flock(lock, fcntl.LOCK_UN)


def main() -> int:
    parser = argparse.ArgumentParser(description="Write structured Agent Shared Fabric postflight records.")
    parser.add_argument("--global-root", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--task-id", default="session")
    parser.add_argument("--decision", action="append", default=[])
    parser.add_argument("--handoff", action="append", default=[])
    parser.add_argument("--open-loop", action="append", default=[])
    parser.add_argument("--promoted-learning", action="append", default=[])
    parser.add_argument("--mempalace-record", action="append", default=[])
    parser.add_argument("--user-question-profile-json", default="")
    args = parser.parse_args()

    root = args.global_root.expanduser().resolve()
    workspace = args.workspace.expanduser().resolve()
    now = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    base = {"timestamp": now, "agent": args.agent, "workspace": str(workspace), "task_id": args.task_id}

    writes = {"receipts": 0, "user_question_profiles": 0}
    for key, values in {
        "decision": args.decision,
        "handoff": args.handoff,
        "open_loop": args.open_loop,
        "promoted_learning": args.promoted_learning,
        "mempalace_record": args.mempalace_record,
    }.items():
        for value in values:
            append_ndjson(root / LANE_FILES[key], {**base, "type": key, "summary": value})
            writes[key] = writes.get(key, 0) + 1

    if args.user_question_profile_json:
        profile = json.loads(args.user_question_profile_json)
        missing = [field for field in REQUIRED_PROFILE_FIELDS if field not in profile]
        if missing:
            raise SystemExit(f"User question profile payload is missing required fields: {', '.join(missing)}")
        append_ndjson(root / "memory" / "user-question-profiles.ndjson", {**base, "type": "user_question_profile", **profile})
        writes["user_question_profiles"] += 1

    writes["receipts"] += 1
    receipt = {**base, "type": "session_end", "summary": args.summary, "status_marker": "[SYNC_OK]", "writes": writes}
    append_ndjson(root / "sync" / "receipts.ndjson", receipt)
    print(json.dumps({"status": "written", "status_marker": "[SYNC_OK]", "writes": writes}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def copy_template(src_rel: str, dst: Path) -> None:
    src = REPO_ROOT / src_rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def backup_existing(path: Path) -> Path:
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    backup = path.with_name(f"{path.name}.{timestamp}.bak")
    shutil.copy2(path, backup)
    return backup


def write_text(path: Path, content: str, executable: bool = False, *, force: bool = False, backup: bool = False) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return {"path": str(path), "status": "skipped", "reason": "exists"}
    backup_path = ""
    if path.exists() and backup:
        backup_path = str(backup_existing(path))
    path.write_text(content, encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | 0o111)
    return {"path": str(path), "status": "written", "backup": backup_path}


def render_startup_snippet(root: Path, workspace: Path) -> str:
    return f"""Use `{root}` as the canonical Agent Shared Fabric root.
You are operating in workspace `{workspace}`.
Load the runtime bridge from `{workspace}/.agents/<runtime>/` if it exists.

Before substantial work, run the generated boot hook:

`WORKSPACE="{workspace}" AGENT_NAME=<runtime> "{root / 'hooks/before-task.sh'}"`

If hooks are not installed yet, run the canonical scripts directly:

`python3 "{root / 'scripts/sync/preflight_check.py'}" --global-root "{root}" --workspace "{workspace}" --agent <runtime>`
`python3 "{root / 'scripts/sync/sync_all.py'}" --global-root "{root}" --workspace "{workspace}" --agent <runtime>`

Report `[BOOT_OK]` only after the hook or both canonical scripts execute successfully.
If boot fails, say so explicitly and do not claim shared context was loaded.

Load global context first, runtime bridge second, project overlay third.

For complex work, log exact phases with the generated phase hook:

`WORKSPACE="{workspace}" AGENT_NAME=<runtime> "{root / 'hooks/log-phase.sh'}" <route|plan|review|dispatch|execute|report> "..."`

Dispatch order:
1. MCP first.
2. Curated/local shared skills second.
3. Indexed external skills through registry lookup only.
4. Maestro/native subagents when available and appropriate.
5. Manual script fallback.

For medium or complex tasks, prefer Maestro orchestration when installed and keep execution human-gated.

At the end, write back through the generated postflight hook:

`WORKSPACE="{workspace}" AGENT_NAME=<runtime> SUMMARY="..." USER_QUESTION_PROFILE_JSON='{{...}}' "{root / 'hooks/after-task.sh'}"`

Fallback direct script:

`python3 "{root / 'scripts/sync/postflight_sync.py'}" --global-root "{root}" --workspace "{workspace}" --agent <runtime> --summary "..." --user-question-profile-json '{{...}}'`

Report `[SYNC_OK]` only after postflight succeeds.
Do not write directly to memory/*.ndjson or sync/*.ndjson; use canonical scripts or hooks.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a local Agent Shared Fabric skeleton.")
    parser.add_argument("--root", type=Path, required=True, help="Governance root to create, e.g. ~/AgentSharedFabric/global-agent-fabric")
    parser.add_argument("--implementation-root", type=Path, default=None, help="Parallel implementation body root. Defaults to a sibling named agent-fabric-implementation.")
    parser.add_argument("--workspace", type=Path, default=None, help="Optional workspace to bridge with AGENTS.md and startup snippet.")
    parser.add_argument("--force", action="store_true", help="Overwrite generated template files when they already exist.")
    parser.add_argument("--backup", action="store_true", help="Back up existing files before overwriting with --force.")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    body = (args.implementation_root or (root.parent / "agent-fabric-implementation")).expanduser().resolve()
    workspace = args.workspace.expanduser().resolve() if args.workspace else None

    dirs = [
        root / "rules/global",
        root / "mcp",
        root / "skills",
        root / "workflows",
        root / "memory",
        root / "projects",
        root / "sync",
        root / "hooks",
        root / "scripts/sync",
        body / "skills/curated",
        body / "skills/local",
        body / "mcp",
        body / "workflows/global",
        body / "agents",
    ]
    for directory in dirs:
        directory.mkdir(parents=True, exist_ok=True)

    template_map = {
        "templates/governance-core/rules/global/agent-shared-fabric.md": root / "rules/global/agent-shared-fabric.md",
        "templates/governance-core/layout/agent-shared-fabric.tree": root / "LAYOUT.tree",
        "templates/governance-core/hooks/before-task.sh": root / "hooks/before-task.sh",
        "templates/governance-core/hooks/log-phase.sh": root / "hooks/log-phase.sh",
        "templates/governance-core/hooks/after-task.sh": root / "hooks/after-task.sh",
        "templates/governance-core/sync/boot-sequence.md": root / "sync/boot-sequence.md",
        "templates/governance-core/sync/runtime-map.example.yaml": root / "sync/runtime-map.yaml",
        "templates/governance-core/mcp/servers.example.yaml": root / "mcp/servers.yaml",
        "templates/governance-core/skills/sources.example.yaml": root / "skills/sources.yaml",
        "templates/governance-core/workflows/sources.example.yaml": root / "workflows/sources.yaml",
        "templates/governance-core/memory/schema.example.yaml": root / "memory/schema.yaml",
        "templates/governance-core/projects/registry.example.yaml": root / "projects/registry.yaml",
    }
    writes = []
    for src_rel, dst in template_map.items():
        if args.force or not dst.exists():
            if dst.exists() and args.backup:
                writes.append({"path": str(dst), "status": "backed_up", "backup": str(backup_existing(dst))})
            copy_template(src_rel, dst)
            writes.append({"path": str(dst), "status": "written"})
        else:
            writes.append({"path": str(dst), "status": "skipped", "reason": "exists"})

    writes.append(write_text(root / "scripts/sync/preflight_check.py", PRE_FLIGHT, executable=True, force=args.force, backup=args.backup))
    writes.append(write_text(root / "scripts/sync/sync_all.py", SYNC_ALL, executable=True, force=args.force, backup=args.backup))
    writes.append(write_text(root / "scripts/sync/log_task_phase.py", LOG_PHASE, executable=True, force=args.force, backup=args.backup))
    writes.append(write_text(root / "scripts/sync/postflight_sync.py", POSTFLIGHT, executable=True, force=args.force, backup=args.backup))

    writes.append(write_text(body / "README.md", f"""# Agent Fabric Implementation Body

This root is intentionally parallel to the governance root.

- Governance root: `{root}`
- Implementation body: `{body}`

Put heavy implementations here: skills, MCP servers, global workflows, and custom subagents.
Reference them from the governance root through YAML registries instead of copying them into the governance brain.

Recommended extension points:

- Add MCP servers in `{root / 'mcp/servers.yaml'}`
- Add skill repositories in `{root / 'skills/sources.yaml'}`
- Add workflow prompt directories in `{root / 'workflows/sources.yaml'}`
- Add custom subagents in this implementation root and route them through Maestro or the runtime bridge
- Keep secrets in environment variables, not in registries
""", force=args.force, backup=args.backup))

    if workspace:
        writes.append(write_text(workspace / "AGENTS.md", f"""# Agent Shared Fabric Workspace Bridge

Use `{root}` as the canonical Agent Shared Fabric root.
Load this file as the project overlay after global and runtime context.

Startup snippet: `.agents/agent-shared-fabric/startup-snippet.md`
""", force=args.force, backup=args.backup))
        writes.append(write_text(workspace / ".agents/agent-shared-fabric/startup-snippet.md", render_startup_snippet(root, workspace), force=args.force, backup=args.backup))

    summary = {
        "status": "ok",
        "governance_root": str(root),
        "implementation_root": str(body),
        "workspace": str(workspace) if workspace else None,
        "writes": writes,
        "next_boot": [
            f"WORKSPACE=\"{workspace or '<workspace>'}\" AGENT_NAME=codex \"{root / 'hooks/before-task.sh'}\"",
        ],
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
