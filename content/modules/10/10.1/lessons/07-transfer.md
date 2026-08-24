# 10.1 — Secure software lifecycle and security culture (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Exception path (E6).

**Product sketch:** Clinic: “HIPAA training complete” as merge.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | CODEOWNERS is not a threat model.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/10.1/10.1-lab` stays the only running system you may break.
