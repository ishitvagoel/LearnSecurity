# 0.1-LO-05 — Authorized lab scope (Verify)

**Kind:** loop-object  
**Loop step:** 5 Verify  
**Standards:** CISA Secure by Design (final public guidance); Saltzer (1975, seminal) where authority appears.

## Property (start here)

Course activity is authorized only for named local lab hosts. A public URL is out of scope even if the learner is curious. This is a 1.2-style **subject–object–action** over the tester’s own actions.

## Attacker capabilities and trust assumptions

**Actor:** the learner. **Object:** remote systems. **Trust:** none for example.com. Local `127.0.0.1` is in the TCB of the course, not of production.

## Root cause / impact / prevention / detection / recovery

Root cause: treating curiosity as authorization. Impact: illegal/unethical testing. Prevention: allowlist of lab hosts. Detection: refuse and log. Recovery: stop, report if a tool was pointed wrongly.

## Framework defaults vs application guarantees

A proxy or browser ‘works’ on the internet. That is not course authorization.

## Practice

What test is the forbidden outcome?

## Transfer

Same.

## Non-goals

Live targets, real PII, weaponized payloads. Mastery gates stay not-attempted.
