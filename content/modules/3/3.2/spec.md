# 3.2 — Threat modeling

## Identity

- **id:** 3.2
- **slug:** threat-modeling
- **title:** Threat modeling
- **phase / track / difficulty:** 3 / core / intermediate
- **estimatedMinutes:** 300
- **prerequisites:** Blueprint §7; 1.1–3.1 authored (SecureCollab's authority model, trust boundaries, and Phase 3 asset/classification inventory).
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 3

## Objective hierarchy

1. Given SecureCollab's Phase 3 assets and boundaries (from [3.1](../3.1/spec.md)), produce a **version-controlled threat model** whose always-name threats survive a green scanner result, whose diagram traces every flow those threats depend on, whose top-priority row resolves to a real mitigation, and whose review triggers demand a recorded re-review rather than a rewritten date — a model a second engineer, or a CI job, could check without asking a follow-up question.
2. Name the attacker and platform capabilities a threat model must survive (a cross-tenant member, a hostile Next.js client, a future worker identity redelivering a share grant) and the trust assumption a green-scan-only process breaks.
3. Transfer: clinic SMS reminders — rewrite the always-name set, the required-flow list, and one prioritized mitigation for a channel no HTTP scanner enumerates, without using a Top 10 or a vendor questionnaire as the definition of security.

## Prerequisite concepts

Property (1.1) → authority cells (1.2) → trust boundaries and what-you-trust-for-this-rule (1.3) → SecureCollab's Phase 3 classification and sink inventory (3.1) → this module's systematic threat walk over that inventory, and the CI gate that keeps it honest.

## Misconceptions

- A green scanner means there are no threats.
- Threat models are a pre-code ceremony; they do not live in git and are never re-checked.
- STRIDE letters on a data-flow diagram are a model even without assets, owners, and a stated way to prove each row wrong.
- Prioritizing threats is the same activity as deciding what to build; a ranked list with no mitigation on the top row has not yet produced a decision.
- OWASP Top 10 / CWE Top 25 are the threat list or a compliance baseline, rather than a regression check run after the causal model exists.
- ASVS 5.0 still has a numbered "do threat modeling" requirement, or an "Appendix D" on the topic (it does neither; see Standards references below for the correction this pass made to the module's own prior citations).

## Concept map

Property (1.1) → authority (1.2) → boundary (1.3) → classification and sinks (3.1) → this module's versioned model, flow tracing, prioritized mitigation, and change-triggered re-review.

## Teaching claims

The module previously taught **one narrow predicate** across all eight lessons: a green scan must not produce an empty threat list. That property still holds and is still worth teaching — it survives below as `C1` — but "threat modeling" promises a systematic walk over a system's assets and boundaries, prioritized mitigation, and a model that stays current as the system changes, and the other three claims below had no lesson, no lab assertion, and no assessment item before this pass. Naming them here follows the same repair [3.1](../3.1/spec.md) made for the identical defect: a title promising a topic while the lessons deliver a single boolean.

1. **C1 — A green scanner result cannot stand in for the versioned model's always-name set.** For SecureCollab's Phase 3 CI merge gate, an engineer relying on a green SAST/DAST/package scan cannot treat that result as evidence that `cross-tenant-read` (a member of another company reading a note by id), `hostile-browser` (a Next.js client no server code should trust), and `stolen-worker` (a future worker redelivering a share grant) have been considered, because the gate's own check must independently confirm all three are present in the versioned model, each with a named owner and a review trigger, regardless of what the scanner reports. If any of the three is missing, or present with no owner or trigger, the answer is no: the gate must fail, and a scanner result — green or not — cannot change that, because none of the three threats is a pattern any SAST/DAST/package rule matches in the first place.

2. **C2 — A threat id present in the model cannot stand in for a traced flow.** For SecureCollab's worker-redelivery path (a share grant redelivered later by a worker adapter, the same "server-built context" pattern [1.3's export-worker example](../../1/1.3/lessons/01-property.md) already established), a reviewer cannot treat `stolen-worker` as covered merely because that string appears as a threat id in the model, because the model's own data-flow diagram must independently declare `worker-share-redelivery` as a traced flow before the id means anything checkable. If the diagram's declared flows omit that path — the same omission an HTTP-only scan would also produce, since a worker path answers to no browser request at all — the answer is no: the id is a label, not a checked boundary, and an attacker who reaches the effect through the untraced path meets no control the model actually verified. This is the concrete version of "what does an incomplete trust-boundary diagram let an attacker do that a complete one would have caught": it lets a threat id exist with nothing behind it.

