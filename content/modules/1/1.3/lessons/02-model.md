# 1.3-LO-02 — Build the SecureCollab boundary and attack-surface model

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP Threat Modeling Project (system representation, assumptions, validation, and lifecycle refinement); OWASP ASVS 5.0.0 `v5.0.0-15.1.3`, `v5.0.0-15.2.2`, `v5.0.0-15.2.5`, and `v5.0.0-15.3.4` as bounded anchors.

## Model a decision, not a cloud cartoon

This lesson constructs the Phase 1 representation used by the lab. It is intentionally a **design model**, not a claim that SecureCollab has production networking, cryptographic workload identity, a real queue, or deployed isolation.

Carry forward two artifacts:

- Module 1.1 says which note confidentiality, authority, availability, and accountability properties matter.
- Module 1.2 says which subjects may perform which actions on which objects in current state.

Module 1.3 asks where those decisions and effects cross assumptions. If the authority matrix says a worker may export Tenant A summaries, the model must show how a caller becomes that worker, how Tenant A and the object set are bound, where the decision is enforced, and which other paths reach the same output.

## Scope ledger

Start with a ledger so a diagram cannot silently grow fictional assurances.

| Item | Phase 1 treatment | Security meaning |
|---|---|---|
| Browser / public caller | In scope and hostile | Chooses request fields, ordering, identifiers, and repetition |
| Public ingress | Conceptual pass-through | Does not establish worker provenance; later request-path configuration is Module 2.2 |
| Public adapter | In scope | Produces a public context; cannot grant worker authority |
| Worker adapter | Local illustrative boundary | Produces worker context only from server-held fixture state; not production identity proof |
| Policy / enforcement | In scope | Resolves current authority and guards the export effect |
| Note/membership store | Synthetic in-memory state | Source of tenant/object relations; no database isolation claim |
| Evidence sink | Synthetic in-memory records | Makes decisions observable; no durable or tamper-resistant logging claim |
| Queue, scheduler, retries | Deferred but modeled as trigger | Module 7.4 must replace the direct worker call with real delayed-state reasoning |
| IdP, email, object store, CDN, analytics | Deferred dependencies | Must not be drawn as already protected or implemented |
| Cloud control plane, backups, CI/build | Residual/later work | Transitive trust remains explicit |

If a reviewer cannot tell what exists, what is illustrative, and what is deferred, the model is misleading before any threat is considered.

## Draw flows with identifiers

Use stable flow identifiers so diagram, inventory, tests, and incident notes can refer to the same thing.

```text
HOSTILE / REQUESTER-CONTROLLED

  [Public caller]
       |
       | F1: requested operation, tenant/object labels,
       |     internal-looking metadata, correlation value
       v
  [Conceptual ingress] -- F2: unchanged untrusted representation --> [Public adapter]
                                                                  |
                                              B1: context-construction boundary
                                                                  |
                                                                  v
TRUSTED FOR CONTEXT CONSTRUCTION                            [PublicContext]
                                                                  |
                                                                  | F3: public operation request
                                                                  v
                                                        [Policy + enforcement] ---- F6 ----> [Evidence sink]
                                                                  |
                                                                  | F4: current tenant/object lookup
                                                                  v
                                                           [Phase 1 store]

  [Synthetic server-held worker registry]
       |
       | F7: worker identity + scoped grant identifier
       v
  [Worker adapter] ---- B2: worker-provenance boundary ----> [WorkerContext]
                                                                  |
                                                                  | F8: export request + narrow capability
                                                                  v
                                                        [Policy + enforcement]
                                                                  |
                                                                  | F9: summary-only export effect
                                                                  v
                                                           [Export result]
```

Boundary B1 does not make request data “trusted.” It makes one narrower statement: the constructed context records that the call arrived through the public adapter and cannot represent worker provenance. Tenant and object identifiers remain untrusted claims until resolved and authorized.

Boundary B2 is also narrow. In the local fixture, it proves that the context came from a separate server-side adapter using registry state, not from public request fields. It does **not** prove how a production workload authenticates, how a queue protects messages, or how deployment configuration resists an operator compromise.

## Annotate every flow

An arrow without content, control, and assumption is decoration. Expand F8:

