# 1.2-LO-04 — Build a trusted decision path and mediate every operation

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** Saltzer and Schroeder fail-safe defaults, complete mediation, separation of privilege, least privilege, economy of mechanism, and open design (1975, seminal); OWASP ASVS 5.0.0 `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.2.3`, `v5.0.0-8.3.1`, `v5.0.0-8.3.2`, `v5.0.0-8.3.3`, and `v5.0.0-8.4.1`.

## What is the smallest mechanism that restores the authority invariant?

The answer is not “install an authorization library.” The smallest trustworthy design has two connected responsibilities:

1. a **policy decision point** resolves current trusted facts and returns a positive or negative decision for one subject–action–object request;
2. an **enforcement point** prevents the protected effect unless that decision allows it.

The policy can be logically centralized without becoming one physical service. The enforcement can be near the service operation, query, database, or protected subsystem. The architecture is correct only when the policy meaning is consistent and no in-scope effect bypasses enforcement.

## Start from the forbidden effect

For a cross-tenant note read:

```text
forbidden: a Tenant B subject receives bytes derived from a Tenant A note body
```

The root cause in the lab is ambient authentication without an object rule. The relevant state is current membership and stored note tenant. The smallest positive rule is:

```text
allow note:read-body only if
  subject is an active member
  AND subject.tenant_id == note.tenant_id
  AND note is in a readable lifecycle state
```

Unknown subject, missing note, unreadable state, policy error, and tenant mismatch do not satisfy the rule. They deny. Whether the response distinguishes “missing” from “forbidden” is a separate disclosure and usability decision; it does not change the internal authority result.

## Resolve authority attributes on the trusted side

The client may submit a note identifier. It must not choose the facts that justify authority.

| Attribute | Untrusted candidate | Trusted source for this model |
|---|---|---|
| subject ID | display name, request body user ID | verified identity context |
| active membership | hidden UI role, token claim with no freshness contract | current server-side membership state |
| tenant scope | `X-Tenant` or form value | membership relationship resolved by policy path |
| object tenant | client JSON or route prefix | stored note record or independently enforced database relation |
| action | caller’s claim that this is “read” | operation chosen by trusted server code |
| policy version | browser bundle version | deployed policy decision component |
| time | client clock | trusted service time within recorded assumptions |

Signed data is not automatically trusted for every purpose. A signed stale role claim may be authentic evidence of what an issuer said earlier while still being insufficient evidence of current authority.

## Make the decision explicit

A small decision record can contain:

```text
allowed: false
reason: tenant_mismatch
subject_id: bob
action: note:read-body
object_id: nA1
authority_version: membership-v7
policy_version: authority-phase1-v2
decided_at: trusted timestamp
```

The record should not contain the note body, session token, password, or unnecessary contact data. Its reason is stable enough for tests and operations but not so detailed in a public response that it reveals protected state.

Returning a decision object is not the security boundary by itself. The operation must consume it before release or mutation:

```text
subject = resolve_current_subject(identity_context)
note = repository.lookup_note(note_id)
decision = policy.decide(subject, "note:read-body", note, now)
if not decision.allowed:
    return safe_denial(decision)
return project_allowed_fields(note)
```

The order matters. Do not serialize the note, enqueue work, or mutate state and then consult the decision.

## Treat roles as scoped inputs, not bypasses

For `membership:revoke`, an active Tenant A admin may revoke an ordinary A membership under the current design. The policy still evaluates:

- admin subject and active status;
- exact action;
- target membership object;
- subject tenant equals target tenant;
- self-revocation or last-admin rules if the product defines them;
- current state and policy version.

Avoid a top-level branch such as `if subject.is_admin: allow`. That discards object, action, tenant, and state—the dimensions that made the role meaningful.

## Design delegation as a constrained authority transformation

When delegation enters scope, validate both issue time and use time.

At issue time:

- the issuer currently holds a delegable form of the requested authority;
- requested action/object scope is no broader than the issuer’s grant;
- expiry, audience, onward-delegation, and use constraints are explicit;
- the grant is attributable and revocable under the stated model.

At use time:

