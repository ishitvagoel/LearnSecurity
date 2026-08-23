---
name: author-module-spec
description: Pass A — write one module specification (objectives, misconceptions, lab briefs, assessment blueprint, standards refs) with no lesson prose. Use when generating or revising a module spec or module.yaml.
---

# Author module specification (Pass A)

## When to use

- `next-iteration` selected Pass A for a module ID
- User asks for a module spec, blueprint, or metadata for a curriculum module
- Revising an existing spec after a standards or sequencing change

## Instructions

1. Run **`standards-pin`** first if pins for this module’s anchors are missing or stale.
2. Read the blueprint row for this module (phase table in §7), the template [`content/templates/module-spec.md`](../../../content/templates/module-spec.md), and [`content/schema/module.schema.json`](../../../content/schema/module.schema.json).
3. Create or update:
   - `content/modules/<phase>/<id>/spec.md` (from the template)
   - `content/modules/<phase>/<id>/module.yaml` (must validate against the schema)
4. Fill every template section. Include: objective hierarchy, prerequisite concepts, misconception list, concept map, invariant prompts, lesson inventory (titles only), lab **briefs** (not implementations), assessment blueprint, exact standards references with version/status/url, update triggers, time budget, route tags, staged-release / SecureCollab dependencies.
5. **Do not** write lesson prose, tutorials, exploit walkthroughs, complete code, quizzes with answers, or vendor setup novels.
6. Use the seven-step loop as the intended lesson inventory structure (see `references/seven-step-loop.md`).
7. Map evidence to blueprint “Evidence produced” and the relevant mastery gate.
8. One module per invocation unless the user named a set (e.g. Phase 1 pilot).
9. Update `content/progress/STATUS.yaml`: set this module `pass: A`, `quality: developing` until `quality-gate` runs. Set `next` to the following legal unit.
10. Point the parent agent at `quality-gate` before calling the spec done.

## Output paths

Phase folders: `0`–`11`, electives under `content/modules/e/<id>/` (e.g. `e/E1`).
