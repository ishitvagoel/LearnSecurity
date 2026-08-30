# 1.3 — Trust boundaries and attack surface

Pass A specification. This file defines the coverage contract; lesson prose, runnable implementations, learner answers, and examiner anchors live in their designated Pass B/C files.

## Identity

- **id:** 1.3
- **slug:** trust-boundaries-and-attack-surface
- **title:** Trust boundaries and attack surface
- **phase / track / difficulty:** 1 / core / foundation
- **estimatedMinutes:** 480
- **prerequisites:** Module 1.1 invariant catalogue; Module 1.2 authority map and access matrix; entry-profile API, Git, test, and SQL familiarity. Module 0.1 vocabulary is recommended, not blocking.
- **routeTags:** complete, accelerated, web-api, mobile
- **releaseMilestone:** none. The model is a design artifact, not M0 runtime evidence.
- **masteryGate:** contributes to Gate 1 but cannot complete it alone.

## Scope and assurance boundary

The in-scope system is the **SecureCollab Phase 1 design**: hostile browser/request data, a conceptual public ingress, application adapters and enforcement, the Phase 1 note/membership store, a local illustrative export-worker handoff, and a security-evidence sink. Identity provider, email, object storage, CDN, queues, production networking, cloud control planes, backups, analytics, and mobile clients are modeled as deferred dependencies or change triggers, not claimed implementations.

The module teaches how to construct and challenge a security representation. It does not certify a deployment, teach a full STRIDE or LINDDUN workshop, prove cryptographic service identity, configure containers, build production queues, or authorize testing of any live system. Those limits must remain visible in every learner artifact.

## Objective hierarchy and coverage contract

1. **Define a boundary from a protected property.**
   - State the invariant, attacker/failure capability, scope, and time window first.
   - Identify where security assumptions or capabilities change.
   - Distinguish actor, principal, component, channel, data flow, entry point, enforcement point, isolation boundary, and trust boundary.
   - Explain why a network hop can cross no relevant trust boundary and why an in-process call can cross one.
2. **Scope a property-relative trusted computing base (TCB).**
   - List only components and assumptions that must be correct for the stated property.
   - Recompute the TCB for confidentiality, integrity/authority, availability, and accountability claims.
   - Mark transitive provider/operator/build/evidence dependencies and explicit residuals.
3. **Model SecureCollab Phase 1.**
   - Annotate assets, actors, flows, boundaries, entry points, enforcement points, trusted attribute sources, shared mechanisms, and deferred components.
   - Trace Module 1.2 authority cells to actual effect paths rather than placing one generic “authorization” label inside the API.
   - State direction, data/control content, attacker control, protocol/representation assumptions, and failure behavior for every in-scope flow.
4. **Derive the attack surface from flows and effects.**
   - Include public, administrative, machine, stored-input, aggregate, retry/replay, evidence, and control-plane influence paths when in scope.
   - Link every surface row to a protected effect, boundary, enforcement point, shared dependency, evidence oracle, and residual.
   - Reject endpoint-only, port-only, product-only, CVE-only, and awareness-list inventories as incomplete.
5. **Analyze transitive trust, shared mechanisms, and blast radius.**
   - Follow trust dependencies until the claim reaches an explicit residual or later-module boundary.
   - Identify common parsers, credentials, identities, configurations, runtimes, stores, operators, and evidence paths.
   - Bound compromise by tenant, action, object set, time, egress, data sensitivity, control plane, and evidence suppression.
6. **Diagnose and repair a boundary failure structurally.**
   - Separate invariant, preconditions, trigger, root cause, impact, prevention, detection, recovery, and residual risk.
   - Replace requester-asserted worker identity/scope with trusted-adapter provenance and a narrowly scoped local capability.
   - Deny unknown, missing, malformed, expired, replayed, or evidence-failed context before the protected effect.
   - Compare rejected fixes such as stripping one header, checking a private address, renaming the route, duplicating the same check, or signing an overbroad assertion.
7. **Make assurance and operations falsifiable.**
   - Produce normal, negative, abuse, failure, and counterfactual evidence.
   - Distinguish a passing decision unit from enforcement coverage and a local proof from a production guarantee.
   - Define privacy-safe evidence, drift/misuse signals, evidence-outage behavior, narrow containment, root-cause recovery, and model-refresh triggers.
8. **Transfer to PreviewForge.**
   - Rebuild the model for hostile document bytes, object storage, asynchronous conversion, shared parser libraries, previews, moderation, egress, and retry state.
   - Identify at least four SecureCollab assumptions that no longer hold.
   - Revise the TCB, surface inventory, isolation argument, blast-radius claim, evidence plan, and review triggers rather than renaming boxes.

