# SecureCollab Phase 1 — authorization and tenant isolation

Design stub for Module 4.4. Not a production policy engine.

## Freeze

- Local `NOTES` / `USERS` / `GRANTS` maps. Synthetic `alice`, `bob`, `carol`, `eve`.
- Tenants `acme` and `clinic`. Notes `n1`, `n2` (acme), `n3` (clinic).
- No live IdP, no PostgreSQL RLS (that is 5.5), no worker identity (7.4).

## Two keys, then a grant

`can_read` is `(subject, tenant, note_id)`. A share of `n1` is not a share of `n2`. An `admin` role in `clinic` is not a grant on `acme` notes. 1.2 named the cells; this module executes them. 3.3 adds a DB-role second mediation; it does not replace this table.

## Tests

`can_read("bob", "n2")` false, `can_read("alice", "n3")` false, `can_read("eve", "n1")` false. Owner and honest-grant paths remain true. Search, export, GraphQL, and workers are named holes until those modules.
