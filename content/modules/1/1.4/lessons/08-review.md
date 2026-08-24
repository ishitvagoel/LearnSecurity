# 1.4 — Risk, people, economics, usable security, and resilience (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
Review `labs/1.4/1.4-risk-register/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/1.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): Confirm button has no accessible name
- Seeded smell (label it yourself): Destructive action distinguished only by red vs green
- Seeded smell (label it yourself): Mouse-only drag-to-confirm
- Seeded smell (label it yourself): Risk register lists residual as “users should be careful”

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Accessibility is a separate compliance track from security
- Friction always increases security
- Work factor applies only to attackers, not to legitimate users stuck in a flow

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

## HITL / WCAG 2.2

WCAG 2.2 Success Criteria 2.1.1 Keyboard, 1.4.1 Use of Color, 2.5.8 Target Size (Minimum) apply to this control. They are not a privacy policy.
