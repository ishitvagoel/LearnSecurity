# Site tree (Pass D)

Do not implement the Vercel learning website until Phase 1–2 Pass A/B pilots exist and the content schema is proven.

When Pass D starts, this tree should become a worked example of the curriculum (blueprint §14.3):

- Public content statically generated where practical
- Progress local-first unless accounts are genuinely required
- Executable vulnerable labs **must not** run inside the public content origin
- Lab infrastructure isolated, disposable, resource-bounded, explicitly authorized
- No real secrets, user PII, or production targets in exercises
- MDX and other rich content treated as code; build only from trusted, reviewed sources
- Identity, progress, assessment, and recovery journeys meet WCAG 2.2
- CSP, headers, telemetry, dependencies, and deployment provenance are in scope

Until then, keep this directory as policy only (this file).
