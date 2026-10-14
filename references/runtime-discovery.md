# Runtime discovery and drift policy

Platform schemas, validator stages, model fleets, taxonomies, rubrics, and
official Team AAI skills evolve. Discover them at the start of an operation;
do not preserve a platform snapshot in this plugin as if it were an API.

## Source precedence

Use the first available source, and record any fallback:

1. Exact task plus validation commit data returned by Codimango. This governs
   the rubric and evidence actually applied to that run.
2. Current official Team AAI review orchestrator, rule, or documentation
   installed in the runtime. Let the orchestrator detect track and format;
   names in profiles are hints.
3. The track profile in this plugin and the task repo's `AGENTS.md` adapter.
4. Conservative local inspection. Mark results UNVERIFIED when authoritative
   evidence is unavailable.

Never let a historical task result override current-commit evidence. Never
silently reinterpret a missing, hidden, pending, redacted, or unknown signal as
a pass. Preserve unrecognized fields, stages, rubric items, statuses, and model
roles in the evidence inventory until they are classified.

## Codimango discovery

Before remote task, job, or trial lookups, confirm task ownership through
`difficulty-source-discovery.md`. Track detection also follows this scope.

- Run `codimango --version` and relevant `<command> --help` before relying on
  optional flags. Do not substitute legacy namespaces or inferred commands.
- Discover JSON with `keys`, types, completeness flags, and counts before
  selecting fields. Treat documented collections rather than response roots as
  arrays. Follow pagination only with flags supported by the installed CLI;
  honor each operation's read/time bounds. Report incomplete coverage when a
  bound or unavailable continuation prevents completion.
- Resolve models with `codimango model list --json` and job/trial metadata.
  Human labels such as Avocado, oracle, or data-collection model are roles and
  targets, not permanent model ids.
- Resolve taxonomy from the task record and current `codimango taxonomy`
  axes. Do not hardcode a closed category list.
- A validator or review stage inventory is open-ended. Union task details,
  errors/stage results, job identities/config, comments/reviews, and artifacts.

### Manifest classification

For a Codimango `task.toml` (or the corresponding manifest used by another
track, such as WebCraft `site.toml`), treat the current manifest structural
validator as authoritative. The `[task]` classification requires
`track_assignment`, `workstream`, and `format`; every value must belong to the
current classification contract. Prefer:

```text
codimango bench validate -p <task-dir> --structural-only --json
```

after confirming the installed command's help. When direct schema inspection
is needed, the authoritative contract is
[`manifest-classification-contract.schema.json`](https://www.internalfb.com/code/fbsource/nest/apps/codimango/lib/coding-acceleration/task-toml-schemas/subschemas/manifest-classification-contract.schema.json?lines=8)
in fbsource. Do not copy the schema's complete enum sets into this plugin: they
evolve independently. Profile triples are current defaults/hints only. If
neither the validator nor schema is available, mark classification UNVERIFIED
and blocking rather than accepting an unchecked or historically valid value.

## Official skills and rules

Use the current Team AAI review orchestrator when available. At the time of this
audit it is `ado-task-review`, whose Stage 0a detects track/format and delegates
to track-specific review skills. Verify the orchestrator at runtime rather than
assuming its name or delegates are permanent. If a profile names a candidate
skill, verify that it exists and matches the detected track and format. If the
orchestrator is unavailable or ambiguous, stop and report the candidates
instead of running a similarly named cross-track review. `review-routing` is a
human-review queue workflow and must not be used for checklist selection.

Copied summaries such as model-role and instruction-style notes are aids. Read
their named canonical source when available; the canonical source wins. If it
cannot be read, disclose that the local summary may be stale before making a
permission-sensitive or provenance-sensitive decision.

## Cache envelope

For research-agent resolution and fallback, follow `researcher-dispatch.md`.
Pass the resolved plugin root to every researcher so its reference paths are
usable outside the parent context.

A cached research brief is reusable only when all relevant fingerprints match:

- operation, task identity, track, and format;
- task content revision or digest, not just wall-clock age;
- Codimango task id, validation SHA/generation, and CLI version for remote data;
- own-task discovery scope (`mine`), account identity when exposed, query,
  candidate ids/commits, and completeness for source research; invalidate any
  brief produced from a broader ownership scope;
- model ids/roles and trial set used for empirical conclusions;
- rubric version and official skill/rule identity when used;
- profile and relevant plugin-reference revisions.

For ideation, also fingerprint the user's seed, requested scope, and proposal
constraints. A changed prompt invalidates an otherwise matching brief. These
fields also apply to research prompted by a changed tuning objective.

Use the profile's scratch directory or an explicit repo-adapter path. Create
it only after checking that scratch is excluded from version control; report
a missing ignore rule rather than staging research artifacts. A profile that
labels a directory "gitignored" does not create the repo's ignore rule.

Age is only an upper bound. Default to seven days when the profile does not set
one, but invalidate immediately when a fingerprint changes. Put the envelope
at the top of the cached brief. A legacy brief without an envelope is stale.

## Partial support

A profile containing unresolved TODOs is unsupported for the missing
capability. Do not infer layout, verifier, review mapping, or targets from a
different track. Continue only with an explicit repo adapter or authoritative
runtime source that supplies the missing fields; otherwise stop with the exact
missing capability.
