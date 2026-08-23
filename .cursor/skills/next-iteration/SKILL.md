---
name: next-iteration
description: Read curriculum STATUS.yaml, choose the next allowed Pass A/B/C unit from the dependency graph, print a one-screen brief, and refuse skipped gates. Use at the start of every authoring session or when the user asks what to generate next.
---

# Next iteration

## When to use

- Start of a curriculum generation session
- User asks “what’s next?” or to continue generating content
- STATUS.yaml may be stale after a partial pass

## Instructions

1. Read [`content/progress/STATUS.yaml`](../../../content/progress/STATUS.yaml) and the blueprint [`secure-application-engineering-curriculum-blueprint.md`](../../../secure-application-engineering-curriculum-blueprint.md) §7 graph.
2. Honor `next` if it is still legal. Recalculate if STATUS is inconsistent (wrong pass before prerequisites, Phase 8 before identity/data/API foundations, electives before Phase 7, Pass D before Phase 1–2 pilots).
3. Dependency rules:
   - Hard phase order: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 9 → 10 → 11. Phase 8 depends on 5 and 7; it may wait for a web/API milestone.
   - Electives E1–E6 only after Phase 7.
   - Within a module: Pass A before B before C. Do not write lesson prose during Pass A.
   - Pilot: finish Pass A for Phase 1 (1.1–1.4) then Phase 2 (2.1–2.4) before mass-authoring later phases. Orientation 0.1–0.2 may be specified in the same pilot wave if the user asks for Phase 0.
   - One unit per session unless the user explicitly names a larger slice (e.g. `/pilot-phase-1`).
4. **Refuse** requests to skip a mastery gate, reorder around Top 10 lists, or generate Pass D site code before pilots exist. Explain the blocker using STATUS.
5. Print a one-screen brief:
   - `id`, title, pass (`A|B|C|...`)
   - prerequisites that must already be `pass: A` (or later)
   - skill to invoke next (`author-module-spec`, `author-lesson`, `author-lab`, `author-assessment`, `standards-pin`, `spiral-revisit`, `quality-gate`)
   - output paths
   - lab-safety reminder if Pass B labs
6. Do not author content in this skill. Stop after the brief unless the user already asked to execute that unit in the same message, **or** the parent skill is `choreograph-curriculum` (then return the brief to the conductor and let it run the next skills).
7. After a unit is completed by another skill, update `next` and the unit’s `pass` / `quality` fields. Do not mark `competent` without `quality-gate`.
