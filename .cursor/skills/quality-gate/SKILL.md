---
name: quality-gate
description: Apply the semantic publishability bar and four-state mastery model before marking a module or gate complete. Use before updating STATUS to competent or publishable and after a material revision.
---

# Quality gate

## When to use

- Before setting a module to quality competent or depth publishable
- After Pass A, B, or C, and after any material rewrite
- When a user asks whether a module is genuinely explanatory, deep, or ready to teach

## Required inputs

Read the target specification, module.yaml, every lesson, the lab README and implementation, the learner assessment, the isolated examiner key, the applicable standards pins, and references/publishability.md. A directory listing or generated summary is not review evidence.

## Procedure

1. Validate module.yaml against content/schema/module.schema.json.
2. Build a coverage contract from the module outcomes: for every outcome, point to an explanation, a worked example, learner practice, feedback or rubric evidence, and a transfer task. Missing cells are blockers.
3. Score every semantic dimension in references/publishability.md from 0 to 3. Cite file paths and concrete passages or test results. Word count, headings, schema validity, and unique strings are diagnostics only.
4. Execute the lab in a clean local environment. Record the exact commands and results for vulnerable and fixed variants. The vulnerable variant must fail for the intended forbidden outcome; the fixed variant must pass for the structural reason taught.
5. Delegate a read-only quality-reviewer after the authoring pass. For executable labs, also delegate a read-only lab-safety-reviewer. Authors and generators cannot approve their own output.
6. Record the independent result at content/progress/reviews/<module>-<YYYY-MM-DD>.md. The record must identify the reviewed commit or branch, files inspected, per-dimension scores, blockers, lab commands/results, reviewer identity, and an independence statement.
7. Update STATUS only after blockers are resolved:
   - quality developing if any required dimension is below 2
   - quality competent when every required dimension is at least 2
   - depth publishable only when every required dimension is at least 2, all critical dimensions are at least 2, the clean lab pair passes, and the independent review artifact exists
   - quality transfer-ready only after satisfactory evidence from the materially changed transfer task
8. Do not average away a failed critical dimension. One critical failure blocks publication.

Pass A can be competent for specification completeness, but its depth remains map-complete. Pass E records that an independent review happened; it does not imply the review passed.
