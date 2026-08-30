# Module 1.3 assessment — learner evidence and rubric

This file is learner-facing. It contains prompts, submission requirements, and evaluation criteria—not seeded findings or model answers. Examiner anchors remain outside the learning site.

## Required evidence pack

Submit one coherent pack containing:

1. three bounded SecureCollab properties (authority/confidentiality, accountability, and availability) with attacker/failure capability, scope, time, forbidden outcome, and evidence;
2. an annotated Phase 1 boundary diagram and complete flow ledger, including explicit implemented, illustrative, deferred, and residual labels;
3. property-relative TCB overlays showing why the component set changes across at least three properties;
4. a flow-derived attack-surface inventory covering public, stored-state, worker, effect, evidence, shared-mechanism, and configuration influence paths;
5. a trust-dependency graph, three fault-specific defensive-independence classifications, and a dimensional blast-radius statement;
6. exact vulnerable and fixed lab commands/results plus causal traces for every intended failure and a safe counterfactual;
7. a boundary-repair decision record covering provenance, authority, enforcement, lifecycle, evidence, rejected alternatives, and residual limits;
8. a five-mode verification matrix that traces claims to diagram flows, inventory rows, state/output/evidence oracles, and closure states;
9. a privacy-safe evidence contract, signal set, evidence-outage decision, accessible operations path, incident runbook, and model-refresh record;
10. the LO-08 seeded review deliverables with at least eight actionable comments across all required failure classes;
11. the PreviewForge transfer pack and a comparison memo naming at least four SecureCollab assumptions that no longer hold.

All material must remain local and synthetic. Do not include real credentials, personal data, harmful documents/payloads, target details, or evidence from a system you do not own or lack explicit authorization to test.

## Knowledge check — retryable at 80%

Answer each in two to five precise sentences. Revise missed answers before resubmission; the score cannot compensate for missing practical evidence.

1. What makes a trust boundary different from a network hop or line between components?
2. Why is a TCB property-relative? Give one component that changes importance between export authority and accountability.
3. Distinguish an actor, principal, component, channel, data flow, and entry point using one SecureCollab path.
4. Why is an endpoint/port/CVE list not a sufficient attack-surface inventory?
5. What makes trust transitive, and where may a model legitimately stop following the dependency?
6. How can a shared mechanism increase both attack surface and blast radius?
7. Why are an edge check and API check correlated when both trust the same requester-controlled field?
8. What dimensions must a reviewable blast-radius statement include?
9. Why does worker provenance not itself grant export authority?
10. What does a policy unit test fail to establish about complete mediation?
11. Why is evidence-sink failure a security design state rather than only an observability inconvenience?
12. Which conclusion does passing the fixed local lab support, and which production conclusions remain unsupported?

## SecureCollab modeling task

Model the Phase 1 design only. Include hostile requester, conceptual ingress, public adapter, worker adapter/registry, policy and effect enforcement, synthetic note/membership state, output, and evidence sink. Mark IdP, email, object storage, CDN, real queue, production networking, cloud control plane, backups, CI/build, analytics, and mobile client as deferred/residual with activation triggers.

Every flow must record:

- stable identifier, source/destination, direction, and representation;
- actor/principal and attacker-controlled fields/state;
- assumption or capability that changes;
- entry point and enforcement point;
- trusted attribute source and still-untrusted values;
- shared parser/credential/configuration/runtime/operator/evidence dependencies;
- protected effect and failure behavior;
- evidence oracle, blast-radius dimensions, residual, owner, and review trigger.

Choose export authority, note-summary confidentiality, and accountability or availability. Overlay each property’s TCB and explain at least three membership differences. A box described simply as “trusted backend” is insufficient.

## Attack-surface and independence task

Build the inventory using this minimum shape:

| Surface / flow | Reachable actor or failure | Controlled input/state | Boundary / entry | Protected effect | Enforcement / trusted source | Shared mechanism | Blast radius | Oracle / evidence | Closure / residual / owner |
|---|---|---|---|---|---|---|---|---|---|

Cover public metadata, public dispatch, stored tenant/object relations, worker registration, grant presentation, output construction, evidence failure/suppression, and configuration/control influence. An item may be deferred, but it may not be silently called closed.

For at least three alleged layer pairs, choose a fault and record decision input, parser/code, identity/credential, configuration/control plane, runtime/failure domain, operator/vendor, evidence path, and bypass behavior. Classify the pair as independent, partially independent, correlated, or unknown **for that fault**. No numerical risk reduction is required or justified.

Write a blast-radius statement for one compromised registered worker/grant covering tenants, objects, fields, actions, time/use/retry, egress, resource use, policy/control plane, and evidence suppression. Every “cannot” or “limited to” needs a mechanism/evidence link or an explicit residual.

