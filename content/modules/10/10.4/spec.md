# 10.4 — Deployment and configuration hardening

Pass A specification. Lesson prose lives in `lessons/`. Production must not boot with debug — not “just for five minutes.” Do not mark M4 or Gate 10 complete.

## Identity

- **id:** 10.4
- **slug:** deployment-and-configuration-hardening
- **title:** Deployment and configuration hardening
- **phase / track / difficulty:** 10 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 5.3 secrets; 10.2 artifacts; 10.3 workload identity.
- **routeTags:** complete, web-api
- **releaseMilestone:** M4
- **masteryGate:** 10

## Objective hierarchy

1. Produce a **boot predicate** so `boot_ok("prod", True)` is false.
2. Name attacker capabilities (anyone who finds `/debug`; error pages with traces) and trust assumptions (local `boot_ok(env, debug)`).
3. Transfer: clinic Django `DEBUG=True`; feature flag that disables authz — without treating `NODE_ENV` or a canary as the invariant.

## Prerequisite concepts

5.3 secrets out of artifacts; 10.2 digest of what you run; 13.4 unintended leakage. ASVS `v5.0.0-13.4.2` (debug off in prod). CISA Secure by Design remains **unverified**. Top 10:2025 A02 is **awareness after** the cause.

## Misconceptions

- IaC means hardened.
- Canary equals secure config.
- Feature flags are not TCB.
- `NODE_ENV=production` is the debug-off check.
- “Just for five minutes” is not a production boot.

## Concept map

Always-true boot (break) → refuse prod+debug (this module) → secrets not in traces (5.3 / `v5.0.0-13.3.1`) → admin not on `0.0.0.0` → rollback drill. Residual: emergency debug with E6 timebox; other flags.

## Invariant prompts

- What must remain true for `boot_ok("prod", True)`?
- What fails if debug is false but a feature flag disables authorization?

## Threat-model prompts

- What can go wrong if production boots with debug?
- What residual remains if debug is off but `/metrics` is public (`v5.0.0-13.4.5`)?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/10.4/10.4-lab`. Forbidden: production process boots with debug enabled. No live production hosts.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-13.4.2` debug modes disabled in production (Level 2); `v5.0.0-13.4.5` documentation and monitoring endpoints not exposed unless intended; `v5.0.0-13.3.1` secrets not in artifacts. `v5.0.0-13.4.6` detailed backend version leakage is **Level 3, labeled advanced**.
- CISA Secure by Design: **unverified** living program page (pin already 403 on fetch) — manufacturer ownership of defaults, not the lab oracle.
- OWASP Top 10:2025 A02: **awareness after** the fail-open cause, not the syllabus.

## Review triggers

Prod+debug boots; admin on `0.0.0.0`; migration fail-open; no rollback drill; feature flag that disables authz.

## Time budget and SecureCollab

Evidence: production-readiness review + local `boot_ok` tests + rollback named. Feeds Gate 10 / M4 (not-attempted).

## Operational considerations

`prod_debug_forbidden`. Kill the process; rotate secrets that appeared in traces. Emergency debug with E6.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: prod-debug-must-not-boot; NODE_ENV is not the predicate |
