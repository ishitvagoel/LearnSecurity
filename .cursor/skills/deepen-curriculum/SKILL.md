---
name: deepen-curriculum
description: Post-generation conductor — sequence modules through deepen-module until every unit meets the publishable teaching bar. Use after Pass A–E when STATUS has no queued generation unit. Invoke with /deepen-curriculum. Designed for /goal run /deepen-curriculum until remaining is empty.
---

# Deepen curriculum

You are the **revision conductor**. Generation (`choreograph-curriculum`, Pass A–E) is finished. This skill does not invent modules, skip mastery gates, or start a new syllabus. It sequences existing units through [`deepen-module`](../deepen-module/SKILL.md) until they meet the blueprint §16 bar and the prose bar in `lesson-prose.mdc`.

Use with Goal, for example:

```text
/goal run /deepen-curriculum until content/progress/STATUS.yaml revision.remaining is empty
```

## The bar

**Reference modules: `content/modules/1/1.2` and `content/modules/1/1.3`.** Read one before conducting.

Module `1.1` is **not** the bar. At 566 words per lesson it sits with the thin modules and is queued for deepening in batch B1. Earlier revisions of this skill named 1.1 as the reference, and modules deepened against it inherited its thinness — if a module claims to have matched the reference, check which reference.

## When to use

- `STATUS.next.skill` is `deepen-curriculum`, or generation `next.id` is null and Pass E exists
- User wants `/deepen-curriculum` or "make the thin modules as good as 1.2"
- `/goal` should keep iterating across turns

Do **not** use this skill to author a missing Pass A spec, to mark gates or milestones complete without evidence, or to deploy Vercel. If the user names an inner skill, do not take over.

## Prerequisites

Before conducting **any** module, confirm workstream **W0** has landed: `scripts/lint_content.py` and `scripts/run_labs.sh` exist and are calibrated (see [`content-lint`](../content-lint/SKILL.md)). Without a mechanical gate, a bad template propagates — which is how 54 modules reached their current state. If W0 is missing, say so and stop.

## Batch order

Later modules cite earlier ones, so deepening out of order creates links into shallow pages.

| Batch | Modules | Note |
|---|---|---|
| **B0 pilot** | `1.4`, `2.1`, `4.3` | Validates the runbook before scale. **Must pass independent review before B1 opens.** |
| B1 | `0.1`, `0.2`, `1.1` | Includes the mis-cited reference module |
| B2 | `2.2`–`2.4`, `3.1`–`3.4` | Heavy downstream citation |
| B3 | `4.1`–`4.5` | `4.5` needs the PKCE / `state` correction carried through all eight lessons |
| B4 | `5.1`–`5.5` | `5.2` already has a real AEAD fixture — use as the Tier 2 template |
| B5 | `6.1`–`6.7` | Highest payoff from naming XSS/CSRF/SSRF/SQLi directly |
| B6 | `7.1`–`7.4`, `9.1`–`9.5` | |
| B7 | `8.1`–`8.5` | Blocked until the phase-8 Kotlin decision is recorded in STATUS |
| B8 | `10.1`–`10.5` | |
| B9 | `E1`–`E6` | |
| B10 | `11` | Capstone, after B1–B8 |

Up to four modules may run in parallel, one per session, never two in the same batch that cite each other. A batch closes when every module in it has a passing review artifact.

## Modes

Default is `auto`.

| Mode | How the user asks | What you run |
|---|---|---|
| `auto` | `/deepen-curriculum` | One module from the current batch |
| `module` | a named id | That id only, then stop |
| `continue` | "keep going" / `/goal` | Repeat `auto` up to **4** modules per invocation unless Goal overrides across turns |

## Pick the unit

1. Read [`content/progress/STATUS.yaml`](../../../content/progress/STATUS.yaml) `revision` and `next`.
2. Honor `next.id` if it is still in `revision.remaining` **and** in the current open batch.
3. Otherwise take the first id in the current batch.
4. Refuse if Pass A–C files are missing for that id — send the user to `choreograph-curriculum`.

## Pipeline

Per module, run [`deepen-module`](../deepen-module/SKILL.md) end to end. It internally sequences `standards-pin`, lesson rewriting, [`upgrade-lab`](../upgrade-lab/SKILL.md), [`author-item-bank`](../author-item-bank/SKILL.md), and validation.

After the module returns, and only then:

1. [`spiral-revisit`](../spiral-revisit/SKILL.md) — if assets, authority, or boundaries changed
2. [`quality-gate`](../quality-gate/SKILL.md) — delegate `quality-reviewer` and `lab-safety-reviewer` as **separate** sessions
3. [`coverage-audit`](../coverage-audit/SKILL.md) — only if this module closed a batch, or the user asked

## STATUS

After `deepen-module` returns, the conductor may update **only**:

- `next.id` → the next id in the batch
- `next.skill: deepen-curriculum`, `next.pass: revise`
- a dated note recording which module was deepened and that review is pending

The conductor **may not** set `depth: publishable`, `quality: competent`, `quality: transfer-ready`, `reviewer`, `lastReviewedAt`, `nextReviewAt`, or `status: published`. Those belong to the independent reviewer that produced the artifact under `content/progress/reviews/`, or to the human.

This restriction is `quality-gate` step 5, `references/publishable-depth.md`, and `metadata-honesty.mdc`. An earlier revision of this skill instructed the conductor to set `depth: publishable` after a successful pass; that instruction is withdrawn, and it is the direct cause of 53 modules carrying review dates for reviews that never happened.

Remove an id from `revision.remaining` only once its review artifact exists and records no blockers.

## Hard stops

Finish the current module's files, write the permitted STATUS fields, report, and **do not** start another module:

- W0 scripts missing or uncalibrated
- Lab-safety or quality-gate **blocker**
- **Two consecutive modules in a batch fail independent review on the same dimension** — the runbook or a linter rule is wrong; fix that instead of authoring a third failure
- B0 pilot not yet reviewed, and the request is to open B1
- Phase 8 requested before the Kotlin decision is recorded
- Missing network for a pin the module newly needs
- Four-module cap
- Request to skip a mastery gate or treat Top 10 as the outline

## Session report

Mode · batch · module ids deepened · defect IDs addressed · validation output · review requests handed over · blockers · exact next command.
