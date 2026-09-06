# 10.4-LO-07 — Transfer: clinic Django DEBUG=True

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** ASVS `v5.0.0-13.4.2`. CISA Secure by Design **unverified**. Top 10:2025 A02 awareness after the cause. `v5.0.0-13.4.6` Level 3 **advanced**.

## Change the workplace; keep NODE_ENV from meaning debug-off

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `boot_ok("prod", True)` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic: Django `DEBUG=True`. Also name a feature flag that disables authz.

**Product sketch:** EHR-lite “we left DEBUG on for five minutes so support can see traces,” plus “NODE_ENV is production and we canary 10%.”

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (anyone who finds `/debug` or an error page — not a live clinic host attack);
2. trust assumptions (prod+debug deny is TCB; NODE_ENV/canary/IaC are not);
3. forbidden outcome (`boot_ok("prod", True)` true, not “HIPAA”);
4. a test idea on a **local** fixture only (no live Django);
5. residual (other flags, sidecar debug, `v5.0.0-13.4.6` Level 3, E6 emergency debug);
6. WCAG if boot is human-read (say prod debug refused).

## Mental model: five minutes vs a boot

```mermaid
flowchart LR
  Five[five minutes] --> Belief[temporary]
  Boot[debug true in prod] --> Reality[the process is debug]
```

If support asked for five minutes while `boot_ok` is always true, the cell is gone. `NODE_ENV`, a canary, and an IaC file do not compare `env` to `debug`. A feature flag that disables authz is the same fail-open family — name it, do not hit a live `/debug` here. Top 10:2025 A02 is a regression label *after* the fail-open cause, not the syllabus. CISA Secure by Design stays unverified. `v5.0.0-13.4.6` is Level 3 advanced: version leakage can remain with debug off.

The clinic rewrite still has to keep the SecureCollab fork: prod+debug denied, prod without debug may boot. Setting `NODE_ENV` without the conjunction leaves `boot_ok("prod", True)` true. The local pytest analogue is `test_prod_debug_must_not_boot` — on a fixture, not a live host.

## What graders reject

| Reject | Why |
|---|---|
| “NODE_ENV is production” | String, not the conjunction |
| Live Django / public `/debug` tutorial | Lab policy |
| “A02 so 1.2 is done” | Awareness after the cause |
| “canary 10%” | Rollout, not boot_ok |
| “Gate 10 complete” | Forbidden stamp |

## Practice

One page. No keys. `labs/10.4/10.4-lab` is the only running system you may break. Do not boot a live host.

## Non-goals

Live-production attacks. Public debug-endpoint walkthroughs. Claiming Gate 10 or M4 from this page.
