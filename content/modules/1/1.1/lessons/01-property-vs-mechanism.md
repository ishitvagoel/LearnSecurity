# 1.1-LO-01 — Property vs mechanism

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** Saltzer & Schroeder (1975, seminal); NIST CSF 2.0 (final) as *outcome* labels, not a control menu.

## Property (start here)

What must remain true of **this system** if someone misuses it, a component fails, or an attacker with stated capabilities acts?

That sentence is a **security invariant**. “We use TLS / JWT / bcrypt / a scanner” is a **mechanism**. Mechanisms can fail the property.

## Attacker capabilities and trust assumptions

State both, or the property is a slogan:

- **Attacker:** e.g. anyone who can send HTTP to the public API; a logged-in member of another tenant; a stolen backup.
- **Trust:** e.g. the FastAPI process and PostgreSQL with least-privilege roles are in the TCB; the Next.js bundle is **not**.

Open design (Saltzer): assume the mechanism can become known. Secrecy of the mechanism is not the property.

## Eight names, made system-specific

Do not paste a CIA triad. For SecureCollab (collaboration notes, tenants, files later), draft lines like:

| Name | Invariant shape (example, not a complete catalogue) |
|---|---|
| Confidentiality | Tenant A’s note bodies are not readable by Tenant B’s members via the API, backups they can obtain, or logs they can read. |
| Integrity | A note’s content changes only through authorized actions; silent corruption is detectable. |
| Availability | Sharing a note does not make the tenant’s other notes unreadable; abuse has a bounded blast radius. |
| Authenticity | Actions attributed to user U were performed with U’s authenticator, not by guessing a URL. |
| Authorization | Being logged in is not permission to read another tenant’s objects (see 1.2). |
| Accountability | High-impact actions leave evidence that a later investigator can use (compromise recording). |
| Privacy | Retention and logs do not keep more personal data than the stated purpose; privacy ≠ confidentiality. |
| Safety | A “delete account” path does not strand a coerced user with no recovery that they can actually complete (1.4). |

If you omit one, write **non-goal** and why.

## Root cause vs impact vs prevention vs detection vs recovery

A hashed password (mechanism) can fail confidentiality of a note (property) if the app logs note bodies. Root cause: wrong trust in the log pipeline. Impact: tenant data in the observability store. Prevention: do not log bodies. Detection: DLP/alerts on log fields. Recovery: rotate, purge, notify.

CSF 2.0 **Protect / Detect / Respond / Recover** name *outcomes*. They do not prove ASVS.

## Framework defaults vs application guarantees

`passlib` hashing is not “passwords cannot be recovered from a stolen DB” unless you also control backups, memory dumps, and logging. Next.js “secure defaults” are not tenant isolation.

## Practice

Pick one row above and rewrite it until a second person could write a test that would fail if the invariant were false.

## Transfer (preview of LO-07)

If SecureCollab adds an offline mobile cache, which rows must change? (Do not answer with “add encryption.” Name the property.)
