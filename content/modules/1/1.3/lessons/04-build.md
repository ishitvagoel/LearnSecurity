# 1.3-LO-04 — Restore trusted provenance and bound the export blast radius

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** Saltzer and Schroeder’s fail-safe defaults, economy of mechanism, complete mediation, and least common mechanism; OWASP ASVS 5.0.0 `v5.0.0-15.3.4` for the analogous requirement that proxy-origin metadata used in security decisions come through trusted, non-user-manipulable fields. This lesson does not claim that ASVS prescribes the fixture’s Python design.

## Repair the assumption before adding checks

The vulnerable design asks an untrusted caller to state whether it is trusted. The first repair is not a longer list of accepted values. It is a change in where provenance originates.

The fixed local design uses two adapters:

```text
public input -> public adapter -> PublicContext -> public policy paths

server-held worker registry -> worker adapter -> WorkerContext
    -> scoped grant decision -> export effect
```

The public adapter can carry requester data, but it cannot construct worker caller kind or worker identity. The worker adapter receives a synthetic registered identity from server-held fixture state. This creates a meaningful in-process trust boundary for the exercise.

Be precise about the claim: a caller using the public function cannot become a worker by setting fields. This does **not** establish mutual TLS, workload certificates, deployment identity, queue authenticity, or resistance to a compromised process/operator. Those are named production design obligations and later-module work.

## Separate provenance, authority, and effect

Three questions must have three answers:

1. **Provenance:** what trusted mechanism establishes the effective caller kind and identity?
2. **Authority:** what current grant permits this caller to perform this action on this tenant and exact object set now?
3. **Effect:** which enforcement point ensures no output is constructed before both answers are positive?

A worker registry answers only the first. A capability or policy record answers the second. A wrapper that calls policy but then invokes an unguarded helper may fail the third.

Use an authority tuple:

```text
(worker_id, action, tenant_id, object_ids, issued_at, expires_at, use_state)
```

The tuple is a reasoning contract, not a mandate for token format. In the fixture, a server-held opaque grant identifier refers to this state. Production alternatives could include current server-side re-authorization, a cryptographically protected capability, or another bounded mechanism, but each must preserve the same product authority and lifecycle.

## Fail safely at every unknown

The fixed decision should deny when any of these is missing or inconsistent:

- caller context is absent or of the wrong kind;
- worker is unknown or no longer registered;
- grant is absent or belongs to another worker;
- action differs from the grant;
- requested tenant differs from the grant;
- requested object set differs from the grant;
- a requested object is missing or belongs to another tenant;
- grant is expired or already consumed;
- required evidence cannot be produced under the exercise’s high-impact policy.

This is fail-safe defaults applied to the decision surface. It is not enough to default one policy branch to deny if a different function performs the export directly. Complete mediation applies to every in-scope effect path.

## Bind exact object scope

Tenant scope alone can still be too broad. Suppose a job was approved to export summaries for `{A1, A2}`. A check that permits every Tenant A note converts an object-scoped grant into tenant-wide ambient authority.

The local exercise compares the exact normalized set of requested object IDs with the grant. It then resolves each stored note and verifies its tenant before constructing output. Both checks matter:

- exact scope prevents the caller from adding another same-tenant object;
- stored relation prevents a mislabeled or corrupt request from treating a Tenant B object as Tenant A.

The output also projects only identifiers and summaries. A correct authority decision does not justify returning fields outside the approved effect. Module 1.2 introduced field-aware authorization; this boundary model traces it to the release point.

## Consume lifecycle state before replay

In the local sequential model, a successful export changes `usable` to `consumed`. A second use denies. An expired grant denies even if its signature or identifier would otherwise look valid.

The production proof obligation is harder:

- check and consumption may need to be atomic;
- a queue may redeliver after timeout;
- two workers may race;
- cancellation and revocation may occur after issuance;
- clocks may disagree;
- retry may need idempotent result reuse rather than a second effect.

Do not hide those under the local result. Record “sequential in-memory lifecycle only” as a residual and attach review triggers for persistence, concurrency, and queues.

## Make evidence part of the decision contract

For this exercise, the export is high impact and must not proceed if its bounded decision record cannot be emitted. The record may include:

- caller kind and worker ID;
- action;
- tenant ID and count of object IDs, not their content;
- grant identifier or one-way reference suitable for correlation, not raw secret material;
- allow/deny and bounded reason code;
- enforcement point and model/policy version;
- time and correlation identifier.

It must not include note bodies, raw grants/tokens, passwords, authorization headers, or unnecessary person attributes.

This choice couples export availability to evidence availability. State that trade-off. A different effect could buffer evidence locally or proceed in a declared degraded mode. The security failure is not choosing one universal behavior; it is leaving behavior undefined and claiming observability anyway.

## Bound blast radius explicitly

Write a claim for a compromised registered worker that holds one grant:

