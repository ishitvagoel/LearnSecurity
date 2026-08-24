# 5.3 — Key and secret lifecycle (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | old image, rotated app, attacker with git history |
| Objects | sk-lab-hardcoded, rotated-now |
| Actions | auth |
| Channels | env, repo, image layers |
| TCB | Current secret store; deny list of retired versions. |
| Untrusted | Source tree, Docker history, CI logs |
| State / time | Rotate T+0; attacker uses git from T-1. |
| 1.1 cell | Authenticity of the service credential over time. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| old default | API | auth | deny |
| rotated current | API | auth | allow |
| git history | default | checkout | must-still-deny |
| worker | own secret | auth | separate |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/5.3/5.3-lab` file `secrets.py`.

## Transfer

Envelope encryption DEK vs KEK; compromise runbook.

## Residual risk

PQC migration is a plan, not this test.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
