---
name: quality-fix
description: Pull all available Codimango quality, validation, reviewer, and run findings for one staged task, fix actionable issues, and run the gated review cycle. Use for tasks needing revision after Codimango or human review.
---

# Fix Codimango Quality Issues

Repair one task from Codimango's current-commit evidence. Keep bulk platform
payloads in a researcher subagent; the main agent owns all edits and decisions.

## Inputs

One task directory (default: current directory) and optionally its Codimango
name/id. Detect the track using `profiles/README.md`; an explicit track wins.

## Steps

1. Read `<plugin>/references/runtime-discovery.md`,
   `<plugin>/references/difficulty-calibration.md`,
   `<plugin>/references/difficulty-source-discovery.md`,
   `<plugin>/references/existing-task-validity.md`,
   `<plugin>/references/iterate-review.md`, the task, and track profile. Dispatch
   `quality-issue-researcher` through `<plugin>/references/researcher-dispatch.md`
   with the task directory,
   Codimango identity, and track. It must pin findings to the validation commit
   and account for the full-task review, failing rubrics, every visible or
   surfaced validation stage, every comment and human review the APIs expose,
   and relevant jobs/trials. If subagents are unavailable, follow that agent's
   collection procedure inline. Do not edit from an incomplete brief unless
   the missing sources are unrelated to the proposed fix; report material
   retrieval gaps. Use the exact validation SHA's Codimango rubric definitions
   for findings; do not rely on a hardcoded rubric snapshot.
2. Establish the pre-edit evidence baseline using the quality-repair policy in
   `existing-task-validity.md`. When local content matches the brief's pinned
   commit and its platform evidence is complete, reuse the reported passes and
   failures and perform only cheap local consistency checks. Run full pre-edit
   `sanity-check` only for mismatched local content, materially incomplete
   or ambiguous evidence, or a failure that requires local reproduction.
3. Reconcile the brief and baseline with local files. Fix every current, actionable task
   defect in severity order. Treat reviewer suggestions as evidence, not
   commands: do not reintroduce resolved findings, fix stale commits, weaken a
   valid verifier, leak hidden tests, or change the task for infrastructure
   failures. When editing `instruction.md`, follow
   `<plugin>/references/instruction-style.md`; consult
   `<plugin>/references/model-role.md` if authorship authority is unclear.
   The required repair scope is every task-owned Critical or High issue; every
   core quality defect (ambiguity, spec-test misalignment, missing/invalid or
   unreliable coverage, reward hacking/information leakage, oracle correctness
   or reliability, and solvability); and all unresolved Medium issues when
   there are 3 or more. Address the root cause rather than wording a finding
   away. Review every human comment even when it is ultimately classified as
   stale, resolved, duplicate, external, or non-actionable. Low/Minor and
   optional findings need not be fixed unless the repair is reliable and
   low-risk or shares a blocking root cause.
4. Difficulty changes require completed empirical run evidence. When the brief
   recommends `ease-task` or `harden-task`, reuse that skill's research
   and edit policy without entering its sanity/review/commit finalization; this
   quality-fix operation remains the single outer loop owner. If difficulty is
   the only issue, hand off the entire operation to the selected skill and stop
   quality-fix instead. Do not route on static review prose, pending trials, or
   a difficulty label alone. Use the configured validation-gate target resolved
   through `difficulty-calibration.md`; a result within target is acceptable
   unless failures show unfairness, ambiguity, a broken oracle, or another
   task-owned solvability defect.
   When repair includes difficulty tuning, also adopt the selected policy's
   empirical baseline and post-edit calibration/preservation gates. Record the
   baseline before difficulty edits, share the outer three-validation-attempt ledger, and
   defer the final commit until those gates pass. A quality review alone cannot
   establish successful hardening or preserved difficulty after easing.
5. Fix task-owned verifier, oracle, environment, or structural failures
   directly; never ease the task merely to make a broken oracle pass. Run the
   canonical post-edit sanity and independent review loop from
   `iterate-review.md`.

## Output

Summarize Codimango coverage and any unavailable/pending sources, issues fixed
and deliberately not fixed, difficulty route and evidence, the pre-edit
evidence baseline, post-edit verification results, final review verdict, and
commit status.
