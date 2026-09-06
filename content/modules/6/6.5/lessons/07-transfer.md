# 6.5-LO-07 — Transfer: clinic fetch lab-result PDF from URL

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-1.3.6`. `v5.0.0-3.7.3` Level 3 advanced for user-facing redirects.

## Change the workplace; keep parse-then-allow-list

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic “fetch lab result PDF from URL.” Also name webhook delivery (7.3) as the same egress deputy.

**Product sketch:** EHR-lite importer that `GET`s whatever URL the form posted.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (URL field — not a live clinic or cloud metadata probe);
2. trust assumptions (parsed host allow-list is TCB; “https” prefix is not);
3. forbidden outcome (`allowed` true for link-local, not “HIPAA”);
4. a test idea on a **local** fixture only (predicate, no fetch);
5. residual (redirects, DNS rebinding, IPv6, `file:`, Level 3 redirect notice);
6. WCAG if a human “could not fetch PDF” path is in the claim (readable error, not a spinner that retries the bad URL).

## Mental model: the PDF URL is still an egress steering wheel

```mermaid
flowchart LR
  Pdf[PDF URL field] --> Belief[UI believes it is a document]
  Egress[server GET] --> Reality[attacker-chosen authority]
```

## What graders reject

| Reject | Why |
|---|---|
| “HTTPS only” | Scheme is not host identity |
| Live metadata / clinic probe | Lab policy |
| API7 as the property | Awareness after the cause |

## Practice

One page. No keys. `labs/6.5/6.5-lab` is the only running system you may break.
