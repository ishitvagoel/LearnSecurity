# 1.4 — Risk, people, economics, usable security, and resilience (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
**Mechanism (not the property):** A React component library “accessible by default” is not your journey. You still test the recovery path.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 1.4 |
|---|---|
| Root cause | Psychological acceptability ignored; control designed for a demo mouse. |
| Preconditions | High-impact action gated by a widget is_usable_accessible() fails. |
| Impact (1.1 cell) | Safety + availability + confidentiality: inaccessible recovery causes lockout *or* unsafe workarounds that leak notes. — Lockout; or user pastes recovery codes into a chat; residual 1.1 confidentiality loss. |
| Prevention | Keyboard operable, name in accessible tree, not color-only (WCAG 2.2). |
| Detection | Support-ticket spike for “can’t click recover”; telemetry on cancel vs confirm without pointer. |
| Recovery | Offer an alternative accessible path; do not lower assurance by emailing the note body. |

## Framework defaults vs application guarantees

A React component library “accessible by default” is not your journey. You still test the recovery path.

## Mechanism limits and bypasses

CAPTCHA or “confirm in the app” can recreate the same exclusion.

Users share an always-on admin session to avoid the broken recovery UX.

## Residual risk

Coercion: a physically present attacker can still force a confirmation. Record as residual (do not pretend UX fixes coercion).

## Practice

Describe the control in words a screen-reader user would hear. If you cannot, it fails.

Run `labs/1.4/1.4-risk-register` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

Banking re-auth dialog.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

WCAG 2.2 Success Criteria 2.1.1 Keyboard, 1.4.1 Use of Color, 2.5.8 Target Size (Minimum) apply to this control. They are not a privacy policy.
