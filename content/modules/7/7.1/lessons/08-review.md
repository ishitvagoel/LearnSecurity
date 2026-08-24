# 7.1 — API contracts, protocols, and inventory (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.

## Property (start here)

Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).

## Attacker capabilities and trust assumptions

- **Attacker:** Authenticated member sending extra JSON keys.
- **Trust:** Local apply(user, patch).
Review `labs/7.1/7.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/7.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): user.__dict__.update(body)
- Seeded smell (label it yourself): Undocumented route not in inventory
- Seeded smell (label it yourself): No is_admin test
- Seeded smell (label it yourself): OpenAPI not generated from code

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- If it’s not in Swagger it cannot be called
- GraphQL is self-documenting therefore safe
- Versioning is a security control

## Practice

Write three review notes. Do not open the keys file.

## Transfer

GraphQL mutation arguments; gRPC unknown fields.
