# Module 1.1 specification — Security as invariants under attack

This specification is the publishable-depth reference for the remediation queue. It remains subordinate to blueprint revision 1.1 and does not introduce a parallel syllabus.

## Identity

- **ID:** 1.1
- **Phase / track / difficulty:** 1 / core / foundation
- **Estimated effort:** 240 focused minutes
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

## Teaching claims

The module previously carried this same seven-outcome list and the eight-lesson skeleton to teach it, but the lessons that shipped against it (Pass B, 2026-08-25) drifted: only `01-property-vs-mechanism.md` actually addressed SecureCollab's invariant catalogue, and `02`–`08` instead walked through a local password-hashing exercise that matched neither the outcomes above nor `module.yaml`'s actual `labSpec` (`1.1-invariant-catalogue`). All eight lessons averaged 386 words against the 900-word floor, and none carried a fenced worked example. Naming the five falsifiable claims below, and rewriting all eight lessons directly against them, is what this deepening pass replaces that drift with.

1. **C1 — A sentence that names a mechanism is not a security invariant, because the mechanism can be fully present while the outcome it is assumed to guarantee fails elsewhere.** "Passwords are hashed," "we use TLS," and "the scanner is green" can all be true on the day a Tenant B member reads a Tenant A note through a support export none of the three ever touches, because none of the three names an asset, an attacker, or a forbidden outcome that a concrete event could falsify.
2. **C2 — A claim is checkable only once it names every envelope element, and field presence alone does not establish that it does.** A catalogue row can satisfy every schema key, avoid every mechanism-slogan phrase, and still say nothing SecureCollab-specific — five rows reading "notes must never leak," "a bad actor," "the server," "thing works," repeated under five different ids, pass a shape-only or slogan-only check while being one empty claim wearing five identifiers.
3. **C3 — A property is verified only across four distinct evidence modes, and a mode's key being present does not mean its value actually evidences that mode.** Normal-case evidence proves a mechanism works when nobody is trying to defeat it; negative, abuse, and failure evidence each rule out a different way that proof could be hollow, and a control-presence statement ("middleware exists") observes a mechanism, not the forbidden outcome the mechanism is supposed to prevent.
4. **C4 — When prevention is incomplete, the claim must pair a forbidden-outcome check with privacy-safe detection and a bounded, human-usable recovery step, or the claim has stated a limit and then ignored it.** A detection design that logs the exact asset a confidentiality claim protects, "to be thorough," has turned its own evidence trail into a second copy of that asset; a recovery step with no accessible path for the human who has to act on it is a claim about a person who does not exist.
5. **C5 — The catalogue method transfers only when the transfer identifies which SecureCollab-specific assumptions fail under the new system's actors, authority relations, and time horizons; renaming nouns is not transfer.** CivicClinic's guardian delegation is revocable mid-session in a way SecureCollab's tenant membership is not, a shared household phone breaks the one-browser-one-attacker assumption, and human-scheduled appointment capacity does not respond to the same fix as compute-bound availability.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break | `test_mechanism_slogan_is_rejected`, `test_field_presence_alone_does_not_pass` (the vulnerable fixture's forbidden outcome) | items.md #1, #4 |
| C2 | 2 Model, 4 Build | `test_five_padded_duplicate_rows_do_not_pass` (new in this pass — see Lab contract) | items.md #2, #6 |
| C3 | 5 Verify | `test_field_complete_but_causally_shallow_claim_does_not_pass` | items.md #3 |
| C4 | 6 Operate | Not directly code-testable — `REQUIRED_DETECTION_FIELDS` is enforced inside `test_selected_catalogue_is_semantically_reviewable`'s pass/fail on the fixed/vulnerable pair, but no dedicated test isolates C4 alone, because this Tier-1 fixture has no persisted operational system to assert a threshold or a recovery step against. Modeled in `lessons/06-operate.md`. | items.md #5, #8 |
| C5 | 7 Generalize | Not code-testable — transfer is assessed as written reasoning about a different system, not a predicate over SecureCollab data. Modeled in `lessons/07-transfer.md`. | items.md #7 |

