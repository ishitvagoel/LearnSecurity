# E2-LO-07 — Transfer: clinic Report-Only as HIPAA header

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** ASVS `v5.0.0-3.4.3`. CSP3 **draft**.

## Change the workplace; keep a header from meaning isolation

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic: Report-Only as “HIPAA header.” Also name Trusted Types and COOP/COEP.

**Product sketch:** EHR-lite “we ship Content-Security-Policy-Report-Only so XSS is blocked,” plus “the reporting dashboard is green.”

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (XSS that would only be logged — not a live clinic XSS);
2. trust assumptions (enforcing header name is TCB; Report-Only/Helmet/dashboard are not);
3. forbidden outcome (`isolation_enforced` true on Report-Only, not “HIPAA”);
4. a test idea on a **local** fixture only (no live origin);
5. residual (encoding skipped, CDN strip, XS-Leaks, Trusted Types **draft**, `v5.0.0-3.4.7` Level 3);
6. WCAG if a blocked-script message is shown.

## Mental model: green report vs blocked script

```mermaid
flowchart LR
  Dash[dashboard green] --> Belief[blocked]
  Ro[Report-Only] --> Reality[script ran]
```

## What graders reject

| Reject | Why |
|---|---|
| “we have CSP” | Name may be Report-Only |
| Live XSS tutorial | Lab policy |
| “CSP3 so 6.2 is done” | Draft layer, not encoding |

## Practice

One page. No keys. `labs/E2/e2-lab` is the only running system you may break.
