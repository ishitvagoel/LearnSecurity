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

**After Pass A–E:** run **`/deepen-curriculum`** (or `/goal run /deepen-curriculum until revision.remaining is empty`). That revises map-complete modules to 1.1-quality publishable depth. Generation conductor **`/choreograph-curriculum`** has no queued A–E unit.

Until Phase 1 and Phase 2 specs exist, the conductor stays on **Pass A only** so the course is not mass-authored too early. Optional phrases:

- “this pass only” — do not advance into lessons
- “whole module” — Pass A through C for one module
- “pilot phase 1” — specs for 1.1–1.4 then stop
- “keep going, N modules” — repeat, capped at 4 per invocation

You can still run inner skills by hand (`next-iteration`, `author-module-spec`, `author-lesson`, `author-lab`, `author-assessment`, `standards-pin`, `quality-gate`, `spiral-revisit`) or **`/coverage-audit`**.

Agent standing instructions: [`AGENTS.md`](AGENTS.md). Rules live in [`.cursor/rules/`](.cursor/rules/). Skills in [`.cursor/skills/`](.cursor/skills/). Review subagents in [`.cursor/agents/`](.cursor/agents/).

## Reproducible QA contract

The repository QA commands are rooted from the checkout, not from the caller's current directory. Start with the disposable, pinned environment:

```bash
python scripts/qa.py bootstrap
python scripts/qa.py doctor
python scripts/qa.py validate
python scripts/qa.py lab-matrix
python scripts/qa.py site
```

`validate` checks module schemas and artifact paths, relative Markdown links, publication/review invariants, canonical standards-pin drift, learner/export boundaries, and path-scoped lab reset wording. `lab-matrix` runs each vulnerable and fixed pair and reports setup failures separately from expected vulnerable failures and fixed regressions. `site` installs the locked Node dependencies when needed, then runs lint plus clean standard and fallback production builds from the repository root.

For a pull request, `python scripts/qa.py changed --base-ref origin/main` runs the repository validator and the lab contracts affected by the change. The site’s ungraded local worksheets are labeled **Reflections**; they do not confer publication status or an automated grade.

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

### Build diagnostic

The standard build is explicitly Turbopack. It passed in this checkout on 2026-09-08 and is the deployment command. If an environment reports a Turbopack cache failure, remove only the generated `site/.next/` directory and run `npm --prefix site run build:webpack` as the documented fallback. The CI site job and `python scripts/qa.py site` verify both builds from a clean `.next/` directory.

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

GitHub is already connected to Vercel project **learn-security** (`.vercel/project.json`). Leave Root Directory empty. Pushes to this PR already create preview deployments; merging to `main` updates production.

A second CLI-created project named `learnsecurity` (alias `workspace-livid-rho.vercel.app`) is a duplicate and can be deleted in the Vercel dashboard so only **learn-security** remains.

`.vercelignore` omits `/labs` and `/content/assessment/keys` (root-anchored) so they are not uploaded. Preview Authentication should be off for this public curriculum, or PR preview URLs will bounce to the Vercel login.
