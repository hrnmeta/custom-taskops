# Empirical hardening calibration

`harden-task` uses this measured loop in addition to the canonical quality
loop. Sanity and review establish validity; target-model trials establish
difficulty. Neither substitutes for the other. Follow
`<plugin>/references/difficulty-calibration.md` for shared measurement and
target policy.

## Recent own-task failure library

Before editing, follow `<plugin>/references/difficulty-source-discovery.md`.
The main agent supplies fresh mine-scoped CLI candidates when available;
`failure-researcher` builds a bounded library from those owned tasks and the
current task. With no suitable owned sources, report the gap and use
current-task evidence and local hypotheses for the measured attempt loop.

1. Resolve the live validation-gate model, agent, attempt count, and result
   fields from `codimango model list --json` plus job metadata. Never assume an
   Avocado model id or a legacy `avocadoPassCount` field.
2. Hydrate the bounded owned candidates supplied by the main agent, or list
   up to 50 recent own tasks with `--filter mine`, ordered by `updated-at`
   descending under the shared discovery policy. Prefer the same format and
   comparable environment. Record completeness, deduplicate, and exclude the
   target task from inspiration sources.
3. Prefer tasks with a passing oracle/valid task state and at least the configured
   number of completed comparable gate trials. Label sparse evidence as
   hypothesis-only rather than measured difficulty. Rank by low gate pass rate,
   evidence volume, recency, and relevance. If fewer than three strong
   same-track sources exist, widen only to the user's own tasks in transferable
   formats/tracks and label the mismatch. Continue from current-task evidence
   if no sources qualify.
4. Select the strongest relevant sources. Inspect at most five source tasks
   total and at most two representative failing trials
   from each. Pull named artifacts only when necessary to understand the
   failure. Preserve the concrete material that carries the difficulty signal:
   source challenge mechanics, interfaces, invariants, state transitions,
   verifier/test architecture, exact failure sequence, trajectory evidence, and
   interaction between layers. Inspect visible source files and named artifacts
   when needed and permitted. Do not retrieve or reproduce hidden verifier
   contents, complete successful answers, or reference solutions.
5. Recommend combinations and modifications that fit the target task. The main
   agent must receive enough concrete source detail to reconstruct why each
   challenge worked; a category label or abstract failure summary is
   insufficient. Preserve the failure-inducing core while transforming the
   material into an original task rather than copying source prose, code, tests,
   fixtures, data, identifiers, or an entire distinctive construction.
   Combining multiple sources does not itself establish originality.
6. Maintain a concrete source dossier containing every source task/job/trial
   id, the relevant mechanics and evidence, what must survive transfer, what
   must not be copied, and the transformations made. Include the mine-scoped queries
   and result fingerprints in the cache envelope. Give this dossier to the main
   agent and official review workflow; keep it bounded through focused excerpts and
   citations rather than erasing the concrete signal or dumping complete raw
   tasks. Use it for provenance, contamination, originality, and embedding-
   dedup assessment.

The bounds keep research quick; completeness refers to the bounded query and
selected trials, not to the entire Codimango corpus.

## Baseline

Before editing any task file, record the target task's comparable five-trial
baseline according to `difficulty-calibration.md`. Otherwise stop before the
attempt loop; never measure already-edited content and call it the baseline.

## Maximum three hardening attempts

The three-attempt ceiling shares the outer operation's three-review-round
budget in `iterate-review.md`. If review fixes consume that budget, stop
uncommitted rather than starting another hardening attempt.

For attempt 1 through 3:

1. Apply one coherent batch using the strongest current-task and own-task
   failure patterns not already attempted, or clearly labeled local hypotheses
   when owned-source history is sparse.
2. Run `sanity-check`, then invoke the track's official review skill directly
   through `iterate-review.md`. Supply the concrete source dossier and require
   explicit assessment of provenance, contamination, originality, and embedding deduplication under
   the current official checklist. Apply blocking review fixes and return
   through sanity before spending trials. Defer the final commit while
   calibration is in progress.
3. Run five comparable validation-gate trials against the current working tree.
   Prefer the local runner so calibration does not require a checkpoint commit
   or push. Resolve flags from current help and the track profile; for current
   TBench tooling the shape is:

   ```text
   codimango bench run -p <task> -a <gate-agent> -m <gate-model> --k-to-n -k 5 --jobs-dir <scratch>/jobs --json
   ```

   Store jobs/results only in profile scratch paths excluded from commits.
4. Triage every failure. Count only legitimate task difficulty; ambiguity,
   broken setup, oracle/verifier defects, timeouts caused by infrastructure,
   and flaky execution route to repair and invalidate the measurement.
5. Apply the configured target resolved through `difficulty-calibration.md`.
   On success, finish the canonical commit workflow. Above target, analyze the
   new trajectories and begin the next attempt with a materially different or
   stronger combination. A lower pass count is useful evidence but is not
   success while it remains above target.

After three complete attempts without reaching target, stop uncommitted and
report the baseline, each attempt, failure classifications, strongest remaining
levers, and any external limitation. Never claim successful hardening from
static review or a difficulty-tag change.

Authorization boundaries come from `difficulty-calibration.md`.
