# SecureCollab — Phase 1 trust-boundary and attack-surface model

**Owner:** Module 1.3

**State:** design reference plus isolated local boundary evidence; not networking, workload-identity, database, queue, or production assurance

**Version:** 2, 2026-08-29

**Depends on:** Module 1.1 invariant catalogue version 1; Module 1.2 authority model version 2

This artifact records where SecureCollab Phase 1 security assumptions change, which flows can influence protected effects, which components must be correct for selected properties, and where current evidence stops. Later slices must preserve or explicitly revise it.

## Boundary invariant

Every in-scope flow that can reveal, mutate, authorize, enqueue, or record a protected effect crosses a named boundary whose trusted side derives caller kind, identity, and authority scope from recorded trusted sources. Requester-controlled metadata—including an internal-sounding field, tenant label, service name, route, source address, or object identifier—is not proof of provenance or permission.

Unknown, missing, malformed, expired, replayed, mismatched, or required-evidence-failed context denies before the effect. Defensive layers are called independent only for a named failure after their shared inputs, code, identity, credentials, configuration, runtime, operators, and evidence paths are examined.

## Product and evidence scope

### Included

- hostile public request data;
- conceptual ingress that preserves untrusted semantics;
- public adapter that cannot construct worker provenance;
- local illustrative worker registry/adapter;
- Module 1.2 policy and effect enforcement;
- synthetic note, membership, registration, and scoped-grant state;
- exact summary export output;
- bounded in-memory decision evidence;
- sequential grant expiry/use behavior.

### Illustrative, not production proof

- the direct worker adapter models a trusted construction path but not cryptographic workload identity;
- single-use grants model lifecycle but not persistent atomicity, concurrency, or queue delivery;
- in-memory evidence models schema and outage behavior but not durability, integrity, access control, retention, or independent delivery;
- the export is a design exercise, not a shipped SecureCollab feature.

### Deferred / review-triggering

- Next.js/FastAPI request-path deployment, proxy/CDN/gateway behavior, TLS, DNS, and routing;
- IdP, email, object storage, analytics, search, caches, queues, schedulers, webhooks, retries, and mobile clients;
- database roles, row policies, transactions, replicas, backups, and restore;
- cryptographic service identity/capabilities, secret/key/certificate rotation, cloud IAM, build/CI, and control plane;
- processes, containers, sandboxing, host isolation, and egress policy;
- production observability, operators, incident objectives, real personal data, and compliance evidence.

Deferred means the Phase 1 evidence does not cover the component. It never means the component is safe by default.

## Components, actors, and principals

| Element | Role in model | Trust treatment |
|---|---|---|
| Public caller/browser | Actor choosing request fields, identifiers, ordering, and repetition | Hostile for all server properties |
| Conceptual ingress | Carries public representation | Not trusted to create worker provenance; header filtering can be hardening/signal later |
| Public adapter | Entry that constructs public-only context | Trusted only to prevent public-to-worker promotion and preserve hostile-field labels |
| Worker registry/adapter | Illustrative server-side source of worker caller kind/identity | Trusted for local provenance; production mechanism unproved |
| Worker principal | Effective subject for modeled export | Identity alone grants nothing; scoped current grant required |
| Policy/effect enforcement | Resolves state, decides, projects, and mediates output | In the TCB for authority/confidentiality; every effect path must reach it |
| Note/membership/grant state | Server-held relations and lifecycle | Trusted within local fixture; storage isolation/persistence unproved |
| Evidence sink | Records bounded decision metadata | Trusted for accountability; chosen export policy also makes it an availability dependency |
| Operator/provider/build/control plane | Transitive ability over code/config/state | Explicit residual and later-phase owner |

Actor, principal, component, channel, flow, and entry point remain distinct. A worker is an actor/principal; its adapter and runtime are components; function arguments are the local channel/representation; public and worker adapters are distinct entry points.

## Phase 1 flows

```text
HOSTILE

Public caller
  | F1 public operation, tenant/object labels, internal-looking metadata
  v
Conceptual ingress
  | F2 same untrusted representation
  v
Public adapter
  | B1 constructs PublicContext; does not establish worker provenance
  | F3 public operation
  v
Policy + effect enforcement <---- F4 ---- synthetic note/membership state
  | F5 bounded protected effect
  +------------------------------ F6 ----> evidence sink

TRUSTED FOR LOCAL WORKER CONTEXT CONSTRUCTION

Synthetic worker registry
  | F7 registered worker identity / grant reference
  v
Worker adapter
  | B2 constructs WorkerContext; production identity remains deferred
  | F8 worker + exact action/tenant/object request + grant
  v
Policy + effect enforcement
  | F9 exact summary-only output and grant consumption
  v
In-process export result
```

