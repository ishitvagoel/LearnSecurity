# 1.4 — Risk, people, economics, usable security, and resilience (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Support-ticket spike for “can’t click recover”; telemetry on cancel vs confirm without pointer. |
| Signal (no bodies) | Recovery success/fail by input modality; never log recovery codes. |
| Revoke / recover | Offer an alternative accessible path; do not lower assurance by emailing the note body. |
| Residual | Coercion: a physically present attacker can still force a confirmation. Record as residual (do not pretend UX fixes coercion). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/1.4/1.4-risk-register`.

## Transfer

Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

## Usability

WCAG 2.2 Success Criteria 2.1.1 Keyboard, 1.4.1 Use of Color, 2.5.8 Target Size (Minimum) apply to this control. They are not a privacy policy.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
