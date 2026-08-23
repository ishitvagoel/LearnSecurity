# 1.1-LO-03 — A local “hashed passwords” claim

**Kind:** mechanism-lab (teaching)  
**Loop step:** 3 Break  
**Lab:** [`labs/1.1/1.1-invariant-catalogue/`](../../../../../labs/1.1/1.1-invariant-catalogue/README.md) — **authorized local fixture only**.

## Property

Does “passwords are hashed” imply any SecureCollab invariant you wrote in LO-02?

## What to observe (local only)

The `vulnerable/` tree claims security *because of a mechanism name*. Your job is to name:

- **Root cause:** property and mechanism were collapsed.
- **Preconditions:** a reviewer (or a future attacker) is asked to trust the label.
- **Impact:** false assurance; real note confidentiality is unstated and untested.
- **Forbidden outcome:** treating the claim as an invariant.

Do **not** attack other systems. Do **not** paste cracking wordlists or exploit payloads. The fixture is a YAML claim file plus tests.

## Practice

Run the tests on `vulnerable/` (they should fail the invariant-shape check) and read the README.

## Transfer

Name one other mechanism slogan (“we use JWT”, “TLS everywhere”) and the property it fails to state.
