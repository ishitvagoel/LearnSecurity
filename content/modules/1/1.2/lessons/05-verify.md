# 1.2-LO-05 — Matrix cells as forbidden-outcome tests

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 (final) — verification is evidence of a requirement, not a scanner score.

## Property (start here)

Each **deny** cell has a test that would fail if the cell were allow.

## Attacker capabilities and trust assumptions

Tests run on the local fixture. They are not permission to scan the internet.

## Evidence

| Cell | Test idea | Vulnerable | Fixed |
|---|---|---|---|
| bob × n1 × read deny | `test_cross_tenant_read_is_denied` | fails | passes |
| alice × n1 × read allow | `test_same_tenant_member_can_read` | passes | passes |
| unknown note deny | `test_unknown_note_denies` | passes if coded | passes |

Happy path alone is not evidence. Abuse (cross-tenant) and failure (missing id) are required.

## Practice

Add one more deny cell in notes (e.g. unauthenticated) and say whether the lab already covers it.

## Transfer

List action vs read-body: a test that only checks `read_note` does not prove `list_notes` is mediated.
