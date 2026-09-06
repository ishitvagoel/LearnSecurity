# Lab 0.1 — reachability is not authorization

**Module:** `0.1`
**Authorized scope:** this directory only. Local course fixture. No public or third-party targets.
**Invariant:** `target_is_authorized("https://example.com/")` is false. Named local lab hosts may be true.
**Root cause class:** authorization collapsed into TCP reachability
**Non-goals:** WSTG as a licence to scan the internet; Burp as a permit.

## Reset

Re-run pytest. Optional: `git checkout -- labs/0.1/0.1-orientation`.

## Vulnerable behavior (local only)

Every URL is treated as in-scope. Forbidden outcome: HTTP to a non-allowlisted host treated as authorized.

## Structural fix

Allow only `127.0.0.1`, `localhost`, and `lab.securecollab.test`.

## Verify

```
python3 -m pytest labs/0.1/0.1-orientation/tests --impl vulnerable
python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed
```

The first command must fail `test_public_host_is_out_of_scope`. The second must pass. Honest localhost tests may pass on both.

## Operate

Signal: `out_of_scope` with host only. Never store response bodies from denied hosts.

## Transfer

Contractor asked to “quickly test our customer’s WordPress.” Prompt only — do not hit that host.
