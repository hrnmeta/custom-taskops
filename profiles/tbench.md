# Track profile: tbench (Harbor / terminal-bench)

## Detection

`task.toml` plus `tests/test.sh` (container setups also carry
`environment/Dockerfile`).

## Layout

```text
<task-name>/
├── task.toml              # metadata, timeouts, resources
├── instruction.md         # eval prompt (the agent under test sees only this plus the container)
├── environment/Dockerfile # container setup
├── tests/test.sh          # verifier entrypoint
├── tests/**               # verifier-owned suites/assets in the task's language(s)
└── solution/solve.sh      # (optional) reference solution for oracle validation
```

## Verifier

Resolve in order: `harbor run -d <task> -a oracle` when `harbor` is on PATH,
else the codimango-backed oracle for the staged task, else direct
container execution through `tests/test.sh`. Verify the current TBench/Harbor
contract at runtime. Historically `test.sh` exits 0 and writes
`/logs/verifier/reward.txt` (`1` pass / `0` fail), but do not assume pytest,
Python test filenames, or a fixed result format when current tooling says
otherwise.

The `sanity-check` phase targets five minutes or less for one pristine and
one oracle direction. The independent official review may execute its own
oracle/golden checks. Codimango's submission validation owns the remote
stability quorum; taskops does not push or emulate that gate.

## Metadata

Historical required fields include `author_name`, `author_email`, `difficulty`,
and taxonomy. The current TBench single-turn classification default is:

```toml
[task]
track_assignment = "t-bench-external-repos"
workstream = "swe_public_repo"
format = "terminal_bench_single_turn"
```

Resolve and validate it against the live Codimango manifest contract described
in `references/runtime-discovery.md`; this profile is a hint, not an enum
authority. Other TBench formats may require a different triple. Resolve author
identity from the task repo's configuration or explicit user input; if a
required author field is missing, ask the user for it.

## Spec rules

No solution hints, no test disclosure, imperative style, no fenced code
blocks. An expert must be able to pass from the spec alone.

## Review routing

Resolve the current official checklist through the Team AAI review
orchestrator. At the time of this audit, `ado-task-review` auto-detects the
track/format and delegates to its current TBench review workflow. Verify the
orchestrator and delegate at runtime; do not pin a `review-task-*-vN` name here.
Apply its checklist and blocking criteria directly. Never fall back to a
similarly named cross-track skill.

## Context target

None.

## Scratch

Review reports and research briefs go to `.review/` (gitignored);
research briefs specifically to `.review/research/<task>-<op>-<YYYYMMDD>.md`.
Never commit `__pycache__/`, `.venv/`, `jobs/`, or `results/`.
