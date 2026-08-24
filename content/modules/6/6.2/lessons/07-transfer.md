# 6.2 — Browser injection and active content (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Markdown-to-HTML sanitizer as a second parser (2.1).

**Product sketch:** Clinic patient nickname field.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | React defaults help in JSX, not in dangerouslySetInnerHTML or a FastAPI HTML tem… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/6.2/6.2-lab` stays the only running system you may break.
