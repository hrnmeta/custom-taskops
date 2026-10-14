#!/bin/sh
# Resolve the helper relative to the installed hook, preserving JSON stdin.
# The advisory hook must never prevent the agent from stopping.
command -v python3 >/dev/null 2>&1 || exit 0
python3 "$(dirname "$0")/task-gate.py" || true
exit 0
