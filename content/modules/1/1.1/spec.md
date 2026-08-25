# Module 1.1 specification — Security as invariants under attack

This specification is the publishable-depth reference for the remediation queue. It remains subordinate to blueprint revision 1.1 and does not introduce a parallel syllabus.

## Identity

- **ID:** 1.1
- **Phase / track / difficulty:** 1 / core / foundation
- **Estimated effort:** 420 focused minutes
- **Prerequisite:** entry profile—small database-backed API, Git, tests, and basic SQL; Module 0.1 vocabulary is recommended
- **Routes:** complete, accelerated, web-api, mobile
- **Mastery contribution:** Gate 1
- **SecureCollab state:** Phase 1 product model only; no production service or M0 evidence

## Purpose

The learner must stop treating security as a list of products, settings, vulnerabilities, or framework defaults. They will define security as bounded system outcomes that remain true under stated adversarial and failure conditions, derive candidate mechanisms from those outcomes, identify mechanism limits, specify evidence, and preserve detection/recovery when prevention is incomplete.

The module uses SecureCollab’s first product model and a local semantic-linting lab. It does not claim that an application implementation exists.

## Outcomes

By the end of the module, the learner can:

1. produce a versioned SecureCollab invariant catalogue with at least five testable, system-specific rows;
2. separate a desired property from mechanisms, mechanism limits, framework defaults, and evidence;
3. bound each claim with assets, subjects/actions, attacker capabilities, trusted and untrusted components, state, time, forbidden outcomes, residual risk, and review triggers;
4. distinguish root cause, preconditions, impact, prevention, detection, and recovery for a mechanism-only assurance failure;
5. specify normal, negative, abuse, and failure evidence without treating control presence as proof;
6. design privacy-safe operational evidence and a bounded response/recovery path;
7. transfer the catalogue method to a materially changed product and explain which original claims fail.

## Coverage contract

Every outcome must have all five evidence types before publication.

| Outcome | Explanation and model | Worked reasoning | Learner practice | Assessment evidence | Transfer |
|---|---|---|---|---|---|
| 1 | LO-01 claim envelope; LO-02 product/state model | LO-02 confidentiality-row interrogation | Five-row catalogue and peer classification | Catalogue dimensions in rubric | CivicClinic six-row catalogue |
| 2 | LO-01 property/mechanism distinction | Hashed-password causal trace; logging alternatives in LO-04 | Slogan-to-bounded-claim rewrite | Mechanism-limit and counterexample criteria | Signed worker-token review |
| 3 | LO-01 claim envelope; LO-02 actor/state tables | Bounded confidentiality example | Full row template and peer challenge | Model completeness is critical | Changed guardian/vendor/shared-device assumptions |
| 4 | LO-03 causal diagnostic table | Vulnerable fixture diagnosis | Annotated SECURITY.md and failure grouping | Seeded review and examiner findings | Alternate mechanism slogan |
| 5 | LO-05 oracle and evidence modes | Cross-tenant evidence trace | Forbidden-outcome matrix | Four evidence modes required | Evidence revised for delegated/time-dependent actions |
| 6 | LO-06 event-to-response sequence | Privacy-safe authorization event | Operate paragraph | Detection/recovery and human factors | Worker/webhook operational delta |
| 7 | LO-07 changed-system analysis | Comparison categories | Independent transfer deliverable | Transfer-ready criteria | CivicClinic is the transfer case |

Missing explanation, practice, assessment, or transfer evidence for an outcome blocks publishable depth.

## Core model

A security claim is represented as:

1. **Asset and required outcome**
2. **Subject, action, object, and allowed condition**
3. **Attacker capabilities**
4. **Trusted and explicitly untrusted components**
5. **Relevant state and time horizon**
6. **Forbidden observable outcome**
7. **Candidate mechanisms and their limits**
8. **Normal, negative, abuse, and failure evidence**
9. **Detection, response, and recovery**
10. **Residual risk, non-goals, and review triggers**

The model distinguishes confidentiality, integrity, availability, authenticity, authorization, accountability, privacy, and safety as prompts rather than universal checkboxes. A learner may omit a property only by recording a reasoned non-goal and review trigger.

## SecureCollab Phase 1 model

### Included now

- tenants and tenant membership;
- tenant members and administrators;
- text notes;
- privacy-safe security events;
- request, retained-log, export, deletion, and restore time horizons as design concerns.

### Deferred and review-triggering

- files and public sharing;
- support impersonation;
- background workers, webhooks, queues, and caches;
- billing simulation;
- offline mobile state;
- production deployment, real PII, real payments, and cloud-administrator assurance.

### Minimum adversaries

- unauthenticated internet client;
- authenticated cross-tenant member with a fully controlled browser;
- stale or over-privileged tenant administrator;
- faulty or abusive authorized client;
- operator with ordinary log access;
- privileged infrastructure administrator as a recorded residual-risk case.

### Intended trusted computing base

The model may depend on a server-side policy path, persistence transaction, structured event constructor, and evidence store for narrowly stated behaviors. Browser claims, client-supplied tenant labels, UI visibility, scanner status, and mechanism secrecy are never trusted enforcement.

