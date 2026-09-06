# 9.1-LO-07 — Transfer: clinic HIPAA done column

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) Level 2 backbone; MASVS 2.1.0 STORAGE for the mobile analogue. SSDF 1.2 IPD remains **draft**. Do not use MASVS L1/L2/R.

## Change the workplace; keep status from meaning coverage

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `covered("AUTHZ-1", [status-only])` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic HIPAA “done” column. Also name MASVS-STORAGE for 8.2.

**Product sketch:** EHR-lite “we imported the HIPAA checklist and marked isolation done,” plus a green CI.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (optimistic status column — not a live hospital);
2. trust assumptions (coverage predicate is TCB; checklist membership is not);
3. forbidden outcome (`covered("AUTHZ-1", status_only)` true, not “HIPAA”);
4. a test idea on a **local** fixture only;
5. residual (unnamed Level 3 `v5.0.0-8.3.2`, exceptions without expiry);
6. WCAG if a human exception path exists (state what is uncovered and when it expires).

## Mental model: same predicate, clinical checklist

```mermaid
flowchart LR
  Col[HIPAA done column] --> Belief[isolation is finished]
  Pred[no isolation assert] --> Reality["1.2 hole ships"]
```

If the HIPAA column is Done while `covered` only matches `req`, the cell is gone. ASVS PDF import, pytest-cov, and SSDF 1.2 IPD (draft) do not assert isolation. MASVS-STORAGE for 8.2 is the same predicate family — name it, do not scrape a live MASVS portal here. A 200-only test that sets the isolation flag by mistake is 9.3.

The clinic rewrite still has to keep the SecureCollab fork: status-only not covered, isolation-assert may count. Marking HIPAA isolation done without an isolation assert leaves `covered("AUTHZ-1", status_only)` true. The local pytest analogue is `test_status_only_row_is_not_coverage` — on a fixture, not a live GRC.

## What graders reject

| Reject | Why |
|---|---|
| “ASVS imported” | Inventory, not coverage |
| Live clinic / real PHI | Lab policy |
| “SSDF 1.2 certified” | 1.2 is IPD draft; not Gate 9 |
| Green CI as AUTHZ-1 | Wrong observation |
| MASVS L1 as current | Obsolete MASVS levels |

## Practice

One page. No keys. `labs/9.1/9.1-lab` is the only running system you may break. Do not scrape a public checklist.

## Non-goals

Live-target GRC. Real PHI. Claiming Gate 9 from this page.
