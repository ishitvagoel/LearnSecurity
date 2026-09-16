---
name: deepen-module
description: Rewrite one module to publishable teaching depth — teaching claims, coverage contract, eight rewritten lessons, an upgraded lab, an item bank, honest metadata, and a request for independent review. Use when deepening, thickening, or fixing the quality of a named module.
---

# Deepen one module

One module is one unit of work: one branch, one commit, one review artifact. Expect 3–6 hours of model time. Do not batch two modules into one pass — that is how 54 template fills happened.

Rationale and evidence: [`content/progress/content-quality-improvement-plan-2026-09-16.md`](../../../content/progress/content-quality-improvement-plan-2026-09-16.md). This skill is the operative procedure; you do not need to read the plan to execute it.

## When to use

- `deepen-curriculum` selected a module, or the user named one
- A review artifact returned blockers on a module
- The user asks to make a module "as good as 1.2/1.3"

Do **not** use this skill to author a module that has no Pass A spec — that is `author-module-spec`.

## Binding rules

`lesson-prose.mdc` · `lab-realism.mdc` · `assessment-items.mdc` · `metadata-honesty.mdc` · `lab-safety.mdc` · `module-content.mdc`

**You may not approve your own output.** Never set `depth`, `quality`, `reviewer`, `lastReviewedAt`, `nextReviewAt`, or `status: published`. Step 9 hands that to a separate reviewer.

## Step 0 — Read

Branch `deepen/<module-id>`. Read, in this order, in full:

1. Blueprint §§3, 9, 10, 16
2. `content/modules/<phase>/<id>/spec.md` and `module.yaml`
3. All eight lessons, the lab, the rubric, and `content/assessment/keys/<id>.md`
4. `content/standards/pins.yaml`
5. **`content/modules/1/1.3/lessons/01-property.md` and `02-model.md`** — the quality bar

A directory listing or a generated summary is not reading. Module `1.1` is not the bar; it is itself queued for deepening.

## Step 1 — Pin standards

Run [`standards-pin`](../standards-pin/SKILL.md). Confirm every `requirementIds` entry still exists at the pinned version and that `status` is accurate. Record `reviewedAt`. If a standard moved, write a migration note. Do not proceed on a stale pin.

## Step 2 — Write the teaching claims

This is the step that fixes the module, and the one most often skipped.

Most modules currently teach **one narrow predicate** across all eight lessons — `5.2` is "Base64 is not encryption", `4.5` is an `aud` comparison, `4.3` is a query-string check. The title promises a topic; the lessons deliver a boolean.

Replace it with **three to five numbered teaching claims** in `spec.md`, ordered by dependency. Each is one falsifiable sentence:

> For `<asset>` in `<the reference system at this phase>`, `<actor with these capabilities>` cannot `<effect>`, because `<the check that must hold>`. If `<context>` is missing, the answer is no.

Worked example — `4.3 Sessions, cookies, and tokens`, which today teaches only claim 1:

1. A session secret placed in a URL is no longer a secret, because the URL is copied into access logs, `Referer`, history, and screenshots.
2. A session identifier must be unguessable **and** bound to the authentication event that minted it, so a pre-authentication identifier cannot survive login.
3. A session needs both an idle and an absolute lifetime, because an unbounded session turns a one-time theft into permanent access.
4. Logout and revocation must invalidate server-side state, because a token the server still honours is not revoked.
5. `HttpOnly`, `Secure`, and `SameSite` each defend a different attacker capability, and naming one does not cover the others.

Then map each claim to loop steps, to assessment items, and to lab assertions. **At least two claims must be exercised by the lab.**

A claim with no lab assertion and no assessment item is not taught. Build the evidence or delete the claim — do not list it as a "residual" and move on.

## Step 3 — Coverage contract

Copy [`assets/coverage-contract.md`](assets/coverage-contract.md) into `spec.md`. One row per outcome in `module.yaml`; columns are explanation file, worked example, practice, assessment item ID, transfer task. **Any empty cell is a blocker.** This is `quality-gate` step 2 made reviewable.

## Step 4 — Rewrite the eight lessons

Follow [`references/lesson-shapes.md`](references/lesson-shapes.md) for what each file must do, and [`references/style-rules.md`](references/style-rules.md) for how to write it.

**Rewrite; do not patch.** The existing files are template fills — cheaper to replace than to repair, and patching preserves the fragment style that is the defect.

## Step 5 — Upgrade the lab

Run [`upgrade-lab`](../upgrade-lab/SKILL.md). Default to Tier 2.

## Step 6 — Author the assessment

Run [`author-item-bank`](../author-item-bank/SKILL.md). Rewrite the rubric to describe module-specific evidence and delete the "session worksheet" reference.

## Step 7 — Correct metadata

Per `metadata-honesty.mdc`: rewrite templated outcomes as observable behaviours, recompute `estimatedMinutes` from the formula, append a changelog entry naming the defect IDs fixed. Leave every review and maturity field untouched.

## Step 8 — Validate, and paste the output

```bash
python scripts/lint_content.py content/modules/<phase>/<id> --no-baseline   # expect clean
bash scripts/run_labs.sh <id>                                              # vulnerable fails, fixed passes
npm --prefix site run build

python scripts/lint_content.py --update-baseline    # the count must FALL
git diff --stat scripts/lint_baseline.json
```

A deepened module must be clean with `--no-baseline`, not merely clean against the baseline. The baseline is for work not yet done; never add a finding to it to make this module pass.

Run the lab pair in a clean environment. Paste the **exact commands and their real output** into the review request. A described result is not a result; if a command was not run, say so.

## Step 9 — Request independent review

A **different** agent or session runs [`quality-reviewer`](../../agents/quality-reviewer.md), and [`lab-safety-reviewer`](../../agents/lab-safety-reviewer.md) for executable labs. It writes `content/progress/reviews/<id>-<YYYY-MM-DD>.md` using [`assets/review-artifact.md`](assets/review-artifact.md).

Hand over: the commit SHA, the files changed, the validation output, and the teaching claims from step 2. Do not summarize your own work as passing.

## Step 10 — STATUS

Only the reviewer or the human updates `content/progress/STATUS.yaml`, `module.yaml` `reviewer`/`lastReviewedAt`, `depth`, or `quality`. If review returned blockers, fix them and return to step 8 — the review artifact records the second pass.

## Report

Module id · teaching claims written · lab tier before and after · item count · defect IDs addressed · validation output · blockers · the exact review request handed over.
