---
name: sanity-check
description: Fast deterministic gate for one task — structure, metadata, verifier contract, test substance, two-direction evidence, and README policy. No edits, no judgment calls.
---

# Sanity Check

Run the fast gate on one task directory. Make no edits. Every check below is
mechanical; semantic judgments about sufficiency, fairness, valid alternatives,
reward hacking, or solution correctness belong in the track's official review.

## Inputs

One task directory (default: the current directory).

Read `<plugin>/references/runtime-discovery.md` and
`<plugin>/references/readme-authorship.md`, detect the track through
`<plugin>/profiles/README.md`, and read its profile and repo adapter. Fail closed
when a required layout, metadata, or verifier capability is unavailable.
Before reusing remote evidence, confirm ownership under the own-task discovery
policy. Invoking this gate authorizes its bounded local structural and oracle
checks for the target, but no remote reruns or publication.

Target five minutes or less for this deterministic gate on TBench. Use the
fastest authoritative verifier route, reuse safe build caches, and run each
direction once; do not add repeated full-oracle runs. Never truncate a run and
call it passing. If the track intrinsically cannot fit, report actual time and
the profile/tooling reason rather than weakening the gate.

## Steps

1. Structure: all files required by the track profile are present.
2. Metadata: every field currently required by the track profile, repo adapter,
   or authoritative task schema is present and well-formed. For a Codimango
   manifest, require `[task].track_assignment`, `[task].workstream`, and
   `[task].format`, and verify all three against the current manifest
   classification contract according to the Manifest classification section of
   `<plugin>/references/runtime-discovery.md`. Prefer the authoritative
   `codimango bench validate -p <task-dir> --structural-only --json`; any
   structural failure is FAIL and must name the failing field or reported
   contract error. Do not accept presence alone, maintain a copied closed enum
   list, or assume the TBench author/difficulty/taxonomy set is universal.
3. Verifier contract: enforce the current contract declared by the track
   profile/tooling. Confirm that the entrypoint executes the real suites rather
   than always passing and emits every required reward/result artifact on all
   paths. Do not impose TBench exit/reward conventions on other tracks.
4. Test mechanics: discover suites and result checks in the task's actual
   language/framework. Confirm that tests contain executable assertions or
   equivalent result checks and that the verifier actually runs them.
   Existence-only or assertion-free/equivalent tests are FAIL; do not judge
   whether the behaviors are sufficient coverage here, and do not require
   Python test functions or a particular assertion syntax.
5. Oracle evidence (both directions): fresh or cached proof that tests
   FAIL without the solution and the oracle PASSES with it. Cached evidence
   counts only when its `runtime-discovery.md` envelope matches; seven days is
   the default maximum age, not sufficient freshness by itself. Otherwise
   re-run. Missing, stale, or failing evidence is FAIL — the oracle must pass
   all tests as specified.
   Fix order: structure/environment blocking the run first,
   then oracle/solution faults; never ease the task to make the oracle
   pass. With no local runtime, record UNVERIFIED (still blocking) plus
   the exact command to run where one exists.
6. Mechanical spec-test contract: every literal interface needed to execute
   the tests—file path, CLI flag, entrypoint, and output format—is named in the
   spec or authoritative environment contract (grep cross-check). List missing
   literals; each omission is FAIL. Whether requirements are semantically
   sufficient, unambiguous, fairly tested, or accepting of valid alternatives
   belongs to the track's official review.
7. README policy: inspect the task README and its diff under
   `readme-authorship.md`. A created or changed README requires matching
   official `update-readme` invocation/result and content fingerprint; absent
   evidence is UNVERIFIED. Task-edit changelogs/history or dated/commit-indexed
   iteration summaries are FAIL. An unchanged existing README needs no new
   generation solely to prove its historical authorship. Report file evidence
   and skill identity. Make no edits; only the official skill regenerates it.
8. Style sweep (advisory, never blocks): grep instruction.md for the
   banned phrases in `<plugin>/references/instruction-style.md` (S1–S7).
   Report hits with file:line for author judgment; a lone hit is not a
   finding, a cluster is.

## Output

PASS/FAIL per check with brief file evidence, commands/results for both oracle
directions, and total elapsed time. Preserve this evidence for the subsequent
review. Any FAIL or UNVERIFIED on checks 1–7 blocks later gates for this
candidate. The outer workflow uses `iterate-review.md` to count this failed
validation attempt and checks its shared three-attempt budget before any fix
or retry. This skill runs one gate invocation and never retries itself;
check 8 is advisory only.
