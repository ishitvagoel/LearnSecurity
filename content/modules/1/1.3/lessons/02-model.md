# 1.3-LO-02 — Annotated SecureCollab trust-boundary diagram

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** Shostack Four Questions via OWASP Threat Modeling (maintained, final).

## Property (start here)

Can a reviewer **challenge** your boxes: what is in the TCB, and where does 1.2 mediation run?

## Attacker capabilities and trust assumptions

Hostile browser; honest local lab operator. No live cloud accounts.

## Draw

Boxes: Next.js (untrusted), FastAPI (TCB for policy), PostgreSQL (data; role isolation is 5.5 residual), future worker (separate identity). Arrows: note read, future export. Star every arrow that can change a 1.1 invariant. Place the 1.2 tenant check **on** the API boundary, not “inside the VPC.”

Shostack: What are we working on? What can go wrong? What will we do? Did we do a good job?

## Practice

One page diagram + inventory of entry points. Mark email/IdP as transitive even if unused this week.

## Transfer

Queue between API and worker: new boundary, new identity, new blast radius.
