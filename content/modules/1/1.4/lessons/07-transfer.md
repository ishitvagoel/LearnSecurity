# 1.4 — Risk, people, economics, usable security, and resilience (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

**Product sketch:** Banking re-auth dialog.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | A React component library “accessible by default” is not your journey. You still… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/1.4/1.4-risk-register` stays the only running system you may break.
