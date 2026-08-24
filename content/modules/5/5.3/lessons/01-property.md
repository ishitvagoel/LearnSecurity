# 5.3 — Key and secret lifecycle (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
**Mechanism (not the property):** pydantic Settings reading .env does not rotate anything.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 5.3 |
|---|---|
| Root cause | Default credential never invalidated. |
| Preconditions | auth(hardcoded) True while current is rotated-now. |
| Impact (1.1 cell) | Authenticity of the service credential over time. — Silent backdoor equal to production admin if copied. |
| Prevention | Generate unique secrets; rotate; refuse known defaults; never commit. |
| Detection | Secret scanning; auth failures on default strings. |
| Recovery | Rotate again; rebuild images; purge logs. |

## Framework defaults vs application guarantees

pydantic Settings reading .env does not rotate anything.

## Mechanism limits and bypasses

Vault without rotation policy is a new hard-to-scan dump.

Secondary default in a worker (7.4); mobile embedded key (8.4).

## Residual risk

PQC migration is a plan, not this test.

## Practice

Inventory: name, location, owner, last rotated, blast radius.

Run `labs/5.3/5.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Envelope encryption DEK vs KEK; compromise runbook.

Clinic lab API key in a GitHub gist.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
