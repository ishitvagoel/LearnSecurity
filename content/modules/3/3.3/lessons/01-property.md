# 3.3 — Secure architecture patterns (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).

## Property (start here)

The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.

## Attacker capabilities and trust assumptions

- **Attacker:** Buggy handler; SQLi later (5.5/6.1); stolen app credentials.
- **Trust:** PostgreSQL RLS/role in the lab stand-in. The app still must mediate.
**Mechanism (not the property):** SQLAlchemy session is not a tenant scope.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 3.3 |
|---|---|
| Root cause | One omnipotent DB user shared by app and migrate. |
| Preconditions | app role can_select other tenant. |
| Impact (1.1 cell) | Confidentiality defense-in-depth. — Forgot WHERE becomes a breach. |
| Prevention | Least-privilege role; RLS as extra layer (5.5). |
| Detection | pg_audit on cross-tenant seqscans. |
| Recovery | Rotate DB password; review grants. |

## Framework defaults vs application guarantees

SQLAlchemy session is not a tenant scope.

## Mechanism limits and bypasses

RLS bypassed by table owners and SECURITY DEFINER (E5).

Connection pooler user; analytics replica without RLS.

## Residual risk

Stolen migrator role — separate credential, shorter life.

## Practice

Draw app vs migrator vs analyst roles.

Run `labs/3.3/3.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Serverless function with a shared “admin” connection string.

Clinic: billing replica.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
