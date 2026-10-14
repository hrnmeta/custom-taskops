# Researcher dispatch

The native manifest registers skills and hooks. Do not assume that bundled
`agents/` definitions are registered by every runtime.

For a research operation:

1. Resolve the plugin root and the intended `agents/<name>.md` file. Include
   the absolute plugin root, explicit task/repo path, operation, track/format,
   evidence revision, objective, and fresh mine-scoped listing when available
   in the input. `<plugin>` in the definition refers to that resolved root.
2. Check the runtime's agent registry. Use `custom-taskops/<name>` only if it
   is registered with this definition. A manually installed definition may be
   registered as `<name>` instead; verify it before using that identity.
3. If no named definition is registered but general subagents are supported,
   read the bundled definition and supply its complete instructions and the
   bounded input to a general research subagent with read/search/shell tools.
   Research remains read-only and follows the own-task discovery policy.
4. If subagents are unavailable, follow the same bundled procedure inline.
   Keep research separate from edits and preserve all evidence/coverage gaps.
   A missing agent registration alone must not block an otherwise supported
   CLI research operation.

The parent owns scratch/cache writes and all task edits, gates, and commits.
The researcher returns its brief; it never creates another producing loop.
