# 2.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

HTTP, TLS, proxies, CDNs, and cache keys

## Evidence checklist

- [ ] Request-path diagram and cache-key tests
- [ ] Transfer task (Clinic: cached /patients/me.)
- [ ] Lab `labs/2.2/2.2-request-path`: what must not happen: **Shared cache returns tenant A's body to tenant B**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: cdn_hit_tenant_mismatch; purge playbook.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **2.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/2.2.md`.
