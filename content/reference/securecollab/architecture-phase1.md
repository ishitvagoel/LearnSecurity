# SecureCollab Phase 1 — architecture planes

Design stub for Module 3.3. Not a production cluster.

## Freeze

- Local `can_select` / `runtime_connection_role` fixture. Synthetic tenants `tA` / `tB`.
- No live PostgreSQL.

## Two mediations

1.2 still checks the handler. The runtime `app` role must not SELECT another tenant if that check is skipped. Migrator and `postgres` are not request-time users.

## Rejected alternative

One superuser `DATABASE_URL` for migrate and serve.

## Tests

`can_select("app", "tB", "tA") is False` is the evidence. A microservice diagram is not.
