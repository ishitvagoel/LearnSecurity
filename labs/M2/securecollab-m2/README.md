# M2 — SecureCollab delayed work and retained exports

**Milestone:** M2  
**Authorized scope:** this directory only. Local synthetic data.  
**Purpose:** extend M1 into a persistent queue and worker path, then test authority again after time and revocation.  
**Status:** dependency-free teaching bridge; this is not production assurance.

The fixture stores requests, jobs, and generated exports in SQLite. A worker runs after the HTTP-like enqueue operation has finished. The fixed policy re-resolves current account state and the note's company at execution time; it does not treat a queued label as authority.

## The property

> A delayed export must be denied when the subject is no longer active or no longer belongs to the note's company. A retained export must be readable only through a current, same-company session.

This makes the time boundary visible: an allow decision at enqueue is not a permanent grant at execution. The `worker-sc` name is a synthetic service identity for this bridge, not proof of a production workload identity.

## Run the local bridge

From this directory, using Python 3.11+:

```text
python fixed/smoke.py
```

The smoke script runs one allowed export, then enqueues another, revokes Alice before the worker runs, and checks that no export is produced and the retained-copy read is denied.

## Break and verify

The vulnerable implementation trusts a client-supplied tenant label at enqueue and does not re-check current membership at worker time. The fixed implementation checks the session and object relation at enqueue, stores only the subject and object identifiers, and checks current state again before writing the export.

```text
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

The vulnerable run must fail the forged-tenant and revocation-after-enqueue assertions. The fixed run must pass. A setup failure is not evidence that a delayed authorization property holds.

## Evidence to keep

- enqueue and worker traces with session values redacted;
- one allowed export and one cross-company denial;
- a revocation-after-enqueue denial with no retained body written;
- a retained-copy access denial after session revocation;
- one residual note covering broker authentication, retry/idempotency, PostgreSQL roles, backups, and production observability.

Reset by stopping the script and deleting any database file named by `SECURECOLLAB_DB`. The default database is in memory. Do not add real identities, credentials, or network targets.
