# Track profiles

Skills and agents in this plugin are task-type agnostic. They adapt to
whatever they are pointed at: the track is detected from the task at
runtime, never hardcoded in the procedure.

Read `references/runtime-discovery.md` before using a profile. Codimango track
and format values are open-ended. A profile may declare aliases, but an unknown
value must not be normalized into the nearest familiar track.

## How detection works

Resolve top to bottom; first hit wins:

1. Explicit track input.
2. The task's declared track and format fields, matched against explicit
   aliases in available profiles. Do not strip unfamiliar suffixes by pattern.
3. The Codimango record (`task show`), when the task is staged and its exact
   identity has first been confirmed by `task list --filter mine`, following
   `references/difficulty-source-discovery.md`.
4. File markers from each profile's `Detection` section, tried in filename
   order. Note `steps/` marks multi-turn *format*, not the long-horizon
   track — format and track are orthogonal.
5. The repo default from the task repo's `AGENTS.md` adapter.
6. Ask the user instead of guessing.

Detection does not prove support. Before an operation, verify that the profile
or repo adapter supplies every capability it needs (layout, verifier, review
routing, scratch/cache, and any context target). A TODO is missing data and
must fail closed for that capability.

Profile filename (minus `.md`) is this plugin's profile id, not necessarily the
Codimango track id. Resolve remote `--track` values from current owned-task
metadata or authoritative runtime documentation. If that mapping is unknown,
omit `--track` on the bounded mine-scoped listing and match profile markers,
track, and format locally; do not send a guessed profile id to the CLI.

## Adding a track

Copy the smallest profile, fill in every section (detection markers are
mandatory), then verify with a sanity run on a task of that track — the
plugin validator does not check profiles. No skill or agent needs to change.