### Boundary meanings

- **B1:** the receiving context can rely only on arrival through the public adapter and inability to represent worker caller kind. Request fields remain attacker-controlled claims.
- **B2:** the local receiving context can rely on identity resolved from fixture registry state rather than public fields. Grant scope, stored relations, expiry, use state, and evidence availability still require enforcement.
- **Effect boundary:** no summary is constructed or released until current positive authority is consumed. A correct policy not reached by every path is insufficient.
- **Evidence boundary:** only bounded decision metadata crosses. Whether evidence failure blocks, buffers, or degrades the effect must be explicit; the local high-impact export blocks.

Network topology is deliberately absent. A future connection can add transport and routing assumptions but cannot redefine attacker-controlled data as authority without an independently justified provenance mechanism.

## Flow ledger

| Flow | Source → destination | Content and attacker control | Changed / unchanged assumption | Protected effect and enforcement | Shared dependencies | Current evidence / residual |
|---|---|---|---|---|---|---|
| F1 | Public caller → ingress | All fields, IDs, timing, repetition are caller-selected | None; hostile | None yet | Public parser/routing later | Local forged-metadata cases; no HTTP proof |
| F2 | Ingress → public adapter | Same public representation | Still hostile; ingress filtering is not authority | Public adapter forces public caller kind | Representation/configuration later | Adapter behavior tested; proxy semantics deferred |
| F3 | Public context → policy/effect path | Requested public action and unresolved IDs | Caller kind known as public; identifiers remain untrusted | Module 1.2 current authorization before note/membership effects | Dispatcher, policy/runtime | Selected in-memory paths only |
| F4 | Store → policy | Current tenant/object/membership/grant relations | Server-held fixture state | Decision binds stored relation | One global in-memory store/runtime | Cross-scope tests; DB/storage isolation deferred |
| F5 | Enforcement → public result | Exact allowed fields/effect | Decision consumed | Direct/list/admin effects per Module 1.2 | Output helpers/serializers later | Local 1.2 evidence; web integration deferred |
| F6 | Decision/effect → evidence | Bounded IDs/count/reason/version/time | Evidence treated as sensitive surface | Exercise export denies if unavailable | Same process/operator; durable sink later | Schema/outage tests; integrity/durability residual |
| F7 | Registry → worker adapter | Registered worker identity and grant reference | Local server-held source, not public claim | Constructs worker context only | Registry, config, process/operator | Unknown worker denial; production identity residual |
| F8 | Worker context → export enforcement | Worker ID, action, tenant, exact object set, grant, time | Provenance established; authority still must be checked | Grant binds all dimensions, denies unknown/expired/used | Runtime, grant/store/policy | 18-test local suite; persistence/queue deferred |
| F9 | Enforcement → export result | IDs and summaries only; grant state becomes consumed | Positive decision required | Exact output after enforcement | Shared store/helper/process | Exact field/state oracle; egress/storage residual |

## Property-relative TCB

| Component / assumption | Export authority | Summary confidentiality | Accountability | Availability |
|---|---|---|---|---|
| Public caller honest | Not trusted | Not trusted | Not trusted | Not trusted |
| Public adapter cannot construct worker identity | Required | Required | Relevant path label | Relevant to denial behavior |
| Worker registry/adapter provenance | Required | Required | Required for attribution | Needed for worker service |
| Grant and current stored relations | Required | Required | Required decision context | State availability needed |
| Policy and effect enforcement | Required | Required | Produces bounded reason | Resource/failure behavior matters |
| Output projection | Relevant to approved effect | Required | Must avoid content in evidence | Minor in local fixture |
| Evidence producer/sink | Not otherwise preventive | Must not copy bodies | Required | Required because local export blocks on failure |
| Conceptual ingress filtering | Not relied upon | Not relied upon | May become a signal | May shape load later |
| Runtime/process/operator | Transitive local trust | Transitive local trust | Can suppress/alter evidence | Common failure domain |

The browser never joins these TCBs. Provider, build, control-plane, and production operator trust remain explicit residuals rather than a “trusted cloud” box.

## Attack-surface inventory

