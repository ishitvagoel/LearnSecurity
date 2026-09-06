# SecureCollab Phase 1 — upload paths

Design stub for Module 6.4. Not a production object store.

## Freeze

- Local `resolve(name)` under `/tmp/sc-lab`.
- Tests assert prefix. They do not read host files.

## Data, not a filesystem object

Join, canonicalize, require the lab prefix. UUID stored names are extra, not the check. Zip/XML/pickle are named residuals.

## Tests

`../outside` leaves the root on the vulnerable join. That escape is the evidence.
