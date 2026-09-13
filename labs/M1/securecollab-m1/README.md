# M1 — SecureCollab identity and current authority

**Milestone:** M1  
**Authorized scope:** this directory only. Local synthetic data.  
**Purpose:** make account, session, and object authorization state observable after the M0 request trace.  
**Status:** dependency-free teaching bridge; this is not production assurance.

The fixture uses a real local SQLite session store so the learner can follow an account from login to a note read and then through revocation. The `session` value is a disposable local token. It is not a production credential and must never be copied outside the lab.

## The property

An active session identifies a current person, but it does not grant every object. A server-side policy must check both current account state and the note's company on every read:

> A current member may read a note only when the note belongs to that member's company. Once the account is revoked, its old session must not read anything.

The browser-supplied company label is input, never authority. The worker and database-role questions remain later milestones.

## Run the local bridge

From this directory, using Python 3.11+:

```text
python fixed/smoke.py
```

The smoke script logs in Alice and Bob, checks an allowed read, checks a cross-company denial even when Bob forges a company label, and checks that Alice's session is denied after revocation.

## Break and verify

The vulnerable implementation trusts the company label and leaves sessions usable after account revocation. The fixed implementation resolves the session and account state on every request, then checks the note relation.

```text
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

The vulnerable run must fail the forged-company and revoked-session assertions. The fixed run must pass all cases. A setup failure is an environment problem, not evidence that the property holds.

## Evidence to keep

- login and session-lifecycle trace (token values redacted);
- Alice allow and Bob cross-company deny responses;
- forged client-company denial;
- revocation-after-login denial;
- one residual note explaining that this bridge does not prove production FastAPI behavior, PostgreSQL roles, refresh-token families, or device caches.

Reset by stopping the script and deleting any database file named by `SECURECOLLAB_DB`. The default database is in memory. Do not add real identities, credentials, or network targets.
