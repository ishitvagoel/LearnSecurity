# 2.1-LO-01 — Bytes vs characters, Unicode, canonicalization, interpreter boundaries

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP Application Security Verification Standard 5.0.0 (final). Awareness lists (Top 10, CWE Top 25) are regression checks, not the outline.

## Property (start here)

What must remain true of **SecureCollab** (or the elective system) regarding **Bytes, text, formats, parsers, and interpreters** when an attacker with stated capabilities acts, a component fails, or a human follows a stressful recovery path?

Invariant prompt for this object: Each interpreter boundary on the scoped path is named; Disagreeing parsers are treated as an invariant failure; No live-target encoding attacks or lesson-page weaponized payloads

## Attacker capabilities and trust assumptions

State both, or the claim is a slogan:

- **Attacker:** anyone who can reach the local lab API; a logged-in member of another tenant; a stolen worker identity; a hostile mobile client where Phase 8 applies.
- **Trust:** FastAPI + PostgreSQL with least-privilege roles are in the TCB for server-side mediation; the Next.js bundle and Android client are **not**. Lab honesty is assumed; no public targets.

Threat-model prompts from the spec:

- Where can an attacker choose encoding, BOM, or nested format?
- Which shared parser is a least-common-mechanism risk?

## Root cause, preconditions, impact, prevention, detection, recovery

| Slice | For Bytes, text, formats, parsers, and interpreters |
|---|---|
| Root cause | Wrong trust in a mechanism, skipped mediation on an indirect path, or a confused interpreter — not “missing a scanner finding.” |
| Preconditions | The local fixture is reachable; the learner is authorized only on this lab; synthetic data only. |
| Impact | Tenant notes, identity, or availability of SecureCollab can fail the named property. |
| Prevention | Smallest structural mechanism that restores the invariant (not a blacklist-only patch). |
| Detection | Logs/alerts that fire when the forbidden outcome is attempted. |
| Recovery | Revoke, rotate, purge, restore from a known-good backup, and record residual risk. |

## Framework defaults vs application guarantees

FastAPI, Next.js, PostgreSQL, or Android “secure defaults” are not the application guarantee for **Bytes, text, formats, parsers, and interpreters**. Name what the app must still enforce.

## Mechanism limits

A green scanner, a named product (JWT, TLS, bcrypt), or an awareness-list item does not prove the invariant. Universal checkboxes fail when risk-based selection is required.

## Practice (local, authorized)

Complete the associated lab under `labs/2.1/` if a labSpec exists. Observe the forbidden outcome on `vulnerable/`. Do not target non-lab systems. Do not copy weaponized payloads into notes.

Safe task: write one testable sentence that would fail if the **bytes** property were false.

## Transfer

Change one asset, principal, or boundary (new worker, webhook, offline cache, or clinic-booking card). Redraw the claim without using a Top 10 item as the definition of security.

## Usability and accessibility

Where a human is part of the control (login, recovery, consent, admin impersonation), the journey must remain usable and accessible (WCAG 2.2 final as the web baseline). Do not rely on color, mouse-only, or memory-only secrets.

## Misconceptions to refuse

- Strings are characters; UTF-8 is just text
- Validation, sanitization, encoding, and parameterization are interchangeable
- Successful JSON.parse means unambiguous meaning across languages
- Framework auto-escaping completely mediates interpreters

## Non-goals

Live-target attacks, real PII, production secrets, and treating this lesson as a product tutorial.
