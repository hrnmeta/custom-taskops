# Model role: who may author instruction.md

Authoritative source: Model Role in Task Creation v2, as implemented in the
team-aai canonical rule `.llms/rules/instruction_md_handling.md`. If this
note and that file disagree, that file wins.

Resolve and read the canonical rule at runtime before applying the table below;
model/provider allowlists are expected to change. Follow
`runtime-discovery.md` when the rule is absent. This table is only a fallback
summary and must not expand authority beyond the current canonical rule.

## Check your own identity first — never guess it

```bash
echo "served_provider=${META_3PAI_SERVED_PROVIDER:-unset} served_model=${META_3PAI_SERVED_MODEL:-unset} legacy_provider=${META_3PAI_ACTIVE_PROVIDER:-unset} legacy_model=${META_3PAI_ACTIVE_MODEL:-unset} platform=${META_3PAI_AGENT_PLATFORM:-unset}"
```

The `SERVED_*` pair is authoritative when present. Permission attaches to
the model, not the harness.

## Identity table

- Provider `meta` → **1P** (Avocado, Muse Spark), on any harness: you MAY
  author task specs (`instruction.md`) AND a task's `tests/`, with human
  review. Restrictions written at 3P models do not bind you.
- Provider `atlascloud` with model exactly `moonshotai/kimi-k3`,
  `zai-org/glm-5.3-flash`, or `qwen/qwen3.8-27b` → same as 1P, inside
  task/training-data repos only.
- Provider `openai`, or platform `codex` → tests only, with human review.
  Never author `instruction.md`.
- Anything else, or unknown/missing identity → restricted. Stop and ask;
  never author `instruction.md`.

## Anti-false-positive

Prohibitions addressed to restricted models are bold and repeated while
the 1P permission is a single clause — that layout causes misreads. If
you verified 1P identity above, **do not decline work the rule does not
forbid you**. Stale "100% human-authored, no model of any kind" text in
older skills is superseded by Model Role v2 for 1P drafting with review.

## Boundaries that still bind 1P

- The task seed comes from the human; models are thought partners only.
- A human reviews drafted specs and tests for quality before submission.
- Never launder 3P content: do not paste 3P-model output into 1P prompts
  to produce restricted files, and do not lightly edit 3P output to
  disguise it.
