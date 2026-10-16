# Custom TaskOps

Hugo Ng

Automated validation. Consistent iteration. A workflow you can customize.

---

# Why I built Custom TaskOps

Repeated prompts, reruns, and tracking each agent’s state
leave less attention for difficult issues.

Common checks & rules

Oracle / setup correctness
Spec clarity / test alignment
Suitable difficulty
Prevent reward hacking
README: official update-readme, no changelogs

Entry points

Create a task
Harden it
Extend context
Resolve review findings

A shared workflow runs checks, fixes, and revalidation without repeated prompts.
Less supervision per task leaves more attention for hard issues and parallel work.

---

# One workflow, from request to validated commit

Quality review checks task validity and quality; local model trials measure difficulty before commit. Creation measures when task/track policy requires it. No automatic platform push/monitor cycle.

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

# From your workflow to your own plugin

github.com/hrnmeta/custom-taskops

1. Repeated work

Which steps or repairs keep needing another prompt?
Where do existing skills leave manual follow-up?

2. Your mental model

Custom steps, reused skills (official review, difficulty tuning), or both?
Plan user input, handoffs, required checks, and failure handling.
If tuning finishes but validation fails, what happens next?

3. Adapt, build, iterate

Adapt Custom TaskOps or build your own plugin; tailor it to how you work.
When behavior misses your intent, ask AI to revise the steps or policies.
Validate and reinstall; keep refining your defaults and track overrides.

Install / update

```bash
muse plugins install /path/to/custom-taskops --scope user
muse plugins approve custom-taskops
```
