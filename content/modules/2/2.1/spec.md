# 2.1 — Bytes, text, formats, parsers, and interpreters

Pass A specification only.

## Identity

- **id:** 2.1
- **slug:** bytes-text-formats-parsers-interpreters
- **title:** Bytes, text, formats, parsers, and interpreters
- **phase / track / difficulty:** 2 / core / foundation
- **estimatedMinutes:** 270
- **prerequisites:** Phase 1 Pass A (1.1–1.4). Gate 1 not required as learner evidence yet.
- **routeTags:** complete, accelerated, web-api, mobile
- **releaseMilestone:** M0 (parser/encoding assumptions on the request path)
- **masteryGate:** 2

## Objective hierarchy

1. Produce a **parser-boundary map** for SecureCollab’s browser → API → DB path: bytes vs characters, Unicode/normalization, encodings, grammars, serialization, interpreter boundaries.
2. Show a **parser differential** or ambiguous decode on a **local fixture** as a property failure (two components disagree), not as a public exploit kit.
3. Transfer: a new format (CSV, JSON, multipart) and list which 1.3 surfaces and 6.x injection families become in-scope.

## Prerequisite concepts

1.1 invariants; 1.3 trust boundaries (where parsers sit).

## Misconceptions

- Strings are characters; UTF-8 is “just text.”
- Validation, sanitization, encoding, and parameterization are interchangeable.
- If JSON.parse succeeds, the meaning is unambiguous across languages.
- Framework “auto-escaping” is complete mediation of interpreters.

## Concept map

```text
Bytes -> decode/normalize/canonicalize -> grammar -> interpreter
  -> two parsers => possible differential => invariant fail
```

## Invariant prompts

- Which interpreter consumes this field, and in which encoding?
- If two parsers disagree, which one is in the TCB?
- Is this check validation, canonicalization, or encoding—and in which context?

## Threat-model prompts

- Where can an attacker choose encoding, BOM, or nested format?
- Which shared parser (JSON, HTML, URL) is a least-common-mechanism risk?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 2.1-LO-01 | concept-model | Bytes vs characters, Unicode, canonicalization, interpreter boundaries | 1 Property |
| 2.1-LO-02 | design-exercise | Parser-boundary map for SecureCollab request path | 2 Model |
| 2.1-LO-03 | mechanism-lab | Local fixture: two parsers disagree on the same byte string | 3 Break |
| 2.1-LO-04 | design-exercise | Pick a structural API (parameterized/typed) that removes the ambiguity | 4 Build |
| 2.1-LO-05 | verification-lab | Ambiguity test suite (forbidden outcomes) | 5 Verify |
| 2.1-LO-06 | operations-exercise | Log parse failures without echoing raw hostile bytes to users | 6 Operate |
| 2.1-LO-07 | transfer-challenge | Add multipart/CSV: new interpreters and invalidated map cells | 7 Generalize |
| 2.1-LO-08 | code-review | Seeded decode-then-concat-then-decode again | 5 Verify |

## Lab briefs

**Lab `2.1-parser-boundaries`:** local fixture only. Invariant: each interpreter boundary is named; differentials are tests. Forbidden: live-target encoding attacks; weaponized payloads in lesson Markdown.

## Assessment blueprint

| Category | Artifact |
|---|---|
| Explain | Bytes vs characters; validation vs encoding |
| Design | Parser-boundary map |
| Build | Deferred; typed/parameterized path |
| Break | Local differential annotation |
| Verify | Ambiguity tests |
| Operate | Safe parse-failure logging |
| Communicate | Why a blacklist of characters is insufficient |

Mastery states as in 1.x. Transfer = LO-07. Gate 2 with 2.2–2.4.

## Standards references

ASVS 5.0.0 V1/V2/V15 (chapter-level, `final`). CWE families as **awareness** only. Pins in `content/standards/pins.yaml`.

## Review triggers

New serializer, template engine, or query builder; Unicode normalization change.

## Time budget and SecureCollab

~270 min. Feeds M0 path and later 6.1–6.2.

## Operational considerations

Parse errors must not leak internals; do not log full hostile bodies.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
