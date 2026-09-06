# E3 — Payments, financial, health, and other high-assurance systems

Pass A specification. Lesson prose lives in `lessons/`. The same idempotency key must not double-charge. This lab does not claim PCI scope. Do not mark Gate 7 complete.

## Identity

- **id:** E3
- **slug:** payments-financial-health-and-other-high-assurance-systems
- **title:** Payments, financial, health, and other high-assurance systems
- **phase / track / difficulty:** 7 / elective / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Opens after Phase 7; 2.4 time; 6.6 consume-once; 7.3 webhooks.
- **routeTags:** complete, elective
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **capture predicate** so two `capture("k1")` calls leave `charge_count() == 1`.
2. Name attacker capabilities (retry after 504; double-click) and trust assumptions (local ledger; synthetic amounts; no PAN).
3. Transfer: health append-only audit; simulated copay — without treating a PCI SAQ as this cell.

## Prerequisite concepts

2.4 retry; 6.6 consume-once; 5.1 no extra copies of sensitive data.

## Misconceptions

- PCI SAQ is this cell.
- Stripe idempotency is your local ledger unless you use it.
- A new key on each retry is fine.

## Concept map

Always-append capture (break) → key as identity (this module) → webhook vs capture race (7.3) → no PAN stored (5.1). Residual: client mints a new key each retry.

## Invariant prompts

- What must remain true for a second `capture("k1")`?
- What fails if the processor is idempotent but your ledger is not?

## Threat-model prompts

- What can a 504 retry do to money-like state?
- What residual remains if the client sends a new key each click?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/E3/e3-lab`. Forbidden: duplicate capture double-charges. No real PAN or processors.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-2.3.4` locking so limited resources cannot be double-booked (Level 2); `v5.0.0-2.3.3` succeed entirely or roll back. `v5.0.0-13.1.2` documented connection limits is **Level 3, labeled advanced**.
- PCI DSS 4.0.1: **awareness** / sector scoping — this lab does **not** claim PCI scope or store PAN.
- ASVS Level 3 as *selection vocabulary* for high-assurance profiles, not as “we are L3 because we have a SAQ.”

## Review triggers

Two capture(k1) charge twice; PAN-like strings; webhook vs capture race ignored; PCI claimed from this lab.

## Time budget and SecureCollab

Elective. Simulated ledger only.

## Operational considerations

`duplicate_capture_denied`. Credit the extra in a runbook; still fail the test first.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: key is identity; PCI is awareness not scope |
