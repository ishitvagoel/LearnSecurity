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

Vercel: install/build commands in `vercel.json` use `npm --prefix site`.
