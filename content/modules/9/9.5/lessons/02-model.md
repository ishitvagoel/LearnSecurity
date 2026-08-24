# 9.5 — Authorized assessment, reporting, and remediation (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | assessor, developer, retester |
| Objects | finding, retest field |
| Actions | close_finding |
| Channels | tracker |
| TCB | Retest artifact linked. |
| Untrusted | “we deployed Friday” |
| State / time | After supposed fix. |
| 1.1 cell | Integrity of the fix loop. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| finding | retest pass | close | allow |
| finding | retest missing | close | deny |
| finding | PDF attached | close | deny |
| variant | same cause | open | allow |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/9.5/9.5-lab` file `pentest.py`.

## Transfer

KEV vs internal-only.

## Residual risk

Unknown variants — hunt (same root cause).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
