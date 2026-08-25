# 1.1-LO-04 — Build the smallest mechanism that restores an invariant

**Kind:** design-exercise  
**Loop step:** 4 Build

## Start from a failed property

A trustworthy build step is not “add more security.” It is a causal argument:

1. a specific forbidden outcome is possible;
2. a root cause and preconditions explain why;
3. a mechanism changes the relevant state transition or trust relation;
4. evidence can distinguish the repaired system from the failed one;
5. residual risk remains explicit.

Choose one catalogue row from LO-02. Do not choose a mechanism first.

## Worked design: note bodies in logs

Assume the property is:

> Application observability events must not contain note-body or credential values during request handling or error reporting.

The attacker is an operator or compromised log reader who cannot directly query note rows. The API process and logging configuration are trusted to enforce a field policy. The time horizon includes retained logs and incident exports.

### Root cause and preconditions

The failure is possible when application code passes arbitrary objects or exception context to a general serializer. A note body is present in process memory, the logging call accepts it, and the log pipeline retains it. TLS and database encryption do not intervene because disclosure occurs before transport to the logging service.

### Candidate mechanisms

| Candidate | What it changes | Limit |
|---|---|---|
| “Install a SIEM” | Stores and queries events | Does not prevent sensitive fields from entering events |
| Redact known note text after serialization | Attempts content matching | Misses encodings, fragments, new fields, and transformed values |
| Structured event allowlist with typed safe fields | Makes sensitive fields unrepresentable in normal event construction | Bypass remains possible through raw logging or exception middleware |
| Encrypt the logging destination | Protects a storage channel | Authorized log readers may still see note bodies |
| Disable all logs | Removes one disclosure path | Destroys accountability and diagnosis; other telemetry may remain |

The smallest plausible structural mechanism is an allowlisted event constructor plus a ban on raw object logging in the trusted API path. It directly constrains which fields can cross the observability boundary. It still needs tests for exception paths and a residual-risk statement for memory dumps or bypass APIs.

### Derive proof obligations

A mechanism is not complete until you can state what must be true of it:

- every security-relevant logging path uses the safe constructor;
- note bodies and credentials have no allowed event field;
- framework and exception middleware cannot append request bodies;
- field-policy failures deny emission or replace the value safely;
- the application still emits enough identifiers for accountability;
- a captured event can be tested without storing the sensitive input.

These obligations become review and test targets. “The library supports redaction” is not one of them.

## Minimize trusted computing base

For your chosen row, draw a small table:

| Component | Must be trusted for this property? | Why or why not? |
|---|---|---|
| Browser/Next.js client | No | A hostile client can construct requests; the property cannot depend on client honesty |
| FastAPI route | Maybe | It gathers subject and object context |
| Central policy function | Yes, if it decides authorization | A wrong decision directly permits the forbidden outcome |
| PostgreSQL role/policy | Depends on design | It may provide independent enforcement or merely obey the API |
| Log pipeline | Only for evidence availability, not request authorization | Conflating the two enlarges trust |
| Scanner | No | It observes selected behavior and cannot enforce the invariant |

Remove unnecessary trusted components. For each remaining one, name the behavior you rely on. “Trust the database” is too broad; “the role cannot select rows outside the bound tenant” is reviewable.

## Framework defaults versus application guarantees

A framework may parse a request, hash a credential, set a cookie flag, escape a template, or emit an access log. Those are default mechanisms under conditions. Your guarantee includes:

- how the application configures the mechanism;
- alternate routes and failure paths;
- version and deployment assumptions;
- state outside the framework;
- tests that exercise the forbidden outcome.

When you rely on a default, record how it could be disabled or bypassed. A default with no invariant and no verification is inherited optimism.

## Build record

For one catalogue row, produce a one-page design record:

1. **Invariant and forbidden outcome**
2. **Root cause and preconditions**
3. **Smallest mechanism**
4. **State transition or trust relation changed**
5. **Why two plausible alternatives are insufficient**
6. **Proof obligations**
7. **Normal, negative, abuse, and failure evidence**
8. **Detection and recovery**
9. **Residual risk**
10. **Review trigger**

The record may propose a future implementation; this Phase 1 exercise does not require SecureCollab product code.

## Design review questions

A reviewer should challenge the record:

- Does the mechanism prevent the forbidden outcome or merely make it less likely?
- Can the same state change occur through another route, worker, retry, import, or restore?
- Does the repair trust the client or a label supplied by the attacker?
- Does the mechanism destroy an accountability, privacy, availability, safety, or usability property?
- What happens when the mechanism is unavailable, stale, or misconfigured?
- Which test would fail if the mechanism were removed?

Revise until the mechanism is both smaller and more directly connected to the property.

## Transfer

SecureCollab later adds webhook delivery. Revisit the log-confidentiality example: payloads, retry metadata, third-party endpoints, and background workers introduce new channels and trusted components. “Reuse the allowlist” is not enough. State which proof obligations survive and which must be rewritten.
