# Commit workflow: single commit after review passes

Canonical final step for producing skills (`create-task`,
`ease-task`, `harden-task`, `increase-context-tokens`,
`quality-fix`).
`sanity-check` never commits, standalone or otherwise. Reviews in the task
operation are verification steps; the commit lives only here, at the end of the
higher-level loop.

## Gate

- Require the README policy gate from `readme-authorship.md`: all changed task
  READMEs must have matching official generation evidence and no task-edit
  changelogs/history. Do not stage hand-authored README fixes or commit an
  unresolved documentation-policy failure.

- Commit only when the official review passes and every
  operation-specific gate passes. Hardening must meet its empirical target;
  easing must preserve the validation-gate target; context growth must show
  comparable measured progress. Follow `difficulty-calibration.md`,
  `hardening-calibration.md`, and `context-calibration.md` respectively.
  The same empirical gates apply when `quality-fix` adopts one of these
  tuning policies; the outer workflow still owns the single commit.
- On any unresolved sanity, review, or empirical failure: do not commit.
  After the third failed validation attempt, stop before further fixes or
  retries, report the attempt ledger, and leave the tree uncommitted.
  Attempt 3 may commit when all required gates pass on its unchanged candidate.
- On explicit user opt-out ("don't commit"): do not commit.

## Procedure

1. Scope: `git status --porcelain -- <task-dir>`; commit only this
   operation's task files by path. Never `add -A` / `add .`.
2. Exclude scratch: never commit `.review/`, `__pycache__/`, `.venv/`,
   `jobs/`, or `results/`.
3. Single commit: stage the op's files and write one commit, e.g.
   `ease <task>: clarify spec paths and relax strict assertion`.
4. If the tree holds unrelated changes you cannot account for, leave them
   untouched — commit only your paths, and say what you left out.

## Output

Report the commit SHA (or that nothing was committed, and why).
