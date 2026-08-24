# 5.4 — Secure communication and channel binding (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
**Forbidden outcome:** Client X-Forwarded-Proto treated as TLS

**Authorized scope:** `labs/5.4/5.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable channel.py trusts the header.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Header https + socket http => True.

## Vulnerable fixture (local)

```python
def channel_is_https(headers, server_scheme):
    return headers.get('X-Forwarded-Proto') == 'https' or server_scheme == 'https'
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Confused deputy: app believes client about the channel. |
| Impact | Session cookies marked as if Secure; users stay on cleartext; HSTS skipped. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/5.4/5.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

mTLS service identity vs this header.

## Non-goals

No live-target instructions. Synthetic data only.
