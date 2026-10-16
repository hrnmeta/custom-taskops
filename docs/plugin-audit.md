# Plugin audit — 2026-10-14

Reviewed the manifest, all seven skills, all three researcher definitions,
profiles, shared references, hook, README, and workflow diagram. Removed the
personal-testing status sentence from the README.

## Issues fixed

| Area | Finding and correction |
| --- | --- |
| Stop hook | Shell parsing split paths with spaces, missed files in new task directories, and mishandled renames. The helper now parses JSON and NUL-delimited Git status, handles nested working directories, and remains non-blocking. |
| Hook guidance | Docker was treated as mandatory, documentation changes skipped review, and truncation could hide the next step. Docker is optional; workflow gates remain authoritative; summaries preserve guidance. |
| Track discovery | Profile filenames were treated as remote track IDs, and remote detection could precede ownership checks. Profile IDs and Codimango track IDs are now distinguished; unknown mappings use bounded mine-scoped listings. |
| Researcher dispatch | Bundled agents were assumed to be registered. Explicit registry resolution, general-subagent dispatch, and inline fallback now share the same bundled definitions and own-task scope. |
| Review ownership | Official review skills could enter another producing workflow, and calibration attempts could reset review limits. Reviews are verification steps under one outer owner and a shared three-round budget. |
| Calibration | Context measurement authorization was unspecified; quality repair could adopt difficulty edits without their empirical gates. Bounded local measurement and inherited calibration gates are now explicit. |
| Sparse history | Multi-source proposal requirements conflicted with empty own-task history. Single-layer or fewer proposals are permitted with clearly labeled hypotheses. Source inspection and copying restrictions are distinguished. |
| Evidence and cache | Seed/scope changes were absent from cache identity, scratch ignore status was assumed, and quality-review continuation lacked its concrete CLI flag. These requirements and bounded continuation are now explicit. |
| Creation | Authoring/capability checks followed ideation, and temporary file placement was described as context isolation. Creation checks authority first; drafting must follow the current canonical context rules. |
| Diagram | Standalone sanity flowed into review and commit despite being read-only. It now reports and ends without committing. |

## Verification

- `muse plugins validate . --json`: valid, zero diagnostics.
- Ten hook regression cases passed against temporary Git repositories.
- `shellcheck hooks/task-gate.sh` and `git diff --check`: passed.
- Manifest/frontmatter names, local reference paths, and researcher definitions
  checked for consistency; removed identifiers and browser commands absent.
- Relevant installed Codimango command help checked, including own-task list
  filters, review pagination, exact-commit review, artifacts, structural
  validation, and local benchmark arguments.
- SVG and PNG regenerated from the corrected Graphviz source.

## Runtime limits

This audit did not run task creation, remote Codimango reads, model trials, or
official Team AAI review workflows. Current authoring/provenance rules, review
delegates, model roles, account authentication, and platform JSON schemas still
require runtime discovery. Named-agent registration depends on the host; the
dispatch fallback handles its absence.

TBench has the concrete profile. Android is a stub; SWE-bench and long-horizon
remain partial until the capabilities documented in their profiles are supplied
by current official sources or a task-repo adapter. Manifest validation alone
does not establish support for those tracks.

The source repository was left untouched. Audit changes are not committed by
this audit.

## Follow-up: validation budget — 2026-10-15

The original cap counted official reviews. Repeated sanity repairs could bypass
it, and calibration described a separate attempt counter. The canonical loop
now uses one numbered ledger of at most three post-edit validation attempts.
Any blocking sanity, review, or empirical failure ends an attempt; the third
failure stops uncommitted before more fixes or retries. A successful third
attempt can commit. Nested policies and handoffs preserve the ledger. Baselines
are excluded, and a five-trial measurement is one batch within an attempt.

Updated difficulty, hardening, context, repair, sanity, commit instructions,
and README/slide diagrams to share this rule. Manifest validation passed with
zero diagnostics; checked all producing entry references, all diagram failure
routes, and static traces for sanity/review/measurement/mixed failures and
success on attempts 1–3. Regenerated SVG/PNG and presentation exports.

The limit is an agent instruction, not an executable runtime guard. No live
Muse task workflow or model trials were run to establish agent compliance.
The advisory Stop hook remains separate from the attempt ledger.

## Follow-up: task README authoring — 2026-10-16

README authorship was restricted in creation but not explicitly shared by
repair and tuning. Added `references/readme-authorship.md` and load it from all
five producing skills plus sanity. Only the current official `update-readme`
skill may create/update task documentation; no changelogs or task-edit history.
Changed READMEs require matching generation evidence; review fixes regenerate
through that same skill. Missing evidence or history blocks sanity and commit,
with retries using the existing shared three-attempt ledger. Unchanged existing
READMEs do not need generation just to reconstruct historical authorship.

Manifest validation passed with zero diagnostics. Verified reference paths,
blocking/advisory check numbering, and source/slide flowchart edge agreement.
Regenerated diagram assets and visually checked slides 2, 3, and 6. Confirmed
installed `codimango bench run`/`bench stats` help supports pre-push local trials
and result inspection; no task trials or remote mutations were performed.
Publication and hosted monitoring behavior were not changed.

These are workflow instructions and evidence checks; no live agent run was
used to demonstrate compliance with the README policy.