For every outcome, Pass B must contain explanation, a worked SecureCollab example, learner practice with success criteria, a misconception counterexample, and a PreviewForge transfer hook. Pass C must require observable evidence. A glossary mention or unassessed paragraph does not satisfy coverage.

## Prerequisite concepts

- **1.1:** an invariant is a bounded claim with asset, property, attacker capability, scope, time, forbidden outcome, and evidence.
- **1.2:** authority is a current subject–action–object decision based on trusted state and explicit grants; authentication is not authorization; enforcement coverage matters as much as policy correctness.
- **Entry profile:** the learner can read a small Python module and pytest output, reason about an API/data-store diagram, and edit local text artifacts.

This module deliberately delays full threat enumeration taxonomies to 3.2. The OWASP Four Questions organize the reasoning, but no particular diagramming tool or elicitation method is mandatory.

## Misconceptions to surface and correct

1. Every arrow, TLS hop, process, container, subnet, or cloud account is automatically a trust boundary.
2. The TCB is a fixed box called “backend,” “internal network,” or “cloud provider.”
3. The attack surface is the number of ports/endpoints or a list of CVEs/OWASP Top 10 categories.
4. Internal-sounding headers, private IPs, service labels, route names, or a signed-but-unscoped message prove caller authority.
5. A WAF plus an API check is independent depth when both trust the same parsed field or configuration.
6. Two controls always halve risk; common credentials, code, operators, vendors, and evidence paths do not matter.
7. A tenant column, container, queue, or sandbox proves isolation and limits blast radius without an effect-level argument.
8. Logs are outside the attack surface because they are defensive, and a missing evidence sink can safely be ignored.
9. A diagram is complete when all deployed components are boxes, even if flows, attacker control, assumptions, and enforcement are absent.
10. Threat modeling is a one-time document rather than a change- and incident-driven reasoning process.

## Concept map

```text
bounded property + attacker/failure capability + scope/time
  -> security assumptions and protected effects
     -> flows that may influence those effects
        -> trust boundaries where assumptions/capabilities change
           -> entry points and enforcement points
              -> flow-derived attack surface
                 -> TCB components that must be correct for this property
                    -> transitive trust and shared mechanisms
                       -> correlated failure and isolation analysis
                          -> bounded blast radius
                             -> evidence, operations, and refresh triggers
```

Important non-equivalences:

- `component != actor != principal`
- `data flow != channel != entry point`
- `network boundary != trust boundary`
- `trusted input != valid input`
- `TCB != everything deployed`
- `isolation mechanism != proven isolation property`
- `additional control != independent defensive layer`
- `inventory row != mitigation`

## Invariant prompts

- What exact confidentiality, integrity/authority, availability, or accountability property must remain true?
- Who or what may be hostile, compromised, mistaken, stale, unavailable, reordered, or replayed?
- Which effect must never occur, and for which tenant, object, action, state, and time?
- Which values may the untrusted side choose? Which facts must the trusted side derive independently?
- What component must be correct for this property? Would it still be in the TCB for a different property?
- If evidence is absent, late, forged, or suppressed, does the protected effect proceed, buffer, or deny?
- What explicit residual remains outside this module’s proof?

## Threat-model prompts

Use OWASP’s methodology-neutral Four Questions:

1. **What are we working on?** State scope, property, actors, dependencies, flows, boundaries, entry points, trusted sources, state, time, and assumptions.
2. **What can go wrong?** Challenge each flow and shared mechanism with attacker control, substitution, replay, widening, alternate path, dependency failure, and evidence suppression.
3. **What are we going to do?** Choose structural prevention, detection, recovery, ownership, evidence, and explicit residuals. Avoid naming a product without a property argument.
4. **Did we do a good enough job?** Use five evidence modes, trace every in-scope effect, remove or bypass a control in a counterfactual, and schedule refresh on meaningful change or incident.

## Required artifact schemas

### Boundary diagram annotation

Every flow identifier must record: source actor/principal and component; destination; direction; data/control content; attacker-controlled fields; changed assumption/capability; entry point; enforcement point; trusted attribute source; shared dependencies; failure behavior; protected effect; evidence; residual; and lifecycle/change trigger.

### Attack-surface inventory

| Surface / flow | Reachable actor or failure | Controlled input or state | Boundary and entry point | Protected effect | Enforcement / trusted source | Shared mechanism | Blast radius | Oracle / evidence | Residual / owner |
|---|---|---|---|---|---|---|---|---|---|

