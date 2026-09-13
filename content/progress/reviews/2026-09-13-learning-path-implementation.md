# First learning path implementation review

**Date:** 2026-09-13  
**Type:** implementation self-review; not an independent quality or lab-safety approval  
**Branch:** `implement-learning-plan`  
**Purpose:** record the exact content and site changes made while addressing the structure and pedagogy review.

## Reviewed change set

**Implementation commit:** `6502bffe17f5ea10d32f3369dc88db7f647be51b`

- `content/modules/0/0.1/` — reduced the orientation to four task-sized episodes; added an explicit course outcome, authorized scope, first action, and local red/green check.
- `content/modules/0/0.2/` — reduced the diagnostic bridge to five episodes; maps capability evidence to tooling bridge ids without waiving security evidence.
- `content/modules/1/1.1/lessons/01-property-vs-mechanism.md` — added the Alice/Bob prediction, worked invariant row, partial row, and explanatory feedback.
- `content/route.yaml` and `site/lib/route.ts` — content-owned required/optional route model.
- `site/app/roadmap/page.tsx`, `site/app/checkpoints/page.tsx`, `site/app/progress/page.tsx`, and lesson navigation — route and evidence continuity.
- `site/components/AssessmentWorkbook.tsx` and `site/components/LearnerDataPortability.tsx` — next-action guidance and versioned local export/import.
- `site/app/reference/[slug]/page.tsx` and `site/app/project/page.tsx` — direct reference readers and SecureCollab milestone history.
- `site/lib/plainCopy.ts` and `site/lib/markdown.tsx` call path — authored lesson prose is rendered without semantic regex rewriting.
- `site/components/HomeContinue.tsx`, `site/components/LastActivityMarker.tsx`, `site/components/LessonKeyNav.tsx`, and `site/components/MermaidDiagram.tsx` — last-activity continuation, topic-boundary keyboard navigation, and heading-linked diagram labels.
- `labs/M0/securecollab-m0/` — loopback-only browser → HTTP → SQLite teaching bridge with vulnerable/fixed tenant-boundary behavior.
- `content/bridges.yaml`, `site/lib/bridges.ts`, and `/bridges/` — five concrete Python, browser, SQL, network, and Git bridge destinations with task, success, and retry criteria.
- `site/components/LastActivityMarker.tsx`, practice/assessment pages, and learner-state components — continuation across bridge, practice, and worksheet pages; replacement preview, bounded backup, rollback, and truthful memory-only storage messaging.
- `.github/workflows/verify.yml`, `labs/requirements-dev.txt`, and `scripts/check_learning_contract.py` — reproducible dependency installation, contract checks, fixed smoke gates, and vulnerable assertion gates.
- `labs/M1/securecollab-m1/` — synthetic PBKDF2 credential verification, additive local migration, and missing/wrong-password assertions.
- `labs/M2/securecollab-m2/` — generated per-worker credential, forged-worker rejection, current-authority checks, and duplicate-delivery oracle.

## Checks completed

- `python3 scripts/check_learning_contract.py` — all 57 module manifests, route IDs, and declared learning-object paths resolve.
- `npm --prefix site run lint` — passed.
- `site/node_modules/.bin/tsc --noEmit -p site/tsconfig.json` — passed.
- `npm --prefix site run build` — static export generated 672 pages, including the five bridge destinations.
- `git diff --check` — passed.
- M0 fixed smoke test — passed; loopback HTTP trace returned Alice 200 and Bob 403.
- M0 vulnerable smoke observation — forged client company returned 200 as the intended seeded failure.
- M1 fixed smoke test — passed; credential verification, current session, cross-company, forged-company, and revocation cases are observable.
- M2 fixed smoke test — passed; worker credential, queue execution, duplicate delivery, revocation-after-enqueue, retained-copy, and forged-tenant cases are observable.
- All 60 lab test suites collect successfully and pass in their fixed form (59 `--impl fixed` suites plus the 1.1 claim validator); M0, M1, and M2 vulnerable forms collect successfully and fail their intended security assertions.
- The M1 additive migration check passed against a pre-credential SQLite schema.

## Review limits and follow-up

This record does not confer publishable depth. An independent reviewer still needs to follow the learner path, inspect the actual rendered wording, and verify the local labs. The M0–M2 fixtures are teaching bridges and do not claim the locked FastAPI/PostgreSQL production stack. Pilot learners still need to validate timings, comprehension, and remediation links. The integrated M0–M4 application, full M2 evidence pack, mobile extension, capstone defense, and independent review remain project work rather than being relabeled complete by these bridge results.

## Follow-up milestone bridges

After the first implementation pass, the local project thread now includes two additional synthetic bridges:

- M1 (`labs/M1/securecollab-m1/`) persists sessions and current account state in SQLite, checks the note's tenant on every read, and demonstrates both forged-company and revoked-session failures in the vulnerable pair.
- M2 (`labs/M2/securecollab-m2/`) persists queued jobs and exports, requires a generated worker credential, re-checks current authority before worker execution in the fixed pair, and demonstrates revocation-after-enqueue, retained-copy denial, and duplicate-delivery behavior.

These bridges make the M1/M2 state and time transitions runnable without introducing third-party dependencies. They remain teaching evidence rather than production FastAPI/PostgreSQL assurance and still require independent milestone review.
