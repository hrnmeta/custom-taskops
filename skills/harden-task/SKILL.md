---
name: harden-task
description: Empirically harden one task using current failures and the user's own Codimango task history, then run up to three five-trial calibration attempts to reach the configured target.
---

# Harden Task

Make one task harder while keeping it fair and solvable. Research runs in a subagent; the main agent actions the brief.

## Inputs

One task directory (default: the current directory). Detect the track from it (precedence per `profiles/README.md`); an explicit track id overrides detection.

## Steps

1. Read `<plugin>/references/runtime-discovery.md`,
   `<plugin>/references/difficulty-strategy.md`,
   `<plugin>/references/difficulty-calibration.md`,
   `<plugin>/references/difficulty-source-discovery.md`,
   `<plugin>/references/existing-task-validity.md`,
   `<plugin>/references/hardening-calibration.md`,
   `<plugin>/references/iterate-review.md`, the task files, and the detected
   track's profile. Establish the existing-task validity baseline using the
   exact-current-content evidence reuse policy in `existing-task-validity.md`.
   Run full pre-edit `sanity-check` only when that evidence is incomplete or
   mismatched; stop and route invalid baseline findings to repair rather than
   hardening an invalid task.
2. Use `difficulty-source-discovery.md` to confirm staged-target ownership and
   collect bounded own-task candidates with `codimango task list --filter mine`.
   If no suitable sources exist, continue from the current task's evidence and
   local reasoning, reporting the source gap. Check the track profile's research-brief cache.
   Reuse a brief only when its
   cache envelope matches; seven days is merely the default maximum age.
   Otherwise dispatch `failure-researcher` through
   `<plugin>/references/researcher-dispatch.md` with op
   `harden`: failure modes of the current configured validation-gate target
   plus the bounded candidates and recent own-task failure library
   defined in the two discovery/calibration references (resolve the live
   role/model rather than assuming one). Pass candidate names, ids, commits,
   authors, review states, and mine-scoped query fingerprint to the subagent. Cache the brief.
3. Triage every reported failure and prepare the first coherent hardening plan,
   but do not edit task files yet. Record or run the empirical baseline from
   `difficulty-calibration.md` and `hardening-calibration.md`; stop if it is
   incomplete or already meets the configured target. Then define attempt
   batches from valid gaps
   (when editing the spec, follow `<plugin>/references/instruction-style.md`; if
   you doubt authority to touch instruction.md, check
   `<plugin>/references/model-role.md` first — 1P models may author it):
   - Valid reasoning gap: plan to exploit it (edge-case tests, tightened assertions,
     removed solution hints, new challenge layers targeting the gap). Combine
     multiple strong gaps by default, including unrelated gaps when they can
     interact feasibly, and preserve the failure-inducing core of each.
   - Not a valid gap (flaky infra, rubric noise, unsolvable as specified): record it and do not force it into the task.
   - When suitable owned sources exist, plan to adapt, substantially modify,
     and combine their strongest patterns into original challenge layers suited
     to this task. With no suitable sources, use current-task evidence and local
     hypotheses, and validate them through the measured attempt loop.
     Follow the concrete-source-dossier and non-copying
     requirements in `hardening-calibration.md`.
4. Run the maximum-three-attempt measured loop in
   `<plugin>/references/hardening-calibration.md`. Use the outer ledger: failed sanity or review also
   consumes an attempt, and the third failure stops before further fixes. Each
   candidate must pass sanity and independent review before its five local
   target-model trials. Defer the
   commit until both quality gates and the configured empirical target pass.
   Bump the difficulty tag only when warranted by the measured result.

## Output

Source-task/trial coverage and concrete source dossier, baseline and per-attempt
pass counts, failure classification, changes with the gap each targets,
sanity/review results, final calibration outcome, and commit status.
