# 1.2-LO-01 — Authority is permission to cause a bounded effect

**Kind:** concept-model
**Loop step:** 1 Property
**Standards:** Saltzer and Schroeder (1975, seminal), especially fail-safe defaults, complete mediation, separation of privilege, and least privilege; OWASP ASVS 5.0.0 (final) `v5.0.0-8.1.1`, `v5.0.0-8.1.2`, `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, and `v5.0.0-8.2.3`.

## What must remain true?

For the SecureCollab Phase 1 model:

> A security-relevant effect on a note, membership, tenant, or authority record may occur only when a current, server-resolved rule positively grants the effective subject that exact action on that object in its current state. Missing or unknown authority denies.

The forbidden outcome is not merely “an unauthenticated request succeeds.” A perfectly authenticated Tenant B member must still be unable to read Tenant A’s note, a Tenant A administrator must not become administrator of Tenant B, and a revoked member must not keep acting merely because an old login session still identifies them.

That distinction is the center of this module. **Authentication supplies identity evidence. Authorization decides whether a particular effect is allowed.** Authentication can be correct while authorization is catastrophically wrong.

## Authority means the ability to cause an effect

Treat authority as a relation, not a badge:

```text
decision = policy(subject, action, object, state, grant, trusted_context, time)
```

- A **subject** is the principal whose authority is being evaluated: a person, service, worker, or delegated actor.
- An **action** is a security-relevant operation such as `read_body`, `list_summary`, `delete_note`, or `grant_membership`.
- An **object** is what receives or reveals the effect: a note body, note summary, membership row, tenant record, or export.
- **State** includes ownership, membership status, document lifecycle, prior approvals, revocation version, and other facts that change the decision.
- A **grant** explains where authority came from: ownership, membership, delegation, a capability, an approved emergency path, or another explicit policy fact.
- **Trusted context** contains attributes resolved by a trusted component. A tenant label supplied by the browser is data to validate, not authority.
- **Time** matters because a grant can begin, expire, be revoked, or become stale between check and use.

The tuple is a reasoning model, not a required function signature. A database policy, operating-system capability, application policy service, or relationship graph may represent it differently. The invariant remains the same.

## The access matrix is an abstract relation

Imagine a large table. Subjects are rows, objects are columns, and each cell contains allowed actions and conditions. This **access matrix** is the abstract authority model.

| Subject | Object | Action | Condition | Decision |
|---|---|---|---|---|
| Alice, active member of A | Note A-17 body | read | note belongs to A | allow |
| Bob, active member of B | Note A-17 body | read | no A membership or grant | deny |
| Admin A | Membership A-9 | revoke | admin remains active in A | allow |
| Admin A | Membership B-4 | revoke | admin role is not global | deny |

Real systems rarely store that literal table. They compress or distribute it.

### ACLs

An access-control list stores authority near an object: “these subjects or groups may perform these actions.” It is an object-centered representation of matrix cells. It raises questions about group expansion, inheritance, default entries, ownership, and revocation.

### Roles

A role groups many permissions so policy is easier to administer. “Tenant admin” might expand into membership-read, membership-grant, membership-revoke, and selected note actions. A role is a compression of cells, not a magical authority fact. If the tenant scope is lost, `role == admin` becomes ambient global authority.

### Relationship or attribute rules

A rule may say that a member can read notes whose `tenant_id` equals the member’s active tenant, or that an editor may update a draft but not a published record. These mechanisms calculate cells from trusted relationships, attributes, and state. If the attributes come from the requester, the apparent sophistication does not help.

### Capabilities

A capability is an unforgeable reference whose possession intentionally conveys a specified authority. A random note identifier is not automatically a capability. For possession to be the grant, the design must address unforgeability, scope, audience or bearer semantics, copyability, attenuation, expiry, revocation, and leakage.

Knowledge of `/notes/7f3...` is not permission if the product’s intended rule is tenant membership. Making the identifier harder to guess raises work factor; it does not change the authority relation.

## Delegation must attenuate authority

Delegation lets one subject authorize another to perform a bounded action. The grant should record at least:

- issuer and grantee;
- action and object or object set;
- constraints and intended audience;
- issue time and expiry;
- revocation state or version;
- whether further delegation is permitted;
- evidence needed at use time.

The delegate cannot legitimately receive more authority than the issuer can grant. If Alice can read Note A-17 but cannot delete it, a grant from Alice should not create delete authority. If Alice’s membership is revoked, the design must say whether existing grants also lose effect and within what time. “Share token exists” is a mechanism statement; the authority contract answers what the token means.

## Ambient authority is authority without an explicit grant for this action

Ambient authority comes from the surrounding environment rather than the request’s justified authority path. Common examples include:

- a global `current_user` treated as permission on every object;
- a process-wide database credential able to read every tenant;
- an unscoped `admin` boolean;
- a worker service account whose broad storage access substitutes for the originating user’s permission;
- a cached “allowed” decision reused after membership changes;
- a recovery shell that bypasses ordinary policy without independent conditions.

Ambient authority is attractive because it makes code convenient. It is dangerous because the authority is available to operations that never justified needing it. Least privilege asks whether the subject and mechanism can hold less. Complete mediation asks whether every effect is checked. Fail-safe defaults ask whether an omitted case becomes denial rather than permission.

## Derive principles from failures

The classic protection principles are not slogans to attach after design. Each responds to a failure shape.

| Failure shape | Derived principle | Design question |
|---|---|---|
| Unknown subject/action/object is allowed | Fail-safe defaults | What positive fact creates permission? |
| List, export, worker, retry, or restore bypasses the check | Complete mediation | Which enforcement point guards every in-scope effect? |
| Tenant admin acts on every tenant | Least privilege | Can authority be narrowed by tenant, action, object, state, and time? |
| One stolen credential performs a catastrophic export | Separation of privilege | Which independent conditions should be required, and are they truly independent? |
| The policy works only while attackers do not know it | Open design | Would publishing the rule make it fail? |
| Administrators cannot understand or revoke grants | Psychological acceptability | Is the secure administrative path understandable and usable under stress? |

Two button clicks by the same user are not separation of privilege. Two checks that depend on the same compromised identity may not be meaningfully independent. The principle asks whether one accident, deception, or breach is enough to cause the protected effect.

## Root cause, impact, and response are different

Consider Bob reading Alice’s note by choosing `nA1`.

- **Root cause:** the read path treats authenticated identity as object authority and omits the subject–object rule.
- **Preconditions:** Bob has a valid Tenant B identity; Note A-17 exists; Bob can choose an identifier.
- **Trigger:** the read operation reaches storage without a current positive decision for Bob × read-body × Note A-17.
- **Impact:** Tenant A note confidentiality fails. The identifier may also reveal note existence.
- **Prevention:** resolve subject and object server-side, evaluate the exact action, and enforce the decision before release.
- **Detection:** privacy-safe decision evidence may reveal repeated tenant-mismatch attempts.
- **Recovery:** revoke stolen authority if applicable, repair every affected path, remove exposed copies where possible, notify owners under the incident process, and retest.

Calling this “IDOR” or “BOLA” can help communicate a known weakness family later. It does not explain why the rule failed or which other paths share the same cause.

## Framework defaults versus application guarantees

FastAPI’s authentication dependency can reject an invalid credential. Next.js can hide an admin control. PostgreSQL can enforce row policies if they are correctly designed and used. None of those facts alone proves SecureCollab’s authority invariant.

The application guarantee must state:

- which identity and object attributes are trusted and where they are resolved;
- which policy rule covers the action;
- which enforcement points cannot be bypassed;
- what happens on unknown state and policy failure;
- how revocation becomes effective;
- which tests observe forbidden outcomes;
- which paths and administrators remain residual risk.

ASVS 5.0.0 provides exact verification requirements for documenting function/data/field rules and enforcing them. It is a verification backbone, not a substitute for the product-specific matrix.

## Guided practice: classify the claim

For each statement, label it **identity evidence**, **authority rule**, **representation/mechanism**, **ambient authority**, or **unsupported conclusion**. Then rewrite unsupported statements as a bounded cell.

1. “The request has a valid session cookie.”
2. “A current Tenant A member may read the body of a Tenant A note.”
3. “The route uses `Depends(get_current_user)`.”
4. “The worker uses the application database role, so its export is authorized.”
5. “The note ID is random, so anyone who has it may read.”
6. “Admin A may revoke active memberships in A, but not in B.”

Your rewrite is successful when another learner can identify subject, object, action, positive grant, state/time condition, forbidden outcome, and what must deny. If they must ask what “admin,” “has access,” or “secure” means, the cell is still underspecified.

## Transfer prompt

A future background job receives a signed message saying “export tenant A.” Do not decide from the signature alone. List the originating subject, effective worker subject, action, object set, source and scope of authority, issue/use time, revocation behavior, trusted context, and one mechanism limit. LO-07 will require this reasoning without the SecureCollab scaffolding.
