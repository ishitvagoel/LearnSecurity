# SecureCollab Phase 1 — interpreter argv

Design stub for Module 6.1. Not a production export worker.

## Freeze

- Local `argv_for_list(name)` / `uses_shell`.
- Synthetic name `notes`. Tests do not execute the argv.

## Data, not grammar

The name is one argv slot after `--`. `sh -c` concatenation is forbidden. SQL parameters (5.5) are the same shape.

## Tests

Argv starts with `ls`, not `sh`. A denylist of `;` is not the evidence.
