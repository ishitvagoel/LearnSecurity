# 7.3 — Webhooks, callbacks, and third-party APIs (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”

## Property (start here)

A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can POST your callback URL.
- **Trust:** Local accept(sig, body, secret).
**Forbidden outcome:** Unsigned webhook body accepted

**Authorized scope:** `labs/7.3/7.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable hook.py accepts missing sig.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: accept('', body, secret) True.

## Vulnerable fixture (local)

```python
def accept(sig, body, secret):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Callback trusted because it hit the path. |
| Impact | Forged “share” or billing events. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/7.3/7.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Signed redirects; outbound webhook SSRF (6.5).

## Non-goals

No live-target instructions. Synthetic data only.
