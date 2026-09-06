# 6.7-LO-07 — Transfer: clinic bulk-export patients

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-2.4.1`. API4/API6 awareness after. WCAG 2.2 for the deny message.

## Change the workplace; keep a per-subject resource account

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic bulk-export patients. Also name notification fan-out and search complexity (7.1).

**Product sketch:** EHR-lite “Export all” with a disabled button in the SPA.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (scripted clinician session — not a live clinic);
2. trust assumptions (server `n <= 3` is TCB; SPA disable and IP rate limit are not);
3. forbidden outcome (`allow(4)` true, not “HIPAA”);
4. a test idea on a **local** fixture only (no public load test);
5. residual (new accounts, GraphQL aliases, Level 3 human timing, extra copies 5.1);
6. WCAG if a human quota path is in the claim (readable “try tomorrow,” not a spinner that retries).

## Mental model: bulk export is still a budget row

```mermaid
flowchart LR
  Bulk[export all] --> Belief[UI believes one click]
  N[n = 4] --> Reality[unbounded CSVs if allow is true]
```

## What graders reject

| Reject | Why |
|---|---|
| “CAPTCHA is on” | Not a resource account |
| Live clinic / public load test | Lab policy |
| Autoscaling | Spends more; does not enforce the cap |

## Practice

One page. No keys. `labs/6.7/6.7-lab` is the only running system you may break.
