# Lab 10.1 — culture is the merge gate, not a poster

**Module:** `10.1`
**Authorized scope:** this directory only. Local course fixture. No live GitHub orgs.
**Invariant:** `merge_ok({})` is false. Honest `{threat_model: "TM-12"}` may merge.
**Root cause class:** security as a later phase
**Non-goals:** SAMM cookbooks as merge_ok; claiming Gate 10 or M4.

## Reset

Re-run pytest. Optional: `git checkout -- labs/10.1/10.1-lab`.

## Vulnerable behavior (local only)

`merge_ok` always returns true. Forbidden outcome: merge without a threat-model identifier.

## Structural fix

Require a truthy `threat_model` field.

## Verify

```
python3 -m pytest labs/10.1/10.1-lab/tests --impl vulnerable
python3 -m pytest labs/10.1/10.1-lab/tests --impl fixed
```

The first command must fail on `{}`. The second must pass. Honest TM id may pass on both.

## Operate

Signal: `merge_blocked_no_tm`. Do not log bodies. Do not claim Gate 10 or M4.

## Transfer

Clinic HIPAA training as merge. Prompt only.
