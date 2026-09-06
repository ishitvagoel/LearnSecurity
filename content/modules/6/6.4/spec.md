# 6.4 — Files, paths, uploads, archives, XML, and deserialization

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 6.4
- **slug:** files-paths-uploads-archives-xml-and-deserialization
- **title:** Files, paths, uploads, archives, XML, and deserialization
- **phase / track / difficulty:** 6 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 6.1 interpreter shape; 2.1 parsers.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 6

## Objective hierarchy

1. Produce a **hostile-name corpus** plus prefix tests for SecureCollab upload paths.
2. Name attacker capabilities (filename field) and trust assumptions (canonical prefix under `/tmp/sc-lab`).
3. Transfer: clinic scan upload; XML/pickle/YAML named as other parsers.

## Prerequisite concepts

6.1 data vs grammar; 2.1 encodings; uploads are not executed (this module).

## Misconceptions

- UUID stored names replace path checks.
- Antivirus is the upload control.
- JSON is always a safe deserialize.

## Concept map

Interpreter shape (6.1) → path object identity (this module) → zip/XML/deserialize residuals → image codecs (E4).

## Invariant prompts

- What must remain true if the filename contains `../`?
- What fails if you strip `..` but never canonicalize?

## Threat-model prompts

- What can go wrong when path grammar mixes with data?
- What residual remains if the prefix is correct but a zip member or XML parser is not?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/6.4/6.4-lab`. Forbidden: resolved path leaves the lab root. Tests assert prefix/shape only. No real host-file reads.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-5.3.2`, `v5.0.0-5.3.1`, `v5.0.0-5.2.2`; `v5.0.0-5.3.3` **Level 3, labeled advanced**.
- CWE-22/434/502 as **awareness after** the cause.

## Review triggers

New upload processor, zip unpack, XML, or pickle/YAML load.

## Time budget and SecureCollab

Evidence: prefix test, isolated processing notes, named zip/XML residuals. Feeds Gate 6.

## Operational considerations

`path_escape_denied`. Malware scan is extra. Image codecs wait for E4.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: path-object mental models; ASVS v5.0.0-5.3.2; L3 5.3.3 labeled advanced |
