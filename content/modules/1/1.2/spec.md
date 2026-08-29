# Module 1.2 specification — Authority and protection

This specification deepens the existing blueprint module. It remains subordinate to curriculum blueprint revision 1.1 and uses Module 1.1 as the instructional-density reference.

## Identity

- **ID:** 1.2
- **Phase / track / difficulty:** 1 / core / foundation
- **Estimated effort:** 480 focused minutes
- **Prerequisite:** Module 1.1’s bounded-invariant method; entry-profile ability to read small Python programs and tests
- **Routes:** complete, accelerated, web-api, mobile
- **Mastery contribution:** Gate 1
- **SecureCollab state:** Phase 1 authority design and a local synthetic policy fixture; no production service or milestone evidence

## Purpose

The learner must replace vague statements such as “members can access notes” or “admins can do anything” with an authority model that can be reviewed, implemented, tested, revoked, and revised. They learn to ask not merely who a requester is, but which subject is acting, on which object, through which action and path, using which grant, in which state, and for how long.

The module treats an access matrix as an abstract relation rather than a spreadsheet-shaped implementation. Roles, ACLs, relationship rules, capabilities, middleware, database privileges, and policy engines are possible representations or enforcement mechanisms. None is the property. The required property is that only explicitly authorized effects occur, every relevant path is mediated, authority attenuates when delegated, and uncertainty does not silently become permission.

SecureCollab remains a design model. The executable lab is an isolated Python policy fixture with synthetic tenants, users, and notes. Passing it is evidence about the selected authority rules, not proof that a web application or database is secure.

## Outcomes

By the end of the module, the learner can:

1. produce a reviewable SecureCollab authority map and access matrix whose cells name subject, object, action, decision, conditions, source of authority, and time;
2. distinguish authentication, authorization, roles, ACLs, capabilities, delegation, and ambient authority without treating any representation as a complete guarantee;
3. derive least privilege, fail-safe defaults, complete mediation, separation of privilege, and secure initial states from system-specific forbidden outcomes;
4. diagnose direct, aggregate, administrative, stale-authority, and unknown-policy failures by separating root cause, preconditions, trigger, impact, prevention, detection, and recovery;
5. implement or explain a small trusted policy path that resolves server-controlled subject and object attributes, denies unknown cases, and is invoked by every in-scope operation;
6. turn matrix cells and authority-lifecycle transitions into normal, negative, abuse, and failure tests, including a counterfactual that proves the enforcement path matters;
7. design privacy-safe grant, use, denial, expiry, revocation, break-glass, and recovery evidence with usable administrative journeys;
8. transfer the model to a release-approval system with a machine principal, two-person approval, artifact binding, and time-bounded execution, explaining which SecureCollab assumptions no longer hold.

## Coverage contract

Every outcome needs all five evidence forms before the module can be published.

| Outcome | Explanation and model | Worked reasoning | Learner practice | Assessment evidence | Material transfer |
|---|---|---|---|---|---|
| 1 | LO-01 authorization tuple; LO-02 authority map and matrix | Alice/Bob/admin cells traced from invariant to decision | Complete Phase 1 matrix with direct and indirect paths | Matrix completeness and executability rubric | ReleaseDesk subject–artifact–environment matrix |
| 2 | LO-01 representation comparison | Guessable note ID contrasted with a capability; role compression counterexample | Classify six claims as identity, authority, mechanism, or ambient authority | Knowledge check plus design defense | CI job message and approver grant analysis |
| 3 | LO-01 principle derivation; LO-04 structural repair | Unknown action, cross-tenant admin, and bulk-export approval cases | Derive one mechanism per forbidden outcome and reject two alternatives | Design record and lab causal trace | Two-person production execution with bounded emergency path |
| 4 | LO-03 local break and causal worksheet | Five vulnerable paths grouped by missing mediation, overbroad role, stale state, or fail-open default | Annotate vulnerable code and failure output before viewing the fixed tree | Seeded review and examiner finding set | Identify the new root causes created by automation and delayed execution |
| 5 | LO-04 policy/enforcement architecture | Policy decision versus enforcement-point bypass; origin subject versus service identity | Draft a policy decision and enforcement inventory | Build evidence and actionable review comments | Bind approved artifact and environment to execution authority |
| 6 | LO-05 four-mode evidence | Matrix-to-test derivation and policy-removal counterfactual | Expand test matrix across subject/object/action/state | Lab record, test rationale, and residual gaps | Approval expiry, replay, revocation, and worker substitution tests |
| 7 | LO-06 authority lifecycle and human factors | Privacy-safe decision event and stale-cache response sequence | Write grant/revocation runbook and accessible break-glass flow | Operate evidence with non-compensating critical criteria | Incident override, independent evidence, and post-use revocation |
| 8 | LO-07 independent transfer | Comparison of changed actors, objects, state, time, and harm | Produce ReleaseDesk map without copying SecureCollab role names | Transfer-ready comparison memo | ReleaseDesk is the assessed changed system |

