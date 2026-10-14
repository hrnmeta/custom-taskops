# Ideation-to-creation composition

Use this composition whenever `create-task` is invoked without a concrete
idea, or when the user asks to ideate and create in one operation. Invoking
`create-task` authorizes automatic proposal selection or combination. This
is one outer creation workflow, not two producing workflows.

Read `<plugin>/references/difficulty-strategy.md` and apply its deliberate
difficulty bias throughout proposal generation, combination, and selection.

1. Run the proposal phase from `ideate-task`, including its failure
   research, evidence references, and bounded concrete source dossier. Retain
   the dossier for the creation review; do not scaffold, review, or commit
   during that phase.
2. Rank the proposals by evidence strength, novelty relative to nearby tasks,
   implementation feasibility, expected model discrimination, and value for an
   under-targeted taxonomy area. Record a short selection rationale.
3. Creatively combine multiple strong proposals by default. Challenge layers
   need not be closely related: an unusual combination can produce a valuable
   larger-scope task. Use a single proposal only when additional strong layers
   create a concrete feasibility, validity, verification, or scope-coherence
   blocker. Integrate the layers meaningfully rather than making disconnected
   chores. Preserve
   each selected proposal's core challenge—especially the reasoning gap or
   behavior associated with target-model failures—and confirm that integration
   does not simplify, bypass, or dilute it.
4. Treat the selected concept as the idea input to `create-task`. Creation
   owns scaffolding, the sanity/review loop, and the single final commit. Give
   the retained dossier and recorded transformations to the independent
   reviewer.

`ideate-task` invoked by itself still returns proposals for human selection
and stops. Difficulty remains an empirical hypothesis until trials.
