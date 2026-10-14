# Track profile: swebench

Partially supported. Per `references/runtime-discovery.md`, fail closed for any
operation whose verifier, routing, scratch, or metadata capability is not
supplied by an authoritative runtime source or repo adapter.

## Known

- Tests carry `config.json` with `patch`, `test_patch`, `FAIL_TO_PASS`,
  `PASS_TO_PASS`, and `selected_test_files_to_run`.
- Author identity: use the task repo's configuration or explicit user input.

## Detection

`tests/config.json` containing `FAIL_TO_PASS` / `PASS_TO_PASS` keys.

## Context target

None.

## TODO(user)

- Required file layout.
- Verifier command and contract.
- Metadata and taxonomy fields.
- Official review skill mapping.
- Scratch and research-brief locations.
