---
name: author-lesson
description: Pass B — write learner-facing lesson objects for one module using the seven-step learning loop. Use when authoring tutorials, concept models, or diagrams after a completed module spec.
---

# Author lesson content (Pass B)

## When to use

- Module already has Pass A `spec.md` and `module.yaml`
- User asks for lessons, concept models, or learner-facing prose for a module ID

## Instructions

1. Refuse if Pass A is missing. Direct the user to `author-module-spec`.
2. Read the module spec, STATUS, `references/learning-object-mix.md`, and the **`lesson-prose.mdc` rule** — it sets the prose bar (derivation before assertion, dual-form vocabulary, diagram minimums, one scope statement, word floors) that blueprint §16 does not cover. Read `content/modules/1/1.3/lessons/01-property.md` as the quality reference; `1.1` is not the bar.
3. Write objects under `content/modules/<phase>/<id>/lessons/`. Prefer one file per learning object. Update `module.yaml` `learningObjects` and `status` as you go.
4. Every substantive lesson:
   - Starts with a **property or question**, not a product command
   - Names attacker capabilities and trust assumptions
   - Distinguishes root cause, preconditions, impact, prevention, detection, recovery
   - Separates framework defaults from application guarantees
   - Includes a safe practice task and a transfer task
   - Labels standards with version and status, in the lesson body (`**Standards:**`), not only in `module.yaml`
   - Meets `lesson-prose.mdc`: ≥900 words of body prose, median sentence ≥11 words, <8% of sentences ≤5 words, at most three rejected alternatives, exactly one authorized-scope statement, titled links instead of bare module IDs, and diagrams that meet the kind and node minimums
5. Target mix (~authoring time, not grading): 20% models/readings, 45% building and break/fix, 20% verification/review, 15% reflection/operations/assessment.
6. **Break/fix implementations** go through **`author-lab`** into `labs/`. Lessons may describe cause and the fix at a teaching level; they must not dump weaponized payloads or live-target steps.
7. Do not write answer keys into lesson files.
8. Validate with `python scripts/lint_content.py content/modules/<phase>/<id>` before handing off.
9. After lessons for this module, run `spiral-revisit` if SecureCollab assumptions changed, then `quality-gate`.
10. Update STATUS: `pass: B` only when lessons **and** required labs for the spec exist (labs may still be in progress—leave `pass: A` and note `notes` if labs are the remaining unit).

Stack defaults: FastAPI + PostgreSQL + TypeScript/Next.js; Android/Kotlin when mobile appears.

To rewrite an existing thin module rather than author a new one, use [`deepen-module`](../deepen-module/SKILL.md) — it carries the teaching-claim, coverage-contract, lab-tier, and item-bank steps this skill does not.
