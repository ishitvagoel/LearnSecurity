# Publishable depth (revision bar)

`depth: map-complete` means Pass A–C files exist and schema-validate, but lessons/labs may still be templated.

`depth: publishable` requires all of the following, judged against module **1.1** (not against the thin generator stubs):

1. Lessons start from a **this-system** property or question (SecureCollab or the elective system), not “for this module’s topic.”
2. Attacker capabilities and trust assumptions are specific (principal, object, channel).
3. Root cause / preconditions / impact / prevention / detection / recovery are distinguished.
4. Standards have version and status; drafts stay draft.
5. Mechanism limits and bypasses are named.
6. A safe practice task and a transfer task exist; keys are not in lesson files.
7. The lab’s forbidden outcome is **module-specific** and tests fail on `vulnerable/`, pass on `fixed/`, in an authorized local tree.
8. Framework defaults are not treated as application guarantees.
9. No universal checkbox security; residual risk is explicit.
10. No live-target or real PII.
11. Lab actually executed in this session (or a recorded clean pytest pair).
12. Human-in-the-loop controls (if any) mention usable/accessible journeys (WCAG 2.2).
13. `reviewer` and `lastReviewedAt` updated for this revision.

A slogan YAML claim that only checks the word “tenant” is **not** publishable for modules whose invariant is not “write a property-shaped claim.”
