# 5.5 — Database and persistence security (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).

## Property (start here)

fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.

## Attacker capabilities and trust assumptions

- **Attacker:** Member who types a note id with SQL metacharacters; stolen app role (3.3).
- **Trust:** Local query object. Real DB roles in 3.3.
**Mechanism (not the property):** SQLAlchemy text() with f-strings is still concat. ORM defaults can still interpolate.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 5.5 |
|---|---|
| Root cause | Data and program mixed in one string. |
| Preconditions | fetch_sql returns a concatenated str. |
| Impact (1.1 cell) | Confidentiality/integrity of rows via interpreter confusion. — Interpreter reads other tenants / mutates rows. |
| Prevention | Parameters; identifier allow-lists for ORDER BY. |
| Detection | SQL error anomalies; WAF is not the property. |
| Recovery | Rotate DB creds; restore if mutated. |

## Framework defaults vs application guarantees

SQLAlchemy text() with f-strings is still concat. ORM defaults can still interpolate.

## Mechanism limits and bypasses

Bound ids plus missing 1.2 still leak via legitimate queries.

Identifier injection in ORDER BY; COPY; search DSL.

## Residual risk

DB superuser tools; replicas.

## Practice

Show bound vs concat for the lab payload *as data*, not as a weaponized cookbook.

Run `labs/5.5/5.5-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

NoSQL operators, GraphQL args (7.1).

Clinic search box.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
