# Lab 7.3 — path hit is not provider-message authenticity

**Module:** `7.3`
**Authorized scope:** this directory only. Local course fixture. No live Stripe, GitHub, or clinic webhooks.
**Invariant:** `accept("", "body", "lab-secret")` is false. A matching HMAC over the same raw body may be true.
**Root cause class:** callback trusted because it hit the path
**Non-goals:** live providers, vendor SDK cookbooks as the property.

## Reset

Re-run pytest. Optional: `git checkout -- labs/7.3/7.3-lab`.

## Vulnerable behavior (local only)

`accept` returns true for every triple. Forbidden outcome: unsigned body accepted.

## Structural fix

HMAC-SHA256 over the raw body with disposable `lab-secret`, compared with `compare_digest`. Empty or wrong signatures deny.

## Verify

```
python3 -m pytest labs/7.3/7.3-lab/tests --impl vulnerable
python3 -m pytest labs/7.3/7.3-lab/tests --impl fixed
```

The first command must fail on a missing signature. The second must pass. Honest matching signatures may pass on both.

## Operate

Signal: `webhook_sig_fail`. Do not log the body or the secret.

## Transfer

Clinic lab-result webhook. Prompt only.
