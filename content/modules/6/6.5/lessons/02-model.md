# 6.5 — Server-side requests and protocol parsing (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).

## Property (start here)

The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.

## Attacker capabilities and trust assumptions

- **Attacker:** User who supplies an unfurl/preview URL.
- **Trust:** Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | app egress, user URL, metadata service |
| Objects | URL, scheme, host |
| Actions | allowed |
| Channels | server-side HTTP |
| TCB | Allow-list of hosts/schemes after parse; no redirect to IP. |
| Untrusted | URL string, redirects, DNS |
| State / time | Redirect hop after first allow. |
| 1.1 cell | Confidentiality of the cloud TCB; integrity of egress. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| user | lab host https | fetch | allow |
| user | link-local | fetch | deny |
| redirect | to link-local | follow | deny |
| webhook | customer URL | 7.3 | signed+allow-list |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/6.5/6.5-lab` file `ssrf.py`.

## Transfer

Webhook delivery (7.3) is egress too.

## Residual risk

Legitimate preview of customer URLs — dedicated egress proxy.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
