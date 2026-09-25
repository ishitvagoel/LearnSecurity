# Fixed — still a local fixture

This variant enforces the idempotency key with a database-level `UNIQUE`
constraint and fails closed when the store cannot be reached. It is a
teaching fixture, not a production idempotency service: it has no
authentication, no TLS, and no production-grade connection pooling. Run it
only under `pytest --impl fixed` inside `labs/2.4/2.4-state-time/`.
