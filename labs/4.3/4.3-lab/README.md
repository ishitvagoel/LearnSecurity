# Lab 4.3 — query string is not a session channel

**Module:** `4.3`
**Authorized scope:** this directory only. Local course fixture. No live CDNs or log drains.
**Invariant:** A session token in the query string is not an acceptable session. Cookie or Authorization only.
**Root cause class:** trust (token in a logged, shared channel)
**Non-goals:** live token replay, real cookies, production logs.

## Reset

No persistent state. Re-run pytest. Optional: `git checkout -- labs/4.3/4.3-lab`.

## Vulnerable behavior (local only)

`session_from_request` returns `query.get("access_token")` first. Forbidden outcome: session established from a query-string token.

## Structural fix

If the query has `access_token`, return `None`. Then read `sc_session` cookie or Authorization.

## Verify

```
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

From repo root:

```
python3 -m pytest labs/4.3/4.3-lab/tests --impl vulnerable
python3 -m pytest labs/4.3/4.3-lab/tests --impl fixed
```

The first command must fail. The second must pass.

## Operate

Signal: `query_token_rejected` with path; never the token. Revoke if it might have been used. Purge logs (3.1).

## Transfer

Clinic appointment deep link; magic-link email (6.6). Prompt only; do not leave this directory.
