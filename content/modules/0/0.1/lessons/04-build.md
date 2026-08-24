# 0.1 — Security engineering orientation (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.

## Property (start here)

A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”

## Attacker capabilities and trust assumptions

- **Attacker:** A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.
- **Trust:** You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.
Parse hostname; compare to ALLOWED_HOSTS; default False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
from urllib.parse import urlparse

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "lab.securecollab.test"}


def target_is_authorized(url: str) -> bool:
    """Fixed: only named local lab hosts; public hosts are out of scope."""
    host = (urlparse(url).hostname or "").lower()
    return host in ALLOWED_HOSTS
```

## Why this restores the cell

Allow-list local names; fail closed; written scope template.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Burp, ZAP, or curl existing is not authorization. CSF GV is governance language, not a pentest permit.

An allow-list of three names still fails if you SSH to a stolen hostname that resolves locally via /etc/hosts tricks — check what you actually connected to.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)

## Residual risk

Official Juice Shop on your machine is OK; a random cloud Juice Shop you do not own is not.
