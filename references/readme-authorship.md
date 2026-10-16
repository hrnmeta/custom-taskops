# Task README authorship

This policy applies to task READMEs in every producing workflow, including
creation, hardening, easing, context growth, and quality repair. Use the
task README location declared by the track/profile, not unrelated upstream
repository READMEs or task implementation artifacts.

## One authoring route

- Create or update a task README only by invoking the current official
  `update-readme` skill (currently `team-aai:update-readme`). Resolve and verify
  it through `runtime-discovery.md` for the current task and track.
- Never hand-write, append, patch, or polish README content, even for a small
  fix, a review finding, or a summary of the latest iteration. Scaffolding
  templates are not a substitute for the official authoring step.
- Give the official skill the current task files and the intended documentation
  update. Require documentation of the current task, without changelogs,
  revision/change history, release notes, dated edit summaries, commit lists,
  or a narrative of the agent's work. Put change summaries in the response or
  commit message, not in the task README.
- The outer workflow owns the commit. Invoke the official skill for README
  generation only; use its supported non-committing route. If that route or
  the skill is unavailable, stop and report the missing capability. Do not
  substitute a custom author or bypass the rule.

## Before validation

After each coherent task edit, determine whether the README needs creation or
refresh to reflect the current task. If so, invoke the official skill before
sanity/review. If not, retain it unchanged and record that decision.

For each created or changed README, retain the official skill identity,
invocation/result, and the resulting content fingerprint with the operation's
gate evidence. Keep this evidence outside the README and outside committed
task files, using approved scratch paths or the operation report. A manual edit
after generation invalidates that evidence and requires official regeneration.

## Blocking validation

The read-only sanity gate checks that:

1. Every created or changed task README has matching official-generation
   evidence. Missing evidence is UNVERIFIED and blocks the candidate.
2. The README contains no task-edit history/changelog sections or dated/
   commit-indexed edit summaries. Inspect headings outside fenced examples
   and the README diff; task requirements that discuss changelog functionality
   are not themselves a history of the agent's edits.

An unchanged existing README does not require new generation solely to
establish its historical authorship. The no-changelog rule still applies.
Official review checks documentation accuracy against the current task;
invocation evidence alone does not establish accuracy.

On failure, the outer workflow requests official regeneration and reruns
validation under the same three-attempt ledger. Neither sanity nor the
reviewer edits the README directly. Do not commit unresolved README failures.
