# 5.2-LO-07 — Transfer: SSN column labeled encrypted that is Base64

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-11.3.3`; RFC 9106 (final) if a password row appears. RFC 9106 is for **passwords**, not the SSN field.

## Change the workplace; keep encoding-is-not-confidentiality

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `protect("secret")` must not round-trip as Base64. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic: SSN column labeled “encrypted” that is Base64. Also name password hashing vs field AEAD vs backup encryption.

**Product sketch:** EHR-lite with an `ssn_encrypted` column.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (DB admin; stolen disk — not a live clinic);
2. trust assumptions (which AEAD+key is TCB; the column name is not);
3. forbidden outcome (Base64 round-trip of the stand-in, not “HIPAA”);
4. a test idea on a **local** fixture only (decode of `protect(ssn)` is not the SSN);
5. residual (key in the same row; nonce reuse Level 3; TLS ≠ at rest);
6. WCAG only if a human “show SSN” path is in the claim (masked until explicit view — `v5.0.0-14.2.6` is Level 3 elsewhere).

## Mental model: the label is not the mechanism

```mermaid
flowchart LR
  Col["ssn_encrypted"] --> B64[Base64]
  B64 --> Reader[Admin reads SSN]
```

If the column name is `ssn_encrypted` and the bytes are Base64, the cell is gone. FastAPI, a Postgres `bytea` type, and a disk-encryption checkbox do not invert the observer. Argon2 on the SSN is the wrong property (password KDF, not field AEAD). HTTPS does not encrypt the column.

The clinic rewrite still has to keep the SecureCollab fork: Base64 decode of the stored stand-in is not the SSN. Renaming the column or wrapping `b64encode` in a function named `encrypt` leaves the observer unchanged. The local pytest analogue is `test_protect_is_not_mere_encoding` — on a fixture, not a live EHR.

## What graders reject

| Reject | Why |
|---|---|
| “Disk encryption is on” | Wrong observer |
| Live clinic DB | Lab policy |
| Argon2 on the SSN | Wrong property |
| HTTPS as at-rest encryption | Wrong hop |
| HTTP 200 as confidentiality evidence | Wrong observation |

## Practice

One page. No keys. `labs/5.2/5.2-lab` is the only running system you may break. Do not decode a live column.

## Non-goals

Live-target decoders. Real SSNs. Claiming Gate 5 from this page.