## Lab break/fix task

Run from the repository root:

```text
python -m pytest labs/1.3/1.3-trust-boundaries/tests --impl vulnerable

python -m pytest labs/1.3/1.3-trust-boundaries/tests --impl fixed
```

For every intended vulnerable failure, submit:

- module invariant and diagram flow/inventory row;
- preconditions and trigger;
- root cause in provenance, worker binding, authority scope, lifecycle, evidence, enforcement, or independence;
- exact forbidden output/state and impact;
- structural prevention and enforcement point;
- privacy-safe detection and bounded recovery;
- fixed state/output/evidence oracle;
- remaining fixture limitation.

Group related failures without collapsing distinct bindings. Explain why public metadata, worker registration, and possession of a known grant answer different questions. Compare at least three plausible non-fixes.

Create a disposable copy of the fixed implementation and remove one protection. Predict the exact tests/effects that should change and those that should remain stable, run only the local fixture, report the result, and delete the copy. Do not edit course variants in place.

## Build/design task

Produce a small local patch in a disposable learner copy or a detailed decision record that:

- separates public and worker context construction;
- obtains caller kind/worker identity from a trusted local adapter rather than requester fields;
- enforces a positive current grant over worker, action, tenant, exact objects, expiry, and use state;
- resolves stored object/tenant relations and projects only approved fields;
- denies unknown, malformed, failed, expired, replayed, or mismatched context before output;
- defines evidence-before-effect behavior and prohibited evidence fields;
- names every in-scope effect path and enforcement point;
- compares three rejected repairs and their remaining forbidden outcomes;
- bounds blast radius and assurance limits;
- identifies production review triggers.

The repair must preserve the valid exact worker export. “Deny all,” header denylisting, internal route naming, UI hiding, private addressing, duplicate checks, or an unscoped global signed assertion do not meet the structural requirement.

## Verification task

Create a matrix with columns:

| Claim / flow | Initial state | Capability / failure | Entry and enforcement path | State/output/evidence oracle | Normal | Negative | Abuse | Failure | Counterfactual | Surface closure | Residual |
|---|---|---|---|---|---|---|---|---|---|---|---|

The pack must include:

- valid exact export and summary-only projection;
- plain public and forged-metadata cases;
- worker, tenant, action, and same-tenant object widening cases;
- expiry and replay state;
- evidence-sink failure and unchanged grant/output;
- unknown/malformed context;
- a counterfactual that establishes causal connection;
- at least one policy correctness versus enforcement coverage distinction;
- closure state of executable, structural, deferred, or residual for every surface row.

Status-only assertions are insufficient. Observe exact fields/IDs, empty output after denial, lifecycle state, sanitized evidence, and effect-path coverage.

## Operations task

Produce:

1. privacy-safe decision/effect event schema and prohibited-field list;
2. at least four signals for public internal metadata, path/provenance mismatch, grant scope/lifecycle denial, decision/effect mismatch, or unexpected blast radius;
3. for each signal: causal hypothesis, window/threshold rationale, evidence, owner, false-positive/negative risk, and first action;
4. a justified block, buffer, or explicit-degrade decision for evidence outage;
5. incident steps for scoping, narrow containment, all-path/common-mechanism enumeration, revocation/rotation, root-cause repair, output/state reconciliation, evidence restoration, five-mode retest, and communication;
6. maximum effective-revocation interval for each authority copy in scope;
7. keyboard/assistive-technology usable operator path, clear failure/completion state, and safe alternative;
8. a model refresh record for adding a persistent queue, including invalidated 1.1 property, 1.2 cells, and 1.3 flows/evidence.

Do not claim recovery reverses a confidentiality disclosure.

## Seeded review task

Review the LO-08 design record plus:

- `labs/1.3/1.3-trust-boundaries/vulnerable/surface.py`
- `labs/1.3/1.3-trust-boundaries/vulnerable/SECURITY.md`

Submit at least eight actionable comments spanning boundary/provenance; authority/lifecycle; complete mediation/output; common mechanisms/false depth; evidence/failure/recovery; and scope/assurance. Each comment needs severity, property/forbidden effect, candidate evidence, root cause, minimum structural change, oracle, and residual.

Use at least two exact, applicable standards mappings and reject one standards overclaim. `v5.0.0-15.2.5` must be labeled Level 3 if used. “V15 violation” without an exact ID and bounded applicability is not accepted.

## Transfer task — PreviewForge

Complete LO-07’s synthetic document-pipeline pack. It must include:

