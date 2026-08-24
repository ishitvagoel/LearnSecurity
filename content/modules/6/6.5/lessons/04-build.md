# 6.5 — Server-side requests and protocol parsing (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).

## Property (start here)

The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.

## Attacker capabilities and trust assumptions

- **Attacker:** User who supplies an unfurl/preview URL.
- **Trust:** Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.
link-local False; lab https host True.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
from urllib.parse import urlparse
ALLOW={'lab.securecollab.test'}
def allowed(url):
    u=urlparse(url)
    host=(u.hostname or '').lower()
    if host in {'169.254.169.254','127.0.0.1','localhost'}:
        return False
    return u.scheme=='https' and host in ALLOW
```

## Why this restores the cell

Allow-list; parse then pin; block link-local, loopback, metadata; no open redirects.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

requests.get is not an allow-list.

DNS rebinding after allow — pin IP or block.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Webhook delivery (7.3) is egress too.

## Residual risk

Legitimate preview of customer URLs — dedicated egress proxy.
