# E4 — Memory safety and native-code boundaries

Pass A specification. Lesson prose lives in `lessons/`. A copy into a 4-byte lab buffer must not return more than 4 bytes. This is not a weaponized native exploit. Do not mark Gate 7 complete.

## Identity

- **id:** E4
- **slug:** memory-safety-and-native-code-boundaries
- **title:** Memory safety and native-code boundaries
- **phase / track / difficulty:** 7 / elective / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Opens after Phase 7; 1.2 mediation; 6.4 file/FFI; 6.1 interpreters.
- **routeTags:** complete, elective
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **bounds predicate** so `copy_into(4, b"abcdefgh", 4)` returns at most 4 bytes.
2. Name attacker capabilities (hostile declared length; FFI caller) and trust assumptions (local Python stand-in; C will not do this for you).
3. Transfer: clinic DICOM parser; image codec FFI — without shipping a native overflow PoC.

## Prerequisite concepts

1.2 complete mediation of the object; 6.4 parsers; CISA memory-safe roadmaps as manufacturer guidance.

## Misconceptions

- Python slice is what C does.
- A memory-safe language removes FFI risk.
- CWE Top 25 is the syllabus.
- ASAN in a lesson is a weaponized exploit.

## Concept map

Trust declared_len (break) → min(dst, declared, src) (this module) → prefer memory-safe languages for new code → FFI still a boundary. Residual: integer wrap; existing C codecs (6.4).

## Invariant prompts

- What must remain true for `copy_into(4, src, 4)`?
- What fails if n is trusted over dst?

## Threat-model prompts

- What can a hostile size field do at an FFI boundary?
- What residual remains if new code is memory-safe but old codecs are not?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/E4/e4-lab`. Forbidden: copy into a 4-byte buffer returns more than 4 bytes. No native exploits.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- CISA *The Case for Memory Safe Roadmaps* (2023-12-06): manufacturer guidance, not the lab oracle. CISA/NSA 2025 memory-safe languages guide as additional guidance.
- CWE Top 25 (awareness): CWE-119/787 after the length cause, not the syllabus.
- OWASP ASVS 5.0.0 (final): `v5.0.0-5.3.1` uploaded/native components must not become executable server code (related). `v5.0.0-5.3.3` zip/user paths inside archives is **Level 3, labeled advanced** (native unpacker residual). Do not invent ASVS memory-safety IDs.

## Review triggers

Copy exceeds destination; native PoC in learner pages; FFI unmarked; CWE used as syllabus.

## Time budget and SecureCollab

Elective. Python length stand-in only.

## Operational considerations

`copy_length_denied`. Patch; do not ship an overflowed binary.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: length is mediation; no native exploits |
