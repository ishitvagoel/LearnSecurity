# Site tree (Pass D)

Phase 1–2 Pass A/B pilots exist and `module.yaml` is schema-proven. This directory is the static Next.js learning site (blueprint §14).

Constraints in force:

- Public content is statically generated (`output: "export"`)
- Progress is local-first (`localStorage`); no accounts
- Executable vulnerable labs **must not** run inside this origin — lab pages are briefs only; pytest runs in `labs/` in the git checkout
- No answer keys linked or copied into `site/`
- Markdown is parsed as trusted curriculum text, not MDX from untrusted authors
- Security headers live in repo-root `vercel.json`
- WCAG 2.2: skip link, visible focus, text (not color-only) links, keyboard-accessible progress checkbox

Build from the repository root so `site/` can read `../content`:

```bash
npm --prefix site install
npm --prefix site run build
```

Vercel: keep the **git repository root** as the project root (see repo `vercel.json`).
Do not set Root Directory to `site/`, or the build cannot read `../content`.
`framework` is `null` so the static `site/out` export is served (not a serverless Next server).
`.vercelignore` excludes `/labs` and `/content/assessment/keys`.
Git deploys use Vercel project **learn-security**; do not also set Root Directory to `site/`.
