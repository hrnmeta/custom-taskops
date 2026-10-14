# Existing-task evidence baseline

Do not rerun a full pre-edit sanity gate when authoritative evidence already
establishes the relevant state of the exact current task content.

Before reading remote baseline evidence, confirm that the staged target belongs
to the authenticated user through the mine-scoped CLI process in
`difficulty-source-discovery.md`. Reuse the operation's fresh listing when
available. For an unstaged task, use local validation; do not fetch another
user's task as a substitute baseline.

## Difficulty and context tuning

Before research or edits:

1. Confirm the task working tree has no task-scoped changes relative to the
   revision identified by Codimango. A commit label alone is insufficient when
   local task content differs.
2. Reuse current-revision platform evidence only when it shows the applicable
   structural and build checks passing, every configured oracle trial passing,
   the required pristine/no-solution direction failing, and no unresolved
   blocking validation or quality defect. Preserve the job, trial, revision,
   verifier, and environment identities.
3. Perform only cheap local consistency checks before editing: required files
   and verifier entrypoint still exist, manifest classification parses, and the
   evidence revision matches the task content. Do not rerun the suites merely
   to reproduce valid exact-content platform evidence.
4. If any required signal is missing, stale, ambiguous, failing, or mismatched
   to local content, run the full `sanity-check` baseline. Route a failure
   to repair rather than tuning an invalid task.

This optimization applies only to the pre-edit baseline. Every changed attempt
must still run a full post-edit sanity gate before review or empirical trials.

## Quality repair

For `quality-fix`, collect the exact-current-commit Codimango brief before
deciding whether local baseline execution is needed. When the local task
matches that commit and the brief completely accounts for structural, build,
oracle, pristine/no-solution, and other blocking validation signals, reuse both
its passes and failures. Failures are repair inputs, not reasons to reproduce
the same failure locally.

Run the cheap local consistency checks above. Run full pre-edit sanity only
when local content differs, material execution evidence is missing or
ambiguous, or local reproduction is necessary to identify the root cause. Full
post-edit sanity and independent review remain mandatory.
