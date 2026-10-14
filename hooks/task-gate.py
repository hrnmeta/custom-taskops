"""Report changed task files without blocking the Stop event."""

import json
import os
from pathlib import Path
import subprocess
import sys


SCRATCH = {".review", "__pycache__", ".venv", "jobs", "results", ".git"}
CONTENT_DIRS = {"tests", "environment", "solution", "audit"}
TASK_FILES = {"task.toml", "site.toml", "instruction.md", "TASK_NOTES.md", "README.md"}


def git(cwd, *args):
    return subprocess.check_output(
        ["git", *args], cwd=cwd, stderr=subprocess.DEVNULL, timeout=5
    )


def changed_paths(status):
    records = iter(status.split(b"\0"))
    for record in records:
        if not record:
            continue
        yield os.fsdecode(record[3:])
        # Porcelain -z emits destination first, then the original rename path.
        if b"R" in record[:2] or b"C" in record[:2]:
            original = next(records, b"")
            if original:
                yield os.fsdecode(original)


def task_dir(root, relative):
    parent = (root / relative).parent
    while parent == root or root in parent.parents:
        if (parent / "task.toml").is_file() or (parent / "site.toml").is_file():
            return parent
        if parent == root:
            break
        parent = parent.parent
    return None


def report(payload):
    if not isinstance(payload, dict) or payload.get("stop_hook_active"):
        return
    cwd = payload.get("cwd", os.getcwd())
    if not isinstance(cwd, str) or not Path(cwd).is_dir():
        return
    root = Path(os.fsdecode(git(cwd, "rev-parse", "--show-toplevel")).rstrip("\n"))
    changes = {}
    for relative in changed_paths(
        git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    ):
        path = Path(relative)
        if SCRATCH.intersection(path.parts):
            continue
        if path.name not in TASK_FILES and not CONTENT_DIRS.intersection(path.parts):
            continue
        directory = task_dir(root, relative)
        # A repository README by itself is not evidence of a benchmark task.
        if directory is None and path.name in {"README.md", "TASK_NOTES.md"}:
            continue
        key = str(directory.relative_to(root)) if directory else "unknown-track:" + str(path.parent)
        substantive = path.name not in {"README.md", "TASK_NOTES.md"}
        previous = changes.get(key)
        changes[key] = (directory, substantive or bool(previous and previous[1]))

    for name, (directory, substantive) in sorted(changes.items())[:6]:
        kind = "SUBSTANTIVE" if substantive else "DOCUMENTATION"
        line = f"task-gate: {name}: task files changed ({kind})"
        if directory and (directory / "task.toml").is_file():
            # Only recognize the concrete TBench layout; other task.toml tracks
            # require their own profile. Docker is optional in the profile.
            if (directory / "tests/test.sh").is_file() or (directory / "environment/Dockerfile").is_file():
                missing = [p for p in ("instruction.md", "tests/test.sh") if not (directory / p).is_file()]
                line += "; structure " + ("MISSING: " + ", ".join(missing) if missing else "ok")
            else:
                line += "; layout checks deferred to track profile"
        else:
            line += "; layout checks deferred to track profile"
        print(line)
    if len(changes) > 6:
        print(f"task-gate: {len(changes) - 6} additional affected task directories")
    if changes:
        print("task-gate: next: follow the operation's sanity, official review, and empirical gates before commit.")


if __name__ == "__main__":
    try:
        report(json.load(sys.stdin))
    except (ValueError, OSError, subprocess.SubprocessError):
        # Invalid input, missing Git, and timeouts must remain non-blocking.
        pass
