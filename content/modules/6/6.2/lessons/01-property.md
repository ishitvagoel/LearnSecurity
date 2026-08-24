# 6.2 — Browser injection and active content (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
**Mechanism (not the property):** React defaults help in JSX, not in dangerouslySetInnerHTML or a FastAPI HTML template.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 6.2 |
|---|---|
| Root cause | HTML grammar mixed with data. |
| Preconditions | render echoes <img without encoding. |
| Impact (1.1 cell) | Integrity of the HTML interpreter; confidentiality of sessions if combined with 2.3 fail. — Active content in the victim origin. |
| Prevention | Encode for HTML text; framework safe constructors; CSP extra. |
| Detection | CSP reports (not enforcement by themselves — E2). |
| Recovery | Patch content; rotate sessions if cookie not HttpOnly. |

## Framework defaults vs application guarantees

React defaults help in JSX, not in dangerouslySetInnerHTML or a FastAPI HTML template.

## Mechanism limits and bypasses

HTML encoding is wrong in a JS string context.

DOM clobbering, prototype pollution, markdown pipeline.

## Residual risk

Trusted admin HTML — explicit tiny exception.

## Practice

Name the context (HTML text vs attr vs JS vs URL).

Run `labs/6.2/6.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Markdown-to-HTML sanitizer as a second parser (2.1).

Clinic patient nickname field.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
