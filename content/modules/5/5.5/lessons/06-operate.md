# 5.5 — Database and persistence security (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).

## Property (start here)

fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.

## Attacker capabilities and trust assumptions

- **Attacker:** Member who types a note id with SQL metacharacters; stolen app role (3.3).
- **Trust:** Local query object. Real DB roles in 3.3.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | SQL error anomalies; WAF is not the property. |
| Signal (no bodies) | sql_error_spike; grant_drift (3.3). |
| Revoke / recover | Rotate DB creds; restore if mutated. |
| Residual | DB superuser tools; replicas. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/5.5/5.5-lab`.

## Transfer

NoSQL operators, GraphQL args (7.1).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
