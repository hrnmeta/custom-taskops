# Own-task source discovery

Use this shared process for every researcher: failure research (ideation,
easing, and hardening), context growth, and quality repair. All remote task
lookups and source discovery are limited to tasks owned by the currently
authenticated Codimango user. Read local task files normally; an unstaged local
task has no remote history yet.

## CLI discovery

1. Inspect `codimango task list --help` and use the supported read-only CLI:

   ```sh
   codimango task list --filter mine --track <track> --limit 50 --sort updated-at --dir desc --json
   ```

   Use the track's current Codimango id, resolved through `runtime-discovery.md`.
   Omit `--track` when no track is known. The explicit `--filter mine` is
   required on every listing. Do not add `--pod` or `--tag`: those flags can
   replace the ownership scope rather than narrow it. Do not use review queues,
   recommended-to-review feeds, or `--filter all`.
2. Keep JSON reads bounded and project only candidate metadata: names, ids,
   current commits, authors/owners, track/format, status, and available
   oracle/validation signals. Inspect response keys instead of assuming a
   collection schema. Preserve stderr and nonzero status through projections.
   Exclude the target task from inspiration candidates and deduplicate by id.
   For failure research, easing, context growth, or repair of a staged target,
   first confirm its exact identity in a mine-scoped listing. A bounded
   `--search <task-name>` query may locate it; require an exact name/id match,
   and report ambiguity or unconfirmed ownership before remote hydration.
3. Prefer comparable track, format, and environment. If fewer than three useful
   sources remain, one additional bounded mine-scoped listing without `--track`
   may supply transferable sources; label track/format differences. The user
   population remains the authenticated user's own tasks throughout.
4. Record the scope (`mine`), authenticated account identity when exposed by
   the CLI, command/query, result count, completeness/truncation signal, and
   candidate ids/commits. Fetch a fresh listing for each operation before
   reusing a source-research brief. Include the ownership scope and candidate
   fingerprint in its cache envelope; previous briefs from broader discovery
   are stale. Pass this bounded metadata to the researcher. A researcher may
   reuse the caller's fresh mine-scoped listing rather than fetch it twice.
5. Use the CLI's existing authentication. On an authentication failure, report
   the error and the supported `codimango auth setup` command for the user to
   run. On a transport or schema failure, report the retrieval gap. Research
   never opens a browser, attaches to a browser session, or calls dashboard
   endpoints. Do not collect or persist credentials in the plugin or brief.

## Limited evidence

Own-task discovery is the normal scope and needs no reduced-coverage approval.
Report the actual number of owned tasks and trials inspected. An empty listing
or sparse history is not a reason to expand to other users' tasks or block
ideation. Continue from the local task, available own-task evidence, and the
user's seed; clearly label unsupported ideas as hypotheses. Hardening and
context growth may use current-task evidence and local reasoning when no
suitable owned source exists. Quality repair reports unavailable remote
findings and follows its existing completeness policy. Empirical operation
gates still require real comparable measurements.

## Evidence hydration and ranking

The researcher hydrates only candidates from the authenticated user's own-task
listing through supported read-only Codimango CLI commands such as task show,
job list, trial list, analysis, and
named trial artifacts. Hydrate at most 15 promising candidates and stop source
research after roughly 15 minutes; return the best supported result with an
explicit coverage note if either bound is reached.

For ideation and hardening, compare completed trials from the task's current
commit and live validation-gate role. Prefer five comparable trials and require
at least three for a measured difficulty ranking; sources with fewer trials may inform clearly labeled
hypotheses only. Never combine stale commits or different models/roles into
one pass rate. Rank candidates by:

1. passing oracle and quality/validation state;
2. low validation-gate pass rate with enough comparable completed trials;
3. repeated, consistent, concrete failure signals;
4. current commit and recency;
5. track, format, and environment relevance;
6. enough accessible detail to explain the actual challenge construction.

For context growth, resolve the current official peak-token measurement and
model rather than assuming a field or counter. Rank candidates by:

1. passing oracle and quality/validation state;
2. high measured peak-token use under comparable measurement;
3. long successful or near-successful validation-gate trajectories;
4. failures after substantial progress rather than setup or infrastructure
   failures;
5. genuine multi-file navigation, tool-output interpretation, state tracking,
   and long reasoning dependencies;
6. track/environment relevance and enough accessible trajectory detail to
   explain what legitimately consumed context.

Inspect at most five sources and at most two representative trajectories per
source. Select by evidence quality, operation-specific signal strength, and
relevance.

## Concrete transfer and provenance

Do not reduce sources to abstract labels. The brief must retain the mechanics,
interfaces, invariants, state transitions, verifier/test architecture, exact
failure or progress sequence, and focused trajectory evidence that created the
signal. Recommend transformed combinations that preserve those difficult or
context-intensive interactions.

Do not retrieve or reproduce hidden verifier contents, complete successful
answers, reference solutions, source prose, code, fixtures, data, identifiers,
or an entire distinctive construction. Maintain source task/job/trial ids and
the transformations proposed so provenance, contamination, originality, and
embedding-dedup risk can be reviewed.
