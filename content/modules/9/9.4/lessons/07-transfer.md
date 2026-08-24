# 9.4 — Automated analysis and tool orchestration (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** SCA CVE vs actually called function.

**Product sketch:** Clinic: 50 unmapped HIGHs.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | GitHub code scanning default is not your policy.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/9.4/9.4-lab` stays the only running system you may break.
