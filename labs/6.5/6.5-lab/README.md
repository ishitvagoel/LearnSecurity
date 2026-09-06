# Lab 6.5 — a preview URL is untrusted authority

**Module:** `6.5`
**Authorized scope:** this directory only. Local course fixture. No live fetches.
**Invariant:** `allowed` is false for link-local metadata and loopback. HTTPS to the named lab host may be true.
**Root cause class:** server would fetch attacker-chosen authority
**Non-goals:** cloud metadata probes, public SSRF, following redirects.

## Reset

Re-run pytest. Optional: `git checkout -- labs/6.5/6.5-lab`.

## Vulnerable behavior (local only)

`allowed` returns true for any `http`/`https` scheme. Forbidden outcome: link-local metadata URL allowed. Tests call the predicate only.

## Structural fix

Parse, require `https`, require hostname in a small allow-list, deny link-local and loopback.

## Verify

```
python3 -m pytest labs/6.5/6.5-lab/tests --impl vulnerable
python3 -m pytest labs/6.5/6.5-lab/tests --impl fixed
```

The first command must fail on link-local (and loopback). The second must pass. Honest lab-host https may pass on both.

## Operate

Signal: `egress_denied`. Do not log full URLs with tokens. Do not fetch the denied destination.

## Transfer

Clinic fetch-PDF URL. Prompt only.