| Field | F8 annotation |
|---|---|
| Source | Worker adapter acting for registered worker `export-worker-1` |
| Destination | Policy/enforcement immediately before export |
| Direction | Adapter to enforcement |
| Representation | In-process `WorkerContext` plus opaque grant identifier |
| Attacker control | A public caller cannot construct the context through the public adapter; a compromised registered worker can choose when to present its own grant |
| Changed assumption | Caller kind and worker ID come from server-held adapter state, not request strings |
| Still untrusted / to verify | Grant existence, tenant, action, object set, expiry/use state, stored note relations |
| Entry point | Worker adapter |
| Enforcement point | Export function before selecting summaries |
| Shared dependencies | Runtime, fixture registry, capability store, policy code, evidence path |
| Failure behavior | Unknown caller/context/grant/scope denies; evidence-failure behavior must be explicit |
| Protected effect | Release only approved Tenant A note summaries |
| Oracle | Decision plus exact output IDs; no note bodies; capability becomes consumed |
| Residual | Local type/adaptor separation is not cryptographic production service identity |

Do the same for every in-scope flow. If the annotation says “validated,” name validation against what. Syntax validation is not provenance. If it says “authorized,” name subject, action, object, current state, and enforcement point.

## Overlay the TCB by property

Do not fill every box with the same trusted color. Use a table or symbols that remain readable without color.

| Component / assumption | Export authority | Note-summary confidentiality | Accountability | Availability |
|---|---|---|---|---|
| Public caller honest | Not trusted | Not trusted | Not trusted | Not trusted |
| Public adapter cannot create worker context | Must be correct | Must be correct | Relevant | Relevant to denial only |
| Worker registry / adapter provenance | Must be correct | Must be correct | Must be attributable | Relevant to worker availability |
| Capability scope/use state | Must be correct | Must be correct | Must be recorded | Expiry/replay state can deny work |
| Policy + effect enforcement | Must be correct | Must be correct | Decision reason producer | Resource use can affect availability |
| Store’s tenant/object relations | Must be correct | Must be correct | Object IDs needed | Store availability needed |
| Evidence sink | Not preventive in this design | Must not receive bodies | Must be correct/available for accountability | Backpressure policy matters |
| Conceptual ingress header stripping | Not relied upon | Not relied upon | May provide a signal only | May shape load later |

The row for ingress is important. If both edge and application trust the same internal-looking header, ingress becomes part of the authority TCB and a common configuration or parsing error defeats both. A safer property does not rely on the public edge to turn an attacker-controlled string into worker provenance.

## Derive the attack-surface inventory

Begin with flows and shared mechanisms, not with a scanner. A partial inventory follows.

| Surface / flow | Reachable actor or failure | Controlled input/state | Boundary / effect | Enforcement / trusted source | Shared mechanism and blast radius | Oracle / residual |
|---|---|---|---|---|---|---|
| F1/F2 public metadata | Any public caller | Internal label, tenant, action, object IDs, repetition | B1 / attempted worker export | Public adapter must force public caller kind | Shared parser/routing can expose all worker-only effects if trusted | Public presentation denies and emits metadata-only evidence; no HTTP proof |
| F3 public operation dispatch | Authenticated or unknown public subject | Operation and identifiers | Policy / note or membership effect | Module 1.2 current policy | Dispatcher shared across tenants; alternate route can bypass mediation | Deny unknown action and trace every effect path |
| F4 stored relation lookup | Stale/corrupt fixture state | Tenant, membership, object relation | Policy / scope decision | Server-held store relation | One global store role can reach all tenants | Cross-tenant and missing-object tests; database isolation deferred |
| F6 evidence write | Sink outage or overbroad logger | Availability and recorded fields | Evidence boundary / accountability and perhaps export | Explicit evidence-failure rule | Shared sink can leak all tenants or hide all decisions | Sanitized schema; simulated failure; durable integrity deferred |
| F7 worker registration | Misconfiguration or compromised operator | Registered ID and grant issuance | B2 / worker provenance | Server-held registry in fixture | Registry administrator may reach every registered worker | Unknown worker denies; production operator/control-plane residual |
| F8 capability presentation | Registered worker or replay | Timing and its grant ID | Policy / export authority | Stored narrow grant and current use state | Reusable/global grant widens tenants, actions, objects, and time | Scope/expiry/replay tests; cryptographic transport deferred |
| F9 result construction | Enforcement or projection defect | Selection code and store state | Output / confidentiality | Exact approved IDs and summary projection | Shared export credential/output sink may expose all notes | Exact IDs/fields oracle; no real storage/egress assurance |

Completeness is relative to stated scope. The inventory is competent only if it covers every in-scope protected effect and labels deferred paths. “No queue in Phase 1” is a legitimate scope statement. Drawing a queue and silently assuming signed messages solve provenance is not.

