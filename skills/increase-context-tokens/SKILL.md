---
name: increase-context-tokens
description: Grow a task toward its peak-token target using the user's own Codimango task history and legitimate context levers, then measure and review the result.
---

# Increase Context Tokens

Raise the task's peak context toward the target defined by its track profile, without breaking validity. Research runs in a subagent; the main agent actions the brief.

## Inputs

One task directory (default: the current directory). Detect the track from it (precedence per `profiles/README.md`); an explicit track id overrides detection.

## Steps

1. Read `<plugin>/references/runtime-discovery.md`,
   `<plugin>/references/readme-authorship.md`,
   `<plugin>/references/difficulty-source-discovery.md`,
   `<plugin>/references/context-calibration.md`,
   `<plugin>/references/existing-task-validity.md`,
   `<plugin>/references/iterate-review.md`, and the detected track's profile.
   Resolve the current official measurement procedure and configured
   model/target. If either is absent, stop and say so. Establish the validity
   baseline using `existing-task-validity.md`; run full pre-edit
   `sanity-check` only when exact-current-content evidence is incomplete or
   mismatched. Then reuse or measure the current peak according to
   `context-calibration.md`; stop without editing if the target is already met.
2. Use `difficulty-source-discovery.md` to confirm staged-target ownership and
   collect bounded own-task candidates with `codimango task list --filter mine`.
   With no suitable sources, continue from current-task evidence and local
   hypotheses. Check the track profile's research-
   brief cache. Reuse a brief only when its
   cache envelope matches; seven days is merely the default maximum age.
   Otherwise dispatch `context-researcher` through
   `<plugin>/references/researcher-dispatch.md` with the
   task, current peak, target, model identity, measurement procedure, and
   candidate names, ids, commits, authors, review states, and mine-scoped query
   fingerprint. Require the
   concrete source material and provenance defined by the shared discovery
   reference. Cache the brief.
3. Apply the brief's ranked levers: more reasoning steps, longer necessary tool outputs, multi-file reasoning, required distractor content. Never pad with junk tokens that break validity or measurability. When adding spec content, follow `<plugin>/references/instruction-style.md`; if you doubt authority to touch instruction.md, check `<plugin>/references/model-role.md` first — 1P models may author it.
4. Run the canonical post-edit sanity and independent review loop from
   `iterate-review.md`, supplying the concrete source dossier to the reviewer.
   Then collect the comparable post-edit measurement required by
   `context-calibration.md`. Do not commit an unmeasured, incomparable, or
   non-improving change.

## Output

Peak before/after with comparable measurement sources, what was added and why,
source-dossier coverage, review verdict, empirical-gate outcome, and commit
status.
