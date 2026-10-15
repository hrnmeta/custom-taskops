# Custom TaskOps

Hugo Ng

Automated validation. Consistent iteration. A workflow you can customize.

---

# Why I built Custom TaskOps

Different task modifications need the same checks—and the same repair loop.

Common checks

Oracle / setup correctness
Spec clarity / test alignment
Resistance to reward hacking

Entry points

Create a task
Harden it
Extend context
Resolve review findings

One command runs shared checks, applies fixes, and rechecks.
Replace repeated verification and repair prompts with a consistent loop.

---

# One workflow, from request to validated commit

Shared validation/repair loop, omitting the sanity-only path. Sanity, official review, required measurement, and a scoped commit. Unresolved blockers stay uncommitted within a shared budget of at most three validation attempts. All failed gates check the cap before repairs; the third failure stops, while a successful third attempt may commit.

---

# Three operations, one validation loop

Different inputs and edits. The same validation and commit rules.

| Entry skill | Starting point | Operation-specific work | Additional validation |
| --- | --- | --- | --- |
| create-task | Idea, or automatic ideation | Scaffold spec, tests, environment, and oracle; invoke official README skill | Measurements required by task/track policy |
| harden-task | Existing valid task | Research failure trajectories; collect baseline trials; edit difficulty | Five comparable candidate trials must meet configured target |
| quality-fix | Staged task and review findings | Fetch findings pinned to the current commit; repair spec/test alignment, oracle, or verifier | Difficulty calibration if repairs include tuning |

All three: sanity → official track review → required measurements → scoped commit.

---

# Inside the plugin: customize the workflow

Shared rules travel with you. Profiles adapt the workflow to each track.

custom-taskops/
├─ .muse-plugin/plugin.json
├─ skills/<name>/SKILL.md
├─ references/*.md
├─ profiles/*.md
├─ agents/*.md
└─ hooks/task-gate.{sh,py}

Skills: define the workflow

Write steps and skill handoffs in SKILL.md.
create-task: research → scaffold → validate → commit.

References: share the rules

Reuse sanity, review, retry, and commit policies.
Change a shared preference once for every operation.

Profiles: adapt each track

Set verifier commands and official review routing per track.
Override difficulty / context targets where needed.

agents/: compact research briefs · Task repo AGENTS.md: local commands
hooks/: event scripts; the Stop hook provides quick advisory checks

Copy / fork → register → validate → install

Ask AI to edit a skill, shared rule, or track profile to match how you work.

---

# Custom TaskOps on GitHub

Try Custom TaskOps

Run a task operation.
Inspect the checks, fixes,
and resulting commit.

Customize it

Keep the useful defaults.
Change steps, policies,
or track-specific behavior.

Build your own

Use this structure
or start a blank plugin.
Ask AI to write the workflow.

github.com/hrnmeta/custom-taskops
