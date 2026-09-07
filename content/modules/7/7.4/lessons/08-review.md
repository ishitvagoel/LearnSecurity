# Would you merge this inherited request context?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Review `labs/7.4/7.4-lab/vulnerable/` as a change to notes-app overnight export. Check whether `exporter({"user_session": "alice", "service": None})` still returns `"alice"`.

You already ran `test_user_session_is_not_worker_identity` — that is the rule. A comment “will bind service later” is not.

## Picture: user_session or service fallback / copy request cookies into the job

**`user_session or service` fallback / copy request cookies into the job**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|alice session is principal| Property["Rule - good if tested"]
  Q -->|VPC queue| Mechanism[Tool - network]
  Q -->|zero trust dashboard| False[False assurance]
```

Alice's session still yields `None`. If the change never checks `service == "worker-sc"`, that confused-deputy path is still open. A private network without that check is still the same problem.

A god-mode `DATABASE_URL` (3.3) and retry after revoke (2.4) are other worker holes — name them, do not skip `test_user_session_is_not_worker_identity`.

## Problems to find (name them yourself)

- `user_session or service` fallback / copy request cookies into the job
- Worker uses a superuser `DATABASE_URL`
- No test that leftover session is rejected
- Retry duplicates after revoke (2.4)

Also reject: live broker attacks; closing findings without re-running `test_user_session_is_not_worker_identity`; keys in learner notes; real session cookies in practice files.

## Common mix-ups

- Internal queue is trusted input
- Async means no authz
- Service account should be superuser just for jobs
- Zero trust as a product replaces worker identity tests
- A zero-trust architecture paper is the check

## Use it somewhere new

Clinic change that “runs on the hospital VLAN with zero trust” without a leftover-session deny test is an incomplete review of inherited request context. Name the independent falsehood that would still keep Alice session `None`.

## What this page is not doing

Do not merge by adding a comment “will bind service later.” That comment is leftover without an owner. Do not attach to a live broker to prove the finding.
