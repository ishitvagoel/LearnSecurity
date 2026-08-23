---
name: author-assessment
description: Pass C — write rubrics, transfer challenges, seeded reviews, and mastery-gate criteria. Keep answer keys under content/assessment/keys/. Use when authoring quizzes, gates, or examiner notes.
---

# Author assessment (Pass C)

## When to use

- Module has Pass B content (or the user is only writing a gate rubric against a completed spec)
- User asks for quizzes, mastery gates, rubrics, seeded code reviews, or answer keys

## Instructions

1. Read the module spec `assessmentBlueprint` and blueprint §10 (evidence categories; four-state gates; no compensating averages).
2. Learner-facing files: `content/modules/<phase>/<id>/assessment/` (prompts, rubrics, evidence checklists). **No answers.**
3. Answer keys, examiner notes, and seeded-finding lists: `content/assessment/keys/<id>.md` only. Never link keys from learner pages or `site/`.
4. Knowledge checks may use an 80% retryable threshold. Practical gates require satisfactory evidence for every critical invariant.
5. Gate results: `not-attempted` | `developing` | `competent` | `transfer-ready`. Core completion will need **Competent** at every gate and **Transfer-ready** at Gates 3, 4, 6, 9, 10, and the capstone.
6. Include at least one transfer challenge (materially changed case).
7. Seeded reviews must list intended findings only in the keys file.
8. Update STATUS `pass: C` after `quality-gate`. Do not claim `transfer-ready` without a transfer artifact.
