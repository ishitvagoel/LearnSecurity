# LearnSecurity site (Pass D)

Static Next.js App Router export. Content is read from `../content` at build time.

```bash
npm install
npm run build
```

Output: `out/`. Do not deploy `labs/` or `content/assessment/keys/` as this origin.

Vercel project root must be the **repository root** so this app can read `../content` at build time. See the root README “Vercel” section.
