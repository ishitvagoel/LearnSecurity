# 1.3-LO-06 — Detect boundary drift and recover from crossed assumptions

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** OWASP Threat Modeling Project lifecycle guidance: revisit when architecture, data flows, implementation choices, or incident evidence change. ASVS references in this module are bounded design/verification anchors, not an operations framework.

## A boundary model is a living operational dependency

At design time, a boundary is an assumption change on a diagram. At runtime, it becomes a set of decisions, configuration, identities, paths, evidence, owners, and failure responses. If those drift while the diagram remains unchanged, the model becomes a source of false confidence.

Operations must answer:

- How will we know which boundary and model version handled an effect?
- Which signals suggest public-to-worker confusion, scope widening, replay, bypass, common-mode failure, or unexpected egress?
- What happens if evidence itself is unavailable or compromised?
- How do we contain the smallest blast radius without preserving a vulnerable alternate path?
- How do we recover properties, state, outputs, authority, and the model—not merely restart a service?
- Which change or incident forces Modules 1.1, 1.2, and 1.3 artifacts to be revised together?

## Design a privacy-safe evidence contract

For each export decision, a real design might record:

| Field | Purpose | Constraint |
|---|---|---|
| event kind and schema version | Stable interpretation | Do not overload one field across meanings |
| model/policy version | Identify the assumptions enforced | Must map to reviewed artifacts |
| caller kind and effective worker ID | Distinguish public/worker provenance | Prefer stable internal identifier; avoid unnecessary person attributes |
| trusted adapter / enforcement point | Detect alternate paths | Must be server-derived, not copied from public claims |
| action, tenant ID, object count | Explain scope | Avoid note content; justify object IDs if logged |
| grant reference or digest | Correlate lifecycle | Never log a bearer secret or raw capability |
| decision and bounded reason | Diagnose allow/deny | Avoid reflecting hostile content in reason text |
| lifecycle state / replay indicator | Detect expired or reused authority | Keep issue/use/revocation semantics explicit |
| correlation ID and time source | Join issue, decision, effect, and response | Treat public correlation values as untrusted; add trusted ID |
| evidence outcome | Show stored, buffered, or failed | A local “logged” call is not durable proof |

Prohibited by default: note bodies, passwords, raw tokens/grants, authorization headers, arbitrary uploaded/request content, full exports, unnecessary email addresses, or debug dumps of context. Evidence is itself a data flow and attack surface. Its readers, retention, tenancy, integrity, availability, and deletion rules require protection.

## Define signals as hypotheses

“Alert on suspicious activity” is not operational. Write a hypothesis, window, threshold, evidence fields, owner, false-positive risk, and response.

### Signal A — internal metadata at the public adapter

**Hypothesis:** a client, proxy, or integration is presenting fields that obsolete designs treated as worker provenance.

**Possible signal:** count public-adapter calls containing reserved internal labels, grouped by public principal/client class and route, over a short window. Alert on a material change from the documented baseline or any use on a worker-only operation.

**Limits:** SDK bugs, migration traffic, or generic header names can create false positives. Absence does not prove no alternate representation exists. Do not store the raw field if a normalized presence/category suffices.

### Signal B — provenance/path mismatch

**Hypothesis:** a worker-only action arrived through a public adapter, or a public action arrived through an unexpected worker path.

This should normally be structurally impossible in the local design. Any observation is high-value drift evidence. Contain the route/adapter and inspect deployments/configuration rather than merely blocking one caller string.

### Signal C — capability scope or lifecycle denial

**Hypothesis:** a stale worker, software defect, replay, or attempted widening is presenting a grant outside tenant/action/object/time/use scope.

Group reason codes without collapsing them. A spike in `object_scope_mismatch` has different causes than `expired` or `already_consumed`. Establish expected retry/clock behavior before choosing thresholds.

### Signal D — boundary decision without effect or effect without decision

**Hypothesis:** a partial failure, bypass, duplicate, or evidence gap has separated authorization from the protected effect.

Correlate issue → decision → use transition → output completion. Exact-one relationships may be wrong when retries/idempotency are introduced, so document permitted state transitions rather than counting log lines blindly.

### Signal E — unexpected blast-radius dimension

**Hypothesis:** a worker, credential, cache key, store role, or egress path can reach more tenants, fields, destinations, or time than the model states.

Use synthetic canaries, access-denial evidence, configuration drift checks, and periodic path review where appropriate. Do not use real sensitive data as a canary in this course.

## Decide evidence-failure behavior

Three broad choices exist:

- **Block:** high-impact effect does not occur without required evidence. Strong accountability, weaker availability, possible denial-of-service pressure.
- **Buffer:** effect proceeds only if bounded local evidence can be durably queued for later delivery. Adds storage, overflow, integrity, replay, and privacy responsibilities.
- **Degrade explicitly:** selected effects proceed with a declared reduced-assurance mode, independent fallback signal, owner notification, and bounded duration. Risky for high-impact releases.

The local export fixture chooses **block**. Your operations artifact must explain why, how users/operators see the failure, and how work resumes without bypassing the boundary. “Retry until it works” needs rate, expiry, duplication, and idempotency rules.

## Incident scenario — public caller reached an export

Assume evidence shows a public call received Tenant A summaries through an alternate helper that bypassed the fixed adapter. Work causally.

### 1. Bound the observation

Record known model version, path, caller kind, tenant/object scope, time, output fields, evidence gaps, and confidence. Do not infer “all tenant data leaked” or “only these two notes” before enumerating reachability.

