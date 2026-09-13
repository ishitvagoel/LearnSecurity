# M0 — SecureCollab observable skeleton

**Milestone:** M0  
**Authorized scope:** this directory only. Local synthetic data.  
**Purpose:** trace one browser request through an HTTP API into a database and identify the trust boundary that protects tenant isolation.  
**Status:** teaching bridge; this is not production assurance and does not complete Gate 2 or M0 by itself.

The canonical implementation target remains FastAPI + PostgreSQL + TypeScript/Next.js. This dependency-free fixture makes the first request/state path observable while those production dependencies are introduced in later milestone work.

## The property

Alice's note belongs to Company A. Bob belongs to Company B. A valid request from Bob must not receive Alice's note body, even when the browser changes a company label or note identifier.

The fixture has four visible stages:

```text
browser/index.html → local HTTP server → request adapter/policy → SQLite notes table
```

The `X-Demo-Actor` header is a synthetic harness input, not real authentication. The fixed policy resolves that actor through a server-side fixture map and ignores the browser's company label. Identity, sessions, persistence roles, and production networking remain explicit later work.

## Run the local skeleton

From this directory, using Python 3.11+:

```text
python fixed/server.py
```

Open `http://127.0.0.1:8765/` and use the two buttons. Alice can read `n1`; Bob receives a denial. Stop with Ctrl-C. The server binds to loopback only and uses a temporary SQLite file unless `SECURECOLLAB_DB` is provided.

The equivalent local trace without a browser is:

```text
python -m fixed.smoke
```

## Break and verify

The vulnerable server trusts the client-supplied `company` query parameter. The fixed server derives the company from the synthetic actor map before querying SQLite.

```text
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

The vulnerable run must fail the cross-company denial assertion. The fixed run must pass Alice's allow and Bob's deny cases, including a forged client company. A test failure or a setup error is not a reason to contact a public host.

## What this milestone proves and leaves open

It proves that a learner can trace a request, identify the API/database boundary, and observe one tenant-isolation oracle in a local synthetic system. It does not prove authentication, PostgreSQL roles, encrypted backups, worker authority, cache invalidation, production deployment, or the full capstone portfolio. Those are M1–M5 changes and revisit triggers for the 1.1 catalogue.

Reset by stopping the server and deleting the temporary database. Do not add real names, credentials, network targets, or production data.
