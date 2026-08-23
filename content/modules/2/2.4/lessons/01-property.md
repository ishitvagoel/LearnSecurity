# 2.4-LO-01 — Time is part of the invariant

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 (final) session/time-related chapters at chapter level. OWASP Top 10:2025 A10 exceptional conditions — **awareness regression**, not the syllabus.

## Property (start here)

A **retried** SecureCollab share with the same idempotency key must not create a **second** share. Timeouts are security, not only UX. Happy-path tests do not prove this.

## Attacker capabilities and trust assumptions

- **Attacker:** a client that retries; two tabs; a future worker (7.4) replaying a job.
- **Trust:** clocks are local-lab; no NTP attack in this fixture. Fail-open “return 200 anyway” is a 1.2 mediation miss over time.

## Practice

Write the invariant with subject, object, action, **and** “at most once.”

## Transfer

Invite tokens: freshness and replay (4.3).
