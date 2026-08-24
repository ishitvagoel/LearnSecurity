---
name: choreograph-curriculum
description: Single entry skill that sequences all curriculum generation skills in order. Use when the user wants one command to generate the next module or continue the course without picking skills by hand. Invoke with /choreograph-curriculum.
---

# Choreograph curriculum

You are the **conductor**. Do not invent a parallel workflow. Read each listed skill’s `SKILL.md` and execute it fully, in order, before opening the next. Treat those files as the source of procedure; this skill only chooses **which** skills run, **for which module**, and **when to stop**.

## When to use

- User wants a single skill / `/choreograph-curriculum` / “just generate the next piece”
- User does not want to run `next-iteration`, `author-module-spec`, etc. separately

If the user names a specialist skill instead, do **not** take over; let that skill run alone.

## Modes

Read the user message. Default is `auto`.

| Mode | How the user asks | What you run |
|---|---|---|
| `auto` | `/choreograph-curriculum` with no extra scope | Pilot-aware (below) |
| `pass` | “this pass only” / “spec only” | Skills for the current STATUS pass only, then stop |
| `module` | “whole module” / “A through C” | Full A→C pipeline for **one** module |
| `pilot` | “pilot phase 1” | Follow `pilot-phase-1` (Pass A for 1.1–1.4 only) |
| `continue` | “keep going” / “N modules” | Repeat `auto` or `module` up to `N` (default **1** if they said keep going without N; **never** more than **4** modules in one invocation) |

**Pilot-aware `auto`:** If any of 1.1–1.4 still have `pass: none` or missing spec files, run only the **Pass A chain** for the next Phase 1 (then Phase 2) module. Do not start Pass B/C until Pass A exists for 1.1–1.4 **and** 2.1–2.4, unless the user explicitly asked for `module` (whole A→C) or Pass B/C.

Never start Pass D (the website) **from this skill**. Never skip gates. Never generate the entire 50-module course in one run.

If `STATUS.yaml` shows Pass E for all units and `revision.remaining` is non-empty, **stop generation** and tell the user to run `/deepen-curriculum` (or `/goal run /deepen-curriculum until revision.remaining is empty`). Do not invent a parallel generation pipeline.

## Pipeline (canonical order)

Skill files (read and follow, do not paraphrase away their constraints):

1. [next-iteration](../next-iteration/SKILL.md) — pick legal `id` + pass; if this choreographer is running, **do not stop after the brief**
2. [standards-pin](../standards-pin/SKILL.md) — before any write/revise of that module
3. [author-module-spec](../author-module-spec/SKILL.md) — if Pass A is missing or `pass` is A
4. [quality-gate](../quality-gate/SKILL.md) — after Pass A (spec completeness)
5. [author-lesson](../author-lesson/SKILL.md) — only if this run includes Pass B
6. [author-lab](../author-lab/SKILL.md) — Pass B labs; skip only if the spec’s lab briefs are explicitly “none”
7. [author-assessment](../author-assessment/SKILL.md) — only if this run includes Pass C
8. [spiral-revisit](../spiral-revisit/SKILL.md) — after B/C or when assumptions changed
9. [quality-gate](../quality-gate/SKILL.md) — again after B/C
10. [coverage-audit](../coverage-audit/SKILL.md) — only when a **phase** just completed Pass A for every module in that phase, or the user asked for an audit

Subagents those skills name (`curriculum-architect`, `standards-auditor`, `quality-reviewer`, `lab-safety-reviewer`) still run **readonly** at the points those skills require.

Hard stops (finish the current skill’s files, write STATUS, report, **do not** start another module):

- Lab-safety or quality-gate **blocker**
- Illegal sequencing / skipped gate (`next-iteration` or `curriculum-architect` refuse)
- Missing network when `standards-pin` cannot verify and the module needs a live pin — record `unverified` and continue only if the blueprint snapshot already lists that source
- User-specified module cap reached
- You are about to leave the Phase 1–2 Pass A pilot without an explicit `module` / Pass B request

## Each step

1. Announce: `Running <skill> for <id> (Pass <X>)`.
2. Read that skill’s `SKILL.md` and any `references/` or `assets/` it points at.
3. Do the work.
4. If the skill fails its own quality/safety bar, stop the pipeline and report what to fix. Do not “push through” with lesson prose after a failed spec.

## STATUS

Update [`content/progress/STATUS.yaml`](../../../content/progress/STATUS.yaml) after each completed pass, not only at the end. Set `next` to the following legal unit when you stop.

## Session report (required)

When you stop, print:

- Mode used
- Module id(s) touched
- Skills actually run (and any skipped, with reason)
- Files written
- Blockers
- Exact next `/choreograph-curriculum` suggestion (e.g. next module spec, or Pass B for 1.1 after the pilot)
