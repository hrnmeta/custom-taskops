# instruction.md style rules (stylometric)

Distilled from the official team-aai `verify-task-provenance` rubric
(Checks 1, 4, 5). The detector counts clusters: 0–1 strong signals is
CLEAN, 2–4 is SUSPECT, 5+ is CONTAMINATED. Single generic-LLM patterns
(bullets, clean grammar, systematic coverage) are expected from approved
models and never sink a file alone. Counter-signals never offset strong
signals, so write clean rather than performing roughness.

This is a convenience summary, not a frozen copy of policy. Before a
provenance-sensitive edit, resolve the current official skill/rubric per
`runtime-discovery.md`; its thresholds, checks, and exceptions win. If the
official source is unavailable, disclose that this summary may be stale.

## Never: strong 3P tells (S1–S7)

- S1 hedges: "Note that", "Make sure to", "Be sure to", "Keep in mind",
  "It's important to note", "You should consider". Write the requirement
  bare: "Output must be valid JSON."
- S2 meta-commentary: sentences about the spec ("This section describes",
  "The following outlines", "The examples below define the order").
  State requirements; plain cross-references ("Section 10 defines it")
  are fine.
- S3 connector tissue: sentence-initial "Additionally", "Furthermore",
  "Moreover", "Consequently". In-sentence adverbs are fine.
- S4 softened imperatives: "You may want to", "Consider implementing",
  "A good approach would be". Command directly: "Use a hash map."
- S5 recaps: summary sections or clauses restating earlier requirements.
  Say each requirement once.
- S6 rationale asides: parenthetical justification ("this ensures …",
  "to prevent …"). Specification parentheticals are fine; justification
  is not.
- S7 cautious tone: "Please note", "It's worth noting", "It should be
  mentioned".

## Structure and polish (M1–M8)

- Vary depth and format across sections; do not make every section a
  uniform bullet list of the same depth (M1, M3).
- Write plain and direct; terse fragments and opinionated constraints
  are fine (A2, A6). Avoid em-dash-plus-"never" chains, colon-chained
  clauses, and soft transitions (M2, M8).
- Enumerate only what the contract inherently requires (M4). Keep
  variable descriptions tight ("Input file path"), cover only relevant
  scenarios, and never follow an example with "The above demonstrates"
  (M5–M7).
- Use domain terms without over-explaining them (A1).

## Cross-file and history (X1–X3, G1–G3)

- Draft the spec without tests/solution files in context (or draft in
  /tmp): shared distinctive clauses with test docstrings or solution
  comments read as single-session generation (X1, X2).
- Do not mirror the solution's structure section-for-section (X3).
- Commit targeted changes; avoid wholesale rewrites of the spec in one
  commit after its first version (G1–G3).

## Do not fake

Never insert typos, grammar errors, or inconsistent formatting to imitate
human roughness (A4, A5). They do not offset strong signals and they
degrade the task. Avoid the tells above instead.

## Self-check

Before finishing, re-read the spec once for clusters of the S-list, shared
clauses with tests/solution, and mirrored structure. Fix what you find.