Modules 1.2 and 1.3 refine authority and boundaries; this module must not pre-claim their implementation evidence.

## Misconceptions to diagnose

- Security is a Top 10, CWE, CVE, scanner, certification, or product list.
- CIA labels are complete without product-specific assets and harms.
- TLS, JWT, password hashing, encryption, validation, or logging is itself the property.
- Authentication implies authorization.
- A successful happy path or status code proves the invariant.
- Configuration presence proves alternate and failure paths.
- Privacy equals confidentiality; safety equals availability.
- “Always” and “never” need no channel, time, or trust boundary.
- Prevention eliminates the need for privacy-safe evidence and recovery.
- A generated reviewer stamp or schema-valid file is independent semantic review.

## Seven-step learning inventory

| Object | Kind | Learning-loop role | Output |
|---|---|---|---|
| 1.1-LO-01 | concept-model | Property | Bounded claim rewrite |
| 1.1-LO-02 | design-exercise | Model | SecureCollab invariant catalogue |
| 1.1-LO-03 | mechanism-lab | Break | Causal diagnosis and vulnerable/fixed lab evidence |
| 1.1-LO-04 | design-exercise | Build | Property-derived mechanism design record |
| 1.1-LO-05 | verification-lab | Verify | Four-mode forbidden-outcome matrix |
| 1.1-LO-06 | operations-exercise | Operate | Privacy-safe detection/response/recovery section |
| 1.1-LO-07 | transfer-challenge | Generalize | CivicClinic catalogue and comparison memo |
| 1.1-LO-08 | code-review | Verify/communicate | Actionable review of mechanism-only claims |

The sequence reduces scaffolding: LO-01 models the method, LO-02 guides construction, LO-03/04/05 challenge and repair it, LO-06 extends it operationally, and LO-07 requires independent transfer.

## Lab contract

**Path:** labs/1.1/1.1-invariant-catalogue

**Authorized scope:** local course files and synthetic SecureCollab data only. No service is started and no network target is needed.

**Invariant:** a submitted catalogue is bounded and semantically shaped for independent review rather than being a mechanism slogan.

**Vulnerable behavior:** a universal security conclusion, public-target text, insufficient catalogue rows, and missing model/evidence/operation fields cause the selected-catalogue test to fail.

**Fixed behavior:** five module-specific claims pass semantic and safety checks.

**Structural fix:** versioned claim records connect product model, forbidden outcome, mechanism limits, four evidence modes, detection/recovery, residual risk, and review triggers.

**Limits:** the validator detects selected defects. Passing it is not proof that an implementation exists or satisfies the catalogue.

**Clean-run requirement:** record exact vulnerable-fail and fixed-pass commands in the independent review artifact.

## Assessment architecture

Critical dimensions are:

- bounded property and product model;
- attacker/trust/state/time;
- causal property-to-mechanism reasoning;
- forbidden-outcome and four-mode evidence;
- safe lab interpretation;
- operations and residual risk;
- materially changed transfer.

Every critical dimension must be satisfactory; scores do not compensate. Knowledge checks may be retryable at 80%, but practical evidence controls Gate 1 contribution. Transfer-ready requires satisfactory CivicClinic evidence and an explanation of which SecureCollab assumptions fail.

Learner prompts remain under this module’s assessment directory. Intended findings and examples remain only under content/assessment/keys/1.1.md.

## Standards

- **Saltzer and Schroeder, 1975, seminal:** exact named principles—economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability, work factor, and compromise recording. These principles critique mechanisms; they do not prove a system property.
- **NIST CSF 2.0, final:** GV, ID, PR, DE, RS, and RC are outcome functions. They help prevent a prevention-only catalogue but are not a verification baseline.
- **ASVS 5.0.0:** intentionally not mapped at requirement level in this first-principles module. Later implementation modules map exact verification requirements; adding unrelated ASVS IDs here would be compliance theater.

Canonical pins are recorded in content/standards/pins.yaml and were reviewed on 2026-08-25.

## Review triggers

Reopen the module when:

- SecureCollab gains a new asset, principal, boundary, state transition, channel, or time horizon;
- the lab validator begins passing mechanism slogans or rejecting bounded claims for superficial reasons;
- a standards source changes status or version;
- human recovery, operator compromise, or accessibility assumptions change;
- generated prose or automated stamps are proposed as review evidence;
- the curriculum is reorganized around an awareness list.

## Publishability decision

Publication requires schema validity, the clean vulnerable/fixed lab pair, semantic scores of at least 2 on every required quality dimension, no critical blocker, an independent quality review, an independent lab-safety review, and a dated review artifact. STATUS is updated only after that evidence exists.

## Changelog

| Date | Change |
|---|---|
| 2026-08-23 | Pass A specification and initial Pass B/C pilot |
| 2026-08-25 | Rebuilt as the semantic-depth reference with coverage contract, causal lessons, executable semantic lab, aligned assessment, and independent-review requirement |
