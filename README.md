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
npm --prefix site install
npm --prefix site run build
```

Labs are not executed by the site. Examiner keys stay under `content/assessment/keys/` and are not linked from learner pages.
