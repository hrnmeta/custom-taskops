# Track profile: long-horizon

Partially supported. Per `references/runtime-discovery.md`, fail closed for any
operation whose layout, verifier, routing, scratch, or metadata capability is
not supplied by an authoritative runtime source or repo adapter.

## Known

- Official skills: `lh-review-task` and `lh-audit` for review,
  `lh-count-tokens` for peak measurement.
- Review routing: official LH review skills and their blocking criteria.
- Author identity: use the task repo's configuration or explicit user input.

## Context target

Historical target: 128k peak tokens for the configured Avocado role. Resolve
the current target, model id, and official measurement procedure at runtime;
do not apply 128k when current policy differs or cannot be verified.

## Detection

TODO(user): marker files that identify this track.

## TODO(user)

- Required file layout.
- Verifier command and contract.
- Metadata and taxonomy fields.
- Scratch and research-brief locations.
