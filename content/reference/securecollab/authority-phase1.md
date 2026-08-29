# SecureCollab — Phase 1 authority model

**Owner:** Module 1.2
**State:** design reference plus isolated local policy evidence; not web, database, or production assurance
**Version:** 2, 2026-08-25
**Depends on:** Module 1.1 invariant catalogue version 1

This artifact defines the Phase 1 relation between subjects, objects, actions, grants, state, and time. Later SecureCollab slices must preserve or explicitly revise it. The executable Module 1.2 fixture tests selected in-memory operations; it does not prove that a future FastAPI, PostgreSQL, worker, cache, or mobile path enforces the model.

## Authority invariant

Every in-scope security-relevant effect must have a current positive rule over a server-resolved subject, action, object, authority state, and time. Every path that can cause the effect must enforce that rule before release or mutation. Missing or unknown authority denies.

Authentication identifies a principal under stated assumptions. It does not grant note, membership, tenant, export, or evidence authority.

The conceptual decision is:

```text
policy(originating_subject, effective_subject, action, object,
       object_state, grant, trusted_context, time) -> allow | deny
```

The decision records a stable reason, policy version, and authority version without copying protected content.

## Product scope

### Included in the Phase 1 model

- tenants and active/inactive tenant membership;
- tenant members and tenant-scoped administrators;
- text-note identifier, summary metadata, body, tenant binding, and lifecycle state;
- membership records;
- privacy-safe authority decision evidence;
- direct read, aggregate list, note delete, membership administration, and an illustrative high-impact tenant export decision.

The export is a design case for separation of privilege, not a shipped product feature.

### Deferred and authority-reviewing

- files, sharing links, public resources, and external collaborators;
- support impersonation, break-glass operations, and customer support roles;
- background workers, queues, webhooks, caches, search indexes, retries, and bulk processing;
- self-contained grants, cryptographic capabilities, and service-to-service policy;
- database roles, row security, cloud administrators, backups, and restore enforcement;
- mobile/offline authority and device copies;
- production deployment, real PII, real payments, and compliance evidence.

Deferred means previous evidence does not cover the feature. It does not mean the feature is safe by default.

## Subjects and authority attributes

| Subject | Current authority source | Trusted attributes | Explicit limit |
|---|---|---|---|
| Unauthenticated requester | none | none | no note or membership authority |
| Active tenant member | verified principal plus current server-side membership | subject ID, active state, tenant, authority version | member actions inside one tenant only |
| Revoked former member | identity may still authenticate | current inactive membership | no member authority; session identity is insufficient |
| Tenant administrator | active tenant membership plus scoped admin role | subject ID, tenant, role, active state, authority version | administrative actions only for the bound tenant and action |
| API policy path | deployed product policy | policy version, trusted subject/object resolvers, trusted time within scope | decides only modeled operations; availability/common-mode risk remains |
| Operation enforcement point | decision consumed before effect | operation-selected action, protected object, decision result | cannot invent or widen policy |

The browser, Next.js client, request identifiers, tenant/role labels, hidden controls, and client clock are untrusted. A future worker or support actor must be added as an originating/effective subject pair rather than called “system.”

## Objects and actions

| Object | Distinct protected views or states | Actions in scope |
|---|---|---|
| Note | identifier, title/summary, body, tenant, active/deleted state | list-summary, read-body, create, update, delete |
| Membership | subject, tenant, role, active/suspended/revoked state, authority version | view, grant, revoke |
| Tenant | identity and modeled export scope | view, approve-export, execute-export design decision |
| Authority event | decision metadata, access and retention state | append, view, export, retain/delete |

Summary and body are separate because a permitted list result need not authorize body release. URL and function names are paths, not actions; any path producing the same effect inherits the same policy meaning.

## Access matrix — required core cells

| Subject | Object | Action | Required state / grant | Decision | Primary evidence |
|---|---|---|---|---|---|
| Active member A | Note A body | read | current A membership; stored note tenant A | allow | normal read plus safe decision event |
| Active member B | Note A body | read | no A grant | deny | cross-tenant body remains absent |
| Revoked former A member | Note A body | read | membership inactive even if identity authenticates | deny | revoked-state negative test |
| Active member A | A note summaries | list | current A membership | allow | only A identifiers/titles returned |
| Active member A | B note summaries | list | no B authority | deny | aggregate result contains no B object |
| Active member A | Note A | delete | ordinary member role | deny | no mutation or side effect |
| Admin A | Note A | delete | current scoped A admin | allow | one intended deletion and event |
| Admin A | Note B | delete | admin scope is A, not global | deny | B state unchanged |
| Admin A | Membership A | grant/revoke | current A admin and applicable target-state rule | allow | authorized transition and event |
| Admin A | Membership B | grant/revoke | no B authority | deny | no cross-tenant membership change |
| One A admin | Tenant A export decision | approve/execute | documented two-person exercise rule unsatisfied | deny | insufficient-approval test |
| Two distinct current A admins | Tenant A export decision | approve/execute | same target tenant/action and active approvals | allow in the modeled case | normal distinct-approval test |
| Duplicate, retired, or B approver | Tenant A export decision | approve | independence/scope/current state absent | deny | abuse tests |
| Any active subject | Unknown action or object | any | no positive rule | deny | fail-safe failure test |
| Unauthenticated/unknown subject | Any protected object | any | no authority source | deny | identity-negative test |

Cells not yet implemented remain design requirements, not evidence claims. The local fixture executes read, list, delete, export-decision, revoked, unknown-subject/object, and unknown-action cases.

## Delegation contract

No delegated sharing feature exists in Phase 1. A future grant must record:

