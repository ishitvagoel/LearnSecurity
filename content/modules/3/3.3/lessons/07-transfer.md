# 3.3-LO-07 — Transfer: serverless admin string and clinic replica

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-8.4.1`; Saltzer and Schroeder (1975, seminal) least privilege. CISA Secure by Design remains **unverified** in this pin set.

## Change the plane; keep two mediations

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Serverless function with a shared `admin` connection string.

**Product sketch:** Clinic billing replica that should see invoice rows, not chart text.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (stolen function secret; forgotten handler filter; replica user with `SELECT` on notes — not a live clinic);
2. trust assumptions (which role is TCB; the cloud vendor IAM name is not);
3. forbidden outcome (`admin` can read tA notes, or billing replica can read chart text — pick one);
4. a test idea on a **local** fixture only;
5. residual (IAM admin still exists; RLS owner bypass);
6. WCAG 2.2 only if a human-mediated control is in the claim (role design itself is not a WCAG problem).

## Mental model: a new compute shape is still a role

```mermaid
flowchart LR
  Fn["Lambda or Cloud Function"] --> Secret["DATABASE_URL"]
  Secret --> Role{admin or app?}
  Role -->|admin| All[All tenants readable]
  Role -->|app plus tenant| Bound[Second mediation]
```

Microservices and serverless do not add a tenant predicate by existing.

## What graders reject

| Reject | Why |
|---|---|
| “Private subnet” as the property | Topology ≠ isolation |
| Live clinic or real RDS | Lab policy |
| RLS ticket without a test | Mechanism theater |

## Practice

One page. No keys. `labs/3.3/3.3-lab` is the only running system you may break.
