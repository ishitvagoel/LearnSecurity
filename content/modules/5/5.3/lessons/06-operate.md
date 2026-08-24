# 5.3 — Key and secret lifecycle (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Secret scanning; auth failures on default strings. |
| Signal (no bodies) | auth_default_denied; image_rebuild after rotate. |
| Revoke / recover | Rotate again; rebuild images; purge logs. |
| Residual | PQC migration is a plan, not this test. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/5.3/5.3-lab`.

## Transfer

Envelope encryption DEK vs KEK; compromise runbook.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
