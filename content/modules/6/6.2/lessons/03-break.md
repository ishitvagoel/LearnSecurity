# 6.2 — Browser injection and active content (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
**Forbidden outcome:** Unencoded markup reaches the HTML interpreter

**Authorized scope:** `labs/6.2/6.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable html.py echoes markup.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: render echoes <img without encoding.

## Vulnerable fixture (local)

```python
def render(body):
    return f'<p>{body}</p>'
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | HTML grammar mixed with data. |
| Impact | Active content in the victim origin. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/6.2/6.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Markdown-to-HTML sanitizer as a second parser (2.1).

## Non-goals

No live-target instructions. Synthetic data only.
