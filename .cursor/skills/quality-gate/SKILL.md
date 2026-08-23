---
name: quality-gate
description: Apply the 13-point publishability bar and four-state mastery model before marking a module or gate complete. Use before updating STATUS to competent or after Pass A/B/C for a module.
---

# Quality gate

## When to use

- Before setting a module `quality` to `competent` or `transfer-ready`
- After Pass A, B, or C for a unit
- User asks if a module is publishable

## Instructions

1. Load `references/publishability.md` and the target files (`spec.md`, `module.yaml`, lessons, labs, assessment).
2. Check schema validity for `module.yaml` against `content/schema/module.schema.json`.
3. Score each of the 13 publishability items: `pass` | `fail` | `n/a` (N/A allowed only when that pass does not yet exist, e.g. executable labs during Pass A).
4. Delegate **`quality-reviewer`** for an independent pass. Do not rewrite content in the same breath as the review; report gaps first.
5. For labs, also delegate **`lab-safety-reviewer`**.
6. Update `content/progress/STATUS.yaml`:
   - `quality: developing` if any required item fails
   - `quality: competent` if all required items for this pass pass
   - `quality: transfer-ready` only if a transfer challenge exists and is scoped
7. Never use averaging to hide a failed critical invariant.

Pass A can be `competent` for specification completeness without lessons. It cannot be marked publishable as a lesson.
