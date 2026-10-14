# Empirical difficulty calibration

This is the shared authority for validation-gate difficulty measurements. An
explicit current task or track policy wins. Otherwise this plugin's
default target is 0–2 successes in five completed comparable trials.

Resolve the live validation-gate role, model, agent, environment, result fields,
and attempt count from current Codimango metadata. Human names such as Avocado
are roles, not permanent model ids. Reuse results only when task content,
revision, verifier, model/agent, environment, and sample policy match. Prefer
five completed trials; replace infrastructure failures or mark the measurement
incomplete rather than counting them as model failures.

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
statistical equivalence. If the preservation gate fails, revise only when an
evidence-backed easing lever remains, then return through full post-edit sanity
and review before measuring again. Otherwise stop uncommitted. An incomplete
comparison blocks the commit.

Invoking hardening or easing authorizes these bounded local calibration trials
for the target task. Remote reruns, checkpoint pushes, or `--push` remain
separate publication actions requiring explicit authorization.
