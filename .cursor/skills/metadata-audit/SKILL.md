---
name: metadata-audit
description: Mechanical bulk correction of module.yaml review fields, templated outcomes, and time estimates across all modules. Use for workstream W2, or when metadata claims a review or a duration that did not happen.
---

# Metadata audit

A one-shot, low-risk, high-value bulk pass. Run it early — it removes false review dates immediately and does not depend on any authoring work.

## The problem being fixed

- **53 of 57** modules carry `reviewer: pending independent quality and lab-safety review` alongside `lastReviewedAt: '2026-08-24'` and `nextReviewAt: '2027-02-24'`. A review date for a review that did not happen is the one thing this repository's governance model exists to prevent.
- **21 modules** carry `Demonstrate: <module title>` as their first outcome, plus four boilerplate lines shared verbatim. That is the title with a verb glued on; it cannot be assessed, so the coverage contract cannot be built from it.
- **47 modules** claim `estimatedMinutes: 240` for ~460-word lessons and a two-line lab.

## Procedure

Run across all 57 `module.yaml` files. Change nothing else.

1. **Review fields.** Where `reviewer` contains `pending`, delete `lastReviewedAt` and `nextReviewAt`. Do not invent a reviewer to keep the date. Leave the four genuinely reviewed modules alone — check `content/progress/reviews/` for the artifact before deciding.
2. **Outcomes.** Rewrite every `Demonstrate: <title>` outcome, and the shared boilerplate lines, as observable behaviours an assessment item could evidence:
   - Bad: `Demonstrate: Sessions, cookies, and tokens`
   - Good: `Given a session parser, identify which of four channels can carry a session secret and justify the ranking.`
   If you cannot state what a learner would *do*, the module's teaching claims are missing — leave a `TODO(D3)` and flag it for `deepen-module` step 2 rather than inventing an outcome.
3. **Estimates.** Recompute with the `metadata-honesty.mdc` formula from what the module actually contains today. Most drop well below 240. That is the honest number until the content exists; it rises again when `deepen-module` adds the content.
4. **Changelog.** One dated entry per module naming the defect IDs: `D12 metadata honesty: cleared unearned review dates; rewrote templated outcomes; recomputed estimate`.
5. **Validate.** `python scripts/lint_content.py --rules L012,L013,L014,L017` — expect clean.

## Boundaries

- Do not touch `depth`, `quality`, or `status`. Clearing a false review date is a correction; granting maturity is a review decision.
- Do not touch lesson prose, labs, or assessments. Those are `deepen-module`'s work and mixing them makes this pass unreviewable.
- One commit per phase keeps the diff readable across 57 files.

## Report

Modules changed · dates cleared · outcomes rewritten · outcomes left as `TODO(D3)` · estimate range before and after.
