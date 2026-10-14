---
name: create-task
description: Scaffold a new benchmark task from the track profile, then run the sanity gate and iterate-review loop, committing once it passes.
---

# Create Task

Scaffold one new task and drive it to commit-ready. The main agent owns all edits; expensive research runs in subagents and reviews follow the official track skill.

## Inputs

Optionally, a task name or idea and the repo it lives in. Default to the current
repo. With no concrete idea, automatically ideate, select or combine the
strongest proposal, and create it. Detect the track from the task context
(precedence per `profiles/README.md`); an explicit track id overrides
detection.

## Steps

1. Before research or scaffolding, detect the track, read
   `<plugin>/references/runtime-discovery.md`, its profile and repo adapter,
   and `<plugin>/references/model-role.md`. Confirm the required capabilities
   and current authoring authority. Automatic selection uses the user's scope;
   if the current canonical rule requires a human seed and none was supplied,
   request it before drafting task content.
2. If no concrete idea was supplied, follow
   `<plugin>/references/ideation-to-creation.md`: run the proposal phase of
   `ideate-task`, record the selection or combination rationale, and
   continue here with the resulting concept. Do not enter a separate
   validation or commit cycle.
3. Read `<plugin>/references/runtime-discovery.md`,
   `<plugin>/references/difficulty-strategy.md`, the detected track's
   profile at `<plugin>/profiles/<track>.md`, and the task repo's `AGENTS.md`
   adapter. Confirm that layout, metadata, verifier, review routing, and scratch
   capabilities are complete; stop with the missing capabilities rather than
   scaffolding from another track. Resolve current taxonomy values and official
   skill names at runtime.
4. Scaffold per the profile: spec, tests, environment, verifier entrypoint, and
   reference solution. Prefer the current official scaffold command/template
   when it supports the detected track and format (currently `codimango task
   init`), so required manifest fields and classification defaults originate
   from the platform contract. Otherwise resolve the classification triple per
   `<plugin>/references/runtime-discovery.md` and emit all three values; never
   copy a closed classification enum list into this plugin. Preserve and test
   every selected challenge layer's core failure-inducing behavior; do not
   quietly narrow the task to the easiest layer during implementation. Before
   writing instruction.md, read
   `<plugin>/references/model-role.md` (confirm 1P authority; never refuse
   permitted work) and `<plugin>/references/instruction-style.md`, and follow
   both.
5. Generate or update the task README only via the current official task README
   skill (currently `team-aai:update-readme`), resolved and verified at runtime.
   If unavailable, report the missing capability rather than inventing a README.
6. Run the new-task path in `<plugin>/references/iterate-review.md`: sanity
   after scaffolding, then independent review; every review fix returns through
   sanity. Invoke the track's official review skill directly as defined in
   that loop. When creation followed ideation, supply its bounded source
   dossier and the transformations actually used.

## Output

Task location, gate results per round, and commit status.
