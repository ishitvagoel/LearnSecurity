---
name: plain-language-pass
description: Move vocabulary and sentence rewrites out of site/lib/plainCopy.ts into authored dual-form prose in content/, so the reviewed artifact is the shipped artifact. Use for workstream W1 or when a render-time rewrite collides with authored text.
---

# Plain language pass

## The problem being fixed

`site/lib/plainCopy.ts` is 1,333 lines and roughly 583 ordered regex replacements applied to authored prose at render time. It rewrites headings (`"Non-goals"` → `"What this page is not doing"`), vocabulary (`invariant` → `rule`, `TCB` → `what you trust`, `pytest` → `the check`, `Phase N` → `part N`), and whole sentences. It also carries repair regexes that patch damage caused by its own earlier substitutions — `"Build the the notes app "` → `"Build the notes app "`.

Three consequences:

1. **Reviewability.** `quality-gate` reviews `content/`. Learners read the transform. The reviewed artifact is not the shipped artifact.
2. **Fragility.** 583 ordered regexes over prose is a compounding bug source, and the file already repairs its own collisions.
3. **Pedagogy.** Suppressing `XSS`, `CSP`, `invariant`, and `attack surface` leaves readers unable to search, read a standard, or speak in a design review. The circumlocutions are frequently harder than the terms: "a content-security header in report-only mode" is worse than "CSP in `Report-Only` mode". The XSS module never says XSS.

Accessibility was the right instinct. The wrong part is the layer it was implemented in.

## Target

`site/lib/plainCopy.ts` under **150 lines**, retaining only structural normalization — mark stripping, heading casing, link-text extraction. **No vocabulary rewrites. No sentence rewrites. No heading remaps.**

## Procedure

Work one rule family at a time, never the whole file at once.

1. **Inventory.** List every replacement in `plainCopy.ts` and classify it: `structural` (keep), `vocabulary` (move to source), `sentence` (move to source), `repair` (delete — it exists only to patch another rule).
2. **Pick one vocabulary family**, e.g. `invariant`.
3. **Author the dual form in `content/`** at first use per lesson, then the real term thereafter:
   > a security invariant (a rule that must stay true)
   Later mentions in the same lesson use `invariant` alone. Do not dual-form every occurrence; that is the regex behaviour being removed.
4. **Delete that family's rules** from `plainCopy.ts`, including its repair rules.
5. **Build and diff the rendered output.** `npm --prefix site run build`, then compare the affected pages before and after. The rendered text should be equivalent or better — never a raw term the reader has not met.
6. **Run the linter** and commit that family alone.

## Terms to restore

Name the real thing, then define it once:

| Currently suppressed | Author as |
|---|---|
| "a content-security header" | `Content-Security-Policy (CSP)` → then `CSP` |
| "grammar mixed with data" (XSS module) | `cross-site scripting (XSS)` → then `XSS` |
| "rule" (for `invariant`) | `a security invariant (a rule that must stay true)` → then `invariant` |
| "what you trust" (for `TCB`) | `the trusted computing base (what you must trust for this claim)` → then keep the plain phrasing where `1.3` already argues it is clearer |
| "ways in" | `attack surface` |
| "the check" (for `pytest`) | `pytest` |
| "part N" / "check-in N" | `Phase N` / `Gate N` |

`1.3/lessons/01-property.md` already models the right pattern: it introduces "trusted computing base", then says the course will keep asking the plainer question instead. That is an authored editorial choice a reviewer can see — not a hidden regex.

## Glossary

`content/glossary/` is empty while `site/lib/glossary.ts` hardcodes 30 terms. Create `content/glossary/terms.yaml` as the single source (`term`, `short`, `long`, `firstTaughtIn`, `standardsRef`) and have `site/lib/glossary.ts` read it. Every term dual-formed in a lesson has a row.

## Do not

- Delete a rule without checking what renders in its place. Some rules mask genuinely broken authored text; that text needs fixing in `content/`, not re-masking.
- Reintroduce jargon without a definition. The goal is *define and use*, not *use and hope*.
- Convert the whole file in one commit. One family per commit keeps the rendered diff reviewable.