| Surface / flow | Reachable capability/failure | Controlled input/state | Protected effect | Enforcement / trusted source | Shared mechanism and blast radius | Evidence / closure |
|---|---|---|---|---|---|---|
| Public metadata F1/F2 | Any public caller chooses internal label, service, tenant, objects | Entire mapping | Worker-only export or alternate public effect | Public adapter cannot create worker context | Shared parser/routing could reach all worker effects if trusted | Executable forged/plain cases locally; production path deferred |
| Public dispatch F3 | Authenticated/unknown subject selects operation/IDs | Action/identifiers until resolved | Note/membership read or mutation | Module 1.2 current policy at each effect | Common dispatcher/policy can be bypass/common failure | Selected 1.2 local paths; routes later |
| Stored relations F4 | Stale/corrupt state or broad code/credential | Membership/tenant/object/grant state | Cross-tenant or stale allow | Server-held resolver and exact checks | Global fixture/store role can reach all tenants under compromise | Local negative cases; DB/backup residual |
| Worker registry F7 | Misconfiguration/operator/process compromise | Registered identity | False worker provenance | Separate server-side adapter | Registry administrator/process may reach all workers | Unknown registration test; production identity/operator residual |
| Grant presentation F8 | Registered worker, replay, logic failure | When and which known grant presented | Tenant/action/object/time widening | Exact current server-held grant | Grant store/policy/runtime; one broad grant widens all dimensions | Worker/scope/expiry/replay tests; atomicity deferred |
| Output construction F9 | Bypass/projection defect | Selection code and state | Unauthorized field/object release | Effect wrapper after allow, exact projection | Shared helper/store/process | Exact IDs/fields and empty-denial oracles; alternate real paths later |
| Evidence F6 | Sink outage, overbroad schema, process/operator compromise | Availability and recorded fields | Unobserved effect or content leakage | Explicit block policy and bounded schema | Same runtime/operator can affect decision and record | Schema/outage tests; durable independence residual |
| Configuration/control | Operator/build/provider compromise | Adapter routing, registry, policy, code | Any modeled effect and evidence | Not independently controlled in Phase 1 | Whole local TCB; all tenants/time | Residual with Phase 10/build/deployment triggers |

The inventory is not a list of ports, endpoints, products, CVEs, or awareness categories. It begins at reachable influence and ends at protected effects, evidence, and residuals.

## Transitive trust and common-mode analysis

```text
export authority
  -> adapter provenance
     -> registry/configuration
        -> process/runtime/build/operator (residual)
  -> scoped grant and relations
     -> state store/policy code
        -> process/runtime/build/operator (shared residual)
  -> effect enforcement/output projection
     -> same process/runtime (shared residual)

accountability
  -> event producer/schema
     -> same process/runtime/operator
  -> durable delivery/storage/access (deferred)
```

Current control classifications:

| Controls | Named fault | Classification | Reason |
|---|---|---|---|
| Edge strips internal field + API trusts field | Public assertion/parser/routing drift | Correlated | Both depend on the same negative filtering and representation; not part of fixed authority argument |
| Public adapter + grant enforcement | Public metadata promotion | Partially independent/complementary | Caller kind and grant state are distinct inputs, but process/runtime/operator and coverage are shared |
| Grant exact scope + output projection | Scope versus field over-release | Partially independent | Different checks can limit different effects; shared policy/helper/runtime compromise can defeat both |
| Prevention + bounded evidence | Ordinary policy defect | Detection may be partially independent logically | Same process/operator can both permit and suppress; durable independent path is unproved |

No numerical reduction is claimed. A future separate product or managed service is not independent until its dependencies and named failures are examined.

## Blast radius

For compromise/misuse of one registered worker holding `grant-a-exact`, the fixed local property intends:

| Dimension | Current local bound | Residual |
|---|---|---|
| Tenants | Tenant A only | Same process/store code can access all fixture state under full compromise |
| Objects | Exactly A1 and A2 | No database credential/row isolation proof |
| Action | `export_summary` | No production action router or destination binding |
| Fields | ID and summary | No downstream file/cache/CDN path |
| Time/use | Before synthetic expiry, one successful sequential use | No persistent atomicity, concurrency, distributed clock, retry, cancellation |
| Egress | In-process return only | Production network/object destination unmodeled |
| Resources | Tiny bounded fixture selection | No production workload/capacity limits |
| Policy/control | No modeled mutation path | Process/operator/build/control plane remain broad residual |
| Evidence | Bounded event required | In-memory evidence can be changed/suppressed by same process/operator |

This table is the isolation claim. “Internal worker,” “tenant column,” or “separate adapter” alone is not.