3. **C3 — A priority ranking cannot stand in for a mitigation decision.** For SecureCollab's three always-name threats, an engineer reading a prioritized list cannot tell what to build first from the ranking alone, because the highest-priority row must resolve to a specific, non-placeholder mitigation — a named mechanism or an owning module, such as "deny-by-default in 4.4's `can_read` matrix" — not a rank number by itself. If the top-priority row's mitigation field is empty, "TBD," or otherwise a placeholder, the answer is no: prioritizing the threats has not yet told anyone what to do about the one that matters most, and the model has produced an ordering without producing a decision.

4. **C4 — A self-reported update date cannot stand in for a recorded re-review.** For SecureCollab's threat model after a named review trigger fires (a new share path, worker identity, or client surface ships), a reviewer cannot accept a recent-looking "last updated" date as evidence that the threat rows that trigger names were reconsidered, because the gate must check, per threat row, whether the fired trigger's name appears in that row's own re-review record — independent of any date field a submitter could simply rewrite. If a trigger has fired and the row it names carries no matching re-review record, the answer is no: the model is stale for that row, whatever date sits at the top of the file. This is the concrete version of "how does a threat model stay current as the system changes": staleness is measured by what was actually re-reviewed, never by what a date field claims.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 4 Build, 5 Verify | `test_complete_model_passes_on_green_scan` (normal), `test_green_scanner_missing_cross_tenant_read_fails` (forbidden outcome), `test_mandatory_threat_without_owner_fails` (malformed), `test_scanner_findings_are_additive_not_replacing` (normal — additive, never a substitute) | items.md #1, #2, #6 |
| C2 | 1 Property, 2 Model, 3 Break, 5 Verify | `test_untraced_worker_flow_fails_even_with_all_ids_present` (boundary — this is the module's own representative failure, not a variant of C1's) | items.md #1, #3, #7 |
| C3 | 2 Model, 4 Build, 5 Verify | `test_top_priority_threat_without_real_mitigation_fails`, `test_missing_priority_field_fails` (malformed) | items.md #4, #5 |
| C4 | 6 Operate, 7 Generalize | `test_fired_trigger_without_revisit_fails` (forbidden outcome for staleness), `test_anti_fake_revisit_is_checked_per_threat_not_globally` (anti-fake) | items.md #4, #8 |

All four claims carry at least one genuine lab assertion — four of four, past the module's own ≥2 bar — because the lab fixture is a single FastAPI CI-gate service (`labs/3.2/3.2-lab`) that opens the stored threat-model document on every call, which lets every claim about "a traced flow," "a real mitigation," or "a recorded re-review" be a real request/response assertion against structured data rather than a modeled residual.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Given a submitted threat-model document and a scanner result, decide whether SecureCollab's CI merge gate should pass or fail, and name which of the four gate checks failed | C1, C2 | [`lessons/01-property.md`](lessons/01-property.md) §The claim you can prove false | [`lessons/03-break.md`](lessons/03-break.md) `vulnerable/app.py`'s single-field gate | `labs/3.2/3.2-lab` vulnerable/fixed pair | items.md #1, #2 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Given a data-flow diagram with one flow missing, identify which always-name threat's coverage claim becomes unchecked, and explain why the threat id alone was not sufficient evidence | C2 | [`lessons/01-property.md`](lessons/01-property.md) §A label is not a traced boundary | [`lessons/02-model.md`](lessons/02-model.md) §Two worked discriminations | `labs/3.2/3.2-lab` `test_untraced_worker_flow_fails_even_with_all_ids_present` | items.md #3, #7 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Given a prioritized threat list with a placeholder mitigation on the top row, explain why ranking the threats did not yet produce an actionable decision, and write a real one | C3 | [`lessons/04-build.md`](lessons/04-build.md) §Seed, trace, then rank | [`lessons/04-build.md`](lessons/04-build.md) `fixed/app.py`'s mitigation check | [`lessons/02-model.md`](lessons/02-model.md) backlog exercise | items.md #4, #5 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Given a named review trigger that has fired, decide whether a specific threat row's re-review record satisfies it, independent of any "last updated" date shown, and design the detection signal for a row that does not | C4 | [`lessons/06-operate.md`](lessons/06-operate.md) §Notice, do not back-date | [`lessons/06-operate.md`](lessons/06-operate.md) signal table | `labs/3.2/3.2-lab` `test_fired_trigger_without_revisit_fails` | items.md #8 | [`lessons/07-transfer.md`](lessons/07-transfer.md) (is the transfer task) |

