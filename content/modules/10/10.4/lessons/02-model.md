# 10.4 — Deployment and configuration hardening (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | prod process, attacker |
| Objects | debug flag |
| Actions | boot_ok |
| Channels | env, feature flags |
| TCB | Fail closed on prod+debug. |
| Untrusted | Default FastAPI debug, leftover env from staging |
| State / time | Boot; hot flag. |
| 1.1 cell | Least privilege of the running config + confidentiality of traces. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| prod | debug True | boot | deny |
| prod | debug False | boot | allow-if-else-ok |
| dev | debug True | boot | allow-local |
| flag | skip_authz | on | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/10.4/10.4-lab` file `cfg.py`.

## Transfer

Feature flag that disables authz.

## Residual risk

Emergency debug with E6 timebox.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