- issuer and the delegable authority they currently hold;
- grantee or intentional bearer semantics;
- exact action and object/object-set scope;
- audience, purpose, and onward-delegation constraints where enforced;
- issue time, expiry, revocation state/version, and maximum stale window;
- use-time authenticity, current state, and policy checks;
- privacy-safe issue/use/revoke evidence;
- copyability, leakage, offline use, and recovery limits.

Delegated authority must attenuate rather than exceed the issuer’s justified authority. A random identifier or signed token is not by itself this contract.

## Authority lifecycle

Minimum membership states:

```text
invited -> active -> suspended -> revoked
                 \-> expired
```

Each transition identifies who can cause it, the new authority version, effect time, evidence, failure behavior, and recovery. Authentication sessions, caches, self-contained claims, grants, queued jobs, offline copies, database roles, and restored state become separate authority copies when introduced. Removing one role record does not prove every copy stopped authorizing.

For information release, later revocation cannot recover already disclosed content. Any accepted stale window therefore remains a confidentiality limit, not merely an operational inconvenience.

## Authority and enforcement map

```text
verified identity ----+
current membership ---+                         +--> direct body read
scoped role ----------+--> policy decision ----+--> aggregate summary list
stored object state --+                         +--> note/membership mutation
grant/approval -------+                         +--> modeled export decision
trusted time ---------+
```

Current/local enforcement evidence:

| Effect | Enforcement evidence now | Gap / later owner |
|---|---|---|
| Note-body read | Module 1.2 fixed in-memory operation consumes explicit decision | FastAPI/DB/session integration: 4.3–4.4, 5.5 |
| Summary list | Fixed operation filters by server-resolved tenant and projects allowed fields | search/cache/GraphQL/export: 2.2, 4.4, 7.2 |
| Note delete | Fixed operation preserves tenant/action scope before mutation | transaction/concurrency/persistence: 2.4, 4.4, 5.5 |
| Membership transition | matrix and lifecycle design only | executable identity/authorization slice: 4.1, 4.4 |
| High-impact export | fixed decision tests distinct current scoped approvals only | job, data, expiry, execution, evidence: 5.1, 7.4, 10.5 |
| Restore visibility | design review trigger only | data lifecycle and recovery: 5.1, 5.5, 10.5 |

A central policy library is not enforcement proof. Every route, query, cache, worker, retry, restore, and maintenance path must appear in this inventory when it enters the product.

## Operational evidence

Authority events may include schema/policy versions, originating and effective subject IDs, tenant/authority domain, action, safe object ID/class, grant or authority version, decision/reason, enforcement point, trusted time, correlation ID, and fresh/cached/emergency/delegated mode.

They exclude note bodies, passwords, cookies, tokens, capability material, raw authorization headers, arbitrary request bodies, and unnecessary contact data.

Required operational behaviors:

- unknown/policy-resolution failure denies and raises an independent health signal;
- repeated tenant mismatch, cross-tenant admin attempts, stale allows, approval anomalies, and event gaps have owned signals;
- containment revokes the narrow subject/grant/path rather than destroying every tenant’s availability by default;
- recovery scopes alternate paths, repairs policy or enforcement root cause, reconciles state/outputs, and reruns four-mode evidence;
- grant, approval, revocation, and break-glass interfaces expose scope, effect, duration, and completion through keyboard-accessible, non-color-only interaction;
- one operator controlling protected state, policy, revocation, and the only evidence store remains residual risk.

## Standards trace

- Saltzer and Schroeder: fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability, and compromise recording.
- ASVS 5.0.0: `v5.0.0-8.1.1`, `v5.0.0-8.1.2`, `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.2.3`, `v5.0.0-8.3.1`, `v5.0.0-8.3.2`, `v5.0.0-8.3.3`, `v5.0.0-8.4.1`, and `v5.0.0-15.3.1` with Level 3 applicability kept explicit.
- CISA Secure by Design: secure defaults/manufacturer-ownership snapshot only; canonical page was unavailable at the 2026-08-25 check and the pin is `unverified`.

No ASVS compliance or implementation assurance is claimed.

## Spiral deltas and required retests

This version makes these assumptions explicit:

- SC-CONF-01 now depends on same-tenant policy at both direct body and aggregate summary enforcement points.
- SC-INTEG-01 now distinguishes scoped administration, current authority state, and high-impact independent conditions.
- SC-ACCT-01 gains policy/authority versions, decision mode, and originating/effective subject requirements.
- SC-AVAIL-01 must use the server-resolved authority domain for future work accounting; client tenant labels remain untrusted.
- SC-PRIV-01 constrains authority evidence and field projections.

Revisit or retest:

- Module 1.1 catalogue rows and mechanism limits against this narrower authority model;
- Module 1.3 boundaries for every policy and enforcement point;
- Module 2.4 for check/use time, retry, cache, and partial failure;
- Module 4.3 for sessions and revocation copies;
- Module 4.4 for executable authorization and tenant isolation;
- Module 5.5 for database roles, row policies, transactions, and restore;
- Modules 7.2/7.4 for API fields, originating authority, workers, and retries;
- M1 and every later milestone after new identities or paths exist.

## Review triggers

Reopen this artifact for any new principal, role, delegation, capability, object field/state, action, route, query, cache, queue, worker, retry, import, export, restore, maintenance tool, policy store, token, database role, emergency path, evidence sink, or revocation objective.

## Honest limits

- The local lab does not implement FastAPI, PostgreSQL, cryptographic capabilities, sessions, workers, caches, transactions, or production identities.
- The two-approver export rule is illustrative and does not establish a universal control.
- Policy availability and centralization create common-mode and denial-of-service risks not measured here.
- Direct database/cloud administrator access and independent evidence durability remain later concerns.
- No Gate, milestone, ASVS baseline, compliance result, or public deployment is complete because this document exists.