## Known residuals

- Cross-tenant authorization itself (the actual `can_read` check that must deny a member of another company) is [4.4 Authorization and tenant isolation](../../4/4.4/spec.md), not this module. This module's gate checks that `cross-tenant-read` is named, traced, prioritized, and current; it does not implement or test the enforcement mechanism that closes it.
- STRIDE, PASTA, and attack-tree facilitation quality (whether a workshop asked good questions) is outside what an automated gate can check; named as a limit in `lessons/05-verify.md` rather than hidden as something the lab proves.
- LINDDUN-style privacy threat enumeration is [5.1 Data lifecycle and privacy engineering](../../5/5.1/lessons/01-property.md)'s to own once retention and disclosure assumptions exist to threaten; this module's data-centric anchor (NIST SP 800-154, still draft) is informative only.
- Whether a `revisited_after` entry reflects an honest re-review or a rubber stamp is not something an automated check can see from the outside; named explicitly in `lessons/05-verify.md` as part of the property, not glossed over.
- The actual worker-identity and redelivery mechanism `stolen-worker` names is [7.4 Queues, workers, events, and service identity](../../7/7.4/spec.md)'s to build; this module only requires that the threat be named, traced, and re-reviewed on schedule.

## Invariant prompts

- What must remain true if every CVE scanner is green and stays green for a year?
- What fails if a threat id is added to the model but the diagram is never updated to show the path it depends on?

## Threat-model prompts

- What can go wrong for SecureCollab's Phase 3 notes, share grants, and session cookies specifically, as distinct assets with distinct blast radii?
- What residual remains if the gate's four checks all pass but the human who wrote `revisited_after` never actually reopened the four questions?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08, seven-step loop).

## Lab briefs

Authorized **local** `labs/3.2/3.2-lab` only, Tier 2 (a FastAPI CI-gate service exercised through `TestClient`). Forbidden outcome: a green scanner result passes SecureCollab's merge gate for a threat model missing a mandatory id, an untraced required flow, a placeholder mitigation on the top-priority threat, or an unrevisited row after its trigger fired. Forbidden: live targets, real PII, weaponized lesson payloads.

## Assessment blueprint

See `module.yaml` assessmentBlueprint. Mastery states: not-attempted | developing | competent | transfer-ready. No compensating averages.

## Standards references

- OWASP ASVS 5.0.0 (final, live-fetched 2026-09-26 against the canonical `v5.0.0` requirements JSON): `v5.0.0-13.1.4` (L3, advanced — a secrets-rotation schedule based on "the organization's threat model and business requirements," the one place the standard names a threat model directly); `v5.0.0-15.1.4` (L3, advanced — application documentation highlights third-party components considered "risky"); `v5.0.0-15.1.5` (L3, advanced — application documentation highlights parts of the application using "dangerous functionality"). This pass corrected two prior citations: `v5.0.0-15.1.3` was miscited as "documented security decisions" when its canonical text is about time-consuming/resource-demanding functionality, and "OWASP ASVS 5.0 Appendix D" (`appendix-d-threat-modeling`) does not exist in the canonical v5.0.0 requirements JSON or docs directory and has been removed as unverifiable. See `content/standards/pins.yaml`'s `owasp-asvs-5.0.0` entry for the full correction note. No ASVS 4.x. No MASVS L1/L2/R.
- OWASP Threat Modeling Project (final, maintained project guidance, re-checked 2026-09-26): Four Question Framework; methodology-neutral umbrella; STRIDE/LINDDUN/PASTA as options, not a single required OWASP method. This pass also corrected the project's dead `url` (see `content/standards/pins.yaml`).
- NIST SP 800-154 (Initial Public Draft, re-checked 2026-09-26): still not final. Informative data-centric modeling only; not a substitute for a version-controlled SecureCollab model with owners, priorities, and review triggers.

## Review triggers

New share path, worker identity, webhook, SMS/email channel, or client surface; a superseding **final** SP 800-154; an ASVS revision that restores or relocates architecture-documentation requirements; a change to SecureCollab's Phase 3 asset or classification inventory in [3.1](../3.1/spec.md).

