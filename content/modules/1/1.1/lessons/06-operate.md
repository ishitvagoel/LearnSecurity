# 1.1-LO-06 — Operate when prevention is not absolute

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST CSF 2.0 (final) Detect / Respond / Recover as *outcomes*.

## Property

If hashing, TLS, or an allowlist can fail, what must still be true?

## Task

For **one** invariant, write:

- **Log:** what event (no note bodies, no passwords).
- **Alert:** who is woken and on what threshold.
- **Revoke:** sessions, keys, or shares.
- **Recover:** restore, purge, user notice.

Compromise recording (Saltzer) is the property that **useful evidence exists under attack**, not “we installed a SIEM.”

## Practice

Attach this paragraph to the same catalogue row.

## Transfer

If the operator is the attacker, which of log/alert/revoke still holds? If none, say so as residual risk (1.4).
