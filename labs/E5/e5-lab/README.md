# Lab E5 — the JSON body is not the tenant

**Module:** `E5`
**Authorized scope:** this directory only. Local course fixture. No public SaaS tenants.
**Invariant:** `tenant_for({"tenant": "A"}, {"tenant": "B"})` is `A`. Matching A/A may keep A.
**Root cause class:** client-chosen tenant (confused deputy of the isolation key)
**Non-goals:** Zanzibar product; Postgres RLS as 1.2; API Top 10 as the syllabus.

Postgres RLS that `SET`s tenant from the body is the **same bug**. This Python binding is a teaching stand-in.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/E5/e5-lab`, then run `git restore --source=HEAD -- labs/E5/e5-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`tenant_for` prefers `body["tenant"]`. Forbidden outcome: JSON body switches the bound tenant.

## Structural fix

Return `session["tenant"]`. Ignore the body field for isolation.

## Verify

```
python3 -m pytest labs/E5/e5-lab/tests --impl vulnerable
python3 -m pytest labs/E5/e5-lab/tests --impl fixed
```

The first command must fail `test_body_cannot_switch_tenant`. The second must pass. Honest matching-tenant tests may pass on both.

## Operate

Signal: `body_tenant_mismatch`. Do not log note bodies.

## Transfer

Clinic group practice `org_id` in JSON. Zanzibar tuple vs this binding. Prompt only.