Missing explanation, worked reasoning, practice, assessment, or transfer evidence for any outcome is a publication blocker.

## Core authority model

An authorization decision is modeled as:

```text
decision = policy(
  originating_subject,
  effective_subject,
  action,
  object,
  object_state,
  grant_or_delegation,
  trusted_context,
  time
)
```

The decision is `allow` only when a positive rule establishes authority. It also records a stable reason and policy version for evidence. Every other case—including unknown subject, object, action, grant, policy error, stale membership, and failed attribute resolution—denies for this module’s scope.

The access matrix is the conceptual relation between subjects, objects, and allowed actions. It can be represented by:

- an object-centered ACL;
- a subject-held, unforgeable and scoped capability;
- role, relationship, or attribute rules that compress many cells;
- database or operating-system enforcement;
- an application policy service.

The representation is correct only insofar as every allowed cell has justified authority and every forbidden cell remains unreachable through all in-scope paths.

### Delegation contract

Delegation must not create authority from nothing. A grant records issuer, grantee, action, object or scope, constraints, issue time, expiry, revocation state, and whether further delegation is permitted. The delegated authority is no broader than the issuer’s authority at issue and use time unless a separately justified policy explicitly says otherwise. Copyability, audience binding, replay, and revocation are mechanism-specific proof obligations.

### Complete-mediation contract

The same policy meaning must govern direct reads, list and search results, bulk export, administrative routes, background work, retries, restore, cache hits, and maintenance paths when those paths enter scope. A central policy function does not prove complete mediation if an operation can reach protected state without calling it, supplies attacker-controlled attributes, or reuses a stale decision after authority changes.

## SecureCollab Phase 1 authority scope

### Current design subjects

- tenant member, bound to one active tenant membership;
- tenant administrator, privileged only inside the bound tenant;
- unauthenticated requester, with no note or membership authority;
- API policy and enforcement path as a narrowly defined trusted component.

### Current design objects

- tenant record;
- membership record;
- note identifier, summary metadata, and note body as separately reviewable fields;
- authority decision event as a protected object.

### Current actions

- list note identifiers or summaries;
- read note body;
- create and update note;
- delete note;
- view membership;
- grant or revoke tenant membership;
- perform a modeled bulk export, explicitly marked as a high-impact design case rather than a shipped feature.

### Deferred and review-triggering principals and paths

- support impersonation and break-glass operators;
- background workers, queues, webhooks, caches, and search indexes;
- files, sharing links, external collaborators, and public resources;
- mobile offline state and device-held authority;
- database administrators, cloud control planes, backups, and production deployment.

These are named holes, not hidden assurances. LO-07 introduces a different machine-principal system for transfer; it does not silently add a SecureCollab product feature.

## Threat and failure model

Minimum cases include:

- an authenticated Tenant B member controlling the browser, identifiers, request order, and client-supplied labels;
- a Tenant A administrator attempting an action on Tenant B because “admin” was treated as global ambient authority;
- a revoked member using a still-valid authentication session or stale cached decision;
- an ordinary developer adding a list, export, admin, GraphQL, worker, or restore path without an enforcement point;
- an operator using a high-impact emergency path, including accidental misuse and evidence failure;
- a policy dependency returning unknown, timing out, or using attributes from the untrusted client;
- a reviewer mistaking an unguessable identifier, hidden button, middleware call, or role name for authority evidence.

## Misconceptions to diagnose

- Authentication proves permission.
- A role is an authority model rather than a lossy compression of matrix cells.
- A UI route or hidden button is an enforcement boundary.
- Random identifiers are capabilities even when knowledge is neither the intended nor the controlled grant.
- One authorization check in an HTTP handler mediates list, export, worker, cache, retry, and restore paths.
- “Admin” is a global boolean whose tenant, action, state, and time need not be modeled.
- A central policy engine guarantees complete mediation regardless of enforcement-point coverage.
- A denylist is fail-safe because known dangerous cases are blocked.
- Delegation may grant whatever the recipient needs even if the issuer lacks it.
- Revocation means removing a UI option; cached or self-contained authority need not change.
- Two clicks by one principal are separation of privilege.
- ASVS, a scanner, or passing tests proves every authorization path is correct.

## Seven-step learning inventory

| Object | Kind | Learning-loop role | Output |
|---|---|---|---|
| 1.2-LO-01 | concept-model | Property | Bounded authorization claim and representation comparison |
| 1.2-LO-02 | design-exercise | Model | SecureCollab authority map and executable access matrix |
| 1.2-LO-03 | mechanism-lab | Break | Causal diagnosis and vulnerable/fixed local evidence |
| 1.2-LO-04 | design-exercise | Build | Policy-decision and enforcement-point design record |
| 1.2-LO-05 | verification-lab | Verify | Four-mode authority test matrix and counterfactual |
| 1.2-LO-06 | operations-exercise | Operate | Grant/revoke/break-glass runbook and evidence schema |
| 1.2-LO-07 | transfer-challenge | Generalize | ReleaseDesk authority model and comparison memo |
| 1.2-LO-08 | code-review | Verify/communicate | Actionable review of ambient and incomplete authority paths |

