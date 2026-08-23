---
name: standards-pin
description: Before writing or revising a module, check canonical standard URLs, record version/status/dates, and flag drafts. Use when pinning ASVS, MASVS, NIST, RFCs, or when standards might be stale.
---

# Standards pin

## When to use

- Before Pass A or any material module revision
- User asks to refresh OWASP/NIST/RFC/MASVS versions
- Quality review found unlabeled drafts or mixed standard generations

## Instructions

1. Read blueprint §12–§17 for the module’s anchors. Canonical URLs are listed in §17.
2. Check the live canonical source when network access exists. If it cannot be fetched, record `status: unverified` and do not present a guessed newer version as fact.
3. Upsert rows in [`content/standards/pins.yaml`](../../../content/standards/pins.yaml) (create the file if missing) with:

   `id`, `source`, `version`, `status` (`final` | `draft` | `candidate` | `bcp` | `awareness` | `unverified`), `publishedAt`, `reviewedAt` (ISO date), `url`, `role`, `notes`

4. **Always label** as non-final until the blueprint snapshot is updated: OAuth 2.1 (Internet-Draft), NIST SP 800-218 Rev. 1 / SSDF 1.2 (IPD), NIST Privacy Framework 1.1 (IPD), WebAuthn Level 3 (Candidate Recommendation as of the 23 Aug 2026 snapshot).
5. Never present OWASP Top 10, API Top 10, Mobile Top 10, or CWE Top 25 as compliance or as the learning order.
6. ASVS identifiers use `v<version>-<chapter>.<section>.<requirement>` when pinning requirement-level refs. Do not mix ASVS 4.x IDs. MASVS 2.x uses testing profiles and MASVS → MASWE → MASTG, not L1/L2/R.
7. If a superseding **final** version exists, add a `migrationNote` and do not silently rewrite old lessons.

See `references/snapshot-2026-08-23.md` for the curriculum’s research snapshot.
