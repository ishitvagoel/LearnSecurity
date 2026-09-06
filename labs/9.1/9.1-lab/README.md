# Lab 9.1 — status=done is not AUTHZ-1 coverage

**Module:** `9.1`
**Authorized scope:** this directory only. Local course fixture. No live ASVS portals or clinic systems.
**Invariant:** a row with `asserts_isolation: False` does not cover `AUTHZ-1`. Honest isolation-assert rows may count as covered.
**Root cause class:** membership / status without an isolation assert
**Non-goals:** ASVS certification cookbooks, claiming Gate 9.

## Reset

Re-run pytest. Optional: `git checkout -- labs/9.1/9.1-lab`.

## Vulnerable behavior (local only)

`covered` is true if any test dict has `req == req_id`. Forbidden outcome: status-only row counted as AUTHZ-1 coverage.

## Structural fix

Require `req == req_id` **and** `asserts_isolation`.

## Verify

```
python3 -m pytest labs/9.1/9.1-lab/tests --impl vulnerable
python3 -m pytest labs/9.1/9.1-lab/tests --impl fixed
```

The first command must fail on the status-only row. The second must pass. Honest isolation-assert rows may pass on both.

## Operate

Signal: `unmapped_req_blocks_release`. Do not log note bodies. Do not claim Gate 9.

## Transfer

Clinic HIPAA “done” column. Prompt only.
