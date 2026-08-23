# LearnSecurity

Curriculum production repository for **Secure Application Engineering from First Principles** (web, API, and mobile).

The syllabus map is [`secure-application-engineering-curriculum-blueprint.md`](secure-application-engineering-curriculum-blueprint.md) (revision 1.1). The repo holds the Cursor harness, authored Pass A–C content, authorized local labs, and a Pass D static site under [`site/`](site/).

## Locked defaults

| Decision | Default |
|---|---|
| Web stack | FastAPI + PostgreSQL + TypeScript/Next.js |
| Mobile | Android/Kotlin first |
| Assurance | Tailored ASVS 5.0 Level 2 + selected Level 3; MASVS 2.1 profiles |
| AI security | Elective E1, not core |
| Site progress | Local-first until accounts are justified |
| Authoring order | Pass A for Phase 1, then Phase 2, before mass-authoring |

Record overrides in [`content/progress/STATUS.yaml`](content/progress/STATUS.yaml).

## How to run the next iteration

**Usual path:** in Cursor Agent run **`/choreograph-curriculum`**. That one skill picks the next legal module from `STATUS.yaml` and runs the others in order (pin standards → write spec → quality-gate; later, lessons → labs → assessment → spiral revisit → quality-gate).

Until Phase 1 and Phase 2 specs exist, the conductor stays on **Pass A only** so the course is not mass-authored too early. Optional phrases:

- “this pass only” — do not advance into lessons
- “whole module” — Pass A through C for one module
- “pilot phase 1” — specs for 1.1–1.4 then stop
- “keep going, N modules” — repeat, capped at 4 per invocation

You can still run inner skills by hand (`next-iteration`, `author-module-spec`, `author-lesson`, `author-lab`, `author-assessment`, `standards-pin`, `quality-gate`, `spiral-revisit`) or **`/coverage-audit`**.

Agent standing instructions: [`AGENTS.md`](AGENTS.md). Rules live in [`.cursor/rules/`](.cursor/rules/). Skills in [`.cursor/skills/`](.cursor/skills/). Review subagents in [`.cursor/agents/`](.cursor/agents/).

## Safety

Offensive exercises are limited to local course apps, official intentionally vulnerable labs, challenges whose terms authorize the work, or systems with written scope. Do not attack public or third-party targets. Do not commit real secrets or PII. Vulnerable code belongs under `labs/` with reset instructions—not in learner-facing lesson pages as copy-paste exploits.

## Layout

```text
secure-application-engineering-curriculum-blueprint.md
AGENTS.md
content/          metadata, specs, later lessons (see content/AGENTS.md)
labs/             future authorized labs only (see labs/AGENTS.md)
site/             Pass D only (see site/AGENTS.md)
```

## Site (Pass D)

```bash
npm --prefix site ci
npm --prefix site run build
```

Static HTML is written to `site/out/`. Labs are not executed by the site. Examiner keys stay under `content/assessment/keys/` and are not linked from learner pages.

### Vercel

Import this GitHub repository in Vercel. Use these project settings (also in `vercel.json`):

| Setting | Value |
|---|---|
| Root Directory | *empty* (repository root), **not** `site/` |
| Framework Preset | Other (`framework: null`) — static export |
| Install | `npm --prefix site ci` |
| Build | `npm --prefix site run build` |
| Output | `site/out` |
| Node | 20 (`.nvmrc`) |

No environment variables are required. Production branch: `main`. Preview deployments: every other branch.

This repository is linked to Vercel project **learnsecurity**. After this branch is merged, connect GitHub in the Vercel dashboard so pushes to `main` build automatically (Project → Settings → Git). The current production alias is `https://workspace-livid-rho.vercel.app` (rename/add a custom domain in Vercel when you want a stable hostname).

`.vercelignore` omits `labs/` and `content/assessment/keys/` so they are not uploaded. After connecting Git, Vercel builds on push; use a preview URL before promoting production.
