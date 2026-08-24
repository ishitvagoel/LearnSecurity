# 6.7 — Resource abuse, automation, and availability (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).

## Property (start here)

The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Scripted member; compromised session.
- **Trust:** Local allow(n).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | member, billing account |
| Objects | export slot 1..4 |
| Actions | allow |
| Channels | API loop |
| TCB | Server-side quota. |
| Untrusted | UI disabled button |
| State / time | Burst of 4. |
| 1.1 cell | Availability and cost; secondary confidentiality via extra copies. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| member | export 1-3 | run | allow |
| member | export 4 | run | deny |
| anon | export | run | deny |
| worker | export | 7.4 | service-quota |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/6.7/6.7-lab` file `limit.py`.

## Transfer

Notification fan-out; search complexity.

## Residual risk

Legitimate burst — owned exception.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
