# Lab 3.3 — runtime role is not superuser

**Module:** `3.3`
**Authorized scope:** this directory only. Local course fixture. No public databases.
**Invariant:** The FastAPI runtime DB role must not `SELECT` another tenant’s rows even if a handler forgets `WHERE`. Architecture is a second mediation, not a substitute for 1.2.
**Root cause class:** trust / authority (omnipotent runtime user)
**Non-goals:** live RDS, real tenant data, weaponized SQL.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/3.3/3.3-lab`, then run `git restore --source=HEAD -- labs/3.3/3.3-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`can_select("app", "tB", "tA")` is true because the role has no tenant predicate. `runtime_connection_role()` is `postgres`. Forbidden outcome: app DB role can SELECT another tenant's rows.

## Structural fix

Runtime role is `app`. `can_select` denies unless `role == "app"` **and** `tenant == note_tenant`. Migrator cannot SELECT notes at runtime.

## Verify

```
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

From repo root:

```
python3 -m pytest labs/3.3/3.3-lab/tests --impl vulnerable
python3 -m pytest labs/3.3/3.3-lab/tests --impl fixed
```

The first command must fail. The second must pass.

## Operate

CI signal: `grant_drift` / `wrong_db_role` with the role name; never a note body. Rotate and rewrite `DATABASE_URL`.

## Transfer

Serverless shared admin string; clinic billing replica. Prompt only; do not leave this directory.