Every row must be derived from an in-scope flow or shared mechanism. A deferred surface is labeled deferred with a review trigger; it is never silently described as protected.

### Independence claim

For each alleged layer, record its function (prevent/detect/recover), decision input, parser/code, identity/credential, configuration/control plane, runtime/failure domain, operator/vendor, evidence path, bypass path, and behavior when the adjacent layer fails. Classify the pair as independent for the stated failure, partially independent, correlated, or unknown. “Different products” is not evidence.

### Blast-radius statement

State the compromised capability; reachable tenants/objects/actions; read/write/execute/egress effects; time and retry window; ability to change policy or evidence; containment control; evidence; and residual. Do not use “limited” without dimensions.

## Lesson inventory

| Object id | Kind | Title | Loop step | Principal evidence |
|---|---|---|---|---|
| 1.3-LO-01 | concept-model | Boundaries are changes in assumptions, not lines around servers | 1 Property | Definitions, property-relative TCB worksheet, counterexamples |
| 1.3-LO-02 | design-exercise | Build the SecureCollab boundary and attack-surface model | 2 Model | Annotated diagram, flow ledger, surface inventory, dependency/independence table |
| 1.3-LO-03 | break-fix-lab | Break the forged worker-provenance boundary locally | 3 Break | Exact vulnerable results and causal traces in authorized fixture |
| 1.3-LO-04 | design-exercise | Restore trusted provenance and bound the export blast radius | 4 Build | Structural repair decision record and fixed comparison |
| 1.3-LO-05 | verification-lab | Prove the boundary claim across five evidence modes | 5 Verify | Traceability matrix and counterfactual evidence |
| 1.3-LO-06 | operations-exercise | Detect boundary drift and recover from crossed assumptions | 6 Operate | Evidence contract, signals, runbook, refresh decision |
| 1.3-LO-07 | transfer-challenge | Transfer the method to the PreviewForge document pipeline | 7 Generalize | New model, comparison memo, revised TCB/surface/blast radius |
| 1.3-LO-08 | code-review | Review a plausible but dishonest boundary design | 5 Verify | Actionable review comments and corrected design |

## Lab brief

**Lab:** `labs/1.3/1.3-trust-boundaries`

- **Authorized scope:** in-process Python course fixture and synthetic SecureCollab tenants, notes, requests, capabilities, and evidence only. No network listener or outbound call.
- **Property:** only a trusted worker adapter may construct worker provenance, and the export effect requires a current, single-use capability bound to caller kind, worker identity, tenant, action, and object set. Unknown or failed context denies.
- **Vulnerable mechanism:** public and worker calls share one adapter; requester-controlled header/service/tenant fields become provenance; the edge and application repeat the same trust assumption; an overbroad reusable worker path widens scope.
- **Structural repair:** separate public and worker adapters; make trusted context non-constructible from public fields; consume a server-held, tenant/action/object-scoped capability; enforce immediately before effect; produce bounded evidence.
- **Forbidden outcomes:** public promotion to worker; tenant/action/object widening; replay; unknown/failure allow; correlated layers presented as independent; live-target or harmful practice.
- **Evidence modes:** normal, negative, abuse, failure, counterfactual; explicit unchanged-output or denied-decision oracles.
- **Reset:** a fresh module state per test; learner mutations occur only in a disposable copy.
- **Limits:** no HTTP stack, TLS, cryptographic service identity, persistent queue, database transaction, sandbox, real worker, cloud IAM, production logging, or proof of end-to-end deployment assurance.

## Assessment blueprint

| Category | What is assessed | Required artifact |
|---|---|---|
| Explain | Exact distinctions among boundary, TCB, entry point, channel, attack surface, transitive trust, isolation, blast radius, and defense independence | Bounded definitions and two counterexamples |
| Design | Coverage of SecureCollab flows, effects, trusted sources, dependencies, shared mechanisms, and residuals | Diagram, flow ledger, surface inventory, dependency and independence analysis |
| Build | Trusted provenance and narrow worker capability at the effect boundary | Local patch/design record with rejected repairs |
| Break | Causal account of forged provenance, widening, replay, alternate path, and shared-assumption failures | Intended vulnerable results and causal worksheet |
| Verify | Evidence that can falsify each claim and distinguish policy correctness from enforcement coverage | Five-mode trace matrix and counterfactual |
| Operate | Detect drift/misuse without leaking content; behave deliberately on evidence failure; contain and recover | Evidence contract, signal rationale, response/runbook, refresh trigger |
| Communicate | Honest scope, transitive trust, correlation, blast radius, later work, and accessibility | Diagram legend, residual memo, incident/change summary |

