# Lab 7.2 — identifiers locate; they do not authorize fields

**Module:** `7.2`
**Authorized scope:** this directory only. Local course fixture. No public GraphQL.
**Invariant:** `resolve("member", "secret_internal")` is false. Honest `display_name` may be true.
**Root cause class:** serializer/resolver dumps without a role × field matrix
**Non-goals:** live targets, real PII, UUID-as-capability cookbooks.

## Reset

Re-run pytest. Optional: `git checkout -- labs/7.2/7.2-lab`.

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