Scaffolding fades across the sequence: LO-01 supplies vocabulary and a worked trace; LO-02 guides the first matrix; LO-03–LO-05 require diagnosis, repair reasoning, and executable evidence; LO-06 adds lifecycle and human failure; LO-07 is independent transfer.

## Lab contract

**Path:** `labs/1.2/1.2-authority-matrix`

**Authorized scope:** local Python files and synthetic SecureCollab users, tenants, notes, and decisions only. No server, socket, credential, public target, or real person is used.

**Invariant:** every in-scope operation obtains a current server-side decision over subject, object, action, tenant, and relevant authority state; unknown cases deny.

**Vulnerable behavior:** authentication is treated as note-read authority; list returns objects across tenants; an unscoped admin role deletes across tenants; revoked membership remains ambient authority; one approval satisfies an illustrative two-person export rule; and an unknown action fails open.

**Fixed behavior:** one explicit policy path resolves current subject and object state, binds tenant and action, checks two distinct current approvals for the illustrative export case, and denies unknown or failed resolutions. Every operation consumes that decision.

**Structural fix:** replace ambient identity/role fallbacks with positive, current, server-resolved policy rules plus explicit enforcement points. A user-specific denylist, hidden identifier, route naming convention, or test-only patch is insufficient.

**Limits:** the fixture has no HTTP layer, database, cryptographic capability, distributed cache, or production identity. Passing proves only the modeled operations and cases. Later modules must revisit persistence, sessions, workers, and enforcement coverage.

## Assessment architecture

Critical dimensions are:

- explicit authority cells and default-deny gaps;
- authentication/authorization and mechanism/property separation;
- delegation attenuation and authority lifecycle;
- causal diagnosis of ambient and incomplete mediation;
- trusted policy and enforcement-point design;
- normal, negative, abuse, and failure evidence;
- safe local lab interpretation;
- privacy-safe operations and usable recovery;
- materially changed transfer.

Every critical dimension must be satisfactory. Strong prose cannot compensate for a cross-tenant allow cell, a fail-open unknown action, missing revocation, an unsafe lab scope, or a transfer that only renames actors. Knowledge questions may be retried at 80%; practical evidence controls the Gate 1 contribution. Transfer-ready requires satisfactory ReleaseDesk evidence and an explanation of which SecureCollab assumptions fail.

Learner prompts remain under this module’s assessment directory. Intended lab findings, example decisions, and evaluation anchors remain only under `content/assessment/keys/1.2.md`.

## Standards

- **Saltzer and Schroeder, 1975, seminal:** fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability, and compromise recording are exact named principles used as design warnings, not compliance claims.
- **OWASP ASVS 5.0.0, final:** exact scoped references are `v5.0.0-8.1.1`, `v5.0.0-8.1.2`, `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.2.3`, `v5.0.0-8.3.1`, `v5.0.0-8.3.2`, `v5.0.0-8.3.3`, `v5.0.0-8.4.1`, and `v5.0.0-15.3.1`. Level 3 requirements are used as advanced reasoning and transfer anchors, not silently added to every application’s baseline.
- **CISA Secure by Design:** the curriculum snapshot uses secure defaults and manufacturer ownership as product guidance. The canonical page returned HTTP 403 during the 2026-08-25 recheck, so the pin is marked `unverified`; no new version or stronger claim is inferred.

Canonical pins live in `content/standards/pins.yaml`.

## Review triggers

Reopen the module when:

- a new principal, role, delegation type, capability, emergency path, or machine identity is introduced;
- an object gains fields with different read/write rules or a new lifecycle state;
- an operation is reachable through a new route, query shape, cache, worker, retry, import, export, restore, or maintenance path;
- authority is cached, embedded in a token, copied to a device, or evaluated across services;
- revocation timing, policy availability, or evidence durability changes;
- the administrative journey becomes inaccessible, ambiguous, or easier to bypass than to use;
- ASVS or another pinned source changes version or status;
- tests or a central policy library are presented as complete-mediation proof without an enforcement inventory.

## Publishability decision

Publication requires schema validity, vulnerable-fail and fixed-pass lab evidence from a clean environment, semantic scores of at least 2 for every required quality dimension, no critical blocker, independent quality and lab-safety reviews, and a dated review artifact. `STATUS.yaml` is updated last.

## Changelog

| Date | Change |
|---|---|
| 2026-08-23 | Pass A specification and initial Pass B/C generated content |
| 2026-08-25 | Rebuilt coverage contract, authority model, exact ASVS mapping, structural lab contract, assessment architecture, and independent-review requirement |
