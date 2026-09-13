# First learning path implementation review

**Date:** 2026-09-13  
**Type:** implementation self-review; not an independent quality or lab-safety approval  
**Branch:** `implement-learning-plan`  
**Purpose:** record the exact content and site changes made while addressing the structure and pedagogy review.

## Reviewed change set

- `content/modules/0/0.1/` — reduced the orientation to four task-sized episodes; added an explicit course outcome, authorized scope, first action, and local red/green check.
- `content/modules/0/0.2/` — reduced the diagnostic bridge to five episodes; maps capability evidence to tooling bridge ids without waiving security evidence.
- `content/modules/1/1.1/lessons/01-property-vs-mechanism.md` — added the Alice/Bob prediction, worked invariant row, partial row, and explanatory feedback.
- `content/route.yaml` and `site/lib/route.ts` — content-owned required/optional route model.
- `site/app/roadmap/page.tsx`, `site/app/checkpoints/page.tsx`, `site/app/progress/page.tsx`, and lesson navigation — route and evidence continuity.
- `site/components/AssessmentWorkbook.tsx` and `site/components/LearnerDataPortability.tsx` — next-action guidance and versioned local export/import.
- `site/app/reference/[slug]/page.tsx` and `site/app/project/page.tsx` — direct reference readers and SecureCollab milestone history.
- `site/lib/plainCopy.ts` and `site/lib/markdown.tsx` call path — authored lesson prose is rendered without semantic regex rewriting.
- `labs/M0/securecollab-m0/` — loopback-only browser → HTTP → SQLite teaching bridge with vulnerable/fixed tenant-boundary behavior.

## Checks completed

- `python3 scripts/check_learning_contract.py` — all 57 module manifests, route IDs, and declared learning-object paths resolve.
- `npm --prefix site run lint` — passed.
- `site/node_modules/.bin/tsc --noEmit -p site/tsconfig.json` — passed.
- `npm --prefix site run build` — static export generated 666 pages.
- `git diff --check` — passed.
- M0 fixed smoke test — passed; loopback HTTP trace returned Alice 200 and Bob 403.
- M0 vulnerable smoke observation — forged client company returned 200 as the intended seeded failure.

## Review limits and follow-up

This record does not confer publishable depth. An independent reviewer still needs to follow the learner path, inspect the actual rendered wording, and verify the local labs. The M0 fixture is a teaching bridge and does not claim the locked FastAPI/PostgreSQL production stack. Pilot learners still need to validate timings, comprehension, and remediation links.

## Follow-up milestone bridges

After the first implementation pass, the local project thread now includes two additional synthetic bridges:

- M1 (`labs/M1/securecollab-m1/`) persists sessions and current account state in SQLite, checks the note's tenant on every read, and demonstrates both forged-company and revoked-session failures in the vulnerable pair.
- M2 (`labs/M2/securecollab-m2/`) persists queued jobs and exports, re-checks current authority before worker execution in the fixed pair, and demonstrates revocation-after-enqueue plus retained-copy denial.

These bridges make the M1/M2 state and time transitions runnable without introducing third-party dependencies. They remain teaching evidence rather than production FastAPI/PostgreSQL assurance and still require independent milestone review.
