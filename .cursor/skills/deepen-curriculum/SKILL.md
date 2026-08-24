---
name: deepen-curriculum
description: Post-generation conductor — revise map-complete modules to 1.1-quality publishable lessons and labs. Use after Pass A–E when STATUS has no queued generation unit. Invoke with /deepen-curriculum. Designed for /goal run /deepen-curriculum until remaining is empty.
---

# Deepen curriculum

You are the **revision conductor**. Generation (`choreograph-curriculum`, Pass A–E) is finished. This skill does **not** invent modules, skip mastery gates, or start a new syllabus. It deepens existing units until they meet the blueprint §16 bar at the same instructional density as the **reference module `1.1`**.

Use with Goal, for example:

```text
/goal run /deepen-curriculum until content/progress/STATUS.yaml revision.remaining is empty and every listed unit is depth: publishable
```

## When to use

- `STATUS.next.skill` is `deepen-curriculum`, or generation `next.id` is null and Pass E exists
- User wants `/deepen-curriculum` or “make the thin modules as good as 1.1”
- `/goal` should keep iterating this skill across turns

Do **not** use this skill to:

- Author a missing Pass A spec (that is `author-module-spec` / `choreograph-curriculum`)
- Mark mastery gates 0–10 or milestones M0–M5 complete without learner/product evidence
- Deploy Vercel (platform work, not this skill)
- Put weaponized payloads or live-target steps in learner-facing pages

If the user names an inner skill (`author-lesson`, `quality-gate`, …), do **not** take over.

## Modes

Default is `auto`.

| Mode | How the user asks | What you run |
|---|---|---|
| `auto` | `/deepen-curriculum` | One module from `revision.remaining` (or `next.id`) |
| `module` | a named id | That id only, then stop |
| `continue` | “keep going” / `/goal` | Repeat `auto` up to **4** modules per invocation unless Goal overrides across turns |

## Pick the unit

1. Read [`content/progress/STATUS.yaml`](../../../content/progress/STATUS.yaml) `revision` and `next`.
2. Honor `next.id` if it is still in `revision.remaining`.
3. Otherwise take the first id in `revision.remaining`.
4. **Reference:** always read `content/modules/1/1.1/` lessons + `labs/1.1/` before rewriting. That density is the bar, not the thin `01-property.md` templates.
5. Refuse if Pass A–C files are missing for that id (send the user back to `choreograph-curriculum`).

## Pipeline (canonical order)

Read and execute each skill’s `SKILL.md` (do not paraphrase away constraints):

1. [standards-pin](../standards-pin/SKILL.md) — before a material rewrite
2. [author-module-spec](../author-module-spec/SKILL.md) — **only** to thicken `spec.md` / `module.yaml` (no new lesson prose in this step)
3. [author-lesson](../author-lesson/SKILL.md) — replace generic seven-step stubs with system-specific SecureCollab (or elective-system) prose
4. [author-lab](../author-lab/SKILL.md) — replace slogan-only YAML fixtures when the module needs a **structural** local break/fix; keep authorized scope; no public targets
5. [author-assessment](../author-assessment/SKILL.md) — rewrite rubric + keys to match the deepened lessons (keys stay under `content/assessment/keys/`)
6. [spiral-revisit](../spiral-revisit/SKILL.md) — if assets, authority, or boundaries changed
7. [quality-gate](../quality-gate/SKILL.md) — 13-point bar vs the rewritten files; delegate `quality-reviewer` and `lab-safety-reviewer`
8. [coverage-audit](../coverage-audit/SKILL.md) — only if this module closed a phase’s remaining list, or the user asked

See [references/publishable-depth.md](references/publishable-depth.md) for the pass/fail definition of `depth: publishable`.

## STATUS

After a successful deepen of `id`:

- Set that unit’s `depth: publishable` (create the field if missing)
- Remove `id` from `revision.remaining`
- Set `next.id` to the new first remaining id, `skill: deepen-curriculum`, `pass: revise`
- If `revision.remaining` is empty: `next.id: null`, note that deepening is complete

Do not change `pass: E` backward. Do not set gate/milestone `quality` to competent.

## Hard stops

Finish the current module’s files, write STATUS, report, **do not** start another module:

- Lab-safety or quality-gate **blocker**
- Missing network for a pin the module newly needs — record `unverified` only if the blueprint snapshot already lists the source
- Four-module cap (unless a Goal turn is still working the same objective)
- Request to skip a mastery gate or treat Top 10 as the outline

## Each step

1. Announce: `Running <skill> for <id> (revise / deepen)`.
2. Read that skill file.
3. Do the work against **this module’s** outcomes and invariants, not a cloned 1.1 catalogue.
4. Schema-validate `module.yaml`.

## Session report (required)

- Mode
- Module id(s) deepened
- Skills run / skipped
- Files written
- Blockers
- Exact next command: `/deepen-curriculum` or `/goal run /deepen-curriculum until revision.remaining is empty`