- at least three bounded properties and five forbidden outcomes;
- object-version-bound lifecycle from upload intent through withdrawal;
- annotated boundaries/flows covering client, object storage, event verifier, queue, job adapter, converter, workspace, egress, quarantine/output, moderation, preview gateway/CDN, evidence, and build/operator paths;
- property-relative TCBs for object/job binding, converter containment, availability, and accountability;
- flow-derived surface inventory including stored inputs, asynchronous/retry state, parser/resource categories, egress, publication/cache, evidence, updates, and control plane;
- four fault-specific independence classifications;
- dimensional converter blast radius;
- five-mode evidence with state, side-effect, output, cache, and evidence oracles;
- operations/recovery plan for partial output, retry, withdrawal/cache invalidation, and evidence failure;
- comparison memo naming at least four SecureCollab assumptions that fail;
- bounded assurance statement and later work.

Use inert placeholders and test doubles only. Creating or sharing a malicious document, targeting a converter, or contacting real storage/queue/CDN systems is an automatic safety blocker.

## Non-compensating rubric

Each critical dimension must independently reach competent. Strong prose cannot compensate for unsafe practice or missing executable/design evidence.

| Dimension | Developing | Competent | Transfer-ready evidence | Critical |
|---|---|---|---|---|
| Bounded property and question | “Secure boundary” or control slogan | Property, capability, scope/time, forbidden effect, and evidence are explicit | Correctly revises multiple properties under asynchronous hostile-byte processing | yes |
| Boundary and vocabulary precision | Lines follow networks/boxes; terms collapse | Assumption changes distinguish actor, principal, component, channel, flow, entry, enforcement, and isolation | Finds non-network boundary and stored/delayed entry points in PreviewForge | yes |
| Property-relative TCB and transitive trust | “Backend/cloud is trusted” | Property-specific must-be-correct set, dependency chain, residual, and changed TCB are reviewable | Recomputes containment/availability/accountability TCBs and challenges risky parser/provider trust | yes |
| Attack-surface completeness | Ports/endpoints/CVEs/products listed | Flow/effect-derived public, worker, state, output, evidence, shared, configuration paths with closure/residual | Discovers delayed, parser, retry, cache, egress, update, and control paths | yes |
| Common mechanisms and defense depth | Counts controls/products | Fault-specific dependency table; correlated/partial/unknown claims; no unsupported risk multiplication | Predicts non-obvious shared parser/capacity/operator/evidence failures and reduces one responsibly | yes |
| Isolation and blast radius | Names container/tenant column; “limited” | Tenant/object/action/field/time/egress/resource/control/evidence dimensions with mechanisms and residuals | Rebuilds blast-radius argument for hostile converter and persistent output | yes |
| Causal diagnosis | Names header spoofing or failed test | Separates invariant, preconditions, trigger, root cause, impact, prevention, detection, recovery, residual across intended failures | Compares repairs and predicts new paths/state failures | yes |
| Structural repair and mediation | Filters/renames/duplicates same assertion | Trusted provenance, narrow current grant, fail-safe unknowns, effect-before-output mediation, valid behavior preserved | Adapts provenance/authority/isolation/publication to async object pipeline | yes |
| Verification and feedback | Green tests or statuses | Five modes, exact state/output/evidence oracles, surface trace, counterfactual, policy vs enforcement distinction | Evidence predicts duplication, partial output, egress, resource, cache, and withdrawal behavior | yes |
| Operations and human factors | “Log and alert”; restart/revoke | Privacy-safe evidence, signal rationale, outage behavior, bounded containment/recovery, artifact refresh, accessible operation | Handles persistent outputs, queue lifecycle, converter failure, cache invalidation, and honest uncertainty | yes |
| Standards accuracy | Unversioned V15/OWASP mandate/compliance claim | Exact 5.0.0 IDs within scope, Level 3 labeled, Saltzer and Four Questions represented accurately | Uses resource/isolation anchors to expose changed availability/containment obligations without tool prescription | no |
| Safety and assurance scope | Live target/data/payload or production claim | Local synthetic execution, clear setup/reset/limits, narrow conclusion | Transfer remains inert while producing realistic design/evidence obligations | yes |
| Editorial and communication integrity | Ambiguous diagram, examiner leakage, hidden residuals | Traceable accessible artifacts, learner/examiner separation, explicit unknowns and owners | Communicates changed assumptions and residuals to technical/operational audiences | no |

## Mastery decisions

- **Not attempted:** required evidence is absent.
- **Developing:** meaningful work exists, but one or more critical dimensions are below competent.
- **Competent:** every critical dimension is competent; knowledge check is at least 80% after retry; lab and scope evidence are correct.
- **Transfer-ready:** competent plus the PreviewForge pack materially reconstructs properties, state, boundaries, TCBs, surfaces, independence, blast radius, evidence, and operations. It is not awarded for renamed SecureCollab artifacts.

Any live-target action, real sensitive data/credential use, harmful payload creation, examiner-answer copying, fabricated test result, or broad production/compliance claim blocks the submission regardless of other scores.
