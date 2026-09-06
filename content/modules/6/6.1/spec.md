# 6.1 — Interpreter confusion and injection

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 6.1
- **slug:** interpreter-confusion-and-injection
- **title:** Interpreter confusion and injection
- **phase / track / difficulty:** 6 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 5.5 bound SQL; 2.1 encodings.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 6

## Objective hierarchy

1. Produce a **multi-interpreter data-flow** plus argv-shape tests for SecureCollab export listing.
2. Name attacker capabilities (user-chosen name as shell grammar) and trust assumptions (argv list; no live OS attack).
3. Transfer: clinic export filename; Jinja/SQL/mail headers as the same shape.

## Prerequisite concepts

5.5 data vs SQL grammar; 2.1 encodings beat denylists; 6.4 paths are a later cell.

## Misconceptions

- Injection is one CWE number.
- A denylist of `;` and `|` is complete mediation.
- `subprocess` wrappers automatically refuse a shell.

## Concept map

SQL parameters (5.5) → OS argv (this module) → HTML encoding (6.2) → other interpreters (templates, mail).

## Invariant prompts

- What must remain true if the export name is hostile to a shell?
- What fails if you strip `;` but still call `sh -c`?

## Threat-model prompts

- What can go wrong when data and shell grammar share one string?
- What residual remains if argv is correct but the binary parses leading `-` as flags?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/6.1/6.1-lab`. Forbidden: `sh -c` with a concatenated name; live command execution. Tests check argv **shape** only.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-1.2.5`, `v5.0.0-1.2.4` (same shape, already 5.5); `v5.0.0-1.2.10` **Level 3, labeled advanced**.
- OWASP Top 10:2025 A05 and CWE-77/78/89 as **awareness after** the cause.

## Review triggers

New export binary, plugin shell, or template engine; superseding **final** ASVS encoding chapter.

## Time budget and SecureCollab

Evidence: argv list, interpreter map, named argument-injection residual. Feeds Gate 6.

## Operational considerations

`child_process_anomaly`. Needed shell for a plugin — isolate that binary.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: data-vs-interpreter-grammar mental models; ASVS v5.0.0-1.2.5; L3 1.2.10 labeled advanced |
