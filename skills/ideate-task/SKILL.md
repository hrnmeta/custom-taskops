---
name: ideate-task
description: Draft task proposals from the authenticated user's own Codimango tasks, failure clusters, taxonomy gaps, and optional seed ideas.
---

# Ideate Task

Produce grounded task proposals. Research runs in a subagent; the caller keeps only the brief and the drafts.

## Inputs

The track to ideate for (taken from the repo you are in unless stated otherwise), plus an optional seed area or direction.

## Steps

1. Read `<plugin>/references/runtime-discovery.md`,
   `<plugin>/references/difficulty-strategy.md`, and
   `<plugin>/references/difficulty-source-discovery.md`. Use the shared
   discovery process to collect bounded own-task candidates with
   `codimango task list --filter mine`. Discovery uses the CLI's existing
   authentication. If the user's task history is sparse or empty, continue
   from the seed and local context, labeling unsupported ideas as hypotheses.
   Check the track
   profile's research-brief cache and reuse it only when its full cache envelope matches;
   seven days is merely the default maximum age.
2. On a cache miss, dispatch `failure-researcher` through
   `<plugin>/references/researcher-dispatch.md` with op `ideate`,
   scoped to that track and supplied with candidate names, ids, commits,
   authors, review states, and the mine-scoped query fingerprint. Prioritize
   high-quality owned tasks with substantial repeated gate failures. Require the
   concrete source material and provenance defined by the shared discovery
   reference, along with taxonomy gaps. Save the returned brief to the cache.
3. Draft 2-4 proposals grounded in the brief and the human's seed
   area. Sparse own-task history may support fewer proposals or a single
   coherent challenge layer; label unmeasured ideas as hypotheses and do not
   invent evidence to fill a proposal count. With sufficient evidence, combine multiple evidence-backed failure modes or challenge
   layers by default, including unrelated layers when they can interact in one
   feasible task. Each has: title, one-paragraph concept, difficulty hypothesis,
   discrimination hypothesis (which agents it separates and why), and the core
   failure-inducing behavior of every layer that must survive implementation.
4. When invoked by itself, return the proposals for human selection and do not
   scaffold. When used as the proposal phase of `create-task`, follow
   `<plugin>/references/ideation-to-creation.md`: rank and select or creatively
   combine the proposals while preserving their failure-inducing core
   challenges, then return the resulting concept to creation. Ideation itself
   never owns scaffolding, review, or a commit.

Difficulty is empirical and confirmed later by codimango CI trials against independent agents, never by subjective judgment alone.

## Output

The proposals with evidence refs and the bounded concrete source dossier from
the cached brief, plus the selection rationale when automatic selection was
explicitly authorized.