C1, C2, and C3 carry genuine lab assertions, exceeding the two-claim minimum. C4 and C5 are honestly declared non-code-testable rather than mapped to a fabricated test: C4 needs a persisted detection/alerting system this fixture does not have, and C5 needs a second system's actors and authority this fixture does not model.

## Coverage contract

Every outcome must have all five evidence types before publication. Assessment-item numbers are cross-checked against each item's own `**Claim assessed:** / **Outcome:**` tag in `content/modules/1/1.1/assessment/items.md`, not merely assigned here and assumed correct — a defect three prior deepening passes each found in this exact table.

| Outcome | Claim | Explanation and model | Worked reasoning | Learner practice | Assessment evidence | Transfer |
|---|---|---|---|---|---|---|
| 1. Produce a 5+ row SecureCollab catalogue | C2 | `lessons/02-securecollab-catalogue.md` | `lessons/02-securecollab-catalogue.md` §Two claims that look alike and are not | `lessons/02-securecollab-catalogue.md` §Practice; `labs/1.1/1.1-invariant-catalogue` | items.md #2 | `lessons/07-transfer.md` CivicClinic catalogue |
| 2. Separate properties from mechanisms, limits, defaults, evidence | C1 | `lessons/01-property-vs-mechanism.md` | `lessons/01-property-vs-mechanism.md` §A worked example: "passwords are hashed" | `lessons/01-property-vs-mechanism.md` §Practice | items.md #1 | `lessons/07-transfer.md` §Worked contrast |
| 3. Bound claims with the full claim envelope | C1, C2 | `lessons/01-property-vs-mechanism.md` §The envelope a rule needs; `lessons/02-securecollab-catalogue.md` §Naming actors... | `lessons/02-securecollab-catalogue.md` state/time section | `lessons/04-smallest-mechanism.md` §Practice | items.md #6 | `lessons/07-transfer.md` success criteria |
| 4. Distinguish root cause/preconditions/impact/prevention/detection/recovery | C1 | `lessons/03-local-hashed-claim.md` | `lessons/03-local-hashed-claim.md` §Reproduce the failure | `lessons/03-local-hashed-claim.md` §Read the causal document | items.md #4 | `lessons/07-transfer.md` |
| 5. Specify normal/negative/abuse/failure evidence | C3 | `lessons/05-forbidden-outcomes.md` | `lessons/05-forbidden-outcomes.md` §What each mode actually rules out | `lessons/05-forbidden-outcomes.md` §Practice | items.md #3 | `lessons/07-transfer.md` |
| 6. Design privacy-safe operational evidence and recovery | C4 | `lessons/06-operate.md` | `lessons/06-operate.md` §Designing a signal | `lessons/06-operate.md` §Practice | items.md #5, #8 | `lessons/07-transfer.md` |
| 7. Transfer to a materially changed system | C5 | `lessons/07-transfer.md` | `lessons/07-transfer.md` §Which SecureCollab claims break | `lessons/07-transfer.md` §Success criteria | items.md #7 | (is the transfer task) |

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

**Invariant:** a submitted catalogue is bounded, distinct row-by-row, and semantically shaped for independent review rather than being a mechanism slogan or five field-complete but content-identical rows.

**Vulnerable behavior:** a universal security conclusion, public-target text, insufficient catalogue rows, and missing model/evidence/operation fields cause the selected-catalogue test to fail.

**Fixed behavior:** five module-specific, mutually distinct claims pass semantic and safety checks.

**Structural fix:** versioned claim records connect product model, forbidden outcome, mechanism limits, four evidence modes, detection/recovery, residual risk, and review triggers.

**Limits:** the validator detects selected defects. Passing it is not proof that an implementation exists or satisfies the catalogue.

