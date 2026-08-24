# 1.4 — Risk, people, economics, usable security, and resilience (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Account owner, support agent, abuser in shared housing |
| Objects | Recovery confirm control, backup codes, session |
| Actions | confirm_recovery, cancel, request_support |
| Channels | Browser UI, email (later 4.1), phone support |
| TCB | The control’s accessible name, keyboard path, and non-color cue. |
| Untrusted | Color, hover-only hit targets, “users will figure it out” |
| State / time | Recovery happens under stress and time pressure. |
| 1.1 cell | Safety + availability + confidentiality: inaccessible recovery causes lockout *or* unsafe workarounds that leak notes. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| owner | recovery | keyboard-confirm | allow |
| owner | recovery | color-only | deny-as-control |
| abuser | recovery | coerce | residual |
| support | codes | read-aloud-over-phone | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/1.4/1.4-risk-register` file `recovery.py`.

## Transfer

Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

## Residual risk

Coercion: a physically present attacker can still force a confirmation. Record as residual (do not pretend UX fixes coercion).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