Critical dimensions are non-compensating: bounded property, model completeness, causal diagnosis, structural repair, evidence traceability, operations, authorized scope, and material transfer must each be competent. Knowledge answers cannot compensate for unsafe or missing practical evidence. Transfer-ready is reserved for demonstrated PreviewForge reconstruction; authored curriculum status remains competent until learner evidence exists.

## Standards references

| Source | Version / status | Exact use | URL |
|---|---|---|---|
| OWASP Threat Modeling Project | maintained-project-guidance / final | Four Questions as a methodology-neutral starting point; system representations, assumptions, validation, and lifecycle refinement | https://owasp.org/www-project-threat-modeling/ |
| OWASP ASVS | 5.0.0 / final | `v5.0.0-15.1.3` resource-demand documentation; `v5.0.0-15.2.2` availability defenses; `v5.0.0-15.2.5` advanced isolation around dangerous/risky components; `v5.0.0-15.3.4` trusted, non-user-manipulable proxy provenance | https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x24-V15-Secure-Coding-and-Architecture.md |
| Saltzer & Schroeder | 1975 / seminal | Economy of mechanism, fail-safe defaults, complete mediation, and least common mechanism as design reasoning | https://web.mit.edu/Saltzer/www/publications/protection/Basic.html |

Pins were live-checked on 2026-08-29 in `content/standards/pins.yaml`. ASVS Level 3 requirement `v5.0.0-15.2.5` is an explicit advanced anchor, not an undisclosed baseline. The module does not claim that these four requirements cover all boundary or architecture verification, that ASVS prescribes this fixture, or that Saltzer principles are auditable compliance clauses.

## Review triggers

Refresh the model when any protected property, attacker capability, actor/principal, authority source, component, flow, entry point, protocol, representation, parser, dependency, shared mechanism, isolation claim, credential, egress path, evidence path, operational owner, or time/retry behavior changes. Refresh after an incident or test finding even if the visible architecture diagram did not change. Record which 1.1 invariant, 1.2 matrix cell, boundary row, oracle, and response step became stale.

## Time budget and SecureCollab / milestone dependencies

| Work | Minutes |
|---|---:|
| Property, vocabulary, and TCB reasoning | 55 |
| SecureCollab diagram, flow ledger, and surface inventory | 80 |
| Authorized break analysis | 55 |
| Structural repair and alternatives | 60 |
| Five-mode verification | 55 |
| Operations and refresh | 50 |
| PreviewForge transfer | 75 |
| Seeded review and assessment synthesis | 50 |
| **Total** | **480** |

This module feeds Gate 1 with design evidence only. Module 1.4 adds risk prioritization. Phase 2 adds real request-path behavior, Phase 3 expands formal threat elicitation, Phase 7 adds real asynchronous workers, Phase 8 treats hostile clients in depth, and Phase 10 handles production architecture/incident concerns. No milestone or mastery gate changes state merely because these learning artifacts are published.

## Operational considerations

- Evidence must identify boundary decision and model version without copying note content, export bodies, credentials, raw tokens, or unnecessary personal attributes.
- A signal needs a defined window, threshold rationale, owner, accessible investigation path, and false-positive/false-negative trade-off.
- Evidence-pipeline failure is a modeled security state: block, buffer, or explicitly degrade according to the effect’s risk; do not silently continue and still claim detection.
- Containment starts with the narrow caller, capability class, tenant, action, adapter, or egress path; investigation expands to all alternate paths and common mechanisms sharing the failed assumption.
- Recovery repairs the assumption and enforcement path, revokes/rotates affected authority, reconciles state and released outputs, restores evidence, retests all five modes, and updates the model.
- Human-readable models and incident actions cannot depend on color alone and must remain usable by keyboard and assistive technology.
- Provider, operator, build, backup, and control-plane trust must be explicit residual or named later work.

## Changelog

| Date | Note |
|---|---|
| 2026-08-23 | Initial Pass A specification and early Pass B/C material |
| 2026-08-24 | First publishability-oriented rewrite |
| 2026-08-29 | Replaced shallow chapter coverage with an eight-outcome contract, exact standards mappings, structural provenance lab, five-mode evidence, operations lifecycle, and material PreviewForge transfer |
| 2026-08-29 | Spiral revisit replaced the boundary stub and requires 1.1 invariant plus 1.2 worker/export authority review when real ingress, queue, persistence, evidence, or service identity changes enter scope |
