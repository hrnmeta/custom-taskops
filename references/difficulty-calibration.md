# Empirical difficulty calibration

This is the shared authority for validation-gate difficulty measurements. An
explicit current task or track policy wins. Otherwise this plugin's
default target is 0–2 successes in five completed comparable trials.

Resolve the live validation-gate role, model, agent, environment, result fields,
and attempt count from current Codimango metadata. Human names such as Avocado
are roles, not permanent model ids. Reuse results only when task content,
revision, verifier, model/agent, environment, and sample policy match. Prefer
five completed trials; mark infrastructure failures as an incomplete
measurement rather than counting them as model failures. A failed or incomplete
post-edit batch ends the current validation attempt under `iterate-review.md`;
any replacement batch consumes the next attempt. An incomplete baseline stops
before task edits. A five-trial batch is not five validation attempts.

## Hardening

Record the five-trial baseline before changing task files. A hardening candidate
passes only when its comparable result is within the configured target. A
static review, difficulty label, or lower but still out-of-range pass count is
not sufficient.

## Easing without weakening the validation gate

Record or reuse a comparable five-trial baseline before editing. If it already
exceeds the configured target ceiling, stop and route the difficulty problem to
hardening rather than making the task easier.

After easing, run five comparable validation-gate trials. The preservation gate
passes only when the post-edit result remains within the configured target and
does not exceed the baseline by more than one success. This one-sample tolerance
acknowledges noise at n=5; report both counts rather than claiming exact
statistical equivalence. If the preservation gate fails, end the attempt. Revise only when an
evidence-backed easing lever remains and the shared three-attempt ledger in
`iterate-review.md` has capacity, then return through full post-edit sanity
and review before measuring again. The third failed attempt stops uncommitted
before any further fixes or measurement. Otherwise stop uncommitted. An incomplete
comparison blocks the commit.

Invoking hardening or easing authorizes these bounded local calibration trials
for the target task. Remote reruns, checkpoint pushes, or `--push` remain
separate publication actions requiring explicit authorization.
