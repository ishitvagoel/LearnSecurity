# 4.1 — Identity lifecycle (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.

## Property (start here)

After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen session cookie after the user left the org; a delayed worker using the old user id.
- **Trust:** Local user+session maps. Real IdP SLO is extra (4.5).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Deleted user's leftover session still authenticates |
| Failure | Fail closed: Invalidate sessions (and tokens, workers) in the same use-case |

Lab tests: `test_property.py` under `labs/4.1/4.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Deleted user's leftover session still authenticates`
- `--impl fixed`: **pass**

after delete_user('alice') session_valid is False.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Contractor access end-date; support impersonation tickets.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