## Time budget and SecureCollab

Blueprint §9.1 phase evolution: Phase 3 produces "product requirements, data classification, threat model, architecture decisions, and misuse cases" for SecureCollab. This module supplies the systematic threat walk over [3.1](../3.1/spec.md)'s inventory and hands prioritized, traceable rows to [3.3](../3.3/spec.md)'s architecture decisions and [4.4](../../4/4.4/spec.md)'s enforcement. Evidence: version-controlled threat model with open assumptions, owners, priorities, review triggers, and decision history.

## Operational considerations

Pair prevention (the CI gate itself) with detection (`missing_mandatory_threat` with a reason code distinguishing not-present, no-owner, no-trigger, and not-revisited) and recovery (add the missing row, the owner, and the mitigation; never back-date the file to make a stale row look current). Unknown unknowns remain; review triggers exist for exactly that residual, not to eliminate it.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-08-23 | Pass A quality-gate: spec completeness competent; expand in a later revision if thin |
| 2026-08-23 | Pass B lessons and authorized local lab |
| 2026-08-23 | Pass C rubric and examiner keys; quality-gate recorded |
| 2026-08-23 | Deepen: 1.1-density lessons; structural local lab; quality-gate recorded |
| 2026-08-24 | Publishable rewrite: unique 1.2-density lessons, structural lab mapping, Pass C keys isolated |
| 2026-09-06 | Depth pass: four-questions and scanner-is-coverage models, mermaid diagrams, ASVS v5.0.0-15.1.3 / v5.0.0-15.1.5 (Level 3 labeled advanced), Appendix D as awareness |
| 2026-09-06 | Thickened lessons 03-08 with green-scan cause tables, seed-then-union limits, and clinic SMS transfer |
| 2026-09-26 | **Deepen (this pass):** fixed **D3** (one narrow predicate stretched across eight lessons) by replacing the single property ("a green scan must not produce an empty threat list") with four dependency-ordered teaching claims (C1–C4) covering the always-name set surviving a scanner, flow tracing behind a threat id, prioritization resolving to a real mitigation, and staleness measured by recorded re-review rather than a self-reported date. Fixed **D1** (telegraphic prose) and **D2** (teaching by negation list) by rewriting all eight lessons to the ≥900-word floor with derivation before assertion and dual-form term definitions, replacing the prior fragment style ("threats = [] if scanner_green" standing alone, noun-phrase tables). Fixed **D6** (decorative diagrams) by rebuilding every Mermaid diagram to the kind/node minimums. Fixed **D7** (unresolved forward references) with titled cross-reference links, including into 1.3, 3.1, 3.3, 4.4, 5.1, and 7.4 for named residuals. Fixed **D8** (labs are predicates, not systems) by upgrading the lab from a Tier 1 12-line pure function with 3 tests to a Tier 2 FastAPI CI-gate service (two endpoints, a stored threat-model document, a real request/response cycle) with 9 tests, including 2 explicit anti-fake tests. Fixed **D9** (assessment has no items) by writing `assessment/items.md` (8 module-specific items) and `content/assessment/keys/3.2.md` with distractor rationales and four-state banding, deleting the "session worksheet" placeholder from `assessment/rubric.md`. Fixed **D11** (standards traceability invisible to the learner) with exact `**Standards:**` lines in `01-property.md` and `05-verify.md`. Fixed **D12** (metadata overstates maturity — `reviewer: pending...` carried a dated `lastReviewedAt`/`nextReviewAt`, a review date for a review that never happened) by nulling both dates and rewriting `module.yaml` outcomes as observable behaviors, recomputing `estimatedMinutes`. Ran `standards-pin` (step 1): live-fetched the canonical ASVS v5.0.0 requirements JSON and found the module's prior `v5.0.0-15.1.3` citation was a miscitation (wrong topic) and its "ASVS 5.0 Appendix D" citation does not exist in the canonical source; both corrected, with three verified replacement ids (`v5.0.0-13.1.4`, `v5.0.0-15.1.4`, `v5.0.0-15.1.5`). Also fixed the OWASP Threat Modeling Project pin's dead url at the shared `content/standards/pins.yaml` level (same class of mechanical dead-link defect 0.1/2.2/2.3/2.4 already fixed for their own pins). Independent review still required; this pass sets no `depth`, `quality`, `reviewer`, or review-date field. |