## Trace authority cells to boundary paths

Take a Module 1.2 cell:

```text
registered export worker × export_summary × {Tenant A: A1, A2}
  with current single-use grant -> allow
```

Trace it end to end:

1. Worker identity originates in the worker adapter, not request metadata.
2. The grant identifier refers to server-held authority; its existence is not enough.
3. Policy checks caller kind, worker ID, action, tenant, exact object set, expiry, and unused state.
4. The effect path selects only allowed objects and projects only summary fields.
5. Use state changes before another successful effect can occur in the fixture’s sequential model.
6. Evidence records a bounded decision and grant hash/ID, not note content.

Now trace the denied cell:

```text
public caller × export_summary × any tenant/object set -> deny
```

No value in F1—including `worker`, an internal route name, or Tenant A—may move the call into the worker cell. That is the boundary property the lab will challenge.

## Analyze defensive independence

Use a dependency table before claiming depth.

| Control | Function | Inputs/dependencies | Bypass/failure | Relation |
|---|---|---|---|---|
| Conceptual ingress strips internal header | Prevention attempt | Same header parser, routing/config, operator | Alternate encoding/path or configuration drift | Correlated with API header trust; not counted as independent |
| Public adapter constructs only `PublicContext` | Prevention | Code path, type/runtime, dispatcher coverage | Direct call to worker effect bypassing adapter | Complementary to effect enforcement; coverage must be tested |
| Capability scope consumed at export | Prevention | Grant store, clock/use state, policy | Global grant, check/use gap, unguarded alternate export | Distinct decision from provenance but shares enforcement/runtime |
| Sanitized decision evidence | Detection/recovery input | Logger schema, sink, correlation/model version | Sink outage or same process compromise | Not preventive; partially independent only if failure path is explicit |

Do not turn “partially independent” into a numerical risk reduction. The table supports an engineering claim: which failures one control can catch when another fails, and which common failures defeat both.

## Worked change: add a queue without granting assurance

Suppose the direct F8 call later becomes:

```text
worker adapter -> queue publisher -> queue -> consumer -> export enforcement
```

New components are not the only change. Ask:

- Is the message a capability, a re-authorization request, or a reference to current server-side state?
- Who is the originating subject and who is the effective consumer?
- Can tenant, action, object set, or destination change between issue and use?
- What do retries, duplication, reordering, delay, cancellation, and revocation mean?
- Which publisher/consumer identities and queue administrators join the TCB?
- Can one queue or consumer credential reach every tenant?
- Where is enforcement repeated immediately before effect?
- What evidence links issue, consume, denial, retry, and effect without leaking content?

This module records those as review triggers. Module 7.4 must supply production-ready asynchronous reasoning. The honest model changes before the implementation claim does.

## Learner practice — produce the Phase 1 pack

Create four linked artifacts:

1. **Annotated diagram:** include F1–F9 or justified equivalents; mark hostile, trusted-for-a-specific-assumption, deferred, and residual using text/symbols as well as color.
2. **Flow ledger:** complete every annotation field shown for F8.
3. **Attack-surface inventory:** cover public, stored-state, worker, export, evidence, and configuration influence paths.
4. **TCB/dependency analysis:** choose export authority and accountability, show how their TCBs differ, and classify at least three control pairs for a named failure.

Then conduct a peer challenge. The reviewer chooses one protected effect and walks backward from effect to every reachable entry point. Any untraced path, untrusted attribute labeled trusted, unnamed shared dependency, or unsupported isolation claim becomes a revision item.

### Success criteria

- Every diagram arrow has a stable flow ID and ledger row.
- Every in-scope Module 1.2 effect maps to at least one enforcement point and oracle.
- Public data remains attacker-controlled after syntax validation and TLS transport.
- Worker provenance and worker authority are separate: provenance says who/caller kind; the grant says what effect is allowed.
- At least one shared mechanism and one transitive dependency are explicit.
- Blast radius is dimensional, not “low/medium/high.”
- Deferred components are named with review triggers and no deployed-control claim.
- The model can be read in grayscale and linear text form.

## Transfer preparation

Archive the SecureCollab pack before LO-07. PreviewForge will invalidate it: stored document bytes become a delayed entry point, parser workers may need egress and sandboxing, object storage and a queue become active dependencies, and availability/resource demand becomes a primary property. The transfer task will score the quality of the reconstruction, not visual similarity.
