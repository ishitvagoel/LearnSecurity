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

## Teaching claims

Five falsifiable claims, ordered by dependency. The module previously taught all five implicitly across the lessons without naming them; naming them here makes the coverage contract checkable.

1. **C1 — One byte sequence must yield one meaning used by every consumer.** For a SecureCollab note ingest, the same request bytes must produce a single company identifier used both for the who-is-allowed check and for the stored row. If two readers of those same bytes would assign different company identifiers, that disagreement is itself a secrecy failure — company B's body can end up stored under company A's access policy — independent of whether authentication was correct. The failure is disagreement, not a missing login.
2. **C2 — Bytes become values through a chain of readers, and each link in the chain is a place ambiguity enters.** Bytes → characters (an encoding choice) → tokens (a grammar choice) → values (a duplicate-key or normalization policy) is not one step but four, and changing any one reader changes the value without changing the bytes. No framework default resolves this chain for you; the question "which reader's result do we trust" has to be answered explicitly, once, and the answer has to be the same object for every consumer.
3. **C3 — Validation, canonicalization, sanitization, and encoding are four different operations that are routinely confused.** Validation asks whether a value matches an expected shape; canonicalization asks whether one representation was chosen before any decision was made; sanitization rewrites content for a different sink; encoding escapes a value for the next reader. Canonicalization — choosing one representation once, before anything else runs — is specifically the missing operation in a parser differential, and none of the other three substitutes for it.
4. **C4 — The structural fix is refuse-on-disagreement or single-reader-only, never guess-the-canonical-answer.** Given two readers that might disagree, a system can refuse the input when they disagree, or restructure so only one reader ever produces a value anyone consumes. Picking "the key Python happens to keep" or "the first match a regex happens to find" is not a third fail-safe option — both are guesses, and a guess that happens to be consistent today is not a guarantee it stays consistent after a library upgrade.
5. **C5 — A new reader on the same bytes reopens the invariant, even when the original ingest path was fixed correctly.** A worker that re-parses stored text tomorrow, a database's own JSON handling, or a second grammar (GraphQL variables alongside a REST body) for the same logical field are each a new reader of bytes that were already believed to have one meaning. Fixing the ingest path does not imply the invariant holds at every later point those bytes are read again.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 5 Verify | `test_duplicate_tenant_keys_are_one_meaning`, `test_middle_duplicate_is_not_silently_dropped`, `test_non_string_duplicate_is_not_invisible_to_the_checker` (the module's forbidden outcome and its boundary cases) | items.md #1, #2, #3, #8 |
| C2 | 1 Property, 2 Model | Not directly code-testable — this claim is about the reader chain in general, not one object's shape. Modeled in `lessons/02-model.md`'s reader table. | items.md #2, #5 |
| C3 | 1 Property, 4 Build | Not directly code-testable — a vocabulary distinction, not a predicate. Modeled in `lessons/01-property.md`'s four-word table and `lessons/04-build.md`. | items.md #5 |
| C4 | 4 Build, 5 Verify | `test_unambiguous_json_is_accepted`, plus the anti-fake pair and the malformed/non-string boundary tests added in this pass (see `upgrade-lab`) | items.md #3, #4, #6 |
| C5 | 6 Operate, 7 Transfer | Not code-testable — no queue or worker exists in this fixture. Modeled in `lessons/06-operate.md` and the transfer scenario. | items.md #7, #8, #9 |

C1 and C4 carry genuine lab assertions, satisfying the ≥2-claims bar. C2, C3, and C5 are honestly declared non-code-testable rather than mapped to a fabricated test — C2 and C3 are vocabulary and modeling claims a unit test cannot assert, and C5 requires a second reader (a worker, a second grammar) this Tier-1 fixture does not have.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Produce a parser-boundary map for the SecureCollab request path | C2 | `lessons/02-model.md` §Step 1 reader table | `lessons/01-property.md` two-reader diagram | `lessons/02-model.md` map exercise | items.md #2 | `lessons/07-transfer.md` clinic REST/GraphQL |
| Explain bytes vs characters, Unicode, canonicalization, encodings, grammars, serialization, interpreter boundaries | C2, C3 | `lessons/01-property.md` §Bytes are not characters | `lessons/01-property.md` four-word table | `lessons/01-property.md` practice | items.md #5 | `lessons/07-transfer.md` |
| Demonstrate a local parser differential as a property failure | C1 | `lessons/01-property.md` §One byte sequence | `lessons/03-break.md` broken `parse_note.py` fixture | `labs/2.1/2.1-parser-boundaries` vulnerable/fixed pair | items.md #1, #3 | `lessons/07-transfer.md` |
| Separate validation, canonicalization, sanitization, and encoding by context | C3, C4 | `lessons/01-property.md` §Four words that are not the same | `lessons/04-build.md` | `lessons/08-review.md` review exercise | items.md #4, #6 | `lessons/07-transfer.md` |
| Transfer the map when a new format is added | C1–C5 | `lessons/07-transfer.md` | `lessons/07-transfer.md` clinic table | `lessons/07-transfer.md` write-up prompts | items.md #7, #8, #9 | (is the transfer task) |

## Known residuals

- PostgreSQL `jsonb` agreement with CPython's reader → named as a residual in `lessons/05-verify.md`; no module currently tests it.
- Unicode identifier lookalike/normalization attacks on display names → named in `lessons/01-property.md` and `06-operate.md` as out of scope for this specific fixture.
- Duplicate keys inside a GraphQL `variables` JSON payload → the transfer task's subject; not lab-tested here. GraphQL's variable coercion happens once per operation, so a declared variable cannot disagree with itself — the residual is in the `variables` payload's own JSON grammar, underneath the type system, not in GraphQL's alias mechanism.
- A worker re-parsing stored bytes tomorrow → named explicitly in C5; picked up when a queue/worker module exists.

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
