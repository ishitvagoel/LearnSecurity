# 6.2 — Browser injection and active content (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
render encodes < to &lt; and no raw <img.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
import html
def render(body):
    return f'<p>{html.escape(body, quote=True)}</p>'
```

## Why this restores the cell

Encode for HTML text; framework safe constructors; CSP extra.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

React defaults help in JSX, not in dangerouslySetInnerHTML or a FastAPI HTML template.

HTML encoding is wrong in a JS string context.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Markdown-to-HTML sanitizer as a second parser (2.1).

## Residual risk

Trusted admin HTML — explicit tiny exception.
