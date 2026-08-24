# 3.4 — Business logic and abuse-resistant design (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Invite tokens (6.6) and export quotas (6.7).

**Product sketch:** Clinic: max 3 guardians per child.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | HTML max=5 is not enforcement.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/3.4/3.4-lab` stays the only running system you may break.