**Bug found and fixed in this pass:** reviewing the lab skeptically per `upgrade-lab`'s precedent (1.4's inverted flag, 2.1's regex/nesting bugs, 4.3's missing absolute-lifetime check) surfaced a real gap: a catalogue with all five rows field-complete, avoiding every phrase on `MECHANISM_ONLY_PHRASES`, and using distinct `id` values, but with every row's `property` and `forbiddenOutcomes` text identical and generic ("notes must never leak," "a bad actor"), passed `validate_catalogue` outright — field presence and slogan-avoidance are not the same property as five distinct, system-specific claims. `catalogue_validator.py` now computes a normalized `property` + `forbiddenOutcomes` signature per claim and flags a repeated signature across rows; `tests/test_claim_shape.py::test_five_padded_duplicate_rows_do_not_pass` asserts both that the padded fixture is now rejected and that the real fixed fixture's five genuinely distinct rows are not falsely flagged. This is C2 (see Teaching claims).

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
- **ASVS 5.0.0:** intentionally not mapped at requirement level in this first-principles module. Later implementation modules map exact verification requirements; adding unrelated ASVS IDs here would be compliance theater. Re-confirmed while deepening this module on 2026-09-18: no lesson, `module.yaml`, or lab file under `content/modules/1/1.1` or `labs/1.1` cites an ASVS requirement ID, so there was nothing to check against the live `v5.0.0` tag this pass — the prior modules' citation errors were all in modules that did cite ASVS IDs. The Saltzer & Schroeder principle names and NIST CSF 2.0 function names above were checked against `content/standards/pins.yaml`'s existing 2026-08-29 and 2026-08-25 reviews and found unchanged and accurately stated; no new fetch was needed for either seminal, non-versioned source.

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
| 2026-09-06 | Additive named mental models and mermaid diagrams on remaining lessons; independent review artifacts unchanged |
| 2026-09-18 | Deepen pass (this content-quality-improvement-plan's B1 item). Lessons `02`–`08` had drifted onto a local password-hashing exercise unrelated to `module.yaml`'s actual `labSpec` (`1.1-invariant-catalogue`) and averaged 356 words against the 900-word floor; all eight lessons rewritten against five named teaching claims (C1–C5), each mapped to loop steps, a lab assertion or an honest non-testability note, and an assessment item, per `deepen-module`'s Step 2. Found and fixed a real bug in `labs/1.1/1.1-invariant-catalogue/catalogue_validator.py` while reviewing it skeptically per that skill's precedent: a catalogue with five field-complete, slogan-free, but content-identical rows passed `validate_catalogue` outright; added a per-claim `property`+`forbiddenOutcomes` signature check and `tests/test_claim_shape.py::test_five_padded_duplicate_rows_do_not_pass` (C2). Authored `content/modules/1/1.1/assessment/items.md` (8 items; none existed before this pass) with `**Claim assessed:**`/`**Outcome:**` tags on every item, rewrote `content/assessment/keys/1.1.md` and `assessment/rubric.md` to match and to drop the stale "notes app" framing, and cross-checked every coverage-contract and teaching-claim citation against those tags directly (the defect class named in this plan's remediation notes for 1.4/2.1/4.3, where an average of five of six coverage rows cited the wrong item). Recomputed `estimatedMinutes` from the metadata-honesty formula: 420 → 240 (9,511 body words across the eight lessons, Tier-1 lab at 45 minutes, 8 items × 12, plus the 60-minute transfer task). No ASVS requirement is cited anywhere in this module before or after this pass, so there was nothing to re-verify against the live ASVS tag; Saltzer & Schroeder and NIST CSF 2.0 citations were re-confirmed against the existing pins rather than re-fetched, since neither source has a newer version. **Metadata reversion (`metadata-honesty.mdc`):** this module carried `status: published`, a named `reviewer`, `lastReviewedAt: '2026-08-25'`, and `nextReviewAt: '2027-02-25'` from a real independent review — but that review was granted against the pre-rewrite lessons named above, not against this pass's content, and a review of prose that no longer exists is not a review of what ships now. Per this rule's own framing (reverting an inaccurate claim to honest "pending" is the same direction as the D12 fixes on other modules, not the forbidden direction of claiming an unreviewed pass is reviewed), `module.yaml`'s `reviewer` is reverted to `pending independent quality and lab-safety review`, `lastReviewedAt`/`nextReviewAt` to `null`, and `status` to `draft`. `content/progress/STATUS.yaml`'s `quality`/`depth` fields for 1.1 are left untouched, per Step 10 — that is the reviewer's or a human's call, not this pass's. A new independent quality review and a new independent lab-safety review are required before either field is set again. |
