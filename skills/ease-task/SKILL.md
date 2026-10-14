---
name: ease-task
description: Make one task easier using codimango failure research biased toward helping non-avocado agents while keeping avocado difficulty unchanged.
---

# Ease Task

Make one task easier while keeping it a valid evaluation. Research runs in a subagent; the main agent actions the brief.

## Inputs

One task directory (default: the current directory). Detect the track from it (precedence per `profiles/README.md`); an explicit track id overrides detection.

## Steps

1. Read `<plugin>/references/runtime-discovery.md`,
   `<plugin>/references/difficulty-calibration.md`,
   `<plugin>/references/difficulty-source-discovery.md`,
   `<plugin>/references/existing-task-validity.md`,
   `<plugin>/references/iterate-review.md`, the task files, and the detected
   track's profile. Establish validity through `existing-task-validity.md`;
   run full pre-edit `sanity-check` only when exact-current-content evidence
   is incomplete or mismatched. Record or run the comparable five-trial
   validation-gate baseline before editing. Stop or route invalid tasks to
   repair, and route an above-target baseline to hardening rather than easing.
2. Confirm staged-target ownership through the mine-scoped CLI discovery
   process. Check the track profile's research-brief cache. Reuse a brief only when its
   cache envelope matches; seven days is merely the default maximum age.
   Otherwise dispatch `failure-researcher` through
   `<plugin>/references/researcher-dispatch.md` with op
   `ease`: failures from current non-target model roles, and tips biased to help
   them while keeping the configured validation-gate target unchanged. Cache
   the brief.
3. Ease with one or more of: clarify the spec (paths, formats, required behaviors); add a worked example (never a solution hint or test disclosure); relax over-strict assertions that reject correct solutions; drop or split multi-behavior tests; adjust the difficulty tag if warranted. When editing the spec, follow `<plugin>/references/instruction-style.md`; if you doubt authority to touch instruction.md, check `<plugin>/references/model-role.md` first — 1P models may author it.
4. Never ease merely to make a failing oracle pass; route structure,
   environment, or oracle faults to repair. Run the canonical post-edit sanity
   and independent review loop from `iterate-review.md`, then run the post-edit
   preservation trials in `difficulty-calibration.md`. Do not commit unless
   both the review loop and empirical preservation gate pass.

## Output

Summary of changes, baseline and post-edit validation-gate counts, verification
results, review verdict, preservation-gate outcome, and commit status.
