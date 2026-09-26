# 3.1 — Assets, data classification, and security requirements

## Identity

- **id:** 3.1
- **slug:** assets-data-classification-and-security-requirements
- **title:** Assets, data classification, and security requirements
- **phase / track / difficulty:** 3 / core / intermediate
- **estimatedMinutes:** 330
- **prerequisites:** Blueprint §7; 1.1–2.4 authored (asset/authority/boundary models; the Phase 2 browser→edge→API→database request path).
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 3

## Objective hierarchy

1. Produce a **data inventory, classification table, and security-requirements backlog** for SecureCollab's Phase 2 assets (note bodies, note/company identifiers, and the session tokens the request path already depends on) that a second engineer could implement and test without asking a follow-up question.
2. Name the attacker and operator capabilities a classification decision must survive (an operator debugging a log, a log vendor indexing a shared drain, another company's admin on shared observability, a support agent pasting into a ticket) and the trust assumption each one breaks if classification stays a label.
3. Transfer: a clinic booking card carrying chart text and appointment time on one record, rewritten without using a Top 10 or CWE list as the definition of security.

## Prerequisite concepts

Property (1.1) → authority cells and the access-matrix tuple (1.2) → trust boundaries and what-you-trust-for-this-rule (1.3) → the Phase 2 request path's company-bound identity and shared-cache scoping (2.2) → this module's per-sink classification rule and requirements backlog.

## Misconceptions

- A classification label (a spreadsheet cell, a Confluence tag, a privacy-policy sentence) is itself a security control.
- An inventory that lists content fields (note body, note title) is complete without also listing the authority artifacts (session tokens, API keys, share-grant identifiers) that grant broader access than the content they gate.
- A field nobody has classified yet is low-risk until proven otherwise; in fact every downstream sink already treats it as unrestricted, which is the opposite default.
- "We log by default" and "we redact by default" are the same design decision described from two different moods.
- Awareness lists (OWASP Top 10, CWE Top 25) are a substitute for deriving a classification and a requirement from this system's own assets.

## Concept map

Property (1.1) → authority (1.2) → boundary (1.3) → request-path identity binding (2.2) → this module's mechanism (a per-field, per-sink classification rule) and evidence (a backlog a second engineer can test).

## Teaching claims

The module previously taught **one narrow predicate** across all eight lessons: a note body must not appear in an application log line. That property still holds and is still worth teaching — it survives below as part of `C1` and `C3` — but "classification and security requirements" promises more than one sink rule for one field, and the other four claims below had no lesson, no lab assertion, and no assessment item before this pass. Naming them here follows the same repair `2.2` and `4.3` made for the same defect: a title promising a topic while the lessons deliver a single boolean.

1. **C1 — Classification is a per-field, per-sink rule with a named check and failure behavior, not a label.** For SecureCollab's note body, classified Confidential, an operator debugging a log, a log vendor indexing a shared drain, or another company's admin on shared observability cannot read the body through the `note_read` application-log sink, because that sink's own policy must refuse a Confidential field and must deny by default when a field's status is unknown. If the classification exists only as a spreadsheet cell with no per-sink allow/deny rule and no test proving the deny holds, the answer is no — the body still reaches the log, because nothing at the sink itself changed.

2. **C2 — An asset inventory that lists only content fields and omits authority artifacts is incomplete, and an authority artifact must be classified at least as sensitively as the content it gates.** For SecureCollab, a session token is an asset the inventory must classify Confidential, at the same level as a note body, because a party who reads that token from a log line, an error dump, or a support ticket can act as the token's owner — read and write everything that owner could reach — which is a strictly larger compromise than reading the content of one field. An inventory entry that says "note body: Confidential" and leaves the session token absent has not finished the inventory; it has stopped at the asset that was easiest to name, and every sink the token can still reach (a second, independently-reached error handler is the concrete case this module's lab uses) stays unclassified along with it.

3. **C3 — A security requirement names the sink, the allow/deny decision, and the failure behavior; a classification level by itself is not a requirement.** For any field in SecureCollab's data inventory, an engineer building a new sink (a log line, an export, a support tool, a backup job) cannot tell from a level alone whether that sink may carry the field, because "Confidential" states a level, not an instruction to any particular piece of code. The requirement must say, for this sink: allow or deny this level, and what happens when a field's level is not yet known. A backlog entry that records a level and not a per-sink allow/deny with a stated failure behavior cannot be implemented correctly and cannot be tested, and every new sink will default to including whatever context it is handed — which is exactly the vulnerable behavior this module's lab reproduces.

