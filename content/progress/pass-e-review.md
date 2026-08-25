# Pass E — independent curriculum and security review

> **Historical record.** This review predates the 2026-08-24 bulk lesson rewrite and cannot approve those later files. For current publishability decisions, use [the 2026-08-25 depth audit](depth-audit-2026-08-25.md), the semantic quality rubric, and a dated per-module review artifact.

Date: 2026-08-23  
Reviewers: `quality-reviewer`, `lab-safety-reviewer`, `standards-auditor`, `curriculum-architect` (readonly; this record).

## Sequencing

Phase 1–2 Pass A/B pilots existed before Pass D. All 57 units remain Pass A–C complete with schema-valid `module.yaml`. Hard phase order in the site roadmap matches blueprint §7. Electives are labeled as opening after Phase 7. Mastery gates and M0–M5 are **not** marked competent.

## Coverage

See [`coverage-audit.md`](coverage-audit.md). No ASVS 4.x IDs. No MASVS L1/L2/R. Drafts remain labeled draft.

## Runnable artifacts

All 57 local YAML labs: `vulnerable/` fails pytest `--claim`; `fixed/` passes (verified 2026-08-23). Site static export does not execute labs. `site/out` contains no `assessment/keys` paths.

## Website / lab threat model (Pass D)

| Asset | Threat | Mitigation |
|---|---|---|
| Public origin | Hosting vulnerable apps | Static export only; lab pytest stays in git `labs/` |
| Keys | Examiner notes leaked | Keys never imported by `site/`; grep of export empty |
| Progress | Account/PII premature | localStorage only |
| XSS via MDX | Untrusted MDX | Trusted Markdown subset parser, no MDX |
| Clickjacking / MIME | | `X-Frame-Options`, `nosniff`, CSP in `vercel.json` |
| Live targets | Course misuse | Policy page + lab briefs |

## Instructional quality (improvement, not blocker)

Generated lessons for Phase 0 / 3–11 / electives are thinner than hand-authored 1.1. Publishable for map coverage; deepen in later revisions. Do not treat `quality: competent` as transfer-ready learner mastery.

## Release

First versioned generation release: Pass A–E artifacts in-repo. Vercel production deploy is optional and out of band.