| Dimension | Bounded local claim | Residual / later work |
|---|---|---|
| Tenant | Only the grant’s tenant | Fixture store is globally readable by implementation code; no database role isolation |
| Objects | Exact grant set | Atomic persistence and concurrent consumption not modeled |
| Action | `export_summary` only | No real action router or production serialization |
| Fields | ID and summary only | No downstream file/object storage or cache |
| Time/use | Before expiry, one successful use | Synthetic clock argument; no distributed clock/retry proof |
| Egress | Returned in-process to the caller | No production destination binding or network egress policy |
| Policy/control plane | Cannot edit registry/grants through modeled functions | Fixture administrator and process compromise are residual |
| Evidence | Bounded decision event required | In-memory sink is neither durable nor tamper-resistant |

The claim is more useful than “the worker is isolated.” It shows exactly which mechanism and evidence support each dimension and where the argument stops.

## Reduce common mechanisms

Least common mechanism suggests reducing unnecessary sharing across callers and tenants. Candidate improvements include:

- separate public and worker adapters instead of one dispatcher that infers caller kind;
- separate context types so public data cannot represent worker provenance;
- tenant/action/object-scoped grants instead of one global worker boolean;
- exact output projection instead of a shared “dump all notes” helper;
- evidence schemas that omit protected content;
- later, separate credentials, queues, storage prefixes, egress rules, and operational roles where justified.

Separation has costs: more configuration, lifecycle management, observability, incident paths, and failure modes. The goal is not maximum boxes. It is a smaller, more reviewable TCB and a narrower common failure domain for the property.

## Evaluate five candidate repairs

### 1. Strip the marker at the public edge

Useful hardening and detection, but insufficient as the authority root. A misroute, alternate adapter, parser disagreement, or edge configuration change can reintroduce the field. If the API treats its presence as worker provenance, the property still depends on the edge’s negative filtering.

### 2. Accept the marker only from a private address

An address may be a routing signal, not a product authority fact. Proxies, shared networks, SSRF paths, misconfiguration, NAT, or compromised internal workloads can defeat the assumption. The mechanism may contribute to network isolation later; it does not replace service provenance and scoped authority.

### 3. Sign the entire request with a global worker key

This can improve integrity and provenance relative to a public string, but a global key may authorize every tenant/action/object indefinitely. It creates a large blast radius and difficult rotation. Signature validity must not be confused with product permission.

### 4. Use separate adapters and a scoped, single-use grant

This is the local structural repair. It removes public metadata from worker provenance and binds the effect to current narrow authority. It still shares a process/runtime, fixture registry, policy code, and store, so the independence and production claims remain bounded.

### 5. Deny all export

This preserves confidentiality but destroys authorized functionality and does not demonstrate a usable security design. A successful repair must preserve valid normal behavior while blocking forbidden effects.

## Build a decision record

Before viewing the fixed implementation, submit:

| Decision field | Required content |
|---|---|
| Property | Public cannot obtain worker-only export; narrow worker grant required |
| Trusted provenance source | Which adapter/state constructs caller kind and identity |
| Untrusted inputs | All public fields; worker-chosen presentation time; requested identifiers until checked |
| Positive rule | Exact worker/action/tenant/object/lifecycle/evidence conditions |
| Enforcement point | Function immediately before summary selection and release |
| Unknown/failure behavior | Deny reason and unchanged output/state |
| Lifecycle | Issue, usable, consumed, expired, revoked/deferred |
| Evidence | Bounded fields, sink behavior, correlation, prohibited fields |
| Rejected alternatives | At least three and their remaining failure |
| Blast radius | Tenant/action/object/field/time/egress/control/evidence dimensions |
| Residual | No production identity, transport, queue, transaction, sandbox, or durable evidence claim |
| Review triggers | Every change that invalidates the local proof |

## Compare with the fixed tree

Only after writing the record, inspect:

- `labs/1.3/1.3-trust-boundaries/fixed/surface.py`
- `labs/1.3/1.3-trust-boundaries/fixed/SECURITY.md`

For each field, cite the code path or test that supports it. If the implementation differs from your design, decide whether it is a defect, a legitimate alternative, or a documented fixture limit. “The tests pass” does not settle an unsupported claim.

### Success criteria

- Public and worker provenance have structurally separate construction paths.
- No requester-controlled field can choose caller kind or worker identity.
- Provenance is not treated as sufficient authority.
- Grant scope includes worker, action, tenant, exact objects, expiry, and use state.
- The decision is consumed before the protected output and every in-scope output path is traced.
- Evidence failure is deliberate and sensitive content is excluded.
- At least three plausible non-fixes are rejected causally.
- Blast radius and residuals are dimensional and testable.

## Transfer hook

PreviewForge cannot use one in-process context type as its production isolation story. A converter processes hostile stored bytes, may require narrowly constrained egress, and may run asynchronously. The same reasoning still applies: provenance of the queued job, current authority to process one object, parser/sandbox TCB, exact output destination, lifecycle/retry state, evidence, and bounded blast radius must be separated.
