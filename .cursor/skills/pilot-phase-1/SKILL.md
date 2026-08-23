---
name: pilot-phase-1
description: Slash-only workflow to complete Pass A specifications for modules 1.1–1.4 then stop. Invoke with /pilot-phase-1. Do not auto-run during unrelated edits.
disable-model-invocation: true
---

# Pilot Phase 1 (Pass A)

Complete **Pass A only** for modules **1.1, 1.2, 1.3, 1.4** in order.

1. Invoke `standards-pin` once for Phase 1 anchors (Saltzer–Schroeder, NIST CSF 2.0, CISA Secure by Design, ASVS V8/V15, OWASP Threat Modeling, NIST SP 800-63-4 / WCAG 2.2 / SAMM as listed on those rows).
2. For each ID, follow `author-module-spec` (one module at a time). Do not write lesson prose or labs.
3. Run `quality-gate` on each spec.
4. Update STATUS: those modules `pass: A`; set `next` to Pass A for `2.1` (Phase 2 pilot) unless the user asked to include Phase 0.
5. **Stop.** Do not start Pass B or Phase 3+.

If 1.1–1.4 already have Pass A, report that and stop without regenerating unless the user requested a revision.
