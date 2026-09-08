# Lab 9.4 — an unmapped HIGH cannot ship

**Module:** `9.4`
**Authorized scope:** this directory only. Local course fixture. No live GitHub Advanced Security or public repo scanning.
**Invariant:** `ship_ok([{"id": "F1", "sev": "HIGH"}], {})` is false. Honest mapped HIGH may ship.
**Root cause class:** scanner output not joined to the 9.1 map
**Non-goals:** scanner cookbooks as 1.2; claiming Gate 9.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/9.4/9.4-lab`, then run `git restore --source=HEAD -- labs/9.4/9.4-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`ship_ok` always returns true. Forbidden outcome: unmapped HIGH finding allows ship.

## Structural fix

Require every HIGH `id` to be a key in `mappings`.

## Verify

```
python3 -m pytest labs/9.4/9.4-lab/tests --impl vulnerable
python3 -m pytest labs/9.4/9.4-lab/tests --impl fixed
```

The first command must fail on unmapped HIGH. The second must pass. Honest mapped HIGH may pass on both.

## Operate

Signal: `unmapped_high_blocks`. Do not log payloads. Do not claim Gate 9.

## Transfer

Clinic 50 unmapped HIGHs. Prompt only.
