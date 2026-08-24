# 5.5 — Database and persistence security (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).

## Property (start here)

fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.

## Attacker capabilities and trust assumptions

- **Attacker:** Member who types a note id with SQL metacharacters; stolen app role (3.3).
- **Trust:** Local query object. Real DB roles in 3.3.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | app, postgres parser, attacker input |
| Objects | SQL text vs bound params |
| Actions | fetch_sql, is_bound |
| Channels | SQL session |
| TCB | Bound API (psycopg parameters). |
| Untrusted | note_id, sort columns, search q |
| State / time | One request; also migrations (residual). |
| 1.1 cell | Confidentiality/integrity of rows via interpreter confusion. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| app | tenant param | query | bound |
| attacker | id field | as-SQL | deny |
| migrator | ddl | run | offline-role |
| analyst | bodies | SELECT | 3.3 |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/5.5/5.5-lab` file `query.py`.

## Transfer

NoSQL operators, GraphQL args (7.1).

## Residual risk

DB superuser tools; replicas.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