4. **C4 — An unclassified field is not a low-risk field; every downstream sink already treats it as ordinary, unrestricted data, so silence resolves to exposure, not to safety.** For a field newly added to SecureCollab's note or account schema, a developer who ships it before writing a classification and a per-sink rule cannot rely on any sink refusing it, because a logger, an error handler, or an export function accepts whatever dictionary or object it is handed and has no reason of its own to treat one key differently from another. The absence of a classification decision does not defer the risk to a later date; it resolves the risk to "expose," immediately, without anyone having chosen that outcome. A correct mechanism must therefore default an unrecognized field to the *most* restrictive level, not the least — the same fail-safe-defaults principle Saltzer and Schroeder state for authority, applied here to data.

5. **C5 — A fix that lives at one call site is not durable; a classification-derived requirement needs a detection signal and a purge or rotation path in addition to the sink check.** For SecureCollab's note-body redaction, correcting `log_event` to exclude the body does not stop a different function — an exception handler, a new export route, an analytics client — from independently reintroducing the same field at a call site the first fix never touched, because each sink is separate code that makes its own decision about what it accepts. A classification requirement that stops at "and then we fixed the logger" is only true until the next code path forgets it; the backlog must also name a detection signal (a redaction-miss count) and a recovery step (purge matching records, rotate any token that was exposed), never re-emitting the exposed value while investigating it.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 4 Build, 5 Verify | `test_note_body_excluded_from_application_log` (forbidden outcome), `test_allowed_metadata_present_after_redaction` (normal case — redaction is not "log nothing"), two anti-fake tests: `test_anti_fake_fresh_secret_not_a_literal_match` (a freshly generated body defeats a hardcoded-substring cheat) and `test_anti_fake_redaction_is_not_a_canned_line` (two distinct notes must still be distinguishable in the log, defeating a fixed-literal-line cheat) | items.md #1, #2, #6 |
| C2 | 1 Property, 2 Model, 3 Break, 5 Verify | `test_session_token_excluded_from_application_log` (forbidden outcome), `test_session_token_excluded_from_error_dump` (boundary — the same asset denied by a second, independently-reached sink) | items.md #1, #3, #7 |
| C3 | 1 Property, 4 Build, 5 Verify | `test_allowed_metadata_present_after_redaction` (the requirement is allow/deny per sink, not blanket silence) | items.md #2, #4 |
| C4 | 4 Build, 5 Verify | `test_unclassified_field_defaults_to_redacted` (boundary and anti-fake — a never-named field is denied by the default, not by a hardcoded pair of field names) | items.md #5 |
| C5 | 6 Operate, 7 Generalize | `test_error_dump_still_diagnosable_without_secrets` (malformed/failure path — the second sink stays useful without the token) | items.md #7, #8 |

C1, C2, C3, C4, and C5 all carry at least one genuine lab assertion — five of five claims, well past the module's own ≥2 bar — because the lab fixture is a single FastAPI service with two independent sinks (`labs/3.1/3.1-lab`), which lets every claim about "a second sink" or "an unnamed field" be a real request/response assertion rather than a modeled residual.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Given a field and a candidate sink, decide allow or deny for that field-sink pair and name the classification level and the check that produced the decision | C1, C3 | [`lessons/01-property.md`](lessons/01-property.md) §A sink rule, not a label | [`lessons/03-break.md`](lessons/03-break.md) `vulnerable/app.py`'s unread `CLASSIFICATION` table | `labs/3.1/3.1-lab` vulnerable/fixed pair | items.md #1, #2 | [`lessons/07-transfer.md`](lessons/07-transfer.md) chart text vs. appointment time |
| Identify every authority artifact an inventory limited to content fields would omit, and justify classifying each at least as sensitively as the content it gates | C2 | [`lessons/01-property.md`](lessons/01-property.md) §The asset that was easiest to name | [`lessons/02-model.md`](lessons/02-model.md) §Two sinks, one asset class | `labs/3.1/3.1-lab` `test_session_token_excluded_from_error_dump` | items.md #3, #7 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Write a requirements-backlog entry for a classified field naming the sink, the allow/deny decision, and the failure behavior when a field's status is unknown, and explain why a level alone is insufficient | C3, C4 | [`lessons/04-build.md`](lessons/04-build.md) §Redact at the sink, not at the field | [`lessons/04-build.md`](lessons/04-build.md) `fixed/app.py`'s `_redact` | [`lessons/02-model.md`](lessons/02-model.md) backlog exercise | items.md #2, #4, #5 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Given a newly added, unclassified field, predict how each existing sink treats it by default and explain why that default is a decision already made, not a delay | C4 | [`lessons/04-build.md`](lessons/04-build.md) §The default an unnamed field gets | [`lessons/05-verify.md`](lessons/05-verify.md) fail-safe-default case | `labs/3.1/3.1-lab` `test_unclassified_field_defaults_to_redacted` | items.md #5 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Design a detection signal and a purge/rotation response for a redaction miss, and explain why a fix at one call site does not cover a second, independently-reached sink | C5 | [`lessons/06-operate.md`](lessons/06-operate.md) §A fix that lives in one function | [`lessons/06-operate.md`](lessons/06-operate.md) signal table | [`lessons/06-operate.md`](lessons/06-operate.md) practice | items.md #7, #8 | [`lessons/07-transfer.md`](lessons/07-transfer.md) (is the transfer task) |

