# 10.4 — Deployment and configuration hardening (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Feature flag that disables authz.

**Product sketch:** Clinic: Django DEBUG=True.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Next.js NODE_ENV=development in prod compose files.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/10.4/10.4-lab` stays the only running system you may break.