- the grant is authentic or otherwise unforgeable under its mechanism;
- presenter/audience and requested effect match the grant;
- the grant is active, unexpired, and not revoked;
- policy says whether issuer revocation or object-state change invalidates it;
- the enforcement point consumes the decision before the effect.

This is **attenuation**: delegated authority narrows rather than expands. A bearer capability may intentionally let any holder exercise the scope. An identity-bound delegation may require a particular grantee. Record the choice instead of mixing the models.

## Use separation of privilege only where the property justifies it

For the lab’s high-impact export case, the design requires two distinct current tenant administrators within a bounded approval window. The mechanism must reject:

- the same approver counted twice;
- an inactive or revoked approver;
- an approver from another tenant;
- approval for a different action, object set, artifact, or time window;
- execution after approval expires or is revoked.

Two approvals that share the same compromised identity provider, device, or operator may still have correlated failure. Record what independence you actually obtain and the remaining common mechanisms.

## Complete mediation needs an enforcement inventory

Centralizing policy logic reduces inconsistent rules, but it cannot guard a path that never calls it. Inventory effects, not just routes.

| Effect | Possible path | Enforcement point | Failure mode to test |
|---|---|---|---|
| Note body release | direct read | service/query before projection | tenant mismatch or policy outage |
| Note summary release | list/search | tenant-bound query and field projection | filter after serialization |
| Note deletion | user or admin mutation | policy plus atomic persistence transition | global admin or stale membership |
| Bulk export | request and later generation | approval check at execution, not only request | approval expires before use |
| Restored data visibility | restore/reconciliation | lifecycle and authority re-evaluation before reopening | old ACL or membership returns |
| Cached response | cache hit | cache key and authorization semantics | decision/result reused across tenant or revocation |

If a worker acts later, ASVS `v5.0.0-8.3.3` provides an advanced anchor: permission should reflect the originating subject rather than silently widening to an intermediary service’s ambient authority. Sometimes a service genuinely has independent authority; document and constrain that case instead of calling it “system.”

## Authority caches are new mechanisms with new limits

Caching a decision can improve latency and availability but changes the time model. Record:

- cache key: subject, action, object, relevant context, authority/policy version;
- maximum age and which actions may be cached;
- invalidation on membership, grant, object, or policy change;
- fail behavior when current state cannot be resolved;
- information-disclosure consequence during a stale window;
- evidence that indicates a cached versus fresh decision.

Immediate revocation may be required for some actions. For others, a bounded stale window plus detection may be accepted. That is a risk decision, not an invisible framework default. Disclosure during the window cannot be “reverted,” so compensating controls have limits.

## Reject plausible but insufficient repairs

| Proposed repair | Why it does not restore the invariant |
|---|---|
| Block Bob’s user ID | New users and tenants remain over-authorized |
| Make note IDs random | Guessing becomes harder; intended tenant authority is unchanged |
| Hide admin buttons | Hostile clients can call the operation directly |
| Add authentication middleware | Identity is resolved; object/action authority is still absent |
| Put `authorize()` in a shared library | Uninventoried paths can bypass it; wrong inputs can still be trusted |
| Return 404 on every denial | Response uniformity does not prevent an internal forbidden effect |
| Log all request bodies | Creates a confidentiality/privacy failure and does not prevent access |
| Add a second approval field | It may contain the same person twice or lack scope, freshness, and independence |

## Design record practice

Choose one SecureCollab effect—note-body read, membership revoke, or modeled bulk export—and produce:

1. invariant and forbidden effect;
2. subject, action, object, state, grant, trusted context, and time;
3. root cause and preconditions of the failed design;
4. smallest policy rule;
5. trusted attribute sources;
6. every in-scope enforcement point;
7. two rejected alternatives and their limits;
8. normal, negative, abuse, and failure proof obligations;
9. revocation and policy-outage behavior;
10. privacy-safe evidence, recovery, residual risk, and review trigger.

A peer should remove the policy call mentally from one path. Your design is ready for LO-05 only if you can name which test fails and which forbidden effect becomes possible.

## Transfer

A background export worker runs with a database credential able to read all notes. Shrinking that credential may help least privilege, but the application still needs to decide whether the worker acts under the requesting member, a tenant-approved export grant, or independent service authority. State which model you choose, how it is bound to the job, when it expires, and what happens if authority changes before execution.
