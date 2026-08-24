# 6.5 — Server-side requests and protocol parsing (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).

## Property (start here)

The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.

## Attacker capabilities and trust assumptions

- **Attacker:** User who supplies an unfurl/preview URL.
- **Trust:** Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.
**Forbidden outcome:** Server-side fetch to link-local metadata is allowed

**Authorized scope:** `labs/6.5/6.5-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable ssrf.py allows any URL.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: allowed(link-local) True.

## Vulnerable fixture (local)

```python
from urllib.parse import urlparse
def allowed(url):
    return urlparse(url).scheme in {'http','https'}
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Server fetches attacker-chosen authority. |
| Impact | In real clouds, credential theft; here, the test fails closed conceptually. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/6.5/6.5-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Webhook delivery (7.3) is egress too.

## Non-goals

No live-target instructions. Synthetic data only.
