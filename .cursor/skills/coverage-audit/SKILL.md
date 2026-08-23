---
name: coverage-audit
description: Slash-only coverage audit of authored modules against ASVS 5.0 chapters, MASVS groups, and awareness lists. Invoke with /coverage-audit. Do not auto-run during ordinary authoring.
disable-model-invocation: true
---

# Coverage audit

1. Read blueprint §12 and all existing `module.yaml` `standardsRefs`.
2. Delegate **`standards-auditor`** (readonly) with the file list.
3. Produce a report (do not mass-edit lessons in this invocation):
   - ASVS 5.0 V1–V16 (and V17 only if E2/WebRTC is in scope) vs principal modules
   - MASVS 2.1 groups vs Phase 8 and shared modules
   - Top 10:2025, API Top 10:2023, Mobile Top 10:2024, CWE Top 25:2025 as **regression gaps**, not a new outline
4. Flag obsolete MASVS L1/L2/R language and mixed ASVS 4.x IDs as defects.
5. Write the report to `content/progress/coverage-audit.md` and leave STATUS `next` unchanged unless the user asked to queue gap-fill specs.
