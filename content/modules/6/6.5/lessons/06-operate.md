# 6.5-LO-06 — Detect egress_denied

**Kind:** operations-exercise
**Loop step:** 6 Operate
**Standards:** NIST CSF 2.0 (final) DE/RS/RC as outcome labels; OWASP ASVS 5.0.0 (final) `v5.0.0-1.3.6`.

## Prevention is not absolute

A new webhook path can fetch again. Pair detect and recover. Do not log full URLs if they contain tokens (4.3). Do not fetch the denied destination “to confirm.”

## Mental model: denied host is a signal

```mermaid
flowchart TD
  Url[preview URL] --> Deny{not on allow-list?}
  Deny -->|yes| Metric["egress_denied += 1"]
  Metric --> Alert["reason=egress_denied no url"]
  Alert --> Stop[Do not fetch]
```

| Outcome | This module |
|---|---|
| Detect | `egress_denied` |
| Signal | request id, reason code; never the full URL if it holds secrets |
| Recover | Keep deny; do not rotate a real instance role in this course |
| Residual | DNS rebinding; customer-URL proxy |

## Practice

Write one log line you would accept. Tie it to `labs/6.5/6.5-lab`.

```
log_denied reason=egress_denied class=link_local request_id=req_65e
```

Reject any line that includes a full URL with a query token, a note body, or a live-fetch transcript.

## Transfer

Clinic: detect PDF fetches to non-allow-listed hosts; do not paste the URL into the ticket if it has a token.

## Non-goals

A cloud WAF product name is not the property.
