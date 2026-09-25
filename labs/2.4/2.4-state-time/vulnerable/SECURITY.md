# Vulnerable — do not deploy

This FastAPI app is an intentionally broken local fixture for module `2.4`.
It has no idempotency check (a retry duplicates the share) and fails open on
any storage error (it reports success without having recorded anything).
Run it only under `pytest --impl vulnerable` inside
`labs/2.4/2.4-state-time/`. It stores data in a throwaway temp SQLite file
created by `reset()` and is not reachable over a network. Do not copy this
pattern, do not point it at real data, and do not run it outside this
directory.
