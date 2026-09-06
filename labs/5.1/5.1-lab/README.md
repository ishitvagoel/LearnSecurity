# Lab 5.1 — analytics copy after delete

**Module:** `5.1`
**Authorized scope:** this directory only. Local course fixture. No live warehouses.
**Invariant:** After `delete_account("alice")`, `body_retained("alice")` and `search_retained("alice")` are None. Retention is a 1.1 privacy/confidentiality property.
**Root cause class:** incomplete deletion graph (secondary copies)
**Non-goals:** live analytics, real PII, GDPR theater.

## Reset

conftest calls `reset()`. Re-run pytest. Optional: `git checkout -- labs/5.1/5.1-lab`.

## Vulnerable behavior (local only)

`delete_account` pops `NOTES` only. `ANALYTICS` and `SEARCH` still hold the body. Forbidden outcome: analytics (or search) copy still holds the note body after account deletion.

## Structural fix

The delete use-case walks the inventory: notes, analytics, search. Missing copy is deny of the property.

## Verify

From repo root:

```
python3 -m pytest labs/5.1/5.1-lab/tests --impl vulnerable
python3 -m pytest labs/5.1/5.1-lab/tests --impl fixed
```

The first command must fail on the deny tests. The second must pass. The active-account test may pass on both.

## Operate

Signal: `deleted_user_body_hits` with user id; never the body. Purge warehouse partitions.

## Transfer

Clinic appointment card with notes. Prompt only; do not leave this directory.
