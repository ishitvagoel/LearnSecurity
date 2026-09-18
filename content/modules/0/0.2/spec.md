# 0.2 — Diagnostic and adaptive bridge

Pass A specification, deepened. Lesson prose lives in `lessons/`. A placement quiz of 100 does not skip 1.2 or Gate 1. NICE language may skip tooling gaps, never invariants. Do not mark Gate 0 complete from a quiz.

## Identity

- **id:** 0.2
- **slug:** diagnostic-and-adaptive-bridge
- **title:** Diagnostic and adaptive bridge
- **phase / track / difficulty:** 0 / bridge / foundation
- **estimatedMinutes:** 240
- **prerequisites:** 0.1 orientation; diagnostics never skip 1.2 or Gate 1.
- **routeTags:** complete, web-api, bridge
- **releaseMilestone:** none
- **masteryGate:** 0

## Objective hierarchy

1. Produce a **skip predicate** so `quiz_score_grants_phase1_skip(100)` is false, a **bridge predicate** that reads only the diagnostic's own gap evidence, and a **required-path function** that never drops 1.2, 1.3, or 1.4 from a learner's path.
2. Name attacker capabilities (a hurried learner; a hiring manager with a badge) and trust assumptions (the local diagnostic repository is honest; quiz items are not production secrets; a credential claim is not the diagnostic's own observation).
3. Transfer: clinic onboarding quiz; vendor cert used to skip a threat-model review.

## Prerequisite concepts

0.1 scope. This module places learners into **tooling** bridges (Git/SQL/HTTP) without minting 1.2, 1.3, or 1.4 cells.

## Misconceptions

- Placement is a security clearance.
- Fast learners skip invariants.
- Tool fluency is threat modeling.
- LMS percentage is Gate 1 evidence.
- A job title or vendor certification is diagnostic evidence.

## Concept map

Score-as-capability (break) → skip only tooling units, on the diagnostic's own evidence (this module) → 1.2/1.3/1.4 still required for every learner. Residual: memorizing answers without running the lab.

## Teaching claims

Five falsifiable claims, ordered by dependency. The module previously taught only the first of these — a single always-false predicate repeated across eight lessons under different headings — while its own spec already named four further review triggers (no link to 1.2 evidence, a badge treated as Gate 1, an adaptive path hiding 1.4, a NICE list treated as the syllabus) that no lesson or test actually exercised. Naming the other four here, and building lab assertions for three of them, closes that gap instead of leaving it as a list of sentences no evidence backs.

1. **C1 — A diagnostic score, however high, cannot satisfy Gate 1's evidence requirement.** `quiz_score_grants_phase1_skip(score)` must be `False` for every input, because a percentage on a tooling quiz and an authority map, a trust-boundary diagram, or a risk register are different kinds of evidence: one is a number a scoring engine produced from multiple-choice answers, and the other is a learner's own reasoning about a specific system, reviewable by another person. A score cannot become the second kind of evidence by being high enough — there is no threshold at which a multiple-choice percentage starts entailing "this learner can write a deny-by-default rule for SecureCollab," because the percentage was never measuring that capability in the first place.
2. **C2 — A tooling-bridge skip may be granted only by the diagnostic's own observation of a real capability gap, never by a credential asserting competence from a different authority.** A job title, a vendor certification screenshot, and an LMS "mastery" badge each report a different organization's judgment, made for a different purpose, under evidence standards this course did not set and cannot inspect — and `tooling_bridge_required` must ignore all three, even on the occasions they happen to be true. This is not distrust of the credential's accuracy; it is that "probably true" and "this diagnostic observed it" are different properties, and a bridge-skip decision that accepts the first is a decision this course cannot audit, because the evidence lives in a system it does not control.
3. **C3 — Modules 1.2, 1.3, and 1.4 are a fixed set for every learner who has not yet produced Gate 1 evidence, and no diagnostic input may shrink it.** `phase1_modules_for_learner` must return all three module ids in its required set regardless of quiz score, a "fast-track" flag, or how many tooling-bridge units the same diagnostic assigns — a high Git score has no bearing on whether a learner can draw a trust boundary (1.3) or reason about a coerced user's residual risk (1.4), so a function that lets tooling fluency shrink the Phase 1 set is applying evidence about one property to a decision about an unrelated one. This claim is not a restatement of C1: C1 forbids one number from unlocking a skip; C3 forbids a *side effect* of a different, legitimate decision (assigning a tooling bridge) from quietly reaching into the Phase 1 set it was never asked about.
4. **C4 — The NICE Workforce Framework's Secure Systems Development work role is informative placement vocabulary, not this course's syllabus.** NIST SP 800-181 Rev. 1 defines "Secure Systems Development" as a *work role* — a description of what a job posting or a hiring rubric might ask for — inside the Design and Development category, and using that description to decide which tooling bridge a learner plausibly needs is a legitimate, narrow use of it. Treating the same description as though completing it satisfied 1.2's authority-map requirement is a different act entirely: a work-role list describes a job, not a reviewed artifact, and it commits the identical error C1 forbids for a quiz score — a signal that measures one thing (does this look like the right job title) standing in for a signal that measures another (can this learner write the artifact).
5. **C5 — A signal that proves a phase-1 skip attempt was denied must identify the learner and the module requested without carrying the diagnostic's item text, answer content, or a badge image.** The point of `phase1_skip_denied` is to let an auditor confirm the deny fired; it is not evidence that needs the quiz's own content to be convincing, and pasting that content into a ticket to "prove" the denial happened — the item text, the answer key, the vendor's certificate screenshot — leaks exactly the practice material this course keeps out of learner-facing files elsewhere, for the same reason the assessment items and their answer keys live in different, separately-scoped locations. Fixing the skip predicate while regularly leaking quiz content through its own audit trail replaces one honesty problem with a confidentiality one.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 5 Verify | `test_high_quiz_score_is_not_authorization`, `test_low_score_does_not_skip`, `test_boundary_old_vulnerable_threshold_is_still_denied`, `test_negative_score_is_malformed_and_still_denied`, `test_anti_fake_quiz_score_fresh_unused_value_is_denied` (all in `labs/0.2/0.2-bridge/tests/test_diagnostic.py`) | items.md #1 |
| C2 | 1 Property, 2 Model, 4 Build | `test_tooling_bridge_required_for_a_genuine_gap`, `test_tooling_bridge_not_required_when_diagnostic_finds_no_gap`, `test_tooling_bridge_forbidden_outcome_job_title_does_not_override_a_real_gap`, `test_tooling_bridge_missing_diagnostic_fails_safe_to_required`, `test_anti_fake_tooling_bridge_a_different_credential_field` | items.md #2, #3, #5 |
| C3 | 1 Property, 4 Build, 6 Operate | `test_phase1_modules_required_for_a_low_score_with_a_real_tooling_gap`, `test_phase1_modules_forbidden_outcome_high_score_does_not_drop_1_4`, `test_phase1_modules_boundary_at_the_old_vulnerable_threshold`, `test_phase1_modules_malformed_missing_tooling_diagnostic_does_not_crash`, `test_anti_fake_phase1_modules_fast_track_alone_does_not_drop_1_4` | items.md #4 |
| C4 | 1 Property, 2 Model | Not directly code-testable — this claim distinguishes a legitimate narrow use of a work-role description (naming a tooling bridge) from an illegitimate broad one (treating it as Gate 1 evidence); no predicate over a work-role string can encode "which purpose is this being used for." Modeled in `lessons/01-property.md`'s vocabulary-vs-syllabus distinction and `lessons/02-model.md`'s evidence-source table. | items.md #6 |
| C5 | 6 Operate | Not directly code-testable — this fixture has no persisted audit log or ticketing integration for a leaked item-text field to appear in. Modeled in `lessons/06-operate.md`'s signal-design worked example. A future Tier-2 upgrade with a real audit store would let a "signal fields exclude item text" assertion be checked directly. | items.md #8 |

C1, C2, and C3 carry genuine lab assertions — three of five claims, exceeding the ≥2 minimum. C4 and C5 are honestly declared non-code-testable rather than mapped to a fabricated test: C4 is a question about which of two legitimate/illegitimate *purposes* a lookup is serving, which a pure-function fixture with no caller context cannot represent, and C5 needs a persisted signal/audit path this Tier-1 fixture does not have. Item #7 (transfer) is cited separately, against the module's combined transfer outcome below, rather than against any single claim's row, because it exercises C1–C4 together against a changed scenario.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Refuse a diagnostic score, at any value, as authorization to skip modules 1.2, 1.3, 1.4, or Gate 1's evidence review | C1 | `lessons/01-property.md` §A score and an authority map are different kinds of evidence | `lessons/01-property.md` score-100 walkthrough | `lessons/03-break.md` | items.md #1 | `lessons/07-transfer.md` clinic onboarding quiz |
| Grant a tooling-bridge skip only on the diagnostic's own observed gap evidence, never on a job title, vendor certification, or LMS badge claim | C2 | `lessons/01-property.md` §A credential is not a diagnostic | `lessons/02-model.md` evidence-source table | `labs/0.2/0.2-bridge` `tooling_bridge_required` tests | items.md #2, #3, #5 | `lessons/07-transfer.md` vendor cert vs. threat-model review |
| Keep modules 1.2, 1.3, and 1.4 in every learner's required path regardless of score, fast-track flag, or bridge assignment | C3 | `lessons/04-build.md` §Required and bridge are two different sets | `lessons/03-break.md` 1.4-drop counterexample | `labs/0.2/0.2-bridge` `phase1_modules_for_learner` tests | items.md #4 | `lessons/07-transfer.md` |
| Treat the NICE Secure Systems Development work role as informative placement vocabulary, not as Gate 1 evidence or a substitute syllabus | C4 | `lessons/01-property.md` §Vocabulary is not a syllabus | `lessons/02-model.md` work-role-vs-cell table | `lessons/08-review.md` review exercise | items.md #6 | `lessons/07-transfer.md` |
| Record a denied skip attempt without leaking the diagnostic's item text, answer content, or a badge image, and without back-dating Gate 1 | C5 | `lessons/06-operate.md` §A denial that leaks the thing it denies | `lessons/06-operate.md` worked log-line example | `lessons/06-operate.md` practice (draft a deny line) | items.md #8 | `lessons/07-transfer.md` |
| Transfer C1–C4 to a clinic's hiring diagnostic and a vendor certification, naming which claim needs its standard reference swapped | C1–C4 | `lessons/07-transfer.md` | `lessons/07-transfer.md` clinic/vendor-cert walkthrough | `lessons/07-transfer.md` write-up prompts | items.md #7 | (is the transfer task) |

## Known residuals

Genuinely out of scope for this module, with the module that picks each one up:

- Real Git/SQL/HTTP tooling gaps still need bridge units after this module — the diagnostic assigns them, but building the bridge content itself is not this module's evidence. Owned by the bridge units named in the blueprint's entry-profile table (§6), not minted here.
- Memorizing the lab's answer without running it → a residual this module cannot remove by construction; named as a limit in [`lessons/05-verify.md`](lessons/05-verify.md), not solved.
- A real Gate 1 evidence review (grading the actual authority map, trust-boundary diagram, and risk register from 1.2–1.4) is owned by those modules and their own mastery-gate evidence, not by this diagnostic → [1.2 Authority and protection](../../1/1.2/lessons/01-property.md), [1.4 Risk, people, economics, usable security, and resilience](../../1/1.4/lessons/01-property.md).
- A live accessibility audit of an actual LMS diagnostic UI (color-only skip indicators, keyboard reachability) is out of scope for a synthetic course fixture with no UI; named as a limit in `lessons/01-property.md`, revisited when [1.4](../../1/1.4/lessons/01-property.md)'s WCAG-oriented recovery-flow review exists to reuse.

## Invariant prompts

- What must remain true for a 100% quiz?
- What fails if Gate 1 is back-dated?
- What must remain true if a job title, not a diagnostic, is the only evidence offered for a tooling-bridge skip?
- What must remain true of the required-modules set when the bridge set changes?

## Threat-model prompts

- What can a 100% quiz fail to prove about tenant isolation?
- What Git/SQL/HTTP gaps still need a bridge?
- Who benefits from a credential standing in for a diagnostic, and what do they gain if it works?
- Who is harmed if 1.4 is quietly dropped from a fast learner's path?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/0.2/0.2-bridge`. Forbidden: quiz score used as authorization to skip 1.2 / Gate 1; a credential claim used as tooling-diagnostic evidence; an adaptive path that drops 1.4.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

OWASP ASVS is not cited by this module: 0.2 governs a placement process, not an application security property, and mints no ASVS ethics/bridge identifiers (recorded in `content/standards/pins.yaml`'s `owasp-asvs-5.0.0` entry).

- NIST SP 800-181 Rev. 1, Workforce Framework for Cybersecurity (NICE Framework) — **final**, published 16 November 2020. Live-checked against `csrc.nist.gov/pubs/sp/800/181/r1/final` and the NICE Framework Resource Center's work-role listing on 2026-09-18. "Secure Systems Development" is a **work role** in the Design and Development (DD) category ("Responsible for the secure design, development, and testing of systems and the evaluation of system security throughout the systems development life cycle"), not a "competency" or "competency area" as the module's prior text and the blueprint's Phase 0 table both called it. This module cites the work role only as informative placement vocabulary for naming a tooling bridge (C4); it is not Gate 1 evidence and mints no 1.2/1.3/1.4 cell.
- NIST Cybersecurity Framework 2.0 — **final**, published 26 February 2024 (CSWP 29). `GV` (Govern) is used only as an outcome-taxonomy label for "this course's placement process has a governance decision to make," consistent with its use elsewhere in this curriculum (`content/standards/pins.yaml`'s `nist-csf-2.0` entry) — not as a control the diagnostic implements or as evidence of anything CSF itself would score.
- W3C Web Content Accessibility Guidelines 2.2 — **final**, W3C Recommendation, 12 December 2024. Success Criterion 1.4.1 Use of Color (Level A), quoted exactly from `w3.org/TR/WCAG22/` on 2026-09-18: "Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element." Applied narrowly here: if a diagnostic's adaptive-path UI ever shows a skip decision, it must not be color-only ("green = skip Phase 1"), which is the exact failure SC 1.4.1 names, not a claim that this module performs or requires a full accessibility audit.

The prior version of this spec called the NICE work role a "competency," which is not the term NICE itself uses for it (NICE reserves "competency area" for a different grouping mechanism, a cluster of knowledge/skill statements, not a work role). Corrected in this pass; the citation's URL and final status were already accurate.

Pinned in `content/standards/pins.yaml` on 2026-09-18.

## Review triggers

Score grants Phase 1 skip; badge as Gate 1; 1.4 hidden by adaptive path; a credential accepted in place of diagnostic evidence.

## Time budget and SecureCollab

Bridge. Python skip/bridge/required-path predicates stand in for the future site's actual diagnostic; SecureCollab itself does not appear as a system in this module's lab, only as the destination Gate 1 evidence (1.2–1.4) will describe.

## Operational considerations

`phase1_skip_denied`. Audit skipped-module lists on every cohort export. Do not back-date Gate 1. Do not paste quiz item text, answer content, or a badge image into a denial ticket.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: quiz score is not a 1.2 cell |
| 2026-09-18 | Deepen (independent review still required): named five teaching claims (C1–C5) and a coverage contract; C1, C2, and C3 carry lab assertions, C4 and C5 declared honestly non-code-testable with a stated reason each. Upgraded the lab from one predicate and two tests to three predicates and fifteen tests, covering C2 (tooling-bridge evidence) and C3 (1.2/1.3/1.4 never dropped) for the first time, each with its own anti-fake test verified by hand against a specific incomplete fake fix. Corrected the NICE standards citation: "Secure Systems Development" is a NICE work role, not a "competency" as this spec and the blueprint's Phase 0 table both called it; re-verified WCAG 2.2 SC 1.4.1's exact text and CSF 2.0's publication date against their canonical pages. Also corrected a bug shared with 1.4, 2.1, and 4.3 before their independent review: `module.yaml` carried `reviewer: pending independent quality and lab-safety review` with `lastReviewedAt`/`nextReviewAt` set to real dates and no artifact under `content/progress/reviews/` — reverted both to `null` per `metadata-honesty.mdc`. |
