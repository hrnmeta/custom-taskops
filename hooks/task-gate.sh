#!/bin/sh
# task-gate: fast, non-blocking Stop hook for benchmark task repos.
# Prints a compact verdict only when task files changed; silent otherwise.
# Never blocks: always exits 0.
INPUT=$(cat)

# Avoid nag loops: stay silent once a Stop hook already fired this session.
if printf '%s' "$INPUT" | grep -q '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  exit 0
fi

CWD=$(printf '%s' "$INPUT" | sed -n 's/.*"cwd"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1)
if [ -n "$CWD" ] && [ -d "$CWD" ]; then
  cd "$CWD" || exit 0
fi

command -v git >/dev/null 2>&1 || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

CHANGED=$(git status --porcelain 2>/dev/null | cut -c4- | sed 's/.* -> //' | grep -E '(^|/)(task\.toml|instruction\.md|TASK_NOTES\.md|README\.md|tests/|environment/|solution/|audit/)' || true)
[ -z "$CHANGED" ] && exit 0

# Classify and locate affected task dirs (tbench: walk up to task.toml).
DIRS=""
CLASS="TRIVIAL"
for f in $CHANGED; do
  case "$f" in
    */tests/*|*/environment/*|*/solution/*|*/instruction.md|*/task.toml|tests/*|environment/*|solution/*|instruction.md|task.toml)
      CLASS="SUBSTANTIVE" ;;
  esac
  d=$(dirname "$f")
  while [ "$d" != "." ] && [ ! -f "$d/task.toml" ]; do d=$(dirname "$d"); done
  if [ -f "$d/task.toml" ]; then
    DIRS="$DIRS $d"
  else
    DIRS="$DIRS unknown-track:$(echo "$f" | cut -d/ -f1)"
  fi
done
DIRS=$(printf '%s\n' $DIRS | sort -u)

OUT=""
for d in $DIRS; do
  case "$d" in
    unknown-track:*)
      OUT="$OUT
task-gate: $d: non-tbench layout, static checks skipped ($CLASS)"
      ;;
    *)
      MISSING=""
      [ -f "$d/instruction.md" ] || MISSING="$MISSING instruction.md"
      [ -f "$d/environment/Dockerfile" ] || MISSING="$MISSING environment/Dockerfile"
      [ -f "$d/tests/test.sh" ] || MISSING="$MISSING tests/test.sh"
      LINE="task-gate: $d: structure"
      if [ -z "$MISSING" ]; then LINE="$LINE ok"; else LINE="$LINE MISSING:$MISSING"; fi
      LINE="$LINE; metadata deferred to current track schema"
      OUT="$OUT
$LINE ($CLASS)"
      ;;
  esac
done

if [ "$CLASS" = "SUBSTANTIVE" ]; then
  OUT="$OUT
task-gate: next: run sanity-check, then the track's official review before commit."
else
  OUT="$OUT
task-gate: next: trivial change, no review needed."
fi
printf '%s\n' "$OUT" | head -n 8
exit 0
