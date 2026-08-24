# 9.4 — Automated analysis and tool orchestration (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | CI, security champion |
| Objects | HIGH F1, map {} |
| Actions | ship_ok |
| Channels | SAST/DAST/SCA |
| TCB | Gate: HIGH needs req id + decision. |
| Untrusted | Tool default severity |
| State / time | Release candidate. |
| 1.1 cell | Integrity of release decision. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| HIGH mapped+fixed | ship | allow |
| HIGH unmapped | ship | deny |
| HIGH accepted E6 | ship | allow-audited |
| info finding | ship | policy |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/9.4/9.4-lab` file `sast.py`.

## Transfer

SCA CVE vs actually called function.

## Residual risk

Blind spots (authz logic) — 9.2/9.3.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