## Known residuals

- Cross-company authorization (which company may read a given note) is 4.4's `can_read` matrix, not this module's. The lab's session lookup identifies a caller's own company for logging context only, and the fixture never gates a read by company — naming that boundary in [`lessons/01-property.md`](lessons/01-property.md) and the lab's own README rather than silently building an authorization check this module does not own.
- Encryption of Confidential fields at rest is [5.3 Encryption and key management](../../5/5.3/lessons/01-property.md) — this module's sink rule governs what a *log or export* may carry, not what the database column itself does.
- Exception middleware, slow-query logs, and full-packet APM capture that never call through `log_event` or `write_error_dump` at all bypass this module's mechanism entirely; named as an explicit residual in `lessons/01-property.md` and `lessons/06-operate.md`, not hidden as a silent pass.
- Log retention after a note is deleted (how long an already-written, correctly-redacted log line survives) is a data-lifecycle question for [5.1 Sensitive data lifecycle](../../5/5.1/lessons/01-property.md), not a classification-sink question this module answers.
- Regex-based redaction applied after the fact, rather than a field-level allow-list applied before rendering, can miss an encoded or re-serialized copy of a denied value; named as a limit in `lessons/04-build.md` and picked up structurally, for a different sink class, in later phases.
- STRIDE-style threat enumeration over the assets this module inventories is [3.2 Threat modeling](../../3/3.2/spec.md), which explicitly lists "classification/sinks (3.1)" as its own prerequisite — this module supplies the inventory and the requirement; 3.2 supplies the systematic threat walk over it.

## Invariant prompts

- What must remain true if a brand-new field is added to the schema tomorrow and nobody remembers to classify it?
- What fails if a sink is reached by a code path other than the one that was fixed?

## Threat-model prompts

- What can go wrong for the note body and the session token specifically, as two distinct assets with two distinct blast radii?
- What residual remains if the sink-level fix holds but the inventory itself is missing an asset?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08, seven-step loop).

## Lab briefs

Authorized **local course fixture** (`labs/3.1/3.1-lab`, Tier 2: a FastAPI service exercised through `TestClient`). Forbidden: live targets, real PII, weaponized lesson payloads, awareness-list-as-syllabus.

## Assessment blueprint

See `module.yaml` assessmentBlueprint. Mastery states: not-attempted | developing | competent | transfer-ready. No compensating averages.

## Standards references

- OWASP ASVS 5.0.0 (final, live-fetched 2026-09-26 against the `v5.0.0` tag): `v5.0.0-14.1.1` (sensitive data identified and classified into protection levels), `v5.0.0-14.1.2` (every protection level has documented protection requirements, including how the data is logged and access controls around sensitive data in logs), `v5.0.0-14.2.3` (defined sensitive data not sent to untrusted parties, e.g. trackers — the anchor for treating a log vendor or a shared-observability co-tenant as untrusted), `v5.0.0-14.2.4` (controls implemented as defined in the protection-level documentation — the anchor for "a level with no per-sink rule is not yet a requirement"), `v5.0.0-16.1.1` (a logging inventory naming what is logged, where, and who can access it), `v5.0.0-16.2.5` (logging enforced by protection level; credentials/payment may not be logged at all, other data such as session tokens only hashed or masked). No ASVS 4.x. No MASVS L1/L2/R.
- NIST CSF 2.0 (final): the Identify function's asset-management outcome family, used as vocabulary for "know what you have before you decide how to protect it," not as a control catalogue.
- Saltzer and Schroeder (1975), fail-safe defaults: the standards anchor for C4's "an unclassified field defaults to the most restrictive level."

