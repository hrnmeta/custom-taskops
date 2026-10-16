# Canonical task-change and review loop

Every skill that edits a task uses this loop. One outer skill owns the loop and
final commit; a nested policy must not start another review/commit cycle.
Read `readme-authorship.md` before any task edits: only the official
`update-readme` skill authors task READMEs, and agent changelogs are prohibited.

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

### One shared budget: at most three validation attempts

The outer operation keeps one attempt ledger, numbered 1–3, for the entire
requested change. An attempt is one changed candidate passing through sanity,
official review, and every applicable empirical gate. Allocate its number
before the first post-edit sanity check; scaffolding is candidate 1. Record
the candidate, sanity verdict, review verdict, measurement verdict (or not
applicable), and remaining budget. A gate not reached is recorded as not run.

A blocking sanity result, blocking review result, failed empirical target,
or invalid/incomplete measurement ends that attempt immediately. Do not run
later gates on a failed candidate. Before applying fixes or trying another
lever, check the ledger: if attempt 3 failed, stop uncommitted and report all
attempts and remaining blockers. Otherwise apply one coherent repair batch
and start the next numbered attempt with fresh sanity. Even a retry without
task edits consumes the next attempt; never retry a failed gate indefinitely.

There is at most one official review invocation per attempt. Passing sanity,
review, and measurement on unchanged content belong to the same attempt.
Attempt 3 may finish and commit if all its required gates pass; reaching the
number 3 alone does not mean failure. Pre-edit baseline checks and research do
not consume this post-edit budget. A configured five-trial measurement is one
batch within an attempt, not five attempts; do not start replacement batches
after a failed/incomplete result without allocating the next attempt.

Repairs, hardening, easing, context growth, nested policies, and handoffs of
the same requested change all share this ledger. Do not reset it to obtain
more attempts. Only a new explicit user request starts a new budget. Missing
authority or required tooling can stop the operation sooner.

Before editing task specs or tests, resolve current authoring authority through
`model-role.md` and its canonical source. Follow current provenance and spec
drafting requirements in `instruction-style.md`; a sanity pass cannot grant
authoring permission. Verification and research remain read-only.

1. Apply one coherent batch of changes for the outer operation.
   Refresh the task README only through the official skill when needed, and
   retain its generation evidence under `readme-authorship.md`. Never append
   an iteration summary or fix README findings by hand.
2. Allocate the next attempt under the shared budget and run `sanity-check`.
   Preserve its commands/results as review evidence. On a blocking failure,
   end this attempt and use the budget rule before fixing or retrying.
3. Resolve and invoke the track's official review skill directly, following
   `runtime-discovery.md` and the detected track profile. Verify the current
   Team AAI review orchestrator and its delegate before invoking them; stop if
   routing is missing or ambiguous. Follow the official skill's checklist,
   blocking criteria, and output format. Supply fresh sanity evidence and any
   README generation evidence required by `readme-authorship.md`, plus the
   bounded source dossier, including the transformations actually used, for
   provenance, contamination, originality, and embedding-dedup assessment.
   Request a read-only review: the outer operation owns fixes, measurements,
   and the final commit. If the official skill normally edits or commits,
   use its supported review-only mode or apply its current checklist as a
   verification step; do not enter another producing workflow. If no such
   route is available, report the missing capability.
   Sanity establishes that the task executes and its literal contract is wired
   correctly; review judges
   semantic quality, fairness, coverage, and oracle correctness. Review may
   reuse fresh sanity execution evidence when the official checklist permits,
   but must perform any independent checks that checklist requires. Neither
   gate's conclusion substitutes for the other.
4. On blocking review findings, end this attempt. Check the shared budget
   before applying actionable fixes and returning to step 2. Never review
   changed files against a stale sanity result.
5. After review passes, run the operation's applicable empirical gates for
   this candidate. A failed or incomplete gate ends the attempt and uses the
   same budget rule before any repair or retry. Once all required gates pass,
   use `commit-workflow.md`; otherwise leave changes uncommitted and report
   status. Never start attempt 4 automatically.

For difficulty or context tuning, a passing official review completes the
quality gate for the current attempt but does not trigger a commit until the
operation's empirical gate also passes. Subsequent edits invalidate both
review and measurement evidence and return through sanity/review within the
same three-attempt budget. Observed trial failures caused by setup, oracle, verifier,
or infrastructure defects invalidate the measurement and route to repair;
they cannot justify a commit even after a previously passing review.

## Composing operations

When an outer skill needs another producing skill's domain policy, reuse only
its research and edit criteria. The outer skill retains ownership of sanity,
the attempt ledger, and commit. Do not invoke a nested producing skill through its
final review/commit steps. If the requested work is solely the nested
operation, hand off entirely and stop the outer workflow instead.
