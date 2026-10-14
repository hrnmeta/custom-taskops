# Canonical task-change and review loop

Every skill that edits a task uses this loop. One outer skill owns the loop and
final commit; a nested policy must not start another review/commit cycle.

## Existing task baseline

Before substantive edits, run `sanity-check` and retain its evidence as the
baseline. Matching cached evidence is allowed under its cache rules. If sanity
fails:

- a repair workflow such as `quality-fix` may continue specifically to fix
  the failure;
- difficulty or context tuning must stop or route to repair first, because it
  cannot attribute outcomes from an invalid baseline.

A newly scaffolded task has no pre-edit baseline; run sanity after scaffolding.

`harden-task` may instead use the exact-current-content validity baseline
defined in `existing-task-validity.md`; `increase-context-tokens` may use
the same policy, as may `ease-task`. `quality-fix` may use that
reference's repair policy, which accepts complete current-commit failures as
repair inputs rather than
rerunning them. This is evidence reuse, not a weaker post-edit gate: missing or
mismatched prerequisites fall back to full sanity, and all changed tasks still
run full sanity.

## Edit and gate

1. Apply one coherent batch of changes for the outer operation.
2. Run `sanity-check`. Fix every blocking mechanical failure before
   review, and preserve its commands/results as review evidence.
3. Resolve and invoke the track's official review skill directly, following
   `runtime-discovery.md` and the detected track profile. Verify the current
   Team AAI review orchestrator and its delegate before invoking them; stop if
   routing is missing or ambiguous. Follow the official skill's checklist,
   blocking criteria, and output format. Supply fresh sanity evidence and any
   bounded source dossier, including the transformations actually used, for
   provenance, contamination, originality, and embedding-dedup assessment.
   Sanity establishes that the task executes and its literal contract is wired
   correctly; review judges
   semantic quality, fairness, coverage, and oracle correctness. Review may
   reuse fresh sanity execution evidence when the official checklist permits,
   but must perform any independent checks that checklist requires. Neither
   gate's conclusion substitutes for the other.
4. Apply actionable review fixes, then return to step 2. Never review changed
   files against a stale sanity result.
5. Stop after at most three review rounds. When the official review passes, use
   `commit-workflow.md`; otherwise leave changes uncommitted and report status.

For `harden-task`, a passing official review completes the quality gate for the
current hardening attempt but does not trigger a commit until the empirical
calibration in `hardening-calibration.md` also passes. A subsequent hardening
edit invalidates that review evidence and returns through sanity/review.

## Composing operations

When an outer skill needs another producing skill's domain policy, reuse only
its research and edit criteria. The outer skill retains ownership of sanity,
review rounds, and commit. Do not invoke a nested producing skill through its
final review/commit steps. If the requested work is solely the nested
operation, hand off entirely and stop the outer workflow instead.
