# 3.4 — Business logic and abuse-resistant design (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Owner, automated client |
| Objects | share count, cap=5 |
| Actions | add_share |
| Channels | API loop |
| TCB | Server-side cap in the same transaction as insert. |
| Untrusted | Client disabling the “max 5” UI |
| State / time | Eight rapid POSTs. |
| 1.1 cell | Integrity of the share policy; availability of the owner’s threat model (too many readers). |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| owner | share 1-5 | add | allow |
| owner | share 6 | add | deny |
| script | parallel 6 | add | deny-with-lock |
| support | override | add | audited-exception |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/3.4/3.4-lab` file `share_limit.py`.

## Transfer

Invite tokens (6.6) and export quotas (6.7).

## Residual risk

Legitimate teams >5 need an owned exception (E6).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
