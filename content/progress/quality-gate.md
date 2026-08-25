# Quality-gate record (Pass C)

> **Historical record.** This presence-oriented Pass C stamp is not semantic approval of the later bulk-generated lessons. It is superseded for depth decisions by [the 2026-08-25 depth audit](depth-audit-2026-08-25.md) and per-module independent reviews.

Date: 2026-08-23  
Reviewers recorded on each `module.yaml`: `quality-reviewer (Pass C); lab-safety-reviewer (local YAML fixture)`.

Scope: all 50 core modules (`0.1`–`10.5`), capstone `11`, electives `E1`–`E6`. Pass D site and Pass E review recorded 2026-08-23.

## Method

For each unit, score the 13 publishability items for **this pass** (lessons + authorized local YAML claim lab + assessment). Labs are local fixtures that fail on mechanism slogans and pass on property-shaped claims — not live-target or weaponized payloads.

| # | Item | Pass C result |
|---|---|---|
| 1 | Property or question first | pass (lesson LO-01) |
| 2 | Attacker capabilities and trust | pass |
| 3 | Root cause / preconditions / impact / prevention / detection / recovery | pass (table in lessons) |
| 4 | Current standards with version/status | pass (module.yaml `standardsRefs`) |
| 5 | Mechanism limits | pass |
| 6 | Practice + transfer | pass (LO practice + LO-07) |
| 7 | Forbidden outcomes / failure behavior | pass (lab tests) |
| 8 | Framework defaults vs application guarantees | pass |
| 9 | No universal claims where risk-based selection is required | pass |
| 10 | No live-target or real sensitive data | pass |
| 11 | Executable labs in a clean environment | pass (pytest `--claim`; vulnerable fails, fixed passes) |
| 12 | Usability/accessibility of human-in-the-loop controls | pass (WCAG 2.2 note; N/A depth for modules with no human control beyond lab honesty) |
| 13 | Reviewer and review date | pass (`lastReviewedAt: 2026-08-23`) |

No compensating averages. Schema: every `module.yaml` validates against `content/schema/module.schema.json`.

## Per-unit stamp

All 57 units: `pass: E`, `quality: competent` in `STATUS.yaml` (generation coverage). Mastery **gates** and product **milestones** remain `not-attempted` until learner/product evidence exists.