### 2. Contain narrowly, then expand by shared assumption

Possible first actions:

- disable the affected export entry/helper;
- revoke the relevant capability class or worker registration;
- block a specific egress destination;
- pause one tenant’s export if evidence supports that scope;
- preserve bounded evidence and state.

Then locate every path sharing the root assumption: public/worker dispatcher, admin export, retry job, restore tool, cached decision, broad store credential, evidence writer. Blocking only the observed string leaves the structural bypass.

### 3. Revoke and rotate abilities

Revoke affected grants, registrations, sessions, or credentials according to actual reach. A global rotation may be necessary if one shared credential crossed all tenants, but unnecessary broad disruption should not substitute for analysis. Record maximum time to effective revocation across caches, queues, retries, and running jobs.

### 4. Repair the root cause

Restore separate provenance construction, mandatory scoped decision, complete effect mediation, fail-safe unknowns, and bounded evidence. Search for every implementation path compiled from the same false boundary pattern.

### 5. Reconcile state and outputs

Identify summaries or other fields released, downstream copies, cached results, queued/retried effects, and evidence missing. Confidentiality cannot always be restored. Recovery may require notification and containment of further dissemination, not a misleading claim that rotation “undoes” disclosure.

### 6. Retest and refresh

Run normal, negative, abuse, failure, and counterfactual evidence. Update:

- Module 1.1 property/capability assumptions;
- Module 1.2 authority cells and enforcement inventory;
- Module 1.3 flows, TCB, surfaces, shared dependencies, blast radius, and signals;
- owners, residuals, change triggers, and later-module backlog.

### 7. Communicate accessibly

Provide a plain-language impact statement, technical causal record, affected scope/confidence, current containment, usable workaround, and next update. Do not rely on red/green diagram colors alone. Operator actions and approval/revocation controls must support keyboard use, assistive technology, explicit focus, clear errors, and confirmation states.

## Distinguish containment, eradication, and recovery

| Phase | Boundary example | Common mistake |
|---|---|---|
| Containment | Disable bypass path and revoke affected grants | Block one header value while alternate path remains |
| Eradication/root-cause repair | Remove public-to-worker provenance inference; guard every effect | Patch only the observed test case |
| Recovery | Reconcile outputs/state, restore evidence, reissue narrow grants, validate five modes | Restart service and declare incident closed |
| Learning | Refresh model, tests, owners, triggers, and shared-failure analysis | Archive report without changing assumptions |

Detection cannot compensate for weak prevention where irreversible confidentiality loss is unacceptable. Recovery cannot un-disclose data. The three functions still belong in one design because prevention will never justify an assumption of perfection.

## Refresh the model on meaningful change

OWASP guidance emphasizes continuous refinement. Trigger review when:

- a new architecture component or data flow appears;
- request or message representation changes;
- a worker gains a tool, action, tenant, destination, or longer lifetime;
- a queue/retry/scheduler makes execution asynchronous;
- a provider, identity source, object store, parser, or evidence sink changes;
- a shared credential/cache/runtime/operator is introduced;
- an isolation or defense-depth claim changes;
- an incident/test shows unmodeled reach even without a visible diagram change.

Use a change record:

| Change | Invalidated assumption | Affected property | 1.2 cells / 1.3 flows | New surface/dependency | Evidence to retire/add | Owner / deadline |
|---|---|---|---|---|---|---|

An unchanged box diagram is not evidence of unchanged security. A library choice can add dangerous parsing and resource use. A configuration change can alter provenance. An AI component can gain new tools/authority without a new network arrow.

## Operations exercise

Produce a boundary-operations pack for the modeled export:

1. privacy-safe event schema and prohibited-field list;
2. at least four signals, each with hypothesis, window/threshold rationale, evidence, owner, false-positive/negative risk, and first action;
3. decision for evidence sink outage: block, buffer, or explicit degrade, with availability and privacy trade-offs;
4. incident runbook covering scope, containment, revocation/rotation, shared-path enumeration, root-cause repair, output/state reconciliation, evidence restoration, five-mode retest, and communication;
5. maximum revocation-effect interval for every authority copy in the modeled scope;
6. an accessible operator path and safe failure alternative;
7. a completed refresh record for the hypothetical addition of a persistent queue;
8. residual risks for provider/operator/process compromise and evidence tampering.

### Peer drill

One learner acts as incident lead, one as skeptical reviewer. The reviewer introduces two facts:

- a second export helper bypasses the main wrapper;
- the evidence sink and application share one administrator and runtime.

The incident lead must revise scope, independence claims, containment, and evidence confidence. Credit comes from changing the model when evidence changes, not defending the original diagram.

### Success criteria

- Evidence enables decisions without storing protected content or bearer secrets.
- Every signal has a causal hypothesis and response, not a vague “anomaly” label.
- Evidence outage behavior and availability cost are explicit.
- Containment covers all paths sharing the root assumption.
- Recovery includes state/output reconciliation and cannot claim to reverse disclosure.
- Prior 1.1/1.2/1.3 artifacts are updated together.
- Operations and communication are accessible and scope-honest.

## Transfer hook

PreviewForge changes operational priorities: parser crashes and resource exhaustion can dominate availability; unexpected converter egress may be the highest-value signal; stored hostile content may contaminate evidence; object-store callbacks and queue retries create provenance/lifecycle ambiguity; and preview caches can preserve unsafe output after the worker is fixed. LO-07 requires a new evidence and recovery plan rather than this export runbook with renamed actors.
