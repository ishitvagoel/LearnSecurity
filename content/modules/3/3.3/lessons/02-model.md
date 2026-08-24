# 3.3 — Secure architecture patterns (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).

## Property (start here)

The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.

## Attacker capabilities and trust assumptions

- **Attacker:** Buggy handler; SQLi later (5.5/6.1); stolen app credentials.
- **Trust:** PostgreSQL RLS/role in the lab stand-in. The app still must mediate.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | app role, migrator role, superuser |
| Objects | notes table rows by tenant |
| Actions | can_select |
| Channels | SQL session |
| TCB | Role grants + optional RLS; migrator not used at runtime. |
| Untrusted | ORM default connection user |
| State / time | Migration-time SUPERUSER leftover in DATABASE_URL. |
| 1.1 cell | Confidentiality defense-in-depth. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| app | own tenant rows | SELECT | allow |
| app | other tenant rows | SELECT | deny |
| migrator | ddl | ALTER | allow-offline |
| analyst | bodies | SELECT | deny-or-tokenize |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/3.3/3.3-lab` file `roles.py`.

## Transfer

Serverless function with a shared “admin” connection string.

## Residual risk

Stolen migrator role — separate credential, shorter life.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
