# 0.1 — Security engineering orientation (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.

## Property (start here)

A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”

## Attacker capabilities and trust assumptions

- **Attacker:** A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.
- **Trust:** You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.
**Forbidden outcome:** HTTP to a non-allowlisted host treated as authorized

**Authorized scope:** `labs/0.1/0.1-orientation` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable/scope.py returns True for https://example.com/.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Learner has a proxy; a public URL is one paste away.

## Vulnerable fixture (local)

```python
def target_is_authorized(url: str) -> bool:
    """Vulnerable: any URL is treated as in-scope."""
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Authorization collapsed into reachability: if TCP connects, it was treated as in-scope. |
| Impact | Unlawful access; course expulsion; harm to uninvolved operators; poisoned evidence. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/0.1/0.1-orientation/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)

## Non-goals

No live-target instructions. Synthetic data only.