## Evidence and operations contract

Current event fields: event/schema or model version, caller kind, effective worker, action, tenant, object count, allow/deny reason, enforcement point, time, and correlation where available. Exclude note bodies, raw grants/tokens, passwords, authorization headers, arbitrary request content, and unnecessary personal attributes.

Required signals for a production successor include:

- internal/reserved metadata observed at public entry;
- worker-only action arriving through public adapter;
- worker/grant, tenant, action, object, expiry, or replay denial changes;
- effect without current decision or decision without expected effect transition;
- unexpected tenant, egress, resource, policy, or evidence reach;
- model/policy/configuration version drift.

For the local high-impact export, evidence unavailable means deny and leave grant unused. A production design may block, buffer, or explicitly degrade per effect, but must model the availability/privacy consequences.

Response to a crossed boundary:

1. scope the observed path, tenant/object/field/time/egress, model version, and evidence confidence;
2. contain the narrow adapter, operation, grant class, worker, tenant, or destination;
3. enumerate all public, worker, admin, retry, restore, cached, and maintenance paths sharing the assumption or broad mechanism;
4. revoke/rotate affected abilities and state the maximum effective interval;
5. repair provenance and mediation root cause;
6. reconcile state and released/persistent outputs; disclosure cannot be undone;
7. restore evidence, run five modes, and refresh Modules 1.1–1.3 plus later backlog;
8. communicate scope and uncertainty accessibly without relying on color alone.

## Standards trace

- OWASP Threat Modeling Project: Four Questions, system representations, assumptions/actions/validation, and lifecycle refinement; no single OWASP methodology is claimed.
- ASVS 5.0.0: `v5.0.0-15.3.4` supports exact reasoning about trusted non-user-manipulable proxy provenance, while its original-IP limitations remain explicit; it is not treated as workload-identity specification.
- ASVS 5.0.0: `v5.0.0-15.1.3` and `v5.0.0-15.2.2` become relevant to resource-demanding worker functions; `v5.0.0-15.2.5` is a labeled Level 3 isolation anchor for dangerous/risky components, principally transferred to PreviewForge.
- Saltzer and Schroeder: economy of mechanism, fail-safe defaults, complete mediation, and least common mechanism are design principles, not numbered compliance clauses.

No ASVS compliance, production isolation, or milestone assurance is claimed.

## Spiral deltas and required revisits

This model changes prior artifacts as follows:

- **SC-CONF-01:** alternate export/evidence/output paths and shared mechanisms join the confidentiality surface; summary and body projection remain separate.
- **SC-INTEG-01:** every mutation path needs boundary provenance plus current authority at the effect; future delayed workers add check/use and replay state.
- **SC-ACCT-01:** evidence has its own trust/data boundary, TCB, privacy limits, and outage behavior.
- **SC-AVAIL-01:** worker/evidence dependencies and resource-demand documentation join the property when real background work appears.
- **SC-PRIV-01:** output/evidence/cache/restore paths must preserve lifecycle absence; future object/CDN paths reopen the row.
- **Module 1.2:** worker identity and worker authority are distinct; the illustrative export decision now has an explicit entry/effect path and lifecycle.

Required later revisits:

- 1.4 risk register prioritizes surface rows without erasing residuals;
- 2.2 replaces conceptual ingress with request-path evidence;
- 2.4 addresses failure, time, check/use, and partial effects;
- 3.2 adds formal threat elicitation/versioning;
- 4.4 and 5.5 add web and persistence enforcement/isolation;
- 7.4 adds queue, worker, retry, cancellation, idempotency, and originating/effective authority;
- 8.1 revisits hostile client behavior and mobile/offline clients;
- 10.5 adds production evidence/incident/recovery obligations.

## Review triggers

Reopen this artifact for any new or changed property, actor/principal, adapter, route, protocol, parser, field representation, authority source, policy/enforcement point, store, cache, queue, scheduler, worker action, retry, webhook, third party, credential, isolation mechanism, egress path, evidence field/sink, operator/control plane, backup/restore path, or incident finding. Update affected 1.1 catalogue rows and 1.2 authority cells at the same time.

## Honest limits

- The local lab proves selected in-process functions and source constraints only.
- Python call separation is not production authentication or isolation.
- Sequential memory is not persistent atomicity, concurrency, queue safety, or revocation propagation.
- One runtime/operator remains a common failure domain.
- No public product, real data, Gate 1, M0, ASVS baseline, compliance result, or production assurance becomes complete because this reference exists.
