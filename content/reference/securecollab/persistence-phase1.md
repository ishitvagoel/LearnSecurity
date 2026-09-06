# SecureCollab Phase 1 — persistence queries

Design stub for Module 5.5. Not a production database.

## Freeze

- Local `fetch_sql(tenant, note_id)` / `is_bound`.
- Synthetic tenants `tA`. No live PostgreSQL.

## Data, not grammar

Tenant and note id travel as a params tuple. Concatenated SQL is forbidden. RLS is extra, not the grant table (3.3 / 1.2).

## Tests

Bound tuple vs concatenated `str` is the evidence. An ORM brand is not.
