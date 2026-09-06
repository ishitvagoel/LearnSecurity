# Lab 6.3 — ambient cookies are not consent to share

**Module:** `6.3`
**Authorized scope:** this directory only. Local course fixture. No live third-party sites.
**Invariant:** `allow_share` from a foreign origin without a matching CSRF token is false. Cookie alone is not consent.
**Root cause class:** cookie authority without site-bound intent
**Non-goals:** live CSRF against public apps, clickjacking trophies, token cookbooks.

## Reset

Re-run pytest. Optional: `git checkout -- labs/6.3/6.3-lab`.

## Vulnerable behavior (local only)

`allow_share` returns true whenever a session cookie is present. Forbidden outcome: cross-origin state-changing POST authorized by cookie alone.

## Structural fix

Require session cookie **and** matching origin **and** matching token. SameSite is a helper, not this predicate.

## Verify

```
python3 -m pytest labs/6.3/6.3-lab/tests --impl vulnerable
python3 -m pytest labs/6.3/6.3-lab/tests --impl fixed
```

The first command must fail on foreign-origin and same-origin-without-token tests. The second must pass. Honest same-origin-with-token may pass on both. Missing cookie may pass on both.

## Operate

Signal: `foreign_origin_post_denied`. Do not log cookies or tokens. Revoke surprise shares.

## Transfer

Clinic share-with-partner POST. Prompt only.
