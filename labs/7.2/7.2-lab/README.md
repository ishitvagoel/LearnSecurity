# Lab 7.2 — identifiers locate; they do not authorize fields

**Module:** `7.2`
**Authorized scope:** this directory only. Local course fixture. No public GraphQL.
**Invariant:** `resolve("member", "secret_internal")` is false. Honest `display_name` may be true.
**Root cause class:** serializer/resolver dumps without a role × field matrix
**Non-goals:** live targets, real PII, UUID-as-capability cookbooks.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/7.2/7.2-lab`, then run `git restore --source=HEAD -- labs/7.2/7.2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`resolve` returns true for every pair. Forbidden outcome: member resolves `secret_internal`.

## Structural fix

`secret_internal` resolves only when `role == "service"`. Other fields may resolve for members.

## Verify

```
python3 -m pytest labs/7.2/7.2-lab/tests --impl vulnerable
python3 -m pytest labs/7.2/7.2-lab/tests --impl fixed
```

The first command must fail on member × `secret_internal`. The second must pass. Honest `display_name` may pass on both.

## Operate

Signal: `field_denied`. Do not log the field value.

## Transfer

Clinic SSN. Prompt only. Use synthetic field names.
