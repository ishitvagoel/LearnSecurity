# Lab 3.2 — scanner is not the threat model

**Module:** `3.2`
**Authorized scope:** this directory only. Local course fixture. No public or third-party scanners.
**Invariant:** A green scanner does **not** yield an empty threat list. SecureCollab must still list `cross-tenant-read` (and the other mandatory ids) with owner and trigger.
**Root cause class:** trust (tool output substituted for thinking)
**Non-goals:** live targets, real PII, production scanner tenants, weaponized exploits.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/3.2/3.2-lab`, then run `git restore --source=HEAD -- labs/3.2/3.2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`assemble_threat_model(scanner_green=True)` returns an empty `threats` list. `threats_from_scan(True)` therefore omits `cross-tenant-read`. That is the forbidden outcome: a green scanner produces an empty SecureCollab threat model.

## Structural fix

Always seed mandatory rows (`cross-tenant-read`, `hostile-browser`, `stolen-worker`) with owner and review trigger. Union scanner findings; never let a green scan replace the set.

## Verify

```
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

From repo root:

```
python3 -m pytest labs/3.2/3.2-lab/tests --impl vulnerable
python3 -m pytest labs/3.2/3.2-lab/tests --impl fixed
```

The first command must fail. The second must pass.

## Operate

CI signal: `missing_mandatory_threat` with the threat id and owner; never a note body. Do not back-date the model file after adding a row.

## Transfer

Clinic SMS reminders: seed channel-specific threats even if the gateway vendor questionnaire is green. Prompt only; do not leave this directory.
