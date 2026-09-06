# 7.4-LO-07 — Transfer: clinic batch-export worker

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-13.2.1`. NIST SP 800-207 as architecture guidance only.

## Change the workplace; keep a worker principal

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic batch-export worker. Also name outbox pattern and event schemas.

**Product sketch:** EHR-lite “Export overnight” that copies the clinician cookie into the Celery task so “the job knows who asked.”

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (stolen session stuffed into a job, or inherited request context — not a live clinic);
2. trust assumptions (worker authenticates as `worker-sc` is TCB; VLAN/internal queue/zero-trust sticker are not);
3. forbidden outcome (`exporter({user_session: alice})` succeeds, not “HIPAA”);
4. a test idea on a **local** fixture only (no live broker);
5. residual (god-mode DB role 3.3, 2.4 retry after revoke, Level 3 originating subject, 7.2 dumps);
6. WCAG if a human export path is in the claim (readable “queued as service,” not a spinner that retries forever).

## Mental model: cookie in the job is still a session

```mermaid
flowchart LR
  Copy["copy request cookie into task"] --> Belief[dev believes convenience]
  Run["worker uses that cookie"] --> Reality[confused deputy]
```

## What graders reject

| Reject | Why |
|---|---|
| “Zero trust is enabled” | Guidance, not the oracle |
| Live clinic / public broker | Lab policy |
| “Internal queue is trusted” | Payload is still untrusted |

## Practice

One page. No keys. `labs/7.4/7.4-lab` is the only running system you may break.
