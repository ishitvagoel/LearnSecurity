---
name: author-item-bank
description: Pass C — author 6-10 module-specific assessment items with distractor rationales in the isolated key, replacing generic prompts and checklist rubrics. Use when a module needs real knowledge checks or its rubric cites the non-existent session worksheet.
---

# Author item bank

`author-assessment` owns rubrics, gates, and key isolation. This skill owns the **items** — the part that does not currently exist.

## The problem being fixed

All 57 rubrics are a ~180-word evidence checklist. 53 say knowledge-check items "live in the session worksheet"; no such worksheet exists. `site/lib/assessment.ts` synthesizes the **same seven prompts for every module**, varying only hints pulled from `module.yaml`. Blueprint §10 promises mastery gates with four states and non-compensating evidence. Nothing implements that.

## When to use

- `deepen-module` step 6
- A rubric cites the "session worksheet"
- A review artifact scored "Assessment alignment" below 2

## Procedure

1. Read the module's teaching claims and coverage contract from `spec.md`, the eight rewritten lessons, and `content/assessment/keys/<id>.md`.
2. Write `content/modules/<phase>/<id>/assessment/items.md` — **6–10 items, no answers**, per the mix in `assessment-items.mdc`:
   2–3 discrimination · 2–3 diagnosis · 1–2 design · 1 transfer · 1 operate.
3. Every teaching claim carries at least one item. Every outcome in the coverage contract names an item ID.
4. Extend `content/assessment/keys/<id>.md` with, per item: the expected answer, **why each distractor is attractive**, and four-state banding with a concrete example answer at each band.
5. Rewrite `assessment/rubric.md` to describe module-specific evidence. Delete the "session worksheet" sentence.
6. Confirm no answer text leaked into `content/modules/**` (`L011`).

## What makes an item module-specific

> An item is module-specific when it cannot be answered correctly by a reader who has only seen a different module.

Fails the test: "State this topic's security rule in one sentence." That is the current generic prompt, and it works for all 57 modules, which is precisely the problem.

Passes: "Four teams propose a fix for the query-token leak: strip `access_token` in the gateway log pipeline; set `Referrer-Policy: no-referrer`; move the token to `localStorage`; refuse the query channel in `session_from_request`. Rank them by which attacker capability each removes, and name the one that changes what the server accepts."

## Distractor rationales

For each wrong option, write the misconception it encodes and where that belief comes from. This is the part that makes an item teach rather than test — and it is the material the examiner needs to band a partially-right answer fairly.

> **Distractor B — `Referrer-Policy: no-referrer`.** Attractive because it is a real control that genuinely addresses one of the four leak paths named in `01-property.md`, so a learner who read carefully will recognize it. It fails because it stops the URL travelling *outward* to third parties and does nothing about the service's own access logs, browser history, or a pasted screenshot. A learner choosing this has understood the `Referer` mechanism and missed that the rule is about the channel, not one consumer of it. Band: **developing**.

## Banding

Give a concrete example answer at each of `not-attempted`, `developing`, `competent`, `transfer-ready`. Abstract band descriptions ("shows partial understanding") cannot be applied consistently by a learner self-assessing, which is the only grader this course has.

Knowledge checks may use an 80% retryable threshold. Practical gates require satisfactory evidence for **every** critical invariant — a strong design answer never compensates for a missing forbidden-outcome test.

## Site

`site/lib/assessment.ts` should load `items.md` when present and fall back to the generic prompts only for modules not yet converted. Keys stay unlinked; CI greps `site/out` for `assessment/keys` paths.