## Review triggers

A new SecureCollab field, sink, or third-party integration that this inventory does not yet name; a company boundary change that changes which parties count as untrusted for a given field; superseding **final** standard.

## Time budget and SecureCollab

Blueprint §9.1 phase evolution: Phase 3 produces "product requirements, data classification, threat model, architecture decisions, and misuse cases" for SecureCollab. This module supplies the classification table and requirements backlog that 3.2's threat model and 3.3's architecture decisions both build on. Evidence: data inventory, classification table, security-requirements backlog, transfer artifact.

## Operational considerations

Pair prevention (the sink-level allow-list) with detection (`log_redaction_miss`) and recovery (purge matching records; rotate any token that was exposed) — prevention at one call site is not durable on its own (C5). Operators still legitimately see Internal fields (note id, company id) in the same log line; that is a different row in the backlog, not evidence that the Confidential fields are also safe.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-08-23 | Pass A quality-gate: spec completeness competent; expand in a later revision if thin |
| 2026-08-23 | Pass B lessons and authorized local lab |
| 2026-08-23 | Pass C rubric and examiner keys; quality-gate recorded |
| 2026-08-23 | Deepen: 1.1-density lessons; structural local lab; quality-gate recorded |
| 2026-08-24 | Publishable rewrite: unique 1.2-density lessons, structural lab mapping, Pass C keys isolated |
| 2026-09-06 | Depth pass: field-times-sink mental models, mermaid diagrams, ASVS 5.0 14.1.1/14.1.2/16.2.5 pins; independent review still required |
| 2026-09-06 | Thickened lessons 03-08 with body-in-log cause tables, sink-API limits, and clinic chart-versus-time transfer; independent review still required |
| 2026-09-26 | **Deepen (this pass):** fixed **D3** (one narrow predicate stretched across eight lessons) by replacing the single property ("note body must not appear in a log line") with five dependency-ordered teaching claims (C1–C5) covering sink-rule derivation, authority-artifact inventory completeness, requirement derivation from a classification level, the fail-safe default for unclassified fields, and prevention/detection/recovery pairing. Fixed **D1** (telegraphic prose that asserts instead of derives) and **D2** (teaching by negation list) by rewriting all eight lessons to the ≥900-word floor with derivation-before-assertion and dual-form term definitions, replacing the prior fragment style ("X is not Y" standing alone, noun-phrase paragraphs). Fixed **D6** (decorative diagrams) by rebuilding every Mermaid diagram to the kind/node minimums in `lesson-prose.mdc`. Fixed **D7** (unresolved forward references) with titled cross-reference links throughout, including to 3.2, 4.4, 5.1, and 5.3 for named residuals. Fixed **D8** (labs are predicates, not systems) by upgrading the lab from a Tier 1 two-line pure function with two tests to a Tier 2 FastAPI component (two independent sinks, a real request/response cycle) with nine tests, including two explicit anti-fake tests and a third test that doubles as an anti-fake check. Fixed **D9** (assessment has no items) by writing `assessment/items.md` (8 module-specific items) and `content/assessment/keys/3.1.md` with distractor rationales and four-state banding, deleting the prior "session worksheet" placeholder from `assessment/rubric.md`. Fixed **D11** (standards traceability invisible to the learner) with exact `**Standards:**` lines in `01-property.md` and `05-verify.md`. Fixed **D12** (metadata overstates maturity) by rewriting `module.yaml` outcomes as observable behaviors and recomputing `estimatedMinutes` from the metadata-honesty formula. Live-fetched and re-verified the ASVS 5.0.0 pin against the canonical `v5.0.0` tag JSON and added three previously-uncited requirement IDs (14.2.3, 14.2.4, 16.1.1) that this module's own new claims depend on. Independent review still required; this pass sets no `depth`, `quality`, `reviewer`, or review-date field. |
